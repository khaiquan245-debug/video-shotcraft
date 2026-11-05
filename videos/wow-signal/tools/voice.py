from pathlib import Path
import json,wave,subprocess,math,re
import numpy as np,sherpa_onnx
from pocketsphinx import Decoder
r=Path(__file__).resolve().parents[1];sr=24000;m=Path('/workspace/ten-seconds/tools/sherpa-onnx-pocket-tts-2026-01-26')
texts=["In 1977, Earth detected a mysterious signal from space. It lasted just 72 seconds. Then... it vanished.","A radio telescope in Ohio had picked up something extraordinary. A powerful, narrow radio signal unlike the usual background noise.","When astronomer Jerry Ehman examined the data, he circled six strange characters... And wrote just one word. Wow!","The signal appeared to come from the direction of Sagittarius. Near a frequency scientists had considered promising for communication across space. Was someone trying to contact Earth?","Scientists searched for it again. And again. But the signal never returned. Some researchers now suspect a natural cosmic event.","Nearly fifty years later, its exact cause remains unconfirmed. So what did Earth detect... for those 72 seconds?"]
(r/'script.json').write_text(json.dumps(texts,indent=2));p=sherpa_onnx.OfflineTtsPocketModelConfig(**{k:str(m/(v)) for k,v in {'lm_flow':'lm_flow.onnx','lm_main':'lm_main.onnx','encoder':'encoder.onnx','decoder':'decoder.onnx','text_conditioner':'text_conditioner.onnx','vocab_json':'vocab.json','token_scores_json':'token_scores.json'}.items()});tts=sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(pocket=p,num_threads=3)))
with wave.open('/workspace/ten-seconds/reference/prompt.wav') as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;rate=w.getframerate()
c=sherpa_onnx.GenerationConfig();c.reference_audio=a;c.reference_sample_rate=rate;c.num_steps=5;c.speed=1
lengths=[9,10,10,12,10,9];full=[];scenes=[];offset=0
for i,text in enumerate(texts):
 raw=r/f'out/native-{i}.wav'
 if not raw.exists():
  z=tts.generate(text,c)
  with wave.open(str(raw),'wb') as w:w.setparams((1,2,z.sample_rate,0,'NONE','not compressed'));w.writeframes((np.clip(z.samples,-.95,.95)*32767).astype(np.int16).tobytes())
 with wave.open(str(raw)) as w:dur=w.getnframes()/w.getframerate()
 tempo=.98 if i==0 else 1.03 if i<5 else 1.0;target=math.ceil((dur/tempo+(.9 if i==5 else .18))*30)/30
 out=r/f'out/voice-{i}.wav';subprocess.run(['ffmpeg','-v','error','-y','-i',str(raw),'-af',f'rubberband=tempo={tempo}:formant=preserved,loudnorm=I=-18:TP=-3:LRA=10','-ar',str(sr),str(out)],check=True)
 with wave.open(str(out)) as w:audio=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
 assert len(audio)<=target*sr
 full.append(np.pad(audio,(0,round(target*sr)-len(audio))))
 pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(out),'-ar','16000','-ac','1','-f','s16le','-'])
 d=Decoder(lm=None,loglevel='ERROR',samprate=16000,beam=1e-80,wbeam=1e-60)
 norm=text.lower().replace('1977','nineteen seventy seven').replace('72','seventy two').replace('...',' ')
 words=re.findall(r"[a-z]+(?:'[a-z]+)?",norm)
 for token,pron in [('ehman','EY M AH N'),('sagittarius','S AE JH AH T EH R IY AH S')]:
  if not d.lookup_word(token):d.add_word(token,pron,True)
 d.set_align_text(' '.join(words));d.start_utt();d.process_raw(pcm,False,True);d.end_utt();ws=[{'text':re.sub(r'\(\d+\)$','',x.word),'from':offset+round(x.start_frame*.3),'to':offset+round((x.end_frame+1)*.3)} for x in d.seg() if x.word not in ['<sil>','<s>','</s>','[NOISE]']]
 scenes.append({'id':i,'from':offset,'duration':round(target*30),'text':text,'words':ws,'tempo':tempo});offset+=round(target*30);print('VOICE',i,dur,tempo,flush=True)
with wave.open(str(r/'out/narration.wav'),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes(np.concatenate(full).tobytes())
(r/'src/timeline.json').write_text(json.dumps(scenes,indent=2));print('VOICE DONE',offset,flush=True)
