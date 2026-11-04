from pathlib import Path
import json,subprocess,hashlib,re,os
r=Path(__file__).resolve().parents[1];o=r/'out';q=o/'qa'
run=lambda a:subprocess.run(a,capture_output=True,text=True,check=True)
scenes=json.loads((r/'src/timeline.json').read_text());shots=json.loads((r/'src/shots.json').read_text());caps=json.loads((r/'src/captions.json').read_text())
tokens=lambda t:re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",t.lower().replace('’',"'").replace('10','ten'))
frames=sum(s['duration'] for s in scenes)
assert shots[0]['from']==0 and shots[-1]['from']+shots[-1]['duration']==frames
assert all(a['from']+a['duration']==b['from'] for a,b in zip(shots,shots[1:]))
for s in scenes:
 assert tokens(s['text'])==tokens(' '.join(c['text'] for c in caps if c['chapter']==s['id']))
assert all(0<=c['from']<c['from']+c['duration']<=frames for c in caps)
assert all(a['from']+a['duration']<=b['from'] for a,b in zip(caps,caps[1:]))
prior=Path(os.environ.get('APPROVED_VOICE_FILM','/workspace/video-shotcraft/videos/ten-seconds/deliverables/ten-seconds.mp4'))
baseline_path=r/'qa/approved-audio-baseline.json'
if prior.exists():baseline=run(['ffmpeg','-v','error','-i',str(prior),'-map','0:a:0','-c','copy','-f','hash','-hash','sha256','-']).stdout.strip()
elif baseline_path.exists():baseline=json.loads(baseline_path.read_text())['approvedEncodedAudio']
else:raise RuntimeError('Set APPROVED_VOICE_FILM or supply recorded approved-audio-baseline.json')
report={'frames':frames,'fps':30,'seconds':frames/30,'chapters':len(scenes),'shots':len(shots),'shortCaptions':len(caps),'scriptWords':sum(len(s['words']) for s in scenes),'scriptPreserved':True,'captionBounds':'passed','fullStoryboardCoverage':'passed','approvedEncodedAudio':baseline,'exports':{}}
main=o/'ten-seconds-cinematic.mp4';nomusic=o/'ten-seconds-cinematic-no-music.mp4'
# Both variants share the identical rendered video; source audio selects frozen master/narration.
run(['ffmpeg','-v','error','-y','-i',str(main),'-i',str(r/'public/audio/narration.flac'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','160k','-t',str(frames/30),'-movflags','+faststart',str(nomusic)])
for p in [main,nomusic]:
 d=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]).stdout);v=next(x for x in d['streams'] if x['codec_type']=='video')
 assert int(v['nb_frames'])==frames and (v['width'],v['height'])==(1920,1080) and v['r_frame_rate']=='30/1'
 assert abs(float(d['format']['duration'])-frames/30)<.1
 run(['ffmpeg','-v','error','-xerror','-i',str(p),'-f','null','-'])
 vh=run(['ffmpeg','-v','error','-i',str(p),'-map','0:v:0','-c','copy','-f','hash','-hash','sha256','-']).stdout.strip()
 ah=run(['ffmpeg','-v','error','-i',str(p),'-map','0:a:0','-c','copy','-f','hash','-hash','sha256','-']).stdout.strip()
 volume=run(['ffmpeg','-hide_banner','-i',str(p),'-vn','-af','volumedetect','-f','null','-']).stderr;peak=float(re.search(r'max_volume: ([-.0-9]+) dB',volume)[1]);assert peak<0
 report['exports'][p.name]={'fullDecode':'passed','videoHash':vh,'audioHash':ah,'peakDBFS':peak,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size};print('VERIFIED',p.name,flush=True)
assert report['exports'][main.name]['audioHash']==baseline
assert report['exports'][main.name]['videoHash']==report['exports'][nomusic.name]['videoHash']
report['approvedVoiceAndMusicBitIdentical']=True;report['samePictureVariants']=True
q.mkdir(parents=True,exist_ok=True);(q/'cinematic-verification.json').write_text(json.dumps(report,indent=2))
for n in [0,7,15,21,26,28,35,43,49,57,62,66,67,71,78,84,87]:
 s=shots[n];t=(s['from']+round(s['duration']*.45))/30
 run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(main),'-frames:v','1',str(q/f'encoded-shot-{n:03}.jpg')])
(o/'chapters.txt').write_text('\n'.join(f'{s["from"]//1800:02}:{s["from"]//30%60:02} {s["title"]}' for s in scenes)+'\n');print('CINEMATIC DELIVERY VERIFIED',flush=True)
