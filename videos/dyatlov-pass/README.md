# The Final Photos Before Nine Hikers Died

Complete55.4-second9:16 illustrated documentary about Dyatlov Pass.1080×1920,30fps,H.264/yuv420p,AACstereo. Main deliverables are output/dyatlov_pass_short.mp4, voice.wav, subtitles.srt, thumbnail.png and sources.md with the same dyatlov_pass prefix. Original standalone background music WAV/MP3 and music permission file are also supplied.

## Scope and sources
The uploaded source ZIP contains links and a download script, not photos. The user explicitly chose illustrations because archival photo rights were unconfirmed. No photographs were downloaded or used; every scene is clearly labeled. Source leads and rights decisions are in output/dyatlov_pass_sources.md. Original package documents are preserved as reference in assets/source-package; its downloader is not part of the build.

The exact six English voice-over paragraphs are in script.json and VOICEOVER_EN.txt. The scientific explanation remains a hypothesis, not a proven complete reconstruction. Nine illustrated hikers/memorial shapes represent the nine who died; the on-screen note distinguishes Yuri Yudin, who turned back and survived. No corpses, injury photographs, fake authentic portraits, monsters or invented witnesses.

## Free local stack and rebuild
Remotion4.0.484,Chromium,FFmpeg/libx264,Python/NumPy,sherpa-onnx PocketTTS FP32 and PocketSphinx. No paid API/credits. Existing node_modules points to the shared installed workbench dependencies. Pinned package/lock supplied.

1. Existing Python: /workspace/ten-seconds-voice-redo/.venv/bin/python. Run tools/voice.py to generate/reuse native utterances, then tools/audio.py to create calm connected narration, word alignment, SRT and original Foley.
2. Run tools/score.py for the original stereo score and voice-ducked full mix; it also exports standalone WAV/MP3. Same speaker model/reference as previous channel videos. Native pitch retained, tempo0.825 gives restrained delivery with no long scene padding.
3. `npm run preview` renders all scene stills and the thumbnail. `npm run typecheck` checks the actual src/index.tsx entry.
4. `npm run render` writes the final full-mix/no-music videos using one identical H264picture stream. A limited-range yuv420p conversion precedes exact-duration AAC muxing.
5. Run tools/verify.py with the Python environment for speech comparison, token/timestamp/SRT checks, format, duration and full decode.

The existing voice model path is /workspace/ten-seconds/tools/sherpa-onnx-pocket-tts-2026-01-26; conditioning is /workspace/ten-seconds/reference/prompt.wav. Weights/reference are not redistributed. Fixed public/audio stems allow rendering without speech generation.

## Execution design
Navy/cold blue/gray documentary palette, muted olive/brown1950s-style coats, canvas packs, wooden skis and old box camera. A shared nine-ID hiker rig maintains clothing/proportions. The source brief supplies visual direction, so the first cheap six scene stills serve as styleframes rather than an unrelated product-template exercise; no Gallery card selected.

- Hook: clearly illustrated nine-person picture card, camera shutter/brief black opening, moving snow, controlled push and restrained title change.
- Expedition: parallax mountain layers, nine walkers/skiers, tracking/boots macro/camera illustration timed to the spoken crossed/photographed/skiing/preparing cues.
- Camp: labeled illustrated camp panel, rotating shovel motion, cloth movement and daylight-to-night transition.
- Discovery: labeled tent reconstruction, restrained cut annotation, boots/clothes left behind, downward pan following footprints.
- Human loss: nine rear silhouettes fade into snow, then nine symbolic anonymous memorial frames; no gore.
- Scientific hypothesis: compact snow slab/weak-layer schematic shifts a short distance above a tent; exposure/cold demonstration; return to a labeled illustration and explicitly uncertain ending.

Original score:72BPM,E-minor/add9,soft pads/strings,piano,bass and quiet discovery tones; source oscillators only. User can use the music in monetized projects without fee/attribution; see MUSIC_LICENSE.txt. Stereo score ducks under narration. No third-party recording represented as licensed audio.

## Limits
This is an original vector illustrated adaptation, not archival footage or a historical photo restoration. Snow/tent/camera optics are schematic, not a physical simulation or reconstruction proven to reproduce the night. Illustrative faces do not identify actual individuals. Technical ASR does not certify subjective voice naturalness. Missing photo rights/source bytes were resolved by the user's explicit illustration-fallback choice.
