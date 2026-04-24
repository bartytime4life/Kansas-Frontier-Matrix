#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render markdown summary for promotion decision.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    state = payload.get("state", "unknown")
    release_id = payload.get("release_id", "n/a")

    md = "\n".join([
        "# Promotion Summary",
        "",
        f"- Release: **{release_id}**",
        f"- State: **{state}**",
    ])

    if args.output:
        Path(args.output).write_text(md + "\n", encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
