"""Force-align the approved recording; retime captions without changing audio."""
from pathlib import Path
import json,re,subprocess,hashlib,math
from pocketsphinx import Decoder
root=Path(__file__).resolve().parents[1]
scenes=json.loads((root/'src/timeline.json').read_text())
manifest=json.loads((root/'out/smooth-voice-manifest.json').read_text())
token=re.compile(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)?")
def words(text):return [x.lower().replace('’',"'").replace('10','ten') for x in token.findall(text)]
decoder=Decoder(lm=None,loglevel='ERROR',samprate=16000,beam=1e-80,wbeam=1e-60)
report=[]
for sc,source in zip(scenes,manifest):
 pos=.45 if sc['id']==0 else .20
 aligned=[]
 for j,p in enumerate(source['paragraphs']):
  path=root/p['path']
  pcm=subprocess.run(['ffmpeg','-v','error','-i',str(path),'-f','s16le','-ar','16000','-ac','1','-'],capture_output=True,check=True).stdout
  expected=words(p['text']);decoder.set_align_text(' '.join(expected));decoder.start_utt();decoder.process_raw(pcm,False,True);decoder.end_utt()
  seg=[s for s in decoder.seg() if s.word not in ['<sil>','<s>','</s>','[NOISE]']]
  assert [re.sub(r'\(\d+\)$','',s.word) for s in seg]==expected,(sc['id'],j,[s.word for s in seg],expected)
  for s in seg:
   aligned.append({'word':re.sub(r'\(\d+\)$','',s.word),'from':round((pos+s.start_frame/100)*30),'to':round((pos+(s.end_frame+1)/100)*30)})
  report.append({'chapter':sc['id']+1,'paragraph':j+1,'words':len(seg),'audioSHA256':hashlib.sha256(path.read_bytes()).hexdigest(),'firstWord':seg[0].start_frame/100,'lastWordEnd':(seg[-1].end_frame+1)/100,'audioSeconds':p['seconds']})
  pos+=p['seconds']+(.18 if sc['id']<8 else .24)
 assert words(sc['text'])==[x['word'] for x in aligned]
 sc['words']=aligned
 cursor=0
 for c in sc['captions']:
  n=len(words(c['text']));selected=aligned[cursor:cursor+n]
  assert words(c['text'])==[x['word'] for x in selected]
  c['from']=selected[0]['from'];c['duration']=max(1,min(sc['duration'],selected[-1]['to']+3)-c['from']);cursor+=n
 for a,b in zip(sc['captions'],sc['captions'][1:]):a['duration']=min(a['duration'],b['from']-a['from'])
 assert all(c['duration']>0 for c in sc['captions'])
 print('FORCE ALIGNED',sc['id']+1,len(aligned),'words',flush=True)
(root/'src/timeline.json').write_text(json.dumps(scenes,indent=2))
(root/'out/qa/word-alignment.json').write_text(json.dumps({'method':'PocketSphinx 5.0.4 acoustic forced word alignment, 16 kHz, 10 ms acoustic frames','audioChanged':False,'paragraphs':report},indent=2))
def stamp(frame):
 ms=round(frame/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
lines=[]
for s in scenes:
 for c in s['captions']:lines.append(f'{len(lines)+1}\n{stamp(s["from"]+c["from"])} --> {stamp(s["from"]+c["from"]+c["duration"])}\n{c["text"]}\n')
(root/'out/ten-seconds-smooth.en.srt').write_text('\n'.join(lines))
