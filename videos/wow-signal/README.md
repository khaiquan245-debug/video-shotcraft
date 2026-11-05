# Wow! Signal

60-second 1920×1080 English narrated animated explainer. Full user script preserved in script.json. Six scenes, slow opening then escalating radio-search tension. Diagrams and printout are stylized reconstructions; 6EQUJ5 is the intensity code, not a decoded message. Natural explanations are hypotheses, not confirmed conclusions. Narration uses PocketTTS FP32 with existing approved English voice conditioning, gentle pitch lowering and continuous phrase timing aligned with PocketSphinx. Original procedural ambient score and radio-like effects; no historical radio recording is claimed.

Run tools/voice.py, tools/mix.py, then node tools/render.mjs with the pinned existing Remotion dependencies. Outputs: out/wow-signal.mp4 and out/wow-signal.en.srt.

Deliverables: [Video](deliverables/wow-signal.mp4), [no music](deliverables/wow-signal-no-music.mp4), [English subtitles](deliverables/wow-signal.en.srt). Timing: opening9s, followed by10/10/12/10/9s scenes, preserving every scripted sentence within60s. Runtime voice model and private conditioning clip are not included; existing public audio stems suffice for picture rerender.
