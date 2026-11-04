# Independent final review — Vietnamese female edition

Reviewed 2026-11-04. **Current result: technical and sampled visual review complete; no required fix remains within that scope.** The replacement film has **16,166 frames / 538.866667s (8:58.87), 146 shots, 370 caption groups, 10 chapters, 171 narrative beats, and 2,364 spoken syllable tokens**. Historical defects are resolved and listed separately below. Perceptual listening and full real-time playback were not performed or approved.

This review applies to these completed replacement files, whose hashes and sizes were independently confirmed:

| File | Bytes | SHA256 |
| --- | ---: | --- |
| `out/learn-100x-vi.mp4` | 74,508,107 | `aae600a454ce0f4a0441a3fcd812c4ef9d6675fc0403d4916d043921a729900e` |
| `out/learn-100x-vi-no-music.mp4` | 74,080,745 | `2f712d5681d75b1d74c3ec122540566ba0789617593efe6acfc8b92b1e0ae34d` |

The reviewer did not participate in production or change production source/assets. This report is the only project file written by the reviewer. The latest Vietnamese/female instruction and `DESIGN.md` supersede the archived brief's English/male instruction. This is an original cartoon adaptation; no Gallery/template fidelity is claimed.

## Current evidence and method

- Read the archived brief, `DESIGN.md`, all 171 English/Vietnamese translation pairs, final storyboard/timeline/caption/SFX declarations, renderer source, narration metadata, all 171 native alignment JSONs and WAV headers, and both current verification reports.
- Reviewed all six corrected still contact sheets covering shots 000–145, with full-size follow-up on shots 029, 032, 077, 078, 091, 092, 095, 099, 128, 140, 141, and 145. Those stills precede the last caption/lock repair; current acceptance is based on the replacement encoded evidence below.
- Re-inspected **all seven regenerated encoded contact sheets**, covering **171 narrative-beat frames plus 3 ending frames** from the current replacement MP4. Full-size current follow-up included encoded beats 028, 070, 084, 097, 172, 173, 174, and the extra `encoded-football-caption.jpg`. The preceding encoded review also enlarged requirements/news/final-question frames 029, 101, 107, and 171; their unaffected pictures are present in the replacement sheets. Exact frame mappings are in `encoded-beat-index.json` and `encoded-ending-index.json`.
- Independently recomputed word/sample/frame preservation, native duration agreement, bounds/order, shot continuity, caption overlap, renderer keyframe rounding, all 370 SRT entries, source-stem decode/peaks, female-asset waveform reconstruction, MP4 metadata and hashes, picture/AAC packet hashes, and selected decoded audio cross-correlations.
- Read the producer's complete decode/black-gap/peak/whole-track AAC verifier and results. Those complete final-file decode checks were performed by the producer and were not independently repeated by this reviewer. The review distinguishes them from independent measurements below.

## Current numbered findings

1. **P1–P4/F1–F3/B1/C1 ✓ within sampled scope — Narrative and execution remain complete.** All ten chapters and all 171 translated beats are retained, including ordinary physical limits, official degree requirements, failed sales/uncertainty, physical practice, independent verification, scientific testing, family reflection, and finite time. All 2,364 written syllable tokens occur in the native alignment, timeline, and captions in exact order. Representative actual encoded evidence includes body limits at **f1145**, degree requirements **f2667/f2822**, drawing **f6709**, software **f8054**, knowledge tests **f9274**, expert verification **f9632**, and final question **f15938**. Sparse picture sampling cannot establish every instant of continuous staging.

2. **V1/V3/V4/B2 ✓ — Character and scene consistency.** The current encoded sheets preserve Stan's white face, spiky black hair, navy hoodie, dark trousers, and pale sneakers; the father, mother, brother, and childhood Stan remain distinguishable. Room geometry and the ivory/teal/coral/amber/navy palette persist across the story. Warm family scenes and cool diagrams follow `DESIGN.md`. No unrelated neon or Ink Press treatment was observed.

