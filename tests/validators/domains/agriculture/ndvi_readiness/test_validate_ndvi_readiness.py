"""Tests for the no-network NDVI readiness sidecar validator."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[5]
MODULE_PATH = REPO_ROOT / (
    "tools/validators/domains/agriculture/ndvi_readiness/"
    "validate_ndvi_readiness.py"
)
FIXTURE_PATH = REPO_ROOT / (
    "fixtures/domains/agriculture/ndvi_readiness/valid/emit_candidate.json"
)

SPEC = importlib.util.spec_from_file_location("kfm_ndvi_readiness", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
validate_payload = MODULE.validate_payload


def _fixture() -> dict[str, object]:
    value = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_emit_candidate_is_structurally_and_semantically_valid() -> None:
    result = validate_payload(_fixture())

    assert result.ok
    assert result.findings == ()


def test_heavy_smoke_requires_hold() -> None:
    payload = _fixture()
    payload["assessment_id"] = "ndvi-readiness-heavy-smoke-hold"
    payload["critical_aoi_summary"]["heavy_smoke_overlap_count"] = 1
    payload["tile_summary"]["primary_blocker"] = "HEAVY_SMOKE_AOI"
    payload["emit_decision"] = {
        "outcome": "HOLD",
        "reasons": ["HEAVY_SMOKE_AOI"],
    }

    result = validate_payload(payload)

    assert result.ok
    assert payload["governance"]["promotion_eligible"] is False


def test_unresolved_input_receipt_requires_hold() -> None:
    payload = _fixture()
    payload["assessment_id"] = "ndvi-readiness-unresolved-receipt-hold"
    payload["inputs"][-1]["receipt_state"] = "UNRESOLVED"
    payload["tile_summary"]["primary_blocker"] = "INPUT_RECEIPT_UNRESOLVED"
    payload["emit_decision"] = {
        "outcome": "HOLD",
        "reasons": ["INPUT_RECEIPT_UNRESOLVED"],
    }

    result = validate_payload(payload)

    assert result.ok


def test_inconsistent_emit_decision_is_rejected() -> None:
    payload = _fixture()
    payload["critical_aoi_summary"]["heavy_smoke_overlap_count"] = 1

    result = validate_payload(payload)

    assert not result.ok
    assert MODULE.Finding(
        "DECISION_OUTCOME_MISMATCH", "/emit_decision/outcome"
    ) in result.findings
    assert MODULE.Finding(
        "DECISION_REASONS_MISMATCH", "/emit_decision/reasons"
    ) in result.findings


def test_readiness_level_must_match_score_ladder() -> None:
    payload = _fixture()
    payload["tile_summary"]["level"] = 2

    result = validate_payload(payload)

    assert not result.ok
    assert result.findings == (
        MODULE.Finding("READINESS_LEVEL_MISMATCH", "/tile_summary/level"),
    )


def test_missing_input_evidence_ref_fails_schema() -> None:
    payload = _fixture()
    del payload["inputs"][0]["evidence_ref"]

    result = validate_payload(payload)

    assert not result.ok
    assert any(
        finding.code == "SCHEMA_INVALID"
        and finding.path == "/inputs/0"
        for finding in result.findings
    )
