# Ten Seconds — normal, continuous narration

English illustrated film at natural speech speed1.0×. Narration is regenerated in26 connected paragraphs, with shorter excessive silence and natural chapter breathing space. Chapter lengths follow the new speech; words are not stretched or squeezed to fill a preset duration. Current duration:8min06.77s, 1920×1080,30fps.

## Run

```sh
npm ci
npm run studio
npm run render
```

Requires Node.js22+, ffmpeg/ffprobe and Chromium. Set `CHROME_BIN` if Chromium is not at `/usr/bin/chromium`. The render helper uses up to four independent browser workers, caches scene renders under `out/parts/`, then joins the picture and adds the continuous master audio. `npm run render:single` uses the standard Remotion CLI instead.

`src/timeline.json` contains audio-derived chapters, captions and story cues. `src/Film.tsx` derives total frames from that timeline. `src/Art.tsx` and `src/Scenes.tsx` keep the reference character and animation. Frozen lossless FLAC audio is included, so normal editing/rendering does not require the private reference sample or any speech model/API.

## Optional regenerate speech

Install Python with sherpa-onnx1.12.26 and numpy. Supply the private reference extract and transcript with `VOICE_REFERENCE_WAV` and `VOICE_REFERENCE_TEXT_FILE`. Set `ZIPVOICE_MODEL_DIR`, `ZIPVOICE_VOCODER`, and `WHISPER_MODEL_DIR` to the official local models described in VOICE-MODEL-CARD.md. Then run:

```sh
python tools/create-smooth-voice.py
python tools/align-and-assemble.py
python tools/mix-smooth.py
python tools/sync-events.py
```

Speech is synthesized at1.0× from the script in `tools/original-timeline.json`. The assembler adds short paragraph/chapter pauses rather than a pause after every small phrase. Long source silence is shortened; speech timing is not compressed. Captions are aligned to recognized speech while retaining the script's words. Regeneration requires reviewing and rerendering the whole film.

## Provenance and checks

Screenplay supplied by the user. Character adapted from their video reference. Voice uses local reference-conditioned ZipVoice synthesis; exact speaker identity is not claimed. Reference media and model weights are not published. The procedural underscore is original to this project. See REFERENCE-ADAPTATION.md and the QA reports for the scope of measured checks; automated ASR is not a listening assessment.

## Saved deliverables

[Finished MP4](deliverables/ten-seconds.mp4) · [English subtitles](deliverables/ten-seconds.en.srt) · [Chapter markers](deliverables/chapters.txt)
