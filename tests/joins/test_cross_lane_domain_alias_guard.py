from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
SPEC = importlib.util.spec_from_file_location("join_candidates_domain_alias_guard", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _candidate(left_domain: str, right_domain: str) -> dict[str, object]:
    candidate = copy.deepcopy(MODULE.fixture_cases()[0][0])
    candidate["endpoints"]["left"]["domain"] = left_domain
    candidate["endpoints"]["right"]["domain"] = right_domain
    return candidate


def _decision(left_domain: str, right_domain: str) -> dict[str, object]:
    return MODULE.derive_decision(_candidate(left_domain, right_domain))


def _rule_counts(decision: dict[str, object]) -> dict[str, int]:
    return {
        item["rule_code"]: item["failure_count"]
        for item in decision["rule_results"]
    }


def test_declared_unresolved_aliases_are_bounded_to_current_projection() -> None:
    assert MODULE._unresolved_domain_aliases() == {
        "air": "atmosphere",
        "settlement": "settlements-infrastructure",
        "transport": "roads-rail-trade",
    }


def test_alias_and_canonical_pairs_abstain_in_both_orientations() -> None:
    for alias, canonical in MODULE._unresolved_domain_aliases().items():
        for left_domain, right_domain in ((alias, canonical), (canonical, alias)):
            decision = _decision(left_domain, right_domain)
            assert decision["validator_outcome"] == "ABSTAIN"
            assert decision["status"] == "NO_JOIN_CANDIDATE"
            assert decision["matched"] is False
            assert decision["reason_codes"] == ["DOMAIN_ALIAS_REVIEW_REQUIRED"]
            assert "ROUTE_TO_DOMAIN_ALIAS_REVIEW" in decision["obligations"]
            assert _rule_counts(decision)["JOIN_PREDICATE_MATCHED"] == 1
            assert not any(decision["effects"].values())


def test_unrelated_distinct_domains_remain_candidate_eligible() -> None:
    decision = _decision("geology", "hydrology")
    assert decision["validator_outcome"] == "ALLOW"
    assert decision["status"] == "JOIN_CANDIDATE"
    assert decision["matched"] is True
    assert decision["reason_codes"] == ["JOIN_PREDICATE_SATISFIED"]
    assert _rule_counts(decision)["JOIN_PREDICATE_MATCHED"] == 0
    assert not any(decision["effects"].values())


def test_same_domain_scope_still_routes_to_domain_local_validation() -> None:
    decision = _decision("agriculture", "agriculture")
    assert decision["validator_outcome"] == "ABSTAIN"
    assert decision["status"] == "NO_JOIN_CANDIDATE"
    assert decision["matched"] is False
    assert decision["reason_codes"] == ["CROSS_DOMAIN_PAIR_REQUIRED"]
    assert "ROUTE_TO_DOMAIN_LOCAL_VALIDATOR" in decision["obligations"]
    assert _rule_counts(decision)["JOIN_PREDICATE_MATCHED"] == 1
    assert not any(decision["effects"].values())


def test_alias_review_does_not_downgrade_dependency_error() -> None:
    candidate = _candidate("air", "atmosphere")
    candidate["request"]["dependency_state"] = "ERROR"
    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ERROR"
    assert decision["status"] == "VALIDATOR_SYSTEM_ERROR"
    assert decision["reason_codes"] == ["VALIDATOR_DEPENDENCY_ERROR"]
    assert "REPAIR_VALIDATOR_DEPENDENCY" in decision["obligations"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 1
    assert _rule_counts(decision)["JOIN_PREDICATE_MATCHED"] == 1


def test_alias_review_does_not_downgrade_living_person_denial() -> None:
    candidate = _candidate("air", "atmosphere")
    candidate["endpoints"]["left"]["living_person"] = True
    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "DENY"
    assert decision["status"] == "LIVING_PERSON_JOIN_DENIED"
    assert decision["reason_codes"] == ["LIVING_PERSON_JOIN_DENIED"]
    assert "REQUIRE_CONSENT_AND_POLICY_REVIEW" in decision["obligations"]
    assert _rule_counts(decision)["LIVING_PERSON_SAFE"] == 1
    assert _rule_counts(decision)["JOIN_PREDICATE_MATCHED"] == 1


def test_alias_review_does_not_downgrade_sensitive_geometry_denial() -> None:
    candidate = _candidate("air", "atmosphere")
    candidate["endpoints"]["left"]["sensitivity"] = "PROHIBITED"
    candidate["endpoints"]["left"]["geometry_precision"] = "EXACT"
    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "DENY"
    assert decision["status"] == "GEOMETRY_PRECISION_BLOCKED"
    assert decision["reason_codes"] == ["GEOMETRY_PRECISION_BLOCKED"]
    assert "GENERALIZE_OR_WITHHOLD_GEOMETRY" in decision["obligations"]
    assert _rule_counts(decision)["SENSITIVITY_SAFE"] >= 1
    assert _rule_counts(decision)["JOIN_PREDICATE_MATCHED"] == 1
