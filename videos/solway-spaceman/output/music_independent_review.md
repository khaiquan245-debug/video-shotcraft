# Independent music revision review

Reviewed2026-11-08. Technical/provenance checks pass for the scored revision. This review does not claim subjective listening or guarantee freedom from platform Content ID matches.

## Bound artifacts

- `solway_spaceman_scored.mp4`: SHA256 `11ea64b5b781c36e20c52f369140e6b8c15abf9ba42aa1f7503d77666efbab65`;9,670,189 bytes;43.800s;1314 frames;1080×1920;30FPS;H.264;AAC48kHz stereo.
- `solway_spaceman_music.wav`: SHA256 `40d29b5fc61b1a6463af66d6a0761a95feb50a9c989fb649914623f1652f4c3c`;43.800s;PCM16;48kHz stereo.
- `solway_spaceman_music.mp3`: SHA256 `bfefe7a499fdec8c6654c02c49cba52011994505778607f2601cad772d297614`;43.824s container duration including MP3 padding;48kHz stereo.
- Existing narration WAV: SHA256 `4878e29790380b2f19413c4fb914a77b77b1b20c4479f83e3648968c2a5a5e25`, matches narration reference in `music_report.json`.

## Checks

M1 ✓ Read `tools/score.py`, `output/MUSIC_LICENSE.txt` and `output/music_report.json`. Score is built from oscillator-based piano-like harmonics, detuned pads, bass and bell tones. No external audio samples, track downloads or third-party music files are loaded.72BPM/D-minor-add9 metadata is consistent with source.
M2 ✓ License text permits this requesting user to use/edit/publish/monetize the original music without required attribution. This is a project provenance statement, not a third-party stock license or a guarantee against accidental similarity/Content ID.
M3 ✓ Full FFmpeg decode of scored MP4, music WAV and music MP3 completed successfully without errors.
M4 ✓ Scored MP4 video elementary stream SHA256 is `5abf20d95d520f6028e3f674aa2e7f1262a4d76ac6b6e2f05bd39e4a2d3f479e`, identical to previously verified no-music/cadence revision. Picture, archival images, captions and timing are unchanged.
M5 ✓ Source mixes the existing `narration-sfx.wav` with the newly synthesized score, using narration-driven ducking and fades. No voice TTS, tempo or pitch change is made. Exact-script/cadence verification from `independent-review.md` continues to apply to unchanged narration; no new ASR claimed.
M6 ✓ Rendered scored AAC peak is−2.9dBFS and mean−17.6dBFS. No sample clipping indicated. Standalone source score peak0.78 and source mix peak0.724 agree with `music_report.json` within numerical representation.
M7 △ Reviewer has no listening playback capability. Musical character, narration masking, perceptual transitions and taste have not been independently auditioned; waveform measurements are not listening claims.
M8 ✓ No required technical correction identified. Previous visual/historical limitations persist: archival source203×300, explanation explicitly unproven, and minor omitted abstract search shot.

Canonical `solway_spaceman_short.mp4` had not yet been replaced when this review was bound; this report specifically approves the hash-named scored file above. If copied byte-for-byte to the canonical filename, the same checks apply.
