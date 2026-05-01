#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

DIGEST_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
FORBIDDEN_PATH_RE = re.compile(r"(?i)(^|/)(RAW|WORK|QUARANTINE)(/|$)")


def has_attestation(value: str | None) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_semantics(doc: dict) -> list[str]:
    errors: list[str] = []
    delta = doc.get("delta_archive", {})
    release_state = doc.get("release_state")

    tile_count = delta.get("tile_count")
    expected = delta.get("expected_tile_count")
    declared = delta.get("completeness_pct")
    if isinstance(tile_count, int) and isinstance(expected, int) and expected > 0:
        computed = round(tile_count / expected, 6)
        if declared is None or abs(float(declared) - computed) > 1e-6:
            errors.append(f"completeness_pct mismatch: declared={declared} computed={computed}")
        if computed < 0.95:
            errors.append(f"completeness_pct below promotion floor: {computed}")

    masked_pct = doc.get("masked_pct")
    if isinstance(masked_pct, (int, float)):
        if masked_pct > 0.30:
            errors.append(f"masked_pct reject threshold exceeded: {masked_pct}")
        if masked_pct > 0.15:
            att = doc.get("attestations", {})
            if not has_attestation(att.get("steward")) or not has_attestation(att.get("reviewer")):
                errors.append("masked_pct in REVIEW band requires steward and reviewer attestation")

    for path in [doc.get("base_archive", {}).get("href"), delta.get("href")]:
        if isinstance(path, str) and FORBIDDEN_PATH_RE.search(path):
            errors.append("public PMTiles ref uses RAW/WORK/QUARANTINE path")

    for name, digest in [("base_archive.digest", doc.get("base_archive", {}).get("digest")), ("delta_archive.digest", delta.get("digest"))]:
        if not isinstance(digest, str) or not DIGEST_RE.match(digest):
            errors.append(f"missing or malformed digest: {name}")

    if release_state in {"PUBLIC", "RELEASED"}:
        if not doc.get("proof_refs"):
            errors.append("missing proofs for public/released manifest")
        if not doc.get("signature_refs"):
            errors.append("missing signatures for public/released manifest")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate governed PMTiles manifest")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--schema", type=Path, default=Path("schemas/tiles/pmtiles_delta_manifest.schema.json"))
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    schema = json.loads(args.schema.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema)
    schema_errors = sorted(validator.iter_errors(manifest), key=lambda e: list(e.path))

    errors = []
    for err in schema_errors:
        path = ".".join(str(x) for x in err.path) or "<root>"
        errors.append({"kind": "schema", "path": path, "message": err.message})

    for message in validate_semantics(manifest):
        errors.append({"kind": "semantic", "path": "<root>", "message": message})

    output = {
        "ok": len(errors) == 0,
        "manifest": str(args.manifest),
        "schema": str(args.schema),
        "errors": errors,
    }
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0 if output["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
