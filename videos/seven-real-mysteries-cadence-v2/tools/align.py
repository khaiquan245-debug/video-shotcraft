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
# Latest user correction supersedes the former 150WPM length target: native reference cadence.
replacements={'1977':'nineteen seventy seven','1912':'nineteen twelve','1901':'nineteen oh one','1959':'nineteen fifty nine','2020':'twenty twenty','2021':'twenty twenty one','1908':'nineteen oh eight','1980':'nineteen eighty','1971':'nineteen seventy one','2016':'twenty sixteen','2014':'twenty fourteen','2015':'twenty fifteen','2017':'twenty seventeen','777':'seven seventy seven','727':'seven twenty seven'}
def spoken(t):
 for k,v in replacements.items():t=re.sub(r'\b'+k+r'\b',v,t)
 return t.replace("'Wow!'",'Wow.').replace('D.B.','D B').replace('Réunion','Reunion').lower()
all_audio=[];offset=0;timeline=[];edits=[]
for number,ch in enumerate(chunks):
 p=r/f'out/level-{ch["id"]}.wav'
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/f'out/native-{ch["id"]}.wav'),'-af','loudnorm=I=-18:TP=-3:LRA=10','-ar',str(sr),str(p)],check=True)
 with wave.open(str(p)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
 ws=align(p,ch['tokens']);matches=list(re.finditer(r"([a-z]+(?:'[a-z]+)?)([^a-z]*)",spoken(ch['text'])));assert [m[1] for m in matches]==ch['tokens']
 pieces=[];cursor=0;local=[]
 for i,(left,right) in enumerate(zip(ws,ws[1:])):
  sep=matches[i][2];sentence=any(z in sep for z in '.!?');clause=any(z in sep for z in ',;:');gap=right['start']-left['end']
  # Sentence breaths vary slightly with clause length. Internal clauses remain connected.
  desired=(.24 if i<12 else .28) if sentence else (.14 if any(z in sep for z in ';:') else .11) if clause else .075
  lo=max(cursor,round((left['end']+.025)*sr));hi=min(len(a),round((right['start']-.025)*sr))
  if hi<=lo:continue
  q=a[lo:hi].astype(float)/32768;quiet=len(q)>=round(.025*sr) and np.sqrt(np.mean(q*q))<.004
  if not quiet:continue
  if gap>desired+.08:
   z=a[cursor:lo].copy();n=min(72,len(z));z[-n:]=(z[-n:]*np.linspace(1,0,n)).astype(np.int16)
   pieces.extend([z,np.zeros(round(max(0,desired-.05)*sr),np.int16)]);cursor=hi
   local.append({'after':left['text'],'before':right['text'],'kind':'sentence' if sentence else 'clause' if clause else 'internal','oldGap':gap,'newGap':desired})
  elif sentence and gap<.18 and hi-lo>round(.03*sr):
   midpoint=(lo+hi)//2;pieces.extend([a[cursor:midpoint],np.zeros(round((desired-gap)*sr),np.int16)]);cursor=midpoint
   local.append({'after':left['text'],'before':right['text'],'kind':'sentence-breath','oldGap':gap,'newGap':desired})
 pieces.append(a[cursor:]);a=np.concatenate(pieces);active=np.flatnonzero(abs(a.astype(np.int32))>10)
 if len(active):a=a[max(0,active[0]-round(.045*sr)):min(len(a),active[-1]+round(.065*sr))]
 p=r/f'out/final-{ch["id"]}.wav';save(p,a);aligned=align(p,ch['tokens']);assert [w['text'] for w in aligned]==ch['tokens']
 chapter_end=number==len(chunks)-1 or chunks[number+1]['chapter']!=ch['chapter'];pad=.22 if chapter_end else .10
 frames=math.ceil((len(a)/sr+pad)*30);target=frames*800
 last=offset
 for w in aligned:
  w['from']=max(last,offset+round(w.pop('start')*30));w['to']=max(w['from']+1,offset+round(w.pop('end')*30));last=w['to']
 assert last<=offset+frames,(ch['id'],last,offset+frames)
 timeline.append({**ch,'from':offset,'duration':frames,'words':aligned,'tempo':1.0,'quietGapEdits':local});edits.extend([{'chunk':ch['id'],**e} for e in local]);all_audio.append(np.pad(a,(0,target-len(a))));offset+=frames;print('NATIVE CADENCE',ch['id'],round(len(a)/sr,3),'edits',len(local),flush=True)
all_audio.append(np.zeros(19200,np.int16));offset+=24;save(r/'output/7_real_unsolved_mysteries_voice.wav',np.concatenate(all_audio));subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'output/7_real_unsolved_mysteries_voice.wav'),'-ar','48000',str(r/'public/audio/narration.wav')],check=True)
chapters=[]
for ch in script:
 t=[z for z in timeline if z['chapter']==ch['id']];start=t[0]['from'];end=t[-1]['from']+t[-1]['duration'];chapters.append({**ch,'from':start,'duration':end-start,'words':[w for z in t for w in z['words']]})
chapters[-1]['duration']+=24;(r/'src/timeline.json').write_text(json.dumps({'fps':30,'frames':offset,'chapters':chapters,'chunks':timeline},indent=2));words=sum(len(c['tokens']) for c in chunks)
(r/'output/voice_report.json').write_text(json.dumps({'seconds':offset/30,'words':words,'wordsPerMinute':words/(offset/30)*60,'sameSpeakerReference':'/workspace/ten-seconds/reference/prompt.wav','sameGenerationSteps':5,'nativeGenerationSpeed':1.0,'tempo':1.0,'pitchShift':False,'timeStretchRemoved':True,'pausePolicy':'Punctuation-aware: short connected internal gaps, clause rests, sentence breaths and distinct chapter pauses. Only acoustic quiet regions edited; native phonemes preserved.','edits':edits,'chunkCount':len(chunks),'note':'Latest user rejected previous rhythm. Native approved Solway cadence takes priority over old150WPM/runtime target.'},indent=2));print('VOICE READY',offset/30,flush=True)
