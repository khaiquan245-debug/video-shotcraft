import json,textwrap
from pathlib import Path
root=Path(__file__).resolve().parents[1];p=root/'src/timeline.json';scenes=json.loads(p.read_text())
for sc in scenes:
 out=[]
 for c in sc['captions']:
  bits=textwrap.wrap(c['text'],width=78,break_long_words=False,break_on_hyphens=False)
  words=sum(len(x.split()) for x in bits);offset=0
  for i,txt in enumerate(bits):
   end=c['duration'] if i==len(bits)-1 else round(c['duration']*sum(len(x.split()) for x in bits[:i+1])/words)
   out.append({'text':txt,'from':c['from']+offset,'duration':end-offset});offset=end
 for a,b in zip(out,out[1:]):a['duration']=min(a['duration'],b['from']-a['from'])
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
