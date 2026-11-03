from pathlib import Path
import json,math
root=Path(__file__).resolve().parents[1];p=root/'src/timeline.json';scenes=json.loads(p.read_text())
for sc in scenes:
 groups=[]
 for c in sc['captions']:
  if groups and groups[-1]['from']+groups[-1]['duration']==c['from']:
   groups[-1]['text']+=' '+c['text'];groups[-1]['duration']+=c['duration']
  else:groups.append(dict(c))
 out=[]
 for c in groups:
  n=math.ceil(len(c['text'])/78);words=c['text'].split();N=len(words);base=0
  for i in range(n):
   lo=round(i*N/n);hi=round((i+1)*N/n);end=round(c['duration']*hi/N)
   out.append({'text':' '.join(words[lo:hi]),'from':c['from']+base,'duration':end-base});base=end
 sc['captions']=out
p.write_text(json.dumps(scenes,indent=2))
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
lines=[]
for sc in scenes:
 for c in sc['captions']:
  start=(sc['from']+c['from'])/30;end=start+c['duration']/30
  lines.append(f'{len(lines)+1}\n{stamp(start)} --> {stamp(end)}\n{c["text"]}\n')
(root/'out/ten-seconds.en.srt').write_text('\n'.join(lines))
print('captions',len(lines),'minimum cue seconds',min(c['duration'] for s in scenes for c in s['captions'])/30)
