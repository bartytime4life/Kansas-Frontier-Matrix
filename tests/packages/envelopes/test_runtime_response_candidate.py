"""Deterministic no-network tests for the RuntimeResponseEnvelope candidate helper."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from envelopes import EnvelopeBuildError, build_runtime_response_candidate


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
RUNTIME_SCHEMA_PATH = REPOSITORY_ROOT / (
    "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json"
)
EVIDENCE_SCHEMA_PATH = REPOSITORY_ROOT / (
    "schemas/contracts/v1/evidence/evidence_ref.schema.json"
)
FIXED_HASH = "sha256:" + ("a" * 64)
FIXED_TIME = "2026-08-05T21:30:00Z"
BASE_FIELDS = {
    "id",
    "spec_hash",
    "version",
    "issued_at",
    "outcome",
    "reason_code",
    "evidence_refs",
    "policy_state",
    "freshness",
    "correction_state",
}
ANSWER_EVIDENCE = {
    "ref": "evidence:synthetic-soil-moisture-series",
    "kind": "measurement",
    "bundle_ref": "bundle:synthetic-soil-moisture-series",
}


def _load_validator() -> Draft202012Validator:
    runtime_schema = json.loads(RUNTIME_SCHEMA_PATH.read_text(encoding="utf-8"))
    evidence_schema = json.loads(EVIDENCE_SCHEMA_PATH.read_text(encoding="utf-8"))
    registry = Registry().with_resource(
        evidence_schema["$id"], Resource.from_contents(evidence_schema)
    )
    return Draft202012Validator(
        runtime_schema,
        registry=registry,
        format_checker=FormatChecker(),
    )


def _kwargs() -> dict[str, object]:
    return {
        "response_id": "runtime:soil-moisture:test-001",
        "spec_hash": FIXED_HASH,
        "version": "runtime-response-v1",
        "issued_at": FIXED_TIME,
        "outcome": "ABSTAIN",
        "reason_code": "FIXTURE_ONLY",
        "evidence_refs": [],
        "policy_state": "fixture_only_not_released",
        "freshness": "fixture_only",
        "correction_state": "not_applicable",
    }


def _precision(*, evidence_ref: dict[str, str] | None = None) -> dict[str, object]:
    ref = evidence_ref or ANSWER_EVIDENCE
    return {
        "spatial": {
            "representation": "point",
            "resolution": "station observation",
            "accuracy": "Source-reported station position; no stronger positional accuracy asserted.",
            "generalization_applied": False,
        },
        "temporal": {
            "granularity": "instantaneous observation",
            "observation_interval": {
                "start": "2026-08-05T21:00:00Z",
                "end": "2026-08-05T21:00:00Z",
            },
            "freshness_class": "current",
        },
        "attribute": {
            "measure": "synthetic soil moisture",
            "unit": "fraction",
            "significant_precision": 3,
            "classification_granularity": None,
        },
        "requested_precision": {
            "spatial": "field scale",
            "temporal": "hourly",
            "attribute": "four decimal places",
        },
        "evidence_refs": [copy.deepcopy(ref)],
        "transform_receipt_refs": [],
    }


@pytest.mark.parametrize("outcome", ["ANSWER", "ABSTAIN", "DENY", "ERROR"])
def test_builds_schema_valid_closed_candidate_for_each_outcome(outcome: str) -> None:
    kwargs = _kwargs()
    kwargs["outcome"] = outcome
    if outcome == "ANSWER":
        kwargs["evidence_refs"] = [copy.deepcopy(ANSWER_EVIDENCE)]
        kwargs["precision_actually_used"] = _precision()

    candidate = build_runtime_response_candidate(**kwargs)

    expected = BASE_FIELDS | ({"precision_actually_used"} if outcome == "ANSWER" else set())
    assert set(candidate) == expected
    assert candidate["outcome"] == outcome
    assert list(_load_validator().iter_errors(candidate)) == []


def test_is_deterministic_and_defensively_copies_nested_inputs() -> None:
    evidence_refs = [copy.deepcopy(ANSWER_EVIDENCE)]
    precision = _precision(evidence_ref=evidence_refs[0])
    kwargs = _kwargs()
    kwargs.update(
        {
            "outcome": "ANSWER",
            "evidence_refs": evidence_refs,
            "precision_actually_used": precision,
        }
    )

    first = build_runtime_response_candidate(**kwargs)
    second = build_runtime_response_candidate(**kwargs)
    evidence_refs[0]["ref"] = "evidence:mutated-after-build"
    precision["spatial"]["resolution"] = "mutated"

    assert first == second
    assert first["evidence_refs"][0]["ref"] == ANSWER_EVIDENCE["ref"]
    assert (
        first["precision_actually_used"]["spatial"]["resolution"]
        == "station observation"
    )


@pytest.mark.parametrize(
    ("field", "value", "code"),
    [
        ("response_id", "Bad Id", "FIELD_PATTERN_INVALID"),
        ("spec_hash", "sha256:short", "FIELD_PATTERN_INVALID"),
        ("issued_at", "2026-08-05T21:30:00", "DATETIME_NOT_OFFSET_AWARE"),
        ("outcome", "ALLOW", "OUTCOME_INVALID"),
        ("reason_code", "", "FIELD_INVALID"),
        ("policy_state", " ", "FIELD_INVALID"),
    ],
)
def test_rejects_invalid_local_fields(field: str, value: object, code: str) -> None:
    kwargs = _kwargs()
    kwargs[field] = value

    with pytest.raises(EnvelopeBuildError) as error:
        build_runtime_response_candidate(**kwargs)

    assert error.value.code == code
    assert value.__repr__() not in str(error.value)


@pytest.mark.parametrize(
    ("evidence_refs", "code"),
    [
        ("not-an-array", "EVIDENCE_REFS_NOT_ARRAY"),
        (["not-an-object"], "EVIDENCE_REF_NOT_OBJECT"),
        ([{"ref": "evidence:1"}], "EVIDENCE_REF_REQUIRED_FIELD_MISSING"),
        (
            [{"ref": "evidence:1", "kind": "claim"}],
            "EVIDENCE_REF_KIND_INVALID",
        ),
        (
            [{"ref": "evidence:1", "kind": "record", "secret": "value"}],
            "EVIDENCE_REF_ADDITIONAL_FIELD",
        ),
        (
            [
                {"ref": "evidence:1", "kind": "record"},
                {"ref": "evidence:1", "kind": "record"},
            ],
            "EVIDENCE_REF_DUPLICATE",
        ),
    ],
)
def test_rejects_invalid_evidence_ref_shapes(
    evidence_refs: object,
    code: str,
) -> None:
    kwargs = _kwargs()
    kwargs["evidence_refs"] = evidence_refs

    with pytest.raises(EnvelopeBuildError) as error:
        build_runtime_response_candidate(**kwargs)

    assert error.value.code == code


def test_answer_requires_evidence_and_precision() -> None:
    kwargs = _kwargs()
    kwargs["outcome"] = "ANSWER"

    with pytest.raises(EnvelopeBuildError) as error:
        build_runtime_response_candidate(**kwargs)
    assert error.value.code == "ANSWER_EVIDENCE_REFS_REQUIRED"

    kwargs["evidence_refs"] = [copy.deepcopy(ANSWER_EVIDENCE)]
    with pytest.raises(EnvelopeBuildError) as error:
        build_runtime_response_candidate(**kwargs)
    assert error.value.code == "ANSWER_PRECISION_REQUIRED"


def test_negative_outcome_forbids_precision_disclosure() -> None:
    kwargs = _kwargs()
    kwargs["precision_actually_used"] = _precision()

    with pytest.raises(EnvelopeBuildError) as error:
        build_runtime_response_candidate(**kwargs)

    assert error.value.code == "NEGATIVE_OUTCOME_PRECISION_FORBIDDEN"


def test_precision_evidence_must_be_bound_at_envelope_top_level() -> None:
    kwargs = _kwargs()
    kwargs.update(
        {
            "outcome": "ANSWER",
            "evidence_refs": [copy.deepcopy(ANSWER_EVIDENCE)],
            "precision_actually_used": _precision(
                evidence_ref={"ref": "evidence:other", "kind": "measurement"}
            ),
        }
    )

    with pytest.raises(EnvelopeBuildError) as error:
        build_runtime_response_candidate(**kwargs)

    assert error.value.code == "PRECISION_EVIDENCE_NOT_TOP_LEVEL"


def test_generalization_requires_transform_receipt() -> None:
    precision = _precision()
    precision["spatial"]["generalization_applied"] = True
    kwargs = _kwargs()
    kwargs.update(
        {
            "outcome": "ANSWER",
            "evidence_refs": [copy.deepcopy(ANSWER_EVIDENCE)],
            "precision_actually_used": precision,
        }
    )

    with pytest.raises(EnvelopeBuildError) as error:
        build_runtime_response_candidate(**kwargs)
    assert error.value.code == "PRECISION_GENERALIZATION_RECEIPT_REQUIRED"

    precision["transform_receipt_refs"] = [
        "urn:kfm:transform-receipt:synthetic-generalization-v1"
    ]
    assert build_runtime_response_candidate(**kwargs)["outcome"] == "ANSWER"


def test_precision_interval_must_not_be_inverted() -> None:
    precision = _precision()
    precision["temporal"]["observation_interval"] = {
        "start": "2026-08-05T22:00:00Z",
        "end": "2026-08-05T21:00:00Z",
    }
    kwargs = _kwargs()
    kwargs.update(
        {
            "outcome": "ANSWER",
            "evidence_refs": [copy.deepcopy(ANSWER_EVIDENCE)],
            "precision_actually_used": precision,
        }
    )

    with pytest.raises(EnvelopeBuildError) as error:
        build_runtime_response_candidate(**kwargs)

    assert error.value.code == "PRECISION_INTERVAL_INVERTED"


def test_does_not_add_authority_or_payload_fields() -> None:
    candidate = build_runtime_response_candidate(**_kwargs())

    assert set(candidate) == BASE_FIELDS
    assert {
        "payload",
        "proof_bundle",
        "catalog_entry",
        "release_manifest",
        "promotion_decision",
        "policy_decision",
        "publication",
    }.isdisjoint(candidate)
