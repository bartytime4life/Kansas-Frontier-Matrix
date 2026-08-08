from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/policy/validate_policy_decision_vocabulary_binding.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/policy/policy_decision/vocabulary_binding"
VOCAB_PATH = REPO_ROOT / "policy/decision/vocabulary.v1.json"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/policy/policy_decision.schema.json"

SPEC = importlib.util.spec_from_file_location("policy_decision_vocab_binding", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(kind: str, name: str):
    return MODULE.validate_binding(
        load(FIXTURE_ROOT / kind / name),
        load(VOCAB_PATH),
        load(SCHEMA_PATH),
    )


def test_answer_with_registered_obligations_passes() -> None:
    result = validate("valid", "answer_render.json")
    assert result["status"] == "PASS"
    assert result["findings"] == []
    assert all(value is False for value in result["authority"].values())


def test_registered_deny_reason_passes() -> None:
    result = validate("valid", "deny_rights.json")
    assert result["status"] == "PASS"


def test_unknown_reason_denies() -> None:
    result = validate("invalid", "unknown_reason.json")
    assert result["status"] == "DENY"
    assert {item["code"] for item in result["findings"]} == {"REASON_CODE_UNKNOWN"}


def test_reason_outcome_mismatch_denies() -> None:
    result = validate("invalid", "outcome_mismatch.json")
    assert result["status"] == "DENY"
    assert "REASON_OUTCOME_MISMATCH" in {item["code"] for item in result["findings"]}


def test_inactive_vocabulary_cannot_claim_authority() -> None:
    vocabulary = load(VOCAB_PATH)
    vocabulary["governance"]["policy_evaluation"] = True
    result = MODULE.validate_binding(
        load(FIXTURE_ROOT / "valid" / "deny_rights.json"),
        vocabulary,
        load(SCHEMA_PATH),
    )
    assert result["status"] == "DENY"
    assert "VOCABULARY_AUTHORITY_OVERCLAIM" in {item["code"] for item in result["findings"]}


def test_cli_is_deterministic_and_no_authority_is_granted() -> None:
    command = [
        sys.executable,
        str(MODULE_PATH),
        str(FIXTURE_ROOT / "valid" / "answer_render.json"),
    ]
    first = subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
    second = subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
    assert first.returncode == 0
    assert first.stdout == second.stdout
    payload = json.loads(first.stdout)
    assert payload["status"] == "PASS"
    assert payload["authority"]["policy_evaluated"] is False
    assert payload["authority"]["publication_authorized"] is False
