#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import sys
from pathlib import Path
from typing import Any


def _iter_ndjson(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _decode_payload(encoded: str) -> dict[str, Any]:
    raw = base64.urlsafe_b64decode(encoded.encode("ascii"))
    doc = json.loads(raw.decode("utf-8"))
    if not isinstance(doc, dict):
        raise ValueError("decoded sidecar payload must be an object")
    return doc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read one sidecar row by person key for controlled review.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--person-key", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    for row in _iter_ndjson(args.input):
        if row.get("person_key") != args.person_key:
            continue
        ciphertext = row.get("ciphertext")
        if not isinstance(ciphertext, str):
            print("ERROR: matching row missing ciphertext", file=sys.stderr)
            return 1
        payload = _decode_payload(ciphertext)
        print(json.dumps({"person_key": args.person_key, "payload": payload}, sort_keys=True))
        return 0

    print("ERROR: person key not found", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
