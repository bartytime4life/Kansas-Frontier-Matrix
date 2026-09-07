from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
SPEC = importlib.util.spec_from_file_location("join_candidates_temporal_boundary", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _spatial_candidate() -> dict:
    return copy.deepcopy(MODULE.fixture_cases()[1][0])


def _rederive_and_seal(candidate: dict) -> dict:
    return MODULE.seal(MODULE.derive_outputs(candidate))


def test_real_temporal_overlap_remains_candidate_eligible() -> None:
    candidate = _rederive_and_seal(_spatial_candidate())
    assert MODULE.validate_document(candidate).coherent
    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ALLOW"
    assert decision["status"] == "JOIN_CANDIDATE"
    assert decision["matched"] is True


def test_zero_tolerance_boundary_touch_abstains_without_inventing_inclusivity() -> None:
    candidate = _spatial_candidate()
    candidate["request"]["temporal_tolerance_seconds"] = 0
    candidate["endpoints"]["left"]["valid_to"] = candidate["endpoints"]["right"]["valid_from"]
    candidate = _rederive_and_seal(candidate)

    assert MODULE.validate_document(candidate).coherent
    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ABSTAIN"
    assert decision["status"] == "NO_JOIN_CANDIDATE"
    assert decision["matched"] is False
    assert decision["reason_codes"] == ["TEMPORAL_BOUNDARY_AMBIGUOUS"]
    assert "ROUTE_TO_PAIR_TEMPORAL_SEMANTICS" in decision["obligations"]
    rules = {item["rule_code"]: item["failure_count"] for item in decision["rule_results"]}
    assert rules["JOIN_PREDICATE_MATCHED"] == 1


def test_positive_tolerance_is_an_explicit_bounded_comparison() -> None:
    candidate = _spatial_candidate()
    candidate["request"]["temporal_tolerance_seconds"] = 1
    candidate["endpoints"]["left"]["valid_to"] = "2026-07-14T23:59:59Z"
    candidate = _rederive_and_seal(candidate)

    assert MODULE.validate_document(candidate).coherent
    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ALLOW"
    assert decision["status"] == "JOIN_CANDIDATE"
    assert decision["matched"] is True

def _upper_datetime_bound_candidate(*, within_tolerance: bool) -> dict:
    candidate = _spatial_candidate()
    candidate["request"]["temporal_tolerance_seconds"] = 86_400
    candidate["endpoints"]["left"]["valid_from"] = "9999-12-30T00:00:00Z"
    candidate["endpoints"]["left"]["valid_to"] = "9999-12-30T12:00:00Z"
    candidate["endpoints"]["right"]["valid_from"] = (
        "9999-12-31T12:00:00Z"
        if within_tolerance
        else "9999-12-31T12:00:01Z"
    )
    candidate["endpoints"]["right"]["valid_to"] = "9999-12-31T23:59:59Z"
    candidate["evaluated_at"] = "9999-12-31T23:59:59Z"
    return _rederive_and_seal(candidate)


def test_maximum_year_gap_at_tolerance_remains_candidate_eligible() -> None:
    candidate = _upper_datetime_bound_candidate(within_tolerance=True)

    assert MODULE.validate_document(candidate).coherent
    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ALLOW"
    assert decision["status"] == "JOIN_CANDIDATE"
    assert decision["matched"] is True


def test_maximum_year_gap_beyond_tolerance_abstains_without_overflow() -> None:
    candidate = _upper_datetime_bound_candidate(within_tolerance=False)

    assert MODULE.validate_document(candidate).coherent
    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ABSTAIN"
    assert decision["status"] == "NO_JOIN_CANDIDATE"
    assert decision["reason_codes"] == ["JOIN_PREDICATE_NOT_SATISFIED"]
    assert decision["matched"] is False
