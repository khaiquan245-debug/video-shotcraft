# Ten Seconds — cinematic reference edition

A full 6:14 English illustrated story, rebuilt with camera grammar learned from two user-supplied reference clips. This is a separate edition; the earlier synchronized film remains in `../ten-seconds/`.

The 89-shot storyboard uses contextual wides, independent reaction portraits, over-shoulder framing, object/desk inserts, selective push-ins and short idea cards. Rooms and streets have layered perspective detail, practical light, warm/cool contrast and a restrained vignette. Prediction moments have localized eye light and temporal tint. All art is original SVG; no footage, watermarks or audio from the supplied references is embedded.

262 short caption phrases follow the existing acoustic word alignment, with a restrained current-word color and warm keyword highlight. The original 12 chapters and 1,162 script words are preserved. The previously user-selected English voice, native1.0 speech rate and original quiet score are unchanged; encoded audio equality is verified against the earlier film.

## Deliverables

- [Full film with music](deliverables/ten-seconds-cinematic.mp4)
- [Same film without music](deliverables/ten-seconds-cinematic-no-music.mp4)
- [English subtitles](deliverables/ten-seconds-cinematic.en.srt)
- [Chapter markers](deliverables/chapters.txt)
- [Design and reference breakdown](DESIGN.md)
- [Independent review](qa/cinematic-review.md)
- [Encoding and preservation checks](qa/cinematic-verification.json)

## Run

Node.js22+, Chromium and ffmpeg/ffprobe are required. No speech model, external media service or private reference is needed to render from the included FLAC tracks.

```sh
npm ci
npm run studio
npm run stills
npm run render
```

`CHROME_BIN` overrides `/usr/bin/chromium`. The render helper captures every shot, renders twelve chapter ranges using four isolated browser workers, concatenates the picture without re-encoding and attaches the frozen master audio. `tools/verify-cinematic.py` generates the no-music variant from the same encoded picture and the original narration source, checks both full decodes and compares the approved encoded audio. Set `APPROVED_VOICE_FILM` to another copy of the earlier synchronized film if it is not at the default adjacent repository location; the frozen baseline record can be used independently.

To rebuild storyboard/caption data from the unchanged timed narration:

```sh
python tools/build-shots.py
python tools/build-captions.py
```

`src/shots.json` is the frame-level storyboard. `src/timeline.json` is the unchanged chapter/action/word alignment; `src/captions.json` derives readable short groups. Camera targets clamp to stage bounds. All motion is deterministic; no random runtime state or remote assets are used. Editing script words requires a new recording/alignment rather than stretching the existing speech.

## Source and checks

`src/Art.tsx` provides the character and rebuilt environments; `src/Story.tsx` stages story actions; `src/Cinematic.tsx` defines camera composition, independent inserts, prediction treatment and lighting; `src/Film.tsx` assembles exactly the shot/caption tables. `src/workbench.ts` exposes the same assembly for visual editing.

Independent review covers reference adaptation, all shot stills, text/camera bounds, script preservation and sampled encoded scenes. Automated checks establish decoding, duration, frame count and audio packet equality. These records do not claim full human listening or exact phoneme-level alignment. User-provided reference videos and private voice conditioning are excluded. Voice-model provenance is in VOICE-MODEL-CARD.md; model weights are not distributed.
