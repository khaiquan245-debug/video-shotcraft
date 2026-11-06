# Independent review — Harrison Okene Short

Reviewed 2026-11-06. Independent reviewer did not edit production source. Basis: supplied master brief, video-shotcraft/SKILL.md §8, references/final-review.md, aesthetic-rules.md, src/index.tsx, src/timeline.json, asset_manifest.json, audio/render tools, six rendered midpoint PNGs and poster. Final binary checks repeated after replacement final-ready notice at 13:41 UTC; see bound artifacts below.

## Findings with evidence

- P1/P2 ✓ Survival story follows the six required narrative beats; exact supplied script appears in timeline. Timeline is 1,680 frames / 56 seconds at 30 fps. Directional scene timings were adjusted within the requested total.
- P3 ✓ Historical claims match the brief: Nigeria 2013 and May 26 (f300), approximately 30m/100ft (f300), eleven crewmates died (f615), rescue after approximately 62 hours (f945 and poster), pressure treatment (f1530). This checks agreement with supplied facts, not an independent primary-source historical investigation.
- F1 ✓ Cold open, capsized tug, survivor air pocket, 24/48/62-hour progression, discovery, and decompression all have implementations. At f1530 chamber and “PRESSURIZED TRANSFER → DECOMPRESSION” are explicit. No direct swim to normal surface recovery is shown in source.
- F2/B1 ✓ Six scenes advance the story. Cold-open hand scene returns as the brief explicitly requests a matching rescue reveal.
- V1/Q2 ✓ Restrained dark ocean palette, yellow emphasis and crisp sans-serif text are consistent across f75, f300, f615, f945, f1245, f1530. Original illustrated scenes and simple explanatory vector diagrams are visibly different levels of detail, but both remain illustration.
- S1–S6 N/A: No Gallery card/variant is used or claimed; exact-demo matching cannot apply.
- B2 ✓ Source applies separate glove reach, survivor-hand motion/finger closure, moving water, particles, boat rotation/descent, diver entry and pressure-transfer diagrams. This is more than a static image slideshow. Frame sequences for motion have not yet been inspected in the final encoded movie.
- B3 ✓ Final “62 HOURS. ONE SURVIVOR.” title begins after cue “moment” near f1590 and lasts until the final fade beginning f1665, allowing more than one second. No brand-wordmark or mass-element assembly applies.
- D1/D2/D5 ✓ No credentials, internal application screens or private customer data seen in inspected source/images. Public historical name is intentionally part of the brief.
- D3/D4 ✓ The public render reads only original illustration/layer files and local synthesized audio. asset_manifest.json says photos_real_included=false. assets/licensed_archive contains no files. Every inspected frame and poster clearly says “ILLUSTRATED RECONSTRUCTION”; no archival footage claim is made. External photo source links are references, not render assets.
- A1/A6/A7/A10: Audio tools create deterministic local ambience, bubbles, impacts and music, explicitly authorized by this user's brief. Source combines voice with low-amplitude beds, checks peak <0.99, and writes real WAV files. No subjective listening or voice-dominance claim is made here.
- A2 ✓ Source hand-motion onset follows the forced-aligned “grabbed”/“moved” word cue; the rescue impact uses the “moved” cue. Audio-cues.json records 42.633–42.933 seconds of all-track silence before “Harrison.” Perceptual sync remains unverified.
- A3/A9 N/A: This is not a strong-beat edit. Final encoded audio alignment still requires measurement if exact onset accuracy is claimed.
- A5 ✓ Entire prebuilt master track has the same timeline length; individual SFX are bounded procedurally rather than unbounded Remotion Audio sequences.
- A8 ✓ render.mjs produces both harrison_okene_short.mp4 (music) and harrison_okene_no_music.mp4 (voice/SFX), using the same limited-range encoded video stream. Final output existence/hash verification pending.
- Q1/Q6 ✓ Midpoint captions are within x70–900 with bottom 280px reservation. At f615 they stay below the face; f1530 caption does not obscure the chamber label. Main title and reconstruction label remain inside canvas. Poster is legible and does not cover the survivor's face.
- Q3/Q4 ✓ Source uses deterministic gentle camera transforms and narrative light beams; no global beat shake or repeated glints. Whole-movie transition smoothness is not established by midpoint images.
- Q9 ✓ Mitigated after independent finding: revised f75 was reopened. Expanded feathered background removal and dark underwater fade substantially conceal the wrist edge and residual silhouette. A faint straight wrist edge is still visible on close inspection; cosmetic, not a delivery blocker.
- Q10 ✓ Fixed after independent finding: revised f300 was reopened and the boat label is now sharp and readable, with inherited stroke removed. Revised f1530 shows the same illustrated survivor face inside the chamber porthole.
- R1/R3 ✓ Scene holds range 5–11 seconds, deliberate pauses are present in source, and final title has readable hold. Natural dramatic delivery cannot be certified by source inspection.
- R2/R4/Q5 ✓ Opening prioritizes hand contact; no mass-card animation or repeated full-frame slam applies. Linear environmental drift is an intentional underwater effect rather than UI entrance animation.
- Q7/Q8/Q9(landing)/C2/C3 N/A: Product UI, orbiting assets, multi-feature finale and 3D annotations do not apply to this documentary-style illustration brief.
- C1 ✓ Full narration is present in timeline, with subtitles generated from aligned words. Forced alignment provides timing, not proof that every word was pronounced correctly.
- P1 ✓ Six midpoint render PNGs and poster were independently opened with view_image. This report identifies their exact frame numbers.
- P2/P3/P4: No Gallery or external motion-reference fidelity claim; required repeated hand motif is brief-driven. Separate creative decision table/styleframe/mode record were not supplied to reviewer, so exact agreement with those documents is unverified.

