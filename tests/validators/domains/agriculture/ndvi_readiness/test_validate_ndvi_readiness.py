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


def _codes(payload: dict[str, object]) -> set[str]:
    return {finding.code for finding in validate_payload(payload).findings}


def _hold(payload: dict[str, object], *reasons: str) -> dict[str, object]:
    """Declare the HOLD that the given reasons require, so only the rule under test can fail."""
    payload["tile_summary"]["primary_blocker"] = reasons[0]
    payload["emit_decision"] = {"outcome": "HOLD", "reasons": sorted(reasons)}
    return payload


def test_each_threshold_reason_is_derived() -> None:
    low_health = _fixture()
    low_health["tile_summary"].update(readiness_score=0.74, level=2)
    assert validate_payload(_hold(low_health, "LOW_MASK_HEALTH")).ok
    low_area = _fixture()
    low_area["tile_summary"]["fraction_ready"] = 0.69
    assert validate_payload(_hold(low_area, "LOW_READY_AREA")).ok
    # Heavy smoke is a reason only when the threshold asks for smoke-free AOIs.
    smoke_allowed = _fixture()
    smoke_allowed["thresholds"]["no_heavy_smoke_in_aois"] = False
    smoke_allowed["critical_aoi_summary"]["heavy_smoke_overlap_count"] = 3
    assert validate_payload(smoke_allowed).ok


def test_primary_blocker_must_name_a_derived_reason() -> None:
    unexpected = _fixture()
    unexpected["tile_summary"]["primary_blocker"] = "LOW_READY_AREA"
    assert _codes(unexpected) == {"PRIMARY_BLOCKER_UNEXPECTED"}
    wrong = _hold(_fixture(), "LOW_READY_AREA")
    wrong["tile_summary"]["fraction_ready"] = 0.69
    wrong["critical_aoi_summary"]["heavy_smoke_overlap_count"] = 1
    wrong["emit_decision"]["reasons"] = ["HEAVY_SMOKE_AOI", "LOW_READY_AREA"]
    assert validate_payload(wrong).ok, "either derived reason may be the primary blocker"
    wrong["tile_summary"]["primary_blocker"] = "LOW_MASK_HEALTH"
    assert _codes(wrong) == {"PRIMARY_BLOCKER_MISMATCH"}


def test_counties_and_inputs_must_be_sorted_and_unique() -> None:
    unsorted_counties = _fixture()
    unsorted_counties["county_readiness"].reverse()
    assert _codes(unsorted_counties) == {"COUNTY_READINESS_NOT_CANONICAL"}
    duplicate_county = _fixture()
    duplicate_county["county_readiness"][1]["fips"] = duplicate_county["county_readiness"][0]["fips"]
    assert _codes(duplicate_county) == {"COUNTY_READINESS_NOT_CANONICAL"}
    unsorted_inputs = _fixture()
    unsorted_inputs["inputs"].reverse()
    assert _codes(unsorted_inputs) == {"INPUTS_NOT_CANONICAL"}


def test_level_ladder_boundaries() -> None:
    for score, level in ((0.0, 0), (0.29, 0), (0.30, 1), (0.59, 1), (0.60, 2), (0.79, 2), (0.80, 3), (1.0, 3)):
        assert MODULE._readiness_level(score) == level, score


def test_unreadable_inputs_are_named_findings(tmp_path: Path) -> None:
    def codes_for(content: str | bytes) -> set[str]:
        path = tmp_path / "candidate.json"
        path.write_bytes(content.encode() if isinstance(content, str) else content)
        return {finding.code for finding in MODULE.validate_file(path).findings}

    assert codes_for('{"a": 1, "a": 2}') == {"JSON_DUPLICATE_KEY"}
    assert codes_for('{"a": NaN}') == {"JSON_NONFINITE_NUMBER"}
    assert codes_for('{"a": ') == {"JSON_INVALID"}
    assert codes_for(b'{"a": "\xff"}') == {"JSON_NOT_UTF8"}
    assert codes_for("[]") == {"ROOT_NOT_OBJECT"}
    # Excessive nesting and over-long integers used to escape as tracebacks.
    assert codes_for('{"a": ' + "[" * 100_000 + "]" * 100_000 + "}") == {"JSON_INVALID"}
    assert codes_for('{"a": ' + "9" * 5000 + "}") == {"JSON_INVALID"}
    # An overflowing float parses to infinity, which the bounded schema refuses.
    overflow = json.dumps(_fixture()).replace('"readiness_score": 0.83', '"readiness_score": 1e400')
    assert codes_for(overflow) == {"SCHEMA_INVALID"}
    assert {f.code for f in MODULE.validate_file(tmp_path / "missing.json").findings} == {"INPUT_NOT_FILE"}
    link = tmp_path / "link.json"
    link.symlink_to(FIXTURE_PATH)
    assert {f.code for f in MODULE.validate_file(link).findings} == {"INPUT_SYMLINK_DENIED"}


def test_cli_reports_findings_and_exit_code(tmp_path: Path, capsys) -> None:
    assert MODULE.main([str(FIXTURE_PATH)]) == 0
    passed = json.loads(capsys.readouterr().out)
    assert passed["ok"] is True and passed["findings"] == []
    assert set(passed["authority"].values()) == {False}
    bad = tmp_path / "bad.json"
    payload = _fixture()
    payload["tile_summary"]["level"] = 2
    bad.write_text(json.dumps(payload), encoding="utf-8")
    assert MODULE.main([str(bad)]) == 1
    assert json.loads(capsys.readouterr().out)["findings"] == [{"code": "READINESS_LEVEL_MISMATCH", "path": "/tile_summary/level"}]
