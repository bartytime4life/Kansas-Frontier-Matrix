#!/usr/bin/env python3
"""
Validate KFM DCAT dataset exports.

Checks:
- JSON Schema validity
- public-only access posture
- provenance pointer present
- distribution licenses present
- no RAW / WORK / QUARANTINE references in public export
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path("contracts/v1/catalog/dcat/kfm_dcat_dataset.schema.json")
FORBIDDEN_PUBLIC_REFS = ("/raw/", "/work/", "/quarantine/", "data/raw/", "data/work/", "data/quarantine/")


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

    if not doc.get("dct:provenance"):
        fail("DCAT dataset missing dct:provenance")

    distributions = doc.get("dcat:distribution", [])

    if not distributions:
        fail("DCAT dataset missing distributions")

    for idx, distribution in enumerate(distributions):
        if not distribution.get("dcat:accessURL"):
            fail(f"distribution[{idx}] missing dcat:accessURL")

        if not distribution.get("dct:license"):
            fail(f"distribution[{idx}] missing dct:license")

    if contains_forbidden_ref(doc):
        fail("public DCAT export references RAW / WORK / QUARANTINE material")

    print(f"ALLOW: valid KFM DCAT dataset export: {dataset_path}")


if __name__ == "__main__":
    main()
