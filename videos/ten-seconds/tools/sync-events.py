import re,json
from pathlib import Path
root=Path(__file__).resolve().parents[1];p=root/'src/timeline.json';scenes=json.loads(p.read_text())
def cue(sc,phrase,default,last=False):
 words=[];frames=[]
 for c in sc['captions']:
  tokens=re.findall('[a-z0-9]+',c['text'].lower())
  for i,w in enumerate(tokens):words.append(w);frames.append(round(c['from']+c['duration']*i/max(1,len(tokens))))
 target=re.findall('[a-z0-9]+',phrase.lower());hits=[frames[i] for i in range(len(words)-len(target)+1) if words[i:i+len(target)]==target]
 return hits[-1 if last else 0] if hits else default
spec={2:{'present':('return to the present',456),'pole':('walk straight into a pole',801)},4:{'fall':('phone about to fall',132),'present':('return to the present',294),'catch':('you catch it',513)},5:{'blink':('Then you blink',237),'present':('return to the present',525),'pass':('vehicle actually flies past',705)},8:{'visionSorry':('I m sorry',360),'confess':('say it anyway',882),'response':('not ready for a relationship',1010)},9:{'future':('look 10 seconds into the future',369),'present':('return to the present',768),'grab':('Grab the man',891),'truck':('The truck flies past',966),'answer':('You answer',1392),'momQuestion':('Did you eat yet',1485),'momReply':('Yeah Mom',1869)}}
for i,events in spec.items():
 sc=scenes[i];sc['events']={key:cue(sc,phrase,default) for key,(phrase,default) in events.items()}
 print(i+1,sc['events'])
p.write_text(json.dumps(scenes,indent=2))
