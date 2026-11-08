from pathlib import Path
import json,re,wave,subprocess
import numpy as np
from pocketsphinx import Decoder
r=Path(__file__).resolve().parents[1];s=json.loads((r/'src/timeline.json').read_text());offset=0;full=[];silence=None
for x in s:
 i=x['id'];origin=x['from'];ws=x['words'];breaks=[];tokens=[]
 for m in re.finditer(r"([A-Za-z]+(?:'[A-Za-z]+)?|[0-9]+)([^A-Za-z0-9]*)",x['text']):
  tokens+=['nineteen','sixty','four'] if m[1]=='1964' else [m[1].lower()]
  if any(c in m[2] for c in '.!?'):breaks.append(len(tokens)-1)
 assert tokens==[w['text'] for w in ws],(i,tokens,ws)
 with wave.open(str(r/f'out/voice-{i}.wav')) as w:sr=w.getframerate();a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
 # Edit only quiet spaces; keep the existing voice samples and native speaking rate.
 chunks=[];cursor=0;edits=[]
 for j in range(len(ws)-1):
  end=(ws[j]['to']-origin)/30;start=(ws[j+1]['from']-origin)/30;gap=start-end
  desired=.20 if j in breaks else .10
  if i==5 and ws[j+1]['text']=='mother':desired=.23
  if gap<=max(desired+.035,.16):continue
  left=round((end+.045)*sr);right=round((start-.045)*sr)
  if right<=left or left<cursor:continue
  quiet=a[left:right].astype(np.float64)/32768
  if np.sqrt(np.mean(quiet*quiet))>.008:continue
  chunks.append(a[cursor:left]);chunks.append(np.zeros(round(max(0,desired-.09)*sr),np.int16));edits.append({'between':[ws[j]['text'],ws[j+1]['text']],'oldSeconds':round(gap,3),'newSeconds':desired});cursor=right
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
 if not d.lookup_word('templeton'):d.add_word('templeton','T EH M P AH L T AH N',True)
 d.set_align_text(' '.join(tokens));d.start_utt();d.process_raw(pcm,False,True);d.end_utt()
 words=[{'text':re.sub(r'\(\d+\)$','',z.word),'from':offset+round(z.start_frame*.3),'to':offset+round((z.end_frame+1)*.3)} for z in d.seg() if z.word not in ['<sil>','<s>','</s>','[NOISE]']]
 cursor_frame=offset
 for w in words:
  w['from']=max(w['from'],cursor_frame);w['to']=max(w['to'],w['from']+1);cursor_frame=w['to']
 x.update({'from':offset,'duration':frames,'words':words,'breaks':breaks,'voiceSeconds':len(a)/sr,'tempo':1.0})
 full.append(np.pad(a,(0,target-len(a))));offset+=frames;print('AUDIO',i,len(a)/sr,frames/30,flush=True)
(r/'src/timeline.json').write_text(json.dumps(s,indent=2))
with wave.open(str(r/'output/solway_spaceman_voice.wav'),'wb') as w:w.setparams((1,2,24000,0,'NONE','not compressed'));w.writeframes(np.concatenate(full).tobytes())
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'output/solway_spaceman_voice.wav'),'-ar','48000',str(r/'public/audio/narration.wav')],check=True)
sr=48000;N=offset*1600;t=np.arange(N)/sr;rng=np.random.default_rng(2013)
with wave.open(str(r/'public/audio/narration.wav')) as w:voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
music=(np.sin(2*np.pi*49*t)+.35*np.sin(2*np.pi*73.4*t)+.18*np.sin(2*np.pi*98.1*t))*.012
music*=np.minimum(1,t/2)*np.minimum(1,(N/sr-t)/1.2)*np.where(t<s[4]['from']/30,1,.45)
fx=rng.normal(0,.0009,N)
def add(at,a):
 j=round(at*sr);n=min(len(a),N-j)
 if n>0:fx[j:j+n]+=a[:n]
for sc in s:
 at=sc['from']/30;tt=np.arange(sr)/sr
 add(at,np.sin(2*np.pi*(62-25*tt)*tt)*.045*np.exp(-tt*8))
 if sc['id'] in [0,1,2]:
  when=.27 if sc['id']==0 else at+sc['duration']/30*.82
  z=np.arange(round(.16*sr))/sr;click=rng.normal(0,.04,len(z))*np.exp(-z*40)+np.sin(2*np.pi*250*z)*.018*np.exp(-z*22);add(when,click)
 if sc['id']==1:
  z=np.arange(3*sr)/sr;add(at,rng.normal(0,.002,len(z))*(.5+.5*np.sin(z*2)))
 if sc['id'] in [2,3]:
  for k in range(3):
   z=np.arange(round(.35*sr))/sr;add(at+.6+k*.75,rng.normal(0,.008,len(z))*np.sin(np.pi*z/.35)**2)
 if sc['id']==3:
  for k in range(min(9,int(sc['duration']/30))):add(at+k,np.sin(2*np.pi*850*tt)*.007*np.exp(-tt*80))
 if sc['id']==4:
  z=np.arange(sr)/sr;add(at+.15,(np.sin(2*np.pi*660*z)+np.sin(2*np.pi*990*z))*.016*np.exp(-z*5))
 if sc['id']==5:
  mother=next(w['from']/30 for w in sc['words'] if w['text']=='mother');add(mother,np.sin(2*np.pi*55*tt)*.055*np.exp(-tt*10))
# Keep the narration unchanged; clear only background immediately before the tentative reveal.
silence=(mother-.22,mother);lo,hi=round(silence[0]*sr),round(silence[1]*sr);music[lo:hi]=0;fx[lo:hi]=0
# Smooth automatic narration-driven BGM ducking (50ms detector,100ms smoothing).
def smooth(a,n):
 c=np.concatenate(([0.0],np.cumsum(a)));v=(c[n:]-c[:-n])/n;return np.pad(v,(n//2,len(a)-len(v)-n//2),mode='edge')
activity=smooth(np.abs(voice),2400);gain=smooth(1-.5*np.clip(activity/.025,0,1),4800);music*=gain
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
(r/'output/solway_spaceman_subtitles.srt').write_text('\n'.join(cues));(r/'output/audio-cues.json').write_text(json.dumps({'backgroundDipBeforeMother':silence,'seconds':offset/30},indent=2));print('AUDIO READY',offset/30,silence)