3. **B2/F3/Q6/Q11 ✓ for repaired main text/actions — Actual encoded semantic checks pass.** At **f2667, encoded beat 028**, the diploma padlock is now below the complete “VẪN PHẢI ĐÁP ỨNG” row. **f2822, beat 029**, shows degree-specific requirements; **f9274, beat 097**, shows advanced mathematics, reasoning, and solution presentation. **f6709, beat 070**, shows the drawing board/pencil with the isolated subtitle “Vẽ.”; **f6749, `encoded-football-caption.jpg`**, shows the football field and isolated “Bóng đá.” **f8054, beat 084**, shows “PHẦN MỀM” and actual code during “Viết phần mềm.” **f9632/f9981, beats 101/107**, retain complete expert/news/meeting labels inside their panels. Narrative headings are Vietnamese; literal programming code remains English intentionally.

4. **Q11/C1 ✓ for caption integrity — All 370 final captions match.** Independently verified all 370 SRT blocks against caption text and timing within **0.51ms**; all text is NFC, captions stay inside the timeline, and no groups overlap. All **2,364 absolute word start/end frames** exactly match the unchanged timeline after the final caption regrouping. Enlarged current encoded frames show intact Vietnamese accents and no observed subtitle clipping. The corrected still set's **141 caption-bearing samples** measured **59–76px** foreground heights; this is not a measurement of all 370 captions or of every illustration label. “Vẽ.” displays for 30 frames; “Bóng đá.” is a separate caption on the football scene. Smaller/background scene labels remain less prominent than the narration captions.

5. **A1/B1/C1 ✓ — Actual native phone-derived timing is internally consistent.** All **171 native WAV/JSON pairs** agree in duration. Word samples are ordered and within their utterance files. Every one of **4,728 word-boundary conversions** agrees with the assigned 30fps frame within **0.49932 frame**. All **146 shots** are contiguous, and all 146 keyframe-index entries match the renderer's exact `Math.round` convention. This is timing evidence from same-inference VITS phoneme durations, not an estimate from text length or a claim of exact lip sync.

6. **A1 ✓ — The actual narration source connects to the selected female assets.** Metadata selects native female **VAIS1000 medium / Piper 1.8.0 / ONNX Runtime CPU FP32**, with no declared pitch shift or male voice reuse. Independently reconstructing the raw track from all 171 native female WAVs and manifest placements matches **all 12,932,800 int16 samples** of `out/narration-raw.wav` exactly. `public/audio/voice.flac` matches the declared int16 conversion of the leveled WAV exactly across **25,865,600 samples**. Phase-aligned raw-to-leveled correlation is **0.997934**. This connects the actual asset chain; model identity and waveform equality do not establish narrator gender, accent, naturalness, or pronunciation by ear.

7. **A1/A6 — Source integrity and headroom verified; audibility unverified.** All five unchanged source FLACs fully decoded independently: **25,865,600 samples each, 48kHz mono, 538.866667s**, zero decoder errors, zero samples at magnitude ≥0.999. Sample peaks: voice **-2.999dBFS**, master **-2.597dBFS**, narration/SFX **-2.886dBFS**, score **-16.988dBFS**, SFX **-30.458dBFS**. These support technical headroom, not perceptual music balance or audibility of every effect.

8. **A1/A8/Q ✓ — Replacement-file properties and picture identity independently verified.** Both current MP4s are **1920×1080 H.264, 30/1fps, 16,166 frames, 538.866667s**, with **48kHz mono AAC** and stream starts at 0. Both picture streams have identical packet SHA256 **`ad803e69bdbc2135590bc2f5679a7372fea8f297fb35c91a2b0c590c7941af43`**. Current audio packet hashes were independently confirmed: main **`94f1ba7ee021bd7da9ce5b415db51919ee52f233eefc6f59c9e8267c077b8adf`**, no-music **`f13c661e636109c3df18164ed6808684ab29cc1363b6ef1bcedad007f823e19e`**. These are unchanged by the final visual repair. The no-music variant therefore has the same picture and retains the intended narration/SFX mix. The producer's current `final-film-verification.json` additionally records successful complete decode, no internal black gaps, decoded audio peaks **-2.595543dBFS / -2.867245dBFS**, and exact AAC packet agreement with separately encoded intended stems. Those complete decode and whole-track intended-stem comparisons are producer-performed checks, reviewed here rather than independently repeated.