## Severity and limits

No historical, rights-labeling, pressure-treatment or caption-face-overlap blocker found in the inspected material. The boat-text defect was fixed and the glove-cutout defect substantially mitigated, verified by reopening revised stills. Final movie format, complete decode and subtitle token coverage were verified below. Subjective naturalness, US accent, male voice impression, pronunciation, and sound quality were not listened to and are not approved by this review. The voice generator uses an existing Pocket TTS reference and tempo=1.0; this is implementation evidence only.

## Final encoded deliverables

- Q11 ✓ ffprobe: final main and no-music videos both 1080×1920, H.264, yuv420p, 30/1 fps, 1,680 frames, 56.000 seconds, AAC audio. Main audio is mono 48kHz.
- Q12 ✓ Main movie complete video/audio decode with `ffmpeg -v error -i ... -f null -` returned exit 0 and no error output.
- C4 ✓ Exported SRT includes exactly the same 120 aligned tokens as timeline, in order. This confirms exported coverage, not speech pronunciation.
- B4 ✓ Final-video extracted grip-01.png (f122) and grip-02.png (f1280) independently opened. f122 visibly has a hand-closing illustration gesture; f1280 clearly reveals the survivor and retains reconstruction labeling.
- Q13 ✓ Resolved in replacement final: new actual-video grip-01.png (f122) was reopened after final-ready. Added capsule digits and duplicated anatomy are absent. Original illustrated finger segments now shorten around their knuckles. This remains a simple 2D deformation rather than fully articulated hand animation, with no delivery blocker found.

Artifact SHA-256:

- `harrison_okene_short.mp4`: `06e89b37f80f6be1f653ecb885479d35c94b206949bd08ea34e48c0c742ee51e`
- `harrison_okene_no_music.mp4`: `9ba5e45e541749e5cc3b1a2c15d4d7ccf8bbb6fb5236ecfb4225f3647681ade3`
- `harrison_okene_voice.wav`: `96ea163ca1f88f0be833dfc990b2aded557671f3949be7238c6daf9cec4d55f2`
- `harrison_okene_subtitles.srt`: `775703a0b09f6a8feb9bab26e3f32871381c080405258f80e1b3cb53de0ea168`
- `harrison_okene_poster.png`: `f43ff2986f3212958e33aaebd4d9b1ee4dc7d88d776a5a4c7da853012da4a407`

- Q14 ✓ No-music movie complete video/audio decode also returned exit 0 with no error output.
