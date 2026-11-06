# VIDEOCRAFT / CODEX — MASTER PRODUCTION PROMPT (EN)

ROLE
You are an expert creative coder, 2D/2.5D animation director, motion designer, audio designer, and video-rendering engineer. Inspect this project and IMPLEMENT a complete vertical YouTube Short from the supplied reference assets and script. This is a real render request, not a plan or a static storyboard.

PROJECT
Title: This Animal Has Three Hearts
Audience: English-speaking US YouTube Shorts viewers
Genre: Surprising animal science / educational fun facts
Target length: 43–48 seconds (audio-sync first; do not abruptly cut narration)
Video: portrait 9:16, 1080x1920, 30fps, H.264 MP4, yuv420p, AAC audio
Language: Natural US English, clear energetic but not shouty male or female narrator.
Keep the entire delivered piece in English. The Vietnamese script file is for editorial reference only.

INPUTS (paths relative to this package folder)
- VOICEOVER_EN.txt — narration text; DO NOT rewrite or omit facts
- SCRIPT_VI_REFERENCE.txt — meaning/context only
- STORYBOARD.csv — timing, individual scenes, text overlays and reference paths
- assets/ai_reference/octopus_character_sheet_4poses.png — canonical appearance of the ONE same octopus
- assets/ai_reference/scene_01_intro_octopus.png — friendly pose
- assets/ai_reference/scene_02_swimming_octopus.png — swimming pose
- assets/ai_reference/scene_03_crawling_octopus.png — crawling pose
- assets/ai_reference/scene_04_eye_closeup.png — opening close-up
- assets/science_diagram/three_hearts_diagram.png + .svg — simplified science visual
- REAL_PHOTO_CC0_LINKS.md — optional REAL photo references, not bundled image files

CANONICAL VISUAL STYLE
- Main subject: one recognizable bright coral-orange/red octopus; mottled mantle, amber eyes, cream suckers, 8 anatomical arms. Keep color, eyes, head/mantle shape, arm markings identical across shots.
- Polished 2D cartoon/comic with delicate 2.5D depth: crisp thick contour, richly shaded water, cinematic teal ocean, rays, particles, layered foreground/midground/background.
- NOT a slideshow: purposefully animate arms with segmented deformation, eye blinks, mantle pulse, water particles, swimming jet, crawling suction, camera dolly/pan, diagram pulses and blood-flow arrows. Use reference images for style/identity and redraw or layer assets when necessary.
- Dynamic timing: change framing, action, or informative graphic every 1–3 seconds. No strobing, excessive camera shake or chaotic jump cuts.
- Text overlays are minimal, bold, English only, high-contrast, in safe area; render subtitles below focal action but above lower Shorts UI; max two lines at a time, not over the octopus face.
- Do not display misleading "real footage" claims for generated illustrations.

NON-NEGOTIABLE SCIENCE ACCURACY
1) Octopuses have three hearts: TWO branchial/gill hearts pump blood through the gills; ONE systemic heart pumps oxygen-rich blood throughout the body. Hearts are within the mantle/internal body region, NOT in the arms.
2) Octopus blood is blue due to copper-containing hemocyanin, a protein that carries oxygen.
3) When an octopus swims, its systemic heart can temporarily stop beating; visualize as a brief pause, not death, permanent cardiac arrest, or three hearts stopping. In the anatomy segment, two smaller hearts are located near the respective gills, systemic heart between them.
4) Octopuses often crawl along the seafloor and swimming is strenuous; do not imply no octopus can swim.
5) The anatomy diagram is simplified and is NOT to scale.
Editorial checks: Smithsonian Ocean and Smithsonian Magazine support heart/blood/swimming details; bibliography is in the source notes.

EXACT VOICE-OVER (en-US; line breaks denote pauses):
This animal has THREE hearts.
But that's not even the weirdest part.

No, it's not an alien.
It's an octopus.

Two hearts pump blood through its gills, where it picks up oxygen.
The third pumps that oxygen-rich blood through the rest of its body.

And unlike us, an octopus has BLUE blood, thanks to a copper-based protein.

