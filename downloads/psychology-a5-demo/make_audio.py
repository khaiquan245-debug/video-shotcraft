import numpy as np, wave, json
from pathlib import Path
from scipy.signal import resample_poly
p=Path(__file__).parent; sr=48000;n=sr*30;rng=np.random.default_rng(29);music=np.zeros(n);fx=np.zeros(n);voice=np.zeros(n)
def add(dst,a,t,g=1):
 i=int(t*sr);m=min(len(a),len(dst)-i)
 if m>0:dst[i:i+m]+=a[:m]*g
def tone(freq,dur):
 t=np.arange(int(dur*sr))/sr
 return (np.sin(2*np.pi*freq*t)+.27*np.sin(4*np.pi*freq*t))*np.exp(-t*3.6)*(1-np.exp(-t*150))
for j in range(60):
 f=[220,277.18,329.63,440,329.63,277.18,246.94,329.63][j%8];add(music,tone(f,1.5),j*.5,.021)
for t in [3.8,10.4,12.8,22.6,25.9]:
 x=np.arange(int(.18*sr))/sr;a=(rng.normal(0,1,len(x))*.12+np.sin(2*np.pi*320*x)) *np.exp(-x*38);add(fx,a,t,.045)
for t in [1.2,8.5,18.2,27.4]:
 x=np.arange(int(.32*sr))/sr;add(fx,np.sin(2*np.pi*(1800*x+250*x*x))*np.sin(np.pi*x/.32)**2,t,.009)
for part,start in zip(json.loads((p/'narration-parts.json').read_text()),[.25,10.15,20.15]):
 with wave.open(str(p/part['file'])) as w:a=np.frombuffer(w.readframes(w.getnframes()),dtype='<i2').astype(float)/32768;rate=w.getframerate()
 a=resample_poly(a,320,147) if rate==22050 else resample_poly(a,sr,rate)
 a*=.65/max(np.max(abs(a)),.01);add(voice,a,start)
# Original synthesized plucked-string music and effects; no external recordings.
mix=voice+music+fx;fade=np.minimum(np.arange(n)/24000,1)*np.minimum(np.arange(n)[::-1]/48000,1);mix*=fade
st=np.stack([mix,mix*.995],axis=1);st=np.clip(st,-.98,.98)
with wave.open(str(p/'output/mix.wav'),'wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((st*32767).astype('<i2').tobytes())
