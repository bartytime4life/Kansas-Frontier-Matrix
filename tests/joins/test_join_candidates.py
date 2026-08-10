from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
SPEC = importlib.util.spec_from_file_location("join_candidates", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads((REPO_ROOT / "schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json").read_text())
    Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_exact_expected_size_and_polarity() -> None:
    assert len(MODULE.fixture_cases()) == 19
    assert MODULE.fixture_profile() == 0


def test_exact_key_is_sql_first_deterministic_and_non_publishing() -> None:
    candidate, result, _, _ = MODULE.fixture_cases()[0]
    assert result.status == "PASS"
    assert candidate["decision"]["validator_outcome"] == "ALLOW"
    assert candidate["decision"]["status"] == "JOIN_CANDIDATE"
    assert candidate["governance"]["sql_database"] == "IN_MEMORY_SQLITE"
    assert not any(candidate["decision"]["effects"].values())
    assert MODULE.seal(candidate)["assessment_id"] == candidate["assessment_id"]


def test_spatial_temporal_and_mismatch_paths_are_finite() -> None:
    cases = MODULE.fixture_cases()
    assert cases[1][0]["decision"]["validator_outcome"] == "ALLOW"
    assert cases[2][0]["decision"]["validator_outcome"] == "ABSTAIN"
    assert cases[3][0]["decision"]["status"] == "NO_JOIN_CANDIDATE"
    assert cases[4][0]["decision"]["matched"] is False


def test_risk_fixtures_preserve_distinct_outcomes() -> None:
    cases = MODULE.fixture_cases()
    assert cases[5][0]["decision"]["status"] == "EVIDENCE_REF_MISSING"
    assert cases[6][0]["decision"]["status"] == "SOURCE_ROLE_REVIEW_REQUIRED"
    assert cases[7][0]["decision"]["validator_outcome"] == "DENY"
    assert cases[8][0]["decision"]["status"] == "LIVING_PERSON_JOIN_DENIED"
    assert cases[9][0]["decision"]["validator_outcome"] == "ERROR"
    assert cases[11][0]["decision"]["status"] == "SENSITIVITY_REVIEW_REQUIRED"
    assert cases[18][0]["decision"]["validator_outcome"] == "DENY"


def test_sql_metacharacters_are_parameter_values() -> None:
    candidate, result, _, _ = MODULE.fixture_cases()[10]
    assert result.status == "PASS"
    assert candidate["decision"]["matched"] is False
    assert candidate["decision"]["validator_outcome"] == "ABSTAIN"


def test_rule_counts_roles_and_sensitivity_are_inspectable() -> None:
    candidate = MODULE.fixture_cases()[6][0]
    results = {item["rule_code"]: item["failure_count"] for item in candidate["decision"]["rule_results"]}
    assert tuple(results) == MODULE.RULE_ORDER
    assert results["SOURCE_ROLES_COMPATIBLE"] == 1
    assert candidate["decision"]["source_roles"] == {
        "left": "AGGREGATE",
        "right": "OBSERVED",
        "output_role": "CANDIDATE_RELATION",
    }


def test_stored_decision_and_identity_tamper_fail_closed() -> None:
    cases = MODULE.fixture_cases()
    assert "JOIN_DECISION_MISMATCH" in {finding.code for finding in cases[12][1].findings}
    assert "JOIN_DECISION_MISMATCH" in {finding.code for finding in cases[13][1].findings}
    identity = {finding.code for finding in cases[17][1].findings}
    assert {"SPEC_HASH_MISMATCH", "ASSESSMENT_ID_MISMATCH"} <= identity


def test_duplicate_keys_and_symlinks_are_denied_without_echoing_values(tmp_path: Path) -> None:
    sentinel = "SENSITIVE_SENTINEL_DO_NOT_ECHO"
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text('{"profile":"%s","profile":"other"}' % sentinel)
    result = MODULE.validate_file(duplicate)
    assert result.status == "FAIL"
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


def test_helper_has_no_network_client_or_file_write_path() -> None:
    source = MODULE_PATH.read_text(encoding="utf-8")
    forbidden = (
        "import requests", "import urllib", "import socket", "httpx", "aiohttp", "boto3",
        "write_text(", "write_bytes(", "open(\"w", "open('w",
    )
    assert not any(token in source for token in forbidden)
