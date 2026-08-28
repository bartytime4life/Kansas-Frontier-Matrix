from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/policy/validate_policy_evaluation_binding_v1.py"
FIXTURE_ROOT = ROOT / "fixtures/contracts/v1/policy/policy_evaluation_binding_v1"

SPEC = importlib.util.spec_from_file_location("policy_eval_binding", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def load(name: str):
    return json.loads((FIXTURE_ROOT / name).read_text(encoding="utf-8"))


def test_valid_binding_passes_without_authority() -> None:
    result = MODULE.validate(load("valid.json"))
    assert result["status"] == "PASS"
    assert result["findings"] == []
    assert all(value is False for value in result["authority"].values())


def test_digest_mismatch_denies() -> None:
    result = MODULE.validate(load("invalid_digest.json"))
    assert result["status"] == "DENY"
    assert {item["code"] for item in result["findings"]} == {"INPUT_DIGEST_MISMATCH"}


def test_evaluator_declaration_mismatch_denies() -> None:
    candidate = load("valid.json")
    candidate["evaluator"]["bundle_version"] = "v2"
    result = MODULE.validate(candidate)
    assert result["status"] == "DENY"
    assert "EVALUATOR_DECLARATION_MISMATCH" in {item["code"] for item in result["findings"]}


def test_authority_escalation_is_schema_error() -> None:
    candidate = load("valid.json")
    candidate["governance"]["policy_evaluated"] = True
    result = MODULE.validate(candidate)
    assert result["status"] == "ERROR"
    assert "BINDING_SCHEMA_INVALID" in {item["code"] for item in result["findings"]}
