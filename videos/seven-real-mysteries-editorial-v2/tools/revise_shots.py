from pathlib import Path
import json,math,csv
r=Path(__file__).resolve().parents[1];d=json.loads((r/'src/timeline.json').read_text());plans=json.loads((r/'src/shotplan.json').read_text())
change={
1:{3:'telescope',6:'annotation',7:'spectrum_search',8:'spectrum_search',9:'radio_origins',10:'hydrogen',11:'print',12:'page_text'},
2:{0:'page_botanical',1:'page_text',2:'page_stars',3:'page_botanical',4:'word_detail',5:'page_text',6:'word_detail',7:'statistics',8:'page_stars'},
3:{1:'fragment_detail',6:'inscriptions',9:'fragment_detail',10:'gearmacro'},
4:{10:'forest_wide'},
5:{1:'forest_wide',2:'forest_wide',3:'forest_floor',4:'forest_detail',5:'airburst',6:'forest',7:'forest_detail',8:'riverbank'},
6:{1:'serial_match',7:'riverbank',9:'pnw_map',10:'pnw_map'}
}
for cid,changes in change.items():
 for index,typ in changes.items():plans[cid][index][1]=typ
plans[5][4][2]='THE MISSING CRATER';plans[5][4][3]='The observation behind the question'
plans[2][4][3]='Recurring word-like groups'
# Short documentary labels replace the long implementation-oriented disclaimers.
for ch in plans[:7]:
 for item in ch:
  item[3]=item[3].replace(' · schematic','').replace(' · not measured corpus data','').replace(' · reconstructed','').replace(' · illustrated','').replace('Reconstruction · not archival footage','Night flight · reconstruction').replace('No supporting evidence of alien technology','No evidence of extraterrestrial technology')
plans[7]=[
 ['Two hundred','plane','MALAYSIA AIRLINES MH370','Boeing 777 · 239 people aboard'],
 ['flying from','route','KUALA LUMPUR → BEIJING','The intended route'],
 ['Satellite data','route','SOUTHERN INDIAN OCEAN','Estimated movement from satellite data'],
 ['In July','flaperon','RÉUNION ISLAND · 2015','A recovered wing component'],
 ['Investigators','flaperon','CONFIRMED MH370 DEBRIS','Physical evidence from the aircraft'],
 ['Yet the main','search_grid','THE MAIN WRECKAGE REMAINS MISSING','Flight recorders and exact location unrecovered'],
 ['The debris','flaperon','PHYSICAL EVIDENCE, UNPROVEN CAUSE','Why the aircraft changed course remains unresolved'],
 ['The multinational','mh_history','2017: SEARCH SUSPENDED','The multinational underwater search'],
 ['The latest search','vessel','THE 2025–2026 SEARCH PHASE','Ended in January 2026 without finding the aircraft'],
 ['Five months','mh_timeline','THE SEARCH AGREEMENT','June 2026 → June 2027'],
 ['leaving thousands','search_grid','THOUSANDS OF SQUARE KILOMETERS','Further seabed still to examine'],
 ['More than twelve','route','MORE THAN TWELVE YEARS','The main wreckage remains missing'],
 ['For the families','search_detail','THE HOPE OF ANSWERS','For the families of those aboard']]
plans[8]=[]
shots=[]
for ch,items in zip(d['chapters'][:8],plans[:8]):
 ws=ch['words'];text=[w['text'] for w in ws];last=0;anchors=[]
 for i,(trigger,kind,title,detail) in enumerate(items):
  tokens=trigger.lower().split();pos=next((i for i in range(last,len(text)-len(tokens)+1) if text[i:i+len(tokens)]==tokens),None)
  if pos is None:raise ValueError((ch['id'],trigger))
  anchors.append({'chapter':ch['id'],'type':kind,'title':title,'detail':detail,'from':ch['from'] if i==0 else ws[pos]['from'],'anchor':trigger});last=pos+len(tokens)
 for i,a in enumerate(anchors):
  end=anchors[i+1]['from'] if i+1<len(anchors) else ch['from']+ch['duration'];dur=end-a['from'];parts=max(1,math.ceil(dur/30/6))
  for j in range(parts):
   start=a['from']+round(dur*j/parts);stop=a['from']+round(dur*(j+1)/parts);typ=a['type']
   # Alternate meaningful details rather than holding an identical diagram.
   if j%2:
    typ={'page_botanical':'word_detail','page_text':'page_stars','fragment':'fragment_detail','forest_wide':'forest_detail','telescope':'spectrum','flaperon':'flaperon_detail','search_grid':'search_detail','word_detail':'page_text'}.get(typ,typ)
   shots.append({**a,'type':typ,'from':start,'duration':stop-start,'variant':j,'id':len(shots)})
# Brief seven-object callbacks, then new map/detail framing for the reflective close.
ch=d['chapters'][8];duration=ch['duration'];cuts=[0,2.35,4.15,6.15,7.35,8.55,9.75,11.8,15.1];types=['print','page_stars','fragment_detail','tent','forest_detail','riverbank','flaperon_detail','route','search_detail'];titles=['72 SECONDS','SIX CENTURIES','ANCIENT GEARS','A MOUNTAIN CAMPSITE','A FOREST TRANSFORMED','MONEY BESIDE A RIVER','PIECES ON DISTANT SHORES','EACH CLUE BRINGS US CLOSER','THE NEXT DISCOVERY'];details=['A recorded radio observation','The Voynich Manuscript','The Antikythera Mechanism','Dyatlov Pass','Tunguska','D.B. Cooper','Malaysia Airlines MH370','To an event we can no longer witness','May change the question']
for i,typ in enumerate(types):
 start=ch['from']+round(cuts[i]*30);stop=ch['from']+round(cuts[i+1]*30) if i+1<len(types) else ch['from']+duration;shots.append({'chapter':8,'type':typ,'title':titles[i],'detail':details[i],'from':start,'duration':stop-start,'variant':i%2,'id':len(shots),'anchor':'closing callback'})
(r/'src/shotplan.json').write_text(json.dumps(plans,indent=2));(r/'src/shots.json').write_text(json.dumps(shots,indent=2))
with (r/'STORYBOARD.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['shot','chapter','from','to','type','title','detail']);w.writerows([[s['id'],s['chapter'],s['from']/30,(s['from']+s['duration'])/30,s['type'],s['title'],s['detail']] for s in shots])
assert shots[0]['from']==0 and all(a['from']+a['duration']==b['from'] for a,b in zip(shots,shots[1:]));assert shots[-1]['from']+shots[-1]['duration']==d['frames'];print('REVISED SHOTS',len(shots),'MAX',max(s['duration']/30 for s in shots))
