# Independent result review — red paperclip B6

Reviewer: independent agent `/root/review_paperclip_b6`, 2026-11-27 UTC.
Current overall status: **local sampled repairs verified; complete observation/acceptance pending**. Earlier needs-repair findings are retained below as history. This is not a completed 35-subcheck review, B6 equivalence claim, AV listening record, or user approval. See the final encoded sampling section for the exact assembled current candidate.

I read the installed `b6-dynamic-meme.md` and `b6-motion-review.md` references under `/tmp/stickman-video-director-install/skills/directing-stickman-videos/references/`. The originally supplied `/workspace/.agents/skills` location was unavailable. This review inspects actual native PNGs, separately rendered native one-frame probes through the unchanged trusted runtime, decoded primary-reference PNGs, and the old draft's contact sheet. It does **not** claim continuous original-speed playback or human listening. The parent has stopped native-06 for art repairs; its incomplete MP4 is not treated as a finished current candidate. These observations describe the pre-repair version and must be rechecked on its replacement.

## Media and actual evidence

- Primary: `project/reference/eiffel-portrait-v44.mp4`, 720×1280, 30 fps, 63.2 s. SHA-256 `b0047f5889a7ca1fd47097d8c8b3db054ef412e2f4a7297d3fe04fc1083e5d79`.
- Actual candidate PNG: `project/outputs/native-06/frame-0000.png`, 720×1280, with active visible caption.
- Current-source native one-frame probes, each created with `run.py frames --trusted-code --seconds 0.03333333333333333`, no runtime/source changes:
  - `project/outputs/independent-spot-contact/frame-0432.png` (14.4 s)
  - `project/outputs/independent-spot-corbin/frame-1125.png` (37.5 s)
  - `project/outputs/independent-spot-town/frame-1329.png` (44.3 s)
  - `project/outputs/independent-spot-tradeup/frame-0354.png` (11.8 s)
  - `project/outputs/independent-spot-house/frame-1437.png` (47.9 s)
- Decoded actual primary frames `review-evidence/reference-{00,10,45}.png`; `reference-sheet.png` is a locator only.
- `review-evidence/head-width-comparison.png` compares the candidate opening crop with primary t0 right actor, approximately normalized from a 270 px primary head width to the candidate's 180 px head width. Crops preserve proportions. This is a still comparison, not certification of all cast/poses.

## Repairable findings

1. **Painted environment mismatch, confirmed in full-size opening/contact/office/hall/house PNGs.** Large facade, sky, wall and furnishing regions use very flat fills and very clean regular contours. Primary t0 and t10 show locally varied pigment, uneven matte edges, modeled value/light within individual surfaces, richer architectural dressing and more irregular line pressure. The candidate faces/shirts have more local texture than their settings, making the head/body/environment treatment uneven. Repair artwork locally rather than applying a global grain or warm filter. Parent has acknowledged and begun this repair. New art still requires re-observation.

2. **Review correction: right-side supporting eyelines are inward.** My first full-frame read incorrectly described Corbin and the mayor as looking right. After the author challenged this, I re-observed enlarged actual PNG eye crops (`review-evidence/corbin-eyes.png`, `town-eyes.png`): pupils are left of their eye centers, toward Kyle/shared prop. The original gaze finding is withdrawn as a reviewer misread; no mirroring change is required. This is a review correction, not a repaired implementation defect.

3. **Trade-up board/hero-prop overlap, confirmed at 11.8 s.** The giant red paperclip overlays the board's central `TRADE UP` lettering. The separate top heading and active caption repeat the same phrase, so the beat remains understandable, but its focal hierarchy is cluttered. Move/reduce the hero prop, simplify the board lettering, or choose a composition where the focal prop and board do not obscure one another.

## Observations that do not establish a complete pass

