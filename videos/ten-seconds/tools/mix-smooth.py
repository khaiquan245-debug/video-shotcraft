from pathlib import Path
import subprocess,json,re,wave
import numpy as np
root=Path(__file__).resolve().parents[1];scenes=json.loads((root/'src/timeline.json').read_text());totalFrames=sum(s['duration'] for s in scenes);seconds=totalFrames/30;sr=48000
# Normalize level only; never stretch or squeeze the speech timing.
analysis=subprocess.run(['ffmpeg','-hide_banner','-i',str(root/'out/narration-raw.wav'),'-af','loudnorm=I=-18:TP=-2:LRA=11:print_format=json','-f','null','-'],capture_output=True,text=True,check=True).stderr
measure=json.JSONDecoder().raw_decode(analysis[analysis.rfind('{'):])[0];(root/'out/qa/loudness.json').write_text(json.dumps(measure,indent=2))
filt=f'loudnorm=I=-18:TP=-2:LRA=11:measured_I={measure["input_i"]}:measured_TP={measure["input_tp"]}:measured_LRA={measure["input_lra"]}:measured_thresh={measure["input_thresh"]}:offset={measure["target_offset"]}:linear=true'
subprocess.run(['ffmpeg','-v','error','-y','-i',str(root/'out/narration-raw.wav'),'-af',filt,'-ar',str(sr),str(root/'out/narration-leveled.wav')],check=True)
with wave.open(str(root/'out/narration-leveled.wav')) as w:voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
N=round(seconds*sr);voice=np.pad(voice[:N],(0,max(0,N-len(voice))));score=np.zeros(N,np.float32);clock=np.zeros(N,np.float32)
chords=[[146.83,174.61,220],[130.81,164.81,196],[116.54,146.83,174.61],[130.81,164.81,196]]
for onset in np.arange(0,seconds,3.75):
 chapter=next((s['id'] for s in reversed(scenes) if onset>=s['from']/30),0)
 for j,freq in enumerate(chords[int(onset/7.5)%4]):
  off=onset+j*.28;n=min(round(5*sr),N-round(off*sr))
  if n<=0:continue
  t=np.arange(n)/sr;emotional=chapter>=8;freq*=2 if emotional else 1;env=(1-np.exp(-t*22))*np.exp(-t*(1.15 if emotional else .65))
  a=(np.sin(2*np.pi*freq*t)+.22*np.sin(2*np.pi*freq*2.002*t)+.08*np.sin(2*np.pi*freq*3*t))*env
  score[round(off*sr):round(off*sr)+n]+=a.astype(np.float32)*(.013 if emotional else .007)
for off in list(range(10))+[seconds-6+i for i in range(6)]:
 idx=round(off*sr);n=min(round(.08*sr),N-idx)
 if n<=0 or idx<0:continue
 t=np.arange(n)/sr;clock[idx:idx+n]+=(np.sin(2*np.pi*1100*t)+.3*np.sin(2*np.pi*1650*t))*np.exp(-t*65)*.024
fade=np.minimum(1,np.arange(N)/(sr*2))*np.minimum(1,(N-np.arange(N))/(sr*2));score*=fade;clock*=fade
for name,a in [('narration',voice+clock),('score',score),('clock',clock),('master',voice+clock+score)]:
 peak=float(np.max(np.abs(a)));assert peak<1,(name,peak)
 raw=root/f'out/{name}-final.wav'
 with wave.open(str(raw),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((a*32767).astype(np.int16).tobytes())
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-c:a','flac',str(root/f'public/audio/{name}.flac')],check=True)
print('MIX COMPLETE seconds',seconds,'frames',totalFrames,flush=True)
