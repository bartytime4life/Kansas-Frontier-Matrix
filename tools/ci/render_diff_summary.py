#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_KEYS = ("added", "changed", "removed")


def read_json(path: str) -> dict:
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"render_diff_summary: input not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except UnicodeDecodeError:
        print(f"render_diff_summary: input is not valid UTF-8: {path}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(f"render_diff_summary: invalid JSON in {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)
    except OSError as exc:
        print(f"render_diff_summary: unable to read input {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(payload, dict):
        print(f"render_diff_summary: expected top-level JSON object in {path}", file=sys.stderr)
        raise SystemExit(2)

    return payload

    if not isinstance(payload, dict):
        print(f"render_diff_summary: expected top-level JSON object in {path}", file=sys.stderr)
        raise SystemExit(2)

    return payload


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
