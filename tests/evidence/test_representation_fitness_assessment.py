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
