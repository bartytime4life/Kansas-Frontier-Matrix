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
        print(f"render_bundle_diff_policy_summary: input not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except UnicodeDecodeError:
        print(f"render_bundle_diff_policy_summary: input is not valid UTF-8: {path}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(f"render_bundle_diff_policy_summary: invalid JSON in {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)
    except OSError as exc:
        print(f"render_bundle_diff_policy_summary: unable to read input {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(payload, dict):
        print(
            f"render_bundle_diff_policy_summary: expected top-level JSON object in {path}",
            file=sys.stderr,
        )
        raise SystemExit(2)

    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Render markdown summary for bundle diff-policy report.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    payload = read_json(args.input)
    if "decision" not in payload or not isinstance(payload["decision"], str):
        print("render_bundle_diff_policy_summary: missing required string key: decision", file=sys.stderr)
        return 2

    reasons = payload.get("reasons", [])
    if not isinstance(reasons, list):
        print("render_bundle_diff_policy_summary: reasons must be a list when provided", file=sys.stderr)
        return 2

    lines = ["# Bundle Diff Policy Summary", "", f"- Decision: **{payload['decision']}**"]
    if reasons:
        lines.append("- Reasons:")
        lines.extend([f"  - {reason}" for reason in reasons])

    md = "\n".join(lines)
    if args.output:
        Path(args.output).write_text(md + "\n", encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
