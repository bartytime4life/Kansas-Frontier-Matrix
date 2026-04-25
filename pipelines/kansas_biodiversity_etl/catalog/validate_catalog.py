#!/usr/bin/env python3
"""
Validate catalog closure for the Kansas biodiversity ETL.

Checks:
- STAC collection exists and parses
- at least one STAC item exists and parses
- DCAT dataset exists and parses
- PROV lineage document exists and parses
- metadata exists and carries spec_hash
- STAC collection spec_hash matches metadata
- every STAC item spec_hash matches metadata
- DCAT spec_hash matches metadata
- PROV dataset spec_hash matches metadata

Fail-closed:
Any violation => FAIL
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


JsonObject = Dict[str, Any]


def fail(reason: str) -> int:
    print(json.dumps({"decision": "FAIL", "reason": reason}, sort_keys=True))
    return 1


def load_json(path: Path) -> JsonObject:
    return json.loads(path.read_text(encoding="utf-8"))


def load_required_json(path: Path, missing_reason: str, invalid_reason: str) -> JsonObject:
    if not path.exists():
        raise RuntimeError(missing_reason)

    try:
        payload = load_json(path)
    except Exception as exc:
        raise RuntimeError(invalid_reason) from exc

    if not isinstance(payload, dict):
        raise RuntimeError(invalid_reason)

    return payload


def metadata_spec_hash(metadata: JsonObject) -> str:
    spec_hash = metadata.get("spec_hash")

    if not spec_hash:
        raise RuntimeError("metadata_missing_spec_hash")

    return str(spec_hash)


def stac_collection_spec_hash(collection: JsonObject) -> str | None:
    summaries = collection.get("summaries")
    if not isinstance(summaries, dict):
        return None

    values = summaries.get("kfm:spec_hash")
    if isinstance(values, list) and values:
        return str(values[0])

    if isinstance(values, str):
        return values

    return None


def stac_item_spec_hash(item: JsonObject) -> str | None:
    properties = item.get("properties")
    if not isinstance(properties, dict):
        return None

    value = properties.get("kfm:spec_hash")
    return str(value) if value else None


def dcat_spec_hash(dcat: JsonObject) -> str | None:
    value = dcat.get("kfm:spec_hash")
    return str(value) if value else None


def prov_spec_hash(prov: JsonObject) -> str | None:
    entity = prov.get("entity")
    if not isinstance(entity, dict):
        return None

    dataset = entity.get("dataset")
    if not isinstance(dataset, dict):
        return None

    value = dataset.get("kfm:spec_hash")
    return str(value) if value else None


def stac_item_paths(stac_root: Path) -> List[Path]:
    if not stac_root.exists():
        raise RuntimeError("stac_root_missing")

    if not stac_root.is_dir():
        raise RuntimeError("stac_root_not_directory")

    paths = sorted(
        path
        for path in stac_root.glob("*.item.json")
        if path.name != "collection.json"
    )

    if not paths:
        raise RuntimeError("no_stac_items_found")

    return paths


def validate_stac_collection(stac_root: Path, expected_hash: str) -> JsonObject:
    collection_path = stac_root / "collection.json"

    collection = load_required_json(
        collection_path,
        "stac_collection_missing",
        "invalid_stac_collection_json",
    )

    if collection.get("type") != "Collection":
        raise RuntimeError("stac_collection_wrong_type")

    actual_hash = stac_collection_spec_hash(collection)

    if not actual_hash:
        raise RuntimeError("stac_collection_missing_spec_hash")

    if actual_hash != expected_hash:
        raise RuntimeError("stac_collection_spec_hash_mismatch")

    return collection


def validate_stac_items(stac_root: Path, expected_hash: str) -> List[JsonObject]:
    items: List[JsonObject] = []

    for item_path in stac_item_paths(stac_root):
        try:
            item = load_json(item_path)
        except Exception as exc:
            raise RuntimeError(f"invalid_stac_item_json:{item_path.name}") from exc

        if not isinstance(item, dict):
            raise RuntimeError(f"invalid_stac_item_json:{item_path.name}")

        if item.get("type") != "Feature":
            raise RuntimeError(f"stac_item_wrong_type:{item_path.name}")

        actual_hash = stac_item_spec_hash(item)

        if not actual_hash:
            raise RuntimeError(f"stac_item_missing_spec_hash:{item_path.name}")

        if actual_hash != expected_hash:
            raise RuntimeError(f"stac_item_spec_hash_mismatch:{item_path.name}")

        items.append(item)

    return items


def validate_dcat(path: Path, expected_hash: str) -> JsonObject:
    dcat = load_required_json(path, "dcat_missing", "invalid_dcat_json")

    actual_hash = dcat_spec_hash(dcat)

    if not actual_hash:
        raise RuntimeError("dcat_missing_spec_hash")

    if actual_hash != expected_hash:
        raise RuntimeError("dcat_spec_hash_mismatch")

    return dcat


def validate_prov(path: Path, expected_hash: str) -> JsonObject:
    prov = load_required_json(path, "prov_missing", "invalid_prov_json")

    actual_hash = prov_spec_hash(prov)

    if not actual_hash:
        raise RuntimeError("prov_missing_spec_hash")

    if actual_hash != expected_hash:
        raise RuntimeError("prov_spec_hash_mismatch")

    return prov


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Kansas biodiversity ETL STAC/DCAT/PROV catalog closure."
    )
    parser.add_argument("--metadata", required=True)
    parser.add_argument("--stac-root", required=True)
    parser.add_argument("--dcat", required=True)
    parser.add_argument("--prov", required=True)
    args = parser.parse_args()

    metadata_path = Path(args.metadata)
    stac_root = Path(args.stac_root)
    dcat_path = Path(args.dcat)
    prov_path = Path(args.prov)

    try:
        metadata = load_required_json(
            metadata_path,
            "metadata_missing",
            "invalid_metadata_json",
        )
        expected_hash = metadata_spec_hash(metadata)

        collection = validate_stac_collection(stac_root, expected_hash)
        items = validate_stac_items(stac_root, expected_hash)
        dcat = validate_dcat(dcat_path, expected_hash)
        prov = validate_prov(prov_path, expected_hash)

    except RuntimeError as exc:
        return fail(str(exc))

    print(
        json.dumps(
            {
                "decision": "PASS",
                "metadata": str(metadata_path),
                "stac_collection": str(stac_root / "collection.json"),
                "stac_items": len(items),
                "dcat": str(dcat_path),
                "prov": str(prov_path),
                "dataset_id": metadata.get("dataset_id"),
                "spec_hash": expected_hash,
                "checks": [
                    "metadata",
                    "stac_collection",
                    "stac_items",
                    "dcat",
                    "prov",
                    "spec_hash_alignment",
                ],
            },
            sort_keys=True,
        )
    )

    # Keep references alive for static analyzers and future debug expansion.
    _ = collection, dcat, prov

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
