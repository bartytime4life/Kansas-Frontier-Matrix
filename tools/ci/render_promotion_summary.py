#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from render_json_io import read_json_object


def read_json(path: str) -> dict:
    return read_json_object(
        path,
        not_found="render_promotion_summary: input not found: {path}",
        non_utf8="render_promotion_summary: input is not valid UTF-8: {path}",
        invalid_json="render_promotion_summary: invalid JSON in {path}: {exc}",
        unreadable="render_promotion_summary: unable to read input {path}: {exc}",
        wrong_type="render_promotion_summary: expected top-level JSON object in {path}",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Render markdown summary for promotion decision.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    payload = read_json(args.input)
    for key in ("release_id", "state"):
        if key not in payload or not isinstance(payload[key], str):
            print(f"render_promotion_summary: missing required string key: {key}", file=sys.stderr)
            return 2

    md = "\n".join([
        "# Promotion Summary",
        "",
        f"- Release: **{payload['release_id']}**",
        f"- State: **{payload['state']}**",
    ])

    if args.output:
        Path(args.output).write_text(md + "\n", encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
