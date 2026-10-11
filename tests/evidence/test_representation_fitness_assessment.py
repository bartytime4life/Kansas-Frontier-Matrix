from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/evidence/validate_representation_fitness_assessment.py"
SPEC = importlib.util.spec_from_file_location("representation_fitness_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_schema_is_valid_draft_2020_12() -> None:
    schema = json.loads((REPO_ROOT / "schemas/contracts/v1/evidence/representation_fitness_assessment.schema.json").read_text())
    Draft202012Validator.check_schema(schema)


def test_fixture_matrix_has_expected_polarity() -> None:
    assert MODULE.fixture_profile() == 0


def test_false_precision_is_rejected() -> None:
    path = REPO_ROOT / "fixtures/contracts/v1/evidence/representation_fitness_assessment/invalid/false_precision_marked_fit.json"
    codes = {finding.code for finding in MODULE.validate(path).findings}
    assert "REPRESENTATION_FALSE_PRECISION" in codes


def test_conditional_result_requires_obligation() -> None:
    path = REPO_ROOT / "fixtures/contracts/v1/evidence/representation_fitness_assessment/invalid/conditional_missing_obligation.json"
    codes = {finding.code for finding in MODULE.validate(path).findings}
    assert "FITNESS_OBLIGATION_REQUIRED" in codes


def test_one_representation_has_use_specific_synthetic_assessments() -> None:
    root = REPO_ROOT / "fixtures/contracts/v1/evidence/representation_fitness_assessment/valid"
    navigation_path = root / "huc12_public_navigation_fit.json"
    operational_path = root / "huc12_operational_decision_unknown.json"
    navigation = json.loads(navigation_path.read_text(encoding="utf-8"))
    operational = json.loads(operational_path.read_text(encoding="utf-8"))

    assert MODULE.validate(navigation_path).ok
    assert MODULE.validate(operational_path).ok
    assert navigation["subject"] == operational["subject"]
    assert navigation["intended_use"]["use_class"] == "PUBLIC_NAVIGATION"
    assert navigation["overall_outcome"] == "FIT"
    assert operational["intended_use"]["use_class"] == "OPERATIONAL_DECISION"
    assert operational["intended_use"]["consequence_level"] == "HIGH"
    assert operational["dimensions"]["temporal"]["outcome"] == "UNKNOWN"
    assert operational["overall_outcome"] == "UNKNOWN"

    # Fixture validation checks declarations, not evidence resolution or release.
    for assessment in (navigation, operational):
        assert assessment["review_state"] == "DRAFT"
        assert assessment["policy_decision_refs"] == []
        assert assessment["governance"]["fixture_only"] is True
        assert assessment["governance"]["truth_authority"] is False
        assert assessment["governance"]["policy_authority"] is False
        assert assessment["governance"]["review_authority"] is False
        assert assessment["governance"]["release_authority"] is False
        assert assessment["governance"]["publication_authority"] is False
