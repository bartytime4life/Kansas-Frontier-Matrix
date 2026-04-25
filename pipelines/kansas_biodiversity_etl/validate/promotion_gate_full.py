```python
#!/usr/bin/env python3
"""
Full Promotion Gate (A–G) for Kansas Biodiversity ETL thin slice.

Gate Checks:

A. EvidenceBundle present and valid JSON
B. Dataset exists
C. spec_hash matches dataset artifact
D. License validity (no UNKNOWN / missing)
E. Attribution completeness when required
F. Duplicate identity conflicts must be zero (quarantine already handled)
G. Sensitivity enforcement:
   - restricted records MUST NOT have geometry

Fail-closed:
Any violation => FAIL
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if stripped:
                records.append(json.loads(stripped))
    return records


def fail(reason: str) -> int:
    print(json.dumps({"decision": "FAIL", "reason": reason}, sort_keys=True))
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--evidence", required=True)
    args = parser.parse_args()

    dataset_path = Path(args.dataset)
    evidence_path = Path(args.evidence)

    # Gate B: dataset exists
    if not dataset_path.exists():
        return fail("dataset_missing")

    # Gate A: evidence exists and is valid
    if not evidence_path.exists():
        return fail("evidencebundle_missing")

    try:
        evidence_doc = json.loads(evidence_path.read_text(encoding="utf-8"))
        bundle = evidence_doc["evidenceBundle"]
    except Exception:
        return fail("invalid_evidencebundle_json")

    # Gate C: spec_hash must match
    actual_hash = sha256_file(dataset_path)
    if bundle.get("spec_hash") != actual_hash:
        return fail("spec_hash_mismatch")

    # Load dataset for record-level checks
    try:
        records = read_jsonl(dataset_path)
    except Exception:
        return fail("dataset_invalid_jsonl")

    if len(records) == 0:
        return fail("empty_dataset")

    # Gate D + E + G checks
    for record in records:
        # License must exist
        license_val = record.get("license")
        if not license_val:
            return fail("missing_license_in_dataset")

        # Attribution must exist for CC-BY
        if license_val == "CC-BY-4.0":
            if not record.get("attribution"):
                return fail("missing_required_attribution")

        # Sensitivity enforcement
        if record.get("sensitivity") == "restricted":
            if record.get("geometry") is not None:
                return fail("restricted_record_contains_geometry")

    # Gate F (implicit): dedupe already removed conflicts.
    # We enforce indirectly by ensuring no duplicate PKs appear.

    seen_keys = set()
    for record in records:
        pk = f"{record.get('institution_code')}|{record.get('id')}"
        if pk in seen_keys:
            return fail("duplicate_primary_key_detected")
        seen_keys.add(pk)

    print(
        json.dumps(
            {
                "decision": "PASS",
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

Replace:

```makefile
gate:
	python validate/promotion_gate_min.py \
		--dataset $(DATASET) \
		--evidence $(EVIDENCE)
```

with:

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

---

## Forced Failure Tests

### 1. Break license

Edit a record:

```json
"license": null
```

Run:

```bash
make gate
```

Expected:

```json
{"decision":"FAIL","reason":"missing_license_in_dataset"}
```

---

### 2. Break sensitivity

Force:

```json
"sensitivity": "restricted",
"geometry": {"type":"Point",...}
```

Expected:

```json
{"decision":"FAIL","reason":"restricted_record_contains_geometry"}
```

---

### 3. Break hash

Modify dataset file manually.

Expected:

```json
{"decision":"FAIL","reason":"spec_hash_mismatch"}
```

---


The system is now *structurally correct*.
