# The Creepy Internet Photo That Was Finally Solved

Original 2D/2.5D-style vector animated Shorts production for the supplied English script. 1080×1920,30 fps,58.867 seconds. Assets are procedural SVG, not archival photographs. Forum, archive and map are labeled reconstructions. The monster passage is expressly fictional. One reusable navy-hoodie character rig supplies every appearance.

## Rebuild
Existing free tools: local PocketTTS FP32 through sherpa-onnx, PocketSphinx forced word alignment, NumPy procedural music/foley, FFmpeg, Remotion and local Chromium. No paid API used.

Use the existing Python environment `/workspace/ten-seconds-voice-redo/.venv/bin/python`. Generate native narration with `tools/voice.py`; run `tools/finish_audio.py` to fit all narration to the target window, write subtitles and mix procedural audio. Then `node tools/render.mjs` renders final assets and the clean thumbnail. `tools/configure.py` records initial script configuration; it is not needed for normal rebuilds. Models reside at `/workspace/ten-seconds/tools/sherpa-onnx-pocket-tts-2026-01-26`; existing English voice conditioning is `/workspace/ten-seconds/reference/prompt.wav`. They are not bundled.

## Outputs
- output/backrooms_short.mp4: full mix
- output/backrooms_no_music.mp4: narration plus effects
- output/backrooms_subtitles.srt: English captions
- output/backrooms_voice.wav: narration only
- output/backrooms_thumbnail.png: vertical thumbnail

Visual direction: muted yellow corridor, navy/white/black cartoon narrator, pale gold emphasis, dark-blue investigation panels; no actual historical image is claimed. Main movement changes by scene: corridor perspective dolly and flicker, animated forum stack, falling rig and retreating corridor, evidence pan and magnifier, archive-to-map location reveal, room-to-hobby-shop dissolve and moving RC car. Caption groups contain three words with active-word yellow highlight and reserve right/bottom interface clearance.

Limits: staged SVG environment changes use layer transforms/dissolves rather than a physically modeled 3D environment. The store and map are schematic illustrations. No rights-unclear images or commercial recordings used. Voice clarity and subtitle timing need both technical checks and audience listening; automated ASR is not proof of subjective naturalness.
