#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Compose promotion review handoff markdown.")
    parser.add_argument("--promotion", required=True)
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--diff", required=True)
    parser.add_argument("--diff-policy", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    promotion = json.loads(Path(args.promotion).read_text(encoding="utf-8"))
    bundle = json.loads(Path(args.bundle).read_text(encoding="utf-8"))
    diff = json.loads(Path(args.diff).read_text(encoding="utf-8"))
    diff_policy = json.loads(Path(args.diff_policy).read_text(encoding="utf-8"))

    md = "\n".join([
        "# Promotion Review Handoff",
        "",
        f"- Release: **{promotion.get('release_id', 'n/a')}**",
        f"- Promotion state: **{promotion.get('state', 'unknown')}**",
        f"- Bundle id: **{bundle.get('bundle_id', 'unknown')}**",
        f"- Diff totals: added={diff.get('added', 0)}, changed={diff.get('changed', 0)}, removed={diff.get('removed', 0)}",
        f"- Diff policy decision: **{diff_policy.get('decision', 'unknown')}**",
    ])

    if args.output:
        Path(args.output).write_text(md + "\n", encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
