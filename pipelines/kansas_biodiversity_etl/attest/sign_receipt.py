```text
pipelines/kansas_biodiversity_etl/attest/sign_receipt.py
```

This creates a lightweight local proof file for the ETL run receipt.

> This is not a replacement for cosign/DSSE. It is a repo-local proof shim so the pipeline can enforce “receipt exists + proof matches receipt” before full attestation tooling is wired.

---

## `pipelines/kansas_biodiversity_etl/attest/sign_receipt.py`

```python
#!/usr/bin/env python3
"""
Create a deterministic proof file for a Kansas Biodiversity ETL run receipt.

Input:
- run_receipt.json

Output:
- receipt_proof.json

Purpose:
- bind the receipt path, receipt hash, generated time, and declared signer
- provide a machine-checkable proof artifact before cosign/DSSE is wired

NOTE:
This is a local proof shim. Full KFM attestation should replace or wrap this
with cosign/DSSE once available.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--proof-output", required=True)
    parser.add_argument("--signer", default="@bartytime4life")
    args = parser.parse_args()

    receipt_path = Path(args.receipt)
    proof_path = Path(args.proof_output)

    if not receipt_path.exists():
        raise SystemExit("receipt_missing")

    proof = {
        "proof_type": "kfm.local_receipt_hash_proof.v1",
        "receipt": str(receipt_path),
        "receipt_hash": sha256_file(receipt_path),
        "signed_at": utc_now(),
        "signer": args.signer,
        "attestation_verified": False,
        "notes": [
            "Local deterministic receipt proof.",
            "Replace or wrap with cosign/DSSE for release-grade attestation.",
        ],
    }

    write_json(proof_path, proof)

    print(json.dumps({"decision": "PROOF_WRITTEN", "proof": str(proof_path)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## Add Proof Verification to the Gate

Create:

```text
pipelines/kansas_biodiversity_etl/attest/verify_receipt_proof.py
```

```python
#!/usr/bin/env python3
"""
Verify local receipt proof for Kansas Biodiversity ETL.

Checks:
- receipt exists
- proof exists
- proof receipt_hash matches current receipt bytes
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def fail(reason: str) -> int:
    print(json.dumps({"decision": "FAIL", "reason": reason}, sort_keys=True))
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--proof", required=True)
    args = parser.parse_args()

    receipt_path = Path(args.receipt)
    proof_path = Path(args.proof)

    if not receipt_path.exists():
        return fail("receipt_missing")

    if not proof_path.exists():
        return fail("proof_missing")

    try:
        proof = json.loads(proof_path.read_text(encoding="utf-8"))
    except Exception:
        return fail("invalid_proof_json")

    expected = proof.get("receipt_hash")
    actual = sha256_file(receipt_path)

    if expected != actual:
        return fail("receipt_proof_hash_mismatch")

    print(
        json.dumps(
            {
                "decision": "PASS",
                "receipt": str(receipt_path),
                "proof": str(proof_path),
                "receipt_hash": actual,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## Makefile Additions

Add:

```makefile
PROOF := $(PROOFS_DIR)/receipt_proof.json
```

Update `.PHONY`:

```makefile
.PHONY: all harvest normalize dedupe publish sign verify-proof gate clean sample catalog
```

Change:

```makefile
all: harvest normalize dedupe publish gate catalog
```

to:

```makefile
all: harvest normalize dedupe publish sign verify-proof gate catalog
```

Add:

```makefile
sign:
	@echo "=== Sign Receipt: Local Proof Shim ==="
	python attest/sign_receipt.py \
		--receipt $(RECEIPT) \
		--proof-output $(PROOF) \
		--signer "@bartytime4life"

verify-proof:
	@echo "=== Verify Receipt Proof ==="
	python attest/verify_receipt_proof.py \
		--receipt $(RECEIPT) \
		--proof $(PROOF)
```

---

## Updated Pipeline Order

```text
harvest
normalize
dedupe
publish
sign
verify-proof
gate
catalog
```

---

## Output Path

```text
data/proofs/kansas_biodiversity_etl/20260425/receipt_proof.json
```

---

## Run

```bash
make clean
make all
```

Expected proof result:

```json
{"decision":"PASS"}
```
