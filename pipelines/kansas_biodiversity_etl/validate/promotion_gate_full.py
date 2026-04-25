#!/usr/bin/env python3
"""
Full Promotion Gate (A-I) for Kansas Biodiversity ETL.

Supports:
- JSONL thin-slice artifacts
- single-file Parquet artifacts
- partitioned Parquet dataset directories
- format-independent spec_hash via _dataset_metadata.json
- local receipt proof verification
- optional catalog closure validation for STAC/DCAT/PROV outputs

Gate Checks:

A. EvidenceBundle present and valid JSON
B. Dataset exists
C. Dataset metadata exists when validating Parquet
D. EvidenceBundle spec_hash matches dataset metadata spec_hash
E. License validity
F. Attribution completeness
G. Sensitivity enforcement
H. Receipt proof verification
I. Catalog closure validation

Fail-closed:
Any violation => FAIL
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

try:
    import pyarrow.parquet as pq
except ImportError:  # pragma: no cover
    pq = None


JsonRecord = Dict[str, Any]
JsonObject = Dict[str, Any]


def fail(reason: str) -> int:
    print(json.dumps({"decision": "FAIL", "reason": reason}, sort_keys=True))
    return 1


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def load_json(path: Path) -> JsonObject:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> List[JsonRecord]:
    records: List[JsonRecord] = []

    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                records.append(json.loads(stripped))

    return records


def read_parquet(path: Path) -> List[JsonRecord]:
    if pq is None:
        raise RuntimeError("pyarrow_missing_for_parquet_validation")

    table = pq.read_table(path)
    return table.to_pylist()


def read_partitioned_parquet(dataset_root: Path) -> List[JsonRecord]:
    parquet_files = sorted(dataset_root.rglob("*.parquet"))

    if not parquet_files:
        raise RuntimeError("no_parquet_files_found")

    records: List[JsonRecord] = []

    for parquet_file in parquet_files:
        records.extend(read_parquet(parquet_file))

    return records


def read_dataset_records(dataset_path: Path) -> List[JsonRecord]:
    if dataset_path.is_dir():
        return read_partitioned_parquet(dataset_path)

    suffix = dataset_path.suffix.lower()

    if suffix == ".jsonl":
        return read_jsonl(dataset_path)

    if suffix == ".parquet":
        return read_parquet(dataset_path)

    raise RuntimeError(f"unsupported_dataset_format:{suffix}")


def resolve_metadata_path(dataset_path: Path, metadata_path: Optional[Path]) -> Optional[Path]:
    if metadata_path is not None:
        return metadata_path

    if dataset_path.is_dir():
        return dataset_path / "_dataset_metadata.json"

    if dataset_path.suffix.lower() == ".parquet":
        return dataset_path.parent / "_dataset_metadata.json"

    return None


def expected_spec_hash(dataset_path: Path, metadata_path: Optional[Path]) -> str:
    if dataset_path.is_dir() or dataset_path.suffix.lower() == ".parquet":
        resolved_metadata_path = resolve_metadata_path(dataset_path, metadata_path)

        if resolved_metadata_path is None or not resolved_metadata_path.exists():
            raise RuntimeError("missing_dataset_metadata")

        try:
            metadata = load_json(resolved_metadata_path)
        except Exception as exc:
            raise RuntimeError("invalid_dataset_metadata_json") from exc

        spec_hash = metadata.get("spec_hash")
        if not spec_hash:
            raise RuntimeError("metadata_missing_spec_hash")

        return str(spec_hash)

    if dataset_path.suffix.lower() == ".jsonl":
        return sha256_file(dataset_path)

    raise RuntimeError(f"unsupported_dataset_format:{dataset_path.suffix.lower()}")


def verify_receipt_proof(receipt_path: Path, proof_path: Path) -> Optional[str]:
    if not receipt_path.exists():
        return "receipt_missing"

    if not proof_path.exists():
        return "proof_missing"

    try:
        proof = load_json(proof_path)
    except Exception:
        return "invalid_proof_json"

    expected = proof.get("receipt_hash")
    actual = sha256_file(receipt_path)

    if not expected:
        return "proof_missing_receipt_hash"

    if expected != actual:
        return "receipt_proof_hash_mismatch"

    return None


def primary_key(record: JsonRecord) -> str:
    return f"{record.get('institution_code')}|{record.get('id')}"


def validate_record_level_rules(records: Iterable[JsonRecord]) -> Optional[str]:
    seen_keys = set()

    for record in records:
        pk = primary_key(record)

        if pk in seen_keys:
            return "duplicate_primary_key_detected"

        seen_keys.add(pk)

        license_val = record.get("license")
        if not license_val:
            return "missing_license_in_dataset"

        if str(license_val).strip().lower() == "unknown":
            return "unknown_license_in_dataset"

        if license_val == "CC-BY-4.0" and not record.get("attribution"):
            return "missing_required_attribution"

        if record.get("sensitivity") == "restricted" and record.get("geometry") is not None:
            return "restricted_record_contains_geometry"

    return None


def validate_metadata_counts(
    metadata_path: Optional[Path],
    dataset_path: Path,
    record_count: int,
) -> Optional[str]:
    resolved_metadata_path = resolve_metadata_path(dataset_path, metadata_path)

    if resolved_metadata_path is None or not resolved_metadata_path.exists():
        return None

    try:
        metadata = load_json(resolved_metadata_path)
    except Exception:
        return "invalid_dataset_metadata_json"

    expected_records = metadata.get("records")
    if expected_records is not None and int(expected_records) != record_count:
        return "metadata_record_count_mismatch"

    return None


def catalog_stac_collection_spec_hash(collection: JsonObject) -> Optional[str]:
    summaries = collection.get("summaries")
    if not isinstance(summaries, dict):
        return None

    values = summaries.get("kfm:spec_hash")

    if isinstance(values, list) and values:
        return str(values[0])

    if isinstance(values, str):
        return values

    return None


def catalog_stac_item_spec_hash(item: JsonObject) -> Optional[str]:
    properties = item.get("properties")
    if not isinstance(properties, dict):
        return None

    value = properties.get("kfm:spec_hash")
    return str(value) if value else None


def catalog_dcat_spec_hash(dcat: JsonObject) -> Optional[str]:
    value = dcat.get("kfm:spec_hash")
    return str(value) if value else None


def catalog_prov_spec_hash(prov: JsonObject) -> Optional[str]:
    entity = prov.get("entity")
    if not isinstance(entity, dict):
        return None

    dataset = entity.get("dataset")
    if not isinstance(dataset, dict):
        return None

    value = dataset.get("kfm:spec_hash")
    return str(value) if value else None


def validate_catalog_closure(
    *,
    metadata_hash: str,
    stac_root: Path,
    dcat_path: Path,
    prov_path: Path,
) -> Optional[str]:
    if not stac_root.exists():
        return "stac_root_missing"

    if not stac_root.is_dir():
        return "stac_root_not_directory"

    stac_collection_path = stac_root / "collection.json"

    if not stac_collection_path.exists():
        return "stac_collection_missing"

    try:
        collection = load_json(stac_collection_path)
    except Exception:
        return "invalid_stac_collection_json"

    if collection.get("type") != "Collection":
        return "stac_collection_wrong_type"

    collection_hash = catalog_stac_collection_spec_hash(collection)

    if not collection_hash:
        return "stac_collection_missing_spec_hash"

    if collection_hash != metadata_hash:
        return "stac_collection_spec_hash_mismatch"

    stac_items = sorted(stac_root.glob("*.item.json"))

    if not stac_items:
        return "no_stac_items_found"

    for item_path in stac_items:
        try:
            item = load_json(item_path)
        except Exception:
            return f"invalid_stac_item_json:{item_path.name}"

        if item.get("type") != "Feature":
            return f"stac_item_wrong_type:{item_path.name}"

        item_hash = catalog_stac_item_spec_hash(item)

        if not item_hash:
            return f"stac_item_missing_spec_hash:{item_path.name}"

        if item_hash != metadata_hash:
            return f"stac_item_spec_hash_mismatch:{item_path.name}"

    if not dcat_path.exists():
        return "dcat_missing"

    try:
        dcat = load_json(dcat_path)
    except Exception:
        return "invalid_dcat_json"

    dcat_hash = catalog_dcat_spec_hash(dcat)

    if not dcat_hash:
        return "dcat_missing_spec_hash"

    if dcat_hash != metadata_hash:
        return "dcat_spec_hash_mismatch"

    if not prov_path.exists():
        return "prov_missing"

    try:
        prov = load_json(prov_path)
    except Exception:
        return "invalid_prov_json"

    prov_hash = catalog_prov_spec_hash(prov)

    if not prov_hash:
        return "prov_missing_spec_hash"

    if prov_hash != metadata_hash:
        return "prov_spec_hash_mismatch"

    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument(
        "--metadata",
        default=None,
        help="Optional metadata path. Required for explicit Parquet metadata validation; defaults to dataset parent/root.",
    )
    parser.add_argument(
        "--receipt",
        default=None,
        help="Optional run receipt path. Required when --proof is supplied.",
    )
    parser.add_argument(
        "--proof",
        default=None,
        help="Optional local receipt proof path. If supplied, receipt proof verification is enforced.",
    )
    parser.add_argument(
        "--stac-root",
        default=None,
        help="Optional STAC output root. If supplied with --dcat and --prov, catalog closure is enforced.",
    )
    parser.add_argument(
        "--dcat",
        default=None,
        help="Optional DCAT dataset JSON path. Required when --stac-root or --prov is supplied.",
    )
    parser.add_argument(
        "--prov",
        default=None,
        help="Optional PROV lineage JSON path. Required when --stac-root or --dcat is supplied.",
    )
    args = parser.parse_args()

    dataset_path = Path(args.dataset)
    evidence_path = Path(args.evidence)
    metadata_path = Path(args.metadata) if args.metadata else None
    receipt_path = Path(args.receipt) if args.receipt else None
    proof_path = Path(args.proof) if args.proof else None
    stac_root = Path(args.stac_root) if args.stac_root else None
    dcat_path = Path(args.dcat) if args.dcat else None
    prov_path = Path(args.prov) if args.prov else None

    if not dataset_path.exists():
        return fail("dataset_missing")

    if not evidence_path.exists():
        return fail("evidencebundle_missing")

    try:
        evidence_doc = load_json(evidence_path)
        bundle = evidence_doc["evidenceBundle"]
    except Exception:
        return fail("invalid_evidencebundle_json")

    if proof_path is not None:
        if receipt_path is None:
            return fail("receipt_required_when_proof_supplied")

        proof_error = verify_receipt_proof(receipt_path, proof_path)
        if proof_error:
            return fail(proof_error)

    try:
        actual_hash = expected_spec_hash(dataset_path, metadata_path)
    except RuntimeError as exc:
        return fail(str(exc))

    evidence_hash = bundle.get("spec_hash")
    if not evidence_hash:
        return fail("evidencebundle_missing_spec_hash")

    if evidence_hash != actual_hash:
        return fail("spec_hash_mismatch")

    if int(bundle.get("items", 0)) <= 0:
        return fail("empty_evidencebundle_items")

    if not bundle.get("source_uris"):
        return fail("missing_source_uris")

    if not bundle.get("license"):
        return fail("missing_evidencebundle_license")

    if not bundle.get("attribution"):
        return fail("missing_evidencebundle_attribution")

    try:
        records = read_dataset_records(dataset_path)
    except RuntimeError as exc:
        return fail(str(exc))
    except Exception:
        return fail("dataset_read_failed")

    if len(records) == 0:
        return fail("empty_dataset")

    if int(bundle.get("items", 0)) != len(records):
        return fail("item_count_mismatch")

    metadata_error = validate_metadata_counts(metadata_path, dataset_path, len(records))
    if metadata_error:
        return fail(metadata_error)

    record_error = validate_record_level_rules(records)
    if record_error:
        return fail(record_error)

    catalog_args = [stac_root, dcat_path, prov_path]
    catalog_requested = any(value is not None for value in catalog_args)

    if catalog_requested:
        if stac_root is None:
            return fail("stac_root_required_for_catalog_validation")

        if dcat_path is None:
            return fail("dcat_required_for_catalog_validation")

        if prov_path is None:
            return fail("prov_required_for_catalog_validation")

        catalog_error = validate_catalog_closure(
            metadata_hash=actual_hash,
            stac_root=stac_root,
            dcat_path=dcat_path,
            prov_path=prov_path,
        )

        if catalog_error:
            return fail(catalog_error)

    passed_gates = ["A", "B", "C", "D", "E", "F", "G"]

    if proof_path is not None:
        passed_gates.append("H")

    if catalog_requested:
        passed_gates.append("I")

    print(
        json.dumps(
            {
                "decision": "PASS",
                "dataset": str(dataset_path),
                "evidence": str(evidence_path),
                "metadata": str(metadata_path) if metadata_path else None,
                "receipt": str(receipt_path) if receipt_path else None,
                "proof": str(proof_path) if proof_path else None,
                "stac_root": str(stac_root) if stac_root else None,
                "dcat": str(dcat_path) if dcat_path else None,
                "prov": str(prov_path) if prov_path else None,
                "records": len(records),
                "spec_hash": actual_hash,
                "gates": passed_gates,
            },
            sort_keys=True,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
