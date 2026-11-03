# Independent review of the complete voice redo

Reviewer: independent QA agent. Scope: new narration provenance, script/caption preservation, timeline bounds, and supplied visual samples. No production code was changed.

## Result

No concrete blockers found in the reviewed source, generated audio provenance records, timeline, or supplied scene stills. Final encoded-file verification is pending the producer's completed render checks.

## Evidence

- All 12 chapters and all 18 narration blocks declare `PocketTTS-FP32`, native speed 1.0. `create-fresh-voice.py` constructs the PocketTTS ONNX configuration, references the supplied private voice prompt, and has no old ZipVoice fallback. Each block's adjacent JSON metadata identifies the new engine. The first block is byte-identical to `out/new-voice-opening.wav`; `test-new-voice.py` generates this sample using the new engine. Existing matching-signature caching is confined to these new-engine files.
- Original source words, manifest paragraph words, timeline text words, and concatenated caption words match for all 12 chapters after normalizing punctuation/case. Original text is retained verbatim in each timeline scene's `originalText`. No missing or duplicated script words were found in those text artifacts.
- All 98 captions have positive duration, start at or after scene frame zero, and end within their scene. The 12 contiguous scene intervals span frames 0–11232, totaling 11233 frames / 374.4333 seconds at 30 fps. Paragraph durations match native audio durations in the manifest.
- Audio-generation and assembly source uses no tempo filter or internal silence deletion. Synthesis applies headroom scaling and a 72-sample edge fade, then assembly inserts explicit short paragraph/scene gaps. The final chapter includes an additional two-second tail.
- ASR comparison reports paragraph similarity 0.9265–1.0. These are corroborating transcription measurements, not proof of perfect pronunciation or natural delivery. The approved opening's dedicated ASR report is 1.0.
- Reviewed all `scene-01-62.png` through `scene-12-62.png` and `rescue.png` in a contact sheet. Captions are legible against dark backing, stay inside the canvas, and do not cover the principal characters' faces. Rescue staging clearly separates the characters and passing truck. Frame ranges: chapter 1 0–624; 2 625–1329; 3 1330–2106; 4 2107–3053; 5 3054–3698; 6 3699–4516; 7 4517–5279; 8 5280–5881; 9 5882–7202; 10 7203–9298; 11 9299–9920; 12 9921–11232.
- Narration loudness report records approximately -17.94 LUFS integrated and -2.00 dBTP after normalization. Encoded master verification remains separate.

## Limits

I did not listen to the audio and cannot independently certify naturalness, voice identity, or frame-accurate spoken-caption synchronization. Caption timings are estimated from ASR segment durations and word-length weighting; valid bounds do not prove phoneme-level alignment. Stills cannot establish motion continuity. This review does not claim comparison against unavailable original visual brief, full storyboard, Gallery references, or licensing documentation. The user's approval of the new opening is recorded by the producer, not independently witnessed here.

## Completed encoded review

Final encoded-file checks are now available. Independent `ffprobe` inspection of `out/ten-seconds-smooth.mp4` confirms 1920×1080, 30 fps, 11233 frames and 374.433333 seconds. The producer's `smooth-encoding-report.json` records successful full decoding for both music and no-music exports, matching decoded-picture hashes, and -1.9 dBFS peaks for both. I reviewed the supplied encoded scene samples 2, 6, 9, 10 and 12: captions remain legible and within the canvas; scene artwork, road/car staging, rescue staging and closing composition show no concrete visual blocker in these samples.

Approved-opening provenance was rechecked after rendering. `new-voice-opening.wav` and `pocket-fp32-00-00.wav` still share SHA256 `3b8f062dc05841ae074edac27318378d7f63a528e876b0abc5bfaad7624adfbc`. This verifies that the first narration block is the new approved sample, consistent with the previously inspected PocketTTS generation source. User approval itself remains a producer-supplied fact.

Final disposition: no concrete blockers found within this review's scope. This update does not claim full listening, independent full decode, or perceptual certification of the complete narration.
