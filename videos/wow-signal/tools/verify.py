from pathlib import Path
import json,subprocess,hashlib,wave,re,difflib
import numpy as np,sherpa_onnx
r=Path(__file__).resolve().parents[1];s=json.loads((r/'src/timeline.json').read_text());m=Path('/workspace/ten-seconds/tools/sherpa-onnx-whisper-tiny.en');rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=str(m/'tiny.en-encoder.int8.onnx'),decoder=str(m/'tiny.en-decoder.int8.onnx'),tokens=str(m/'tiny.en-tokens.txt'),num_threads=2,language='en')
def norm(t):return re.findall(r"[a-z]+(?:'[a-z]+)?",t.lower().replace('1977','nineteen seventy seven').replace('72','seventy two').replace('...',' '))
checks=[]
for sc in s:
 p=r/f'out/voice-{sc["id"]}.wav'
 if p.exists():
  with wave.open(str(p)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768;sr=w.getframerate()
 else:
  with wave.open(str(r/'public/audio/narration.wav')) as w:
   sr=w.getframerate();w.setpos(round(sc['from']/30*sr));a=np.frombuffer(w.readframes(round(sc['duration']/30*sr)),np.int16).astype(np.float32)/32768
 st=rec.create_stream();st.accept_waveform(sr,a);rec.decode_stream(st);ratio=difflib.SequenceMatcher(None,norm(sc['text']),norm(st.result.text),autojunk=False).ratio();checks.append({'scene':sc['id'],'heard':st.result.text,'similarity':ratio});print('ASR',sc['id'],ratio,st.result.text,flush=True)
 assert ratio>.68
for name in ['wow-signal.mp4','wow-signal-no-music.mp4']:
 p=r/'out'/name
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]));v=next(x for x in info['streams'] if x['codec_type']=='video');assert int(v['nb_frames'])==1800 and v['width']==1920 and v['height']==1080;assert abs(float(info['format']['duration'])-60)<.05
 subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True)
checks.append({'mainSha256':hashlib.sha256((r/'out/wow-signal.mp4').read_bytes()).hexdigest(),'seconds':60,'frames':1800,'allScenesAndWordsPreserved':all(norm(x['text'])==[w['text'] for w in x['words']] for x in s)})
(r/'out/verification.json').write_text(json.dumps(checks,indent=2));print('VERIFIED',flush=True)
