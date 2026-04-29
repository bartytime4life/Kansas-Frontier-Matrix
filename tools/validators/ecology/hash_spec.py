#!/usr/bin/env python3
"""
Deterministic KFM spec hash helper.

Uses canonical JSON equivalent:
- sorted keys
- compact separators
- UTF-8
- excludes known non-deterministic fields by default
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any


DEFAULT_EXCLUDE_FIELDS = {
    "timestamp",
    "created",
    "updated",
    "retrieved_at",
    "run_started_at",
    "run_finished_at",
    "change_timestamp",
    "signature",
    "signatures",
}


def strip_fields(value: Any, exclude: set[str]) -> Any:
    if isinstance(value, dict):
        return {
            k: strip_fields(v, exclude)
            for k, v in sorted(value.items())
            if k not in exclude
        }
    if isinstance(value, list):
        return [strip_fields(v, exclude) for v in value]
    return value


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def spec_hash(value: dict[str, Any]) -> str:
    stable = strip_fields(copy.deepcopy(value), DEFAULT_EXCLUDE_FIELDS)
    return hashlib.sha256(canonical_json(stable)).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", type=Path)
    parser.add_argument("--expect", help="expected sha256")
    args = parser.parse_args()

    data = json.loads(args.json_file.read_text(encoding="utf-8"))
    digest = spec_hash(data)

    print(digest)

    if args.expect and args.expect != digest:
        print(f"ERROR: spec hash mismatch: expected {args.expect}, got {digest}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
