# Independent reference adaptation preflight

Scope: source and supplied still-image review only; generation and final rendering are ongoing. This is not final delivery approval. Inspected REFERENCE-ADAPTATION.md, src/Art.tsx, src/Scenes.tsx, the original script opening, reference/character.jpg, reference/contact.jpg, and out/qa/character-match.png.

1. V1 PASS — The main character in character-match.png has the required white oval face, dark spiky hair, vertical oval eyes, navy hoodie, two drawstrings, outlined kangaroo pocket, black/dark trousers and grey-white outlined sneakers. These identity features agree with the supplied reference. No character identity blocker found. The stronger spikes and slightly longer proportions are acceptable adaptation differences; pixel identity is not required.
2. V1 PASS — The inspected still retains a cream presentation background, dark sans-serif chapter heading, outlined flat cartoon illustration and navy caption panel. The night scene is compatible with the reference contact sheet's use of dark interior scenes. Caption text fits in the inspected still.
3. B2 SOURCE CONCERN — In src/Scenes.tsx, scene id 9 changes the hero x position from 570 immediately before `grab` to 820 at `grab`; the rescue tween interpolates 820 to 820, so there is an instantaneous 250-unit horizontal jump. Inspect encoded frames immediately before/at `grab` and replace with an approach tween if the jump reads as teleportation. This is a concrete continuity issue in the current source, not yet verified against the final encode. The narrative needs a legible grab/pull before the truck passes; a frozen post-rescue still cannot establish that.
4. B1 PASS WITH LIMITED SCOPE — Source retains the Ten Seconds future-vision premise and its coffee, office, pet/phone, road, sport, confession, rescue/call and emotional ending scenes. It has not been replaced by the reference's reflexes lesson. This preflight did not perform a line-by-line full screenplay audit.
5. A1 UNVERIFIED — The documentation describes local ZipVoice conditioning on an eight-second user-reference sample. voice-similarity.json reports 0.2123 for conditioned versus reference and -0.0035 for the prior voice. This is supporting numerical evidence only; it does not prove matching speaker identity, naturalness, intelligibility or rhythm. No audio listening assessment was performed.
6. Q / A FINAL CHECKS PENDING — Final encoded frames, cross-scene character consistency, complete subtitle timing, transitions, rescue action, speech quality and final audio mix must be reviewed after rendering. The currently supplied still cannot establish those results.

Required before final sign-off: resolve or visually verify the scene 9 grab-position discontinuity; inspect final encoded contact sheets and rescue-boundary frames; complete final audio assessment with an appropriate listening path. No source edits made by this reviewer.

## Updated keyframe/source review

Reviewed the latest 12-scene contact-sheet.jpg, rescue.png, and full-size scene-02/03/05/06/09/10-18.png. These are renderer stills, not final encoded MP4 frames.

7. B2 RESOLVED IN SOURCE / STILL — Scene id 9 now approaches continuously from x=570 to x=990 before grab and retreats from x=990 to x=820 afterward. Elder retreats from x=1160 to x=985; both reach y=570. rescue.png shows the hero's extended arm meeting the elder at shoulder level with both above the road while the truck passes below. Truck faces its leftward travel direction. The original source discontinuity is resolved; final temporal verification remains pending.
8. V1 PASS — Across the contact sheet and additional full-size frames, main-character identity is consistent with the reference attributes. No new reference-character blocker. Navy versus coral clothing separates roles clearly.
9. Q DIRECTION ISSUE — Scene id 5 crossing uses a car moving from x=1650 to x=-300 while the default Car artwork faces right. The full-size scene-06-18.png confirms the right-facing nose; current source does not apply flip for this car. Recommend applying flip for the leftward pass to avoid a reversing-car reading. This is a local illustration/action issue rather than a character-match failure.
10. Q OPTIONAL — scene-10-18.png's large calling-phone inset partially covers the elder's left side/face. The MOM call is legible and the later rescue still is clear, so this is optional composition polish, not a blocker.

No new character or general composition blockers found in inspected stills. The final encode, transitions and audio remain unverified; do not treat this update as final readiness approval.

## Final encoded-frame review

Artifact: out/ten-seconds-reference.mp4. Inspected encoded-scene-2.jpg, encoded-scene-9.jpg, encoded-scene-10.jpg and encoded-scene-12.jpg, plus reviewer-extracted reviewer-crossing-f4848.jpg at global frame 4848 (161.6 seconds; scene id 5 start 4200 + pass 663 - 15).

11. V1 PASS — Encoded rules, confession, rescue and closing-family frames preserve the reference character's white face, black spiky hair, navy drawstring/pocket hoodie, dark trousers and grey-white outlined sneakers. Chapter typography and cream/navy presentation remain consistent. The rescue frame's dark hair has reduced contrast against the night sky but the face and silhouette remain readable; this is not a delivery blocker.
12. B2 PASS — encoded-scene-10.jpg shows the hero touching the elder at shoulder level with both on the upper sidewalk and the left-facing truck below on the roadway. This establishes the intended rescue outcome in the encoded artifact. Source approach continuity was already verified in the prior update; this still review does not claim continuous playback assessment.
13. Q RESOLVED — reviewer-crossing-f4848.jpg confirms the crossing car now faces left, consistent with the source's leftward pass. The previous direction concern is closed.
14. Q PASS — Inspected encoded frames show readable headings and captions without text cut-off, gross masking errors or missing character details. Confession preserves its emotional staging, and the ending retains the family-table image. No concrete visual delivery blocker found in these samples.
15. Q TECHNICAL REPORT CHECK — encoding-report.json records 1920×1080, 30 fps, 14400 frames, full-decode passes for both variants, identical video-stream hashes and measured audio peaks of -5.9/-2.9 dBFS. Container durations are 480.042667/480.000000 seconds. These are reviewed recorded checks, not an independently repeated full decode by this reviewer.
16. A LIMITED — The producer reports full-narration ASR similarity 0.9526. This supports text recovery but cannot establish voice identity, pleasantness, speaker resemblance or mix quality. Listening remains unverified, and exact speaker identity is not claimed.

Final visual result: no remaining concrete delivery blocker identified in the sampled encoded frames; earlier rescue-discontinuity and car-direction concerns are closed. Audio listening quality and continuous full-film playback are outside this review's verified scope. No code edits made.
