from pathlib import Path
import json,re,subprocess,hashlib,wave,difflib,sys
import numpy as np,sherpa_onnx
r=Path(__file__).resolve().parents[1];d=json.loads((r/'src/timeline.json').read_text());caps=json.loads((r/'src/captions.json').read_text());shots=json.loads((r/'src/shots.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(t):
 t=t.lower().replace('réunion','reunion')
 special=[('$5,800','five thousand eight hundred dollars'),('$200,000','two hundred thousand dollars'),('$20','twenty dollar'),('1.5 mm','one and a half millimeters'),('1.5 millimeters','one and a half millimeters'),('1,420','fourteen hundred and twenty'),('1420','fourteen hundred and twenty'),('mhz','megahertz'),('2,000','two thousand'),('1,000','a thousand'),('km²','square kilometers'),('august 15','august fifteenth'),('june 30','june thirtieth'),('november 24','november twenty fourth'),('march 8','march eighth'),('15th','fifteenth'),('6equj5','six e q u j five'),('6 eq uj5','six e q u j five'),('big-year','big ear')]
 for a,b in special:t=t.replace(a,b)
 numbers={'1977':'nineteen seventy seven','1912':'nineteen twelve','1901':'nineteen oh one','1959':'nineteen fifty nine','2020':'twenty twenty','2021':'twenty twenty one','1908':'nineteen oh eight','1980':'nineteen eighty','1971':'nineteen seventy one','2016':'twenty sixteen','2014':'twenty fourteen','2015':'twenty fifteen','2017':'twenty seventeen','2026':'twenty twenty six','2027':'twenty twenty seven','239':'two hundred and thirty nine','240':'two hundred and forty','777':'seven seventy seven','727':'seven twenty seven','370':'three seven zero','72':'seventy two','30':'thirty','4':'four','12':'twelve','6':'six'}
 for a,b in numbers.items():t=re.sub(r'\b'+a+r'\b',b,t)
 return re.findall(r"[a-z]+(?:'[a-z]+)?",t)
assert len(d['chapters'])==9 and [c['id'] for c in d['chapters']]==list(range(9));assert 360<=d['frames']/30<=480;assert all(s['duration']<=180 for s in shots)
ws=[w for c in d['chapters'] for w in c['words']];assert [w['text'] for w in ws]==' '.join(c['text'] for c in caps).split();assert all(c['from']<=w['from']<w['to']<=c['from']+c['duration'] for c in d['chapters'] for w in c['words']);assert all(a['to']<=b['from'] for a,b in zip(caps,caps[1:]))
for c in caps:assert norm(c['display'])==norm(c['text']),(c['display'],c['text'],norm(c['display']),norm(c['text']))
srt=(r/'output/7_real_mysteries_v2.srt').read_text().strip().split('\n\n');assert len(srt)==len(caps)
for c,s in zip(caps,srt):assert ' '.join(s.splitlines()[2:])==c['display']
ban=re.compile(r'CURRENT STATUS NOT VERIFIED|NOT VERIFIED|NEEDS CONFIRMATION|SOURCE NEEDED|TODO|FIXME|PLACEHOLDER|\bVERIFY\b',re.I)
for p in [r/'script.json',r/'VOICEOVER_EN.txt',r/'src/shots.json',r/'src/shotplan.json',r/'src/captions.json',r/'src/Art.tsx',r/'src/Upgrade.tsx',r/'src/index.tsx',r/'output/7_real_mysteries_v2.srt']:assert not ban.search(p.read_text()),p
assert not any(s['type']=='hypothesis' for s in shots)
checks={'seconds':d['frames']/30,'frames':d['frames'],'chapters':9,'shots':len(shots),'maxShotSeconds':max(s['duration']/30 for s in shots),'subtitleCues':len(caps),'spokenTokens':len(ws),'semanticCoverageAndNumeralEquivalencePass':True,'productionTextGatePass':True}
# Reuse measured ASR only for byte-identical prior waveforms; freshly decode the four replacement chunks.
old=Path('/workspace/seven-real-mysteries-cadence-v2');oldasr={z['id']:z for z in json.loads((old/'output/verification.json').read_text()).get('asr',[])};newasr={z['id']:z for z in json.loads((r/'output/new_narration_asr.json').read_text())};asr=[]
for ch in d['chunks']:
 p=r/f'out/final-{ch["id"]}.wav';op=old/f'out/final-{ch["id"]}.wav';cached=ch['id'] in oldasr and op.exists() and sha(p)==sha(op)
 if cached:recognized=oldasr[ch['id']]['recognized'];method='prior measured ASR reused for byte-identical waveform'
 else:recognized=newasr[ch['id']]['recognized'];method='fresh ASR of replacement waveform'
 ratio=difflib.SequenceMatcher(None,norm(ch['text']),norm(recognized),autojunk=False).ratio();assert ratio>.80,(ch['id'],ratio,recognized)
 asr.append({'id':ch['id'],'recognized':recognized,'similarity':ratio,'method':method,'waveSha256':sha(p)});print('VOICE',ch['id'],round(ratio,3),flush=True)
checks['asr']=asr;(r/'output/verification.json').write_text(json.dumps(checks,indent=2))
if '--audio-only' in sys.argv:print('SOURCE/AUDIO PASS');raise SystemExit(0)
files=[]
for name in ['7_real_mysteries_v2.mp4','7_real_mysteries_v2_no_music.mp4']:
 p=r/'output'/name;info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]));v=next(z for z in info['streams'] if z['codec_type']=='video');a=next(z for z in info['streams'] if z['codec_type']=='audio');assert (v['width'],v['height'],v['codec_name'],v['pix_fmt'],v['r_frame_rate'])==(1920,1080,'h264','yuv420p','30/1');assert int(v['nb_frames'])==d['frames'];assert a['codec_name']=='aac' and a['sample_rate']=='48000';assert abs(float(info['format']['duration'])-d['frames']/30)<.05;subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True)
 pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-vn','-f','f32le','-']);audio=np.frombuffer(pcm,np.float32);peak=float(abs(audio).max());assert peak<1
 files.append({'file':name,'sha256':sha(p),'seconds':float(info['format']['duration']),'frames':int(v['nb_frames']),'width':v['width'],'height':v['height'],'fps':'30/1','codec':'H264/yuv420p/AAC','audioChannels':a['channels'],'decodedAudioPeak':peak,'fullDecodePass':True});print('VIDEO PASS',name,flush=True)
checks['files']=files;(r/'output/verification.json').write_text(json.dumps(checks,indent=2));print('FINAL PASS')
