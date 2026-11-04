from pathlib import Path
import subprocess,json,re,hashlib,wave
import numpy as np
r=Path(__file__).resolve().parents[1];o=r/'out';q=o/'qa';run=lambda a:subprocess.run(a,capture_output=True,text=True,check=True)
scenes=json.loads((r/'src/timeline.json').read_text());shots=json.loads((r/'src/shots.json').read_text());caps=json.loads((r/'src/captions.json').read_text());original=json.loads((r/'tools/original-timeline.json').read_text());frames=sum(s['duration'] for s in scenes);seconds=frames/30
norm=lambda t:re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",t.lower().replace('’',"'"))
assert len(scenes)==10 and 480<=seconds<=600
assert shots[0]['from']==0 and shots[-1]['from']+shots[-1]['duration']==frames
assert all(a['from']+a['duration']==b['from'] for a,b in zip(shots,shots[1:]))
for sc,src in zip(scenes,original):
 assert norm(sc['originalText'])==norm(src['text'])==norm(sc['text'])==norm(' '.join(c['text'] for c in caps if c['chapter']==sc['id']))
assert all(0<=c['from']<c['from']+c['duration']<=frames for c in caps)
assert all(a['from']+a['duration']<=b['from'] for a,b in zip(caps,caps[1:]))
final=scenes[-1];last=next(b for b in final['beats'] if b['tag']=='final');hold=frames-max(final['from']+last['from'],shots[-1]['from'])-30;assert hold>=150
main=o/'learn-100x.mp4';nomusic=o/'learn-100x-no-music.mp4'
run(['ffmpeg','-v','error','-y','-i',str(main),'-i',str(r/'public/audio/narration-sfx.flac'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','160k','-t',str(seconds),'-movflags','+faststart',str(nomusic)])
reference=q/'expected-audio.m4a';run(['ffmpeg','-v','error','-y','-i',str(r/'public/audio/master.flac'),'-c:a','aac','-b:a','160k','-t',str(seconds),str(reference)])
hashtrack=lambda p,track:run(['ffmpeg','-v','error','-i',str(p),'-map',track,'-c','copy','-f','hash','-hash','sha256','-']).stdout.strip()
expectedAudio=hashtrack(reference,'0:a:0');report={'title':'What If You Could Learn 100 Times Faster?','frames':frames,'fps':30,'seconds':seconds,'chapters':len(scenes),'shots':len(shots),'shortCaptions':len(caps),'sourceWords':sum(len(norm(s['text'])) for s in original),'fullScriptPreserved':True,'captionBounds':'passed','storyboardContiguous':True,'finalQuestionFullOpacityFrames':hold,'voiceWordsPerMinute':1610/seconds*60,'exports':{}}
for p in [main,nomusic]:
 d=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]).stdout);v=next(x for x in d['streams'] if x['codec_type']=='video');assert (v['width'],v['height'],int(v['nb_frames']),v['r_frame_rate'])==(1920,1080,frames,'30/1');assert abs(float(d['format']['duration'])-seconds)<.1
 decode=run(['ffmpeg','-hide_banner','-v','info','-xerror','-i',str(p),'-vf','blackdetect=d=0.2:pix_th=0.06:pic_th=0.98','-f','null','-']).stderr
 black=[list(map(float,m)) for m in re.findall(r'black_start:([.0-9]+) black_end:([.0-9]+) black_duration:([.0-9]+)',decode)]
 assert all(a<1 or b>seconds-1 for a,b,c in black),(p.name,black)
 volume=run(['ffmpeg','-hide_banner','-i',str(p),'-vn','-af','volumedetect','-f','null','-']).stderr;peak=float(re.search(r'max_volume: ([-.0-9]+) dB',volume)[1]);assert peak<0
 report['exports'][p.name]={'fullDecode':'passed','peakDBFS':peak,'videoHash':hashtrack(p,'0:v:0'),'audioHash':hashtrack(p,'0:a:0'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'blackIntervals':black};print('VERIFIED',p.name,flush=True)
assert report['exports'][main.name]['audioHash']==expectedAudio
assert report['exports'][main.name]['videoHash']==report['exports'][nomusic.name]['videoHash']
report['finalMixExactlyEncoded']=True;report['samePictureVariants']=True
# Final-source cue samples include short phases that midpoint shot stills can miss.
requests=[(0,'alarm'),(0,'brain'),(0,'comparison'),(1,'body'),(2,'diploma'),(3,'zero'),(3,'orders'),(4,'pianoMistake'),(4,'miss'),(5,'employees'),(5,'investors'),(5,'testing'),(6,'viral'),(6,'privacy'),(6,'everyone'),(7,'evidence'),(7,'unknown'),(8,'dinner'),(8,'memory'),(8,'aha'),(9,'aging'),(9,'oneLife'),(9,'window'),(9,'final')]
for i,tag in requests:
 sc=scenes[i];b=next(x for x in sc['beats'] if x['tag']==tag);end=next((x['from'] for x in sc['beats'] if x['from']>b['from']),sc['duration']);offset=min(35,max(1,(end-b['from'])//2));frame=sc['from']+b['from']+offset
 run(['ffmpeg','-v','error','-y','-ss',str(frame/30),'-i',str(main),'-frames:v','1',str(q/f'encoded-{i+1:02}-{tag}.jpg')])
# Isolated opening tick provides a signal-based AAC/output offset probe.
with wave.open(str(r/'public/audio/sfx/original-tick.wav')) as w:tick=np.frombuffer(w.readframes(2400),np.int16).astype(np.float32)/32768
probe=subprocess.run(['ffmpeg','-v','error','-i',str(main),'-t','0.15','-ac','1','-ar','48000','-f','f32le','-'],capture_output=True,check=True).stdout
decoded=np.frombuffer(probe,np.float32);search=np.pad(decoded[:4800],(2400,0));corr=np.correlate(search,tick,'valid');index=int(np.argmax(corr));lag=index-2400
similarity=float(corr[index]/max(1e-12,np.linalg.norm(tick)*np.linalg.norm(search[index:index+len(tick)])))
assert abs(lag)<=1600 and similarity>.25,(lag,similarity)
report['openingTickDecodedOffset']={'samplesAt48k':lag,'seconds':lag/48000,'framesAt30fps':lag/1600,'normalizedCorrelation':similarity}
(q/'film-verification.json').write_text(json.dumps(report,indent=2));reference.unlink()
(o/'chapters.txt').write_text('\n'.join(f'{s["from"]//1800:02}:{s["from"]//30%60:02} {s["title"]}' for s in scenes)+'\n');print('FULL FILM DELIVERY VERIFIED',flush=True)
