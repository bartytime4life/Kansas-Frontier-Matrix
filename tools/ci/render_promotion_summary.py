#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def read_json(path: str) -> dict:
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"render_promotion_summary: input not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(f"render_promotion_summary: invalid JSON in {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(payload, dict):
        print(f"render_promotion_summary: expected top-level JSON object in {path}", file=sys.stderr)
        raise SystemExit(2)

    return payload


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
