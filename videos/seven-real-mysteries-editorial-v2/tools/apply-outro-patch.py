from pathlib import Path
import json,subprocess
r=Path(__file__).resolve().parents[1];d=json.loads((r/'src/timeline.json').read_text());p=json.loads((r/'out/outro-patch.json').read_text());start=p['from']/30;end=p['to']/30
filt=f"[1:v]setpts=PTS-STARTPTS+{start:.12f}/TB,scale=in_range=full:out_range=tv,format=yuv420p[p];[0:v][p]overlay=x=0:y=0:eof_action=pass:repeatlast=0:enable='gte(t,{start:.12f})*lt(t,{end:.12f})',format=yuv420p[v]"
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'out/limited.mp4'),'-i',str(r/'out/outro-patch-pc.mp4'),'-filter_complex',filt,'-map','[v]','-an','-c:v','libx264','-preset','fast','-crf','18','-r','30','-frames:v',str(d['frames']),'-color_range','tv','-movflags','+faststart',str(r/'out/corrected-picture.mp4')],check=True)
for stem,name in [('master','7_real_mysteries_v2'),('no-music','7_real_mysteries_v2_no_music')]:
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'out/corrected-picture.mp4'),'-i',str(r/f'public/audio/{stem}.wav'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-t',str(d['frames']/30),'-movflags','+faststart',str(r/f'output/{name}.mp4')],check=True)
(r/'output/outro_map_correction.json').write_text(json.dumps({'correctedSource':'src/Art.tsx: Map treats chapter8callback as IndianOcean geography','globalFrames':[p['from'],p['to']-1],'fullFinalVideoReencoded':True,'narrationUnchanged':True,'subtitleClockUnchanged':True},indent=2));print('FINAL OUTRO MAP CORRECTED',flush=True)
