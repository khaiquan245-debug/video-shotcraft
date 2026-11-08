# The Astronaut Who Appeared in a Family Photo

43.8-second vertical mystery documentary Short. Full supplied English narration retained; same PocketTTS FP32 reference/model as Harrison Okene and octopus videos. 1080×1920,30fps,H.264/yuv420p,AAC. Required outputs are in output/; source is src/index.tsx and src/timeline.json.

## Archival source and distinction
The user explicitly confirmed photo reuse permission, then supplied SOLWAY_FIRTH_PHOTO_FOR_CODEX.zip. Its PNG is the actual203×300historical photo, not generated art. assets/archival/solway_original.png and public/archival/solway_original.png are byte-identical to the supplied PNG. output/archival_manifest.json records SHA-256 and provenance. Attribution: Jim Templeton, May1964. This relies on user-supplied authorization, not a public-domain/CC claim. No other archival photograph or footage was downloaded or used. Full license/source notes: output/asset_licenses.md.

Photo bytes remain untouched. Frames, arrows/circles and magnified crops are separate annotation layers; the photograph is never reshaped into an astronaut or recolored to force a match. The Annie comparison uses a clearly labeled original cartoon reconstruction because no authorized second outing photograph was supplied.

## Historical qualification
The mother/viewfinder/overexposure demonstration is a proposed explanation, expressly not conclusively proven. The narration keeps 'Researchers believe', 'may have' and the final conditional conclusion. On-screen comparison says possible match, not proof. Illustrative newspapers are labeled as designed headlines, not archival newspapers. The viewfinder diagram is schematic, not to scale or a measurement of the actual camera.

## Production / rebuild
Existing free stack: Remotion4.0.484, local Chromium, FFmpeg/libx264, Python/NumPy/Pillow, sherpa-onnx PocketTTS FP32 and PocketSphinx forced alignment. No paid API or credits.

- Python speech environment: /workspace/ten-seconds-voice-redo/.venv/bin/python.
- Run tools/voice.py then tools/audio.py to create native speech, sentence pauses, actual word timing, separate WAV/SRT and original ambient/foley stems.
- Models: /workspace/ten-seconds/tools/sherpa-onnx-pocket-tts-2026-01-26. Existing reference voice: /workspace/ten-seconds/reference/prompt.wav. These are not redistributed. Fixed stems in public/audio allow direct picture re-render without speech generation.
- To import the user-authorized photo: system Python with Pillow, `python tools/import_photo.py path/to/photo.zip`. This preserves original bytes and updates src/media.json.
- `node tools/stills.mjs` produces scene/critical stills and thumbnail for review.
- `node tools/render.mjs` creates complete music and no-music MP4s from one picture stream, including exact-duration AAC muxing and full-to-limited-range yuv420p conversion.
- `tools/verify.py` checks ASR/script coverage, word bounds, SRT token order, codecs/frame count/duration and full decode.

## Visual execution record
Autonomous implementation of the supplied shot list, using original vector reconstructions rather than a product template or Gallery card.

1. Original photo after the requested0.25-second black/flash opening; controlled push toward background figure and red annotation circle at1.5seconds.
2. Shared girl/father rigs on windy marsh, wide/medium/girl close-up/over-the-shoulder/shutter macro staging.
3. Darkroom film strip, developing-photo reveal, original full frame alongside an unaltered magnified detail.
4. Moving designed newspaper layouts, labeled astronaut speculation icon, connecting world-map lines and a magnifier.
5. Annie cartoon portrait/dress with original mystery-detail comparison; left artwork explicitly reconstruction.
6. Same actors with mother facing away, schematic excluded-viewfinder band, pale-blue-to-white illustrated exposure, hypothesis/original-detail split and return to original full photo with qualified ending.

Palette: navy/charcoal for mystery, faded green/cream/brown for family scenes, restrained red/gold clue accents. Subtitles use76px bold type, maximum2words per group and up to2lines; right180px/bottom240px reserved. All labels and narration in English.

Audio is original deterministic synthesis, not third-party recorded Foley. Requested Freesound sourcing was attempted, but the configured proxy denied the destination with403Forbidden; see asset_licenses.md. The music follows quiet suspense → investigative pulse → restrained reveal, kept below normalized narration. No licensed-source recording claim is made.

## Limitations
The sole archival photo is low resolution203×300; enlargement is visibly soft and is not AI-enhanced. No second actual Annie photograph is available. Family faces/clothing are stylized and not claimed as authentic portraits. Camera optics and exposure are explanatory cartoons, not a validated recreation of Jim's camera. Technical ASR is not a subjective listening assessment.

## Continuous-cadence revision
The latest user instruction prioritizes continuous short-form speech over the former55–60second slot targets. The original native utterances, script, speaker conditioning, speaking tempo and pitch are preserved. Only low-energy interword spaces are shortened, recording-only edges trimmed, and artificial scene-end padding removed. Each scene follows the resulting narration plus0.1s tail (0.4s final). New duration is1314frames/43.8seconds. Actual longest aligned gap fell from4.167s to0.367s; there are no aligned gaps over0.5s. Captions, visual word cues, shutter timing, music ducking and reveal accents were rebuilt on this timeline. Metrics are in output/cadence_revision.json.
