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
        print(f"render_promotion_bundle_summary: input not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except UnicodeDecodeError:
        print(f"render_promotion_bundle_summary: input is not valid UTF-8: {path}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(f"render_promotion_bundle_summary: invalid JSON in {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(payload, dict):
        print(
            f"render_promotion_bundle_summary: expected top-level JSON object in {path}",
            file=sys.stderr,
        )
        raise SystemExit(2)

    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Render markdown summary for promotion bundle.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    payload = read_json(args.input)
    if "bundle_id" not in payload or not isinstance(payload["bundle_id"], str):
        print("render_promotion_bundle_summary: missing required string key: bundle_id", file=sys.stderr)
        return 2

    artifacts = payload.get("artifacts")
    if not isinstance(artifacts, list):
        print("render_promotion_bundle_summary: missing required list key: artifacts", file=sys.stderr)
        return 2

    md = "\n".join([
        "# Promotion Bundle Summary",
        "",
        f"- Bundle: **{payload['bundle_id']}**",
        f"- Artifacts: **{len(artifacts)}**",
    ])

    if args.output:
        Path(args.output).write_text(md + "\n", encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
