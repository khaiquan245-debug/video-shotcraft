from pathlib import Path
import numpy as np,wave,json,subprocess,math
r=Path(__file__).resolve().parents[1];d=json.loads((r/'src/timeline.json').read_text());shots=json.loads((r/'src/shots.json').read_text());sr=48000;N=d['frames']*1600;score=np.zeros((N,2),np.float32);fx=np.zeros(N,np.float32);rng=np.random.default_rng(1977)
def put(at,a,pan=0):
 j=round(at*sr);n=min(len(a),N-j)
 if n<=0:return
 score[j:j+n,0]+=a[:n]*np.sqrt((1-pan)/2);score[j:j+n,1]+=a[:n]*np.sqrt((1+pan)/2)
def note(at,midi,dur,amp,kind='piano',pan=0):
 t=np.arange(round(dur*sr),dtype=np.float32)/sr;f=440*2**((midi-69)/12)
 if kind=='pad':
  a=(np.sin(2*np.pi*f*.999*t)+np.sin(2*np.pi*f*1.001*t))*.5+.15*np.sin(2*np.pi*f*2*t);a*=np.minimum(1,t/.8)*np.minimum(1,(dur-t)/1.2)
 elif kind=='pulse':a=np.sin(2*np.pi*f*t)*np.exp(-t*6)*(1-np.exp(-t*60))
 elif kind=='bell':a=(np.sin(2*np.pi*f*t)+.2*np.sin(2*np.pi*f*2.007*t))*np.exp(-t/1.4)*(1-np.exp(-t*120))
 else:a=(np.sin(2*np.pi*f*t)+.22*np.sin(2*np.pi*f*2*t)*np.exp(-t*2)+.08*np.sin(2*np.pi*f*3*t))*np.exp(-t/1.9)*(1-np.exp(-t*80))
 a*=np.minimum(1,(dur-t)/.1);put(at,a*amp,pan)
profiles=[(72,52,'radio'),(72,52,'radio'),(64,57,'parchment'),(82,50,'mechanical'),(66,52,'cold'),(74,48,'airburst'),(84,52,'investigation'),(60,57,'ocean'),(66,52,'reflection')]
for ch in d['chapters']:
 cid=ch['id'];start=ch['from']/30;end=(ch['from']+ch['duration'])/30;bpm,root,theme=profiles[cid];beat=60/bpm;bar=beat*4
 for b,at in enumerate(np.arange(start,end,bar)):
  chord=[[0,7,14,15],[-4,3,10,15],[-7,0,7,12],[-5,2,7,12]][b%4]
  for k,n in enumerate(chord):note(float(at),root+n,bar+1.3,.016 if cid==8 else .019 if cid in [4,7] else .025,'pad',[-.65,.65,-.3,.3][k])
  pattern={0:[(0,24),(2,19)],1:[(0,24),(2.5,26)],2:[(.5,19),(2.5,15)],3:[(0,12),(1,19),(2.5,24)],4:[(.5,15),(3,14)],5:[(0,12),(2.5,19)],6:[(0,19),(1.5,24),(3,22)],7:[(.5,19)],8:[(0,24),(2,19),(3,15)]}[cid]
  for k,(bt,n) in enumerate(pattern):note(float(at+bt*beat),root+n,2.6,.024 if cid==8 else .032 if cid==7 else .047,'bell' if cid==1 else 'piano',(-.25 if k%2 else .25))
  if cid in [0,3,5,6]:
   for k in range(4):note(float(at+k*beat),root-12,.7,.026 if k%2==0 else .014,'pulse')
# Original procedural ambience/effects, each pinned to actual visual shot timing.
def add(at,a):
 j=round(at*sr);n=min(len(a),N-j)
 if n>0:fx[j:j+n]+=a[:n]
def noise(seconds,amp,seed):
 z=np.random.default_rng(seed).normal(0,1,round(seconds*sr)).astype(np.float32);kernel=np.ones(81,np.float32)/81;return np.convolve(z,kernel,mode='same')*amp
for ch in d['chapters']:
 start=ch['from']/30;dur=ch['duration']/30;n=round(dur*sr);tt=np.arange(n,dtype=np.float32)/sr
 if ch['id'] in [0,1]:amb=noise(dur,.010,100+ch['id'])+.0008*np.sin(2*np.pi*102*tt)
 elif ch['id']==4:amb=noise(dur,.034,104)*(.6+.4*np.sin(tt*.6)**2)
 elif ch['id'] in [6,7]:amb=noise(dur,.014,100+ch['id'])+.0013*np.sin(2*np.pi*(48 if ch['id']==6 else 38)*tt)
 else:amb=noise(dur,.004,100+ch['id'])
 amb*=np.minimum(1,tt/.35)*np.minimum(1,(dur-tt)/.35);add(start,amb)
