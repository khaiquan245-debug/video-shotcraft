# Independent cinematic review — pre-encode

Reviewed 2026-11-04. Inputs: DESIGN.md, full Film/Cinematic/Art/Story sources, timeline/shots/captions JSON, both reference overview sheets and 89 rendered stills (shot-000–088), final-review.md and aesthetic-rules.md. No production source edited. Final movie unavailable at review time; no claim of listening or continuous-motion viewing. Frame numbers below are 30fps timeline positions (shot starts unless specified).

## Findings requiring resolution

1. V1/Q11 ✗ f625 onward, e.g. shot-067: persistent top-left chapter label ('THE PHONE CALL') conflicts with DESIGN's explicit 'No persistent slide title' direction. It is also only 21px CSS. Remove it; sparse concept cards already communicate narrative pivots.
2. Q11 ✗ f2464, f5721, f6600, f8579: dialogue balloon font is 25 SVG px, approximately30px output before camera scale; long sentences are visually tiny. Essential dialogue is preserved in readable bottom captions, so this does not lose words, but the bubbles invite reading without meeting32px auxiliary threshold. Enlarge/wrap balloon text or remove redundant balloon text. Also opening secondary lines (28/30 SVG px) and future label27px are marginal; actual glyph height is smaller than fontSize.
3. Q11 caution: narration is56px CSS bold, but visible capital glyph height is approximately41px; the rule explicitly asks for56px effective rendered height. Current captions look clear at1080p and fit their safe area, but strict skill threshold needs a larger font (roughly76px Arial) and width verification. Treat as a guideline deviation only if explicitly documented; do not claim strict Q11 compliance from fontSize alone.

## Reference and narrative checks

4. P1/F1/B1 ✓ All12 story chapters remain mapped, from premise through present-moment ending. Frames0,625,1330,2107,3054,3699,4517,5280,5882,7203,9299,9921 retain distinct beats.
5. C1/F1 ✓ Programmatic normalized word comparison: every chapter's concatenated short-caption text equals timeline text, preserving all words (case/punctuation normalized,10→ten). This checks caption completeness, not acoustic intelligibility.
6. V1/P2 ✓ Reference1's wide→reaction and object insert grammar visibly appears (f175 cup,257 face,679 blink,7294 phone). Reference2's room perspective, practical lighting and dark idea-card grammar appears (f625 room,3616/5075/9809 concept cards). Warm/cool palettes and original protagonist remain coherent. No reference watermarks or footage are visible.
7. Q3/R4 ✓ Source has smooth2–3.5% shot-local pushes, no random shake or rhythmic full-screen pumping. Blink is a narrative eyelid mask (f679), with captions unaffected. Continuous-motion smoothness remains unverified until encode.
8. Q6/B2 ✓ Camera target clamps keep world view within1600×760. Across89 stills, no exposed stage edges, accidental face decapitation or cut-off essential captions. Face and insert compositions are independent, rather than simple global zooms. Deliberate clipping of protagonist legs in close-ups reads naturally.
9. B2/F3 ✓ Cat/phone action retains contextual views (f3161,3281,3362). Crossing retains vehicle context (f3883,4030). Rescue run/grab/pull/truck is allocated one continuous world shot f7863–8102; event sequence is local729 run,749 grab,768 pull,795 truck. Midshot still clearly presents protagonist holding elder. Full action sweep still needs encoded viewing to verify transient collisions/vehicle visibility.
10. R1/R3 ✓ Main opening card175f and ending concept cards85f/174f allow reading. Some opening object inserts are intentionally38–44f; acceptable as quick examples with matching captions, not detailed instruction. No product brand hold applies.
11. D1–D5 ✓ Original illustrated narrative; no live product data, keys, internal addresses, reference logos or watermarks in sampled artwork. Original media remain external to artwork. File/repository privacy policy outside visual frame review was not audited.
12. Q2/Q4 ✓ Native SVG edges and typography are crisp in sampled stills. Restrained vignette/light pools, deterministic dust, localized eye cue; no repeated decorative sweeps or broken rounded masks observed.

## Rules not applicable / not yet verified

