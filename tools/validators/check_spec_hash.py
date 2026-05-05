#!/usr/bin/env python3
"""Validate EvidenceBundle canonical spec_hash."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

EXCLUDED_ROOT_KEYS = {"spec_hash", "computed_spec_hash", "signatures", "attestations", "_signature"}
SHA256_RE = re.compile(r"^[a-fA-F0-9]{64}$")

def canonical_bundle_bytes(bundle: dict[str, Any]) -> bytes:
    normalized = copy.deepcopy(bundle)
    for key in EXCLUDED_ROOT_KEYS:
        normalized.pop(key, None)
    return json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def compute_spec_hash(bundle: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bundle_bytes(bundle)).hexdigest()

def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_bundle", nargs="?", default="artifacts/EvidenceBundle.json")
    parser.add_argument("spec_hash_file", nargs="?", default="artifacts/spec_hash.txt")
    parser.add_argument("--receipt-out", default="")
    args = parser.parse_args()

    bundle_path = Path(args.evidence_bundle)
    spec_path = Path(args.spec_hash_file)
    if not bundle_path.is_file():
        return fail(f"missing EvidenceBundle: {bundle_path}")
    if not spec_path.is_file():
        return fail(f"missing spec_hash file: {spec_path}")

    try:
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return fail(f"invalid EvidenceBundle JSON: {exc}")
    if not isinstance(bundle, dict):
        return fail("EvidenceBundle root must be a JSON object")

    spec_hash_text = spec_path.read_text(encoding="utf-8").strip()
    if not SHA256_RE.match(spec_hash_text):
        return fail("spec_hash.txt must contain a 64-character sha256 hex digest")

    computed = compute_spec_hash(bundle)
    embedded = bundle.get("spec_hash")
    receipt = {
        "algorithm": "canonical-json-v1",
        "evidence_bundle": str(bundle_path),
        "spec_hash_file": str(spec_path),
        "computed_spec_hash": computed,
        "spec_hash_file_value": spec_hash_text,
        "embedded_spec_hash": embedded,
        "excluded_root_keys": sorted(EXCLUDED_ROOT_KEYS),
        "valid": computed == spec_hash_text and (embedded in (None, spec_hash_text)),
    }
    if args.receipt_out:
        out = Path(args.receipt_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if computed != spec_hash_text:
        return fail(f"canonical spec_hash mismatch: computed {computed}, file has {spec_hash_text}")
    if embedded is not None and embedded != spec_hash_text:
        return fail(f"EvidenceBundle.spec_hash {embedded} does not match {spec_hash_text}")

    print(f"spec_hash OK: {computed}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
