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
