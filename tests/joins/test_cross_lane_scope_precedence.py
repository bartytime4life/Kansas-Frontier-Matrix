from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
SPEC = importlib.util.spec_from_file_location("join_candidates_scope_precedence", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_same_domain_scope_precedes_dependency_error() -> None:
    same_domain = copy.deepcopy(MODULE.fixture_cases()[19][0])
    same_domain["request"]["dependency_state"] = "ERROR"

    candidate = MODULE.seal(MODULE.derive_outputs(same_domain))
    result = MODULE.validate_document(candidate)
    assert result.coherent

    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ABSTAIN"
    assert decision["status"] == "NO_JOIN_CANDIDATE"
    assert decision["reason_codes"] == ["CROSS_DOMAIN_PAIR_REQUIRED"]
    assert "ROUTE_TO_DOMAIN_LOCAL_VALIDATOR" in decision["obligations"]
    rules = {item["rule_code"]: item["failure_count"] for item in decision["rule_results"]}
    assert rules["DEPENDENCIES_READY"] == 1
    assert rules["JOIN_PREDICATE_MATCHED"] == 1


def test_cross_domain_dependency_error_remains_system_error() -> None:
    cross_domain = copy.deepcopy(MODULE.fixture_cases()[0][0])
    cross_domain["request"]["dependency_state"] = "ERROR"

    candidate = MODULE.seal(MODULE.derive_outputs(cross_domain))
    result = MODULE.validate_document(candidate)
    assert result.coherent

    decision = candidate["decision"]
    assert decision["validator_outcome"] == "ERROR"
    assert decision["status"] == "VALIDATOR_SYSTEM_ERROR"
    assert decision["reason_codes"] == ["VALIDATOR_DEPENDENCY_ERROR"]
    assert "REPAIR_VALIDATOR_DEPENDENCY" in decision["obligations"]