- In the inspected 14.4/37.5/44.3 s contact stills, each participant has two visible arms and two planted legs; both hands meet the appropriate side of the single shared prop. I see no duplicate arm or disconnected wrist in these particular pictures. Supporting off-hands point down instead of extending outward. Shared-state stills cannot certify owner → contact → release or foot stability over time.
- The opening paperclip and final-house keys are recognizable. Active captions are large and readable, with white fill/dark outline, and sit across the lower torso region rather than over the prop. The sampled frames do not certify all cues, cue switches, font fingerprint, semantic timing or sound sync.
- Matched-head-width comparison does **not** show the candidate's limbs drifting to thinner V90 wire lines: candidate opening arms/legs are broadly at least as heavy as the compared primary character. Candidate limbs have less obvious pressure variation; primary face eyebrows/eye silhouettes also read bolder. This does not justify a universal thickness change or a full line-weight pass.
- In the contact probes, foreground lamp remains well left of the main hand/prop action. Tables are visually behind the actors; I do not see a decisive table-through-body or duplicate-limb failure in these stills. It remains necessary to inspect the complete action and occlusion transitions.
- The 47.9 s house is legible as a two-level facade, with keys held to the side. Its figure appears illustratively placed over the entrance rather than demonstrating physical movement through that architecture; no depth/travel pass follows from this picture.

## Unobserved requirements

The stopped native-06 has no completed full-range reviewed MP4. Original-speed full AV, contact approach/release, expression timing, camera acceleration/landings, new spatial information during travel, both sides of all cuts, the full cast/angle inventory, caption transition neighbors, and the 35 detailed gate entries remain unverified by this reviewer. The old low-resolution draft and source descriptions cannot close these items. Review the replacement native candidate with the same primary reference after the local repairs, retaining this failure evidence.

## Replacement native-07 initial observation

The author supplied exact-source checkpoint ranges `native-07-a` (frames 0–588), `native-07-b` (589–1042), and `native-07-c` (1043–1613), with new environment art and trade-up graphic repair. I viewed their first actual 720×1280 PNGs: `a/frame-0000.png`, `b/frame-0589.png`, `c/frame-1043.png`. This is fresh still evidence, not continuous playback.

- **Confirmed new top-coverage seam:** all three show a straight horizontal boundary at approximately screen y=199: flat sampled fill above, textured projected sky/wall below. It is especially obvious on the office wall and cafe sky. The background plate's top does not cover the viewport and its new pigment differs from the fill. Repair projected plate overscan/extension while preserving story object placement. This is a local coverage defect, not a reason to replace unaffected characters/audio.
- New facade and wall images show more localized pigment/light and architectural dressing than native-06. The original extreme flatness is reduced. The current repeated closed loops on window/table/furniture rectangle corners look decorative and mechanically repeated; pressure-varied imperfect contours in V44 do not generally produce the same loop at every corner. This remains an art-quality shortfall, with lower urgency than the viewport seam.
- Corbin's initial owner phase at 34.7667 s has one snow globe owned by Kyle, one visible near holding arm, and Corbin's arms down. The new PNG does not show a duplicate limb/prop. Shared and release phases still need consecutive/current moving inspection.
- **Interior ground registration concern:** in `native-07-c/frame-1043.png`, soles and their contact shadows sit at about y995–1000, above the painted baseboard/floor boundary (roughly y1008–1028), while the background table legs reach the lower boundary. This makes the actors appear slightly raised onto the wall region. Align the interior plate's painted ground with the actor ground plane and re-observe. This is a smaller staging concern, not a claim of incorrect bone anatomy; avoid shifting exterior actors indiscriminately.

## Replacement native-08 sampled repair review

Current sampled status: **specific local repairs verified in the viewed frames; complete motion/AV/B6 acceptance remains pending**. This supersedes native-07 for the local repair observations below while retaining its findings as history. No P0 anatomy, prop-ownership, layering or legibility defect was identified in these current sampled pictures.

Actual current 720×1280 frames viewed:

- `project/outputs/native-08-a/frame-0000.png`
- `project/outputs/native-08-b/frame-0589.png`
- `project/outputs/native-08-c/frame-1043.png`
- `project/outputs/independent-08-tradeup/frame-0354.png` (11.8 s), generated through the unchanged trusted `frames` command. Its `report.json` binds source fingerprint `12562253fd863feaf2376c70cc0a46f52204cd8500346ccb0cede7840af7d3f9`.

Observed repair results:

