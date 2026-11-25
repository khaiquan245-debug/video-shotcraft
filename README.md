# Rigby2D joint-animation demo

Download rigby2d_animation_demo.mp4:10seconds,1080×1920,60fps. Required order: idle/breath/blink0–2, walk2–4, run/decelerate4–6, crouch/pick up6–8, rise/surprise/camera gaze8–10.

Revised according to the user: both knees point forward; holding elbows face outward; no abrupt hand teleport at8seconds. Actual technical tests and remaining limits are in INSTALLATION_REPORT.md and JSON reports. Playback was muted technical playback, not human critical listening. No paid API/cloud inference.

hero-demo.rigby is the real editable23-bone/20-slot character and600frame animation, with separate embedded artwork and a weighted vest mesh. The full50clip native library exists in the Codex workspace at output/rigby2d/characters/hero-library-50-v3.rigby; it is not duplicated into this download-only branch. Source integration/skill remain in the working repository for review. This branch does not modify main or existing movies.

MCPserver was exercised overstdio(60tools), and explicitCodexconfig was recognized. The managed session did not automatically register it; CLI fallback is usable. Rule-based script matching and RMS lip sync are documented approximations, not universal story understanding or Vietnamese phoneme alignment.
