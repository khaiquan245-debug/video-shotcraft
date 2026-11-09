from pathlib import Path
import json,re,shutil
r=Path(__file__).resolve().parents[1];previous=Path('/workspace/seven-real-mysteries-cadence-v2');script=json.loads((previous/'script.json').read_text());chunks=json.loads((previous/'out/chunks.json').read_text())
ending=["The latest search ended in January 2026 without finding the aircraft.","Five months later, Malaysia extended its agreement with Ocean Infinity through June 2027, leaving thousands of square kilometers still to examine.","More than twelve years after the disappearance, the main wreckage remains missing.","For the families of the 239 people aboard, every new search carries the hope of finally learning what happened."]
outro=["A radio signal lasted seventy-two seconds.","A manuscript survived six centuries.","An ancient machine preserved its gears, and a missing aircraft left pieces on distant shores.","Each clue brings us closer to an event we can no longer witness.","The next discovery may change a theory, settle a question, or reveal that we've been asking the wrong one."]
head=[c['text'] for c in chunks if c['id'] in ['7-0','7-1']];script[7]['paragraphs']=head+ending;script[7]['text']=' '.join(head+ending);script[8]['paragraphs']=outro;script[8]['text']=' '.join(outro)
(r/'script.json').write_text(json.dumps(script,indent=2));(r/'VOICEOVER_EN.txt').write_text('\n\n'.join(s['text'] for s in script)+'\n')
newchunks=[c for c in chunks if c['chapter']<7 or c['id'] in ['7-0','7-1']]
for cid,text in [('7-2',' '.join(ending[:2])),('7-3',' '.join(ending[2:])),('8-0',' '.join(outro[:3])),('8-1',' '.join(outro[3:]))]:newchunks.append({'id':cid,'chapter':int(cid[0]),'text':text})
(r/'out/chunks.json').write_text(json.dumps(newchunks,indent=2))
for cid in ['7-2','7-3','8-0','8-1']:
 for stem in ['native','level','connected','final']:
  p=r/f'out/{stem}-{cid}.wav'
  if p.exists():p.unlink()
for p in (r/'output').iterdir():
 if p.is_file() and p.name not in ['MUSIC_LICENSE.txt','7_real_unsolved_mysteries_thumbnail.png']:p.unlink()
# Keep supplied revision brief as documentation, never use it as narration/rendered text.
shutil.copyfile('/workspace/attachments/b1daa9de-2d9e-4853-b9c2-4825983285e5/Văn bản đã dán.txt',r/'assets/reference/revision_prompt.txt')
