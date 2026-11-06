# The Man Who Survived 3 Days at the Bottom of the Ocean

Harrison Okene / Jascon-4, May2013. Original illustrated vertical short,56seconds,1080×1920,30fps. User script is preserved in script.json. Primary output is output/harrison_okene_short.mp4. Narration-only WAV, English SRT, clean poster PNG, and a no-music variant are alongside it.

## Assets and historical framing
Four supplied illustrations are used as source artwork; no real press images or rescue footage were supplied or downloaded. assets/real_photo_references holds links only, with uncleared rights. Every scene carries ILLUSTRATED RECONSTRUCTION. No illustration is called an authentic2013 photograph or video. The final camera icon refers to the historical rescue recording, not this animation.

Historical anchors:29-year-old Nigerian cook, tug capsized May26,2013,approximately30m/100ft deep, discovery approximately62hours later,11crewmates died. Controlled pressurized rescue and decompression are shown before normal atmospheric pressure; the edit does not show a direct unprotected swim to the surface.

## Rebuild
Free local stack: Remotion4.0.484, Chromium, FFmpeg/libx264, Python/NumPy/Pillow, PocketTTS FP32 (sherpa-onnx) and PocketSphinx forced alignment. No paid API or credits used.

1. Existing dependencies: node_modules links to /workspace/video-shotcraft/workbench/node_modules. A pinned package-lock is supplied.
2. Python executable: /workspace/ten-seconds-voice-redo/.venv/bin/python. Run tools/voice.py to generate or reuse original native speech and align it; then tools/audio.py to insert sentence pauses, re-align the edited narration, create the56-second timeline, SRT and music/foley mix. Running audio.py expects the baseline timeline from voice.py.
3. Run tools/layers.py to derive hand/glove layers from user art. No image-generation API is required.
4. Run node tools/render.mjs. It emits midpoint stills/poster, renders the full picture, converts full-range rendering to limited-range yuv420p, and muxes full/no-music AAC variants with identical pictures.
5. Run tools/verify.py for speech-recognition comparison, script/token bounds and full final-file decode/format checks.

Speech weights are already installed at /workspace/ten-seconds/tools/sherpa-onnx-pocket-tts-2026-01-26; existing voice conditioning is /workspace/ten-seconds/reference/prompt.wav. Models and conditioning are not redistributed here. Fixed narration and stems are in public/audio, so the supplied composition can be re-rendered without regenerating speech. Initialization helper tools/configure.py is optional and should not be rerun during a normal build.

## Execution / storyboard record
Autonomous implementation of the supplied six-scene brief; no Gallery card or template was selected.

-0–5s: separately masked glove and bare hand with timed curling original finger segments, torchlight, particles and perspective push. Match grip to spoken 'grabbed'.
-5–15s: supplied storm illustration rolls with animated rain/wave overlays; dissolve into a red/white procedural tug capsize and descent, with30m depth marker.
-15–26s: same supplied cook in an air pocket, camera drift, moving waterline, drops and a restrained memorial card.
-26–37s:24/48/62-hour graphic, shifting sky light, sun/moon progression, submerged tug; diver enters the wreck on the relevant spoken cue.
-37–46s: glove reach/hand movement match-cut to supplied living-survivor illustration. All sound is muted for0.3s directly before 'Harrison was alive'.
-46–56s: pressure bell followed by decompression chamber, then empty ocean with62HOURS.ONE SURVIVOR and reference to the real rescue camera recording.

Palette derives from supplied dark teal/ocean/rust art with pale-gold accents. Caption groups have at most2words and do not cross sentence boundaries. Bold white captions emphasize selected key words in yellow; right180px/bottom280px reserved for Shorts controls. Music, bubbles, drips, metal-like groans and impacts are deterministically synthesized locally; no commercial audio used. The first four images remain at original aspect ratio.

## Limits
Hand motion uses masks, transforms and segmented original fingers; pressure equipment and tug are schematic rather than precise engineering models. Raster source artwork has limited native resolution. Environmental depth uses 2D layer parallax/perspective, not a physically modeled3D simulation. Technical ASR and forced timing do not establish subjective voice naturalness or accent quality. Independent-review evidence and machine verification are included in output/.

## Motion revision (approved narration retained)
The user requested a complete illustrated revision while keeping the original script and voice. No licensed real media was provided; archival links remain unused. `output/unchanged-narration.json` records SHA-256 evidence that script.json, the narration-only output WAV and public narration WAV are byte-identical to the approved 017de3c version.

New scene2 cabin uses independently masked original head/body layers, breathing, slight head motion, three camera phases, foreground rising water/ripples/bubbles, drops and moving light. No facial-feature overlay is used. `tools/motion_layers.py` rebuilds these masks. The storm has independently moving wave layers; sinking uses a brief dip transition, rotating descending tug and bubble trails. The rescue hand receives a tightly framed camera push and a short settling motion at contact. The pressure chamber has subtle perspective movement and an animated gauge. Ending uses a clearly labeled illustrated portrait instead of a camera icon.

Captions use82px type and maximum2words per cue (at most2lines), with selected keywords highlighted progressively. `tools/revision_sound.py` changes only the background/effects mix, adding220ms pre-impact background dips and strengthened impacts; narration is preserved. For rebuilding this revision from the original audio mix, run voice.py and audio.py first, then motion_layers.py and revision_sound.py. To preserve the approved exact voice, normally use the fixed public/audio stems and simply render. `tools/upgrade_motion.py` is an implementation record, not a normal build step; do not rerun it on already upgraded source.
