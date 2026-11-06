from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
texts=["This animal has THREE hearts. But that's not even the weirdest part.","No, it's not an alien. It's an octopus.",'Two hearts pump blood through its gills, where it picks up oxygen. The third pumps that oxygen-rich blood through the rest of its body.',"And unlike us, an octopus has BLUE blood, thanks to a copper-based protein.","But here's the twist. When an octopus swims, its main heart can temporarily stop beating.",'Swimming is exhausting, so it often prefers crawling along the ocean floor.',"Three hearts. Blue blood. And somehow, swimming is STILL too much cardio. Nature is wild."]
(r/'script.json').write_text(json.dumps(texts,indent=2));(r/'VOICEOVER_EN.txt').write_text('\n\n'.join(texts))
p=r/'tools/voice.py';s=p.read_text().replace(".replace('2013','twenty thirteen')",'').replace("[('okene','OW K EY N EY')]","[('octopus','AA K T AH P AH S')]").replace('i==5','i==len(texts)-1');p.write_text(s)
