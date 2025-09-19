#!/usr/bin/env python3
"""
write_meta.py — emit .sha256 and .meta.json next to an artifact.

Usage:
  python scripts/write_meta.py PATH/TO/ARTIFACT --inputs in1 in2 ...
"""
from __future__ import annotations
import argparse, hashlib, json, os, sys, time
from pathlib import Path

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("artifact", type=Path)
    ap.add_argument("--inputs", nargs="*", default=[])
    ap.add_argument("--extra", nargs="*", default=[], help="K=V pairs to include")
    args = ap.parse_args()

    art = args.artifact
    if not art.exists():
        print(f"[ERR] artifact not found: {art}", file=sys.stderr); return 2

    # checksum
    (art.with_suffix(art.suffix + ".sha256")).write_text(sha256(art))

    # meta
    meta = {
        "artifact": str(art),
        "size": art.stat().st_size,
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "cwd": os.getcwd(),
        "command": " ".join(sys.argv),
        "inputs": args.inputs,
    }
    for kv in args.extra:
        if "=" in kv:
            k, v = kv.split("=", 1)
            meta[k] = v
    (art.with_suffix(".meta.json")).write_text(json.dumps(meta, indent=2))
    print(f"[OK] meta → {art.with_suffix('.meta.json')}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
