from pathlib import Path
import json,re,math
r=Path(__file__).resolve().parents[1];scenes=json.loads((r/'src/timeline.json').read_text())
def norm(t):return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?",t.lower().replace('’',"'"))
def find(sc,p):
 if not p:return 0
 w=[x['word'] for x in sc['words']];q=norm(p);hits=[i for i in range(len(w)-len(q)+1) if w[i:i+len(q)]==q];assert hits,(sc['id'],p);return sc['words'][hits[0]]['from']
plans=[
[('', 'alarm'),('You can learn anything','brain'),('Something that takes someone else','comparison'),('A subject that normally takes months','knowledge'),('Mathematics','mathematics'),('Programming','programming'),('Economics','economics'),('Foreign languages','languages'),('But forget about getting perfect grades','grades'),('How much money','money'),('And what happens','worldAttention')],
[('', 'rules'),('You can understand','learn'),('But your body','body'),('A day still','day'),('And if humanity','unknown'),('These might sound','limits')],
[('', 'classroom'),('Your teacher','equation'),('Within minutes','solution'),('While everyone else','nextChapter'),('So you decide','testLimits'),('You move on to physics','physics'),('Then chemistry','chemistry'),('Economics','economics'),('And computer science','programming'),('After just one week','week'),('Of course knowing','diploma'),('You still have to meet','requirements'),('But you\'ve realized','opportunity')],
[('', 'money'),('You start by learning how to code','programming'),('Next comes website design','web'),('App development','apps'),('Artificial intelligence','ai'),('Marketing','marketing'),('And business management','management'),('So you decide to launch','store'),('First you research','research'),('You study customer behavior','customers'),('Learn how to choose products','products'),('Analyze competitors','competitors'),('And figure out how online advertising works','ads'),('You launch your first product','launch'),('Nothing','zero'),('So you investigate','investigate'),('Is the price too high','price'),('Are the product photos','photos'),('Or does nobody','demand'),('You test different ideas','test'),('Finally the first order','orders'),('You realize your greatest advantage','adapt'),('Next you study investing','investing'),('Stocks','stocks'),('Real estate','realEstate'),('Financial markets','finance'),('But even with your extraordinary brain','uncertainty'),('Because the economy','decisions')],
[('', 'map'),('You start with English','English'),('Then Mandarin Chinese','Mandarin'),('Japanese','Japanese'),('French','French'),('And Spanish','Spanish'),('Vocabulary grammar','languageStudy'),('You\'ll still need to practice','conversation'),('Now you can read research','worldResearch'),('Then you try learning','skills'),('Piano','pianoTheory'),('Drawing','drawing'),('Football','footballTheory'),('But when you sit down','piano'),('Your fingers still make mistakes','pianoMistake'),('And when you step','football'),('You can still completely miss','miss'),('Because understanding','practice'),('For the first time','bodyLimit')],
[('', 'startup'),('You understand technology','expertise'),('Whenever you encounter','problem'),('So you decide to start','company'),('You identify a problem','identify'),('You design a product','design'),('Write the software','software'),('Develop a business strategy','strategy'),('Hire employees','employees'),('And pitch to investors','investors'),('Tasks that normally','team'),('But building a successful company','testing'),('Customers need convincing','customers'),('Employees need leadership','leadership'),('And one bad decision','risk'),('You\'re not guaranteed','notGuaranteed'),('But if you use','advantage'),('There\'s just one problem','secret')],
[('', 'private'),('You pass advanced','tests'),('You become conversational','sixLanguages'),('Then one day a video','viral'),('At first people think','fake'),('But after experts','verify'),('The invitations begin','invites'),('Technology companies','tech'),('Investment firms','investment'),('World class research institutions','researchOrg'),('And perhaps even government','government'),('Everyone wants to work','attention'),('But your privacy','privacy'),('And that raises','question'),('What if tomorrow','everyone'),('Education would change','education'),('A university degree alone','degreeNormal'),('And your extraordinary ability','normal'),('If everyone could learn','creativity'),('You\'d still have','notAlone')],
[('', 'money'),('Or will you try','impact'),('You begin thinking','challenges'),('Cancer','health'),('Clean energy','energy'),('Climate change','climate'),('Diseases that still','disease'),('You study biology','biology'),('Chemistry','chemistry'),('Artificial intelligence','ai'),('And materials science','materials'),('You absorb knowledge','connections'),('Perhaps you identify','prototype'),('But scientific discoveries','evidence'),('Theories must be tested','testing'),('Inventions must be validated','validation'),('And some questions','questions'),('You can learn almost everything','known'),('But to discover something truly new','unknown')],
[('', 'year'),('In that single year','library'),('But tonight','dinner'),('Your parents talk','parents'),('Your younger brother','brother'),('You smile and listen','listen'),('But your mind','analyze'),('That you\'ve started to forget','forget'),('You remember those evenings','memory'),('The frustration','frustration'),('And the excitement','aha'),('It\'s been a long time','quiet'),('You\'ve learned countless things','knowledge'),('But none of that','unhappy'),('You can still feel exhausted','exhausted'),('Still make decisions','regret'),('And still face questions','questions'),('For the first time','journey')],
[('', 'recap'),('Explore multiple careers','careers'),('Build businesses','business'),('Create new technologies','technology'),('And possibly contribute','science'),('But there\'s one thing','limit'),('Time','clock'),('A day still','day'),('You still need to sleep','sleep'),('You still need to eat','eat'),('You still need to rest','rest'),('And the people you love','family'),('Will continue growing older','aging'),('You might learn','photo'),('But you can\'t live','oneLife'),('In the end','meaning'),('It\'s what you choose','sunset'),('Because if you woke up','window'),('What would be the very first','final')]
]
shots=[]
for sc,plan in zip(scenes,plans):
 beats=[{'from':find(sc,p),'tag':tag,'phrase':p} for p,tag in plan];assert all(a['from']<b['from'] for a,b in zip(beats,beats[1:])),sc['id'];sc['beats']=beats
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
(r/'src/timeline.json').write_text(json.dumps(scenes,indent=2));(r/'src/shots.json').write_text(json.dumps(shots,indent=2));print(len(shots),'shots')