But here's the twist.
When an octopus swims, its main heart can temporarily stop beating.

Swimming is exhausting, so it often prefers crawling along the ocean floor.

Three hearts. Blue blood.
And somehow, swimming is STILL too much cardio.
Nature is wild.

TIMELINE (guideline — conform final cut to generated voice timestamps)
SCENE 1 | 0:00–0:04 | Close-up octopus eye, black negative space, dramatic zoom, 3 bright graphic hearts appear. Text '3 HEARTS?!'. 3 short heartbeats, subtle bass impact.
SCENE 2 | 0:04–0:08 | 0.5-sec alien outline tease, smash reveal to the SAME orange octopus swimming into illuminated ocean. Text 'IT'S AN OCTOPUS'. Swipe whoosh.
SCENE 3 | 0:08–0:20 | Animate three hearts in the MANTLE: 2 gill hearts highlight, arrows through gills, then central systemic heart pumps oxygen-rich blood through body. Text '2 HEARTS → GILLS', then '1 HEART → BODY'. Do not put hearts in arms. Use science diagram as visual reference not necessarily as an immobile full-frame card.
SCENE 4 | 0:20–0:27 | Macro flow of blue blood inside stylized vessels, overlay simple copper/hemocyanin model. Caption 'BLUE BLOOD?!'. Very quick push-in, soft science chime.
SCENE 5 | 0:27–0:36 | The SAME octopus swims using jet propulsion; animate appendages and dynamic currents. A small translucent inset shows only SYSTEMIC heart briefly PAUSING while gill hearts keep pulsing. Text 'ONE HEART PAUSES?!'. Pull back, tiny audio dip, no flatline implying death.
SCENE 6 | 0:36–0:42 | Dynamic low camera tracking crawling octopus moving over rocks/coral, individual suction cups contact environment, 2.5D layers; text 'CRAWLING > SWIMMING'. Music becomes lightly playful.
SCENE 7 | 0:42–0:47 | Reveal all 3 heart icons + a blue blood droplet next to same octopus, exaggerated humorous expression, gentle zoom-out. Text '3 HEARTS. BLUE BLOOD.' End tightly on 'Nature is wild.' Show subtle subscribe icon only, no extra spoken CTA.

PRODUCTION REQUIREMENTS
- Inspect environment for existing VideoCraft/remotion/FFmpeg/Python assets and leverage installed free tools.
- Do not use paid services, watermark templates or unlicensed copyrighted tracks/media.
- If TTS can run locally (e.g., Piper or equivalent already installed), synthesize natural US English voice. If unavailable, find a locally implementable free alternative. If unable to generate voice, clearly report the blocker rather than falsely claiming a completed video.
- Generate per-sentence/word timestamps based on actual TTS; sync subtitles, visuals, and SFX with narration. Normalize spoken audio and duck background music below narration; do not clip the master bus.
- Make loop-friendly ending if possible. Maintain full motion, not a set of still cards.
- Add subtitles with clean bold font and occasional yellow emphasis on THREE, BLUE, PAUSES. No giant text wall; minimal logos.
- Avoid unsafe/copyrighted external downloads; supplied AI refs may be used. Optional real photo links only if license verified and local asset actually provided.
- Render a short preview and review generated video; then final render and use ffprobe for exact duration/resolution/audio verification.

REQUIRED OUTPUTS
output/octopus_three_hearts_short.mp4
output/octopus_three_hearts_subtitles.srt
output/octopus_three_hearts_voice.wav (if generated)
output/render_report.txt (duration, fps, resolution, voice present, music/sfx present, missing assets)
Keep editable project/source files and rerun command.

SUCCESS CRITERIA
Real MP4 with correctly synchronized script, 7 narrative beats, consistent 8-armed octopus identity, scientifically plausible heart diagram, real motion, strong 0–2 second hook, natural voice, clean English captions, smooth audio and scene transitions. If any requirement cannot be completed, say which and produce the best honestly validated working artifact without inventing files.

NOW IMPLEMENT, RENDER, VERIFY, AND REPORT THE RESULT. DO NOT STOP AT A PLAN.