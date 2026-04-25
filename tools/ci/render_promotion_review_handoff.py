#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def read_json(path: str, label: str) -> dict:
    try:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"render_promotion_review_handoff: {label} input not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except UnicodeDecodeError:
        print(
            f"render_promotion_review_handoff: {label} input is not valid UTF-8: {path}",
            file=sys.stderr,
        )
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(f"render_promotion_review_handoff: invalid JSON in {label} input {path}: {exc}", file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(payload, dict):
        print(
            f"render_promotion_review_handoff: expected top-level JSON object in {label} input {path}",
            file=sys.stderr,
        )
        raise SystemExit(2)

    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Compose promotion review handoff markdown.")
    parser.add_argument("--promotion", required=True)
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--diff", required=True)
    parser.add_argument("--diff-policy", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    promotion = read_json(args.promotion, "promotion")
    bundle = read_json(args.bundle, "bundle")
    diff = read_json(args.diff, "diff")
    diff_policy = read_json(args.diff_policy, "diff-policy")

    required = [
        (promotion, "release_id", str),
        (promotion, "state", str),
        (bundle, "bundle_id", str),
        (diff, "added", int),
        (diff, "changed", int),
        (diff, "removed", int),
        (diff_policy, "decision", str),
    ]

    type_labels = {str: "string", int: "integer"}

    for payload, key, typ in required:
        if key not in payload or not isinstance(payload[key], typ):
            type_label = type_labels.get(typ, typ.__name__)
            print(
                f"render_promotion_review_handoff: missing required {type_label} key: {key}",
                file=sys.stderr,
            )
            return 2

    md = "\n".join([
        "# Promotion Review Handoff",
        "",
        f"- Release: **{promotion['release_id']}**",
        f"- Promotion state: **{promotion['state']}**",
        f"- Bundle id: **{bundle['bundle_id']}**",
        f"- Diff totals: added={diff['added']}, changed={diff['changed']}, removed={diff['removed']}",
        f"- Diff policy decision: **{diff_policy['decision']}**",
    ])

    if args.output:
        Path(args.output).write_text(md + "\n", encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
