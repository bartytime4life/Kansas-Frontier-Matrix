#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render markdown summary for promotion bundle.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output")
    args = parser.parse_args()

    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    bundle_id = payload.get("bundle_id", "unknown")
    artifacts = payload.get("artifacts", [])

    md = "\n".join([
        "# Promotion Bundle Summary",
        "",
        f"- Bundle: **{bundle_id}**",
        f"- Artifacts: **{len(artifacts)}**",
    ])

    if args.output:
        Path(args.output).write_text(md + "\n", encoding="utf-8")
    else:
        print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
