# Seven mysteries — native cadence revision

Latest user rejected the former voice/pause rhythm. Script unchanged. Same approved Solway male voice; native1.0 tempo restored. Quiet spaces are edited by clause/sentence/chapter punctuation, with conservative acoustic guards. No runtime padding or global slow-down. Actual duration in output/voice_report.json.

The earlier7–8min/150WPM brief is superseded by this correction. The original labeled illustrative reconstruction, MH370 current-status caveat and original music permissions remain.

Rebuild with /workspace/ten-seconds-voice-redo/.venv/bin/python tools/align.py, then tools/timeline.py, tools/captions.py and tools/score.py. tools/retime.py maps the prior approved encoded visuals at /workspace/seven-real-mysteries/out/limited.mp4 onto the revised speech timeline, covers the entire old subtitle band and burns new ASS subtitles. The original Remotion scene source remains for a fresh source render. Dependencies/weights/reference use the same existing local environment; no paid API.

Final outputs include mainMP4,no-musicMP4,narrationWAV,SRT,thumbnail,musicMP3,source and production reports. Independent review records technical evidence and subjective listening limits.

Archive omits optional music WAV and intermediate48k narration WAV to avoid duplicate storage. They remain in the local project and regenerate with align.py/score.py. Primary archived video source for retime.py falls back to sibling seven-real-mysteries/output/7_real_unsolved_mysteries.mp4.
