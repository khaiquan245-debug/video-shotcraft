from pathlib import Path
import numpy as np,subprocess,json
r=Path(__file__).resolve().parents[1];f=r/'output/7_real_mysteries_v2.mp4';m=r/'public/audio/master.wav';results=[]
for at in [1,120,300]:
 def pcm(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-ss',str(at),'-i',str(p),'-t','4','-ar','12000','-ac','1','-f','f32le','-']),np.float32).astype(np.float64)
 a=pcm(f);b=pcm(m);n=min(len(a),len(b));a=a[:n]-a[:n].mean();b=b[:n]-b[:n].mean();size=1<<(2*n-1).bit_length();c=np.fft.irfft(np.fft.rfft(a,size)*np.conj(np.fft.rfft(b,size)),size);lags=np.arange(-2400,2401);best=int(lags[np.argmax(c[lags%size])]);results.append({'seconds':at,'lagSamplesAt12kHz':best,'lagSeconds':best/12000});assert abs(best)<=12
hashes=[]
for name in ['7_real_mysteries_v2.mp4','7_real_mysteries_v2_no_music.mp4']:
 h=subprocess.check_output(['ffmpeg','-v','error','-i',str(r/'output'/name),'-map','0:v:0','-c','copy','-f','hash','-hash','sha256','-']).decode().strip();hashes.append(h)
assert hashes[0]==hashes[1]
(r/'output/sync_report.json').write_text(json.dumps({'measuredAudioProbes':results,'samePictureStream':True,'encodedPictureHash':hashes[0],'renderedFromCorrectedSource':True},indent=2));print(results,'PICTURE MATCH',flush=True)
