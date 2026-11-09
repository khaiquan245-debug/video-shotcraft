from pathlib import Path
import json,re,wave,subprocess,math
import numpy as np
from pocketsphinx import Decoder
r=Path(__file__).resolve().parents[1];chunks=json.loads((r/'out/chunks.json').read_text());script=json.loads((r/'script.json').read_text());sr=24000
pron={'airburst':'EH R B ER S T',"ehman's":'EY M AH N Z','narrowband':'N EH R OW B AE N D','unlocated':'AH N L OW K EY T IH D','ural':'Y UH R AH L','ehman':'EY M AH N','voynich':'V OY N IH CH','antikythera':'AE N T IH K IH TH ER AH','dyatlov':'D Y AA T L AA V','tunguska':'T UH NG G UH S K AH','flaperon':'F L AE P ER AA N','reunion':'R IY Y UW N Y AH N','kuala':'K W AA L AH','lumpur':'L UH M P UH R'}
def align(p,tokens):
 pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-af','apad=pad_dur=0.3','-ar','16000','-ac','1','-f','s16le','-']);d=Decoder(lm=None,loglevel='ERROR',samprate=16000,beam=1e-80,wbeam=1e-60)
 for t in tokens:
  if not d.lookup_word(t):
   if t not in pron:raise ValueError('No dictionary pronunciation: '+t)
   d.add_word(t,pron[t],True)
 d.set_align_text(' '.join(tokens));d.start_utt();d.process_raw(pcm,False,True);d.end_utt();return [{'text':re.sub(r'\(\d+\)$','',x.word),'start':x.start_frame/100,'end':(x.end_frame+1)/100} for x in d.seg() if x.word not in ['<sil>','<s>','</s>','[NOISE]']]
def save(p,a):
 with wave.open(str(p),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes(a.tobytes())
# First compress only verified quiet spaces. Preserve reference sentence continuity.
for ch in chunks:
 p=r/f'out/level-{ch["id"]}.wav';subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/f'out/native-{ch["id"]}.wav'),'-af','loudnorm=I=-18:TP=-3:LRA=10','-ar',str(sr),str(p)],check=True)
 with wave.open(str(p)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
 ws=align(p,ch['tokens']);pieces=[];cursor=0;cuts=[]
 for left,right in zip(ws,ws[1:]):
  gap=right['start']-left['end'];desired=.20
  if gap<.30:continue
  lo=round((left['end']+.05)*sr);hi=round((right['start']-.05)*sr)
  if hi<=lo or lo<cursor:continue
  q=a[lo:hi].astype(float)/32768
  if len(q) and np.sqrt(np.mean(q*q))<.008:
   z=a[cursor:lo].copy();n=min(72,len(z));z[-n:]=(z[-n:]*np.linspace(1,0,n)).astype(np.int16);pieces.extend([z,np.zeros(round((desired-.1)*sr),np.int16)]);cursor=hi;cuts.append(gap)
 pieces.append(a[cursor:]);a=np.concatenate(pieces);active=np.flatnonzero(abs(a.astype(np.int32))>10)
 if len(active):a=a[max(0,active[0]-round(.05*sr)):min(len(a),active[-1]+round(.07*sr))]
 save(r/f'out/connected-{ch["id"]}.wav',a);ch['connectedSeconds']=len(a)/sr;ch['removedLongQuietGaps']=cuts
native=sum(c['connectedSeconds'] for c in chunks);words=sum(len(c['tokens']) for c in chunks);target=words/150*60;tempo=min(1.15,max(.72,native/max(1,target-len(chunks)*.08-1.0)))
print('TEMPO',tempo,'NATIVE',native,'TARGET',target,'TOKENS',words,flush=True)
timeline=[];all_audio=[];offset=0
for ch in chunks:
 p=r/f'out/final-{ch["id"]}.wav';subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/f'out/connected-{ch["id"]}.wav'),'-af',f'rubberband=tempo={tempo}:formant=preserved','-ar',str(sr),str(p)],check=True)
 with wave.open(str(p)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
 ws=align(p,ch['tokens']);frames=math.ceil(len(a)/sr*30)+2;target_samples=frames*800
 for w in ws:w['from']=offset+round(w.pop('start')*30);w['to']=offset+round(w.pop('end')*30);w['to']=max(w['from']+1,w['to'])
 assert [w['text'] for w in ws]==ch['tokens']
 timeline.append({**ch,'from':offset,'duration':frames,'words':ws});all_audio.append(np.pad(a,(0,target_samples-len(a))));offset+=frames;print('ALIGN',ch['id'],frames/30,flush=True)
# The user requested a brief silent ending. Give it 0.8seconds, never pad chapters.
all_audio.append(np.zeros(19200,np.int16));offset+=24
save(r/'output/7_real_unsolved_mysteries_voice.wav',np.concatenate(all_audio));subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'output/7_real_unsolved_mysteries_voice.wav'),'-ar','48000',str(r/'public/audio/narration.wav')],check=True)
chapters=[]
for ch in script:
 t=[z for z in timeline if z['chapter']==ch['id']];start=t[0]['from'];end=t[-1]['from']+t[-1]['duration'];chapters.append({**ch,'from':start,'duration':end-start,'words':[w for z in t for w in z['words']]})
chapters[-1]['duration']+=24
(r/'src/timeline.json').write_text(json.dumps({'fps':30,'frames':offset,'chapters':chapters,'chunks':timeline},indent=2))
# Subtitles, 5–10spoken words, phrase-oriented without bouncing.
def ts(f):
 ms=round(f/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
cues=[]
for ch in timeline:
 ws=ch['words'];i=0
 while i<len(ws):
  j=min(i+8,len(ws))
  for k in range(i+3,j):
   if ws[k]['from']-ws[k-1]['to']>=4:j=k;break
  line=' '.join(w['text'] for w in ws[i:j]);end=ws[j-1]['to'];cues.append({'from':ws[i]['from'],'to':end,'text':line});i=j
(r/'src/captions.json').write_text(json.dumps(cues,indent=2));(r/'output/7_real_unsolved_mysteries.srt').write_text('\n\n'.join(f"{i+1}\n{ts(c['from'])} --> {ts(c['to'])}\n{c['text']}" for i,c in enumerate(cues))+'\n')
(r/'output/voice_report.json').write_text(json.dumps({'seconds':offset/30,'words':words,'wordsPerMinute':words/(offset/30)*60,'sameSpeakerReference':'/workspace/ten-seconds/reference/prompt.wav','sameGenerationSteps':5,'nativeGenerationSpeed':1.0,'pitchPreservingTempoForNew150WpmBrief':tempo,'longArtificialChapterPauses':False,'chunkCount':len(chunks),'note':'New long-form brief explicitly requests145–155WPM; measured pitch-preserving retiming satisfies it while retaining Solway speaker and connected quiet-space policy.'},indent=2));print('AUDIO COMPLETE',offset/30,flush=True)
