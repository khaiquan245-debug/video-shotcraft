# Wow! Signal

46.367-second 1080×1920 English narrated animated explainer. Full user script preserved in script.json. Six scenes, slow opening then escalating radio-search tension. Diagrams and printout are stylized reconstructions; 6EQUJ5 is the intensity code, not a decoded message. Natural explanations are hypotheses, not confirmed conclusions. Narration uses PocketTTS FP32 with existing approved English voice conditioning, native pitch and near-native tempo and continuous phrase timing aligned with PocketSphinx. Original procedural ambient score and radio-like effects; no historical radio recording is claimed.

Run tools/voice.py, tools/mix.py, then node tools/render.mjs with the pinned existing Remotion dependencies. Outputs: out/wow-signal.mp4 and out/wow-signal.en.srt.

Pace revision: 1391 frames (46.367 seconds), all original narration retained. Tempo is0.98 for the opening,1.03 for the middle and1.0 for the ending. Previous forced60-second slowing and pitch shifting were removed. Every scene, subtitle and radio cue was rebuilt against the new narration.

Shorts layout: portrait9:16,1080×1920, rebuilt scene staging rather than a crop; captions reserve180px at right and300px at bottom for interface clearance.

Deliverables: [Shorts video](deliverables/wow-signal.mp4), [without music](deliverables/wow-signal-no-music.mp4), [English subtitles](deliverables/wow-signal.en.srt). QA evidence is in qa/.
