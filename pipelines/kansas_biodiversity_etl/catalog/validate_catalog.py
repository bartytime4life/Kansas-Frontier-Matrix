#!/usr/bin/env python3
"""
Validate catalog closure for the Kansas biodiversity ETL.

Checks:
- metadata exists and carries spec_hash
- STAC collection exists and parses
- at least one STAC item exists and parses
- DCAT dataset exists and parses
- PROV lineage document exists and parses
- STAC collection spec_hash matches metadata
- every STAC item spec_hash matches metadata
- DCAT spec_hash matches metadata
- PROV dataset spec_hash matches metadata
- optional JSON Schema validation when --schema-root is supplied

Fail-closed:
Any violation => FAIL
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


JsonObject = Dict[str, Any]


try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None


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


def schema_path(schema_root: Optional[Path], filename: str) -> Optional[Path]:
    if schema_root is None:
        return None
    return schema_root / filename


def validate_schema(instance: JsonObject, schema_file: Optional[Path], failure_reason: str) -> None:
    if schema_file is None:
        return

    if jsonschema is None:
        raise RuntimeError("jsonschema_missing")

    if not schema_file.exists():
        raise RuntimeError(f"catalog_schema_missing:{schema_file.name}")

    try:
        schema = load_json(schema_file)
        jsonschema.validate(instance=instance, schema=schema)
    except RuntimeError:
        raise
    except Exception as exc:
        raise RuntimeError(failure_reason) from exc


def stac_collection_spec_hash(collection: JsonObject) -> Optional[str]:
    summaries = collection.get("summaries")
    if not isinstance(summaries, dict):
        return None

    values = summaries.get("kfm:spec_hash")
    if isinstance(values, list) and values:
        return str(values[0])

    if isinstance(values, str):
        return values

    return None


def stac_item_spec_hash(item: JsonObject) -> Optional[str]:
    properties = item.get("properties")
    if not isinstance(properties, dict):
        return None

    value = properties.get("kfm:spec_hash")
    return str(value) if value else None


def dcat_spec_hash(dcat: JsonObject) -> Optional[str]:
    value = dcat.get("kfm:spec_hash")
    return str(value) if value else None


def prov_spec_hash(prov: JsonObject) -> Optional[str]:
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


def validate_stac_collection(
    stac_root: Path,
    expected_hash: str,
    schema_root: Optional[Path],
) -> JsonObject:
    collection_path = stac_root / "collection.json"

    collection = load_required_json(
        collection_path,
        "stac_collection_missing",
        "invalid_stac_collection_json",
    )

    validate_schema(
        collection,
        schema_path(schema_root, "stac_collection.schema.json"),
        "invalid_stac_collection_schema",
    )

    if collection.get("type") != "Collection":
        raise RuntimeError("stac_collection_wrong_type")

    actual_hash = stac_collection_spec_hash(collection)

    if not actual_hash:
        raise RuntimeError("stac_collection_missing_spec_hash")

    if actual_hash != expected_hash:
        raise RuntimeError("stac_collection_spec_hash_mismatch")

    return collection


def validate_stac_items(
    stac_root: Path,
    expected_hash: str,
    schema_root: Optional[Path],
) -> List[JsonObject]:
    items: List[JsonObject] = []

    for item_path in stac_item_paths(stac_root):
        try:
            item = load_json(item_path)
        except Exception as exc:
            raise RuntimeError(f"invalid_stac_item_json:{item_path.name}") from exc

        if not isinstance(item, dict):
            raise RuntimeError(f"invalid_stac_item_json:{item_path.name}")

        validate_schema(
            item,
            schema_path(schema_root, "stac_item.schema.json"),
            f"invalid_stac_item_schema:{item_path.name}",
        )

        if item.get("type") != "Feature":
            raise RuntimeError(f"stac_item_wrong_type:{item_path.name}")

        actual_hash = stac_item_spec_hash(item)

        if not actual_hash:
            raise RuntimeError(f"stac_item_missing_spec_hash:{item_path.name}")

        if actual_hash != expected_hash:
            raise RuntimeError(f"stac_item_spec_hash_mismatch:{item_path.name}")

        items.append(item)

    return items


def validate_dcat(path: Path, expected_hash: str, schema_root: Optional[Path]) -> JsonObject:
    dcat = load_required_json(path, "dcat_missing", "invalid_dcat_json")

    validate_schema(
        dcat,
        schema_path(schema_root, "dcat_dataset.schema.json"),
        "invalid_dcat_schema",
    )

    actual_hash = dcat_spec_hash(dcat)

    if not actual_hash:
        raise RuntimeError("dcat_missing_spec_hash")

    if actual_hash != expected_hash:
        raise RuntimeError("dcat_spec_hash_mismatch")

    return dcat


def validate_prov(path: Path, expected_hash: str, schema_root: Optional[Path]) -> JsonObject:
    prov = load_required_json(path, "prov_missing", "invalid_prov_json")

    validate_schema(
        prov,
        schema_path(schema_root, "prov_document.schema.json"),
        "invalid_prov_schema",
    )

    actual_hash = prov_spec_hash(prov)

    if not actual_hash:
        raise RuntimeError("prov_missing_spec_hash")

    if actual_hash != expected_hash:
        raise RuntimeError("prov_spec_hash_mismatch")

    return prov


def resolve_schema_root(value: Optional[str]) -> Optional[Path]:
    if not value:
        return None

    root = Path(value)

    if not root.exists():
        raise RuntimeError("schema_root_missing")

    if not root.is_dir():
        raise RuntimeError("schema_root_not_directory")

    return root


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Kansas biodiversity ETL STAC/DCAT/PROV catalog closure."
    )
    parser.add_argument("--metadata", required=True)
    parser.add_argument("--stac-root", required=True)
    parser.add_argument("--dcat", required=True)
    parser.add_argument("--prov", required=True)
    parser.add_argument(
        "--schema-root",
        default=None,
        help="Optional schema root, usually schemas/catalog.",
    )
    args = parser.parse_args()

    metadata_path = Path(args.metadata)
    stac_root = Path(args.stac_root)
    dcat_path = Path(args.dcat)
    prov_path = Path(args.prov)

    try:
        schema_root = resolve_schema_root(args.schema_root)

        metadata = load_required_json(
            metadata_path,
            "metadata_missing",
            "invalid_metadata_json",
        )
        expected_hash = metadata_spec_hash(metadata)

        collection = validate_stac_collection(stac_root, expected_hash, schema_root)
        items = validate_stac_items(stac_root, expected_hash, schema_root)
        dcat = validate_dcat(dcat_path, expected_hash, schema_root)
        prov = validate_prov(prov_path, expected_hash, schema_root)

    except RuntimeError as exc:
        return fail(str(exc))

    checks = [
        "metadata",
        "stac_collection",
        "stac_items",
        "dcat",
        "prov",
        "spec_hash_alignment",
    ]

    if args.schema_root:
        checks.append("json_schema")

    print(
        json.dumps(
            {
                "decision": "PASS",
                "metadata": str(metadata_path),
                "stac_collection": str(stac_root / "collection.json"),
                "stac_items": len(items),
                "dcat": str(dcat_path),
                "prov": str(prov_path),
                "schema_root": str(schema_root) if args.schema_root else None,
                "dataset_id": metadata.get("dataset_id"),
                "spec_hash": expected_hash,
                "checks": checks,
            },
            sort_keys=True,
        )
    )

    _ = collection, dcat, prov

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
