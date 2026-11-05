from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
texts=['This room is real. And nobody knew where it was.','In 2019, a photo of an empty yellow room spread across the internet. Fluorescent lights. Endless-looking walls. No people. It became known as The Backrooms.','An internet horror story claimed you could slip out of reality... and get trapped here forever. People invented monsters, hidden levels, and escape routes.','But the biggest mystery was real. Where was this photo actually taken?','Then, in 2024, online detectives found a forgotten webpage from 2003. It led them to Oshkosh, Wisconsin.','The supposedly endless nightmare was just a former furniture store being renovated for a hobby shop... and an RC car racetrack. No secret dimension. No monsters. Just one ordinary photo... that scared the entire internet.']
(r/'script.json').write_text(json.dumps(texts,indent=2))
p=r/'tools/voice.py';s=p.read_text();a=s.index('texts=');b=s.index("\n(r/'script.json')",a);s=s[:a]+'texts=json.loads((r/"script.json").read_text())'+s[b:];s=s.replace("tempo=.98 if i==0 else 1.03 if i<5 else 1.0",'tempo=1.0')
s=s.replace("norm=text.lower().replace('1977','nineteen seventy seven').replace('72','seventy two').replace('...',' ')","norm=text.lower().replace('2019','twenty nineteen').replace('2024','twenty twenty four').replace('2003','two thousand three').replace('...',' ').replace('-', ' ')")
s=s.replace("[('ehman','EY M AH N'),('sagittarius','S AE JH AH T EH R IY AH S')]","[('backrooms','B AE K R UW M Z'),('oshkosh','AA SH K AA SH')] ")
p.write_text(s)
