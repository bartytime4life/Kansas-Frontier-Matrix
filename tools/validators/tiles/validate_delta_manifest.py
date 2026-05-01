#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

DIGEST_RE = re.compile(r"^sha256:[a-fA-F0-9]{64}$")
FORBIDDEN_PATH_RE = re.compile(r"(^|/)(RAW|WORK|QUARANTINE)(/|$)", re.IGNORECASE)


def canonical_json_hash(payload: dict) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def validate_semantics(doc: dict) -> list[str]:
    errors: list[str] = []

    base = doc.get("base_pmtiles", {})
    if not base.get("spec_hash"):
        errors.append("base_pmtiles.spec_hash is required")

    tiles = doc.get("tiles", [])
    produced = doc.get("produced_tile_count")
    if isinstance(produced, int) and produced != len(tiles):
        errors.append(f"produced_tile_count ({produced}) must equal len(tiles) ({len(tiles)})")

    qc = doc.get("qc", {})
    review_threshold = qc.get("masked_pct_review_threshold")

    for idx, tile in enumerate(tiles):
        prefix = f"tiles[{idx}]"
        digest = tile.get("digest")
        prior = tile.get("prior_digest")
        change_type = tile.get("change_type")
        run_receipt_url = tile.get("run_receipt_url")

        if not isinstance(digest, str) or not DIGEST_RE.match(digest):
            errors.append(f"{prefix}.digest malformed")

        if prior is not None and (not isinstance(prior, str) or not DIGEST_RE.match(prior)):
            errors.append(f"{prefix}.prior_digest malformed")

        if change_type in {"modified", "removed"} and prior is None:
            errors.append(f"{prefix}.prior_digest must be non-null for {change_type}")

        if change_type == "added" and prior is not None:
            errors.append(f"{prefix}.prior_digest must be null for added")

        if not isinstance(run_receipt_url, str) or not run_receipt_url.strip():
            errors.append(f"{prefix}.run_receipt_url missing or empty")

        if isinstance(run_receipt_url, str) and FORBIDDEN_PATH_RE.search(run_receipt_url):
            errors.append(f"{prefix}.run_receipt_url references forbidden RAW/WORK/QUARANTINE path")

        if isinstance(digest, str) and FORBIDDEN_PATH_RE.search(digest):
            errors.append(f"{prefix}.digest references forbidden RAW/WORK/QUARANTINE path")

        masked_pct = tile.get("masked_pct")
        if isinstance(masked_pct, (int, float)) and isinstance(review_threshold, (int, float)):
            if masked_pct > review_threshold:
                errors.append(
                    f"{prefix}.masked_pct ({masked_pct}) exceeds qc.masked_pct_review_threshold ({review_threshold})"
                )

    base_url = base.get("url")
    if isinstance(base_url, str) and FORBIDDEN_PATH_RE.search(base_url):
        errors.append("base_pmtiles.url references forbidden RAW/WORK/QUARANTINE path")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate KFM PMTiles delta manifest v1")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--schema", type=Path, default=Path("contracts/kfm/delta_manifest.v1.json"))
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    schema = json.loads(args.schema.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema)
    schema_errors = sorted(validator.iter_errors(manifest), key=lambda e: list(e.path))

    errors: list[str] = []
    for err in schema_errors:
        path = ".".join(str(x) for x in err.path) or "<root>"
        errors.append(f"schema: {path}: {err.message}")

    errors.extend(validate_semantics(manifest))

    manifest_hash = canonical_json_hash(manifest)

    if errors:
        print("FAIL: delta_manifest.v1 validation failed")
        print(f"canonical_manifest_hash={manifest_hash}")
        for item in errors:
            print(f" - {item}")
        return 1

    print("PASS: delta_manifest.v1 validation passed")
    print(f"canonical_manifest_hash={manifest_hash}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
