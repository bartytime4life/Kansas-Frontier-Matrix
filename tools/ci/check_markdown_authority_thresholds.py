#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

MARKERS = ["TODO", "UNKNOWN", "NEEDS VERIFICATION"]


def load_config(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"config not found: {path}")
    except UnicodeDecodeError:
        raise ValueError(f"config is not valid UTF-8: {path}")
    except json.JSONDecodeError as exc:
        raise ValueError(f"config is not valid JSON: {path}: {exc}") from exc

    if not isinstance(value, dict):
        raise ValueError("config root must be an object")

    checks = value.get("checks")
    if not isinstance(checks, list) or not checks:
        raise ValueError("config.checks must be a non-empty array")

    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Check markdown marker thresholds for authority docs.")
    parser.add_argument("--root", default=".", help="Repository root path")
    parser.add_argument(
        "--config",
        default="tools/ci/markdown_authority_thresholds.json",
        help="Path to threshold config JSON",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"check_markdown_authority_thresholds: invalid root path: {root}", file=sys.stderr)
        return 2

    try:
        config = load_config(root / args.config)
    except ValueError as exc:
        print(f"check_markdown_authority_thresholds: {exc}", file=sys.stderr)
        return 2

    failures: list[str] = []
    print("check_markdown_authority_thresholds: report")
    for entry in config["checks"]:
        if not isinstance(entry, dict):
            print("check_markdown_authority_thresholds: invalid check entry (expected object)", file=sys.stderr)
            return 2

        rel_path = entry.get("path")
        max_total = entry.get("max_total")
        if not isinstance(rel_path, str) or not rel_path:
            print("check_markdown_authority_thresholds: each check.path must be a non-empty string", file=sys.stderr)
            return 2
        if not isinstance(max_total, int):
            print("check_markdown_authority_thresholds: each check.max_total must be an integer", file=sys.stderr)
            return 2

        path = root / rel_path
        if not path.is_file():
            failures.append(f"{rel_path}: missing file")
            print(f"- {rel_path}: missing file")
            continue

        text = path.read_text(encoding="utf-8")
        total = sum(text.count(marker) for marker in MARKERS)
        print(f"- {rel_path}: total={total} max_total={max_total}")

        if total > max_total:
            failures.append(f"{rel_path}: total {total} > max_total {max_total}")

    if failures:
        print("check_markdown_authority_thresholds: FAILED", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("check_markdown_authority_thresholds: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
