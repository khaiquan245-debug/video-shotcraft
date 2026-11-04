from pathlib import Path
import subprocess,json,time,wave,re,math,hashlib
import numpy as np
from pocketsphinx import Decoder
import sherpa_onnx,difflib
r=Path(__file__).resolve().parents[1];o=r/'out';sr=24000
while 'VOICE GENERATION COMPLETE' not in (o/'voice.log').read_text():time.sleep(3)
m=json.loads((o/'smooth-voice-manifest.json').read_text());native=sum(p['seconds'] for s in m for p in s['paragraphs']);target=1610/170*60;tempo=native/target
assert .7<tempo<1.3,tempo
norm=lambda t:re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",t.lower().replace('’',"'"))
def read(p):
 with wave.open(str(p)) as w:return np.frombuffer(w.readframes(w.getnframes()),np.int16).copy(),w.getframerate()
def write(p,a):
 with wave.open(str(p),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes(a.astype(np.int16).tobytes())
dec=Decoder(lm=None,loglevel='ERROR',samprate=16000,beam=1e-80,wbeam=1e-60)
wh=Path('/workspace/ten-seconds/tools/sherpa-onnx-whisper-tiny.en')
asr=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=str(wh/'tiny.en-encoder.int8.onnx'),decoder=str(wh/'tiny.en-decoder.int8.onnx'),tokens=str(wh/'tiny.en-tokens.txt'),num_threads=1,language='en')
scenes=[];full=[];frame=0;report=[]
for s in m:
 parts=[np.zeros(round(.35*sr),np.int16)];pos=.35;words=[]
 for j,p in enumerate(s['paragraphs']):
  old=r/p['path'];new=o/f'voice-{s["id"]:02}-{j:02}.wav'
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(old),'-af',f'rubberband=tempo={tempo}:transients=smooth:formant=preserved','-ar',str(sr),str(new)],check=True)
  a,rate=read(new);assert rate==sr
  pcm=subprocess.run(['ffmpeg','-v','error','-i',str(new),'-ar','16000','-ac','1','-f','s16le','-'],capture_output=True,check=True).stdout
  expected=norm(p['text']);unknown=[w for w in expected if not dec.lookup_word(w)];assert not unknown,unknown
  dec.set_align_text(' '.join(expected));dec.start_utt();dec.process_raw(pcm,False,True);dec.end_utt();seg=[x for x in dec.seg() if x.word not in ['<sil>','<s>','</s>','[NOISE]']]
  clean=lambda w:re.sub(r'\(\d+\)$','',w)
  assert [clean(x.word) for x in seg]==expected,(s['id'],j)
  for w in seg:words.append({'word':clean(w.word),'from':round((pos+w.start_frame/100)*30),'to':round((pos+(w.end_frame+1)/100)*30)})
  # Independent unconstrained transcription coverage, in 15-second windows.
  heard=[]
  for k in range(0,len(a),15*sr):
   st=asr.create_stream();st.accept_waveform(sr,a[k:k+15*sr].astype(np.float32)/32768);asr.decode_stream(st);heard+=norm(st.result.text)
  ratio=difflib.SequenceMatcher(None,expected,heard,autojunk=False).ratio();assert ratio>.72,(s['id'],j,ratio,heard)
  report.append({'chapter':s['id']+1,'paragraph':j+1,'wordSimilarity':ratio,'seconds':len(a)/sr,'sourceSHA256':hashlib.sha256(new.read_bytes()).hexdigest()})
  parts.extend([a,np.zeros(round(.28*sr),np.int16)]);pos+=len(a)/sr+.28
  print('ALIGNED',s['id']+1,j+1,'ASR',round(ratio,3),flush=True)
 parts.append(np.zeros(round((6 if s['id']==9 else .55)*sr),np.int16));a=np.concatenate(parts);duration=math.ceil(len(a)/(sr/30));a=np.pad(a,(0,duration*800-len(a)))
 sc={**{k:s[k] for k in ['id','title','label','text','originalText']},'from':frame,'duration':duration,'words':words};assert norm(sc['text'])==[w['word'] for w in words]
 scenes.append(sc);full.append(a);frame+=duration
(r/'src/timeline.json').write_text(json.dumps(scenes,indent=2));write(o/'narration-raw.wav',np.concatenate(full))
(o/'qa/voice-alignment.json').write_text(json.dumps({'engine':'PocketTTS-FP32, same user-selected voice conditioning','rawNativeSeconds':native,'uniformTempo':tempo,'pitchPreserved':True,'totalFrames':frame,'seconds':frame/30,'words':1610,'totalWordsPerMinute':1610/(frame/30)*60,'paragraphs':report},indent=2));print('ALIGNMENT COMPLETE',frame,frame/30,flush=True)
