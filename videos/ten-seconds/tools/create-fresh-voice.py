from pathlib import Path
import json,re,wave,time,shutil,hashlib,os,os
import numpy as np,sherpa_onnx
root=Path(__file__).resolve().parents[1];m=Path(os.environ.get('POCKET_MODEL_DIR',str(root/'tools/sherpa-onnx-pocket-tts-2026-01-26')));sr=24000
p=sherpa_onnx.OfflineTtsPocketModelConfig(lm_flow=str(m/'lm_flow.onnx'),lm_main=str(m/'lm_main.onnx'),encoder=str(m/'encoder.onnx'),decoder=str(m/'decoder.onnx'),text_conditioner=str(m/'text_conditioner.onnx'),vocab_json=str(m/'vocab.json'),token_scores_json=str(m/'token_scores.json'))
tts=sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(pocket=p,num_threads=3,provider='cpu')))
with wave.open(os.environ['VOICE_REFERENCE_WAV']) as w:reference=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;refsr=w.getframerate()
config=sherpa_onnx.GenerationConfig();config.reference_audio=reference;config.reference_sample_rate=refsr;config.speed=1.0;config.num_steps=5
scenes=json.loads((root/'tools/original-timeline.json').read_text());manifest=[]
def read(path):
 with wave.open(str(path)) as w:return np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768,w.getframerate()
for sc in scenes:
 original=sc['text'];text=original.replace('…',',').replace('’',"'").replace('“','"').replace('”','"');text=re.sub(r'([.!?]["\'])\s*,',r'\1',text);text=re.sub(r'\s+',' ',text).strip()
 if len(text.split())<=90:chunks=[text]
 else:
  chunks=[];buf=''
  for sentence in re.split(r'(?<=[.!?])\s+|(?<=[.!?]["\'])\s+',text):
   if buf and len((buf+' '+sentence).split())>85:chunks.append(buf);buf=''
   buf=(buf+' '+sentence).strip()
   if len(buf.split())>=55:chunks.append(buf);buf=''
  if buf:
   if chunks and len(buf.split())<18:chunks[-1]+=' '+buf
   else:chunks.append(buf)
 assert re.findall('[a-z0-9]+',original.lower().replace('’',"'"))==re.findall('[a-z0-9]+',' '.join(chunks).lower())
 chapter=[]
 for j,chunk in enumerate(chunks):
  path=root/f'out/pocket-fp32-{sc["id"]:02}-{j:02}.wav';meta=path.with_suffix('.json');signature=hashlib.sha256(chunk.encode()+reference.tobytes()+b'pocket-fp32-steps5-speed1').hexdigest()
  approved_meta=root/'out/new-voice-opening-approved.json'
  if sc['id']==0 and j==0 and (root/'out/new-voice-opening.wav').exists() and approved_meta.exists() and json.loads(approved_meta.read_text()).get('signature')==signature:
   shutil.copy2(root/'out/new-voice-opening.wav',path);a,rate=read(path);info={'source':'new-validated-opening','peakAfterScale':float(np.max(np.abs(a)))}
  elif path.exists() and meta.exists() and json.loads(meta.read_text()).get('signature')==signature:
   a,rate=read(path);info=json.loads(meta.read_text())
  else:
   start=time.time();z=tts.generate(chunk,config);a=np.asarray(z.samples,dtype=np.float32);rate=z.sample_rate;assert rate==sr and len(a)>sr*.3 and np.all(np.isfinite(a))
   peak=float(np.max(np.abs(a)));gain=min(1.0,.92/max(peak,1e-8));a*=np.float32(gain)
   # Preserve every phoneme and native pause. Only remove a possible edge click.
   edge=min(72,len(a)//4);a[:edge]*=np.linspace(0,1,edge);a[-edge:]*=np.linspace(1,0,edge)
   with wave.open(str(path),'wb') as w:w.setparams((1,2,rate,0,'NONE','not compressed'));w.writeframes((a*32767).astype(np.int16).tobytes())
   info={'source':'new-pocket-fp32-synthesis','rawPeak':peak,'gainForHeadroom':gain,'peakAfterScale':float(np.max(np.abs(a))),'generationSeconds':time.time()-start}
  assert rate==sr;info.update(signature=signature,engine='PocketTTS-FP32',speed=1.0);meta.write_text(json.dumps(info,indent=2));chapter.append({'text':chunk,'path':str(path.relative_to(root)),'seconds':len(a)/rate,'rawSeconds':len(a)/rate,'engine':'PocketTTS-FP32'})
  print('NEW VOICE',sc['id']+1,j+1,len(chunk.split()),'words',round(len(a)/rate,2),'seconds',info['source'],flush=True)
 manifest.append({'id':sc['id'],'title':sc['title'],'label':sc['label'],'originalText':original,'text':text,'paragraphs':chapter,'engine':'PocketTTS-FP32'})
 (root/'out/smooth-voice-manifest.json').write_text(json.dumps(manifest,indent=2));print('CHAPTER COMPLETE',sc['id']+1,flush=True)
print('VOICE GENERATION COMPLETE',flush=True)
