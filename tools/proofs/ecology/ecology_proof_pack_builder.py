from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PASSING_RECEIPT_DECISIONS = {
    "pass",
}

PROMOTABLE_MANIFEST_DECISIONS = {
    "ready_for_promotion",
    "proof_complete",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(value, dict):
        raise ValueError("Proof-pack input must be a JSON object.")

    return value


def normalize_catalog_refs(catalog_refs: dict[str, Any] | None) -> dict[str, list[str]]:
    if catalog_refs is None:
        return {
            "dcat": [],
            "stac": [],
            "prov": [],
        }

    return {
        "dcat": [str(value) for value in catalog_refs.get("dcat", [])],
        "stac": [str(value) for value in catalog_refs.get("stac", [])],
        "prov": [str(value) for value in catalog_refs.get("prov", [])],
    }


def assert_catalog_refs(catalog_refs: dict[str, list[str]]) -> None:
    if not catalog_refs["prov"]:
        raise ValueError("proof pack requires at least one PROV catalog reference")


def build_proof_pack(
    *,
    manifest: dict[str, Any],
    manifest_ref: str,
    catalog_refs: dict[str, Any] | None = None,
) -> dict[str, Any]:
    decision = str(manifest.get("decision", ""))

    if decision not in PROMOTABLE_MANIFEST_DECISIONS:
        raise ValueError(f"manifest not promotable: {decision}")

    candidate_id = manifest.get("candidate_id")
    candidate_type = manifest.get("candidate_type")
    spec_hash = manifest.get("spec_hash")
    receipts = manifest.get("receipts", [])

    if not candidate_id:
        raise ValueError("manifest missing candidate_id")

    if not candidate_type:
        raise ValueError("manifest missing candidate_type")

    if not spec_hash:
        raise ValueError("manifest missing spec_hash")

    if not isinstance(receipts, list) or not receipts:
        raise ValueError("manifest receipts must contain at least one receipt")

    for receipt in receipts:
        if not isinstance(receipt, dict):
            raise ValueError("manifest receipt entries must be JSON objects")

        receipt_decision = str(receipt.get("decision", ""))
        if receipt_decision not in PASSING_RECEIPT_DECISIONS:
            raise ValueError(f"receipt not passing: {receipt_decision}")

        receipt_spec_hash = receipt.get("spec_hash")
        if receipt_spec_hash and receipt_spec_hash != spec_hash:
            raise ValueError("receipt spec_hash mismatch")

    normalized_catalog_refs = normalize_catalog_refs(catalog_refs)
    assert_catalog_refs(normalized_catalog_refs)

    return {
        "proof_pack_id": f"kfm.proof.ecology.{candidate_id}",
        "candidate_id": candidate_id,
        "candidate_type": candidate_type,
        "spec_hash": spec_hash,
        "manifest_ref": manifest_ref,
        "receipts": receipts,
        "catalog_refs": normalized_catalog_refs,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "proof_complete",
    }


def write_proof_pack(path: Path, proof_pack: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(proof_pack, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
