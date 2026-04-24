#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a markdown summary for a diff report.")
    parser.add_argument("--input", required=True, help="Path to JSON diff report")
    parser.add_argument("--output", help="Optional output markdown path")
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    added = payload.get("added", 0)
    changed = payload.get("changed", 0)
    removed = payload.get("removed", 0)

    md = "\n".join(
        [
            "# Diff Summary",
            "",
            f"- Added: **{added}**",
            f"- Changed: **{changed}**",
            f"- Removed: **{removed}**",
        ]
    )

    if args.output:
        Path(args.output).write_text(md + "\n", encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
