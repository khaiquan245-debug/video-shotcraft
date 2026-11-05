# Independent review — faster narration revision

Status: final faster narration and9:16 portrait revision independently checked, bound to the confirmed unchanged16:26 files below.

Scope: requested faster narration, corresponding video alignment, and subsequent1080×1920(9:16) Shorts rebuild. This revision intentionally changes the earlier60s pacing to46.3667s. No perceptual listening was performed; technical tempo changes are not a subjective judgment of naturalness or voice quality.

B1 ✓ All six scene texts exactly equal script.json. Normalizing1977→“nineteen seventy seven” and72→“seventy two”, every script word exactly matches the aligned word sequence. Forced alignment alone does not prove audible speech completeness; final unconstrained ASR is separate evidence.
B2 ✓ Scenes are contiguous with durations249/220/186/286/216/234 frames:1391f at30fps,46.3666667s. Every aligned word interval lies inside its owning scene. Dynamic composition duration derives from timeline rather than the previous1800f constant.
A1 ✓ tools/voice.py applies tempo.98 opening,1.03 middle,1.0 ending. The earlier pitch-shift filter is absent. Existing native voice files are reused, which preserves the same voice source while removing the earlier artificial slowing.
A2 ✓ tools/mix.py now derives master length and scene effects from the rebuilt timeline; render.mjs derives midpoint sample frames and mux duration from the same timeline. Narration.wav/master.wav/narration-sfx.wav each measure46.3666667s.
F1/P3/D1 ✓ All six story beats remain: two-reflector Big Ear schematic, stylized6EQUJ5 printout, Sagittarius/frequency, no confirmed repeat, unconfirmed cause. Vertical printout labels the reconstruction but omits the former explicit intensity-code caveat; no decoded-alien-message claim is made. Retaining an intensity-code label would improve historical clarity. Evidence f359/f562/f798/f1049/f1274.
V1/V2/Q3 ✓ Restrained layered2.5D foreground perspective over starfield retained, with deterministic gentle movement. No random camera shake or beat pumping found in reviewed source.
Q6 ✓ Rebuilt vertical midpoint stills f124,f359,f562,f798,f1049,f1274 inspected at1080×1920. No clipping of required text or illustrations observed. Captions are72px/four-word groups and auxiliary caveats46px. Some captions use two or three lines; f359's three-line panel overlaps decorative spectrum bars but leaves telescope and its schematic label clear. Suggest lifting those bars above1300px.
Q11 △ Text is visibly legible in reviewed portrait samples, but the skill's literal percentage-of-frame-height target is not fully met:72px subtitle font gives~52px glyphs versus~100px for5.2% of1920;46px auxiliary gives~33px versus~58px for3%. Applying the landscape percentage unchanged to portrait is a documented production-rule limitation; this report does not claim strictQ11 compliance.
V-Shorts ✓ Caption layout reserves80px left,180px right and300px bottom; panel bottom is1620px. Essential narrative text generally occupies upper/central areas, with no sampled caption-to-label collision. Top closing title reaches aboutx910 but stays within frame. Actual Shorts UI overlays were not rendered; platform safety is inferred from layout reserves rather than app playback.
B3/R1 △ Wow! appears at the new aligned word onset f636 and cuts at655:19f(~0.63s) on screen, shorter than the general1s key-information hold recommendation. This is a pacing tradeoff under the user’s faster revision; the intensity code itself remains visible for the full6.2s printout scene.
R3 ✓ Opening8.3s remains the gentle hook; remaining scenes6.2–9.53s are materially shorter than the prior10–12s holds. This is measured timing, not a listening assessment.
C1 ✓ Four-word captions cover all aligned words and the SRT uses revised timings. Minor polish suggestion: restore punctuation/capitalization and avoid sentence-boundary joins such as f124 “signal from space it”.
A8 ✓ Final mixed/no-music pair independently probed and decoded. Both contain identical copied H.264 video stream SHA256e301f38f513b7e91c3b992a42fd8a8ae750cf43bc9fa6d5451c832f4bc8f5d1e. Voice/SFX stem construction is documented; no perceptual audio-identity claim is made.
A10 △ Retained sourcing exception: radio/static effects and ambient drone are original procedural audio, not historical recordings or Freesound assets. No third-party license provenance is claimed.

Required fixes from inspected source/stills: no new clipping/story/timing defect for this pace/portrait revision. StrictQ11 percentage compliance is not claimed; see limitation above. Suggested: consider a1s Wow! hold if it does not undermine desired pace; preserve caption sentence punctuation.

Unverified: actual male timbre, perceived naturalness/speed, emotional tension, pronunciation, perceptual mix/SFX audibility and full-speed continuous viewing. Source tempo factors and later ASR must not be described as listening. Gallery/product-specific recipe checks are N/A to this original historical explainer; the earlier detailed independent review remains contextual evidence, with its old60s artifact hashes superseded for this revision.


## Confirmed final artifact binding

- `wow-signal.mp4`: SHA256 `65753feb36754622ae45508a4ce11ee184c72fa808121cee5bf0b8b965e212e5`.
- `wow-signal-no-music.mp4`: SHA256 `5f8b8e6e2e28371f78d3b34b7c89137dd444d91815221a028de5e3fc5880e543`.
- Both: H.2641080×1920(9:16),30fps,1391frames,46.366667s container duration, AAC48kHz. Both fully decode with FFmpeg exit0 and no errors.
- Encoded video payload is identical between versions, confirming unchanged picture. Sampled visual evidence is the final portrait frame-124.jpg,frame-359.jpg,frame-562.jpg,frame-798.jpg,frame-1049.jpg,frame-1274.jpg.
- Source/SRT/forced-alignment word checks establish script/timing consistency;32SRT cues concatenate exactly to the aligned word sequence and final cue ends46.367s.
- Faster landscape verification.json was inspected before portrait rebuild: six unconstrained ASR similarity scores0.95,1.0,0.8421,0.9630,0.95,0.9730. Audio source/timing is unchanged for portrait, but these scores are coverage evidence only and do not prove pronunciation or naturalness. The recognizer misrenders “astronomer Jerry Ehman” and an opening phrase. Root's final portrait verification is separate and may still be running; it was not substituted for listening here.

No subjective listening or actual Shorts-app overlay playback was performed. Technical and sampled-visual results above retain the disclosed procedural-SFX and portraitQ11 limitations.
