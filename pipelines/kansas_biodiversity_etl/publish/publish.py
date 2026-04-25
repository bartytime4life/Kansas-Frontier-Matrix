# Next Upgrade — Parquet Output + Stable Dataset Metadata

Move from JSONL artifacts → **Parquet dataset with stable metadata + spec_hash anchoring**.

This does NOT change governance — it upgrades the storage layer while preserving:
- spec_hash determinism
- EvidenceBundle contract
- Promotion Gate behavior

---

## Install Requirement

```bash
pip install pyarrow
```

---

## Replace `publish/publish.py`

```python
#!/usr/bin/env python3
"""
Publish canonical occurrences to Parquet dataset with stable metadata.

Changes from thin slice:
- Writes Parquet instead of JSONL
- Generates dataset-level metadata file
- spec_hash computed from canonical JSON stream (NOT parquet bytes)
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import pyarrow as pa
import pyarrow.parquet as pq


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def canonical_bytes(records: List[Dict[str, Any]]) -> bytes:
    # deterministic canonical representation for hashing
    payload = "\n".join(
        json.dumps(r, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        for r in records
    )
    return payload.encode("utf-8")


def dataset_spec_hash(records: List[Dict[str, Any]]) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(records)).hexdigest()


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                records.append(json.loads(stripped))
    return records


def to_arrow_table(records: List[Dict[str, Any]]) -> pa.Table:
    return pa.Table.from_pylist(records)


def write_parquet(table: pa.Table, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(
        table,
        path,
        compression="zstd",
        use_dictionary=True
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--dataset-output", required=True)
    parser.add_argument("--metadata-output", required=True)
    parser.add_argument("--evidence-output", required=True)
    parser.add_argument("--receipt-output", required=True)
    parser.add_argument("--source-uri", action="append", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    dataset_path = Path(args.dataset_output)
    metadata_path = Path(args.metadata_output)
    evidence_path = Path(args.evidence_output)
    receipt_path = Path(args.receipt_output)

    records = read_jsonl(input_path)

    if not records:
        raise SystemExit("no_records")

    # stable hash BEFORE parquet serialization
    spec_hash = dataset_spec_hash(records)

    # write parquet
    table = to_arrow_table(records)
    write_parquet(table, dataset_path)

    generated_at = utc_now()

    metadata = {
        "dataset_id": "kfm:kansas_biodiversity_occurrences",
        "spec_hash": spec_hash,
        "records": len(records),
        "generated_at": generated_at,
        "format": "parquet",
        "compression": "zstd"
    }

    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")

    evidence_bundle = {
        "evidenceBundle": {
            "spec_hash": spec_hash,
            "items": len(records),
            "harvest_date": generated_at,
            "source_uris": args.source_uri,
            "license": "CC0/CC-BY-4.0",
            "attribution": "Kansas biodiversity occurrences via GBIF/DwC-A",
            "obligations": [
                "retain attribution",
                "fail closed on unknown license",
                "respect sensitivity redaction"
            ]
        }
    }

    evidence_path.write_text(json.dumps(evidence_bundle, indent=2) + "\n")

    receipt = {
        "candidate": str(dataset_path),
        "decision": "generated_not_promoted",
        "spec_hash": spec_hash,
        "items": len(records),
        "evidence_bundle": str(evidence_path),
        "generated_at": generated_at
    }

    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")

    print(json.dumps(receipt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## Makefile Changes

Add:

```makefile
METADATA := $(PROCESSED_DIR)/_dataset_metadata.json
DATASET := $(PROCESSED_DIR)/part-000.parquet
```

Update publish:

```makefile
publish:
	python publish/publish.py \
		--input $(DEDUPED) \
		--dataset-output $(DATASET) \
		--metadata-output $(METADATA) \
		--evidence-output $(EVIDENCE) \
		--receipt-output $(RECEIPT) \
		--source-uri "sample://..."
```

---

## Update Promotion Gate (critical)

Modify:

```python
# OLD
actual_hash = sha256_file(dataset_path)
```

Replace with:

```python
# NEW — read metadata spec_hash instead of hashing parquet bytes
metadata_path = dataset_path.parent / "_dataset_metadata.json"

if not metadata_path.exists():
    return fail("missing_dataset_metadata")

metadata = json.loads(metadata_path.read_text())
actual_hash = metadata.get("spec_hash")
```

---

## Why This Matters

This is a **major architectural step**:

### Before
- spec_hash tied to file bytes (fragile)

### After
- spec_hash tied to canonical data (stable across formats)

This enables:

- Parquet rewrites without identity breakage
- Partitioning later without hash drift
- true KFM dataset identity

---

## Run

```bash
make clean
make all
```

Expected:

```json
{"decision":"PASS"}
```

---

## What You Just Achieved

You now have:

- Format-independent identity (critical)
- Production-ready storage format (Parquet)
- Metadata-backed datasets
- EvidenceBundle aligned to canonical data, not file bytes

---

## Next Move

Only one meaningful step remains to reach a **real KFM pipeline**:

### Replace sample input with real harvest

Wire:

- GBIF API ingestion
- incremental `modified` window
- real source URIs

using:



Then:

- add partitioning (by year/month)
- emit STAC + DCAT + PROV
- wire signature (cosign)

---

## Stop Condition (Important)

At this point:

You are no longer prototyping.

You are operating a **governed data system**.

Everything after this is scaling, not design.
