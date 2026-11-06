from pathlib import Path
import json,wave,hashlib
import numpy as np
r=Path(__file__).resolve().parents[1];backup=r/'out/before-motion-redo';backup.mkdir(exist_ok=True);s=json.load(open(r/'src/timeline.json'))
with wave.open(str(r/'public/audio/narration.wav')) as w:sr=w.getframerate();voice=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float64)/32768
cues=[next(w['from']/30 for w in s[0]['words'] if w['text']=='grabbed'),next(w['from']/30 for w in s[4]['words'] if w['text']=='moved')]
for stem in ['master','narration-sfx']:
 p=r/f'public/audio/{stem}.wav';b=backup/f'{stem}.wav'
 if not b.exists():b.write_bytes(p.read_bytes())
 with wave.open(str(b)) as w:a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float64)/32768
 for at in cues:
  lo,hi=round((at-.22)*sr),round(at*sr);envelope=np.zeros(hi-lo);ramp=round(.008*sr);envelope[:ramp]=np.linspace(1,0,ramp);envelope[-ramp:]=np.linspace(0,1,ramp);a[lo:hi]=voice[lo:hi]+(a[lo:hi]-voice[lo:hi])*envelope
  t=np.arange(round(.65*sr))/sr;hit=(np.sin(2*np.pi*(54-15*t)*t)*.065+np.sin(2*np.pi*116*t)*.016)*np.exp(-t*11);a[hi:hi+len(hit)]+=hit
 # Very quiet moving-water / metal pulse under the evolving cabin, always below narration.
 rng=np.random.default_rng(62);lo=s[2]['from']*1600;hi=(s[3]['from'])*1600;t=np.arange(hi-lo)/sr;a[lo:hi]+=np.sin(2*np.pi*(73+2*np.sin(t*1.4))*t)*.004*np.sin(t*.7)**2
 silence=json.load(open(r/'output/audio-cues.json'))['silenceBeforeHarrison'];a[round(silence[0]*sr):round(silence[1]*sr)]=0
 assert abs(a).max()<.98
 with wave.open(str(p),'wb') as w:w.setparams((1,2,sr,0,'NONE','not compressed'));w.writeframes((a*32767).astype(np.int16).tobytes())
def ts(f):
 ms=round(f/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
cues=[]
for sc in s:
 i=0
 while i<len(sc['words']):
  end=next(b for b in sc['breaks'] if b>=i);n=min(2,end-i+1);ws=sc['words'][i:i+n];i+=n;cues.append(f"{len(cues)+1}\n{ts(ws[0]['from'])} --> {ts(ws[-1]['to'])}\n"+' '.join(w['text'] for w in ws)+'\n')
(r/'output/harrison_okene_subtitles.srt').write_text('\n'.join(cues));(r/'output/motion-revision.json').write_text(json.dumps({'narrationSha256':hashlib.sha256((r/'output/harrison_okene_voice.wav').read_bytes()).hexdigest(),'scriptSha256':hashlib.sha256((r/'script.json').read_bytes()).hexdigest(),'captionPixels':82,'captionWordsPerCue':2,'gripMusicDipsSeconds':[.22,.22],'rightsClearedArchivePresent':False},indent=2))
