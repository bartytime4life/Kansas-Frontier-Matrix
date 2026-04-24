#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render markdown summary for bundle diff-policy report.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    decision = payload.get("decision", "unknown")
    reasons = payload.get("reasons", [])

    lines = ["# Bundle Diff Policy Summary", "", f"- Decision: **{decision}**"]
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
