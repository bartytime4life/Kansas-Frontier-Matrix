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
ANSWER_EVIDENCE = [
    {
        "ref": "evidence:synthetic-soil-moisture-series",
        "kind": "measurement",
        "bundle_ref": "bundle:synthetic-soil-moisture-series",
    }
]


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


def _precision(
    evidence_refs: list[dict[str, str]] | None = None,
) -> dict[str, object]:
    refs = copy.deepcopy(evidence_refs or ANSWER_EVIDENCE)
    return {
        "spatial": {
            "representation": "grid",
            "resolution": "250 m modeled grid",
            "accuracy": (
                "Source-reported grid resolution; positional accuracy is not asserted."
            ),
            "generalization_applied": False,
        },
        "temporal": {
            "granularity": "daily",
            "observation_interval": {
                "start": "2026-08-04T00:00:00Z",
                "end": "2026-08-05T00:00:00Z",
            },
            "freshness_class": "stale-accepted",
        },
        "attribute": {
            "measure": "synthetic_soil_moisture",
            "unit": "percent",
            "significant_precision": 2,
            "classification_granularity": None,
        },
        "requested_precision": {
            "spatial": "30 m",
            "temporal": "hourly",
            "attribute": "3 decimal places",
        },
        "evidence_refs": refs,
        "transform_receipt_refs": [],
    }


@pytest.mark.parametrize("outcome", ["ANSWER", "ABSTAIN", "DENY", "ERROR"])
def test_builds_schema_valid_closed_candidate_for_each_outcome(outcome: str) -> None:
    kwargs = _kwargs()
    kwargs["outcome"] = outcome
    if outcome == "ANSWER":
        kwargs["evidence_refs"] = copy.deepcopy(ANSWER_EVIDENCE)
        kwargs["precision_actually_used"] = _precision()

    candidate = build_runtime_response_candidate(**kwargs)

    expected_fields = BASE_FIELDS | (
        {"precision_actually_used"} if outcome == "ANSWER" else set()
    )
    assert set(candidate) == expected_fields
    assert candidate["outcome"] == outcome
    assert list(_load_validator().iter_errors(candidate)) == []


def test_answer_requires_precision_and_non_answer_forbids_it() -> None:
    answer = _kwargs()
    answer["outcome"] = "ANSWER"
    answer["evidence_refs"] = copy.deepcopy(ANSWER_EVIDENCE)
    with pytest.raises(EnvelopeBuildError) as missing:
        build_runtime_response_candidate(**answer)
    assert missing.value.code == "PRECISION_REQUIRED"

    abstain = _kwargs()
    abstain["precision_actually_used"] = _precision()
    with pytest.raises(EnvelopeBuildError) as forbidden:
        build_runtime_response_candidate(**abstain)
    assert forbidden.value.code == "PRECISION_FORBIDDEN"


def test_precision_is_defensively_copied_and_evidence_bound() -> None:
    evidence_refs = copy.deepcopy(ANSWER_EVIDENCE)
    precision = _precision(evidence_refs)
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
    assert first["evidence_refs"][0]["ref"] == (
        "evidence:synthetic-soil-moisture-series"
    )
    assert first["precision_actually_used"]["spatial"]["resolution"] == (
        "250 m modeled grid"
    )


def test_rejects_precision_evidence_not_present_at_top_level() -> None:
    kwargs = _kwargs()
    kwargs.update(
        {
            "outcome": "ANSWER",
            "evidence_refs": copy.deepcopy(ANSWER_EVIDENCE),
            "precision_actually_used": _precision(
                [{"ref": "evidence:other", "kind": "measurement"}]
            ),
        }
    )

    with pytest.raises(EnvelopeBuildError) as error:
        build_runtime_response_candidate(**kwargs)
    assert error.value.code == "PRECISION_EVIDENCE_NOT_TOP_LEVEL"


def test_is_deterministic_and_defensively_copies_evidence_refs() -> None:
    evidence_refs = [
        {
            "ref": "evidence:synthetic-soil-moisture-series",
            "kind": "measurement",
        }
    ]
    kwargs = _kwargs()
    kwargs["evidence_refs"] = evidence_refs

    first = build_runtime_response_candidate(**kwargs)
    second = build_runtime_response_candidate(**kwargs)
    evidence_refs[0]["ref"] = "evidence:mutated-after-build"

    assert first == second
    assert first["evidence_refs"] == [
        {
            "ref": "evidence:synthetic-soil-moisture-series",
            "kind": "measurement",
        }
    ]


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
