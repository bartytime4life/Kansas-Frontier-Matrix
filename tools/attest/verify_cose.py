#!/usr/bin/env python3
"""Verify a KFM PMTiles signature bundle shape.

Cryptographic COSE verification is intentionally dependency-pluggable here.
Until a repository-approved COSE library and key registry are wired in, this tool
fails closed unless --shape-only is explicitly passed for development fixtures.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SHA256_RE = re.compile(r"^sha256:[a-fA-F0-9]{64}$")


def fail(msg: str) -> int:
    print(f"DENY: {msg}", file=sys.stderr)
    return 1


def validate_shape(path: Path) -> None:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if obj.get("schema_version") != "kfm.pmsig.v1":
        raise ValueError("schema_version must be kfm.pmsig.v1")
    subject = obj.get("subject")
    if not isinstance(subject, dict):
        raise ValueError("subject must be object")
    for field in ["pmtiles_sha256", "pmidx_merkle_root", "spec_hash"]:
        value = subject.get(field)
        if not isinstance(value, str) or not SHA256_RE.match(value):
            raise ValueError(f"subject.{field} must be sha256:<64 hex>")
    if not isinstance(obj.get("key_id"), str) or not obj["key_id"]:
        raise ValueError("key_id is required")
    if not isinstance(obj.get("signature"), str) or not obj["signature"]:
        raise ValueError("signature is required")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pmsig", nargs="+", type=Path)
    parser.add_argument("--shape-only", action="store_true", help="development only; skips cryptographic verification")
    args = parser.parse_args()

    status = 0
    for path in args.pmsig:
        try:
            validate_shape(path)
            if not args.shape_only:
                raise ValueError("cryptographic COSE verification not wired; use approved verifier/key registry")
            print(f"ALLOW: {path}: signature bundle shape valid [shape-only]")
        except Exception as exc:  # noqa: BLE001
            status |= fail(f"{path}: {exc}")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
