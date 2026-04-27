#!/usr/bin/env python3
"""
Validate KFM DCAT dataset exports.

Checks:
- JSON Schema validity
- public-only access posture
- provenance pointer present
- evidence and release manifest references present
- distribution access URLs and licenses present
- distribution license consistency
- no RAW / WORK / QUARANTINE references in public export
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path("contracts/v1/catalog/dcat/kfm_dcat_dataset.schema.json")

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
        fail("usage: validate_dcat_dataset.py <dataset.jsonld>")

    dataset_path = Path(sys.argv[1])

    if not dataset_path.exists():
        fail(f"missing DCAT dataset: {dataset_path}")

    if not SCHEMA_PATH.exists():
        fail(f"missing schema: {SCHEMA_PATH}")

    schema = load_json(SCHEMA_PATH)
    doc = load_json(dataset_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))

    if errors:
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"DENY: schema error at {loc}: {error.message}", file=sys.stderr)
        sys.exit(1)

    if doc.get("@type") != "dcat:Dataset":
        fail("DCAT export must be @type dcat:Dataset")

    if doc.get("kfm:policy_label") != "public":
        fail("DCAT public export requires kfm:policy_label=public")

    if doc.get("dct:accessRights") != "public":
        fail("DCAT public export requires dct:accessRights=public")

    if doc.get("kfm:sensitivity") not in (None, "public"):
        fail("DCAT public export requires kfm:sensitivity=public when provided")

    license_value = assert_present(doc, "dct:license", "dataset")
    assert_not_blocked(license_value, "dataset dct:license")

    assert_present(doc, "dct:provenance", "dataset")
    assert_present(doc, "kfm:spec_hash", "dataset")
    assert_present(doc, "kfm:evidence_ref", "dataset")
    assert_present(doc, "kfm:release_manifest_ref", "dataset")
    assert_present(doc, "kfm:source_role", "dataset")

    review_state = doc.get("kfm:review_state")
    if review_state not in {"reviewed", "published"}:
        fail("DCAT public export requires kfm:review_state reviewed or published")

    distributions = doc.get("dcat:distribution", [])

    if not distributions:
        fail("DCAT dataset missing distributions")

    for idx, distribution in enumerate(distributions):
        if distribution.get("@type") != "dcat:Distribution":
            fail(f"distribution[{idx}] must be @type dcat:Distribution")

        assert_present(distribution, "dcat:accessURL", f"distribution[{idx}]")

        distribution_license = assert_present(
            distribution,
            "dct:license",
            f"distribution[{idx}]",
        )
        assert_not_blocked(distribution_license, f"distribution[{idx}] dct:license")

        if distribution_license != license_value:
            fail(
                f"distribution[{idx}] license differs from dataset license; "
                "reviewed exception is not represented"
            )

    if contains_forbidden_ref(doc):
        fail("public DCAT export references RAW / WORK / QUARANTINE material")

    print(f"ALLOW: valid KFM DCAT dataset export: {dataset_path}")


if __name__ == "__main__":
    main()
