#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def validate(summary: dict, require_normalized_only: bool = False) -> list[str]:
    errors: list[str] = []
    paths = summary.get("artifact_paths") or {}
    digests = summary.get("artifact_digests") or {}

    pairs = [
        ("check_receipt", "check_receipt", "check_receipt_sha256"),
        ("provenance_sync_receipt", "provenance_sync_receipt", "provenance_sync_receipt_sha256"),
        ("presence_output", "presence_output", "presence_output_sha256"),
    ]
    for map_key, path_key, digest_key in pairs:
        if paths.get(map_key) != summary.get(path_key):
            errors.append(f"artifact_paths mismatch for {map_key}")
        if digests.get(map_key) != summary.get(digest_key):
            errors.append(f"artifact_digests mismatch for {map_key}")

    if require_normalized_only:
        legacy_fields = [
            "check_receipt",
            "provenance_sync_receipt",
            "presence_output",
            "check_receipt_sha256",
            "provenance_sync_receipt_sha256",
            "presence_output_sha256",
        ]
        present_legacy = [f for f in legacy_fields if f in summary]
        if present_legacy:
            errors.append("legacy fields present in normalized-only mode: " + ",".join(sorted(present_legacy)))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("summary", type=Path)
    parser.add_argument("--require-normalized-only", action="store_true")
    args = parser.parse_args()

    summary = json.loads(args.summary.read_text(encoding="utf-8"))
    errors = validate(summary, args.require_normalized_only)
    payload = {
        "check": "doctrine_preflight_summary_consistency",
        "summary": str(args.summary),
        "result": "pass" if not errors else "fail",
        "errors": errors,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
