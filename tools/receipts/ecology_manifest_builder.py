from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


BLOCKING_DECISIONS = {
    "fail",
    "hold",
    "not_ready",
}


READY_DECISIONS = {
    "pass",
    "ready_for_promotion",
    "proof_complete",
}


@dataclass(frozen=True)
class ManifestReceipt:
    receipt_type: str
    receipt_ref: str
    decision: str
    generated_at: str
    validator: str | None = None
    spec_hash: str | None = None


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(value, dict):
        raise ValueError("Receipt must be a JSON object.")

    return value


def receipt_to_manifest_item(path: Path, receipt: dict[str, Any]) -> ManifestReceipt:
    return ManifestReceipt(
        receipt_type=str(receipt.get("receipt_type", "")),
        validator=receipt.get("validator"),
        receipt_ref=str(path),
        decision=str(receipt.get("decision", "")),
        spec_hash=receipt.get("spec_hash"),
        generated_at=str(receipt.get("generated_at", "")),
    )


def decide_manifest(receipts: list[ManifestReceipt], spec_hash: str) -> str:
    if not receipts:
        return "not_ready"

    for receipt in receipts:
        if receipt.decision in BLOCKING_DECISIONS:
            return "not_ready"

        if receipt.spec_hash and receipt.spec_hash != spec_hash:
            return "not_ready"

        if receipt.decision not in READY_DECISIONS:
            return "hold"

    return "ready_for_promotion"


def build_manifest(
    *,
    candidate_id: str,
    candidate_type: str,
    spec_hash: str,
    receipt_paths: list[Path],
) -> dict[str, Any]:
    manifest_receipts = [
        receipt_to_manifest_item(path, load_json(path))
        for path in receipt_paths
    ]

    decision = decide_manifest(manifest_receipts, spec_hash)

    return {
        "manifest_id": f"kfm.receipt_manifest.ecology.{candidate_id}",
        "candidate_id": candidate_id,
        "candidate_type": candidate_type,
        "spec_hash": spec_hash,
        "receipts": [
            {
                key: value
                for key, value in {
                    "receipt_type": receipt.receipt_type,
                    "validator": receipt.validator,
                    "receipt_ref": receipt.receipt_ref,
                    "decision": receipt.decision,
                    "spec_hash": receipt.spec_hash,
                    "generated_at": receipt.generated_at,
                }.items()
                if value is not None
            }
            for receipt in manifest_receipts
        ],
        "decision": decision,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def validate_manifest(
    *,
    manifest: dict[str, Any],
    schema_path: Path,
) -> list[str]:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    return [
        f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
        for error in sorted(
            validator.iter_errors(manifest),
            key=lambda item: list(item.path),
        )
    ]


def write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
