#!/usr/bin/env python3
"""
Validate KFM CatalogMatrix files.

Checks:
- JSON Schema validity
- closure status is closed
- public-only policy posture
- reviewed or published review state
- required top-level refs exist
- required artifact closure refs exist
- artifact_count matches artifacts length when both are present
- no RAW / WORK / QUARANTINE references
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path("contracts/v1/catalog/kfm_catalog_matrix.schema.json")

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
    "",
}


REQUIRED_TOP_LEVEL_REFS = (
    "artifact",
    "provenance",
    "evidence",
    "stac",
    "dcat",
    "release",
    "publish_receipt",
)

REQUIRED_ARTIFACT_REFS = (
    "artifact_ref",
    "evidence_ref",
    "provenance_ref",
    "stac_ref",
    "dcat_ref",
    "release_ref",
    "publish_receipt_ref",
)


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


def validate_ref_object(doc: dict[str, Any], key: str) -> None:
    value = assert_present(doc, key, "CatalogMatrix")

    if not isinstance(value, dict):
        fail(f"CatalogMatrix {key} must be an object")

    ref = assert_present(value, "ref", f"CatalogMatrix.{key}")
    assert_not_blocked(ref, f"CatalogMatrix.{key}.ref")

    resolved = value.get("resolved")
    if resolved is not None and not isinstance(resolved, bool):
        fail(f"CatalogMatrix.{key}.resolved must be boolean when provided")


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_catalog_matrix.py <catalog-matrix.json>")

    matrix_path = Path(sys.argv[1])

    if not matrix_path.exists():
        fail(f"missing CatalogMatrix: {matrix_path}")

    if not SCHEMA_PATH.exists():
        fail(f"missing schema: {SCHEMA_PATH}")

    schema = load_json(SCHEMA_PATH)
    doc = load_json(matrix_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))

    if errors:
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"DENY: schema error at {loc}: {error.message}", file=sys.stderr)
        sys.exit(1)

    if doc.get("status") != "closed":
        fail("CatalogMatrix requires status=closed for public publication")

    if doc.get("policy_label") not in (None, "public"):
        fail("CatalogMatrix requires policy_label=public when provided")

    if doc.get("review_state") not in (None, "reviewed", "published"):
        fail("CatalogMatrix requires review_state reviewed or published when provided")

    if doc.get("sensitivity") not in (None, "public"):
        fail("CatalogMatrix requires sensitivity=public when provided")

    for key in REQUIRED_TOP_LEVEL_REFS:
        validate_ref_object(doc, key)

    artifacts = doc.get("artifacts", [])

    if artifacts:
        if not isinstance(artifacts, list):
            fail("CatalogMatrix artifacts must be an array")

        artifact_count = doc.get("artifact_count")
        if artifact_count is not None and artifact_count != len(artifacts):
            fail("CatalogMatrix artifact_count does not match artifacts length")

        for idx, artifact in enumerate(artifacts):
            if not isinstance(artifact, dict):
                fail(f"artifacts[{idx}] must be an object")

            label = f"artifacts[{idx}]"

            for key in REQUIRED_ARTIFACT_REFS:
                value = assert_present(artifact, key, label)
                assert_not_blocked(value, f"{label}.{key}")

    if contains_forbidden_ref(doc):
        fail("public CatalogMatrix references RAW / WORK / QUARANTINE material")

    print(f"ALLOW: valid KFM CatalogMatrix: {matrix_path}")


if __name__ == "__main__":
    main()
