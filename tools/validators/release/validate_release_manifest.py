#!/usr/bin/env python3
"""
Validate KFM ReleaseManifest closure.

Checks:
- JSON Schema validity
- public-only policy posture
- reviewed or published review state
- each artifact has evidence, provenance, STAC, and DCAT refs
- artifact spec_hash matches manifest spec_hash when manifest-level spec_hash exists
- no RAW / WORK / QUARANTINE references in public release
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path("contracts/v1/release/kfm_release_manifest.schema.json")

FORBIDDEN_PUBLIC_REFS = (
    "/raw/",
    "/work/",
    "/quarantine/",
    "data/raw/",
    "data/work/",
    "data/quarantine/",
)

BLOCKED_PUBLIC_VALUES = {
    "TODO",
    "todo",
    "UNKNOWN",
    "unknown",
    "NEEDS-VERIFICATION",
    "restricted",
    "deny",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    sys.exit(1)


def contains_forbidden_ref(value: Any) -> bool:
    if isinstance(value, str):
        lowered = value.lower()
        return any(token in lowered for token in FORBIDDEN_PUBLIC_REFS)

    if isinstance(value, dict):
        return any(contains_forbidden_ref(v) for v in value.values())

    if isinstance(value, list):
        return any(contains_forbidden_ref(v) for v in value)

    return False


def assert_present(mapping: dict[str, Any], key: str, label: str) -> Any:
    value = mapping.get(key)
    if value in (None, ""):
        fail(f"{label} missing {key}")
    return value


def assert_not_blocked(value: Any, label: str) -> None:
    if isinstance(value, str) and value in BLOCKED_PUBLIC_VALUES:
        fail(f"{label} cannot be {value}")


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_release_manifest.py <release-manifest.json>")

    manifest_path = Path(sys.argv[1])

    if not manifest_path.exists():
        fail(f"missing ReleaseManifest: {manifest_path}")

    if not SCHEMA_PATH.exists():
        fail(f"missing schema: {SCHEMA_PATH}")

    schema = load_json(SCHEMA_PATH)
    doc = load_json(manifest_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))

    if errors:
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"DENY: schema error at {loc}: {error.message}", file=sys.stderr)
        sys.exit(1)

    if doc.get("policy_label") != "public":
        fail("ReleaseManifest requires policy_label=public")

    if doc.get("review_state") not in {"reviewed", "published"}:
        fail("ReleaseManifest requires review_state reviewed or published")

    manifest_spec_hash = doc.get("spec_hash")
    artifacts = doc.get("artifacts", [])

    if not artifacts:
        fail("ReleaseManifest missing artifacts")

    for idx, artifact in enumerate(artifacts):
        label = f"artifacts[{idx}]"

        for key in (
            "artifact_ref",
            "spec_hash",
            "evidence_ref",
            "provenance_ref",
            "stac_ref",
            "dcat_ref",
            "policy_label",
            "review_state",
        ):
            value = assert_present(artifact, key, label)
            assert_not_blocked(value, f"{label} {key}")

        if artifact.get("policy_label") != "public":
            fail(f"{label} requires policy_label=public")

        if artifact.get("review_state") not in {"reviewed", "published"}:
            fail(f"{label} requires review_state reviewed or published")

        if artifact.get("sensitivity") not in (None, "public"):
            fail(f"{label} requires sensitivity=public when provided")

        if manifest_spec_hash and artifact.get("spec_hash") != manifest_spec_hash:
            fail(f"{label} spec_hash does not match manifest spec_hash")

    if contains_forbidden_ref(doc):
        fail("public ReleaseManifest references RAW / WORK / QUARANTINE material")

    print(f"ALLOW: valid KFM ReleaseManifest: {manifest_path}")


if __name__ == "__main__":
    main()
