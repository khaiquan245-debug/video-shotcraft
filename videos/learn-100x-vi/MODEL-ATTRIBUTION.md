# Narration and sound attribution

Narrator model: `vi_VN-vais1000-medium`, one native Vietnamese female voice, 22,050Hz, FP32. Upstream distribution: https://github.com/k2-fsa/sherpa-onnx/releases/tag/tts-models (`vits-piper-vi_VN-vais1000-medium.tar.bz2`). See the included upstream model card.

VAIS1000 speech corpus: https://ieee-dataport.org/documents/vais-1000-vietnamese-speech-synthesis-corpus . Upstream model card identifies the dataset license as Creative Commons Attribution 4.0: https://creativecommons.org/licenses/by/4.0/ . Training was fine-tuned from the U.S. English Lessac medium voice. This production does not claim the voice belongs to the narrator of the reference video.

Synthesis software: Piper TTS 1.8.0 (https://github.com/OHF-Voice/piper1-gpl), ONNX Runtime and eSpeak NG, with their upstream software licenses. The model is locally loaded and patched in memory only to expose existing phoneme duration outputs.

Music and effects: original procedural compositions and synthesized Foley authored for the Learn 100× Faster production. Source recipe: `tools/score-and-sound.py`; hashes and actual cue times: `out/qa/audio-authorship.json` and `src/sfx-cues.json`. No third-party recording or reference-video soundtrack is embedded.
