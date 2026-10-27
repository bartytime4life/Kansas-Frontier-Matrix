#!/usr/bin/env python3
"""Build finite, attributed README previews from pinned Explorer recordings.

Requires Pillow and imageio-ffmpeg in an operator environment, not the app.
This transports recorded display pixels; it neither admits data nor benchmarks it.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

from PIL import Image
import imageio_ffmpeg

SOURCE_COMMIT = "bbcec824fe57e6be0409ba1e35d737fa99581560"
TOURS = {"water": "rivers-2", "terrain": "science-1",
         "groundwater": "underground-2", "history": "history-1", "wind": "weather-2"}
WIDTH, HEIGHT, FPS = 960, 540, 8


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-checkout", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    app, out = args.app_checkout.resolve(), args.output.resolve()
    commit = subprocess.check_output(["git", "-C", str(app), "rev-parse", "HEAD"], text=True).strip()
    if commit != SOURCE_COMMIT:
        raise SystemExit(f"Expected {SOURCE_COMMIT}; received {commit}")
    def committed_json(path):
        # Metadata must come from the pinned tree, even in a dirty operator checkout.
        return json.loads(subprocess.check_output(
            ["git", "-C", str(app), "show", f"{SOURCE_COMMIT}:{path}"], text=True))

    manifest = committed_json("scripts/welcome-demos/runtime-assets.json")
    derivatives = committed_json("public/welcome/animations/provenance.json")
    recorded = {Path(f["source"]).stem: f for f in derivatives["files"]}
    captures = {c["id"]: c for c in manifest["captures"]}
    # Validate every input before producing any output.
    for ident in TOURS.values():
        source = app / "public/welcome/demos" / f"{ident}.webm"
        capture = captures[ident]
        if sha(source) != recorded[ident]["sourceSha256"]:
            raise SystemExit(f"Input hash mismatch: {ident}")
        if capture["state"] != "complete" or capture["frameCount"] != 120:
            raise SystemExit(f"Incomplete capture: {ident}")
    out.mkdir(parents=True, exist_ok=True)
    outputs = []
    for name, ident in TOURS.items():
        source = app / "public/welcome/demos" / f"{ident}.webm"
        pixels = subprocess.check_output([
            imageio_ffmpeg.get_ffmpeg_exe(), "-v", "error", "-i", str(source),
            "-vf", f"fps={FPS},scale={WIDTH}:{HEIGHT}:flags=lanczos", "-f", "rawvideo",
            "-pix_fmt", "rgb24", "pipe:1"])
        size = WIDTH * HEIGHT * 3
        if len(pixels) != size * 56:
            raise SystemExit(f"Unexpected duration/frame count: {ident}")
        frames = [Image.frombytes("RGB", (WIDTH, HEIGHT), pixels[i:i+size])
                  for i in range(0, len(pixels), size)]
        animation = out / f"kfm-tour-{name}.webp"
        poster = out / f"kfm-tour-{name}.jpg"
        frames[0].save(animation, save_all=True, append_images=frames[1:],
                       duration=125, loop=1, quality=65, method=6, minimize_size=True)
        frames[0].save(poster, quality=88, optimize=True)
        # Reopen output; validate finite playback, dimensions, total duration and motion.
        with Image.open(animation) as check:
            durations, hashes = [], set()
            if check.info.get("loop") != 1 or check.size != (WIDTH, HEIGHT):
                raise SystemExit(f"Invalid playback metadata: {name}")
            for i in range(check.n_frames):
                check.seek(i)
                check.load()
                durations.append(check.info["duration"])
                hashes.add(hashlib.sha256(check.tobytes()).hexdigest())
            if sum(durations) != 7000 or len(hashes) < 3:
                raise SystemExit(f"Invalid motion/duration: {name}")
        capture = captures[ident]
        outputs.append({"name": name, "sourceId": ident,
                        "sourcePath": f"public/welcome/demos/{ident}.webm",
                        "sourceSha256": sha(source), "capturedAt": capture["capturedAt"],
                        "sourceTimes": capture["sourceTimes"], "attribution": capture["attribution"],
                        "limitation": capture["limitation"],
                        "captureWallSeconds": capture["captureWallSeconds"],
                        "animation": animation.name, "animationSha256": sha(animation),
                        "bytes": animation.stat().st_size, "poster": poster.name,
                        "posterSha256": sha(poster), "width": WIDTH, "height": HEIGHT,
                        "durationMs": 7000, "playCount": 1, "encodedFrames": len(durations),
                        "distinctDecodedFrames": len(hashes)})
    record = {"kind": "documentation-display-derivative", "authority": "NONE",
              "sourceCommit": SOURCE_COMMIT, "live": False,
              "method": "Existing rendered map tours; rescale and sample only. No new map data or frame interpolation.",
              "toolVersions": {"pillow": Image.__version__,
                               "ffmpeg": imageio_ffmpeg.get_ffmpeg_version()}, "files": outputs}
    (out / "showcase-media.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"tours": len(outputs), "animationBytes": sum(f["bytes"] for f in outputs),
                      "sourceCommit": SOURCE_COMMIT}))


if __name__ == "__main__":
    main()
