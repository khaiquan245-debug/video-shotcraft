from pathlib import Path
import json,re,wave,subprocess
import numpy as np
from pocketsphinx import Decoder
r=Path(__file__).resolve().parents[1];s=json.loads((r/'src/timeline.json').read_text());lengths=[5.2,3.6,10,6.3,7.1,5.5,7.3];offset=0;full=[];silence=None
for x in s:
 i=x['id'];origin=x['from'];ws=x['words'];breaks=[];tokens=[]
 for m in re.finditer(r"([A-Za-z]+(?:'[A-Za-z]+)?|[0-9]+)([^A-Za-z0-9]*)",x['text']):
  tokens+=[m[1].lower()]
  if any(c in m[2] for c in '.!?'):breaks.append(len(tokens)-1)
 assert tokens==[w['text'] for w in ws],(i,tokens,ws)
 with wave.open(str(r/f'out/voice-{i}.wav')) as w:sr=w.getframerate();a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
 chunks=[];cursor=0;insertions=[]
 for j in breaks:
  if j>=len(ws)-1:continue
  start=(ws[j]['to']-origin)/30;end=(ws[j+1]['from']-origin)/30;desired=.36
  if i==6:desired=.38
  if i==4:desired=.36
  if i==0:desired=.34
  extra=max(0,desired-(end-start));point=round((start+end)/2*sr)
  chunks+=[a[cursor:point],np.zeros(round(extra*sr),np.int16)];cursor=point;insertions.append((point/sr,extra))
 chunks.append(a[cursor:]);a=np.concatenate(chunks);target=round(lengths[i]*sr);assert len(a)<=target,(i,len(a)/sr,lengths[i])
 # Realign the resulting narration so animation and captions follow the edited pauses.
 final=r/f'out/final-{i}.wav'
 with wave.open(str(final),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes(a.tobytes())
 pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(final),'-ar','16000','-ac','1','-f','s16le','-'])
 d=Decoder(lm=None,loglevel='ERROR',samprate=16000,beam=1e-80,wbeam=1e-60)
 if not d.lookup_word('octopus'):d.add_word('octopus','AA K T AH P AH S',True)
 d.set_align_text(' '.join(tokens));d.start_utt();d.process_raw(pcm,False,True);d.end_utt()
 words=[{'text':re.sub(r'\(\d+\)$','',z.word),'from':offset+round(z.start_frame*.3),'to':offset+round((z.end_frame+1)*.3)} for z in d.seg() if z.word not in ['<sil>','<s>','</s>','[NOISE]']]
 cursor_frame=offset
 for w in words:
  w['from']=max(w['from'],cursor_frame);w['to']=max(w['to'],w['from']+1);cursor_frame=w['to']
 x.update({'from':offset,'duration':round(lengths[i]*30),'words':words,'breaks':breaks,'voiceSeconds':len(a)/sr,'tempo':1.0})
 full.append(np.pad(a,(0,target-len(a))));offset+=round(lengths[i]*30);print('AUDIO',i,len(a)/sr,lengths[i],flush=True)
(r/'src/timeline.json').write_text(json.dumps(s,indent=2))
with wave.open(str(r/'output/octopus_three_hearts_voice.wav'),'wb') as w:w.setparams((1,2,24000,0,'NONE','not compressed'));w.writeframes(np.concatenate(full).tobytes())
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'output/octopus_three_hearts_voice.wav'),'-ar','48000',str(r/'public/audio/narration.wav')],check=True)
sr=48000;N=offset*1600;t=np.arange(N)/sr;rng=np.random.default_rng(2013)
with wave.open(str(r/'public/audio/narration.wav')) as w:voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
music=(np.sin(2*np.pi*65.406*t)+.4*np.sin(2*np.pi*98*t)+.2*np.sin(2*np.pi*130.81*t))*.009
music*=np.minimum(1,t/2)*np.minimum(1,(N/sr-t)/1.5)*np.where(t<s[5]['from']/30,1,.55)
fx=np.sin(2*np.pi*32*t)*.003+rng.normal(0,.001,N)
def add(at,a):
 j=round(at*sr);n=min(len(a),N-j)
 if n>0:fx[j:j+n]+=a[:n]
for sc in s:
 at=sc['from']/30;tt=np.arange(sr)/sr
 add(at,np.sin(2*np.pi*(62-25*tt)*tt)*.055*np.exp(-tt*8))
 # Bubbles and water drops, procedurally synthesized and deterministic.
 for k in range(sc['duration']//30):
  z=np.arange(round(.15*sr))/sr;add(at+k+.35,np.sin(2*np.pi*(320+1500*z)*z)*.006*np.exp(-z*35))
 if sc['id']==0:
  for k in range(3):add(at+.3+k*.4,np.sin(2*np.pi*72*tt)*.04*np.exp(-tt*17))
  when=next(w['from']/30 for w in sc['words'] if w['text']=='three');add(when,np.sin(2*np.pi*48*tt)*.055*np.exp(-tt*12))
 if sc['id']==1:
  z=np.arange(3*sr)/sr;add(at,rng.normal(0,.012,len(z))*(.6+.4*np.sin(z*3)))
 if sc['id'] in [2,3]:
  z=np.arange(2*sr)/sr;add(at+1,np.sin(2*np.pi*(85+2*np.sin(z*7))*z)*.013*np.exp(-z*2))
 if sc['id']==3:
  for k in range(10):add(at+k,np.sin(2*np.pi*62*tt)*.025*np.exp(-tt*15))
 if sc['id']==4:
  when=next(w['from']/30 for w in sc['words'] if w['text']=='temporarily');add(when,np.sin(2*np.pi*50*tt)*.055*np.exp(-tt*10))
# A brief background dip in all tracks immediately before the living-survivor reveal.
silence=(next(w['from']/30 for w in s[4]['words'] if w['text']=='temporarily')-.15,next(w['from']/30 for w in s[4]['words'] if w['text']=='temporarily'));lo,hi=map(lambda z:round(z*sr),silence);music[lo:hi]=0;fx[lo:hi]=0
# Original quiet, playful plucked notes; no copyrighted composition or recording.
for k in range(int(N/sr/.55)):
 start=round((k*.55)*sr);count=min(round(.32*sr),N-start);z=np.arange(count)/sr;note=[261.626,329.628,391.995,440,391.995,329.628,293.665,391.995][k%8];music[start:start+count]+=(np.sin(2*np.pi*note*z)+.2*np.sin(2*np.pi*note*2*z))*.004*np.exp(-z*12)
music[lo:hi]=0
for name,a in [('master',voice+fx+music),('narration-sfx',voice+fx)]:
 assert np.max(np.abs(a))<.99
 with wave.open(str(r/f'public/audio/{name}.wav'),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((a*32767).astype(np.int16).tobytes())
def ts(f):
 ms=round(f/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
cues=[]
for sc in s:
 i=0
 while i<len(sc['words']):
  end=next(b for b in sc['breaks'] if b>=i);n=min(2,end-i+1);ws=sc['words'][i:i+n];i+=n;cues.append(f"{len(cues)+1}\n{ts(ws[0]['from'])} --> {ts(ws[-1]['to'])}\n"+' '.join(w['text'] for w in ws)+'\n')
(r/'output/octopus_three_hearts_subtitles.srt').write_text('\n'.join(cues));(r/'output/audio-cues.json').write_text(json.dumps({'backgroundDipOnSystemicPause':silence,'seconds':offset/30},indent=2));print('AUDIO READY',offset/30,silence)
