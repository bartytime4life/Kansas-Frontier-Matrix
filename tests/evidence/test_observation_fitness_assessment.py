from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/evidence/validate_observation_fitness_assessment.py"
SPEC = importlib.util.spec_from_file_location("observation_fitness_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads((REPO_ROOT / "schemas/contracts/v1/evidence/observation_fitness_assessment.schema.json").read_text())
    Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_exact_expected_size_and_polarity() -> None:
    assert len(MODULE.fixture_cases()) == 14
    assert MODULE.fixture_profile() == 0


def test_excluded_observation_is_retained_for_reinterpretation() -> None:
    candidate, result, _, _ = MODULE.fixture_cases()[1]
    assert result.outcome == "HOLD"
    assert candidate["decision"]["state"] == "EXCLUDED"
    assert candidate["decision"]["handling"] == "RETAIN_AND_EXCLUDE"
    assert "RETAIN_EXCLUDED_EVIDENCE" in candidate["decision"]["obligations"]
    assert set(candidate["decision"]["retained_evidence_refs"]) == MODULE._required_evidence(candidate)


def test_missing_qa_abstains_and_single_observation_is_qualified() -> None:
    cases = MODULE.fixture_cases()
    assert cases[4][0]["decision"]["state"] == "UNKNOWN"
    assert cases[4][0]["decision"]["handling"] == "ABSTAIN"
    assert cases[5][0]["decision"]["state"] == "CONDITIONALLY_FIT"
    assert "LABEL_SINGLE_OBSERVATION_LIMIT" in cases[5][0]["decision"]["obligations"]


def test_contradictory_context_and_self_promotion_fail_closed() -> None:
    cases = MODULE.fixture_cases()
    contradictory = {finding.code for finding in cases[7][1].findings}
    promoted = {finding.code for finding in cases[9][1].findings}
    assert "CONFOUNDER_CONTEXT_CONTRADICTORY" in contradictory
    assert "FITNESS_DECISION_MISMATCH" in promoted


def test_correction_is_append_only_and_requires_lineage() -> None:
    corrected, result, _, _ = MODULE.fixture_cases()[6]
    assert result.outcome == "HOLD"
    assert corrected["correction_lineage"]["state"] == "CORRECTED"
    assert corrected["correction_lineage"]["supersedes_assessment_ref"] is not None
    missing = {finding.code for finding in MODULE.fixture_cases()[11][1].findings}
    assert "CORRECTION_PREDECESSOR_REQUIRED" in missing


def test_identity_is_deterministic_and_tamper_evident() -> None:
    first = MODULE.fixture_cases()[0][0]
    second = MODULE.seal(first)
    assert first["spec_hash"] == second["spec_hash"]
    assert first["assessment_id"] == second["assessment_id"]
    tamper = {finding.code for finding in MODULE.fixture_cases()[13][1].findings}
    assert {"SPEC_HASH_MISMATCH", "ASSESSMENT_ID_MISMATCH"} <= tamper


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
