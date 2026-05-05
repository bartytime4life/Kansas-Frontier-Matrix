#!/usr/bin/env python3
"""
Validate KFM STAC Item exports.

Checks:
- JSON Schema validity
- public-only policy posture
- reviewed or published review state
- required provenance, evidence, and release links
- required data and provenance assets
- public sensitivity posture when provided
- no RAW / WORK / QUARANTINE references in public export
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path("contracts/v1/catalog/stac/kfm_stac_item.schema.json")

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


def link_rels(doc: dict[str, Any]) -> set[str]:
    return {
        link.get("rel", "")
        for link in doc.get("links", [])
        if isinstance(link, dict)
    }


def asset_roles(asset: dict[str, Any]) -> set[str]:
    roles = asset.get("roles", [])
    if not isinstance(roles, list):
        return set()
    return {role for role in roles if isinstance(role, str)}


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_stac_item.py <item.json>")

    item_path = Path(sys.argv[1])

    if not item_path.exists():
        fail(f"missing STAC item: {item_path}")

    if not SCHEMA_PATH.exists():
        fail(f"missing schema: {SCHEMA_PATH}")

    schema = load_json(SCHEMA_PATH)
    doc = load_json(item_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))

    if errors:
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"DENY: schema error at {loc}: {error.message}", file=sys.stderr)
        sys.exit(1)

    if doc.get("type") != "Feature":
        fail("STAC item must be GeoJSON Feature")

    props = doc.get("properties", {})

    if props.get("kfm:policy_label") != "public":
        fail("STAC public export requires kfm:policy_label=public")

    if props.get("kfm:review_state") not in {"reviewed", "published"}:
        fail("STAC public export requires reviewed or published review state")

    if props.get("kfm:sensitivity") not in (None, "public"):
        fail("STAC public export requires kfm:sensitivity=public when provided")

    assert_present(props, "kfm:spec_hash", "properties")
    assert_present(props, "kfm:evidence_ref", "properties")
    assert_present(props, "kfm:run_receipt_url", "properties")
    assert_present(props, "kfm:release_manifest_ref", "properties")
    assert_present(props, "kfm:source_role", "properties")
    assert_present(props, "processing:software", "properties")
    assert_present(props, "processing:version", "properties")
    assert_present(props, "processing:datetime", "properties")

    for key in (
        "kfm:evidence_ref",
        "kfm:run_receipt_url",
        "kfm:release_manifest_ref",
        "kfm:source_role",
        "processing:software",
        "processing:version",
    ):
        assert_not_blocked(props.get(key), f"properties {key}")

    required_rels = {"provenance", "evidence", "release-manifest"}
    missing_rels = sorted(required_rels - link_rels(doc))

    if missing_rels:
        fail(f"missing required STAC links: {', '.join(missing_rels)}")

    assets = doc.get("assets", {})

    data_asset = assets.get("data")
    if not isinstance(data_asset, dict):
        fail("STAC item missing data asset")

    provenance_asset = assets.get("provenance")
    if not isinstance(provenance_asset, dict):
        fail("STAC item missing provenance asset")

    assert_present(data_asset, "href", "assets.data")
    assert_present(provenance_asset, "href", "assets.provenance")

    data_roles = asset_roles(data_asset)
    provenance_roles = asset_roles(provenance_asset)

    if data_roles and "data" not in data_roles:
        fail("assets.data roles must include data when roles are provided")

    if provenance_roles and "provenance" not in provenance_roles:
        fail("assets.provenance roles must include provenance when roles are provided")

    if props.get("kfm:redaction_receipt_url") and "redaction-receipt" not in link_rels(doc):
        fail("redaction receipt property requires redaction-receipt link")

    if props.get("kfm:ai_receipt_url") and "ai-receipt" not in link_rels(doc):
        fail("AI receipt property requires ai-receipt link")

    if props.get("kfm:attestation_url") and "attestation" not in link_rels(doc):
        fail("attestation property requires attestation link")

    if contains_forbidden_ref(doc):
        fail("public STAC export references RAW / WORK / QUARANTINE material")

    print(f"ALLOW: valid KFM STAC item export: {item_path}")


if __name__ == "__main__":
    main()
