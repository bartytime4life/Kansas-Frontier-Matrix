```python
from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.validators.promotion_gate.ecology_manifest import (
    decision_to_dict,
    evaluate_ecology_receipt_manifest,
    load_manifest,
)


SPEC_HASH = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def manifest(*, decision: str = "ready_for_promotion") -> dict:
    return {
        "manifest_id": "kfm.receipt_manifest.ecology.eco_index.example",
        "candidate_id": "eco_index.example",
        "candidate_type": "eco_index",
        "spec_hash": SPEC_HASH,
        "receipts": [
            {
                "receipt_type": "validator_result",
                "validator": "tools/validators/ecology_index",
                "receipt_ref": "data/receipts/ecology/index/example.validator_receipt.json",
                "decision": "pass",
                "spec_hash": SPEC_HASH,
                "generated_at": "2026-04-24T00:00:00Z",
            }
        ],
        "decision": decision,
        "generated_at": "2026-04-24T00:00:00Z",
    }


def test_ready_manifest_passes_promotion_gate(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="ready_for_promotion"))

    result = evaluate_ecology_receipt_manifest(manifest_path)

    assert result.ok
    assert result.gate == "ecology_receipt_manifest"
    assert result.decision == "pass"
    assert result.candidate_id == "eco_index.example"
    assert result.spec_hash == SPEC_HASH
    assert result.errors == []
    assert result.warnings == []


def test_proof_complete_manifest_passes_promotion_gate(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="proof_complete"))

    result = evaluate_ecology_receipt_manifest(manifest_path)

    assert result.ok
    assert result.decision == "pass"


def test_hold_manifest_returns_hold(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="hold"))

    result = evaluate_ecology_receipt_manifest(manifest_path)

    assert not result.ok
    assert result.decision == "hold"
    assert result.errors == []
    assert result.warnings == ["manifest decision requires review: hold"]


def test_proof_required_manifest_returns_hold(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="proof_required"))

    result = evaluate_ecology_receipt_manifest(manifest_path)

    assert not result.ok
    assert result.decision == "hold"
    assert result.warnings == ["manifest decision requires review: proof_required"]


def test_not_ready_manifest_fails(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="not_ready"))

    result = evaluate_ecology_receipt_manifest(manifest_path)

    assert not result.ok
    assert result.decision == "fail"
    assert result.errors == ["manifest decision blocks promotion: not_ready"]


def test_quarantine_manifest_fails(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="quarantine"))

    result = evaluate_ecology_receipt_manifest(manifest_path)

    assert not result.ok
    assert result.decision == "fail"
    assert result.errors == ["manifest decision blocks promotion: quarantine"]


def test_unknown_manifest_decision_fails(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, manifest(decision="approved_by_vibes"))

    result = evaluate_ecology_receipt_manifest(manifest_path)

    assert not result.ok
    assert result.decision == "fail"
    assert result.errors == ["unknown manifest decision: approved_by_vibes"]


def test_missing_candidate_id_fails(tmp_path: Path) -> None:
    value = manifest()
    value.pop("candidate_id")

    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, value)

    result = evaluate_ecology_receipt_manifest(manifest_path)

    assert not result.ok
    assert result.decision == "fail"
    assert "manifest missing candidate_id" in result.errors


def test_missing_spec_hash_fails(tmp_path: Path) -> None:
    value = manifest()
    value.pop("spec_hash")

    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, value)

    result = evaluate_ecology_receipt_manifest(manifest_path)

    assert not result.ok
    assert result.decision == "fail"
    assert "manifest missing spec_hash" in result.errors


def test_non_object_manifest_raises(tmp_path: Path) -> None:
    manifest_path = tmp_path / "manifest.json"
    write_json(manifest_path, [])

    with pytest.raises(ValueError, match="Receipt manifest must be a JSON object"):
        load_manifest(manifest_path)


def test_decision_to_dict() -> None:
    value = evaluate_like = {
        "gate": "ecology_receipt_manifest",
        "decision": "pass",
        "manifest_ref": "manifest.json",
        "candidate_id": "eco_index.example",
        "spec_hash": SPEC_HASH,
        "errors": [],
        "warnings": [],
    }

    manifest_path = Path("manifest.json")
    write_value = {
        "gate": "ecology_receipt_manifest",
        "decision": "pass",
        "manifest_ref": str(manifest_path),
        "candidate_id": "eco_index.example",
        "spec_hash": SPEC_HASH,
        "errors": [],
        "warnings": [],
    }

    from tools.validators.promotion_gate.ecology_manifest import PromotionManifestDecision

    decision = PromotionManifestDecision(**write_value)

    assert decision_to_dict(decision) == value
```
