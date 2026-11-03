from pathlib import Path
import json,re,wave,subprocess,time,math,difflib,hashlib,os
import numpy as np,sherpa_onnx
root=Path(__file__).resolve().parents[1];sr=24000
m=Path(os.environ.get('WHISPER_MODEL_DIR',str(root/'tools/sherpa-onnx-whisper-tiny.en')))
r=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=str(m/'tiny.en-encoder.int8.onnx'),decoder=str(m/'tiny.en-decoder.int8.onnx'),tokens=str(m/'tiny.en-tokens.txt'),num_threads=1,language='en',enable_segment_timestamps=True)
word_re=re.compile(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)?")
def norm(w):return w.lower().replace('’',"'").replace('10','ten')
def read(path):
 with wave.open(str(path)) as w:return np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768,w.getframerate()
def write(path,a,rate):
 with wave.open(str(path),'wb') as w:w.setparams((1,2,rate,0,'NONE','not compressed'));w.writeframes((np.clip(a,-.99,.99)*32767).astype(np.int16).tobytes())
def recognize(a,rate,cache):
 audio_hash=hashlib.sha256(a.tobytes()+str(rate).encode()).hexdigest()
 if cache.exists():
  cached=json.loads(cache.read_text())
  if isinstance(cached,dict) and cached.get('audioHash')==audio_hash and cached.get('windowSeconds')==15:return cached['words']
 words=[]
 for offset in range(0,len(a),15*rate):
  x=a[offset:offset+15*rate];stream=r.create_stream();stream.accept_waveform(rate,x);r.decode_stream(stream);data=json.loads(str(stream.result))
  texts=data.get('segment_texts') or [data['text']];starts=data.get('segment_timestamps') or [0.];durations=data.get('segment_durations') or [len(x)/rate]
  for text,start,duration in zip(texts,starts,durations):
   tokens=word_re.findall(text);weights=[max(2,len(w)) for w in tokens];total=max(1,sum(weights));pos=0
   for w,weight in zip(tokens,weights):
    words.append({'word':w,'start':offset/rate+start+duration*pos/total,'end':offset/rate+start+duration*(pos+weight)/total});pos+=weight
 cache.write_text(json.dumps({'audioHash':audio_hash,'windowSeconds':15,'words':words}));return words
def captions(text,recognized,offset):
 matches=list(word_re.finditer(text));source=[norm(x[0]) for x in matches];target=[norm(x['word']) for x in recognized]
 matcher=difflib.SequenceMatcher(None,source,target,autojunk=False);ratio=matcher.ratio();times=np.full(len(source),np.nan);ends=np.full(len(source),np.nan)
 for block in matcher.get_matching_blocks():
  for k in range(block.size):times[block.a+k]=recognized[block.b+k]['start'];ends[block.a+k]=recognized[block.b+k]['end']
 known=np.where(np.isfinite(times))[0]
 if len(known)==0:raise RuntimeError('No speech alignment matches')
 for values in [times,ends]:
  values[:]=np.interp(np.arange(len(source)),known,values[known]);values[:]=np.maximum.accumulate(values)
 n=max(1,math.ceil(len(text)/74));N=len(matches);result=[]
 for i in range(n):
  lo=round(i*N/n);hi=round((i+1)*N/n)
  start=0 if lo==0 else matches[lo].start();finish=matches[hi].start() if hi<N else len(text)
  f=round((offset+times[lo])*30);end=round((offset+ends[hi-1]+.10)*30)
  result.append({'text':text[start:finish].strip(),'from':f,'duration':max(1,end-f)})
 return result,ratio
scenes=[];full=[];globalframe=0;quality=[]
for i in range(12):
 while True:
  try:data=json.loads((root/'out/smooth-voice-manifest.json').read_text());sc=data[i];break
  except (FileNotFoundError,json.JSONDecodeError,IndexError):time.sleep(1)
 lead=.45 if i==0 else .20;gap=.18 if i<8 else .24;parts=[np.zeros(round(lead*sr),np.float32)];pos=lead;caps=[]
 for j,p in enumerate(sc['paragraphs']):
  a,rate=read(root/p['path']);assert rate==sr
  recog=recognize(a,rate,root/f'out/asr-{i:02}-{j:02}.json')
  last=max(x['end'] for x in recog);factor=min(1,(len(a)/rate)/max(last,.001))
  if factor<1:
   recog=[{**x,'start':x['start']*factor,'end':x['end']*factor} for x in recog]
  c,ratio=captions(p['text'],recog,pos);caps.extend(c);quality.append({'chapter':i+1,'paragraph':j+1,'wordSimilarity':ratio,'duration':len(a)/sr})
  if ratio<.65:raise RuntimeError(f'Speech coverage too low in chapter{i+1}: {ratio}')
  parts.extend([a,np.zeros(round(gap*sr),np.float32)]);pos+=len(a)/sr+gap
 tail=2.0 if i==11 else .35;parts.append(np.zeros(round(tail*sr),np.float32));audio=np.concatenate(parts);duration=math.ceil(len(audio)/(sr/30));audio=np.pad(audio,(0,round(duration*sr/30)-len(audio)))
 for a,b in zip(caps,caps[1:]):a['duration']=min(a['duration'],b['from']-a['from'])
 for c in caps:
  c['duration']=min(c['duration'],duration-c['from'])
  assert c['from']>=0 and c['duration']>0 and c['from']+c['duration']<=duration,(i,c,duration)
 scenes.append({'id':i,'title':sc['title'],'label':sc['label'],'from':globalframe,'duration':duration,'text':sc['text'],'originalText':sc['originalText'],'captions':caps,'speechRate':1.0,'cadence':'continuous-paragraphs'})
 full.append(audio);globalframe+=duration;print('ALIGNED',i+1,'chapter seconds',round(duration/30,2),'min similarity',round(min(x['wordSimilarity'] for x in quality if x['chapter']==i+1),3),flush=True)
 (root/'out/alignment-progress.json').write_text(json.dumps(quality,indent=2))
voice=np.concatenate(full);write(root/'out/narration-raw.wav',voice,sr)
(root/'src/timeline.json').write_text(json.dumps(scenes,indent=2));(root/'out/qa/narration-alignment.json').write_text(json.dumps({'speed':1.0,'noFixedDuration':True,'totalFrames':globalframe,'seconds':globalframe/30,'paragraphs':quality},indent=2))
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
lines=[]
for sc in scenes:
 for c in sc['captions']:
  t=(sc['from']+c['from'])/30;lines.append(f'{len(lines)+1}\n{stamp(t)} --> {stamp(t+c["duration"]/30)}\n{c["text"]}\n')
(root/'out/ten-seconds-smooth.en.srt').write_text('\n'.join(lines));print('ALIGNMENT COMPLETE',globalframe,globalframe/30,flush=True)
