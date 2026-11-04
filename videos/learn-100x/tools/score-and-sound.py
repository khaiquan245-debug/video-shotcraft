from pathlib import Path
import numpy as np,wave,json,subprocess,hashlib,re
r=Path(__file__).resolve().parents[1];o=r/'out';sr=48000;scenes=json.loads((r/'src/timeline.json').read_text());seconds=sum(s['duration'] for s in scenes)/30;N=round(seconds*sr)
run=lambda a:subprocess.run(a,capture_output=True,text=True,check=True)
raw=o/'narration-raw.wav'
measure=run(['ffmpeg','-hide_banner','-i',str(raw),'-af','loudnorm=I=-18:TP=-3:LRA=11:print_format=json','-f','null','-']).stderr;m=json.JSONDecoder().raw_decode(measure[measure.rfind('{'):])[0]
f=f'loudnorm=I=-18:TP=-3:LRA=11:measured_I={m["input_i"]}:measured_TP={m["input_tp"]}:measured_LRA={m["input_lra"]}:measured_thresh={m["input_thresh"]}:offset={m["target_offset"]}:linear=true'
run(['ffmpeg','-v','error','-y','-i',str(raw),'-af',f,'-ar',str(sr),str(o/'voice-leveled.wav')])
with wave.open(str(o/'voice-leveled.wav')) as w:voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768
voice=np.pad(voice[:N],(0,max(0,N-len(voice))));music=np.zeros(N,np.float32);fx=np.zeros(N,np.float32);rng=np.random.default_rng(100)
def add(dst,a,onset,gain=1):
 i=round(onset*sr);a=a.astype(np.float32)
 if i<0:a=a[-i:];i=0
 n=min(len(a),len(dst)-i)
 if n>0:dst[i:i+n]+=a[:n]*gain
def piano(freq,d=3):
 t=np.arange(round(sr*d))/sr;env=(1-np.exp(-t*110))*np.exp(-t*1.8)
 return ((np.sin(2*np.pi*freq*t)+.3*np.sin(2*np.pi*freq*2.003*t)*np.exp(-t*2)+.1*np.sin(2*np.pi*freq*3.01*t)*np.exp(-t*3))*env).astype(np.float32)
