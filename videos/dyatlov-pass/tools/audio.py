from pathlib import Path
import json,re,wave,subprocess
import numpy as np
from pocketsphinx import Decoder
r=Path(__file__).resolve().parents[1];tempo=.825;s=json.loads((r/'src/timeline.json').read_text());offset=0;full=[];silence=None
for x in s:
 i=x['id'];origin=x['from'];ws=x['words'];breaks=[];tokens=[]
 for m in re.finditer(r"([A-Za-z]+(?:'[A-Za-z]+)?|[0-9]+)([^A-Za-z0-9]*)",x['text']):
  tokens+=['nineteen','fifty','nine'] if m[1]=='1959' else [m[1].lower()]
  if any(c in m[2] for c in '.!?'):breaks.append(len(tokens)-1)
 assert tokens==[w['text'] for w in ws],(i,tokens,ws)
 source=r/f'out/voice-{i}.wav';paced=r/f'out/paced-{i}.wav'
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(source),'-af',f'rubberband=tempo={tempo}:formant=preserved','-ar','24000',str(paced)],check=True)
 with wave.open(str(paced)) as w:sr=w.getframerate();a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
 # Edit only quiet spaces; keep the existing voice samples and native speaking rate.
 chunks=[];cursor=0;edits=[]
 for j in range(len(ws)-1):
  end=(ws[j]['to']-origin)/30/tempo;start=(ws[j+1]['from']-origin)/30/tempo;gap=start-end
  desired=.33 if j in breaks else .12
  if j in breaks and x['text'].find('...')>=0:desired=.36
  if j in breaks and .04<gap<desired:
   point=round((end+start)/2*sr);region=a[max(0,point-240):min(len(a),point+240)].astype(np.float64)/32768
   if len(region) and np.sqrt(np.mean(region*region))<.02:
    piece=a[cursor:point].copy();chunks.append(piece);chunks.append(np.zeros(round((desired-gap)*sr),np.int16));cursor=point;continue
  if gap<=max(desired+.035,.17):continue
  left=round((end+.045)*sr);right=round((start-.045)*sr)
  if right<=left or left<cursor:continue
  quiet=a[left:right].astype(np.float64)/32768
  if np.sqrt(np.mean(quiet*quiet))>.008:continue
  piece=a[cursor:left].copy();n=min(72,len(piece));piece[-n:]=(piece[-n:]*np.linspace(1,0,n)).astype(np.int16)
  chunks.append(piece);chunks.append(np.zeros(round(max(0,desired-.09)*sr),np.int16));edits.append({'between':[ws[j]['text'],ws[j+1]['text']],'oldSeconds':round(gap,3),'newSeconds':desired});cursor=right
 chunks.append(a[cursor:]);a=np.concatenate(chunks)
 # Remove recording-only leading/trailing silence with a low threshold and protective margins.
 energy=np.abs(a.astype(np.int32));active=np.flatnonzero(energy>8)
 if len(active):
  lo=max(0,int(active[0]) - round(.06*sr));hi=min(len(a),int(active[-1])+round(.08*sr));a=a[lo:hi]
 frames=int(np.ceil(len(a)/sr*30))+(12 if i==5 else 3);target=frames*800
 x['quietGapEdits']=edits
 # Realign the resulting narration so animation and captions follow the edited pauses.
 final=r/f'out/final-{i}.wav'
 with wave.open(str(final),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes(a.tobytes())
 pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(final),'-ar','16000','-ac','1','-f','s16le','-'])
 d=Decoder(lm=None,loglevel='ERROR',samprate=16000,beam=1e-80,wbeam=1e-60)
 if not d.lookup_word('ural'):d.add_word('ural','Y UH R AH L',True)
 d.set_align_text(' '.join(tokens));d.start_utt();d.process_raw(pcm,False,True);d.end_utt()
 words=[{'text':re.sub(r'\(\d+\)$','',z.word),'from':offset+round(z.start_frame*.3),'to':offset+round((z.end_frame+1)*.3)} for z in d.seg() if z.word not in ['<sil>','<s>','</s>','[NOISE]']]
 cursor_frame=offset
 for w in words:
  w['from']=max(w['from'],cursor_frame);w['to']=max(w['to'],w['from']+1);cursor_frame=w['to']
 x.update({'from':offset,'duration':frames,'words':words,'breaks':breaks,'voiceSeconds':len(a)/sr,'tempo':tempo})
 full.append(np.pad(a,(0,target-len(a))));offset+=frames;print('AUDIO',i,len(a)/sr,frames/30,flush=True)
(r/'src/timeline.json').write_text(json.dumps(s,indent=2))
with wave.open(str(r/'output/dyatlov_pass_voice.wav'),'wb') as w:w.setparams((1,2,24000,0,'NONE','not compressed'));w.writeframes(np.concatenate(full).tobytes())
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'output/dyatlov_pass_voice.wav'),'-ar','48000',str(r/'public/audio/narration.wav')],check=True)
sr=48000;N=offset*1600;t=np.arange(N)/sr;rng=np.random.default_rng(2013)
with wave.open(str(r/'public/audio/narration.wav')) as w:voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
# Original cold-wind / tent / snow Foley, no recorded third-party assets.
fx=rng.normal(0,.0013,N);music=(np.sin(2*np.pi*41.2*t)+.25*np.sin(2*np.pi*61.74*t))*.008
music*=np.minimum(1,t/1.5)*np.minimum(1,(N/sr-t)/1.2)
def add(at,a):
 j=round(at*sr);n=min(len(a),N-j)
 if n>0:fx[j:j+n]+=a[:n]
for sc in s:
 at=sc['from']/30;tt=np.arange(sr)/sr
 add(at,np.sin(2*np.pi*(56-18*tt)*tt)*.05*np.exp(-tt*9))
 if sc['id'] in [0,1]:
  z=np.arange(round(.13*sr))/sr;when=.2 if sc['id']==0 else next(w['to']/30 for w in sc['words'] if w['text']=='photographed');add(when,rng.normal(0,.035,len(z))*np.exp(-z*38))
 if sc['id'] in [1,2,3]:
  for k in range(max(1,int(sc['duration']/30/1.2))):
   z=np.arange(round(.20*sr))/sr;a=rng.normal(0,.009,len(z))*np.sin(np.pi*z/.2)**2;add(at+.4+k*1.2,a)
 if sc['id'] in [2,3]:
  z=np.arange(2*sr)/sr;add(at+.3,np.sin(2*np.pi*(75+2*np.sin(z*4))*z)*.006*np.sin(np.pi*z/2)**2)
 if sc['id']==4:
  for k in range(3):add(at+.2+k*1.4,np.sin(2*np.pi*65*tt)*.018*np.exp(-tt*18))
 if sc['id']==5:
  when=next(w['from']/30 for w in sc['words'] if w['text']=='avalanche');z=np.arange(sr)/sr;add(when,rng.normal(0,.009,len(z))*np.sin(np.pi*z)**2)
silence=(next(w['from']/30 for w in s[5]['words'] if w['text']=='nobody')-.18,next(w['from']/30 for w in s[5]['words'] if w['text']=='nobody'));lo,hi=map(lambda z:round(z*sr),silence);music[lo:hi]=0;fx[lo:hi]=0
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
(r/'output/dyatlov_pass_subtitles.srt').write_text('\n'.join(cues));(r/'output/audio-cues.json').write_text(json.dumps({'backgroundDipBeforeUncertainty':silence,'seconds':offset/30},indent=2));print('AUDIO READY',offset/30,silence)
