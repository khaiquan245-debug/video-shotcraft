from pathlib import Path
import json,math,re,csv
r=Path(__file__).resolve().parents[1];t=json.loads((r/'src/timeline.json').read_text());plan=json.loads((r/'src/shotplan.json').read_text());shots=[]
for ch,items in zip(t['chapters'],plan):
 ws=ch['words'];text=[w['text'] for w in ws];last=0;anchors=[]
 for n,(trigger,kind,title,detail) in enumerate(items):
  tokens=re.findall(r"[a-z]+(?:'[a-z]+)?",trigger.lower());pos=next((i for i in range(last,len(text)-len(tokens)+1) if text[i:i+len(tokens)]==tokens),None)
  if pos is None:raise RuntimeError((ch['id'],trigger,'not found',last))
  frame=ch['from'] if n==0 else ws[pos]['from'];anchors.append({'chapter':ch['id'],'type':kind,'title':title,'detail':detail,'from':frame,'anchor':trigger});last=pos+len(tokens)
 for i,a in enumerate(anchors):
  end=anchors[i+1]['from'] if i+1<len(anchors) else ch['from']+ch['duration'];dur=end-a['from'];parts=max(1,math.ceil(dur/30/5.3))
  for j in range(parts):
   start=a['from']+round(dur*j/parts);stop=a['from']+round(dur*(j+1)/parts);shots.append({**a,'from':start,'duration':stop-start,'variant':j,'id':len(shots)})
assert shots[0]['from']==0 and shots[-1]['from']+shots[-1]['duration']==t['frames']
(r/'src/shots.json').write_text(json.dumps(shots,indent=2))
with (r/'STORYBOARD.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['id','chapter','from_seconds','to_seconds','scene','headline','detail','spoken_anchor']);w.writerows([[s['id'],s['chapter'],s['from']/30,(s['from']+s['duration'])/30,s['type'],s['title'],s['detail'],s['anchor']] for s in shots])
print('SHOTS',len(shots),'FRAMES',t['frames'],'SECONDS',t['frames']/30)
