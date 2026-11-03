# Ten Seconds — approved voice with word-timed illustrations

All narration has been regenerated using the new voice selected by the user. The first chapter uses the exact newly approved opening sample; every remaining block is a fresh PocketTTS FP32 synthesis. No previous ZipVoice production audio is used.

The film keeps the original 12-scene English story and reference-style character. Native speech speed is1.0; there are no tempo filters, forced chapter durations, or internal silence-cutting filters. Current duration is6min14.43s at1920×1080/30fps. Scene transitions retain their native recording durations. Captions and narrative action cues now follow acoustic forced word alignment of that same recording; no audio was regenerated for the picture-sync revision.

## Run

```sh
npm ci
npm run studio
npm run render
```

Requires Node.js22+, ffmpeg/ffprobe and Chromium. `CHROME_BIN` overrides `/usr/bin/chromium`. The render helper uses four scene workers and assembles one continuous audio track. Frozen lossless FLAC files are included, so editing/rendering does not need a speech model or the private reference.

`src/Art.tsx`/`src/Scenes.tsx` define the character and motion. `src/timeline.json` is the shared timing/caption source. `src/Film.tsx` computes total frames from that data. `src/workbench.ts` enables Motion Workbench.

## Optional regenerate voice

Python dependencies: sherpa-onnx1.13.8, numpy and pocketsphinx==5.0.4 (for acoustic word alignment). Set `POCKET_MODEL_DIR` to the official PocketTTS2026-01-26 FP32 package, `VOICE_REFERENCE_WAV` to your private reference extract, and `WHISPER_MODEL_DIR` to the local Whisper tiny.en ONNX package. Run:

```sh
python tools/create-fresh-voice.py
python tools/align-and-assemble.py
python tools/mix-smooth.py
python tools/align-picture-cues.py
python tools/sync-events.py
```

The script is `tools/original-timeline.json`. Speech blocks are generated afresh for changed text/reference signatures. Only minimal edge fades and headroom scaling are applied before the continuous track's loudness normalization; phonemes and native pauses are preserved. Regeneration changes timing and requires a complete rerender.

## Provenance and checks

Script supplied by the user; character adapted from their uploaded reference. Voice synthesis: PocketTTS by Kyutai, ONNX export by KevinAHM, served locally through sherpa-onnx. Private reference media and model weights are excluded. See VOICE-MODEL-CARD.md for model sources/notices. The procedural underscore is original to this project.

Automated ASR, clipping checks, media decoding and independent sampled-frame review are recorded in the QA reports. They do not substitute for listening approval. The user explicitly selected the new opening sample before full-film production.

## Picture synchronization

`tools/align-picture-cues.py` aligns every original script word to the unchanged approved narration with PocketSphinx's English acoustic model at 16 kHz. Its 10 ms acoustic boundaries are rounded to the 30 fps picture grid. `tools/sync-events.py` requires exact spoken-phrase matches and writes event frames for all 12 scenes; missing phrases fail instead of silently using old timing. Captions retain the script's text, grouped for readability, with starts/ends derived from these word boundaries. Automatic alignment is an estimate, not a claim of human-certified phoneme precision.

The picture revision updates blink/future switches, coffee spill/sidestep, meeting/interview dialogue, phone fall/catch contact, crossing preview/pass, sports direction changes, confession, elderly entry/rescue/call, time horizons and closing cards. Audio, approved voice, playback speed, scene durations and script words stay unchanged. `qa/picture-sync-cues.json` lists the exact phrases and global times. `qa/picture-sync-verification.json` records encoded media checks and comparison with the previous approved audio stream.

## Saved deliverables

- [Finished film](deliverables/ten-seconds.mp4)
- [English subtitles](deliverables/ten-seconds.en.srt)
- [User-selected voice sample](deliverables/approved-voice-sample.wav)
- [Chapter markers](deliverables/chapters.txt)
