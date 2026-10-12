"""Deterministic no-network tests for the AIReceipt candidate helper."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys

import pytest
from jsonschema import Draft202012Validator, FormatChecker

from envelopes.ai_receipt import (
    AI_RECEIPT_OUTCOMES,
    build_ai_receipt_candidate,
)
from envelopes.runtime_response import EnvelopeBuildError


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPOSITORY_ROOT / (
    "schemas/contracts/v1/runtime/ai_receipt.schema.json"
)
VALIDATOR_PATH = REPOSITORY_ROOT / "tools/validators/validate_ai_receipt.py"
FIXED_INPUT_DIGEST = "sha256:" + ("a" * 64)
FIXED_OUTPUT_DIGEST = "sha256:" + ("b" * 64)
REQUIRED_FIELDS = {
    "id",
    "run_id",
    "adapter",
    "model_ref",
    "inputs_digest",
    "outputs_digest",
    "policy_decision_ref",
    "citation_validation_ref",
    "outcome",
}


def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _kwargs() -> dict[str, str]:
    return {
        "receipt_id": "ai_receipt:focus:test-001",
        "run_id": "mock-run-001",
        "adapter": "mock",
        "model_ref": "fixture-only",
        "inputs_digest": FIXED_INPUT_DIGEST,
        "outputs_digest": FIXED_OUTPUT_DIGEST,
        "policy_decision_ref": "policy-decision:fixture-001",
        "citation_validation_ref": "citation-validation:fixture-001",
        "outcome": "ABSTAIN",
    }


@pytest.mark.parametrize("outcome", sorted(AI_RECEIPT_OUTCOMES))
def test_builds_schema_valid_closed_candidate_for_each_outcome(outcome: str) -> None:
    kwargs = _kwargs()
    kwargs["outcome"] = outcome

    candidate = build_ai_receipt_candidate(**kwargs)

    assert set(candidate) == REQUIRED_FIELDS
    assert candidate["outcome"] == outcome
    assert list(_validator().iter_errors(candidate)) == []


def test_is_deterministic() -> None:
    first = build_ai_receipt_candidate(**_kwargs())
    second = build_ai_receipt_candidate(**_kwargs())

    assert first == second
    assert json.dumps(first, sort_keys=True, separators=(",", ":")) == json.dumps(
        second, sort_keys=True, separators=(",", ":")
    )


@pytest.mark.parametrize(
    ("field", "value", "code"),
    [
        ("receipt_id", "Bad Id", "FIELD_PATTERN_INVALID"),
        ("run_id", "", "FIELD_INVALID"),
        ("adapter", " ", "FIELD_INVALID"),
        ("model_ref", "", "FIELD_INVALID"),
        ("inputs_digest", "sha256:short", "FIELD_PATTERN_INVALID"),
        ("outputs_digest", "SHA256:" + ("a" * 64), "FIELD_PATTERN_INVALID"),
        ("policy_decision_ref", "", "FIELD_INVALID"),
        ("citation_validation_ref", "", "FIELD_INVALID"),
        ("outcome", "ALLOW", "OUTCOME_INVALID"),
    ],
)
def test_rejects_invalid_local_fields(field: str, value: str, code: str) -> None:
    kwargs = _kwargs()
    kwargs[field] = value

    with pytest.raises(EnvelopeBuildError) as error:
        build_ai_receipt_candidate(**kwargs)

    assert error.value.code == code
    assert error.value.field == ("id" if field == "receipt_id" else field)
    assert value.__repr__() not in str(error.value)


@pytest.mark.parametrize("field", ["inputs_digest", "outputs_digest"])
def test_rejects_zero_placeholder_digests(field: str) -> None:
    kwargs = _kwargs()
    kwargs[field] = "sha256:" + ("0" * 64)

    with pytest.raises(EnvelopeBuildError) as error:
        build_ai_receipt_candidate(**kwargs)

    assert error.value.code == "DIGEST_PLACEHOLDER"
    assert error.value.field == field


def test_candidate_passes_repository_validator(tmp_path: Path) -> None:
    candidate_path = tmp_path / "ai_receipt.json"
    candidate_path.write_text(
        json.dumps(build_ai_receipt_candidate(**_kwargs()), indent=2) + "\n",
        encoding="utf-8",
    )

    completed = subprocess.run(
        [sys.executable, str(VALIDATOR_PATH), str(candidate_path)],
        cwd=REPOSITORY_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr or completed.stdout
    result = json.loads(completed.stdout.strip())
    assert result["outcome"] == "PASS"
    assert result["scope"] == "ai-receipt-shape-and-local-consistency-only"


def test_does_not_add_authority_or_payload_fields() -> None:
    candidate = build_ai_receipt_candidate(**_kwargs())

    assert set(candidate) == REQUIRED_FIELDS
    assert {
        "answer",
        "chain_of_thought",
        "evidence_bundle",
        "policy_decision",
        "citation_validation",
        "proof_bundle",
        "release_manifest",
        "promotion_decision",
        "publication",
    }.isdisjoint(candidate)
