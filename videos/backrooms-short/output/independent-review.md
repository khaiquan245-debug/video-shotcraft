# Independent final review

Reviewer did not implement the production. Reviewed 2026-11-05 against the exact attached Vietnamese brief, video-shotcraft SKILL.md §8, final-review.md, aesthetic-rules.md, README, src/index.tsx, src/timeline.json, tools/render.mjs and six rendered scene midpoint PNGs plus thumbnail. This initial section reviews the pre-final stills; final-file technical results will be appended after render.

## Evidence and findings

P1/P2 ✓ Subject and narrative match the Backrooms origin mystery. Timeline text preserves all six official narration paragraphs and order; target viewer is served by English text and illustrated mystery vocabulary.
P3/D1/D2 ✓ No customer or sensitive material observed. Forum image explicitly says ROOM ILLUSTRATION · NOT THE ORIGINAL PHOTO (f315); archive says RECONSTRUCTION (f1109); monster section says FICTION · NOT A REAL MONSTER SIGHTING (f655). No original archival photograph is falsely presented.
P4 ? No separate requirement-to-execution decision table, frozen design spec, or formal final storyboard supplied; README provides a concise production record. Cannot verify against missing approval artifacts.
F1 ✓ Six story stages present: room (f68), spread (f315), fictional horror (f655), investigation (f896), 2003/2024/Oshkosh discovery (f1109), hobby/RC reveal (f1504).
F2 ✓ Distinct information per scene; ending returns to the room as requested.
F3/B2 △ Some detailed storyboard actions are simplified: browser cards do not show a genuinely changing cursor/search; magnifier is an outlined lens rather than enlarged clue; map is a very schematic abstract polygon, not a readily recognizable USA silhouette, and lacks separate state-to-city zoom; no storefront orbit; no true character head turn/backstep. README accurately discloses schematic environments and layered dissolves. These are animation fidelity limitations, not full omission of the story.
V1/V3 ✓ Six frames consistently use muted yellow/olive corridor, navy hoodie, white face, dark panels and yellow emphasis. No unrelated product-template skin.
V2/B1 ✓ Timeline totals 1766 frames = 58.8667s. Scene boundaries 0,136,494,816,976,1243; brief explicitly permits shifting timings to spoken words. No Math.random or Date.now in visual source.
S1–S6 N/A Custom narrative vectors; no Gallery cards claimed or required, so no Gallery-fidelity assertion.
D3/Q1 N/A No real product-page reproduction. Original SVGs are appropriate under the user's explicit asset permission and remain labeled illustrations.
Q2/Q6/C1 ✓ Main titles and karaoke captions are sharp and legible in the examined PNGs. Captions are white bold sans serif, black outline/shadow, active word yellow, lower center; observed groups use one line. No caption clipping or face overlap in f68,315,655,896,1109,1504.
Q-composition △ f315: translucent repost windows cover most of hero's face. Captions do not cause it, but character readability is reduced. Move hero or reduce stack intrusion if revising.
Q-safe-area △ f1504: RENOVATION → RC RACETRACK begins around x24, insufficient visual breathing room for phone display; recommend two lines or smaller text. Caption panel overlaps feet only, not face.
Q-thumbnail △ Thumbnail at f65 includes the incomplete karaoke fragment 'real and nobody'; clean title-only thumbnail would read more deliberately.
R1/R2/R3 △ Main scene holds exceed one second; no batch deal animation requiring 0.5s settle. Continuous slight character bob and room dolly are stylistic, while 3D object-orbit/product-launch finale rules are inapplicable to this narrative horror brief.
R4/Q3/Q4 ✓ Source contains no beat-driven camera pump, random shake, repeated decorative sheen or uncontrolled glow. Intentional light flicker serves the horror scene. Temporal smoothness still requires final output sampling.
Q5 ✓ Opening has one clear subject: the corridor; title supports it.
Q7/Q8 N/A Asset-orbit and product-family finale are product-promo conventions, not requirements for this story.
B3 ✓ Opening title persists for 136 frames; no branded wordmark required.
A5 ✓ One fixed full-length master file is used by Remotion; mux script explicitly limits final output to composition length.
A7/A10 ✓ User explicitly permits synthesized sound effects and music, so procedural audio is authorized; Freesound sourcing is not required here. No commercial recording claimed.
A8 ? Script produces full mix and narration/SFX variants from the same rendered video; must verify both final artifacts exist and their picture streams match.
A1/A2/A3/A4/A6/A9 ? No subjective listening performed. Cannot certify natural US male timbre, suspense, narrator intelligibility, SFX audibility or perceptual sync from waveform/ASR alone. Technical audio measurements and final decoding remain separate evidence.

