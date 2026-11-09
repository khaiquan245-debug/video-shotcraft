from pathlib import Path
import json,re
r=Path(__file__).resolve().parents[1];d=json.loads((r/'src/timeline.json').read_text());replacements={'1977':'nineteen seventy seven','1912':'nineteen twelve','1901':'nineteen oh one','1959':'nineteen fifty nine','2020':'twenty twenty','2021':'twenty twenty one','1908':'nineteen oh eight','1980':'nineteen eighty','1971':'nineteen seventy one','2016':'twenty sixteen','2014':'twenty fourteen','2015':'twenty fifteen','2017':'twenty seventeen','777':'seven seventy seven','727':'seven twenty seven'};cues=[]
for ch in d['chunks']:
 t=ch['text']
 for k,v in replacements.items():t=re.sub(r'\b'+k+r'\b',v,t)
 t=t.replace('D.B.','D B').replace('Réunion','Reunion').lower();matches=list(re.finditer(r"([a-z]+(?:'[a-z]+)?)([^a-z]*)",t));assert [m[1] for m in matches]==ch['tokens'];ws=ch['words'];i=0
 while i<len(ws):
  j=min(i+7,len(ws));natural=[k+1 for k in range(i,j) if any(p in matches[k][2] for p in '.?!:;') or (k-i>=3 and ',' in matches[k][2])]
  if natural:j=natural[0]
  elif j<len(ws):j=min(i+7,len(ws))
  cues.append({'from':ws[i]['from'],'to':ws[j-1]['to'],'text':' '.join(w['text'] for w in ws[i:j])});i=j
(r/'src/captions.json').write_text(json.dumps(cues,indent=2))
def ts(f):
 ms=round(f/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(r/'output/7_real_unsolved_mysteries.srt').write_text('\n\n'.join(f"{i+1}\n{ts(c['from'])} --> {ts(c['to'])}\n{c['text']}" for i,c in enumerate(cues))+'\n');print(len(cues),'PHRASE CUES')
