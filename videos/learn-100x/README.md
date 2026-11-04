# What If You Could Learn100Times Faster?

A full English2D animated narrative based on the user's complete ten-scene production brief.1920×1080,30fps,9:51, all1610word tokens preserved. Stan retains the white rounded face, black spiky hair, navy hoodie and gray/white shoes. Father, mother, younger brother, teacher and researchers use stable role variants.

## Deliverable

[Complete MP4](deliverables/learn-100x.mp4), with synchronized English narration, original music and38 original short sound-design cues. [English subtitles](deliverables/learn-100x.en.srt) and [chapter markers](deliverables/chapters.txt) are also included. `brief.md` is the user's exact requested production brief; `DESIGN.md` records implementation decisions. `qa/independent-review.md` and `qa/film-verification.json` report review scope and measured checks.

## Render

Requires Node.js22+, Chromium and ffmpeg/ffprobe. Frozen lossless audio is included; no private voice reference or speech-model weights are needed to rerender.

```sh
npm ci
npm run studio
npm run render
```

`CHROME_BIN` overrides `/usr/bin/chromium`. The helper renders one muted range for each of the ten chapters and attaches the continuous mixed audio once, avoiding voice cuts between shots. `tools/build-story.py` derives the camera/beat table from exact phrase matches. `tools/build-captions.py` makes short readable phrase captions from the same acoustic word alignment. `src/workbench.ts` imports these tables for visual editing.

The final delivery repairs the classroom diploma card with a single same-frame-budget replacement chapter. `tools/repair-diploma.mjs` documents that assembly; a fresh `npm run render` already uses the corrected source, so the repair is not needed on a clean rerender. `tools/verify-film.py` checks both complete decode and script preservation, final hold, audio packet equality with the intended source mix, no internal black gaps, and an isolated opening-tick output-offset probe. A no-music working export retaining narration/SFX is generated for editing support; the primary deliverable is the requested complete mixed film.

## Audio and provenance

All new narration was generated with PocketTTS FP32, using the same voice conditioning previously selected by the user. A single0.94963 pitch-preserving tempo factor gently adjusts this recording; total delivery pace is163.45 words/minute. No paragraph is omitted or compressed to an arbitrary chapter target. The private reference and model weights are excluded. See VOICE-MODEL-CARD.md for upstream notices.

Music and effects are original procedural synthesis authored for this project; they are not third-party recordings or sampled reference-video audio. Freesound search returned proxy403Forbidden, so no downloaded replacement sound was silently substituted. `tools/score-and-sound.py` contains the synthesis recipes; `qa/audio-authorship.json` lists effect hashes and cue timing. The score progresses through curiosity, learning, business, adventure, ambition, tension, hope and intimate piano, with speech-responsive ducking and a gentle ending fade. Median score energy during active voice is approximately21.6dB below speech. Foley is intentionally subtle; synthesized effects are not described as field recordings.

Optional voice regeneration requires Python, numpy, sherpa-onnx1.13.8 and pocketsphinx5.0.4 plus separately obtained speech/ASR models. Set `POCKET_MODEL_DIR` and `VOICE_REFERENCE_WAV` before `tools/create-voice.py`; the alignment helper currently documents session model paths for Whisper. Generated files cache within ignored out/. Editing words requires regenerating and aligning voice before rebuilding the storyboard.

## Accuracy and review

Faster learning does not confer future prediction, physical speed, guaranteed money, automatic degrees or proven cures. The script's cautions remain in both narration and on-screen staging. The family, childhood memory and ordinary clock emphasize that knowledge does not multiply a lifetime. The final question holds for more than5seconds before fading.

Checks include normalized source/caption equivalence, independent unconstrained ASR coverage, acoustic word alignment, contiguous shot/caption bounds, full media decoding and sampled animated sequences. These checks and rendered-frame reviews do not claim complete human listening or exact phoneme-level certainty.
