# Reference-conditioned voice

Engine: sherpa-onnx1.12.26. Acoustic model: ZipVoice Distill INT8 zh-en Emilia. Vocoder: Vocos24kHz. Four synthesis steps. Eight-second reference extract supplied by the user, with a locally transcribed prompt. The supplied sample is retained privately outside the public project.

Official model source: https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models
Vocoder: https://github.com/k2-fsa/sherpa-onnx/releases/tag/vocoder-models
Engine and examples: https://github.com/k2-fsa/sherpa-onnx
ZipVoice: https://github.com/k2-fsa/ZipVoice

Frozen FLAC tracks permit repeatable rendering without the model or reference sample. The voice aims to approximate the reference; perfect identity or indistinguishability is not claimed. Speaker-embedding and ASR reports are measurements, not a human listening assessment.
