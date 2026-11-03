"""Verify current encoded picture, preserved audio, and word/caption bounds."""
from pathlib import Path
import json,subprocess,hashlib,re
root=Path(__file__).resolve().parents[1];out=root/'out'
run=lambda args:subprocess.run(args,capture_output=True,text=True,check=True)
scenes=json.loads((root/'src/timeline.json').read_text());frames=sum(s['duration'] for s in scenes)
baseline_path=out/'qa/picture-sync-audio-baseline.json'
if not baseline_path.exists():baseline_path=root/'qa/picture-sync-audio-baseline.json'
baseline=json.loads(baseline_path.read_text())
assert hashlib.sha256((root/'public/audio/master.flac').read_bytes()).hexdigest()==baseline['masterFLAC']
assert hashlib.sha256((root/'public/audio/narration.flac').read_bytes()).hexdigest()==baseline['narrationFLAC']
tokens=lambda s:re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",s.lower().replace('’',"'").replace('10','ten'))
for sc in scenes:
 assert tokens(sc['text'])==[w['word'] for w in sc['words']]
 assert tokens(sc['text'])==tokens(' '.join(c['text'] for c in sc['captions']))
 assert all(0<=c['from']<c['from']+c['duration']<=sc['duration'] for c in sc['captions'])
 assert all(0<=t<sc['duration'] for t in sc['events'].values())
 for a,b in zip(sc['captions'],sc['captions'][1:]):assert a['from']+a['duration']<=b['from']
main=out/'ten-seconds-smooth.mp4';nomusic=out/'ten-seconds-smooth-no-music.mp4'
run(['ffmpeg','-v','error','-y','-i',str(main),'-i',str(root/'public/audio/narration.flac'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','160k','-t',str(frames/30),'-movflags','+faststart',str(nomusic)])
report={'method':'acoustic word-timed picture revision','frames':frames,'seconds':frames/30,'scriptWords':sum(len(s['words']) for s in scenes),'scenes':len(scenes),'captionBounds':'passed','scriptPreserved':True,'losslessAudioUnchanged':True,'exports':{}}
for p in [main,nomusic]:
 probe=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]).stdout)
 v=next(s for s in probe['streams'] if s['codec_type']=='video')
 assert int(v['nb_frames'])==frames and abs(float(probe['format']['duration'])-frames/30)<.1 and (v['width'],v['height'])==(1920,1080)
 run(['ffmpeg','-v','error','-xerror','-i',str(p),'-f','null','-'])
 h=run(['ffmpeg','-v','error','-i',str(p),'-map','0:v:0','-c','copy','-f','hash','-hash','sha256','-']).stdout.strip()
 ah=run(['ffmpeg','-v','error','-i',str(p),'-map','0:a:0','-c','copy','-f','hash','-hash','sha256','-']).stdout.strip()
 volume=run(['ffmpeg','-hide_banner','-i',str(p),'-vn','-af','volumedetect','-f','null','-']).stderr
 peak=float(re.search(r'max_volume: ([-.0-9]+) dB',volume)[1]);assert peak<0
 report['exports'][p.name]={'fullDecode':'passed','videoHash':h,'audioHash':ah,'peakDBFS':peak,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 print('VERIFIED',p.name,flush=True)
assert report['exports'][main.name]['videoHash']==report['exports'][nomusic.name]['videoHash']
assert report['exports'][main.name]['audioHash']==baseline['previousEncodedAudio']
report['encodedMusicAudioIdenticalToApprovedExport']=True;report['musicAndNoMusicSamePicture']=True
(out/'qa/picture-sync-verification.json').write_text(json.dumps(report,indent=2));print('PICTURE SYNC DELIVERY VERIFIED',flush=True)
