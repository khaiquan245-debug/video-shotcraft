# This Animal Has Three Hearts

45-second vertical animated educational Short. 1080×1920,30fps,H.264/yuv420p,AAC. Main output: output/octopus_three_hearts_short.mp4. Full narration text remains in script.json and VOICEOVER_EN.txt. User-supplied uppercase emphasis is preserved in the script, but speech synthesis receives normal-case words to avoid letter spelling.

## Voice continuity
Uses the exact PocketTTS FP32 model set, generation settings and reference conditioning file used for the preceding Harrison Okene project: /workspace/ten-seconds/tools/sherpa-onnx-pocket-tts-2026-01-26 and /workspace/ten-seconds/reference/prompt.wav. No voice model/conditioning switch and no pitch shift. Speech is generated locally at native tempo, with sentence pauses inserted and the resulting audio force-aligned. This establishes pipeline identity; subjective voice naturalness is not established by ASR.

## Artwork and science
No reference image package accompanied the pasted brief. All named canonical reference PNGs, diagram assets, STORYBOARD.csv, Vietnamese reference and source-note bibliography were absent. The production therefore uses an original editable vector rig, not a match to an unseen character sheet. Coral-orange mottled mantle, amber horizontal-pupil eyes, cream suckers and exactly8independently animated arm groups are reused in every scene. No external photos, stock footage or generated documentary images are used.

Two branchial hearts and paired gills flank a central systemic heart inside the mantle. Flow is schematic and explicitly not to scale. Hemocyanin/copper is presented as a simplified oxygen-carrier symbol rather than a molecular structure. The systemic heart alone briefly pauses in the swim inset; the two gill hearts continue beating and the main heart resumes. Crawling is a preference/effort comparison, not an inability to swim.

## Rendering
Free local tools: Remotion4.0.484,Chromium,FFmpeg,Python/NumPy,sherpa-onnx PocketTTS and PocketSphinx. No paid service/credits.

- Existing Python: /workspace/ten-seconds-voice-redo/.venv/bin/python.
- Run tools/voice.py, then tools/audio.py. Cached native WAV files are reused unless removed. Original model weights and conditioning are not redistributed.
- Run node tools/preview.mjs for actual5-second half-resolution preview and seven scene stills.
- Run node tools/render.mjs for final full/no-music MP4s with the same picture stream. Final limited-range yuv420p conversion follows the local Chromium renderer.
- Run tools/verify.py for speech recognition comparison, full script/word bounds, SRT coverage, frame count, format and full decode.
- Fixed public/audio stems allow picture re-rendering without generating speech again.

Visual plan: eye macro pulling out to3heart graphic icons; brief alien tease then same octopus reveal; mantle diagram with moving flow arrows and role highlights; blue-blood vessel macro and copper symbol; active swim/jet trails with transient systemic-pause inset; low seafloor crawl with alternating arm/cup contacts and separate layers; humorous recurring character with3heart icons/blue droplet and tight English ending. All movement is deterministic and frame-based.

Original synthesized underscore and Foley/heartbeats are made with NumPy and mixed below narration. No third-party audio recordings are used or represented as licensed source recordings. Freesound sourcing was unavailable without configured credentials; original synthesis is the documented free/local fallback.

Limits: stylized vector animation and schematic anatomy, not a scientific scan or fluid simulation. Character design is original because canonical reference assets were not supplied. Deep camera separation is created with layered2D transforms, not photoreal3D. Reports distinguish technical checks from subjective listening.
