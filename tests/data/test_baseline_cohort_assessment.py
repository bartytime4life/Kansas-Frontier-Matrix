from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/data/validate_baseline_cohort_assessment.py"
SPEC = importlib.util.spec_from_file_location("baseline_cohort_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads(
        (REPO_ROOT / "schemas/contracts/v1/data/baseline_cohort_assessment.schema.json").read_text()
    )
    Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_exact_expected_size_and_polarity() -> None:
    cases = MODULE.fixture_cases()
    assert len(cases) == 19
    assert MODULE.fixture_profile() == 0


def test_clean_cohort_is_only_a_review_candidate() -> None:
    candidate, result, _, _ = MODULE.fixture_cases()[0]
    assert result.outcome == "HOLD"
    assert candidate["baseline_validation_report"]["baseline_state"] == "REPLAYABLE"
    assert candidate["baseline_validation_report"]["decision"] == "REVIEW_CANDIDATE"
    assert "HUMAN_REVIEW_REQUIRED" in candidate["baseline_validation_report"]["obligations"]


def test_exclusions_missingness_and_resolved_discontinuity_remain_qualified() -> None:
    cases = MODULE.fixture_cases()
    for index in (1, 2, 3, 4):
        candidate, result, _, _ = cases[index]
        assert result.outcome == "HOLD"
        assert candidate["baseline_validation_report"]["baseline_state"] == "QUALIFIED"
        assert candidate["baseline_validation_report"]["decision"] == "REVIEW_CANDIDATE"


def test_unresolved_discontinuity_holds() -> None:
    candidate, result, _, _ = MODULE.fixture_cases()[7]
    assert result.outcome == "HOLD"
    assert candidate["baseline_validation_report"]["baseline_state"] == "DISCONTINUITY_UNRESOLVED"
    assert candidate["baseline_validation_report"]["decision"] == "HOLD"


def test_counts_and_missingness_must_reconcile() -> None:
    cases = MODULE.fixture_cases()
    assert "COHORT_COUNTS_DO_NOT_CLOSE" in {finding.code for finding in cases[9][1].findings}
    assert "EXCLUSION_COUNTS_DO_NOT_CLOSE" in {finding.code for finding in cases[10][1].findings}
    assert "MISSINGNESS_STATE_MISMATCH" in {finding.code for finding in cases[11][1].findings}


def test_discontinuity_order_and_rebuild_lineage_fail_closed() -> None:
    cases = MODULE.fixture_cases()
    assert "DISCONTINUITIES_NOT_CHRONOLOGICAL" in {finding.code for finding in cases[12][1].findings}
    assert "BASELINE_SUPERSESSION_MISMATCH" in {finding.code for finding in cases[13][1].findings}
    assert "CORRECTION_PREDECESSOR_REQUIRED" in {finding.code for finding in cases[14][1].findings}


def test_identity_is_deterministic_and_tamper_evident() -> None:
    first = MODULE.fixture_cases()[0][0]
    second = MODULE.seal(first)
    assert first["spec_hash"] == second["spec_hash"]
    assert first["assessment_id"] == second["assessment_id"]
    tamper_codes = {finding.code for finding in MODULE.fixture_cases()[18][1].findings}
    assert {"SPEC_HASH_MISMATCH", "ASSESSMENT_ID_MISMATCH"} <= tamper_codes


def test_duplicate_keys_and_symlinks_are_denied_without_echoing_values(tmp_path: Path) -> None:
    sentinel = "SENSITIVE_SENTINEL_DO_NOT_ECHO"
    duplicate = tmp_path / "duplicate.json"
    duplicate.write_text('{"subject_ref":"%s","subject_ref":"other"}' % sentinel)
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
