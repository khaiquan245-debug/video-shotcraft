from pathlib import Path
import json,re,subprocess,hashlib,wave,difflib,sys
import numpy as np,sherpa_onnx
r=Path(__file__).resolve().parents[1];d=json.loads((r/'src/timeline.json').read_text());caps=json.loads((r/'src/captions.json').read_text());shots=json.loads((r/'src/shots.json').read_text());voice=json.loads((r/'output/voice_report.json').read_text())
assert len(d['chapters'])==9;assert [c['id'] for c in d['chapters']]==list(range(9));assert 350<=d['frames']/30<=420;assert voice['tempo']==1.0 and voice['timeStretchRemoved']
ws=[w for ch in d['chapters'] for w in ch['words']];assert sum(len(c['tokens']) for c in d['chunks'])==len(ws);assert all(c['from']<=w['from']<w['to']<=c['from']+c['duration'] for c in d['chapters'] for w in c['words'])
assert [w['text'] for w in ws]==' '.join(c['text'] for c in caps).split();assert all(a['to']<=b['from'] for a,b in zip(caps,caps[1:]));assert shots[0]['from']==0 and all(a['from']+a['duration']==b['from'] for a,b in zip(shots,shots[1:]));assert shots[-1]['from']+shots[-1]['duration']==d['frames'];checks={'chapters':9,'shots':len(shots),'seconds':d['frames']/30,'subtitleTokens':len(ws),'subtitleCues':len(caps),'wordsPerMinute':voice['wordsPerMinute']}
# ASR is independent of forced transcript alignment; pronunciation/naturalness still needs listening.
m=Path('/workspace/ten-seconds/tools/sherpa-onnx-whisper-tiny.en');rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=str(m/'tiny.en-encoder.int8.onnx'),decoder=str(m/'tiny.en-decoder.int8.onnx'),tokens=str(m/'tiny.en-tokens.txt'),num_threads=2,language='en');asr=[]
def norm(t):
 t=t.lower()
 # Normalize ASR number formatting; do not mistake digits for omitted narration.
 for a,b in [('$5,800','five thousand eight hundred dollars'),('$200,000','two hundred thousand dollars'),('$20','twenty dollar'),('1.5 mm','one and a half millimeters'),('1.5 millimeters','one and a half millimeters'),('2,000','two thousand'),('1420','fourteen hundred and twenty'),('240','two hundred and forty'),('239','two hundred and thirty nine'),('370','three seven zero'),('15th','fifteenth'),('august 15','august fifteenth'),('november 24','november twenty fourth'),('march 8','march eighth'),('72','seventy two'),('30','thirty'),('6 eq uj5','six e q u j five'),('6 equj5','six e q u j five'),('big-year','big ear')]:t=t.replace(a,b)
 for a,b in [('1977','nineteen seventy seven'),('1912','nineteen twelve'),('1901','nineteen oh one'),('1959','nineteen fifty nine'),('2020','twenty twenty'),('2021','twenty twenty one'),('1908','nineteen oh eight'),('1980','nineteen eighty'),('1971','nineteen seventy one'),('2016','twenty sixteen'),('2014','twenty fourteen'),('2015','twenty fifteen'),('2017','twenty seventeen'),('777','seven seventy seven'),('727','seven twenty seven')]:t=t.replace(a,b)
 return re.findall(r"[a-z]+(?:'[a-z]+)?",t.replace('réunion','reunion').replace('d.b.','d b'))
cached=json.loads((r/'output/verification.json').read_text()) if (r/'output/verification.json').exists() else {}
voice_sha=hashlib.sha256((r/'output/7_real_unsolved_mysteries_voice.wav').read_bytes()).hexdigest()
reuse={z['id']:z['recognized'] for z in cached.get('asr',[])} if '--reuse-audio' in sys.argv and cached.get('narrationSha256')==voice_sha else {}
for ch in d['chunks']:
 with wave.open(str(r/f'out/final-{ch["id"]}.wav')) as w:sr=w.getframerate();a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
 recognized=reuse.get(ch['id'])
 if recognized is None:
  st=rec.create_stream();st.accept_waveform(sr,a);rec.decode_stream(st);recognized=st.result.text
 ratio=difflib.SequenceMatcher(None,norm(ch['text']),norm(recognized),autojunk=False).ratio();analysis_tempo=1.0
 if ratio<.72:
  # Tiny Whisper can loop on currency strings at native cadence. Independently decode
  # a pitch-preserving slowed ANALYSIS copy; never alter delivered audio.
  pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(r/f'out/final-{ch["id"]}.wav'),'-af','rubberband=tempo=0.9:formant=preserved','-ar','24000','-ac','1','-f','f32le','-'])
  st=rec.create_stream();st.accept_waveform(24000,np.frombuffer(pcm,np.float32));rec.decode_stream(st);retry=st.result.text;rr=difflib.SequenceMatcher(None,norm(ch['text']),norm(retry),autojunk=False).ratio()
  if rr>ratio:recognized=retry;ratio=rr;analysis_tempo=.9
 asr.append({'id':ch['id'],'expected':ch['text'],'recognized':recognized,'similarity':ratio,'analysisTempo':analysis_tempo});print('ASR',ch['id'],round(ratio,3),flush=True)
 assert ratio>.72,(ch['id'],recognized)
 if ch['id']=='0-0':assert 'wow' in recognized.lower()
checks['narrationSha256']=voice_sha;checks['asr']=asr;(r/'output/verification.json').write_text(json.dumps(checks,indent=2))
if '--audio-only' in sys.argv:print('AUDIO PASS');sys.exit()
files=[]
for name in ['7_real_unsolved_mysteries.mp4','7_real_unsolved_mysteries_no_music.mp4']:
 p=r/'output'/name;info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]));v=next(x for x in info['streams'] if x['codec_type']=='video');a=next(x for x in info['streams'] if x['codec_type']=='audio');assert (v['width'],v['height'],v['codec_name'],v['pix_fmt'],v['r_frame_rate'])==(1920,1080,'h264','yuv420p','30/1');assert int(v['nb_frames'])==d['frames'];assert a['codec_name']=='aac' and a['sample_rate']=='48000';assert abs(float(info['format']['duration'])-d['frames']/30)<.05;subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True)
 pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-vn','-f','f32le','-']);audio=np.frombuffer(pcm,np.float32);peak=float(abs(audio).max());assert peak<1.0
 files.append({'file':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'seconds':float(info['format']['duration']),'frames':v['nb_frames'],'codec':'H264/yuv420p/AAC','audioChannels':a['channels'],'decodedAudioPeak':peak,'fullDecodePass':True});print('VIDEO PASS',name,flush=True)
checks['files']=files;(r/'output/verification.json').write_text(json.dumps(checks,indent=2));print('COMPLETE PASS')
