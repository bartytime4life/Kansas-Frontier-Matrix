from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO_ROOT / "tools/validators/governance/validate_coverage_priority_scorecard.py"
SPEC = importlib.util.spec_from_file_location("coverage_priority_scorecard_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads((REPO_ROOT / "schemas/contracts/v1/governance/coverage_priority_scorecard.schema.json").read_text())
    Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_exact_expected_size_and_polarity() -> None:
    assert len(MODULE.fixture_cases()) == 14
    assert MODULE.fixture_profile() == 0


def test_density_and_gap_profiles_produce_inspectable_rank_flip() -> None:
    candidate, result, _, _ = MODULE.fixture_cases()[0]
    assert result.outcome == "HOLD"
    density_order = [entry["area_ref"] for entry in candidate["rankings"][0]["entries"]]
    gap_order = [entry["area_ref"] for entry in candidate["rankings"][1]["entries"]]
    assert density_order != gap_order
    assert candidate["stability"] == {
        "compared_profile_ids": ["DENSITY_LED", "GAP_LED"],
        "rank_correlation_milli": -1000,
        "rank_flip_count": 2,
        "stable": False,
        "counterfactual_status": "RANKING_CHANGED",
    }


def test_cost_components_are_subtracted_and_all_components_visible() -> None:
    candidate = MODULE.fixture_cases()[0][0]
    entry = candidate["rankings"][0]["entries"][0]
    assert set(entry["component_scores"]) == set(MODULE.METRICS)
    assert entry["component_scores"]["sensitivity_burden"] < 0
    assert entry["component_scores"]["review_cost"] < 0


def test_missingness_and_source_cap_produce_coherent_abstention() -> None:
    missing_candidate, missing_result, _, _ = MODULE.fixture_cases()[2]
    assert missing_result.outcome == "HOLD"
    assert missing_candidate["decision"]["outcome"] == "ABSTAIN"
    cap_candidate, cap_result, _, _ = MODULE.fixture_cases()[3]
    assert cap_result.outcome == "HOLD"
    assert cap_candidate["decision"]["outcome"] == "ABSTAIN"
    assert any(entry["source_role_cap_exceeded"] for ranking in cap_candidate["rankings"] for entry in ranking["entries"])


def test_score_and_stability_tamper_are_rejected() -> None:
    cases = MODULE.fixture_cases()
    score_codes = {finding.code for finding in cases[4][1].findings}
    stability_codes = {finding.code for finding in cases[5][1].findings}
    assert "RANKING_DERIVATION_MISMATCH" in score_codes
    assert "STABILITY_DERIVATION_MISMATCH" in stability_codes


def test_identity_is_deterministic_and_tamper_evident() -> None:
    first = MODULE.fixture_cases()[0][0]
    second = MODULE.seal(first)
    assert first["spec_hash"] == second["spec_hash"]
    assert first["scorecard_id"] == second["scorecard_id"]
    tamper_codes = {finding.code for finding in MODULE.fixture_cases()[11][1].findings}
    assert {"SPEC_HASH_MISMATCH", "SCORECARD_ID_MISMATCH"} <= tamper_codes


def test_duplicate_keys_and_symlinks_are_denied_without_echoing_values(tmp_path: Path) -> None:
    sentinel = "SENSITIVE_SENTINEL_DO_NOT_ECHO"
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text('{"profile":"%s","profile":"other"}' % sentinel)
    result = MODULE.validate_file(duplicate)
    assert result.outcome == "DENY"
    assert {finding.code for finding in result.findings} == {"INPUT_JSON_INVALID"}
    assert sentinel not in repr(result)

    target = tmp_path / "target.json"
    target.write_text("{}")
    link = tmp_path / "link.json"
    try:
        os.symlink(target, link)
    except (OSError, NotImplementedError):
        return
    assert {finding.code for finding in MODULE.validate_file(link).findings} == {"INPUT_JSON_INVALID"}


def test_validator_has_no_network_client_imports() -> None:
    source = MODULE_PATH.read_text(encoding="utf-8")
    forbidden = ("import requests", "import urllib", "import socket", "httpx", "aiohttp", "boto3")
    assert not any(token in source for token in forbidden)
