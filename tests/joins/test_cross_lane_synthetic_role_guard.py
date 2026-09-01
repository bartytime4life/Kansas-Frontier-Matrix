from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
SPEC = importlib.util.spec_from_file_location("join_candidates_source_role_guard", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _candidate(left_role: str, right_role: str) -> dict[str, object]:
    return {
        "request": {
            "predicate": "EXACT_KEY",
            "temporal_tolerance_seconds": 0,
            "dependency_state": "READY",
        },
        "endpoints": {
            "left": {
                "domain": "fixture-left",
                "join_key": "fixture-key-alpha",
                "source_role": left_role,
                "evidence_ref": "kfm:fixture:evidence:left-alpha",
                "sensitivity": "PUBLIC_SAFE",
                "living_person": False,
                "geometry_precision": "GENERALIZED",
            },
            "right": {
                "domain": "fixture-right",
                "join_key": "fixture-key-alpha",
                "source_role": right_role,
                "evidence_ref": "kfm:fixture:evidence:right-alpha",
                "sensitivity": "PUBLIC_SAFE",
                "living_person": False,
                "geometry_precision": "GENERALIZED",
            },
        },
    }


def _rules(decision: dict[str, object]) -> dict[str, int]:
    return {
        item["rule_code"]: item["failure_count"]
        for item in decision["rule_results"]  # type: ignore[index]
    }


def _assert_role_review(left_role: str, right_role: str) -> None:
    decision = MODULE.derive_decision(_candidate(left_role, right_role))

    assert decision["validator_outcome"] == "ABSTAIN"
    assert decision["status"] == "SOURCE_ROLE_REVIEW_REQUIRED"
    assert decision["reason_codes"] == ["SOURCE_ROLE_CONFLICT"]
    assert "RESOLVE_SOURCE_ROLE_COMPATIBILITY" in decision["obligations"]
    assert decision["source_roles"] == {
        "left": left_role,
        "right": right_role,
        "output_role": "CANDIDATE_RELATION",
    }
    assert _rules(decision)["SOURCE_ROLES_COMPATIBLE"] == 1


def test_equal_roles_remain_fixture_only_join_candidates() -> None:
    for role in ("SYNTHETIC", "OBSERVED", "REGULATORY", "ADMINISTRATIVE"):
        decision = MODULE.derive_decision(_candidate(role, role))

        assert decision["validator_outcome"] == "ALLOW"
        assert decision["status"] == "JOIN_CANDIDATE"
        assert decision["reason_codes"] == ["JOIN_PREDICATE_SATISFIED"]
        assert _rules(decision)["SOURCE_ROLES_COMPATIBLE"] == 0


def test_mixed_synthetic_and_non_synthetic_roles_abstain_without_role_laundering() -> None:
    for left_role, right_role in (("SYNTHETIC", "OBSERVED"), ("REGULATORY", "SYNTHETIC")):
        _assert_role_review(left_role, right_role)


def test_distinct_non_synthetic_roles_require_pair_owned_compatibility_review() -> None:
    for left_role, right_role in (
        ("OBSERVED", "REGULATORY"),
        ("REGULATORY", "ADMINISTRATIVE"),
        ("ADMINISTRATIVE", "OBSERVED"),
    ):
        _assert_role_review(left_role, right_role)
