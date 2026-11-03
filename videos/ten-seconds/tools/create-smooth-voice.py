from pathlib import Path
import json,re,wave,subprocess,time,os,hashlib
import numpy as np,sherpa_onnx
root=Path(__file__).resolve().parents[1];sr=24000
model=Path(os.environ.get('ZIPVOICE_MODEL_DIR',str(root/'tools/sherpa-onnx-zipvoice-distill-int8-zh-en-emilia')))
c=sherpa_onnx.OfflineTtsZipvoiceModelConfig(tokens=str(model/'tokens.txt'),encoder=str(model/'encoder.int8.onnx'),decoder=str(model/'decoder.int8.onnx'),vocoder=os.environ.get('ZIPVOICE_VOCODER',str(root/'tools/vocos.onnx')),data_dir=str(model/'espeak-ng-data'),lexicon=str(model/'lexicon.txt'))
tts=sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(zipvoice=c,num_threads=3,provider='cpu')))
with wave.open(os.environ['VOICE_REFERENCE_WAV']) as w:prompt=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;prompt_sr=w.getframerate()
prompt_text=Path(os.environ['VOICE_REFERENCE_TEXT_FILE']).read_text().strip()
scenes=json.loads((root/'tools/original-timeline.json').read_text());manifest=[]
def read(path):
 with wave.open(str(path)) as w:return np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768,w.getframerate()
def write(path,a,rate):
 with wave.open(str(path),'wb') as w:w.setparams((1,2,rate,0,'NONE','not compressed'));w.writeframes((np.clip(a,-.99,.99)*32767).astype(np.int16).tobytes())
for sc in scenes:
 original=sc['text'];text=re.sub(r'\s*…+\s*',', ',original).replace('’',"'").replace('“','"').replace('”','"')
 text=re.sub(r'\.\s+(And|But|Or|Because|So|Then)\b',lambda m:', '+m[1].lower(),text)
 text=re.sub(r'\bNo\.\s+The\b','No, the',text);text=re.sub(r'\s+',' ',text).strip()
 assert re.findall('[a-z0-9]+',original.lower().replace('’',"'"))==re.findall('[a-z0-9]+',text.lower())
 sentences=re.split(r'(?<=[.!?])\s+',text);chunks=[];buf=''
 for sentence in sentences:
  if not sentence.strip():continue
  if buf and len((buf+' '+sentence).split())>85:chunks.append(buf);buf=''
  buf=(buf+' '+sentence).strip()
  if len(buf.split())>=45:chunks.append(buf);buf=''
 if buf:
  if chunks and len(buf.split())<15:chunks[-1]+=' '+buf
  else:chunks.append(buf)
 chapter=[]
 for j,chunk in enumerate(chunks):
  raw=root/f'out/voice-{sc["id"]:02}-{j:02}-raw.wav';clean=root/f'out/voice-{sc["id"]:02}-{j:02}.wav'
  signature=hashlib.sha256(chunk.encode()+prompt.tobytes()+prompt_text.encode()+b'zipvoice-speed1-steps4').hexdigest();meta=raw.with_suffix('.meta.json')
  if not raw.exists() or not meta.exists() or json.loads(meta.read_text()).get('signature')!=signature:
   t=time.time();audio=tts.generate(chunk,prompt_text=prompt_text,prompt_samples=prompt,sample_rate=prompt_sr,speed=1.0,num_steps=4);assert audio.sample_rate>0 and len(audio.samples)>0
   write(raw,audio.samples,audio.sample_rate);meta.write_text(json.dumps({'signature':signature}));print('SYNTH',sc['id']+1,j+1,len(chunk.split()),'words',round(time.time()-t,1),'seconds',flush=True)
  limit=.75 if sc['id']>=8 else .50;keep=.28 if sc['id']>=8 else .16
  # Trim only long silence; no speech time-stretching and no forced chapter length.
  filt=f'silenceremove=start_periods=1:start_duration=0.02:start_threshold=-50dB:start_silence=0.05:stop_periods=-1:stop_duration={limit}:stop_threshold=-45dB:stop_silence={keep}'
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-af',filt,'-ar',str(sr),str(clean)],check=True)
  a,rate=read(clean);assert rate==sr and len(a)>sr*.2
  n=min(120,len(a)//4);a[:n]*=np.linspace(0,1,n);a[-n:]*=np.linspace(1,0,n)
  write(clean,a,sr);chapter.append({'text':chunk,'path':str(clean.relative_to(root)),'seconds':len(a)/sr,'rawSeconds':len(read(raw)[0])/sr})
 manifest.append({'id':sc['id'],'title':sc['title'],'label':sc['label'],'originalText':original,'text':text,'paragraphs':chapter})
 (root/'out/smooth-voice-manifest.json').write_text(json.dumps(manifest,indent=2))
 if sc['id']==0:
  preview=np.concatenate([np.concatenate([read(root/x['path'])[0],np.zeros(int(.18*sr),np.float32)]) for x in chapter]);write(root/'out/smooth-voice-preview.wav',preview,sr)
 print('CHAPTER',sc['id']+1,'paragraphs',len(chapter),'speech seconds',round(sum(x['seconds'] for x in chapter),2),flush=True)
print('VOICE GENERATION COMPLETE',flush=True)
