from pathlib import Path
import numpy as np,wave,json,subprocess,hashlib,math,shutil
r=Path(__file__).resolve().parents[1];s=json.loads((r/'src/timeline.json').read_text());sr=48000;seconds=sum(x['duration'] for x in s)/30;N=round(seconds*sr);score=np.zeros((N,2),np.float64);rng=np.random.default_rng(1964)
def hz(note):return 440*2**((note-69)/12)
def put(at,a,pan=0):
 start=round(at*sr)
 if start<0:a=a[-start:];start=0
 n=min(len(a),N-start)
 if n<=0:return
 angle=(pan+1)*np.pi/4;score[start:start+n,0]+=a[:n]*np.cos(angle);score[start:start+n,1]+=a[:n]*np.sin(angle)
def note(at,midi,dur,amp,kind='piano',pan=0):
 n=round(dur*sr);t=np.arange(n)/sr;f=hz(midi);a=np.zeros(n)
 if kind=='piano':
  for harmonic,level,decay in [(1,1,1.8),(2,.24,1.25),(3,.1,.8),(4,.045,.5)]:a+=level*np.sin(2*np.pi*f*harmonic*t)*np.exp(-t/decay)
  a*=1-np.exp(-t*110)
 elif kind=='bell':
  for h,l in [(1,1),(2.008,.27),(3.005,.12),(4.16,.035)]:a+=l*np.sin(2*np.pi*f*h*t)*np.exp(-t/(2.0/h**.3))
  a*=1-np.exp(-t*55)
 elif kind=='pad':
  for detune in [-.0016,.0014]:
   for h,l in [(1,.6),(2,.16),(3,.045)]:a+=l*np.sin(2*np.pi*f*(1+detune)*h*t+detune*100)
  a*=(np.minimum(1,t/.7)*np.minimum(1,(dur-t)/1.1))*(.93+.07*np.sin(t*2.1))
 elif kind=='bass':a=np.sin(2*np.pi*f*t)*np.minimum(1,t/.12)*np.exp(-t/1.5)
 a*=np.minimum(1,(dur-t)/.09);put(at,a*amp,pan)
# An original E-minor/add9 motif, built locally; no third-party recording or tune.
beat=60/72;bar=beat*4;chords=[[52,59,66,67],[48,55,62,67],[45,52,59,64],[47,54,59,64]]
for b in range(math.ceil(seconds/bar)):
 at=b*bar;chord=chords[b%4];reveal=at>=s[5]['from']/30;clue=s[4]['from']/30<=at<s[5]['from']/30
 if reveal:chord=[[52,59,64,66],[48,55,62,64],[47,54,59,66]][(b-10)%3]
 for j,n in enumerate(chord):note(at,n,bar+1.4,.032 if not clue else .019,'pad',[-.7,.65,-.35,.35][j])
 note(at,chord[0]-12,2.8,.055 if not clue else .025,'bass')
 if at<s[1]['from']/30:notes=[(0,74), (2.5,69)]
 elif at<s[2]['from']/30:notes=[(0,chord[0]+24),(1.5,chord[1]+12),(3,chord[2]+12)]
 elif at<s[4]['from']/30:notes=[(0,64),(1,71),(2,78),(3,67 if b%2 else 76)]
 elif clue:notes=[(.5,77),(2.5,74)]
 else:notes=[(0,chord[2]+12),(1.5,chord[1]+12),(3,74)]
 for k,(t,n) in enumerate(notes):note(at+t*beat,n,2.6,.068 if not clue else .048,'piano',(-.28 if k%2==0 else .3))
# Suspense pulse confined to discovery/worldwide-attention passages; sparse, soft.
start=s[2]['from']/30;stop=s[4]['from']/30
for at in np.arange(start,stop,beat):
 note(float(at),38,.52,.022,'bass');note(float(at+beat*.5),57,.8,.014,'piano',.45)
# Small harmonic turning points tied to the actual edit, not fixed old timestamps.
for at,n in [(s[4]['from']/30+.12,86),(s[5]['from']/30+.12,81)]:note(at,n,2.9,.046,'bell',.25)
# Fade and one subtle breath before the final tentative mother reveal.
t=np.arange(N)/sr;fade=np.minimum(1,t/.4)*np.minimum(1,(seconds-t)/1.7);score*=fade[:,None]
mother=next(w['from']/30 for w in s[5]['words'] if w['text']=='nobody');dip=1-.82*np.exp(-((t-(mother-.1))/.14)**4);score*=dip[:,None]
peak=np.max(abs(score));score*=.78/max(peak,1e-8)
def save(p,a):
 with wave.open(str(p),'wb') as w:w.setparams((2,2,sr,0,'NONE','not compressed'));w.writeframes((np.clip(a,-.999,.999)*32767).astype(np.int16).tobytes())
save(r/'output/dyatlov_pass_music.wav',score);save(r/'public/audio/score.wav',score)
with wave.open(str(r/'public/audio/narration-sfx.wav')) as w:base=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float64)/32768
with wave.open(str(r/'public/audio/narration.wav')) as w:voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float64)/32768
assert len(base)==N==len(voice)
def smooth(a,n):
 c=np.concatenate(([0.0],np.cumsum(a)));v=(c[n:]-c[:-n])/n;return np.pad(v,(n//2,len(a)-len(v)-n//2),mode='edge')
duck=smooth(1-.55*np.clip(smooth(abs(voice),2400)/.025,0,1),4800);mix=base[:,None]+score*.14*duck[:,None];assert abs(mix).max()<.98
save(r/'public/audio/master.wav',mix)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'output/dyatlov_pass_music.wav'),'-c:a','libmp3lame','-b:a','256k',str(r/'output/dyatlov_pass_music.mp3')],check=True)
(r/'output/music_report.json').write_text(json.dumps({'seconds':seconds,'sampleRate':sr,'channels':2,'tempoBpm':72,'tonalCenter':'E minor/add9','composition':'Original procedural cinematic score; no third-party samples or melody references','layers':['felt-piano motif','detuned soft pads','round bass pulse','discovery glass tones'],'standalonePeak':float(abs(score).max()),'mixedPeak':float(abs(mix).max()),'musicGain':.14,'voiceDucking':True,'narrationSourceUnchanged':True,'narrationWavSha256':hashlib.sha256((r/'output/dyatlov_pass_voice.wav').read_bytes()).hexdigest()},indent=2))
print('COMPOSED',seconds,'MIX PEAK',float(abs(mix).max()),flush=True)


