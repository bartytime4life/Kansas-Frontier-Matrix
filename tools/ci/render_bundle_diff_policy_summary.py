#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from render_json_io import read_json_object


def read_json(path: str) -> dict:
    return read_json_object(
        path,
        not_found="render_bundle_diff_policy_summary: input not found: {path}",
        non_utf8="render_bundle_diff_policy_summary: input is not valid UTF-8: {path}",
        invalid_json="render_bundle_diff_policy_summary: invalid JSON in {path}: {exc}",
        unreadable="render_bundle_diff_policy_summary: unable to read input {path}: {exc}",
        wrong_type="render_bundle_diff_policy_summary: expected top-level JSON object in {path}",
    )


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