- Gallery S1–S6: N/A. Project explicitly claims original narrative illustration, no Gallery card/template equivalence. UI screenshot/product functionality rules P3/Q1/Q2/Q7/Q8/Q9/Q10 and product slogan C2/C3 do not directly apply.
- R2: N/A, no bulk flying-card sequence. Q5: opening has one clear headline. P3: no ambiguous feedback action reviewed. P4: repeated camera grammar is appropriate narrative continuity, not repeated product claims.
- Audio A1–A10/S1–S5: unavailable perceptually. Source routes exact master/narration files with no new timing offsets; packet equality, clipping, decode and final music/no-music equivalence require final artifacts. No new SFX license claims checked.
- P1: key-still review completed; full encode, full-duration contact sheet, technical decode, final frame and transition sampling still required.

## Verdict

Pre-encode direction and still composition pass with the text/persistent-label issues above. Final delivery approval remains pending final movie inspection and technical/audio verification. No finding here establishes full audio listening, complete temporal continuity, or final-encode health.

## Updated still pass — final source, 06:13 UTC

Re-reviewed all89 regenerated stills, with full-resolution checks of shots000,022,050,067,084,088. The earlier findings are superseded as follows:

- V1/Q11 resolved: persistent chapter labels removed.
- Q11 narration resolved:78px caption font produces approximately56px visible capital height. Sampled long caption at shot050 fits comfortably within1920px width; text baselines and descenders remain above bottom edge. All89 samples have readable captions and no clipped words.
- Balloon issue resolved for composition/readability:30 SVG px text, wrapped into dynamic-height balloons; shots022 and050 contain complete lines with padding. Supporting bubble text is still secondary to full-size narration captions.
- B2/V1: family ending now uses Room environment. Emergency portraits show shock and later relief; single entrance eyelid cue removes duplicate blink masking.
- Optional only: central child's mouth is hidden behind serving plate at shots084/085. This is ordinary depth occlusion and does not block narrative understanding.

Updated verdict: no concrete blockers in final-source still pass. Approve progression to final encode. Full-duration temporal/technical/audio verification remains pending final MP4; this is provisional visual approval only.

## Final encoded review

Inspected17 decoded representative MP4 frames (`encoded-shot-*`), plus24 sequential samples at3fps across rescue f7863–8102 (`encoded-rescue-sequence.jpg`). Reviewed verification script and completed `cinematic-verification.json`.

- Q/P1 ✓ Encoded samples retain final-source composition, sharp SVG/text rendering, safe caption bounds and wrapped balloons. No reintroduced labels or stage-edge holes. Selected coverage includes opening, blink/reaction, meeting, cat/phone, crossing, sport reaction, interview, confession, phone call, rescue, uncertainty, dinner and ending.
- B2/F3 ✓ Rescue sequence explicitly shows run→contact/grab→backward pull→truck crossing foreground→safe hold in one continuous wide. Caption changes match corresponding action states in sampled frames; truck passes without apparent character collision. Evidence: encoded-rescue-sequence.jpg.
- Metadata ✓ Both exports1920×1080,30fps,11233 frames,374.4333seconds (6:14.43),12chapters,89shots,262captions,1162script words. Full shot coverage has no gaps and captions satisfy temporal bounds.
- A8 ✓ Music and no-music exports have identical compressed video packet hashes (`4bcdb02a…01dd4f6e`); picture is identical. Both fully decode with ffmpeg `-xerror`.
- A1 technical ✓ Both peak at−1.9dBFS, below clipping. Main export's encoded audio SHA256 `856bf00a565d26ce4fd14ef9b59ab45a9f8c3cf2966428d249caadde787a86a0` exactly equals approved-film encoded audio baseline. This establishes unchanged approved narration/music packets; no new voice or speed change inferred.
- Limits: no full listening performed; therefore no new perceptual assertion about voice quality, music balance or diction. Full real-time viewing was not performed; frame review and3fps rescue sampling do not prove every intermediate motion frame.

Final verdict: PASS for delivery based on reviewed visual samples, preserved script/captions, approved audio packet identity and complete technical decode. No blocking issue remains. Optional child/plate occlusion note remains cosmetic.
