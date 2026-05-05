#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from render_json_io import read_json_object


REQUIRED_KEYS = ("added", "changed", "removed")


def read_json(path: str) -> dict:
    return read_json_object(
        path,
        not_found="render_diff_summary: input not found: {path}",
        non_utf8="render_diff_summary: input is not valid UTF-8: {path}",
        invalid_json="render_diff_summary: invalid JSON in {path}: {exc}",
        unreadable="render_diff_summary: unable to read input {path}: {exc}",
        wrong_type="render_diff_summary: expected top-level JSON object in {path}",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a markdown summary for a diff report.")
    parser.add_argument("--input", required=True, help="Path to JSON diff report")
    parser.add_argument("--output", help="Optional output markdown path")
    args = parser.parse_args()

    payload = read_json(args.input)
    missing = [k for k in REQUIRED_KEYS if k not in payload]
    if missing:
        print(f"render_diff_summary: missing required key(s): {', '.join(missing)}", file=sys.stderr)
        return 2

    if not all(isinstance(payload[k], int) for k in REQUIRED_KEYS):
        print("render_diff_summary: required keys must be integers", file=sys.stderr)
        return 2

    md = "\n".join(
        [
            "# Diff Summary",
            "",
            f"- Added: **{payload['added']}**",
            f"- Changed: **{payload['changed']}**",
            f"- Removed: **{payload['removed']}**",
        ]
    )

    if args.output:
        Path(args.output).write_text(md + "\n", encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