9. **A9 ✓ within measured scope — No measured encoded audio offset or drift.** Independent decoded five-second windows at **2s, 280s, and 525s** were compared with their intended FLACs over ±0.2s using FFT cross-correlation. All six measurements have **0-sample / 0-frame lag**. Main correlations: **0.999988, 0.999976, 0.999964**; no-music: **0.999987, 0.999981, 0.999977**. These measurements were made before the final picture-only repair and remain applicable because both current AAC packet hashes are identical. The current hash-bound producer report separately measures the first 12 seconds at **0 samples**, correlation **0.999992**. This supports technical mux alignment; it does not approve the perceived placement of every SFX.

10. **R1/B3 ✓ — Clean final hold and fade confirmed.** **f15938, beat 171**, shows the final question with its caption. The last subtitle ends at **f15984 (532.8s)**; the native final utterance including pause ends at **532.7467s**. Current actual encoded ending frames **f16020/f16136**, evidence 172/173, show the unobstructed final question with no subtitle. **f16165**, evidence 174, is near black. Independent image-plane measurements show a stable card through f16136 and a one-second fade afterward: about **5.07s of clean post-caption hold before fading**, **6.12s** from utterance-file end to movie end.

11. **D1/D2/D5 ✓; D3/D4 inapplicable — Fictional material is appropriate.** The film uses authored cartoon diagrams, simulated stores, code, and invented figures. No real private customer page, address, credential, or personal dataset was observed in the reviewed evidence. No real-product screenshot fidelity is claimed.

12. **A10/S1 — Documented retained-audio exception.** `audio-authorship.json` identifies original procedural music and synthesized Foley, with local hashes and measured peak lags; it does not mislabel synthesis as field recordings. The current adaptation retains those existing authored assets. The generic skill's Freesound-only sourcing rule is not met by original synthesized effects; `DESIGN.md` records that exception. No third-party licensing approval or realistic Foley quality is inferred from the manifest. Source hashes were checked; provenance metadata is not a listening approval.

13. **A1/A2/A3/A4/A6/A7/V2 — Unverified perceptual/continuous qualities.** No perceptual listening or full real-time viewing was performed. Vietnamese pronunciation/accent, voice naturalness, narrator gender by ear, emotional delivery, joins, music masking, SFX audibility, perceived SFX/action fit, and continuous motion smoothness remain **unverified**. Exact lip synchronization is not claimed. Technical timing, selected frame review, and successful decoding must not be represented as a human listening or full playback approval.

## Aesthetic-rules coverage for the current film

