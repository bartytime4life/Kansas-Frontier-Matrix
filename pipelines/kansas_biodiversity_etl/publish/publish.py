```python
#!/usr/bin/env python3
"""
Publish deduped Kansas biodiversity occurrence records to a governed,
partitioned Parquet dataset.

Path:
    pipelines/kansas_biodiversity_etl/publish/publish.py

Input:
    Canonical/deduped JSONL records from dedupe_occurrences.py.

Outputs:
    - Partitioned Parquet dataset root
    - _dataset_metadata.json
    - EvidenceBundle JSON
    - run_receipt.json

Identity:
    spec_hash is computed from a deterministic canonical JSON stream,
    not from Parquet bytes. This keeps dataset identity stable across
    storage rewrites, compression changes, and partition layout changes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import pyarrow as pa
import pyarrow.parquet as pq


JsonRecord = Dict[str, Any]


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def read_jsonl(path: Path) -> List[JsonRecord]:
    records: List[JsonRecord] = []

    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue

            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid_jsonl_line:{line_number}") from exc

            if not isinstance(record, dict):
                raise ValueError(f"jsonl_line_not_object:{line_number}")

            records.append(record)

    return records


def canonical_record(record: JsonRecord) -> JsonRecord:
    """
    Return the record shape used for dataset identity.

    Current rule:
    - include all governed record fields exactly as emitted by dedupe
    - sort keys during serialization
    - do not include runtime receipt fields or file layout details

    If future publisher-only fields are added, exclude them here explicitly.
    """
    return dict(record)


def canonical_bytes(records: Iterable[JsonRecord]) -> bytes:
    lines = [
        json.dumps(
            canonical_record(record),
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        for record in records
    ]

    return ("\n".join(lines) + "\n").encode("utf-8")


def dataset_spec_hash(records: List[JsonRecord]) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(records)).hexdigest()


def partition_key(record: JsonRecord) -> Tuple[str, str]:
    event_date = str(record.get("event_date") or "")

    if len(event_date) >= 7 and event_date[4] == "-" and event_date[5:7].isdigit():
        return event_date[:4], event_date[5:7]

    return "unknown", "unknown"


def group_by_partition(records: List[JsonRecord]) -> Dict[Tuple[str, str], List[JsonRecord]]:
    grouped: Dict[Tuple[str, str], List[JsonRecord]] = defaultdict(list)

    for record in records:
        grouped[partition_key(record)].append(record)

    return dict(grouped)


def remove_existing_dataset_contents(dataset_root: Path) -> None:
    """
    Remove previous partition outputs while preserving the dataset root.

    This prevents stale Parquet files from surviving between runs.
    """
    dataset_root.mkdir(parents=True, exist_ok=True)

    for child in dataset_root.iterdir():
        if child.name == "_dataset_metadata.json":
            child.unlink()
        elif child.is_dir() and child.name.startswith("year="):
            shutil.rmtree(child)
        elif child.is_file() and child.suffix == ".parquet":
            child.unlink()


def arrow_table(records: List[JsonRecord]) -> pa.Table:
    return pa.Table.from_pylist(records)


def write_partitioned_parquet(records: List[JsonRecord], dataset_root: Path) -> List[str]:
    remove_existing_dataset_contents(dataset_root)

    partitions = group_by_partition(records)
    written_files: List[str] = []

    for file_index, ((year, month), group) in enumerate(sorted(partitions.items())):
        partition_dir = dataset_root / f"year={year}" / f"month={month}"
        partition_dir.mkdir(parents=True, exist_ok=True)

        output_file = partition_dir / f"part-{file_index:03d}.parquet"

        pq.write_table(
            arrow_table(group),
            output_file,
            compression="zstd",
            use_dictionary=True,
        )

        written_files.append(str(output_file))

    return written_files


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def build_metadata(
    *,
    dataset_id: str,
    spec_hash: str,
    records: List[JsonRecord],
    written_files: List[str],
    generated_at: str,
) -> Dict[str, Any]:
    partitions = [
        {"year": year, "month": month, "records": len(group)}
        for (year, month), group in sorted(group_by_partition(records).items())
    ]

    return {
        "dataset_id": dataset_id,
        "spec_hash": spec_hash,
        "records": len(records),
        "files": len(written_files),
        "file_paths": written_files,
        "generated_at": generated_at,
        "format": "parquet_partitioned",
        "compression": "zstd",
        "partitioning": ["year", "month"],
        "partitions": partitions,
    }


def build_evidence_bundle(
    *,
    spec_hash: str,
    dataset_id: str,
    records: List[JsonRecord],
    source_uris: List[str],
    generated_at: str,
    license_label: str,
    attribution: str,
) -> Dict[str, Any]:
    return {
        "evidenceBundle": {
            "spec_hash": spec_hash,
            "dataset_id": dataset_id,
            "items": len(records),
            "harvest_date": generated_at,
            "source_uris": source_uris,
            "license": license_label,
            "attribution": attribution,
            "obligations": [
                "retain attribution",
                "fail closed on unknown license",
                "respect sensitivity redaction",
            ],
        }
    }


def build_receipt(
    *,
    dataset_root: Path,
    metadata_path: Path,
    evidence_path: Path,
    spec_hash: str,
    records: List[JsonRecord],
    written_files: List[str],
    generated_at: str,
) -> Dict[str, Any]:
    return {
        "candidate": str(dataset_root),
        "decision": "generated_not_promoted",
        "spec_hash": spec_hash,
        "items": len(records),
        "files": len(written_files),
        "metadata": str(metadata_path),
        "evidence_bundle": str(evidence_path),
        "generated_at": generated_at,
        "attestation_verified": False,
        "notes": [
            "Publisher generated governed artifacts only.",
            "Promotion requires validator pass and signature verification.",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Publish Kansas biodiversity occurrences to partitioned Parquet."
    )

    parser.add_argument("--input", required=True, help="Deduped canonical JSONL input")
    parser.add_argument("--dataset-root", required=True, help="Partitioned Parquet dataset root")
    parser.add_argument("--metadata-output", required=True, help="Dataset metadata JSON output")
    parser.add_argument("--evidence-output", required=True, help="EvidenceBundle JSON output")
    parser.add_argument("--receipt-output", required=True, help="Run receipt JSON output")
    parser.add_argument("--source-uri", action="append", required=True, help="Source URI; may be repeated")
    parser.add_argument(
        "--dataset-id",
        default="kfm:kansas_biodiversity_occurrences",
        help="Stable dataset identifier",
    )
    parser.add_argument(
        "--license",
        default="CC0/CC-BY-4.0",
        help="Dataset-level license summary",
    )
    parser.add_argument(
        "--attribution",
        default="Kansas biodiversity occurrences via GBIF/DwC-A",
        help="Dataset-level attribution summary",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()

    input_path = Path(args.input)
    dataset_root = Path(args.dataset_root)
    metadata_path = Path(args.metadata_output)
    evidence_path = Path(args.evidence_output)
    receipt_path = Path(args.receipt_output)

    records = read_jsonl(input_path)

    if not records:
        raise SystemExit("no_records")

    spec_hash = dataset_spec_hash(records)
    generated_at = utc_now()

    written_files = write_partitioned_parquet(records, dataset_root)

    if not written_files:
        raise SystemExit("no_parquet_files_written")

    metadata = build_metadata(
        dataset_id=args.dataset_id,
        spec_hash=spec_hash,
        records=records,
        written_files=written_files,
        generated_at=generated_at,
    )

    evidence_bundle = build_evidence_bundle(
        spec_hash=spec_hash,
        dataset_id=args.dataset_id,
        records=records,
        source_uris=args.source_uri,
        generated_at=generated_at,
        license_label=args.license,
        attribution=args.attribution,
    )

    receipt = build_receipt(
        dataset_root=dataset_root,
        metadata_path=metadata_path,
        evidence_path=evidence_path,
        spec_hash=spec_hash,
        records=records,
        written_files=written_files,
        generated_at=generated_at,
    )

    write_json(metadata_path, metadata)
    write_json(evidence_path, evidence_bundle)
    write_json(receipt_path, receipt)

    print(json.dumps(receipt, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Makefile target

```makefile
publish:
	python publish/publish.py \
		--input $(DEDUPED) \
		--dataset-root $(DATASET_ROOT) \
		--metadata-output $(METADATA) \
		--evidence-output $(EVIDENCE) \
		--receipt-output $(RECEIPT) \
		--source-uri "https://api.gbif.org/v1/occurrence/search?stateProvince=Kansas"
```
