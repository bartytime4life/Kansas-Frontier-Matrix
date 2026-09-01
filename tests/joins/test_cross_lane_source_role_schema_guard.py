from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json"
SPEC = importlib.util.spec_from_file_location("join_candidates_source_role_schema_guard", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def test_source_role_shape_has_one_closed_authority_definition() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    expected_ref = {"$ref": "#/$defs/source_role"}
    assert schema["$defs"]["endpoint"]["properties"]["source_role"] == expected_ref
    assert schema["$defs"]["source_roles"]["properties"]["left"] == expected_ref
    assert schema["$defs"]["source_roles"]["properties"]["right"] == expected_ref


def test_valid_derived_source_roles_remain_schema_valid() -> None:
    candidate = MODULE.fixture_cases()[0][0]
    assert list(_validator().iter_errors(candidate)) == []


def test_unknown_decision_source_role_is_schema_rejected() -> None:
    candidate = copy.deepcopy(MODULE.fixture_cases()[0][0])
    candidate["decision"]["source_roles"]["left"] = "UNREGISTERED_ROLE"
    errors = list(_validator().iter_errors(candidate))
    assert any(tuple(error.absolute_path) == ("decision", "source_roles", "left") for error in errors)


def test_unknown_endpoint_source_role_is_rejected_by_same_definition() -> None:
    candidate = copy.deepcopy(MODULE.fixture_cases()[0][0])
    candidate["endpoints"]["left"]["source_role"] = "UNREGISTERED_ROLE"
    errors = list(_validator().iter_errors(candidate))
    assert any(tuple(error.absolute_path) == ("endpoints", "left", "source_role") for error in errors)
