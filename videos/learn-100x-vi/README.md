# Học nhanh gấp 100 lần — bản tiếng Việt, giọng nữ

Complete Vietnamese adaptation of the English Learn 100× Faster film. The female narrator, camera timeline, subtitles, score and sound effects are regenerated together. All 171 narrative beats are preserved.

Published delivery: [video](deliverables/learn-100x-vi.mp4) and [Vietnamese subtitles](deliverables/learn-100x.vi.srt). Duration 8:58.867, 1920×1080, 30fps. Regeneration produces `out/learn-100x-vi.mp4` and `out/learn-100x-vi-no-music.mp4`; the second variant preserves the identical picture track and narration/SFX.

The model and Python environments are local production dependencies and are not included in Git. Install the exact recorded dependencies in `requirements-production.txt`, download the model named in `MODEL-ATTRIBUTION.md`, and run:

```bash
python tools/narrate-female-aligned.py
python tools/build-story.py
python tools/build-captions.py
python tools/score-and-sound.py
npm ci
npx tsc --noEmit
node tools/render-film.mjs
python tools/verify-vietnamese-sync.py --video
python tools/check-encoded-beats.py
```

Piper exposes native phoneme durations from the same audio synthesis pass. Vietnamese word groups are checked against all narration text; scene/caption timings are quantized to 30fps. See `DESIGN.md` and the QA JSON files for the precise methods and limits. `src/workbench.ts` makes the shots, subtitles, narration, effects and music available to the repository's visual workbench.

Keep uploaded reference videos, failed voice auditions, model weights, caches, virtual environments, and tokens outside committed deliverables. No token is needed in this project's files.

## Thumbnail

[Download JPG](deliverables/thumbnail-learn-100x-vi.jpg) · [Original PNG](deliverables/thumbnail-learn-100x-vi.png). Both are below 2 MiB. The generated artwork uses Stan from the film and Vietnamese headline typography.
