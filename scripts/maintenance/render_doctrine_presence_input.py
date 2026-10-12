#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("receipt", type=Path, help="JSON output from check_required_doctrine_artifacts.py")
    args = parser.parse_args()

    payload = json.loads(args.receipt.read_text(encoding="utf-8"))
    present = payload.get("present")
    if not isinstance(present, dict):
        raise SystemExit("receipt missing 'present' map")

    print(json.dumps({"present": present}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