| Rules | Current disposition |
| --- | --- |
| R1 | Final question, post-caption hold, and fade verified in finding 10. Product wordmark prescription is inapplicable. |
| R2 | No product-card flood; sampled action/diagram states serve the narrative. Continuous motion remains unverified. |
| R3 | Total length and chapter pacing follow the full story. Brief drawing/software states have explicit readable holds; actual frames verified. Perceptual rhythm remains unverified. |
| R4 | No whole-screen beat-pump treatment observed in source or samples; no full playback claim. |
| Q1–Q2 | Original 2D cartoon compositions; no real-product facsimile or 3D texture path. Enlarged sampled text edges are clean. |
| Q3 | Deterministic eased framing in source; no random handheld shake. Continuous motion smoothness unverified. |
| Q4–Q5 | No repeated glint/sweep, observed corner leakage, or competing opening ensemble. Opening establishes sleeping Stan and the brain premise. |
| Q6 | Repaired principal panels/labels fit in the sampled encoded compositions. Some background board fragments remain partially occluded deliberately by foreground props. |
| Q7–Q9 | Product orbit, product feature-family-photo finale, and flying UI insertion recipes are inapplicable. The recorded target is family reflection and a final question. |
| Q10 | Fictional papers and screens, with context-specific degree/test content now verified. No real document fidelity claim. |
| Q11 | Captions preserve Unicode and have no observed clipping; sampled foreground heights 59–76px. No blanket 56px measurement for all illustration text is claimed. Narrow main-label occlusions found during review are resolved. |
| S1 | Recorded cartoon/audio direction applies; original synthesis sourcing exception remains disclosed in finding 12. Perceptual style unverified. |
| S2–S5 | 37 cues declare source lag, action frame, gain, and duration; durations are explicit and under 5s. Current output offset is measured. Source metadata cannot establish audibility/perceptual fit of each cue. |
| C1 | All beats and words preserved; selected important scene/utterance matches verified. |
| C2–C3 | Product feature/tagline syntax and 3D annotations are inapplicable. Concrete narrative caveats and flat screen captions are retained. |
| P1 | Complete still-set review plus all 174 current encoded evidence frames via seven sheets and selected full-size checks. No full continuous viewing claim. |
| P2 | Original existing-film adaptation; no Gallery card/variant/reference fidelity claim. Final-review Gallery S1–S6 checks are therefore inapplicable. |
| P3 | Explicit Vietnamese/female direction is the applicable current instruction. No user listening approval was inferred. |
| P4 | Ten chapters/171 beats covered. Reused rooms and characters maintain narrative continuity; the specific unrelated insert was corrected. |

## Historical findings — resolved, not current blockers

These observations refer to superseded snapshots; their old frame numbers should not be used to identify the current movie.

- **Software insert:** initial **f8010, shot 078** showed an unrelated research checklist during software narration. Current **f8054** shows code and “PHẦN MỀM.” Resolved.
- **Contextual papers:** initial **f2843/f9256** used generic research tasks for degree requirements and university tests. Current **f2822/f9274** contain purpose-specific text. Resolved.
- **Untranslated narrative headings:** initial “BUILD SOMETHING USEFUL,” “IDENTIFY,” and “ENJOY THIS MOMENT” at **f3214/f7900/f15209/f15371**. Current Vietnamese headings verified in corrected stills and encoded sheets. Resolved.
- **Cropped news panel/counter:** initial **f9636/f10067** cropped main right-hand labels and phone count. Current **f9632/f9981**, plus corrected count evidence **f10125**, fit within their surfaces. Resolved.
- **Diploma lock overlap:** first encoded final **f2667** covered part of the third diploma row. Replacement encoded **f2667** has the lock below the complete row. Resolved.
- **Combined short captions:** previous encoded **f6709** displayed “Vẽ. Bóng đá.” on the drawing picture. Current **f6709** has “Vẽ.” and exact **f6749** has “Bóng đá.” on the football field. Resolved; final caption count is 370.
- **Upper lamp/shelf collision:** corrected six-language and childhood labels were moved into clearer space. Remaining contrast/size of small illustration labels is optional polish, not a missing spoken-caption defect.

The first preliminary snapshot had 16,108 frames/145 shots/374 caption groups. The intermediate corrected snapshot had 16,166 frames/146 shots/366 caption groups. Neither is the current 370-caption deliverable identified at the top of this report.

## Required, recommended, and unverified disposition

**Required fixes remaining: none identified within the technical and sampled visual review.** All specific required findings raised during this review have been rechecked in actual encoded replacement evidence and closed.

**Optional polish:** the short `rest` beat **f15265–15296**, sampled at **f15280**, uses the city/clock setting. It supports the ordinary-time theme; reusing the sleeping-room scene would be a more literal picture of resting. Small/background illustration-label contrast and occluded board fragments could also be refined. These do not remove spoken captions or narrative beats and do not require another render for this review.

**Unverified:** the perceptual and continuous-playback qualities listed in finding 13. This is a completed technical/sampled visual review, not human listening approval or full real-time viewing approval.
