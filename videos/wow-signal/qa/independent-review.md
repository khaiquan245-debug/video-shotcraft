# Independent final review — technical and sampled visual scope

Scope: original historical explainer, English mysterious Wow! Signal story, low male narrator, slow opening then tension, 2D animation with 2.5D camera, space music/radio effects, 60 seconds. Reviewed script.json, src/timeline.json, src/index.tsx, README.md, tools/mix.py, tools/render.mjs and six supplied rendered keyframes. This report does not claim perceptual listening or full-speed playback.

P1/F1 ✓ Six narrative beats are present: detection, Ohio telescope, Ehman printout, Sagittarius/frequency, failed repeat searches/natural hypotheses, unresolved closing question. Evidence f120/420/720/1050/1380/1680.
P3/D1 ✓ f420 depicts two reflectors and labels the schematic; f720 calls 6EQUJ5 a signal intensity code and reconstruction; f1380/f1680 retain uncertainty. No decoded alien message or confirmed natural cause is asserted.
P4/F2 ✓ Each scene adds a distinct narrative beat. Product-specific goals/UI/Gallery mappings are N/A. No Gallery template fidelity claimed or verified.
B1 ✓ The six timeline texts exactly equal script.json. Scene lengths 270/300/300/360/300/270 frames are contiguous, total1800 at30fps (60s). Aligned word intervals stay inside their scenes.
B2 ✓ Wow! reveal is now keyed to the aligned spoken word onset at f839; it is absent at f720. Captions use four-word lowercase chunks without sentence punctuation, with occasional sentence-boundary joins; readable but less polished than script.
V1 ✓ The six inspected frames consistently use navy, muted teal and warm gold, clear flat schematic shapes and restrained light.
V2/Q-camera ✓ Updated source separates a stationary-depth starfield from a foreground SVG with perspective1800px, translateZ20→65px, and rotateY−1.2→1.2degrees, plus gentle scale. This supplies restrained2.5D foreground/background camera motion; keyframes remain readable.
D2 ✓ No personal/customer data, secrets or internal addresses visible in the reviewed frames. D3/D4/D5 product screenshot requirements N/A.
A1/A6 ? The source mixes narration, a55Hz-based ambient drone and original procedural radio noise/tones. Male timbre, intelligibility, music character, voice/music balance and actual SFX audibility are unverified without perceptual listening. Numerical gain cannot prove these qualities.
A2/A3/A9 ? SFX events are listed in seconds in tools/mix.py, but no output-offset correlation or beat-sync measurement record was supplied. This is a slow atmospheric story, not a beat-dense product spot; do not claim frame-accurate sound synchronization.
A5 ✓ Procedural tones are explicitly bounded at0.4s and noise bursts at0.09s; master waveform length is60s by construction.
A8 ✓ Final mixed and no-music MP4s both contain1800 video frames. Their copied H.264 video payload SHA256 is identical (79ebb1736e929a04274e8322c7400dd9589850f487ea2654768c9475fa647105), establishing identical encoded picture. No-music voice/SFX stem construction is documented; perceptual audio identity is not claimed.
A10 △ Disclosed workflow exception: The newly made SFX are procedural originals rather than the skill-required Freesound sources; README discloses the origin. No third-party licensing claim is made. This is a workflow deviation, not evidence of copyright infringement.

## Aesthetic rules

R1 △ Key information holds across long scenes, but continuous slight zoom means no literal static camera hold; no product wordmark applies.
R2 △ The main camera zoom is linear. Batch fly-ins do not apply.
R3 ✓ The9s opening supports the slow hook and all scene holds exceed3s. Perceived narration pace remains unverified.
R4 ✓ No global beat pumping, flash barrage or shake found in source.
Q1/Q2 N/A Product screenshot/3D texture reproduction is not used; vector typography appears crisp at the reviewed frames.
Q3 ✓ Deterministic slow camera scaling; no random handheld camera noise found.
Q4 ✓ No repeated glint/sweep or rounded mask spill found in six frames.
Q5 △ Opening presents Earth and a two-line information card together; coherent single story but not a single isolated object.
Q6 ✓ Essential labels face the camera. f720 printout tilt is mild and code stays clear.
Q7/Q8/Q9/Q10 N/A Product object close-up recipe, launch-family finale, layout-slot fly-ins and product-document reconstruction do not fit this historical schematic explainer.
Q11 ✓ Final regenerated samples use46px auxiliary fonts. Color-mask glyph bounds measure f720 caveat33px(y887–919), f1380 caveat33px(y903–935), f1680 cause34px(y835–868), meeting32px. f420 caveat is visibly comparable. Captions64px are readable; four-word grouping keeps f1050 single-line with a clear gap below the gold question.
S1 N/A Product tech-house/music recipe conflicts with the requested space mystery atmosphere; apply the user brief. Perceptual tonal judgment unverified.
S2 △ FX timestamps are centralized in mix.py, but lack frame-by-frame visual action annotations; no dense repeated Foley sequence applies.
S3 ? Picture/audio production ordering not independently verified.
S4 ✓ Source explicitly limits effect durations. Actual render audibility unverified.
S5 ? Output audio latency not measured in provided artifacts.
C1 ✓ All scenes have narration/caption word coverage; brief interphrase pauses are intentional.
C2 N/A Product benefit/tagline recipe.
C3 N/A No product page-space annotation system; foreground labels share the new perspective layer.
P1 ✓ Six rendered keyframes were independently inspected.
P2/P3 N/A No reference-motion fidelity or ambiguous-feedback work is claimed in this review.
P4 ✓ Six distinct story beats map to six scenes. Slow scale camera motion repeats, but the illustrations/information differ.

## Required fixes / review limitations

No required picture/story/completeness fix remains in the sampled final revision. The procedural-SFX exception is explicitly disclosed; retain this limitation in handoff rather than claim Freesound sourcing. Audio perceptual review remains outstanding.

Suggested: preserve sentence punctuation in captions, strengthen staged visual reveals for rising tension.

Unable to verify: low male voice and emotional delivery; perceptual music/SFX mix; continuous playback motion quality; output sound timing; source licensing workflow beyond documented procedural origin. Final files were independently probed and fully decoded without FFmpeg errors. This confirms technical decodability, not listening quality.


## Final artifact binding

- Mixed: `wow-signal.mp4`, SHA256 `7a9b3541d94c948c06fab1a051083689462b1da3d899dcc4e8222428e237823e`.
- No music: `wow-signal-no-music.mp4`, SHA256 `58d79425e3052716d485ef5560a65eb3106ea5163cd5d2c809271a175512e58c`.
- Both: H.2641920×1080,30fps,1800 decoded video frames; AAC48kHz audio. Both fully decode to null with exit0 and no errors.
- Picture and container durations are exactly60.000000s for both final files. The main file was remuxed with the original master audio; unchanged video payload SHA256 confirms prior sampled visual evidence still applies. The current remuxed main was independently fully decoded with exit0 and no FFmpeg errors.
- Final visual evidence inspected: frame-120.jpg, frame-420.jpg, frame-720.jpg, frame-1050.jpg, frame-1380.jpg, frame-1680.jpg regenerated from the final source. This is sampled visual review, not full real-time viewing or perceptual listening. Root verification.json was inspected: six unconstrained English ASR similarity scores are0.95,1.0,0.8421,0.9630,0.95,0.9730. These support broad script coverage, but the recognizer misrenders “astronomer Jerry Ehman” and one opening phrase; ASR does not establish exact pronunciation, timbre, delivery or mix quality. All listening limitations above remain.
