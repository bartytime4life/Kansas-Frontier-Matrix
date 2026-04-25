Replace:

```text
pipelines/kansas_biodiversity_etl/validate/promotion_gate_full.py
```

with:

```python
#!/usr/bin/env python3
"""
Full Promotion Gate (A-G) for Kansas Biodiversity ETL.

Supports:
- JSONL thin-slice artifacts
- Parquet dataset artifacts
- format-independent spec_hash via _dataset_metadata.json

Gate Checks:

A. EvidenceBundle present and valid JSON
B. Dataset exists
C. Dataset metadata exists when validating Parquet
D. EvidenceBundle spec_hash matches dataset metadata spec_hash
E. License validity
F. Attribution completeness
G. Sensitivity enforcement

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


def fail(reason: str) -> int:
    print(json.dumps({"decision": "FAIL", "reason": reason}, sort_keys=True))
    return 1


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                records.append(json.loads(stripped))
    return records


def read_parquet(path: Path) -> List[Dict[str, Any]]:
    if pq is None:
        raise RuntimeError("pyarrow_missing_for_parquet_validation")

    table = pq.read_table(path)
    return table.to_pylist()


def read_dataset_records(dataset_path: Path) -> List[Dict[str, Any]]:
    suffix = dataset_path.suffix.lower()

    if suffix == ".jsonl":
        return read_jsonl(dataset_path)

    if suffix == ".parquet":
        return read_parquet(dataset_path)

    raise RuntimeError(f"unsupported_dataset_format:{suffix}")


def expected_spec_hash(dataset_path: Path, metadata_path: Optional[Path]) -> str:
    suffix = dataset_path.suffix.lower()

    if suffix == ".jsonl":
        return sha256_file(dataset_path)

    if suffix == ".parquet":
        if metadata_path is None:
            metadata_path = dataset_path.parent / "_dataset_metadata.json"

        if not metadata_path.exists():
            raise RuntimeError("missing_dataset_metadata")

        try:
            metadata = load_json(metadata_path)
        except Exception as exc:
            raise RuntimeError("invalid_dataset_metadata_json") from exc

        spec_hash = metadata.get("spec_hash")
        if not spec_hash:
            raise RuntimeError("metadata_missing_spec_hash")

        return str(spec_hash)

    raise RuntimeError(f"unsupported_dataset_format:{suffix}")


def primary_key(record: Dict[str, Any]) -> str:
    return f"{record.get('institution_code')}|{record.get('id')}"


def validate_record_level_rules(records: Iterable[Dict[str, Any]]) -> Optional[str]:
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument(
        "--metadata",
        default=None,
        help="Optional metadata path. Required for explicit Parquet metadata validation; defaults to dataset parent.",
    )
    args = parser.parse_args()

    dataset_path = Path(args.dataset)
    evidence_path = Path(args.evidence)
    metadata_path = Path(args.metadata) if args.metadata else None

    # Gate B: dataset exists
    if not dataset_path.exists():
        return fail("dataset_missing")

    # Gate A: evidence exists and is valid
    if not evidence_path.exists():
        return fail("evidencebundle_missing")

    try:
        evidence_doc = load_json(evidence_path)
        bundle = evidence_doc["evidenceBundle"]
    except Exception:
        return fail("invalid_evidencebundle_json")

    # Gate C/D: spec_hash must match expected identity source.
    try:
        actual_hash = expected_spec_hash(dataset_path, metadata_path)
    except RuntimeError as exc:
        return fail(str(exc))

    evidence_hash = bundle.get("spec_hash")
    if not evidence_hash:
        return fail("evidencebundle_missing_spec_hash")

    if evidence_hash != actual_hash:
        return fail("spec_hash_mismatch")

    # EvidenceBundle completeness.
    if int(bundle.get("items", 0)) <= 0:
        return fail("empty_evidencebundle_items")

    if not bundle.get("source_uris"):
        return fail("missing_source_uris")

    if not bundle.get("license"):
        return fail("missing_evidencebundle_license")

    if not bundle.get("attribution"):
        return fail("missing_evidencebundle_attribution")

    # Load dataset for record-level checks.
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

    record_error = validate_record_level_rules(records)
    if record_error:
        return fail(record_error)

    print(
        json.dumps(
            {
                "decision": "PASS",
                "dataset": str(dataset_path),
                "evidence": str(evidence_path),
                "records": len(records),
                "spec_hash": actual_hash,
                "gates": ["A", "B", "C", "D", "E", "F", "G"],
            },
            sort_keys=True,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## Makefile Update

For Parquet mode, use:

```makefile
gate:
	python validate/promotion_gate_full.py \
		--dataset $(DATASET) \
		--evidence $(EVIDENCE) \
		--metadata $(METADATA)
```

For JSONL thin-slice mode, this still works:

```makefile
gate:
	python validate/promotion_gate_full.py \
		--dataset $(DATASET) \
		--evidence $(EVIDENCE)
```

---

## Verification Run

```bash
make clean
make all
```

Expected:

```json
{"decision":"PASS"}
```