# Ten chapter cues, nine musical moods; shared motif, compatible harmony, overlap at cuts.
roots=[146.83,146.83,130.81,130.81,196.0,174.61,146.83,174.61,130.81,130.81];bpms=[88,84,106,112,102,104,78,86,68,64]
for sc in scenes:
 c=sc['id'];start=sc['from']/30;end=(sc['from']+sc['duration'])/30;beat=60/bpms[c];root=roots[c]
 chords=[[1,1.1892,1.4983],[.8909,1.1225,1.3348],[.7937,1,1.1892],[.8909,1.1225,1.3348]] if c in [0,1,6] else [[1,1.2599,1.4983],[.8909,1.1225,1.4983],[.7937,1,1.2599],[.7492,1.1225,1.3348]]
 for k,on in enumerate(np.arange(start,end,beat*(2 if c>=8 else 1))):
  chord=chords[(k//4)%4];freq=root*chord[k%3]*(2 if c>=8 else 1)
  a=piano(freq,3.8 if c>=8 else 2.6);edge=min(1,(on-start+.5)/2,(end-on+.5)/2)
  add(music,a,on,.022*edge if c>=8 else .012*edge)
  if k%4==0:
   tt=np.arange(4*sr)/sr;pad=sum(np.sin(2*np.pi*root*ratio*tt) for ratio in chord)*(1-np.exp(-tt*2))*np.exp(-tt*.8)
   add(music,pad,on,.0035*edge)
  if c in [2,3,5] and k%2==0:
   tt=np.arange(int(.18*sr))/sr;kick=np.sin(2*np.pi*(55*tt+18*(1-np.exp(-tt*20))/20))*np.exp(-tt*25);add(music,kick,on,.009*edge)
  if c in [2,3,4,5] and k%2:
   tt=np.arange(int(.055*sr))/sr;noise=rng.normal(0,1,len(tt));add(music,np.diff(noise,prepend=0)*np.exp(-tt*85),on,.0018*edge)
# Speech-responsive music ducking, smooth release; voice remains untouched.
env=np.abs(voice[::480]);env=np.convolve(env,np.ones(35)/35,'same');duck=(1-.7*np.clip(env/.022,0,1)).astype(np.float32);music*=np.repeat(duck,480)[:N]
for sc in scenes:
 for b in sc['beats']:
  if b['tag']=='zero' or (sc['id']==9 and b['tag']=='final'):
   i=round((sc['from']+b['from'])/30*sr);j=min(N,i+round(1.3*sr));music[i:j]*=.08
music*=np.minimum(1,np.arange(N,dtype=np.float32)/(sr*2))*np.minimum(1,(N-np.arange(N,dtype=np.float32))/(sr*4))
fxdir=r/'public/audio/sfx';fxdir.mkdir(parents=True,exist_ok=True)
def sound(kind):
 d={'typing':1.8,'paper':.65,'pencil':1.1,'vibrate':.9,'house':1.4,'news':1.6,'lab':1.3,'pianoWrong':.9}.get(kind,.4);t=np.arange(round(d*sr))/sr;noise=rng.normal(0,1,len(t));hp=np.diff(noise,prepend=0)
 if kind=='typing':
  a=np.zeros(len(t));
  for k in range(12):
   pos=round((.05+k*.13+(k%3)*.012)*sr);tt=np.arange(round(.035*sr))/sr;n=min(len(tt),len(a)-pos)
   if n>0:a[pos:pos+n]+=(rng.normal(0,1,n)*.45+np.sin(2*np.pi*(650+k*37)*tt[:n]))*np.exp(-tt[:n]*125)
 elif kind=='paper':a=hp*np.sin(np.pi*np.minimum(t/d,1))**2*(.45+.45*np.sin(t*53)**2)
 elif kind=='pencil':a=hp*(.15+.3*np.sin(t*23)**2)*np.minimum(1,t*50)*np.minimum(1,(d-t)*30)
 elif kind=='tick':a=(np.sin(2*np.pi*1600*t)+.4*hp)*np.exp(-t*150)
 elif kind=='clink' or kind=='house':a=sum(np.sin(2*np.pi*f*t)*np.exp(-t*(8+i*3)) for i,f in enumerate([1720,2790,4100]))
 elif kind=='shutter' or kind=='click':a=hp*np.exp(-t*115)+.4*np.roll(hp,round(.045*sr))*np.exp(-np.maximum(0,t-.045)*95)*(t>.045)
 elif kind=='vibrate':a=(np.sin(2*np.pi*145*t)+.2*noise)*np.exp(-t*1.5)*(np.sin(t*18)>0)
 elif kind=='kick' or kind=='impact':a=(np.sin(2*np.pi*(70*t+10*t*t))+.35*noise)*np.exp(-t*32)
 elif kind=='news' or kind=='lab':a=(np.sin(2*np.pi*220*t)*.2+np.convolve(noise,np.ones(25)/25,'same'))*np.sin(np.pi*t/d)**2
 elif kind=='pianoWrong':a=sum(piano(f,d) for f in [261.63,277.18,392])
 elif kind=='alarm':a=(np.sin(2*np.pi*780*t)+np.sin(2*np.pi*1040*t))*(np.sin(t*24)>0)*np.exp(-t*3)
 elif kind=='activation':a=(np.convolve(noise,np.ones(13)/13,'same')+np.sin(2*np.pi*(400*t+250*t*t))*.15)*np.sin(np.pi*t/d)**2
 else:a=(np.sin(2*np.pi*783.99*t)+.55*np.sin(2*np.pi*987.77*t))*np.exp(-t*12)*(1-np.exp(-t*150))
 a=np.asarray(a,np.float32);a*=.30/max(.00001,np.max(np.abs(a)));a[:72]*=np.linspace(0,1,72);a[-240:]*=np.linspace(1,0,240);return a
assets={};cues=[]
def get(kind):
 if kind in assets:return assets[kind]
 a=sound(kind);p=fxdir/f'original-{kind}.wav'
 with wave.open(str(p),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((a*32767).astype(np.int16).tobytes())
 # Peak location in10ms energy windows, for source-lag compensation.
 block=480;pad=np.pad(a,(0,(-len(a))%block));energy=np.mean(pad.reshape(-1,block)**2,axis=1);peak=int(np.argmax(energy))*block/sr
 assets[kind]=(a,peak,p);return assets[kind]
def cue(sc,b,kind,offset=0,gain=.10):
 a,lag,p=get(kind);target=(sc['from']+b['from']+offset)/30;on=target-lag;add(fx,a,on,gain);cues.append({'chapter':sc['id']+1,'tag':b['tag'],'source':str(p.relative_to(r/'public')),'actionPeakFrame':sc['from']+b['from']+offset,'sourcePeakLagSeconds':lag,'fromSeconds':max(0,on),'duration':len(a)/sr,'gain':gain,'originalSynthesis':True})
for sc in scenes:
 for b in sc['beats']:
  tag=b['tag'];c=sc['id']
  if c==0 and tag=='alarm':
   cue(sc,b,'alarm',38,.10)
   for off in [0,30,60,90]:cue(sc,b,'tick',off,.06)
  if c==0 and tag=='brain':cue(sc,b,'activation',0,.06)
  if c==1 and tag in ['learn','body','day','unknown']:cue(sc,b,'notification',0,.045)
  if (c==2 and tag in ['nextChapter','week']) or (c==4 and tag=='worldResearch'):cue(sc,b,'paper',10,.07)
  if c==2 and tag=='equation':cue(sc,b,'pencil',20,.07)
  if c==3 and tag in ['programming','web','apps']:cue(sc,b,'typing',20,.075)
  if c==3 and tag=='launch':cue(sc,b,'click',20,.08)
  if c==3 and tag=='orders':
   for off in [0,45,90]:cue(sc,b,'notification',off,.085)
  if c==3 and tag=='uncertainty':cue(sc,b,'impact',95,.07)
  if c==4 and tag=='pianoMistake':cue(sc,b,'pianoWrong',0,.10)
  if c==4 and tag=='miss':cue(sc,b,'kick',1,.10)
  if c==5 and tag in ['software','design']:cue(sc,b,'typing' if tag=='software' else 'pencil',15,.07)
  if c==6 and tag=='viral':cue(sc,b,'vibrate',4,.07);cue(sc,b,'notification',50,.06)
  if c==6 and tag=='attention':cue(sc,b,'news',0,.04)
  if c==6 and tag=='privacy':
   end=next((x['from'] for x in sc['beats'] if x['from']>b['from']),sc['duration'])
   for frame in range((b['from']//60+1)*60,end,60):cue(sc,b,'shutter',frame-b['from'],.075)
  if c==7 and tag in ['biology','prototype']:cue(sc,b,'lab',10,.045)
  if c==8 and tag in ['dinner','parents','brother']:cue(sc,b,'house' if tag=='dinner' else 'clink',10,.045)
  if c==8 and tag=='frustration':cue(sc,b,'pencil',0,.07)
  if c==9 and tag=='clock':
   end=next(x['from'] for x in sc['beats'] if x['from']>b['from'])
   for frame in range((b['from']//30+1)*30,end,30):cue(sc,b,'tick',frame-b['from'],.075)
music*=5.5
for name,a in [('voice',voice),('score',music),('sfx',fx),('narration-sfx',voice+fx),('master',voice+fx+music)]:
 peak=float(np.max(np.abs(a)));assert peak<.99,(name,peak)
 p=o/f'{name}-mix.wav'
 with wave.open(str(p),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((np.clip(a,-.99,.99)*32767).astype(np.int16).tobytes())
 run(['ffmpeg','-v','error','-y','-i',str(p),'-c:a','flac',str(r/f'public/audio/{name}.flac')]);print('MIXED',name,'peak',round(peak,3),flush=True)
(r/'src/sfx-cues.json').write_text(json.dumps(cues,indent=2))
manifest={'provenance':'Original procedural music and sound design for this production; no third-party samples. Foley effects are synthesis, not field recordings.','externalSearch':'Freesound keyboard search failed: proxy Tunnel403Forbidden. No alternate third-party recordings used.','sampleRate':sr,'scoreMoods':['curiosity','precise rules','playful learning','business rhythm','adventure','ambition','tension','hope','intimate piano','reflective piano and pads'],'speechDucking':'35-frame100Hz envelope; music attenuated under speech','files':[{'kind':k,'path':str(v[2].relative_to(r)),'sha256':hashlib.sha256(v[2].read_bytes()).hexdigest(),'peakLagSeconds':v[1]} for k,v in assets.items()],'cues':cues}
(o/'qa/audio-authorship.json').write_text(json.dumps(manifest,indent=2));(o/'qa/narration-loudness.json').write_text(json.dumps(m,indent=2));print('SCORE AND SOUND COMPLETE',len(cues),'cues',flush=True)
