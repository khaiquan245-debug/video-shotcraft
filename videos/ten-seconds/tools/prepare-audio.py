from pathlib import Path
import subprocess
root = Path(__file__).resolve().parents[1]
for name in ["master", "narration", "score", "clock"]:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(root / f"public/audio/{name}.wav"), "-c:a", "flac", str(root / f"public/audio/{name}.flac")], check=True)
