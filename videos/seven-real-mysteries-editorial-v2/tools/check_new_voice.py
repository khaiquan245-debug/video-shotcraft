from pathlib import Path
import json,wave
import numpy as np,sherpa_onnx
r=Path(__file__).resolve().parents[1];m=Path('/workspace/ten-seconds/tools/sherpa-onnx-whisper-tiny.en');rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=str(m/'tiny.en-encoder.int8.onnx'),decoder=str(m/'tiny.en-decoder.int8.onnx'),tokens=str(m/'tiny.en-tokens.txt'),num_threads=2,language='en');result=[]
chunks=json.loads((r/'out/chunks.json').read_text())
for cid in ['7-2','7-3','8-0','8-1']:
 with wave.open(str(r/f'out/final-{cid}.wav')) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;sr=w.getframerate()
 s=rec.create_stream();s.accept_waveform(sr,a);rec.decode_stream(s);result.append({'id':cid,'expected':next(c['text'] for c in chunks if c['id']==cid),'recognized':s.result.text});print(cid,s.result.text,flush=True)
(r/'output/new_narration_asr.json').write_text(json.dumps(result,indent=2))
