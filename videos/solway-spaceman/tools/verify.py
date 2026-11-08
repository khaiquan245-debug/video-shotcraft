from pathlib import Path
import json,subprocess,re,wave,difflib,hashlib
import numpy as np,sherpa_onnx
r=Path(__file__).resolve().parents[1];s=json.loads((r/'src/timeline.json').read_text());m=Path('/workspace/ten-seconds/tools/sherpa-onnx-whisper-tiny.en');rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=str(m/'tiny.en-encoder.int8.onnx'),decoder=str(m/'tiny.en-decoder.int8.onnx'),tokens=str(m/'tiny.en-tokens.txt'),num_threads=2,language='en')
def norm(t):return re.findall(r"[a-z]+(?:'[a-z]+)?",t.lower().replace('1964','nineteen sixty four'))
checks=[]
for sc in s:
 with wave.open(str(r/f'out/final-{sc["id"]}.wav')) as w:sr=w.getframerate();a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
 st=rec.create_stream();st.accept_waveform(sr,a);rec.decode_stream(st);ratio=difflib.SequenceMatcher(None,norm(sc['text']),norm(st.result.text),autojunk=False).ratio();print(sc['id'],ratio,st.result.text,flush=True);assert ratio>.67
 assert norm(sc['text'])==[w['text'] for w in sc['words']]
 assert all(sc['from']<=w['from']<w['to']<=sc['from']+sc['duration'] for w in sc['words'])
 checks.append({'scene':sc['id'],'asr':st.result.text,'similarity':ratio})
cues=(r/'output/solway_spaceman_subtitles.srt').read_text().strip().split('\n\n');caption_words=[]
for cue in cues:caption_words+=cue.splitlines()[2].split()
assert caption_words==[w['text'] for sc in s for w in sc['words']]
checks.append({'subtitleTokens':len(caption_words),'subtitleCues':len(cues),'sameNarratorConditioning':'/workspace/ten-seconds/reference/prompt.wav'})
arch=json.loads((r/'output/archival_manifest.json').read_text());media=json.loads((r/'src/media.json').read_text());assert media['photoAvailable'] and media['userPermissionConfirmed']
actual=hashlib.sha256((r/'public'/media['photoFile']).read_bytes()).hexdigest();assert actual==arch['sha256'];assert (r/'assets/archival'/Path(media['photoFile']).name).read_bytes()==(r/'public'/media['photoFile']).read_bytes()
checks.append({'archivalPhotoIncluded':True,'sourceResolution':[arch['width'],arch['height']],'unalteredSourceSha256':actual,'permission':'User confirmed reuse rights in chat'})
flat=[w for sc in s for w in sc['words']];maxgap=max((b['from']-a['to'])/30 for a,b in zip(flat,flat[1:]));assert maxgap<=.5
checks.append({'maxAlignedNarrationGapSeconds':maxgap,'continuousCadence':True})
frames=sum(x['duration'] for x in s)
for name in ['solway_spaceman_short.mp4','solway_spaceman_no_music.mp4']:
 p=r/'output'/name;info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]));v=next(x for x in info['streams'] if x['codec_type']=='video');a=next(x for x in info['streams'] if x['codec_type']=='audio');assert (v['width'],v['height'],v['codec_name'],v['pix_fmt'],v['r_frame_rate'])==(1080,1920,'h264','yuv420p','30/1');assert int(v['nb_frames'])==frames;assert 35<=float(info['format']['duration'])<=55;assert a['codec_name']=='aac';subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True);checks.append({'file':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'frames':frames,'seconds':float(info['format']['duration']),'codec':'H264/yuv420p/AAC'})
(r/'output/verification.json').write_text(json.dumps(checks,indent=2));print('PASS')
