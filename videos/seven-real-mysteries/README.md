# 7 Real Unsolved Mysteries and What the Evidence Actually Shows

A complete nine-section English documentary, horizontal1920×1080 at30fps. Original explicitly labeled illustrated reconstructions/diagrams instead of unverified archival images, as permitted by the supplied brief. All7cases in order, male narration based on the approved Solway speaker, natural phrase subtitles, chapter-specific original music and original local sound effects.

The historical-source access limitation and single contemporary-MH370 script edit are documented in output/asset_sources.md and output/script_changes.md. Current search status has NOT been independently verified; no2026 operational claim is made. This is an illustrated documentary adaptation, not a film using authentic archival photography. Claims about subjective voice naturalness are not based on ASR alone.

## Rebuild
Existing Node dependency link points to /workspace/video-shotcraft/workbench/node_modules; Python environment /workspace/ten-seconds-voice-redo/.venv/bin/python provides numpy/sherpa-onnx/pocketsphinx. Remotion4.0.484, installed Chromium, FFmpeg with rubberband/libx264/AAC. No paid service.

1. `python tools/narrate.py` (use the above venv) creates native voice chunks with same speaker reference as Solway. Then run tools/repair_hook.py once to preserve the short word Wow if the model omits it; the repair is idempotent and its provenance is recorded. Model/reference paths are local prerequisites, not redistributed.
2. `python tools/align.py` compresses verified quiet gaps, measures native rate, retimes to150WPM per new brief, aligns each word, exports narration and SRT. This explicit new long-form rate request supersedes native-speed short-form defaults for this project only.
3. `python tools/shotplan.py` then `python tools/timeline.py` and `python tools/captions.py` produce semantic shot table and storyboard based on actual words.
4. `python tools/score.py` generates original nine-theme score, sound cues, ducking and two-pass loudness-normalized stems.
5. `npm run typecheck`, `node tools/render.mjs --stills` then `npm run render`. Renderer creates one identical encoded picture stream and muxes full/no-music versions from it.
6. `python tools/verify.py` (venv) validates actual MP4s, complete decoding, audio peak, all aligned tokens, subtitles, ASR and source hashes. Independent final review in output/independent-review.md.

Scene design, requirements mapping and custom-component rationale in DESIGN.md; exact final frame table in STORYBOARD.csv. Source supplied prompt preserved in assets/reference. No UI recreation or Gallery-template resemblance claimed.

GitHub archive omits the optional standalone music WAV and intermediate48kHz narration WAV to avoid duplicate storage. Full files remain at /workspace/seven-real-mysteries. Music MP3, required24kHz narration WAV, and both fixed final render stems are archived. Re-running align.py and score.py regenerates omitted intermediates.
