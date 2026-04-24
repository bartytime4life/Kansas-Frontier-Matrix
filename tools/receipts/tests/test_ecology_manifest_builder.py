```python
from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.receipts.ecology_manifest_builder import (
    build_manifest,
    write_manifest,
)


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def validator_receipt(
    *,
    decision: str = "pass",
    spec_hash: str = SPEC_HASH,
) -> dict:
    return {
        "receipt_type": "validator_result",
        "validator": "tools/validators/ecology_index",
        "schema_ref": "schemas/ecology/kfm_eco_index.schema.json",
        "input_ref": "candidate.json",
        "decision": decision,
        "errors": [],
        "warnings": [],
        "spec_hash": spec_hash,
        "generated_at": "2026-04-24T00:00:00Z",
    }


def test_build_manifest_ready_for_promotion(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipt.json"
    write_json(receipt_path, validator_receipt())

    manifest = build_manifest(
        candidate_id="eco_index.example",
        candidate_type="eco_index",
        spec_hash=SPEC_HASH,
        receipt_paths=[receipt_path],
    )

    assert manifest["manifest_id"] == "kfm.receipt_manifest.ecology.eco_index.example"
    assert manifest["candidate_id"] == "eco_index.example"
    assert manifest["candidate_type"] == "eco_index"
    assert manifest["spec_hash"] == SPEC_HASH
    assert manifest["decision"] == "ready_for_promotion"
    assert len(manifest["receipts"]) == 1


def test_failed_receipt_blocks_promotion(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipt.json"
    write_json(receipt_path, validator_receipt(decision="fail"))

    manifest = build_manifest(
        candidate_id="eco_index.example",
        candidate_type="eco_index",
        spec_hash=SPEC_HASH,
        receipt_paths=[receipt_path],
    )

    assert manifest["decision"] == "not_ready"


def test_mismatched_spec_hash_blocks_promotion(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipt.json"
    write_json(
        receipt_path,
        validator_receipt(
            spec_hash="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        ),
    )

    manifest = build_manifest(
        candidate_id="eco_index.example",
        candidate_type="eco_index",
        spec_hash=SPEC_HASH,
        receipt_paths=[receipt_path],
    )

    assert manifest["decision"] == "not_ready"


def test_unknown_receipt_decision_holds_manifest(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipt.json"
    write_json(receipt_path, validator_receipt(decision="needs_human"))

    manifest = build_manifest(
        candidate_id="eco_index.example",
        candidate_type="eco_index",
        spec_hash=SPEC_HASH,
        receipt_paths=[receipt_path],
    )

    assert manifest["decision"] == "hold"


def test_empty_receipt_list_not_ready() -> None:
    manifest = build_manifest(
        candidate_id="eco_index.example",
        candidate_type="eco_index",
        spec_hash=SPEC_HASH,
        receipt_paths=[],
    )

    assert manifest["decision"] == "not_ready"
    assert manifest["receipts"] == []


def test_non_object_receipt_raises(tmp_path: Path) -> None:
    receipt_path = tmp_path / "receipt.json"
    write_json(receipt_path, [])

    with pytest.raises(ValueError, match="Receipt must be a JSON object"):
        build_manifest(
            candidate_id="eco_index.example",
            candidate_type="eco_index",
            spec_hash=SPEC_HASH,
            receipt_paths=[receipt_path],
        )


def test_write_manifest_creates_parent_directory(tmp_path: Path) -> None:
    manifest_path = tmp_path / "nested" / "manifest.json"

    manifest = {
        "manifest_id": "kfm.receipt_manifest.ecology.eco_index.example",
        "candidate_id": "eco_index.example",
        "candidate_type": "eco_index",
        "spec_hash": SPEC_HASH,
        "receipts": [],
        "decision": "not_ready",
        "generated_at": "2026-04-24T00:00:00Z",
    }

    write_manifest(manifest_path, manifest)

    assert manifest_path.exists()
    written = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert written["decision"] == "not_ready"
```