1. **Top plate coverage:** opening house, cafe generator insert and office owner-phase frames now show continuous pigment to the top edge. The old straight fill-to-billboard seam at y≈199 is absent in these pictures. The office cornice is a pair of authored wall lines, not the former pigment boundary. Remaining frustum extremes still need current full-range inspection.
2. **Repeated corner loops:** visible window frames, table edges and shelf corners no longer have the repeated closed curls from native-07. They use separate imperfect edges and join as recognizable material boundaries.
3. **Ground registration:** office soles/contact shadows now sit on visible floor below the baseboard; the background table's feet and actor feet no longer suggest the actors standing on the wall. Opening soles meet the porch step. These repairs are visible in the specific frames, not inferred from source changes.
4. **Trade-up prop/text overlap:** the actual 11.8 s current-source PNG places the red paperclip above the board with a visible gap. `ONE RED PAPERCLIP` and `TRADE UP` are fully legible. The redundant top heading is absent and the dialogue caption remains clear. The earlier obscuration is resolved in this sample.
5. **Artwork:** localized window reflections, facade siding, surface washes and simpler imperfect edges improve the old flat settings. This is a measurable local visual improvement; it does not establish strict whole-film equivalence with V44's denser painted architecture, bold face/ink hierarchy, value design or spatial performance.

The selected current frames retain a single recognizable prop, clear owner phase, clean down off-hands and readable caption lettering. They do not reveal a new P0 repair. Full intended-speed AV, all contact phases, expression transitions, meaningful world-route reveals, cut joins and the 35 detailed subchecks remain unverified by this reviewer. Do not convert these sampled repair observations into a full playback record, a formal broad pass or user approval. The assembled current full preview must still retain these same bytes/source and receive the remaining actual-media review.

## Final assembled encoded candidate — independent sampled review

Exact current video: `/workspace/outputs/red-paperclip-b6-20261127/delivery/Red_Paperclip_To_A_House_B6_EN.mp4`.

I independently verified its SHA-256 as `a8ac9645bbaa24599a11309effb13186a895cf8b633da0b3037e9eae6c27bdac`. `ffprobe` reports 720×1280, 30 fps, 1614 video frames, 53.800000 s, with an audio stream. The per-checkpoint authoring fingerprint supplied by the author and matching my independent 11.8 s probe is `12562253fd863feaf2376c70cc0a46f52204cd8500346ccb0cede7840af7d3f9`. Technical probe results do not establish creative acceptance.

I viewed **all 17 actual native-size decoded PNG samples** `qa-encoded/sample-01.png` through `sample-17.png`, in addition to using the contact sheet only as a locator. The actual `sample-index.json` maps these to global frames `[24,240,354,430,455,588,589,590,780,1008,1042,1043,1044,1125,1330,1450,1575]`.

Observed encoded results:

- The repaired sky/wall coverage remains continuous in the sampled encoded pictures. The old y≈199 fill/plate boundary and repeated closed corner loops do not reappear.
- Encoded frame354 retains a gap between the hero paperclip and board. Board words and caption are legible. Opening and house-payoff keys/clip remain recognizable.
- Fish exchange at430 shows both hands at opposite ends of one fish pen;455 shows Kyle holding that pen while the woman's hand has returned down. Corbin shared state at1125 and town shared document at1330 show a single central prop, correct inward supporting pupils and distinct hands. These are separate encoded state observations, not a continuous motion claim.
- The office/hall actor feet sit on the visible floor, and house opening/payoff feet meet the porch steps in the sampled frames. The earlier ground registration problem is absent here.
- **Checkpoint boundary 588→589→590:**588 is the stove insert's last frame;589 is a deliberate hard cut to the generator insert;590 continues that generator picture with the same caption and ordinary tiny movement. No black/garbled/intermediate wrong-source frame is visible in these decoded neighbors.
- **Checkpoint boundary1042→1043→1044:**1042 is the solo doubtful Kyle/snow-globe reaction;1043 deliberately cuts wider to Kyle plus Corbin;1044 continues the same new composition and active caption. No corruption, swapped identity, duplicate prop or seam is visible in these neighbors. This verifies the viewed join pixels, not intended-speed cut rhythm or audio continuity.
- White outlined caption lettering is readable in the active samples and clear of the main hand/prop action. Frames455,588 and1042 are subtitle-free; this alone does not diagnose unwanted caption flashing, since no current audio listening or complete neighboring cue inspection was performed.

**No new P0 repair was identified in this encoded sampling.** The previously confirmed local defects are resolved in the pictures actually re-observed. The whole-film moving result still has unverified acting/rhythm/depth requirements and a simpler geometric environment/face-ink treatment than the primary sample; this report makes no strict-match claim. I did not watch continuous original-speed AV or listen to the narration/mix, and I did not populate a formal 35-subcheck pass or infer user acceptance. The exact assembled file may be described as a **full-story native review copy**; this independent sampled review is not completed B6 creative approval.
