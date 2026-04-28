#!/usr/bin/env python3
"""Render ecology validator summary from run_all output."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render ecology validator summary")
    parser.add_argument("report", help="Path to run_all JSON output")
    args = parser.parse_args()

    report = json.loads(Path(args.report).read_text(encoding="utf-8"))
    print(f"# Ecology validation summary\n")
    print(f"Overall decision: **{report.get('decision', 'unknown')}**\n")
    print("| Validator | Decision | Errors |")
    print("| --- | --- | --- |")
    for result in report.get("results", []):
        errors = ", ".join(result.get("errors", [])) if result.get("errors") else "-"
        print(f"| {result.get('validator')} | {result.get('decision')} | {errors} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
