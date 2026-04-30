from __future__ import annotations

import json
from pathlib import Path


FIXTURE_DIR = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURE_DIR / name).read_text(encoding="utf-8"))


def test_evidence_ref_fixture_marks_resolved_bundle() -> None:
    evidence_ref = load_fixture("evidence_ref.valid.json")

    assert evidence_ref["object_type"] == "EvidenceRef"
    assert evidence_ref["resolved"] is True
    assert evidence_ref["bundle_id"].startswith("kfm://evidence/")


def test_evidence_ref_missing_bundle_fixture_is_invalid_for_resolution() -> None:
    evidence_ref = load_fixture("evidence_ref.missing_bundle.invalid.json")

    assert evidence_ref["object_type"] == "EvidenceRef"
    assert evidence_ref["resolved"] is False
    assert "bundle_id" not in evidence_ref
