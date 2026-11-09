from pathlib import Path
import runpy,wave,subprocess,re,json,hashlib
import numpy as np
from pocketsphinx import Decoder
r=Path(__file__).resolve().parents[1]
if (r/'output/hook_repair.json').exists() and (r/'out/native-0-0.wav').exists():
 prior=json.loads((r/'output/hook_repair.json').read_text())
 if prior.get('repairedNativeSha256')==hashlib.sha256((r/'out/native-0-0.wav').read_bytes()).hexdigest():
  print('Hook repair already present');raise SystemExit(0)
env=runpy.run_path(str(r/'tools/narrate.py'));tts=env['tts'];c=env['c'];sr=24000;text='The word wow sounded surprising.';z=tts.generate(text,c);p=r/'out/hook-word-context.wav'
with wave.open(str(p),'wb') as w:w.setparams((1,2,z.sample_rate,0,'NONE','not compressed'));w.writeframes((np.clip(z.samples,-.95,.95)*32767).astype(np.int16).tobytes())
def seg(p,text):
 d=Decoder(lm=None,loglevel='ERROR',samprate=16000,beam=1e-80,wbeam=1e-60);d.set_align_text(text);d.start_utt();d.process_raw(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-af','apad=pad_dur=0.3','-ar','16000','-ac','1','-f','s16le','-']),False,True);d.end_utt();return [(re.sub(r'\(\d+\)$','',x.word),x.start_frame/100,(x.end_frame+1)/100) for x in d.seg()]
ss=seg(p,'the word wow sounded surprising');print('CONTEXT',ss,flush=True);wow=next(x for x in ss if x[0]=='wow');assert wow[2]-wow[1]>.18
with wave.open(str(p)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
word=a[max(0,round((wow[1]-.025)*sr)):round((wow[2]+.025)*sr)].copy();n=min(120,len(word));word[:n]=(word[:n]*np.linspace(0,1,n)).astype(np.int16);word[-n:]=(word[-n:]*np.linspace(1,0,n)).astype(np.int16)
p=r/'out/native-0-0.wav';tokens=env['norm'](env['chunks'][0]['text']);tokens.remove('wow');ss=seg(p,' '.join(tokens));them=next(x for x in ss if x[0]=='them');nxt=next(x for x in ss if x[0]=='the' and x[1]>them[1]);point=round((them[2]+nxt[1])/2*sr)
with wave.open(str(p)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).copy()
# The supplied single word was omitted by the model; insert same-speaker context-generated word at its correct clause boundary.
repaired=np.concatenate([a[:point],np.zeros(round(.10*sr),np.int16),word,np.zeros(round(.12*sr),np.int16),a[point:]])
with wave.open(str(p),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes(repaired.tobytes())
(r/'output/hook_repair.json').write_text(json.dumps({'repairedNativeSha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source':'same PocketTTS speaker/reference','contextText':text,'word':'wow','contextWordSeconds':wow[2]-wow[1],'nativeInsertionSeconds':point/sr,'reason':'Model omitted short quoted word; isolated context-generated word inserted at original script position. No change to spoken script.'},indent=2));print('REPAIRED',point/sr,len(word)/sr,flush=True)
