# Sources and credits
- Picture, character animation, room layouts and props: original local Canvas 2D rendering; newly authored for this film, with the creator's previous local character-rig code reused. Not a slideshow and not a generative-video provider output.
- Visual guidance: installed directing-stickman-videos A6 reference pack, inspected locally. No reference image pixels are composited into this film.
- Narration: user-selected Minh Quân / canonical Hải Đăng, VieNeu-TTS v3 Turbo (Apache-2.0), local ONNX CPU, SDK 3.8.4. Model https://huggingface.co/pnnbao-ump/VieNeu-TTS-v3-Turbo ; SDK https://github.com/pnnbao97/VieNeu-TTS . Exact narration and model provenance are included in narration-provenance.json.
- Codec used in original narration generation: OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano-ONNX. This codec does not change the narrator's model to VieNeu Nano.
- Music, room tone, heartbeat, latch, steps, cloth, transitions and bell accents: original NumPy synthesis for this film; no third-party music recordings or sound samples used. No Content-ID clearance guarantee is made.
- Caption timing: faster-whisper small, local int8 CPU; timestamps corrected to the approved script where ASR substituted four words. Inference model files stored outside Git. Recognition is not a human listening review.
- Titles and Vietnamese glyph coverage: system Noto Sans Display Bold, used instead of Latin-only condensed styling so Vietnamese marks render correctly.
- No creator watermark. No paid API or paid GPU. No environment publication or upload performed.
