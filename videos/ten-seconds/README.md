# Ten Seconds Into the Future

An eight-minute illustrated film adapted from the supplied English screenplay. 1920×1080, 30 fps, synthetic English narration, original music, and burned-in English captions.

## Watch and download

- [Finished MP4](deliverables/ten-seconds.mp4)
- [English subtitles](deliverables/ten-seconds.en.srt)
- [Chapter markers](deliverables/chapters.txt)

## Run and edit

Requires Node.js 22+ and npm. From this directory:

```sh
npm ci
npm run studio
npm run render
```

The rendered file is `out/ten-seconds.mp4`. Linux Chromium is configured at `/usr/bin/chromium`; adjust `remotion.config.ts` and the render script for another installation. To render without music, append `--props=props-no-music.json` to the render command.

`src/timeline.json` defines chapter and subtitle timing. `src/Scenes.tsx` and `src/Art.tsx` contain the editable vector animation. `src/workbench.ts` imports the same data for Motion Workbench. From the repository root, connect this project with:

```sh
node workbench/scripts/open.mjs videos/ten-seconds --no-open
```

The frozen audio is stored as lossless FLAC; no API key, speech model, or network service is needed to render the film. Render outputs and dependencies are ignored by Git.

## Optional: regenerate narration and music

Create a Python virtual environment and install `sherpa-onnx==1.12.26` and `numpy`. Download and extract the [Lessac medium model](https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-lessac-medium.tar.bz2) into `tools/`. Then run, in order:

```sh
python tools/narrate.py
python tools/mix.py
python tools/separate-clock.py
python tools/split-captions.py
python tools/balance-captions.py
python tools/prepare-audio.py
```

This regenerates the frozen audio, timing, and subtitles in `out/`. Rerender and review after regeneration. Models, intermediate WAVs, caches, and the Python environment are ignored.

## Provenance

Screenplay supplied by the user; illustrations, animation, and procedural score created for this project. Narration uses the synthetic English Piper Lessac medium voice through sherpa-onnx. See [voice model metadata](VOICE-MODEL-CARD.md), [original screenplay](script-original.md), and [production brief](DESIGN.md). No stock video or Freesound recordings are used.
