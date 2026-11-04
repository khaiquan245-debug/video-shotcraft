"""Generate the female Vietnamese narrator with timings from the same audio inference."""
from pathlib import Path
import argparse
import hashlib
import json
import math
import re
import wave

import numpy as np
import onnx
import onnxruntime as ort
from piper import PiperVoice, SynthesisConfig
from piper.config import PiperConfig
from piper.patch_voice_with_alignment import add_alignment_output

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / 'tools/vits-piper-vi_VN-vais1000-medium/vi_VN-vais1000-medium.onnx'
OUT = ROOT / 'out/female-aligned'
OUT.mkdir(parents=True, exist_ok=True)
WORDS = re.compile(r"\w+(?:['’]\w+)?", re.UNICODE)
PUNCTUATION = set('^$.,;:!?…—–-()[]{}“”\"«»')
PROFILE = 'female-vais1000-native-piper1.8-aligned-v1'


def load_voice():
    graph = onnx.load(str(MODEL))
    add_alignment_output(graph)
    options = ort.SessionOptions()
    options.intra_op_num_threads = 2
    options.inter_op_num_threads = 1
    options.add_session_config_entry('session.intra_op.allow_spinning', '0')
    session = ort.InferenceSession(graph.SerializeToString(), options,
                                  providers=['CPUExecutionProvider'])
    config = PiperConfig.from_dict(json.loads(MODEL.with_suffix('.onnx.json').read_text()))
    return PiperVoice(session=session, config=config)


def groups_with_offsets(alignments):
    """Group actual phoneme sample spans at the phonemizer's word spaces."""
    groups = []
    current = []
    pos = 0
    for item in alignments:
        end = pos + int(item.num_samples)
        phone = item.phoneme
        if phone.isspace():
            if current:
                groups.append(current)
                current = []
        elif phone not in PUNCTUATION:
            current.append((phone, pos, end))
        pos = end
    if current:
        groups.append(current)
    return groups, pos


def phone_groups(phonemes):
    groups = []
    current = []
    for phone in phonemes:
        if phone.isspace():
            if current:
                groups.append(current)
                current = []
        elif phone not in PUNCTUATION:
            current.append(phone)
    if current:
        groups.append(current)
    return groups