cues=[]
for s in shots:
 if s['variant']!=0:continue
 at=s['from']/30+.15;kind=s['type'];dur=s['duration']/30
 if kind=='print':
  tt=np.arange(round(.45*sr))/sr;a=np.random.default_rng(700+s['id']).normal(0,.010,len(tt))*np.exp(-tt*12);a+=np.sin(2*np.pi*140*tt)*.01*np.exp(-tt*18);add(at,a);cues.append({'shot':s['id'],'at':at,'effect':'original printer mechanism'})
 elif kind in ['book','parchment','glyphs','page_botanical','page_stars','page_text','word_detail']:
  a=noise(.32,.026,900+s['id'])*np.sin(np.pi*np.arange(round(.32*sr))/(.32*sr))**2;add(at,a);cues.append({'shot':s['id'],'at':at,'effect':'original paper movement'})
 elif kind in ['gears','gearmacro','gear']:
  tt=np.arange(round(.09*sr))/sr;a=(np.sin(2*np.pi*1200*tt)*.008+np.sin(2*np.pi*2100*tt)*.003)*np.exp(-tt*65)
  for b in np.arange(0,max(.1,dur-.3),(5/3)):add(at+float(b),a)
  cues.append({'shot':s['id'],'at':at,'effect':'original mechanical ticks'})
 elif kind=='airburst' and not any(c['effect']=='original restrained airburst' for c in cues):
  tt=np.arange(sr*2)/sr;a=np.sin(2*np.pi*(58-12*tt)*tt)*.07*np.exp(-tt*3)+noise(2,.06,1908)*np.exp(-tt*2);add(at,a);cues.append({'shot':s['id'],'at':at,'effect':'original restrained airburst'})
 elif kind=='sonar':
  tt=np.arange(round(.8*sr))/sr;add(at,np.sin(2*np.pi*690*tt)*.008*np.exp(-tt*7)*(1-np.exp(-tt*100)));cues.append({'shot':s['id'],'at':at,'effect':'original quiet sonar pulse'})
 # Soft designed tonal chapter accents, not explosive jumps.
 if s['from']==d['chapters'][s['chapter']]['from']:
  tt=np.arange(sr)/sr;add(at,np.sin(2*np.pi*(52-10*tt)*tt)*.025*np.exp(-tt*8))
t=np.arange(N,dtype=np.float32)/sr;secs=N/sr;score*=np.minimum(1,t/.6)[:,None]*np.minimum(1,(secs-.6-t)/2).clip(0,1)[:,None];fx*=np.minimum(1,(secs-.6-t)/.5).clip(0,1)
score*=.70/max(.01,float(abs(score).max()))
def save(p,a):
 channels=1 if a.ndim==1 else a.shape[1]
 with wave.open(str(p),'wb') as w:w.setparams((channels,2,sr,0,'NONE','not compressed'));w.writeframes((np.clip(a,-.99,.99)*32767).astype(np.int16).tobytes())
save(r/'output/7_real_mysteries_v2_music.wav',score)
with wave.open(str(r/'public/audio/narration.wav')) as w:voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
assert len(voice)==N
def smooth(a,n):
 c=np.concatenate(([0.0],np.cumsum(a,dtype=np.float64)));v=(c[n:]-c[:-n])/n;return np.pad(v,(n//2,len(a)-len(v)-n//2),mode='edge').astype(np.float32)
duck=smooth(1-.58*np.clip(smooth(abs(voice),2400)/.023,0,1),4800);base=voice+fx;master=base[:,None]+score*.10*duck[:,None];assert abs(master).max()<.98
save(r/'out/master-raw.wav',master);save(r/'out/no-music-raw.wav',base)
# Two-pass final loudness normalization; preserve measured dynamics.
measures={}
for name in ['master','no-music']:
 p=r/f'out/{name}-raw.wav';res=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-af','loudnorm=I=-16:TP=-1.5:LRA=9:print_format=json','-f','null','-'],capture_output=True,text=True,check=True);m=json.JSONDecoder().raw_decode(res.stderr[res.stderr.rfind('{'):])[0];filt=f"loudnorm=I=-16:TP=-1.5:LRA=9:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true"
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(p),'-af',filt,'-ar','48000',str(r/f'public/audio/{name}.wav')],check=True);measures[name]=m
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'output/7_real_mysteries_v2_music.wav'),'-c:a','libmp3lame','-b:a','192k',str(r/'output/7_real_mysteries_v2_music.mp3')],check=True)
(r/'output/sfx_cues.json').write_text(json.dumps(cues,indent=2));(r/'output/music_report.json').write_text(json.dumps({'seconds':secs,'original':True,'thirdPartySamples':False,'chapterProfiles':profiles,'musicGain':.10,'voiceDucking':True,'finalLoudnessTargetLUFS':-16,'truePeakTargetDBTP':-1.5,'normalizationMeasurements':measures},indent=2));print('SCORE COMPLETE',secs,flush=True)
