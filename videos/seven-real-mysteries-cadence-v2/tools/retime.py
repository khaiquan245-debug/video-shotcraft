from pathlib import Path
import json,subprocess,re,math,bisect
from PIL import ImageFont
r=Path(__file__).resolve().parents[1];oldroot=r.parent/'seven-real-mysteries';old=json.loads((oldroot/'src/timeline.json').read_text());new=json.loads((r/'src/timeline.json').read_text());caps=json.loads((r/'src/captions.json').read_text());report=[]
source=oldroot/'out/limited.mp4'
if not source.exists():source=oldroot/'output/7_real_unsolved_mysteries.mp4'
# Retain every approved illustration/animation. Map the original visual clock to actual native speech clock.
oldw=[w for c in old['chapters'] for w in c['words']];neww=[w for c in new['chapters'] for w in c['words']];assert [w['text'] for w in oldw]==[w['text'] for w in neww]
points={0:[0.]}
for a,b in zip(oldw,neww):
 for edge in ['from','to']:points.setdefault(a[edge]/30,[]).append(b[edge]/30)
for a,b in zip(old['chapters'],new['chapters']):points[a['from']/30]=[b['from']/30]
points[old['frames']/30]=[new['frames']/30]
xs=sorted(points);ys=[]
for x in xs:ys.append(max(ys[-1] if ys else 0,sum(points[x])/len(points[x])))
# A balanced expression avoids the FFmpeg expression parser's recursion limit.
def line(i):
 slope=(ys[i+1]-ys[i])/(xs[i+1]-xs[i]);return f'({ys[i]:.9f}+(T-{xs[i]:.9f})*{slope:.9f})'
def tree(a,b):
 if b-a==1:return line(a)
 m=(a+b)//2;return f'if(lt(T,{xs[m]:.9f}),{tree(a,m)},{tree(m,b)})'
expr=tree(0,len(xs)-1);fps=30;seconds=new['frames']/30
(r/'output/visual_time_map.json').write_text(json.dumps({'source':str(source),'oldSeconds':old['frames']/30,'newSeconds':seconds,'mapping':'monotone piecewise linear old/new aligned word start/end anchors','points':list(zip(xs,ys))},indent=2))
# Source punctuation and case; keep actual spoken number tokens so captions track the voice.
replacements={'1977':'nineteen seventy seven','1912':'nineteen twelve','1901':'nineteen oh one','1959':'nineteen fifty nine','2020':'twenty twenty','2021':'twenty twenty one','1908':'nineteen oh eight','1980':'nineteen eighty','1971':'nineteen seventy one','2016':'twenty sixteen','2014':'twenty fourteen','2015':'twenty fifteen','2017':'twenty seventeen','777':'seven seventy seven','727':'seven twenty seven'}
display={}
for ch in new['chunks']:
 t=ch['text']
 for a,b in replacements.items():t=re.sub(r'\b'+a+r'\b',b,t)
 t=t.replace("'Wow!'",'Wow!').replace('D.B.','D B').replace('Réunion','Reunion');matches=list(re.finditer(r"([A-Za-z]+(?:'[A-Za-z]+)?)([^A-Za-z]*)",t));assert [m[1].lower() for m in matches]==ch['tokens']
 for w,m in zip(ch['words'],matches):display[w['from']]=(m[1],''.join(z for z in m[2] if z in ',.;:!?'))
font=ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',78)
def ass_ts(f):
 cs=round(f/30*100);return f'{cs//360000:01}:{cs//6000%60:02}:{cs//100%60:02}.{cs%100:02}'
def srt_ts(f):
 ms=round(f/30*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
header='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
ScaledBorderAndShadow: yes
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Liberation Sans,78,&H00E9F1F0,&H00E9F1F0,&H0010140B,&H0010140B,0,0,0,0,100,100,0,0,1,1.5,1.5,2,170,170,36,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
events=[];srt=[];layout=[]
for i,c in enumerate(caps):
 ws=[w for w in neww if c['from']<=w['from'] and w['to']<=c['to']];words=[display[w['from']][0]+display[w['from']][1] for w in ws];lines=[];buf=[]
 for word in words:
  if buf and font.getlength(' '.join(buf+[word]))>1520:lines.append(' '.join(buf));buf=[]
  buf.append(word)
 if buf:lines.append(' '.join(buf))
 assert len(lines)<=2,(i,lines)
 c['display']=' '.join(words);layout.append({'cue':i,'lines':len(lines),'maximumLineWidth':max(font.getlength(x) for x in lines)})
 txt=r'\N'.join(lines)
 txt=re.sub(r'\b(evidence|confirmed|unknown|uncertain|unproven|hypothesis|Wow)\b',lambda m:r'{\c&H75C4E4&}'+m[0]+r'{\c&HE9F1F0&}',txt,flags=re.I)
 events.append(f"Dialogue: 0,{ass_ts(c['from'])},{ass_ts(c['to'])},Default,,0,0,0,,{txt}")
 srt.append(f"{i+1}\n{srt_ts(c['from'])} --> {srt_ts(c['to'])}\n"+'\n'.join(lines))
(r/'src/captions.json').write_text(json.dumps(caps,indent=2));(r/'output/7_real_unsolved_mysteries.srt').write_text('\n\n'.join(srt)+'\n');(r/'public/subtitles.ass').write_text(header+'\n'.join(events)+'\n');(r/'output/caption_layout.json').write_text(json.dumps(layout,indent=2))
# Whole old caption area is a dedicated empty band below artwork/case detail, so no evidence is hidden.
filt=f"[0:v]setpts='{expr}/TB',fps=30,tpad=stop_mode=clone:stop_duration=1,trim=duration={seconds:.9f},drawbox=x=0:y=873:w=1920:h=207:color=0x0b1420:t=fill,ass=public/subtitles.ass,format=yuv420p[v]"
(r/'out/retime-filter.txt').write_text(filt)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(source),'-filter_complex_script',str(r/'out/retime-filter.txt'),'-map','[v]','-an','-c:v','libx264','-preset','fast','-crf','19','-r','30','-color_range','tv','-movflags','+faststart',str(r/'out/revised-picture.mp4')],check=True)
for stem,name in [('master','7_real_unsolved_mysteries'),('no-music','7_real_unsolved_mysteries_no_music')]:
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'out/revised-picture.mp4'),'-i',str(r/f'public/audio/{stem}.wav'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-t',str(seconds),'-movflags','+faststart',str(r/f'output/{name}.mp4')],check=True)
print('REVISED VIDEO READY',seconds,'ANCHORS',len(xs),flush=True)
