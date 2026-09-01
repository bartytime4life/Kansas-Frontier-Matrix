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


def _candidate(left_domain: str, right_domain: str):
    value = copy.deepcopy(MODULE.fixture_cases()[0][0])
    value["endpoints"]["left"]["domain"] = left_domain
    value["endpoints"]["right"]["domain"] = right_domain
    return MODULE.seal(MODULE.derive_outputs(value))


def test_unresolved_alias_pair_abstains_without_normalizing_domain_identity() -> None:
    candidate = _candidate("air", "atmosphere")
    assert MODULE.validate_document(candidate).coherent

    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ABSTAIN"
    assert decision["status"] == "NO_JOIN_CANDIDATE"
    assert decision["matched"] is False
    assert decision["reason_codes"] == ["DOMAIN_ALIAS_REVIEW_REQUIRED"]
    assert "ROUTE_TO_DOMAIN_ALIAS_REVIEW" in decision["obligations"]
    assert candidate["endpoints"]["left"]["domain"] == "air"
    assert candidate["endpoints"]["right"]["domain"] == "atmosphere"
    rules = {item["rule_code"]: item["failure_count"] for item in decision["rule_results"]}
    assert rules["JOIN_PREDICATE_MATCHED"] == 1


def test_all_current_unresolved_aliases_route_to_review() -> None:
    aliases = MODULE._unresolved_domain_aliases()
    assert aliases == {
        "air": "atmosphere",
        "settlement": "settlements-infrastructure",
        "transport": "roads-rail-trade",
    }
    for alias, target in aliases.items():
        candidate = _candidate(alias, target)
        decision = candidate["decision"]
        assert decision["validator_outcome"] == "ABSTAIN"
        assert decision["reason_codes"] == ["DOMAIN_ALIAS_REVIEW_REQUIRED"]
        assert "ROUTE_TO_DOMAIN_ALIAS_REVIEW" in decision["obligations"]
        assert not any(decision["effects"].values())


def test_distinct_non_alias_domains_remain_candidate_eligible() -> None:
    candidate = _candidate("fixture-left", "fixture-right")
    assert MODULE.validate_document(candidate).coherent
    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ALLOW"
    assert decision["status"] == "JOIN_CANDIDATE"
    assert decision["matched"] is True


def test_exact_same_domain_keeps_domain_local_routing_precedence() -> None:
    candidate = _candidate("air", "air")
    assert MODULE.validate_document(candidate).coherent
    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ABSTAIN"
    assert decision["reason_codes"] == ["CROSS_DOMAIN_PAIR_REQUIRED"]
    assert "ROUTE_TO_DOMAIN_LOCAL_VALIDATOR" in decision["obligations"]
