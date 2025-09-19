#!/usr/bin/env python3
"""
validate_cogs.py — validate all COGs under a path (uses rio-cogeo if present).
"""
from __future__ import annotations
import argparse, shutil, subprocess, sys
from pathlib import Path

RIO = shutil.which("rio")

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path)
    ap.add_argument("--pattern", default="*.tif")
    ap.add_argument("--fail-fast", action="store_true")
    args = ap.parse_args()

    if not RIO:
        print("[WARN] rio-cogeo not found; skipping validation.", file=sys.stderr)
        return 0

    files = [p for p in args.root.rglob(args.pattern) if p.suffix.lower() in {".tif", ".tiff"}]
    if not files:
        print("[INFO] no rasters found"); return 0

    failures = 0
    for f in files:
        try:
            print("[VAL]", f)
            subprocess.check_call([RIO, "cogeo", "validate", str(f)])
        except subprocess.CalledProcessError as e:
            failures += 1
            print(f"[FAIL] {f}: {e}", file=sys.stderr)
            if args.fail_fast:
                return 1
    if failures:
        print(f"[WARN] {failures} file(s) failed COG validation.", file=sys.stderr)
        return 1
    print("[OK] all COGs valid")
    return 0

if __name__ == "__main__":
    sys.exit(main())
