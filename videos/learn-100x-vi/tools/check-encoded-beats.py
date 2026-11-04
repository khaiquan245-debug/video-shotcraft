"""Extract evidence at every narrated beat and measure final mux audio offset."""
from pathlib import Path
import hashlib
import json
import math
import subprocess
import numpy as np

root=Path(__file__).resolve().parents[1]
out=root/'out';qa=out/'qa';movie=out/'learn-100x-vi.mp4'
scenes=json.loads((root/'src/timeline.json').read_text())
captions=json.loads((root/'src/captions.json').read_text())
rows=[]
for scene in scenes:
    for i,beat in enumerate(scene['beats']):
        end=scene['beats'][i+1]['from'] if i+1<len(scene['beats']) else scene['duration']
        frame=scene['from']+beat['from']+min(15,max(1,(end-beat['from'])//2))
        cap=next((c['text'] for c in captions if c['from']<=frame<c['from']+c['duration']),'')
        rows.append({'id':len(rows)+1,'chapter':scene['id']+1,'tag':beat['tag'],
                     'frame':frame,'narratedText':beat['phrase'],'visibleCaption':cap,
                     'file':f'encoded-beat-{len(rows)+1:03}.jpg'})
def balanced_sum(terms):
    # FFmpeg's expression parser has a depth limit; a linear 171-term sum exceeds it.
    if len(terms)==1:return terms[0]
    mid=len(terms)//2
    return f'({balanced_sum(terms[:mid])}+{balanced_sum(terms[mid:])})'

total=sum(s['duration'] for s in scenes)
endings=[]
for tag,frame in [('post-speech-hold',total-146),('fade-start',total-30),('last-frame',total-1)]:
    i=len(rows)+len(endings)+1
    endings.append({'id':i,'chapter':10,'tag':tag,'frame':frame,'file':f'encoded-beat-{i:03}.jpg'})
all_rows=rows+endings
expression=balanced_sum([f'eq(n,{r["frame"]})' for r in all_rows])
subprocess.run(['ffmpeg','-v','error','-y','-i',str(movie),'-an','-vf',f"select='{expression}'",
                '-fps_mode','vfr','-q:v','3','-frames:v',str(len(all_rows)),
                str(qa/'encoded-beat-%03d.jpg')],check=True)
assert all((qa/r['file']).is_file() for r in all_rows)
(qa/'encoded-beat-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(qa/'encoded-ending-index.json').write_text(json.dumps(endings,ensure_ascii=False,indent=2))
subprocess.run(['ffmpeg','-v','error','-y','-framerate','1','-i',str(qa/'encoded-beat-%03d.jpg'),
                '-vf',"scale=384:216,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='evidence %{n}':start_number=1:fontcolor=white:fontsize=16:box=1:boxcolor=black@0.8:x=5:y=5,tile=5x5:nb_frames=25",
                '-frames:v',str(math.ceil(len(all_rows)/25)),'-q:v','3',str(qa/'encoded-contact-%02d.jpg')],check=True)

def samples(path):
    result=subprocess.run(['ffmpeg','-v','error','-i',str(path),'-t','12','-map','0:a:0',
                           '-ar','48000','-ac','1','-f','f32le','-'],check=True,capture_output=True)
    return np.frombuffer(result.stdout,np.float32).astype(np.float64)

source=samples(root/'public/audio/master.flac');encoded=samples(movie)
n=min(len(source),len(encoded));source=source[:n];encoded=encoded[:n]
size=1<<int(math.ceil(math.log2(2*n)))
correlation=np.fft.irfft(np.fft.rfft(encoded,size)*np.conj(np.fft.rfft(source,size)),size)
limit=round(.2*48000);window=np.r_[correlation[-limit:],correlation[:limit+1]]
lag=int(np.argmax(window))-limit
normalized=float(window.max()/np.sqrt(np.sum(source*source)*np.sum(encoded*encoded)))
assert abs(lag)/48000*30<=1, 'Encoded mux shifted narration by more than one video frame'
assert normalized>.95, 'Encoded audio does not closely match the intended mix'
report={'encodedNarrativeBeatFrames':len(rows),'encodedEndingEvidenceFrames':len(endings),'audioOffsetSamples':lag,
        'audioOffsetMilliseconds':lag/48,'audioOffsetFramesAt30fps':lag/48000*30,
        'first12SecondsCorrelationWithIntendedMix':normalized,
        'method':'FFT cross-correlation of decoded final AAC against intended 48kHz master; plus actual encoded frames for all 171 narrative beats',
        'movieSha256':hashlib.sha256(movie.read_bytes()).hexdigest()}
(qa/'encoded-alignment-evidence.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
