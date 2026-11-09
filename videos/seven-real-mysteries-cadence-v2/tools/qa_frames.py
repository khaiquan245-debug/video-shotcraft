from pathlib import Path
import subprocess,json
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).resolve().parents[1];d=json.loads((r/'src/timeline.json').read_text());shots=json.loads((r/'src/shots.json').read_text());q=r/'out/qa';q.mkdir(exist_ok=True)
edges=[z for c in d['chapters'] for z in [c['from'],c['from']+c['duration']-1]]
frames=sorted(set([z for s in shots for z in [s['from']+min(3,s['duration']-1),s['from']+s['duration']//2,s['from']+s['duration']-2]]+edges));
def balanced(xs):
 if len(xs)==1:return f'eq(n,{xs[0]})'
 k=len(xs)//2;return '('+balanced(xs[:k])+'+'+balanced(xs[k:])+')'
expr=balanced(frames)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'output/7_real_unsolved_mysteries.mp4'),'-vf',f"select='{expr}',scale=768:432",'-fps_mode','vfr','-q:v','2',str(q/'selected-%04d.jpg')],check=True)
index={f:q/f'selected-{i+1:04d}.jpg' for i,f in enumerate(frames)};records=[]
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',21)
for ch in d['chapters']:
 chosen=[s for s in shots if s['chapter']==ch['id']];rows=len(chosen);im=Image.new('RGB',(768*3,462*rows),'#0b1420');draw=ImageDraw.Draw(im)
 for i,s in enumerate(chosen):
  fs=[s['from']+min(3,s['duration']-1),s['from']+s['duration']//2,s['from']+s['duration']-2]
  for j,f in enumerate(fs):
   pic=Image.open(index[f]);im.paste(pic,(768*j,462*i));draw.text((768*j+12,462*i+435),f"shot{s['id']} · frame{f} · {s['type']}",font=font,fill='#e4c475')
  records.append({'shot':s['id'],'chapter':ch['id'],'actualFrames':fs})
 out=r/f'output/qa-chapter-{ch["id"]}.jpg';im.save(out,quality=85)
edge_sheet=Image.new('RGB',(1536,462*len(d['chapters'])),'#0b1420');draw=ImageDraw.Draw(edge_sheet)
for i,c in enumerate(d['chapters']):
 for j,f in enumerate([c['from'],c['from']+c['duration']-1]):
  edge_sheet.paste(Image.open(index[f]),(j*768,i*462));draw.text((j*768+12,i*462+435),f'chapter{i} frame{f}',font=font,fill='#e4c475')
edge_sheet.save(r/'output/chapter_boundaries.jpg',quality=90)
(r/'output/frame_qa_index.json').write_text(json.dumps(records,indent=2));print('EXTRACTED',len(frames),'actual final frames')
