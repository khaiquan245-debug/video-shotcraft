from pathlib import Path
import json,re,wave
import numpy as np,sherpa_onnx
r=Path(__file__).resolve().parents[1]
replacements={'1977':'nineteen seventy seven','1912':'nineteen twelve','1901':'nineteen oh one','1959':'nineteen fifty nine','2020':'twenty twenty','2021':'twenty twenty one','1908':'nineteen oh eight','1980':'nineteen eighty','1971':'nineteen seventy one','2016':'twenty sixteen','2014':'twenty fourteen','2015':'twenty fifteen','2017':'twenty seventeen','2026':'twenty twenty six','2027':'twenty twenty seven','239':'two hundred and thirty nine','777':'seven seventy seven','727':'seven twenty seven'}
def spoken(t):
 for k,v in replacements.items():t=re.sub(r'\b'+k+r'\b',v,t)
 return t.replace("'Wow!'",'Wow.').replace('D.B.','D B').replace('Réunion','Reunion')
def norm(t):return re.findall(r"[a-z]+(?:'[a-z]+)?",spoken(t).lower())
m=Path('/workspace/ten-seconds/tools/sherpa-onnx-pocket-tts-2026-01-26');p=sherpa_onnx.OfflineTtsPocketModelConfig(**{k:str(m/v) for k,v in {'lm_flow':'lm_flow.onnx','lm_main':'lm_main.onnx','encoder':'encoder.onnx','decoder':'decoder.onnx','text_conditioner':'text_conditioner.onnx','vocab_json':'vocab.json','token_scores_json':'token_scores.json'}.items()});tts=sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(pocket=p,num_threads=3)))
with wave.open('/workspace/ten-seconds/reference/prompt.wav') as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;rate=w.getframerate()
c=sherpa_onnx.GenerationConfig();c.reference_audio=a;c.reference_sample_rate=rate;c.num_steps=5;c.speed=1
chunks=json.loads((r/'out/chunks.json').read_text())
for ch in chunks:
 p=r/f'out/native-{ch["id"]}.wav'
 if not p.exists():
  z=tts.generate(spoken(ch['text']),c)
  with wave.open(str(p),'wb') as w:w.setparams((1,2,z.sample_rate,0,'NONE','not compressed'));w.writeframes((np.clip(z.samples,-.95,.95)*32767).astype(np.int16).tobytes())
 ch['tokens']=norm(ch['text'])
 with wave.open(str(p)) as w:ch['nativeSeconds']=w.getnframes()/w.getframerate()
 print('VOICE',ch['id'],round(ch['nativeSeconds'],2),flush=True)
(r/'out/chunks.json').write_text(json.dumps(chunks,indent=2))
