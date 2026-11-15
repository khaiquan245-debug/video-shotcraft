# Repository-local installation

Source: https://github.com/kaomei/stickman-video-director

Upstream commit: `44873d1e9757c34c4db037e1d68c2a5548e2d7dc`

The complete `skills/directing-stickman-videos/` directory is vendored here,
including hidden configuration, scripts, references, examples, tests, fonts,
audio, and reference videos. Upstream file contents are preserved. The upstream
MIT license is included as `LICENSE`; asset-specific notices remain in place.

Existing Video Shotcraft files are unchanged. This is a regular Git directory,
not a submodule or a nested repository. Runtime dependencies in `node_modules/`
are local and must not be committed.

## Local setup and checks

From this directory, with Node.js 20+, npm, FFmpeg, and FFprobe installed:

```sh
npm ci
npm run doctor
node --test --test-concurrency=2 tests/runtime.test.mjs tests/b-style-workflow.test.mjs tests/audio-library.test.mjs
```

For the B6 Python renderer, use an isolated environment outside the repository:

```sh
python3 -m venv /workspace/stickman-runtime-venv
/workspace/stickman-runtime-venv/bin/python -m pip install -r assets/b6/hong-kong-v90/requirements.txt
export B6_PYTHON=/workspace/stickman-runtime-venv/bin/python
node scripts/autopilot.mjs doctor --style B6
```

Read `SKILL.md` before using the skill. Keep generated video projects outside
this installed directory, as required by its runtime.

## Installation verification

- All 1,884 upstream skill files matched byte-for-byte after installation.
- Every local Markdown link in `SKILL.md` resolved.
- The selected offline regression suites passed: 78 tests, no failures or skips.
  These include actual local rendering, cache, workflow, and audio-library checks.
- General, B4, and B6 doctor checks passed; B6 uses the isolated Python environment.
- Every vendored file is below GitHub's 100 MiB per-file limit. The complete
  upstream package contains 505,859,086 bytes, including its reference media.
- Upstream evidence files contain whitespace flagged by `git diff --check`.
  These files are intentionally preserved rather than reformatted.

## Cost constraint

The installation request prohibits paid APIs. Installation and local checks
do not authorize image, video, narration, or other billable generation calls.
Use local/offline tools and user-supplied assets. Director-mode proposals and
prompts can be prepared without generation API access. Autopilot generation
providers are not configured or verified by this installation.

## First use

Director mode prepares storyboards and standalone prompts; Autopilot combines
artwork, narration, captions, and animation into an MP4 using its selected
style's workflow. Browse the upstream
[Director styles](https://github.com/kaomei/stickman-video-director/blob/main/README.en.md#a-styles)
and [Autopilot styles](https://github.com/kaomei/stickman-video-director/blob/main/README.en.md#b-styles).

Example request: “Use directing-stickman-videos in Director mode, A3, 16:9,
30 seconds, to prepare a proposal about [topic]. Do not use paid APIs.”
