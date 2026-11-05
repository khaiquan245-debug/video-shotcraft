from pathlib import Path
import wave,numpy as np,subprocess,json
r=Path(__file__).resolve().parents[1];sr=48000;N=60*sr;t=np.arange(N)/sr;rng=np.random.default_rng(1977)
voice=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(r/'out/narration.wav'),'-ar',str(sr),'-f','s16le','-']),np.int16).astype(np.float32)/32768
music=(np.sin(2*np.pi*55*t)+.5*np.sin(2*np.pi*82.4069*t)+.3*np.sin(2*np.pi*110.11*t))*.014
music*=np.minimum(1,t/3)*np.minimum(1,(60-t)/3)
fx=rng.normal(0,1,N).astype(np.float32)*.0015
for when in [1.2,4.0,8.2,11,20,29,41,43,47,52,56]:
 i=int(when*sr);tt=np.arange(int(.4*sr))/sr;a=np.sin(2*np.pi*(950+130*np.sin(tt*18))*tt)*np.exp(-tt*10)*.025;fx[i:i+len(a)]+=a
for i in range(30,52):
 start=int(i*sr);tt=np.arange(int(.09*sr))/sr;fx[start:start+len(tt)]+=rng.normal(0,1,len(tt))*.01*np.exp(-tt*40)
a=voice+music+fx;assert np.max(np.abs(a))<.99
with wave.open(str(r/'public/audio/master.wav'),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((a*32767).astype(np.int16).tobytes())

with wave.open(str(r/'public/audio/narration-sfx.wav'),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes(((voice+fx)*32767).astype(np.int16).tobytes())
print('MIX',len(a)/sr,float(np.abs(a).max()))
