from pathlib import Path
import json,re,math
r=Path(__file__).resolve().parents[1];scenes=json.loads((r/'src/timeline.json').read_text())
def norm(t):return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",t.lower().replace('’',"'"))
def find(sc,p):
 if not p:return 0
 w=[x['word'] for x in sc['words']];q=norm(p);hits=[i for i in range(len(w)-len(q)+1) if w[i:i+len(q)]==q];assert hits,(sc['id'],p);return sc['words'][hits[0]]['from']
shots=[]
for sc in scenes:
 beats=sc["beats"]
 # Preserve brief spoken lists as within-shot changes rather than machine-gun cuts.
 starts=[0]
 for b in beats[1:]:
  if b['from']-starts[-1]>=(126 if sc['id']>=8 else 76):starts.append(b['from'])
 if sc['duration']-starts[-1]<35 and len(starts)>1:starts.pop()
 starts.append(sc['duration'])
 for a,b in zip(starts,starts[1:]):
  maxdur=210 if sc['id']>=8 else 145;n=max(1,math.ceil((b-a)/maxdur))
  for k in range(n):
   lo=a+round((b-a)*k/n);hi=a+round((b-a)*(k+1)/n);beat=next(x for x in reversed(beats) if lo>=x['from']);tag=beat['tag']
   protect={'alarm','comparison','body','day','unknown','diploma','piano','pianoMistake','football','miss','orders','viral','privacy','everyone','education','dinner','parents','brother','listen','analyze','forget','quiet','eat','family','aging','clock','final'}
   face={'opportunity','adapt','uncertainty','bodyLimit','notGuaranteed','advantage','secret','fake','normal','notAlone','forget','unhappy','exhausted','regret','journey','meaning','window'}
   mode='portrait' if tag in face and k%2==0 else 'wide'
   if tag not in protect and tag not in face:
    mode=['wide','medium','over'][k%3]
    if tag in ['research','design','strategy','requirements','diploma','tests','evidence'] and k%2==0:mode='top'
   if tag=='comparison':mode='split'
   if tag=='final':mode='concept'
   shots.append({'id':len(shots),'chapter':sc['id'],'from':sc['from']+lo,'localFrom':lo,'duration':hi-lo,'mode':mode,'tag':tag,'phrase':beat['phrase'],'zoom':1 if mode in ['wide','split','concept'] else 1.35,'x':800 if mode!='medium' else 720,'y':380})
# A static reaction/overhead insert must not hide the next narrated physical action.
world_actions={'alarm','comparison','body','day','unknown','diploma','piano','pianoMistake','football','miss','orders','viral','privacy','everyone','education','dinner','parents','brother','listen','analyze','quiet','eat','family','aging','clock','final','testing','equation','launch','zero'}
for shot in shots:
 if shot['mode'] not in ['portrait','top'] or shot['chapter']==9:continue
 sc=scenes[shot['chapter']]
 active=[b for b in sc['beats'] if shot['localFrom']<=b['from']<shot['localFrom']+shot['duration']]
 top_context={'research','worldResearch','design','strategy','requirements','diploma','tests','evidence'}
 if any(b['tag'] in world_actions and b['tag']!=shot['tag'] for b in active) or (shot['mode']=='top' and any(b['tag'] not in top_context for b in active)) or (shot['mode']=='portrait' and any(b['tag'] not in face for b in active)):
  shot.update(mode='wide',zoom=1,x=800,y=380)
news_tags={'viral','fake','verify','invites','tech','investment','researchOrg','government','attention'}
for shot in shots:
 if shot['chapter']==6:
  sc=scenes[shot['chapter']]
  tags=[b['tag'] for b in sc['beats'] if shot['localFrom']<=b['from']<shot['localFrom']+shot['duration']]
  if shot['tag'] in news_tags or any(t in news_tags for t in tags):shot.update(mode='wide',zoom=1,x=800,y=380)
(r/'src/timeline.json').write_text(json.dumps(scenes,indent=2));(r/'src/shots.json').write_text(json.dumps(shots,indent=2));print(len(shots),'shots')
