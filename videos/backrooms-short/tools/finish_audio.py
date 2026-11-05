from pathlib import Path
import json,wave,subprocess,re
import numpy as np
r=Path(__file__).resolve().parents[1];s=json.loads((r/'src/timeline.json').read_text());offset=0;full=[];tempo=1.02
for x in s:
 i=x['id'];p=r/f'out/voice-{i}.wav';q=r/f'out/phrased-{i}.wav'
 with wave.open(str(p)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy();sr=w.getframerate()
 # Keep voiced edges intact and normalize only alignment-confirmed quiet gaps.
 chunks=[];cursor=0;boundaries={};tokens=[]
 for match in re.finditer(r"([A-Za-z]+(?:'[A-Za-z]+)?|[0-9]+)([^A-Za-z0-9]*)",x['text']):
  token=match[1].lower();expanded={'2019':['twenty','nineteen'],'2024':['twenty','twenty','four'],'2003':['two','thousand','three']}.get(token,[token]);tokens.extend(expanded)
  if any(c in match[2] for c in '.!?'):boundaries[len(tokens)-1]=.32 if '...' in match[2] else .24
 ws=x['words'];origin=x['from'];changes=[]
 for j in range(len(ws)-1):
  end=(ws[j]['to']-origin)/30;start=(ws[j+1]['from']-origin)/30
  gap=start-end;desired=boundaries.get(j,min(gap,.11))
  if gap>.14 and abs(gap-desired)>.035:
   left=round((end+.045)*sr);right=round((start-.045)*sr)
   if right>left:
    chunks.append(a[cursor:left]);replacement=np.zeros(round(max(0,desired-.09)*sr),np.int16);chunks.append(replacement);changes.append((right/sr,(len(replacement)-(right-left))/sr));cursor=right
 chunks.append(a[cursor:]);a=np.concatenate(chunks)
 with wave.open(str(q),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes(a.tobytes())
 final=r/f'out/final-{i}.wav';subprocess.run(['ffmpeg','-v','error','-y','-i',str(q),'-af',f'rubberband=tempo={tempo}:formant=preserved','-ar','24000',str(final)],check=True)
 with wave.open(str(final)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
 dur=int(np.ceil(len(a)/800))+ (16 if i==5 else 4)
 for w in ws:
  for key in ['from','to']:
   old=(w[key]-origin)/30;new=old+sum(delta for when,delta in changes if when<=old+.001);w[key]=offset+round(new/tempo*30)
 x['from']=offset;x['duration']=dur;x['tempo']=tempo;offset+=dur;full.append(np.pad(a,(0,dur*800-len(a))))
assert 1050<offset<1650,offset
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
