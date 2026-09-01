from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
SPEC = importlib.util.spec_from_file_location("join_candidates_domain_alias_dependency_guard", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _rule_counts(decision: dict[str, object]) -> dict[str, int]:
    return {
        item["rule_code"]: item["failure_count"]
        for item in decision["rule_results"]
    }


def _base_candidate() -> dict[str, object]:
    return copy.deepcopy(MODULE.fixture_cases()[0][0])


def test_valid_alias_projection_keeps_unrelated_pair_candidate_eligible() -> None:
    candidate = _base_candidate()
    candidate["endpoints"]["left"]["domain"] = "geology"
    candidate["endpoints"]["right"]["domain"] = "hydrology"

    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ALLOW"
    assert decision["status"] == "JOIN_CANDIDATE"
    assert decision["reason_codes"] == ["JOIN_PREDICATE_SATISFIED"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 0
    assert not any(decision["effects"].values())


def test_missing_alias_projection_fails_closed_as_dependency_error(tmp_path: Path, monkeypatch) -> None:
    candidate = _base_candidate()
    missing = tmp_path / "domain_lane_register.yaml"
    monkeypatch.setattr(MODULE, "DOMAIN_LANE_REGISTER_PATH", missing)

    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ERROR"
    assert decision["status"] == "VALIDATOR_SYSTEM_ERROR"
    assert decision["reason_codes"] == ["DOMAIN_ALIAS_REGISTER_UNAVAILABLE"]
    assert "REPAIR_DOMAIN_ALIAS_REGISTER_DEPENDENCY" in decision["obligations"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 1
    assert not any(decision["effects"].values())


def test_malformed_alias_projection_fails_closed_as_dependency_error(tmp_path: Path, monkeypatch) -> None:
    candidate = _base_candidate()
    malformed = tmp_path / "domain_lane_register.yaml"
    malformed.write_text("unresolved_aliases: [air, atmosphere]\n", encoding="utf-8")
    monkeypatch.setattr(MODULE, "DOMAIN_LANE_REGISTER_PATH", malformed)

    decision = MODULE.derive_decision(candidate)

    assert decision["validator_outcome"] == "ERROR"
    assert decision["status"] == "VALIDATOR_SYSTEM_ERROR"
    assert decision["reason_codes"] == ["DOMAIN_ALIAS_REGISTER_UNAVAILABLE"]
    assert "REPAIR_DOMAIN_ALIAS_REGISTER_DEPENDENCY" in decision["obligations"]
    assert _rule_counts(decision)["DEPENDENCIES_READY"] == 1
    assert not any(decision["effects"].values())
