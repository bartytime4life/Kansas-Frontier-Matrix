#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def _load_json(path: str) -> dict[str, Any]:
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"stable_diff: input not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except UnicodeDecodeError:
        print(f"stable_diff: input is not valid UTF-8: {path}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(f"stable_diff: invalid JSON in {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)
    except OSError as exc:
        print(f"stable_diff: unable to read input {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(payload, dict):
        print(f"stable_diff: expected top-level JSON object in {path}", file=sys.stderr)
        raise SystemExit(2)

    return payload


def _build_report(left_path: str, right_path: str) -> tuple[dict[str, Any], bool]:
    left = _load_json(left_path)
    right = _load_json(right_path)

    left_keys = set(left.keys())
    right_keys = set(right.keys())

    added = sorted(right_keys - left_keys)
    removed = sorted(left_keys - right_keys)
    changed = sorted(key for key in (left_keys & right_keys) if left[key] != right[key])

    changed_any = bool(added or removed or changed)
    report: dict[str, Any] = {
        "tool": "stable-diff",
        "status": "changed" if changed_any else "same",
        "blocking": False,
        "left": left_path,
        "right": right_path,
        "summary": {
            "added": added,
            "removed": removed,
            "changed": changed,
        },
    }
    return report, changed_any


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministically compare top-level keys and values of two JSON objects."
    )
    parser.add_argument("--left", required=True, help="Path to left JSON file")
    parser.add_argument("--right", required=True, help="Path to right JSON file")
    parser.add_argument("--output", help="Optional path for JSON report output")
    parser.add_argument(
        "--fail-on-change",
        action="store_true",
        help="Exit with status 1 when a change is detected.",
    )
    args = parser.parse_args()

    report, changed_any = _build_report(args.left, args.right)
    if args.fail_on_change:
        report["blocking"] = changed_any

    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(encoded, encoding="utf-8")
    else:
        sys.stdout.write(encoded)

    if args.fail_on_change and changed_any:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
