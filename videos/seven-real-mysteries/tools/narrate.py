from pathlib import Path
import json,re,wave,subprocess,math
import numpy as np,sherpa_onnx
from pocketsphinx import Decoder
r=Path(__file__).resolve().parents[1];sr=24000
script=json.loads((r/'script.json').read_text())
# Accuracy-priority edit: do not assert unverified contemporary search dates.
old='A new Ocean Infinity search ended in January 2026 without locating the wreckage. In June, Malaysia extended its search agreement through June 2027. The extension allows further searching but establishes no discovery.'
new='Further search proposals have offered hope, but an agreement is not a discovery. The latest operational status needs confirmation from official updates. The evidence discussed here cannot establish when or where a future search might succeed.'
sc=script[7];sc['text']=sc['text'].replace(old,new)
sc['paragraphs']=sc['text'].split('\n\n') if '\n\n' in sc['text'] else re.split(r'(?<=[.!?])\s+(?=[A-Z])',sc['text'])
(r/'script.json').write_text(json.dumps(script,indent=2))
(r/'output/script_changes.md').write_text('# Accuracy edit\n\nThe supplied2026 MH370 search-end/extension assertions could not be independently verified: direct requests to official MOT/Yale/Commons sources were denied by the environment proxy (HTTP403). Replaced only the three contemporary-status sentences with: '+new+'\n\nAll other source narration preserved. No claim that a current search is operating or that wreckage has been discovered. Historical status is distinguished from unverified later operations on screen.\n')
replacements={'1977':'nineteen seventy seven','1912':'nineteen twelve','1901':'nineteen oh one','1959':'nineteen fifty nine','2020':'twenty twenty','2021':'twenty twenty one','1908':'nineteen oh eight','1980':'nineteen eighty','1971':'nineteen seventy one','2016':'twenty sixteen','2014':'twenty fourteen','2015':'twenty fifteen','2017':'twenty seventeen','777':'seven seventy seven','727':'seven twenty seven'}
def spoken(t):
 for k,v in replacements.items():t=re.sub(r'\b'+k+r'\b',v,t)
 return t.replace("'Wow!'",'Wow.').replace('D.B.','D B').replace('Réunion','Reunion').replace('word-like','word like').replace('seventy-two-second','seventy two second').replace('twenty-dollar','twenty dollar').replace('wind-loaded','wind loaded')
def norm(t):return re.findall(r"[a-z]+(?:'[a-z]+)?",spoken(t).lower().replace('-',' '))
m=Path('/workspace/ten-seconds/tools/sherpa-onnx-pocket-tts-2026-01-26');p=sherpa_onnx.OfflineTtsPocketModelConfig(**{k:str(m/v) for k,v in {'lm_flow':'lm_flow.onnx','lm_main':'lm_main.onnx','encoder':'encoder.onnx','decoder':'decoder.onnx','text_conditioner':'text_conditioner.onnx','vocab_json':'vocab.json','token_scores_json':'token_scores.json'}.items()});tts=sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(pocket=p,num_threads=3)))
with wave.open('/workspace/ten-seconds/reference/prompt.wav') as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;rate=w.getframerate()
c=sherpa_onnx.GenerationConfig();c.reference_audio=a;c.reference_sample_rate=rate;c.num_steps=5;c.speed=1
chunks=[]
for ch in script:
 # Narration paragraphs of 12–45 words preserve connected sentences.
 paragraphs=ch['paragraphs'];groups=[];buf=''
 for para in paragraphs:
  if buf and len((buf+' '+para).split())>48:groups.append(buf);buf=''
  buf=(buf+' '+para).strip()
 if buf:groups.append(buf)
 for j,text in enumerate(groups):
  k=f'{ch["id"]}-{j}';p=r/f'out/native-{k}.wav'
  if not p.exists():
   z=tts.generate(spoken(text),c)
   with wave.open(str(p),'wb') as w:w.setparams((1,2,z.sample_rate,0,'NONE','not compressed'));w.writeframes((np.clip(z.samples,-.95,.95)*32767).astype(np.int16).tobytes())
  with wave.open(str(p)) as w:seconds=w.getnframes()/w.getframerate()
  chunks.append({'id':k,'chapter':ch['id'],'text':text,'tokens':norm(text),'nativeSeconds':seconds});print('SYNTH',k,round(seconds,2),flush=True)
(r/'out/chunks.json').write_text(json.dumps(chunks,indent=2));print('NATIVE DONE',sum(x['nativeSeconds'] for x in chunks),sum(len(x['tokens']) for x in chunks),flush=True)
