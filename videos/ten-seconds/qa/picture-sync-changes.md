# Picture synchronization revision

The approved English recording, music, scene lengths and script words are unchanged. Captions now use acoustic forced word boundaries rather than character-weight interpolation within ASR segments. Action switches are pinned to exact matched phrases; missing phrase matches stop the build.

Times below are local to each scene (seconds):

| Scene and action | Previous picture switch | Current spoken-word switch |
| --- | ---: | ---: |
| 4: boss asks “What do you think?” | 6.31 | 11.90 |
| 4: intelligent answer | 18.94 | 15.03 |
| 8: interviewer asks follow-up | 12.04 | 14.70 |
| 11: “Tomorrow” appears | 4.00 | 11.87 |
| 11: “Next year” appears | 8.00 | 12.63 |

The remaining narrative cues include blink/future/return switches, coffee sidestep, phone fall and catch, sports direction changes, confession, road entry/rescue and closing cards. Phone catch coordinates meet the unrotated rescue-pose hand; the elderly character begins on the sidewalk and steps into the road with the narrated entry.

`picture-sync-cues.json` contains all cue frames and global times. `picture-sync-verification.json` records media decoding, picture equality between music variants and exact encoded-audio preservation against the prior approved-voice film. Automatic word alignment and sampled frames do not constitute full human listening or phoneme-level certification.