## Priority

Required before final acceptance: verify actual MP4 dimensions/fps/codecs/duration, full audio/video decode, existence of requested assets, and final narration not truncated. No critical clipping defect found in midpoint stills.

Recommended: avoid face obstruction at f315; add title safe margins at f1504; use clean thumbnail without live subtitle fragment; improve recognizable geography and character action fidelity if schedule permits.

Unverified: entire final temporal playback; subjective audio listening; archived historical assertions independently sourced; missing formal decision-table/styleframe/storyboard artifacts. Do not describe this review as a subjective audio listen or a pixel-level Gallery match.

## Revision recheck (17:08 UTC)

Updated scene-1.png f315 and scene-5.png f1504 visually inspected. Q-composition ✓ Hero redrawn in foreground at lower right; face is now unobstructed. Q-safe-area ✓ RENOVATION / RC RACETRACK is now two centered lines with generous margins. These confirmations supersede the earlier corresponding recommendations. Thumbnail recommendation and storyboard simplifications remain advisory.

Thumbnail recheck: new dedicated title/character thumbnail visually inspected; incomplete live-caption fragment removed. Q-thumbnail ✓ Clean text, sharp face, suitable margins. This supersedes the earlier thumbnail recommendation.

## First final-file technical check

Both initial final MP4 files fully decoded with FFmpeg exit 0 and no error output. ffprobe: 1080×1920, H.264, 30/1 fps, 1766 frames, 58.866667s; AAC mono 48kHz, 58.866s. Video packet hashes match across music variants (81b77ceadc18b50a983f8363ecac6d4e7cb646753bf6a3f6be7e42e23e736cf1), confirming same picture stream. Required correction discovered: both report yuvj420p/full range instead of explicitly requested yuv420p. Producer notified; hashes deliberately not treated as approved final until conversion.

## Corrected final acceptance


backrooms_short.mp4: SHA256 ffcd12ce0b6f858f70c246e912a0a8a9c5469bb6d9e62afbf8de5e7ffe20d251; 1080×1920, h264, yuv420p, range=tv, 30/1fps, 1766frames, 58.866667s; aac 48000Hz. Full decode exit 0, errors=''. Picture SHA256=bdf0e3664fbcece29c07a665f958f004eb4b12c4787274cbabb725b6817adfb2.

backrooms_no_music.mp4: SHA256 2e634ac321f87a7d343f11014e6b8fb461ed94f7e3e31c44d5895e09febcae54; 1080×1920, h264, yuv420p, range=tv, 30/1fps, 1766frames, 58.866667s; aac 48000Hz. Full decode exit 0, errors=''. Picture SHA256=bdf0e3664fbcece29c07a665f958f004eb4b12c4787274cbabb725b6817adfb2.

Final technical acceptance ✓ Both corrected outputs meet required format, decode without errors, and share identical video packet hash. Requested SRT, voice WAV and thumbnail exist. Narration text remains intact in timeline; producer reports final aligned word ends f1732, leaving34frames, but subjective voice naturalness and SFX balance remain unverified by this reviewer. The schematic map, layered dissolves and simplified gestures are disclosed limitations. No required technical/layout fix remains from this review.
