#!/usr/bin/env python3
from __future__ import annotations

import argparse
import pathlib
import re
import sys

PUBLIC_CODE_ROOTS = [
    pathlib.Path("apps/web/src"),
    pathlib.Path("apps/ui"),
    pathlib.Path("apps/governed_api/routes"),
]
CODE_EXTENSIONS = {".js", ".jsx", ".ts", ".tsx", ".py"}
RAW_LANE_PATTERN = re.compile(r"data/(raw|work|quarantine)/")


def scan_paths(paths: list[pathlib.Path]) -> list[str]:
    bad: list[str] = []
    for root in paths:
        if not root.exists():
            continue
        for file_path in root.rglob("*"):
            if not file_path.is_file() or file_path.suffix not in CODE_EXTENSIONS:
                continue
            text = file_path.read_text(errors="ignore")
            if RAW_LANE_PATTERN.search(text):
                bad.append(str(file_path))
    return sorted(bad)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-fail", action="store_true", help="Report findings but return 0")
    args = parser.parse_args()

    bad = scan_paths(PUBLIC_CODE_ROOTS)
    if bad:
        print("BLOCKED direct raw/work/quarantine references detected:")
        print("\n".join(bad))
        return 0 if args.allow_fail else 1

    print("OK no direct public raw/work/quarantine refs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
