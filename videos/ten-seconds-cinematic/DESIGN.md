# Ten Seconds — reference-directed cinematic edition

## Brief and decisions

User selected the existing full English “10 seconds into the future” script after supplying two new reference videos. Autonomous production; keep all 12 chapters, original words, selected PocketTTS recording and native 1.0 speech speed. Maintain established 1920×1080, 30 fps output; references' portrait wrappers are not a new aspect-ratio request. Preserve the earlier film as a separate edition.

This is an illustrated narrative, not a product/UI promo. The supplied references directly define camera grammar; no Gallery card/template is claimed or required. Dedicated preliminary HTML styleframes are skipped because explicit visual references exist; render shot stills before the full encode. All scene art is original SVG, not extracted footage, logos or watermarks. Private reference media and voice conditioning files stay outside the repository.

## Reference inspection

Reference 1: 576×1024, 51.93 s. Reference 2: 576×1024, 183.90 s; the latter contains a wide narrative film within a portrait wrapper. Extracted approximately104 /92 evenly spaced frames respectively, plus full-duration overviews. Reviewed overviews and detailed sequences for camera changes, object inserts, reaction framing and lighting. This is a visual-frame study, not a claim of full audio listening.

| Technique | Reference evidence | Adaptation |
| --- | --- | --- |
| Wide → face reaction | First clip's street/office/neighbor exchanges; second clip's classroom and reaction portraits | Hard cuts to independently composed face shots, followed by contextual wide shots; native SVG sharpness |
| Object insert | First clip's phone alarm; second clip's grade paper, clock, guitar finger detail | Phone, coffee cup and time-horizon inserts anchored to spoken object words |
| Deliberate push-in | First clip's eyes/scan moment, second clip's face and clock | Shot-specific gentle 2–5% push; camera resets on a purposeful cut, not perpetual global drift |
| Perspective environments | First clip's street, balcony and kitchen; second clip's room/window/classroom | Rebuilt layered skyline and perspective room, foreground rails, window shadows, shelves, practical light |
| Superpower cue | First clip's teal eyes and scan ring | Localized eye light / temporal tint only when the story enters a future vision; return-to-present edge cue |
| Title/idea hold | Second clip's dark short idea cards | Sparse short cards at story pivots, with static reading holds |
| Brief subtitles | First clip's bold outlined phrase captions; second clip's green emphasized words | 3–7 spoken words per caption, warm keyword highlight and restrained word activity; acoustic word timing |
| Warm/cool contrast | Golden street/rooms versus blue night sequences | Warm daylight, cool prediction tint and darker rescue/call palette, warmer family ending |
| Portrait blur wrapper, watermarks | Both social uploads | Omitted: keep established clean widescreen film and original attribution-free art |

## Visual and motion tokens

Colors: midnight #101b2b, navy #223449, teal #78d6cf, warm ivory #f5eddb, coral #ef7868, amber #e9b68a. Retain the approved white-faced, spiky-haired navy-hoodie protagonist. New environmental colors extend these tokens with brown wall/wood and blue dusk gradients. Subtitles Arial bold 78px with dark outline; short labels 30px SVG minimum. World remains 1600×760 SVG within 1920×1080 composition, with intentional cinematic top/bottom safe areas. No persistent slide title, cream presentation border or chapter counter.

Camera grammar: contextual wide, medium two-shot, reaction close-up, object insert, narrative concept card. Cuts follow aligned speech and action; shot duration typically2–7s, longer breathing room in emotional ending. World cameras stay within the stage boundaries. Push amplitude2–5%, smooth ease-in-out; no random shake or repeated decorative glints. Mild vignette, practical light pools and sparse deterministic dust make depth; no copied source footage.

## Execution mapping and storyboard

`src/shots.json` is the complete frame-level storyboard and camera mapping; every record has chapter, local from/to, mode, target, zoom and rationale phrase. `src/timeline.json` retains original narration/action word timing. `tools/build-shots.py` requires exact script phrase matches; `tools/build-captions.py` derives short caption groups from the same words. `src/Film.tsx` is the only whole-film assembly.

All story functions preserved: premise, rules, coffee mishap, meeting, cat/phone, crossing danger, sports/flexible future, interview, confession, rescue/mother call, uncertainty and present-moment ending. Rescue's run/grab/pull/truck stays in a continuous readable wide shot. Dialogue remains contextual; close-ups are placed on setup/reaction beats rather than clipping an action.

Audio: reuse the exact approved master/narration FLAC tracks. No new voice or SFX is synthesized or sourced; existing quiet score remains. Both music and no-music exports use the same rendered picture. Verify full decode, bounds, audio packet equality with the prior film, caption words and original script preservation. Independent final review must check reference fidelity, changed camera samples and narrative synchronization, recording any unverified perceptual claims.

Final storyboard:89 shots and262 short captions. On-frame captions use78px bold type to maintain roughly56px capital glyph height; the persistent chapter label was removed after preflight review. Dialogue wraps within adaptive bubbles at30 SVG px.
