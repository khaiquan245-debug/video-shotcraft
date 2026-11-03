import wave
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parents[1]/'public/audio';sr=48000
with wave.open(str(root/'narration.wav')) as w:voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
with wave.open(str(root/'score.wav')) as w:score=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
clock=np.zeros_like(voice)
for off in list(range(0,10))+list(range(474,480)):
 n=int(.08*sr);t=np.arange(n)/sr
 tick=(np.sin(2*np.pi*1100*t)+.3*np.sin(2*np.pi*1650*t))*np.exp(-t*65)*.028
 clock[off*sr:off*sr+n]+=tick
fade=np.minimum(1,np.arange(len(score))/(sr*3))*np.minimum(1,(len(score)-np.arange(len(score)))/(sr*3));clock*=fade
for name,a in [('narration',voice+clock),('score',score-clock),('clock',clock)]:
 with wave.open(str(root/f'{name}.wav'),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((np.clip(a,-.98,.98)*32767).astype(np.int16).tobytes())
