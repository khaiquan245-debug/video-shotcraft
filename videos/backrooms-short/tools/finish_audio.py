from pathlib import Path
import json,wave,subprocess,re
import numpy as np
r=Path(__file__).resolve().parents[1];s=json.loads((r/'src/timeline.json').read_text());old=sum(x['duration'] for x in s);target=1770;tempo=(old-12)/(target-18);offset=0;full=[]
for x in s:
 i=x['id'];p=r/f'out/voice-{i}.wav';q=r/f'out/final-{i}.wav'
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(p),'-af',f'rubberband=tempo={tempo}:formant=preserved','-ar','24000',str(q)],check=True)
 with wave.open(str(q)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
 dur=round(x['duration']/tempo);dur=max(dur,int(np.ceil(len(a)/800))+3)
 for w in x['words']:w['from']=offset+round((w['from']-x['from'])/tempo);w['to']=offset+round((w['to']-x['from'])/tempo)
 x['from']=offset;x['duration']=dur;offset+=dur;full.append(np.pad(a,(0,dur*800-len(a))))
# Fit remaining tail only; never truncate speech.
assert offset<=1800,(offset,tempo)
if offset<1650:
 extra=1650-offset;s[-1]['duration']+=extra;full[-1]=np.pad(full[-1],(0,extra*800));offset+=extra
(r/'src/timeline.json').write_text(json.dumps(s,indent=2))
with wave.open(str(r/'output/backrooms_voice.wav'),'wb') as w:w.setparams((1,2,24000,0,'NONE','not compressed'));w.writeframes(np.concatenate(full).tobytes())
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'output/backrooms_voice.wav'),'-ar','48000',str(r/'public/audio/narration.wav')],check=True)
sr=48000;N=offset*1600;t=np.arange(N)/sr;rng=np.random.default_rng(2024)
with wave.open(str(r/'public/audio/narration.wav')) as w:voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
reveal=s[4]['from']/30;music=(np.sin(2*np.pi*48*t)+.35*np.sin(2*np.pi*71.8*t)+.2*np.sin(2*np.pi*96.1*t))*.013*(.7+.3*np.sin(t*.3)**2);music*=np.where(t<reveal,1,.25)*np.minimum(1,t/2)*np.minimum(1,(N/sr-t)/1.4)
fx=np.sin(2*np.pi*120*t)*.003+rng.normal(0,.0008,N)
def add(when,a):
 i=round(when*sr);n=min(len(a),N-i)
 if n>0:fx[i:i+n]+=a[:n]
for j,sc in enumerate(s):
 at=sc['from']/30;tt=np.arange(sr)/sr
 add(at,np.sin(2*np.pi*(65-25*tt)*tt)*np.exp(-tt*8)*.07)
 if j in [1,3]:
  for k in range(14):
   z=np.arange(1800)/sr;add(at+.5+k*.21,rng.normal(0,.025,len(z))*np.exp(-z*100))
 if j==2:
  add(at,rng.normal(0,.028,sr)*np.linspace(0,1,sr)*np.exp(-tt*2))
  for k in range(5):add(at+1+k*.8,np.sin(2*np.pi*70*tt)*np.exp(-tt*20)*.05)
 if j==4:add(at+.1,(np.sin(2*np.pi*660*tt)+np.sin(2*np.pi*990*tt))*.027*np.exp(-tt*5))
 if j==5:add(at+.1,rng.normal(0,.035,sr)*np.exp(-tt*17)*np.sin(tt*110))
for name,a in [('master',voice+fx+music),('narration-sfx',voice+fx)]:
 assert np.max(np.abs(a))<.99
 with wave.open(str(r/f'public/audio/{name}.wav'),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((a*32767).astype(np.int16).tobytes())
def ts(f):
 ms=round(f/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
cues=[]
for sc in s:
 for i in range(0,len(sc['words']),3):
  ws=sc['words'][i:i+3];cues.append(f"{len(cues)+1}\n{ts(ws[0]['from'])} --> {ts(ws[-1]['to'])}\n"+' '.join(w['text'] for w in ws)+'\n')
(r/'output/backrooms_subtitles.srt').write_text('\n'.join(cues));print('FINAL AUDIO',offset,offset/30,'tempo',tempo)
