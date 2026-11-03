"""Pin story actions to acoustically aligned words in the approved narration."""
import re,json
from pathlib import Path
root=Path(__file__).resolve().parents[1];p=root/'src/timeline.json';scenes=json.loads(p.read_text())
def tokens(s):return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",s.lower().replace('’',"'").replace('10','ten'))
def cue(sc,phrase,last=False):
 words=[w['word'] for w in sc['words']];target=tokens(phrase)
 hits=[i for i in range(len(words)-len(target)+1) if words[i:i+len(target)]==target]
 assert hits,(sc['id'],phrase)
 return sc['words'][hits[-1 if last else 0]]['from']
spec={
0:{'examples':'Avoid an embarrassing fall','accident':'Prevent an accident','crush':'Find out what your crush','meaning':'Ten seconds can sometimes change everything'},
1:{'blink':'blink','future':'you can see exactly','present':'you return to the present','choice':'or try to change it'},
2:{'spill':'entire cup of coffee','present':'You return to the present','step':'Step slightly to the left','pole':'a pole','bonk':'BONK'},
3:{'boss':'boss calling your name','scan':'You open the document','question':'What do you think','answer':'give a surprisingly intelligent answer','impressed':'Your boss looks impressed'},
4:{'fall':'phone about to fall','impact':'The screen hits the floor','present':'You return to the present','push':'The cat pushes the phone','catch':'you catch it'},
5:{'blink':'Then you blink','present':'You return to the present','pass':'vehicle actually flies past','realize':'you realize something'},
6:{'right':'opponent move to the right','present':'You return to the present','move':'and move right','left':'Left','fixed':'The future is not fixed'},
7:{'question':'What is your biggest weakness','answer':'You deliver the perfect answer','future':'you look ten seconds ahead','followup':'Did you prepare that answer'},
8:{'visionSorry':"I'm sorry",'breath':'You take a breath','confess':'I like you','response':"I'm just not ready for a relationship"},
9:{'ring':'Your phone starts ringing','elder':'an elderly man steps into the road','future':'you look ten seconds into the future','present':'You return to the present','run':'You run','grab':'Grab the man','pull':'Pull him backward','truck':'The truck flies past','answer':'You answer','momQuestion':'Did you eat yet','momReply':'Yeah Mom'},
10:{'minutes':'in ten minutes','tomorrow':'Tomorrow','year':'Next year'},
11:{'street':'look before crossing the street','feelings':'say what you really feel','parents':'You can call your parents','closing':'The future can wait','question':'If you really could see'}
}
report=[]
for i,events in spec.items():
 sc=scenes[i];sc['events']={key:cue(sc,phrase) for key,phrase in events.items()}
 for key,phrase in events.items():report.append({'chapter':i+1,'event':key,'phrase':phrase,'localFrame':sc['events'][key],'globalSeconds':round((sc['from']+sc['events'][key])/30,3)})
 print(i+1,sc['events'])
p.write_text(json.dumps(scenes,indent=2))
(root/'out/qa/picture-sync-cues.json').write_text(json.dumps({'method':'actions pinned to forced-aligned spoken words','fps':30,'events':report},indent=2))
