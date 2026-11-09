from pathlib import Path
import json,zipfile
r=Path(__file__).resolve().parents[1]
texts=['These photos were taken by nine hikers. Days later... Every one of them was dead.',"In February 1959, the group crossed Russia's frozen Ural Mountains. They photographed each other smiling, skiing, and preparing their final campsite.",'One of their last photos shows them cutting into a snowy slope to pitch their tent. That night... Something went terribly wrong.','When rescuers arrived weeks later, they found the tent cut open from the inside. Boots and winter clothes were left behind. Footprints led downhill into the deadly cold.','All nine were eventually found dead. Some had suffered devastating injuries. Why would experienced hikers flee into the snow?','Decades later, scientists proposed a small avalanche, followed by deadly cold. But nobody knows exactly what happened that night. Their final photos remain.']
(r/'script.json').write_text(json.dumps(texts,indent=2));(r/'VOICEOVER_EN.txt').write_text('\n\n'.join(texts))
p=r/'tools/voice.py';s=p.read_text().replace(".replace('1964','nineteen sixty four')",".replace('1959','nineteen fifty nine')").replace("[('templeton','T EH M P AH L T AH N')]","[('ural','Y UH R AH L')]");p.write_text(s)
with zipfile.ZipFile('/workspace/attachments/60d38032-5017-438b-b52f-9aa2e4ebcd65/DYATLOV_3_PHOTO_SOURCES_FOR_CODEX.zip') as z:
 for n in z.namelist():
  if not n.endswith('/'): (r/'assets/source-package'/Path(n).name).write_bytes(z.read(n))
