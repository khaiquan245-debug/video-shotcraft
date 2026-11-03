from pathlib import Path
import json,wave,subprocess
import numpy as np
root=Path(__file__).resolve().parents[1]; sr=48000
scenes=json.loads((root/'src/timeline.json').read_text())
voice=np.zeros(480*sr,np.float32)
for sc in scenes:
 for c in sc['captions']:
  if sc['id']==11:c['text']=c['text'].replace('Black screen. Text appears: ', '').replace(' Then: ', ' ')
 parts=[]
 for j,c in enumerate(sc['captions']):
  src=root/f'public/audio/raw-{sc["id"]}-{j}.wav'
  with wave.open(str(src)) as w: a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768; native_sr=w.getframerate()
  parts.append(a)
 target=sc['duration']/30; speech=sum(len(a)/native_sr for a in parts);rate=max(.97,speech/(target-1.8-.12*len(parts)))
 gap=max(.12,(target-1.5-speech/rate)/len(parts));timeline=[];audio=[np.zeros(round(.6*sr),np.float32)];pos=.6
 for j,(a,c) in enumerate(zip(parts,sc['captions'])):
  src=root/f'public/audio/raw-{sc["id"]}-{j}.wav'
  out=root/'tools/temp.wav'
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(src),'-af',f'atempo={rate}','-ar',str(sr),str(out)],check=True)
  with wave.open(str(out)) as w:b=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
  timeline.append({'text':c['text'],'from':round(pos*30),'duration':round((len(b)/sr+min(gap,.3))*30)})
  audio.extend([b,np.zeros(round(gap*sr),np.float32)]);pos+=len(b)/sr+gap
 chunk=np.concatenate(audio);offset=round(sc['from']/30*sr);length=round(target*sr)
 voice[offset:offset+min(length,len(chunk))]=chunk[:length]
 sc['captions']=timeline;sc['speechRate']=rate
 print(sc['id']+1,'voice speed',round(rate,2),'pause',round(gap,2),flush=True)
# A consistent voice level, gentle original underscore.
voice*=min(1.3,.72/(np.max(np.abs(voice))+1e-9))
score=np.zeros_like(voice)
chords=[[146.83,174.61,220],[130.81,164.81,196],[116.54,146.83,174.61],[130.81,164.81,196]]
for onset in np.arange(0,480,3.75):
 chapter=next((s['id'] for s in reversed(scenes) if onset>=s['from']/30),0)
 notes=chords[int(onset/7.5)%4]
 emotional=chapter>=8
 for j,freq in enumerate(notes):
  off=onset+j*.28;dur=min(5,480-off);n=int(dur*sr)
  if n<=0:continue
  t=np.arange(n)/sr
  if emotional: freq*=2
  env=(1-np.exp(-t*22))*np.exp(-t*(1.15 if emotional else .65))
  tone=(np.sin(2*np.pi*freq*t)+.22*np.sin(2*np.pi*freq*2.002*t)+.08*np.sin(2*np.pi*freq*3*t))*env
  gain=.018 if emotional else .009
  if chapter==9 and 350<onset<370:gain=.004
  idx=int(off*sr);score[idx:idx+n]+=tone.astype(np.float32)*gain
# Fictional countdown motif, deliberately sparse; no sampled sound effects.
for off in list(range(0,10))+list(range(474,480)):
 n=int(.08*sr);t=np.arange(n)/sr
 tick=(np.sin(2*np.pi*1100*t)+.3*np.sin(2*np.pi*1650*t))*np.exp(-t*65)*.028
 idx=off*sr;score[idx:idx+n]+=tick
fade=np.minimum(1,np.arange(len(score))/(sr*3))*np.minimum(1,(len(score)-np.arange(len(score)))/(sr*3))
score*=fade
for name,a in [('narration',voice),('score',score),('master',voice+score)]:
 with wave.open(str(root/f'public/audio/{name}.wav'),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((np.clip(a,-.98,.98)*32767).astype(np.int16).tobytes())
(root/'src/timeline.json').write_text(json.dumps(scenes,indent=2))
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
lines=[]
for sc in scenes:
 for c in sc['captions']:
  start=(sc['from']+c['from'])/30;end=min((sc['from']+sc['duration'])/30,start+c['duration']/30)
  lines.append(f'{len(lines)+1}\n{stamp(start)} --> {stamp(end)}\n{c["text"]}\n')
(root/'out/ten-seconds.en.srt').write_text('\n'.join(lines))
