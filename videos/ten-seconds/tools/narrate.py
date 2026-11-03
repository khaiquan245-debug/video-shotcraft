import re,json,wave,subprocess,os
from pathlib import Path
import numpy as np,sherpa_onnx
root=Path(__file__).resolve().parents[1]
model=Path(os.environ.get('ZIPVOICE_MODEL_DIR',str(root/'tools/sherpa-onnx-zipvoice-distill-int8-zh-en-emilia')))
c=sherpa_onnx.OfflineTtsZipvoiceModelConfig(tokens=str(model/'tokens.txt'),encoder=str(model/'encoder.int8.onnx'),decoder=str(model/'decoder.int8.onnx'),vocoder=os.environ.get('ZIPVOICE_VOCODER',str(root/'tools/vocos.onnx')),data_dir=str(model/'espeak-ng-data'),lexicon=str(model/'lexicon.txt'))
tts=sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(zipvoice=c,num_threads=3,provider='cpu')))
with wave.open(os.environ['VOICE_REFERENCE_WAV']) as w: prompt=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;prompt_sr=w.getframerate()
prompt_text=Path(os.environ['VOICE_REFERENCE_TEXT_FILE']).read_text().strip()
s=root.joinpath('script-original.md').read_text()
scenes=[]; start=0
names=['What could ten seconds change?','A glimpse. A choice.','Dignity: not included','Emergency meeting mode','The cat has other plans','Ten seconds on the road','The future fights back','The perfect answer?','The courage to hear no','The call you almost missed','You still cannot see everything','The ten seconds you have now']
short=['THE QUESTION','THE RULES','THE COFFEE','THE MEETING','THE CAT','THE CROSSING','THE GAME','THE INTERVIEW','THE CONFESSION','THE PHONE CALL','THE TWIST','RIGHT NOW']
targets=[25,25,30,35,25,40,35,30,55,90,30,60]
for i,p in enumerate(re.split(r'## SCENE ',s)[1:]):
 v=re.split(r'\*\*\[Voice-over[^\]]*\]\*\*',p)[1]
 v=re.split(r'\*\*\[(?:Sound|Visual)',v)[0].split('---')[0].strip().replace('**','')
 text=re.sub(r'\s+',' ',v).strip()
 if i==11:text=text.replace('Black screen. Text appears: ', '').replace(' Then: ', ' ')
 chunks=re.split(r'(?<=[.!?…])\s+',text)
 merged=[]
 for c in chunks:
  if not c.strip():continue
  if merged and len(merged[-1].split())<5 and len(merged[-1])+len(c)<130:merged[-1]+=' '+c
  else:merged.append(c)
 parts=[]; local=[]; pos=0; sr=22050
 for j,c in enumerate(merged):
  out=root/f'public/audio/raw-{i}-{j}.wav'
  if out.exists():
   with wave.open(str(out)) as w: a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768;sr=w.getframerate()
  else:
   z=tts.generate(c,prompt_text=prompt_text,prompt_samples=prompt,sample_rate=prompt_sr,speed=1.03 if i<8 else 1.0,num_steps=4);sr=z.sample_rate;a=z.samples
   with wave.open(str(out),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((np.clip(a,-1,1)*32767).astype(np.int16).tobytes())
  local.append({'text':c,'start':pos/sr,'end':(pos+len(a))/sr})
  gap=np.zeros(int(sr*(.15 if i<8 else .24)),dtype=np.float32)
  parts.extend([a,gap]);pos+=len(a)+len(gap)
 audio=np.concatenate(parts); native=len(audio)/sr; target=targets[i];available=target-1.5
 rate=native/available
 raw=root/f'public/audio/scene-{i+1:02}-raw.wav';final=root/f'public/audio/scene-{i+1:02}.wav'
 with wave.open(str(raw),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((np.clip(audio,-1,1)*32767).astype(np.int16).tobytes())
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-af',f'atempo={rate},adelay=600:all=1,apad','-t',str(target),'-ar','48000',str(final)],check=True)
 caps=[{'text':c['text'],'from':round((.6+c['start']/rate)*30),'duration':max(1,round((c['end']-c['start'])/rate*30))} for c in local]
 scene={'id':i,'title':names[i],'label':short[i],'from':start,'duration':target*30,'captions':caps,'audio':f'audio/scene-{i+1:02}.wav','text':text,'speechRate':round(rate,3)}
 scenes.append(scene);start+=target*30
 print(i+1, 'native',round(native,1),'target',target,'rate',round(rate,2),flush=True)
root.joinpath('src/timeline.json').write_text(json.dumps(scenes,indent=2))
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
lines=[]
for sc in scenes:
 for c in sc['captions']:
  t=(sc['from']+c['from'])/30;end=min((sc['from']+sc['duration'])/30,t+c['duration']/30)
  lines.append(f'{len(lines)+1}\n{stamp(t)} --> {stamp(end)}\n{c["text"]}\n')
root.joinpath('out/ten-seconds.en.srt').write_text('\n'.join(lines))
