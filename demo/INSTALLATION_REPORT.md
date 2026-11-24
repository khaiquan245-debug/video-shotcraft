# Installation and actual test report — Wyzowl SFX Director

Installed at: /workspace/video-shotcraft/.agents/skills/wyzowl-sfx-director
Repository module: /workspace/video-shotcraft/integrations/sfx_director
Automatic project instructions: /workspace/video-shotcraft/AGENTS.md (appended section; prior text retained).
Upstream: https://github.com/wyzowl/sfx-kit
Pinned revision: 92780e7ab0cdfb557497a988089c47f46e8c7412
License: CC0-1.0, including all sounds and metadata. No attribution required; source retained.

## Verified installation

320 WAV files, 28 categories, 67,486,986 audio bytes. All official SHA-256 values matched. All WAV headers/data were inspected: 48 kHz, 24-bit PCM, 228 mono and 92 stereo. No source sample clipping. Complete required upstream files were retained, including GUIDE, catalogue, schema, analysis, README and LICENSE. Git administration is outside the parent repository at /workspace/sfx-runtime/wyzowl-upstream.git to avoid an embedded submodule.

Dependencies already present: Python 3.12, NumPy, jsonschema, FFmpeg/ffprobe, Node/Canvas and Chromium. No paid API, subscription or cloud inference. No existing Video Shotcraft movie, rig, visual skill, subtitle or approved narration was edited. Only the new module/skill and the authorized project instruction section were added.

## Actual tests

- Eight behavioral tests passed: material selection, rate-aware sync, negative preroll, speech masking exclusions, explicit missing-asset reporting, disabled mode, output collision protection and locked voice spans.
- Full disabled-mode mix passed. Event list empty, SFX stem silent; original narration copy max float difference 0.0000001187.
- ATM demo: actual 10-second MP4, 1080×1920, 30fps, 300 H.264 frames, AAC 48 kHz stereo. 11 selected cues. -14.2 LUFS, -1.9 dBTP. No clipping, QC errors or warnings. Metadata sync error: 0.0 frames.
- Crane story: actual 35.5-second MP4, same resolution/fps, 1065 frames. 24 selected cues. -13.9 LUFS, -2.0 dBTP. No clipping, QC errors or warnings. Authored sync error: 0.0 frames. Original Vietnamese script retained.
- Actual encoded keyframes inspected: ATM insertion, two bills, reversal; crane salvage, fishing, exposed washed-out foundation, overhead pod transfer, descent and final ship base. Whole-file FFmpeg decode passed in pipeline QC. Fixed-length rig checks passed on rendered frames. Chromium playback logs are recorded separately after completion.

## Issues encountered and resolved

No repository download or networking failure. An attempted TTS call was refused because the matching native WAV already existed; its script/hash/model were verified and the file was reused without overwrite. First demo mix exposed transient crest factor and one masking window; added latency-compensated limiting when needed and 4 dB extra speech-driven effect attenuation, then passed QC. The first crane plan blocked a second splash due to a conservative repeat cooldown; the two distinct visible water contacts are 0.65 seconds apart, so the project cooldown was set to 0.55 seconds. Both use the actual compatible water asset. No unresolved missing assets.

## Limits and use

Automatic selection is local deterministic ranking of real Wyzowl metadata using authored visual markers; it is not automatic visual recognition or a general semantic model. Exact sync arithmetic does not itself verify the depicted contact. Encoded visual checks were sampled. Muted browser playback and numerical masking checks do not constitute human listening approval. Wyzowl describes these as original code-synthesized sounds, not field recordings.

Use: python -m integrations.sfx_director run --animation PATH/animation-events.json --voiceover PATH/working.wav --picture PATH/picture.mp4 --out-dir NEW_OUTPUT --name final-with-sfx.mp4
Switch off with --disabled or SHOTCRAFT_SFX_ENABLED=0. Existing movies remain untouched. All required models stay outside Git. New sources and weights are not pushed by this installation task.

Requested demo exports also exist directly at:
- /workspace/video-shotcraft/output/sfx-demo-10s.mp4
- /workspace/video-shotcraft/output/sfx-demo-10s.wav
- /workspace/video-shotcraft/output/sfx-timeline.json
- /workspace/video-shotcraft/output/audio-quality-report.md

The uploaded request was read completely. Its final section ends mid-sentence at “2. Kiểm tra giấy”; all fully specified tasks in sections 1–12 were implemented without inventing missing instructions.
