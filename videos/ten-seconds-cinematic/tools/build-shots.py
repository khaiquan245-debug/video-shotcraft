from pathlib import Path
import json,re
r=Path(__file__).resolve().parents[1];scenes=json.loads((r/'src/timeline.json').read_text())
def tok(t):return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",t.lower().replace('’',"'").replace('10','ten'))
def at(sc,phrase):
 if not phrase:return 0
 words=[w['word'] for w in sc['words']];p=tok(phrase);hits=[j for j in range(len(words)-len(p)+1) if words[j:j+len(p)]==p]
 assert hits,(sc['id'],phrase)
 return sc['words'][hits[0]]['from']
# phrase, visual mode, target x/y, camera scale, optional idea text
plans=[
[('', 'concept',800,380,1,'TEN SECONDS AHEAD'),('Avoid an embarrassing fall','cup',800,380,1),('Prevent an accident','danger',800,380,1),('Find out what your crush','face',800,380,1),('use those ten seconds','world',800,380,1),('But think about it','concept',800,380,1,'A SMALL POWER. A BIG CHANGE.')],
[('', 'world',800,380,1),('focus and blink','face',800,380,1),('exactly ten seconds into the future','world',900,360,1.25),('Then you return to the present','world',800,380,1),('At first','face',800,380,1)],
[('', 'world',800,380,1),('entire cup of coffee','world',900,450,1.5),('someone nearby','world',1250,380,1.65),('You return to the present','world',800,380,1),('You smile confidently','face',800,380,1),('Then you walk straight into a pole','world',1080,380,1.5),('Apparently','face',800,380,1)],
[('', 'world',800,380,1),('You have exactly ten seconds','face',800,380,1),('You open the document','desk',800,380,1),('What do you think','world',800,380,1),('And give a surprisingly intelligent answer','over',800,380,1),('Congratulations','face',800,380,1),('And honestly','world',800,380,1)],
[('', 'world',800,380,1),('phone about to fall','world',1120,490,1.7),('You return to the present','world',800,380,1),('The cat pushes the phone','world',1000,470,1.45),('Your superpower just saved','face',800,380,1),('things start getting much more serious','concept',800,380,1,'THEN IT GETS SERIOUS.')],
[('', 'world',800,380,1),('Then you blink','face',800,380,1),('And see a vehicle','world',1020,480,1.25),('If you keep moving','danger',800,380,1),('You return to the present','world',800,380,1),('you realize something','face',800,380,1),('It could save your life','concept',800,380,1,'IT COULD SAVE A LIFE.')],
[('', 'world',800,380,1),('opponent move to the right','world',1080,450,1.35),('You return to the present','world',800,380,1),('He sees you move','world',1050,420,1.5),('Left','world',800,470,1.3),('And that is when','face',800,380,1),('The future is not fixed','concept',800,380,1,'THE FUTURE IS NOT FIXED.'),('Every decision','world',800,380,1)],
[('', 'world',800,380,1),('You have ten seconds to prepare','face',800,380,1),('You deliver the perfect answer','over',800,380,1),('But then','world',800,380,1),('Did you prepare that answer','world',800,380,1.08),('Okay','face',800,380,1)],
[('', 'world',800,380,1),('The words have been stuck','face',800,380,1),('You blink','world',900,370,1.15),('Now you have a choice','face',800,380,1),('But then you start thinking','world',800,380,1),('You take a breath','face',800,380,1),('I like you','world',800,380,1),('But this time you smile','face',800,380,1),('Some futures do not need to be changed','world',800,380,1)],
[('', 'world',800,380,1),('Your phone starts ringing','phone',800,380,1),('You are busy','face',800,380,1),('your finger moves','phone',800,380,1),('you look ten seconds into the future','world',800,380,1),('an elderly man steps into the road','world',1270,450,1.25),('You return to the present','world',800,380,1),('You are breathing hard','face',800,380,1),('Then your phone vibrates again','phone',800,380,1),('You answer','world',800,380,1),('Did you eat yet','world',1020,330,1.18),('No emergency','face',800,380,1),('You laugh','world',800,380,1),('Nothing dramatic happens','world',800,380,1.12),('and nearly ignored someone','face',800,380,1)],
[('', 'face',800,380,1),('Because even if','world',800,380,1),('in ten minutes','world',1000,380,1),('And maybe','concept',800,380,1,'UNCERTAINTY GIVES LIFE MEANING.')],
[('', 'world',800,380,1),('there is no rewind button','concept',800,380,1,'NO REWIND. NO WARNING.'),('But maybe','face',800,380,1),('look before crossing the street','world',800,380,1),('You can call your parents','world',800,380,1),('And sometimes','world',800,380,1.12),('You just need to stop wasting','face',800,380,1),('The future can wait','concept',800,380,1,'THE FUTURE CAN WAIT.\nTHIS MOMENT CAN’T.'),('If you really could see','concept',800,380,1,'WHAT WOULD YOU DO?')]
]
shots=[]
for sc,plan in zip(scenes,plans):
 local=[]
 for phrase,mode,x,y,z,*text in plan:
  local.append({'chapter':sc['id'],'localFrom':at(sc,phrase),'from':sc['from']+at(sc,phrase),'mode':mode,'x':x,'y':y,'zoom':z,'phrase':phrase,'text':text[0] if text else ''})
 assert all(a['localFrom']<b['localFrom'] for a,b in zip(local,local[1:])),sc['id']
 for j,shot in enumerate(local):
  shot['duration']=(local[j+1]['localFrom'] if j+1<len(local) else sc['duration'])-shot['localFrom'];shot['id']=len(shots);shots.append(shot)
assert sum(s['duration'] for s in shots)==11233
(r/'src/shots.json').write_text(json.dumps(shots,indent=2))
print(len(shots),'shots; shortest',min(s['duration'] for s in shots),'frames')
