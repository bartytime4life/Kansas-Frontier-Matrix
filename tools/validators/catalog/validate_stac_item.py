#!/usr/bin/env python3
"""
Validate KFM STAC Item exports.
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


def link_rels(doc: dict[str, Any]) -> set[str]:
    return {
        link.get("rel", "")
        for link in doc.get("links", [])
        if isinstance(link, dict)
    }


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

    props = doc.get("properties", {})

    if props.get("kfm:policy_label") != "public":
        fail("STAC public export requires kfm:policy_label=public")

    if props.get("kfm:review_state") not in {"reviewed", "published"}:
        fail("STAC public export requires reviewed or published review state")

    required_rels = {"provenance", "evidence", "release-manifest"}
    missing_rels = sorted(required_rels - link_rels(doc))

    if missing_rels:
        fail(f"missing required STAC links: {', '.join(missing_rels)}")

    assets = doc.get("assets", {})

    if "data" not in assets:
        fail("STAC item missing data asset")

    if "provenance" not in assets:
        fail("STAC item missing provenance asset")

    if contains_forbidden_ref(doc):
        fail("public STAC export references RAW / WORK / QUARANTINE material")

    print(f"ALLOW: valid KFM STAC item export: {item_path}")


if __name__ == "__main__":
    main()