def save_wav(path, samples, rate):
    with wave.open(str(path), 'wb') as f:
        f.setparams((1, 2, rate, 0, 'NONE', 'not compressed'))
        f.writeframes((np.clip(samples, -.99, .99) * 32767).astype(np.int16).tobytes())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--preflight', action='store_true')
    args = parser.parse_args()
    translation = json.loads((ROOT / 'translation.json').read_text())
    labels = ['THE AWAKENING', 'THE RULES', 'DAY ONE', 'BUILD. FAIL. ADAPT.',
              'BEYOND BOOKS', 'THE COMPANY', 'THE WORLD IS WATCHING',
              'THE UNKNOWN', 'ONE YEAR LATER', 'TIME']
    original = [{'label': label, 'text': ' '.join(p['en'] for p in chapter['segments'])}
                for chapter, label in zip(translation, labels)]
    voice = load_voice()
    mismatches = []
    unknown = set()
    for chapter in translation:
        for segment in chapter['segments']:
            text = segment['vi']
            phonemes = voice.phonemize(text)
            groups = [g for sentence in phonemes for g in phone_groups(sentence)]
            unknown.update(p for sentence in phonemes for p in sentence
                           if p not in voice.config.phoneme_id_map)
            if len(groups) != len(WORDS.findall(text)):
                mismatches.append({'chapter': chapter['id'], 'tag': segment['tag'],
                                   'text': text, 'words': len(WORDS.findall(text)),
                                   'spokenGroups': len(groups)})
    report = {'unknownPhonemes': sorted(unknown), 'wordMappingMismatches': mismatches}
    (OUT / 'phoneme-preflight.json').write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print('PREFLIGHT', json.dumps(report, ensure_ascii=False), flush=True)
    if args.preflight:
        return
    assert not unknown and not mismatches, 'Resolve all phoneme/word mappings before generating narration'

    scenes = []
    all_audio = []
    manifest = []
    global_frame = 0
    rate = voice.config.sample_rate
    for chapter, old in zip(translation, original):
        speed = .92 if chapter['id'] >= 8 else .95
        config = SynthesisConfig(length_scale=1/speed, normalize_audio=False)
        pieces = [np.zeros(round(.35 * rate), np.float32)]
        position = len(pieces[0])
        words = []
        beats = []
        utterances = []
        for index, segment in enumerate(chapter['segments']):
            text = segment['vi']
            beats.append({'from': round(position / rate * 30), 'tag': segment['tag'],
                          'phrase': text, 'sourceEnglish': segment['en']})
            key = hashlib.sha256((PROFILE + str(speed) + text).encode()).hexdigest()
            cached = OUT / f'chapter-{chapter["id"]:02}-beat-{index:02}.wav'
            metadata = cached.with_suffix('.json')
            if cached.is_file() and metadata.is_file() and json.loads(metadata.read_text()).get('key') == key:
                item = json.loads(metadata.read_text())
                with wave.open(str(cached)) as f:
                    assert f.getframerate() == rate
                    audio = np.frombuffer(f.readframes(f.getnframes()), np.int16).astype(np.float32) / 32768
            else:
                chunks = list(voice.synthesize(text, config, include_alignments=True))
                text_words = WORDS.findall(text)
                native = []
                spans = []
                cursor = 0
                word_index = 0
                for c in chunks:
                    assert c.sample_rate == rate and c.phoneme_alignments
                    groups, sample_count = groups_with_offsets(c.phoneme_alignments)
                    assert sample_count == len(c.audio_float_array), 'Alignment/audio duration mismatch'
                    for group in groups:
                        spans.append({'word': text_words[word_index].lower(),
                                      'fromSample': cursor + group[0][1],
                                      'toSample': cursor + group[-1][2]})
                        word_index += 1
                    native.append(c.audio_float_array)
                    cursor += len(c.audio_float_array)
                    # The model supplies sentence-final silence. Keep it intact.
                assert word_index == len(text_words)
                audio = np.concatenate(native).astype(np.float32)
                assert np.isfinite(audio).all() and len(audio) > rate * .12
                audio *= min(1, .90 / max(.0001, float(np.abs(audio).max())))
                fade = min(round(.002 * rate), len(audio)//2)
                audio[:fade] *= np.linspace(0, 1, fade)
                audio[-fade:] *= np.linspace(1, 0, fade)
                save_wav(cached, audio, rate)
                item = {'key': key, 'text': text, 'sampleRate': rate,
                        'seconds': len(audio)/rate, 'words': spans,
                        'timingMethod': 'VITS phoneme durations from the same synthesis forward pass'}
                metadata.write_text(json.dumps(item, ensure_ascii=False, indent=2))
            start = position
            for word in item['words']:
                a = round((start + word['fromSample']) / rate * 30)
                b = max(a+1, round((start + word['toSample']) / rate * 30))
                words.append({'word': word['word'], 'from': a, 'to': b})
            pieces.append(audio)
            position += len(audio)
            minimum_visual_beat = {'drawing': 1.6, 'software': 1.4}.get(segment['tag'], 0)
            pause_seconds = max(.12, minimum_visual_beat-len(audio)/rate)
            pause = np.zeros(round(pause_seconds * rate), np.float32)
            pieces.append(pause)
            position += len(pause)
            utterances.append({'text': text, 'tag': segment['tag'],
                               'fromSeconds': start/rate, 'seconds': len(audio)/rate,
                               'audio': str(cached.relative_to(ROOT)), 'key': key})
            print('FEMALE BEAT', chapter['id']+1, index+1, segment['tag'], round(position/rate, 2), flush=True)
        tail = 6 if chapter['id'] == 9 else .55
        pieces.append(np.zeros(round(tail * rate), np.float32))
        native = np.concatenate(pieces)
        frames = math.ceil(len(native)/rate*30)
        # Assemble once on a 24kHz grid: exactly 800 samples per video frame.
        n = round(len(native)/rate*24000)
        audio = np.interp(np.arange(n)/24000, np.arange(len(native))/rate, native).astype(np.float32)
        audio = np.pad(audio, (0, frames*800-len(audio)))
        beats[0]['from'] = 0
        text = ' '.join(s['vi'] for s in chapter['segments'])
        assert len(WORDS.findall(text)) == len(words)
        scenes.append({'id': chapter['id'], 'title': chapter['title'], 'label': old['label'],
                       'from': global_frame, 'duration': frames, 'text': text,
                       'originalText': text, 'sourceEnglish': old['text'], 'words': words, 'beats': beats})
        manifest.append({'id': chapter['id'], 'seconds': frames/30, 'speed': speed,
                         'utterances': utterances})
        all_audio.append(audio)
        global_frame += frames
        (OUT / 'progress.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))

    save_wav(ROOT/'out/narration-raw.wav', np.concatenate(all_audio), 24000)
    (ROOT/'src/timeline.json').write_text(json.dumps(scenes, ensure_ascii=False, indent=2))
    (ROOT/'out/qa/vietnamese-narration.json').write_text(json.dumps({
        'language': 'vi-VN', 'voice': 'native female VAIS1000 medium',
        'engine': 'Piper 1.8.0 / ONNX Runtime CPU, FP32', 'profile': PROFILE,
        'pitchShiftApplied': False, 'maleVoiceReused': False,
        'nativePausesPreserved': True, 'nativeSampleRate': rate,
        'alignment': 'Actual phoneme sample durations from the same audio inference; converted to 30fps words',
        'frames': global_frame, 'seconds': global_frame/30, 'manifest': manifest,
        'humanListeningApproval': 'not claimed; user authorized female narration and full video production',
    }, ensure_ascii=False, indent=2))
    print('FEMALE NARRATION COMPLETE', global_frame, global_frame/30, flush=True)


if __name__ == '__main__':
    main()
