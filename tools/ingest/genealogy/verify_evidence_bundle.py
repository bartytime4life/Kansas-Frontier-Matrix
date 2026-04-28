#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("bundle must be a JSON object")
    return data


def _normalize_hex(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    candidate = value.lower().strip()
    if candidate.startswith("sha256:"):
        candidate = candidate.split(":", 1)[1]
    if len(candidate) != 64:
        return None
    if any(c not in "0123456789abcdef" for c in candidate):
        return None
    return candidate


def _expected_digest(bundle: dict[str, Any]) -> str | None:
    for key in ("content_sha256", "content_digest", "payload_sha256", "sha256"):
        normalized = _normalize_hex(bundle.get(key))
        if normalized is not None:
            return normalized

    payload = bundle.get("payload")
    if isinstance(payload, dict):
        for key in ("sha256", "digest", "content_sha256", "content_digest"):
            normalized = _normalize_hex(payload.get(key))
            if normalized is not None:
                return normalized

    evidence = bundle.get("evidence")
    if isinstance(evidence, dict):
        for key in ("sha256", "digest", "content_sha256", "content_digest"):
            normalized = _normalize_hex(evidence.get(key))
            if normalized is not None:
                return normalized

    return None


def _has_usable_keyset(path: Path) -> bool:
    doc = _load_json(path)

    keys = doc.get("keys")
    if isinstance(keys, list) and any(isinstance(item, dict) for item in keys):
        return True

    if any(name in doc for name in ("public_keys", "trusted_keys", "jwks")):
        return True

    return len(doc) > 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify genealogy EvidenceBundle payload digest and keyset presence.")
    parser.add_argument("--bundle", type=Path, required=True, help="Path to evidence bundle JSON.")
    parser.add_argument("--content", type=Path, required=True, help="Path to source content file (e.g. GEDCOM).")
    parser.add_argument("--trusted-keys", type=Path, required=True, help="Path to trusted keys JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.bundle.exists() or not args.content.exists() or not args.trusted_keys.exists():
        print("ERROR: one or more required inputs do not exist", file=sys.stderr)
        return 1

    try:
        bundle = _load_json(args.bundle)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: failed to read bundle: {exc}", file=sys.stderr)
        return 1

    expected = _expected_digest(bundle)
    if expected is None:
        print("ERROR: bundle missing usable sha256 digest field", file=sys.stderr)
        return 1

    actual = _sha256_file(args.content)
    if actual != expected:
        print("ERROR: content digest mismatch", file=sys.stderr)
        print(f"  expected: {expected}", file=sys.stderr)
        print(f"  actual:   {actual}", file=sys.stderr)
        return 1

    try:
        if not _has_usable_keyset(args.trusted_keys):
            print("ERROR: trusted key set is empty or invalid", file=sys.stderr)
            return 1
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: failed to read trusted keys: {exc}", file=sys.stderr)
        return 1

    print("PASS: evidence bundle verification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
