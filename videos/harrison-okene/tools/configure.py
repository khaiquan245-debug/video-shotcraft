from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
texts=['The diver reached for a lifeless hand. Then... it grabbed him back.',"In 2013, a tugboat flipped off Nigeria's coast and sank almost a hundred feet. Trapped inside was Harrison Okene, the ship's cook.","In total darkness, he found a small pocket of air above the rising water. Eleven other crew members didn't survive. And the air around him was running out.",'Hours passed. Then another day. More than sixty hours after the sinking, rescue divers entered the wreck, expecting to find bodies.','One diver spotted a hand. He reached for it... and the hand moved. Harrison was alive.','He was carefully rescued and treated in a decompression chamber. And the unbelievable part? That moment... was caught on camera.']
(r/'script.json').write_text(json.dumps(texts,indent=2))
p=r/'tools/voice.py';s=p.read_text();s=s.replace(".replace('2019','twenty nineteen').replace('2024','twenty twenty four').replace('2003','two thousand three')",".replace('2013','twenty thirteen')");s=s.replace("[('backrooms','B AE K R UW M Z'),('oshkosh','AA SH K AA SH'),('rc','AA R S IY'),('racetrack','R EY S T R AE K')]","[('okene','OW K EY N EY')]");p.write_text(s)
(r/'public/audio').mkdir(exist_ok=True)
import shutil
shutil.copytree(r/'assets/illustrations',r/'public/illustrations',dirs_exist_ok=True)
