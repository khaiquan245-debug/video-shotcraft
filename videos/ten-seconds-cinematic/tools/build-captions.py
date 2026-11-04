from pathlib import Path
import json,re
r=Path(__file__).resolve().parents[1];scenes=json.loads((r/'src/timeline.json').read_text());captions=[]
for sc in scenes:
 matches=list(re.finditer(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)?",sc['text']));assert len(matches)==len(sc['words'])
 lo=0
 while lo<len(matches):
  hi=lo+1
  while hi<len(matches) and hi-lo<6:
   segment=sc['text'][matches[lo].start():matches[hi].end()]
   tail=sc['text'][matches[hi-1].end():matches[hi].start()]
   if len(segment)>34 or (hi-lo>=2 and any(p in tail for p in '.?!')):break
   hi+=1
  a=matches[lo].start();b=matches[hi].start() if hi<len(matches) else len(sc['text'])
  text=sc['text'][a:b].strip();ws=sc['words'][lo:hi];start=sc['from']+ws[0]['from'];end=sc['from']+ws[-1]['to']+3
  captions.append({'id':len(captions),'chapter':sc['id'],'from':start,'duration':max(1,min(sc['from']+sc['duration'],end)-start),'text':text,'words':[{**w,'from':sc['from']+w['from']-start,'to':sc['from']+w['to']-start} for w in ws]});lo=hi
for a,b in zip(captions,captions[1:]):a['duration']=min(a['duration'],b['from']-a['from'])
assert all(c['duration']>0 for c in captions)
(r/'src/captions.json').write_text(json.dumps(captions,indent=2))
def stamp(n):
 ms=round(n/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(r/'out/ten-seconds-cinematic.en.srt').write_text('\n'.join(f'{i+1}\n{stamp(c["from"])} --> {stamp(c["from"]+c["duration"])}\n{c["text"]}\n' for i,c in enumerate(captions)))
print(len(captions),'short captions')
