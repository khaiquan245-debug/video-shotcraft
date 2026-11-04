"""Validate the actual female narration, scene/caption timing, and final encoded files."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import unicodedata
import wave

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'out'
WORDS = re.compile(r"\w+(?:['’]\w+)?", re.UNICODE)


def tokens(text):
    return [w.lower() for w in WORDS.findall(unicodedata.normalize('NFC', text))]


def run(args):
    return subprocess.run(args, check=True, capture_output=True)


def video_info(path):
    return json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)]).stdout)


def stream_hash(path, stream):
    return run(['ffmpeg','-v','error','-i',str(path),'-map',stream,'-c','copy',
                '-f','hash','-hash','sha256','-']).stdout.decode().strip()


def encoded_audio_hash(source, seconds, encode):
    args=['ffmpeg','-v','error','-i',str(source),'-map','0:a:0','-t',str(seconds)]
    args += ['-c:a','aac','-b:a','160k'] if encode else ['-c:a','copy']
    return hashlib.sha256(run(args+['-f','adts','-']).stdout).hexdigest()


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--video',action='store_true');args=parser.parse_args()
    scenes=json.loads((ROOT/'src/timeline.json').read_text())
    shots=json.loads((ROOT/'src/shots.json').read_text())
    captions=json.loads((ROOT/'src/captions.json').read_text())
    translation=json.loads((ROOT/'translation.json').read_text())
    narration=json.loads((OUT/'qa/vietnamese-narration.json').read_text())
    preflight=json.loads((OUT/'female-aligned/phoneme-preflight.json').read_text())
    assert not preflight['unknownPhonemes'] and not preflight['wordMappingMismatches']
    assert narration['voice']=='native female VAIS1000 medium' and not narration['pitchShiftApplied']
    total=sum(s['duration'] for s in scenes)
    assert len(scenes)==len(translation)==10 and total==narration['frames']
    source_words=[];caption_words=[];beat_count=0;native_files=0
    for i,(scene,chapter) in enumerate(zip(scenes,translation)):
        assert scene['id']==i and scene['from']==sum(s['duration'] for s in scenes[:i])
        expected=' '.join(p['vi'] for p in chapter['segments'])
        assert tokens(expected)==tokens(scene['text'])==[w['word'] for w in scene['words']]
        source_words+=tokens(expected)
        assert len(scene['beats'])==len(chapter['segments'])
        word_index=0
        for j,(beat,segment) in enumerate(zip(scene['beats'],chapter['segments'])):
            assert beat['tag']==segment['tag'] and beat['phrase']==segment['vi']
            subset=scene['words'][word_index:word_index+len(tokens(segment['vi']))]
            assert subset[0]['from']>=beat['from']
            end=scene['beats'][j+1]['from'] if j+1<len(scene['beats']) else scene['duration']
            assert subset[-1]['to']<=end+1
            word_index+=len(subset);beat_count+=1
        for a,b in zip(scene['words'],scene['words'][1:]):assert a['to']<=b['from']+1
        assert all(0<=w['from']<w['to']<=scene['duration'] for w in scene['words'])
    for item in (OUT/'female-aligned').glob('chapter-*-beat-*.json'):
        metadata=json.loads(item.read_text())
        with wave.open(str(item.with_suffix('.wav'))) as f:
            assert f.getframerate()==metadata['sampleRate']
            assert abs(f.getnframes()/f.getframerate()-metadata['seconds'])<1e-7
            assert metadata['words'][-1]['toSample']<=f.getnframes()
        assert tokens(metadata['text'])==[w['word'] for w in metadata['words']]
        native_files+=1
    assert native_files==beat_count==171
    with wave.open(str(OUT/'narration-raw.wav')) as f:
        assert f.getframerate()==24000 and f.getnframes()==total*800
    position=0
    for shot in shots:
        assert shot['from']==position and shot['duration']>0
        assert shot['localFrom']==shot['from']-scenes[shot['chapter']]['from']
        position+=shot['duration']
    assert position==total
    for c in captions:
        assert 0<=c['from']<c['from']+c['duration']<=total
        assert tokens(c['text'])==[w['word'] for w in c['words']]
        caption_words+=tokens(c['text'])
    for a,b in zip(captions,captions[1:]):assert a['from']+a['duration']<=b['from']
    assert caption_words==source_words
    report={'frames':total,'seconds':total/30,'chapters':10,'narrativeBeats':beat_count,
            'nativeAlignedAudioFiles':native_files,'spokenSyllableTokens':len(source_words),
            'shots':len(shots),'captionGroups':len(captions),'unknownPhonemes':0,
            'allWrittenWordsPreserved':True,'captionWordOrderExact':True,
            'noShotGaps':True,'noCaptionOverlap':True,'audioFrameGridExact':True,
            'alignmentSource':'Same-inference VITS phoneme sample durations; word boundaries quantized to 30fps',
            'perceptualLimits':'Technical checks do not imply human listening approval or exact lip synchronization'}
    if args.video:
        main=OUT/'learn-100x-vi.mp4';nomusic=OUT/'learn-100x-vi-no-music.mp4'
        results=[]
        for path in [main,nomusic]:
            info=video_info(path);v=next(s for s in info['streams'] if s['codec_type']=='video')
            assert (v['width'],v['height'],v['avg_frame_rate'],int(v['nb_frames']))==(1920,1080,'30/1',total)
            assert abs(float(info['format']['duration'])-total/30)<.05
            decode=run(['ffmpeg','-hide_banner','-nostats','-v','info','-i',str(path),
                        '-vf','blackdetect=d=0.08:pix_th=0.02:pic_th=0.98',
                        '-af','astats=metadata=1:reset=0','-f','null','-'])
            log=decode.stderr.decode(errors='replace')
            peaks=re.findall(r'Peak level dB:\s*(-?[\d.]+)',log)
            assert peaks and float(peaks[-1])<0, 'Encoded audio reaches clipping'
            black=[{'from':float(a),'to':float(b),'seconds':float(c)} for a,b,c in
                   re.findall(r'black_start:([\d.]+) black_end:([\d.]+) black_duration:([\d.]+)',log)]
            assert not any(x['from']>.5 and x['to']<total/30-.5 for x in black), 'Internal encoded black gap'
            results.append({'file':path.name,'bytes':path.stat().st_size,
                            'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                            'completeDecode':True,'frames':int(v['nb_frames']),
                            'decodedAudioPeakDbfs':float(peaks[-1]),'noInternalBlackGaps':True,
                            'blackIntervals':black})
        picture_main=stream_hash(main,'0:v:0');picture_nomusic=stream_hash(nomusic,'0:v:0')
        assert picture_main==picture_nomusic
        main_hash=encoded_audio_hash(main,total/30,False)
        expected_main=encoded_audio_hash(ROOT/'public/audio/master.flac',total/30,True)
        dry_hash=encoded_audio_hash(nomusic,total/30,False)
        expected_dry=encoded_audio_hash(ROOT/'public/audio/narration-sfx.flac',total/30,True)
        assert main_hash==expected_main and dry_hash==expected_dry
        report.update({'videos':results,'bothVariantsUseIdenticalEncodedPicture':True,
                       'picturePacketHash':picture_main,'encodedAudioMatchesIntendedMixes':True,
                       'mainAudioSha256':main_hash,'noMusicAudioSha256':dry_hash})
    name='final-film-verification.json' if args.video else 'synchronization-verification.json'
    (OUT/'qa'/name).write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
