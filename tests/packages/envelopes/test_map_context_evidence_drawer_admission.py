"""Tests for MapContextEnvelope → EvidenceDrawerPayload admission."""

from __future__ import annotations

import copy
import json
import socket
import sys
from pathlib import Path
from unittest import mock

import pytest
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = ROOT / "packages/envelopes/src"
if str(PACKAGE_SRC) not in sys.path:
    sys.path.insert(0, str(PACKAGE_SRC))

from envelopes import (  # noqa: E402
    EnvelopeBuildError,
    build_map_context_evidence_drawer_admission_candidate,
)

FIXTURES = ROOT / "fixtures/ui/map_context_evidence_drawer_admission"
CASES = json.loads((FIXTURES / "cases.json").read_text(encoding="utf-8"))
DECISION_SCHEMA = json.loads(
    (ROOT / "schemas/contracts/v1/runtime/decision_envelope.schema.json").read_text(
        encoding="utf-8"
    )
)
DECISION_VALIDATOR = Draft202012Validator(
    DECISION_SCHEMA,
    format_checker=FormatChecker(),
)
EXPECTED_FIELDS = {
    "decision_id",
    "id",
    "outcome",
    "decision",
    "policy_family",
    "reason_code",
    "reasons",
    "obligations",
    "evidence_refs",
    "evaluated_at",
    "issued_at",
    "version",
}


def _load(path: str) -> dict[str, object]:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def _run(case: dict[str, object]) -> dict[str, object]:
    return build_map_context_evidence_drawer_admission_candidate(
        decision_id=f"decision:render:{case['case_id']}",
        evaluated_at=str(case["evaluated_at"]),
        map_context=_load(str(case["map_context"])),
        drawer_payload=_load(str(case["drawer_payload"])),
        allow_system_test=bool(case["allow_system_test"]),
    )


def test_manifest_cases_have_exact_finite_results() -> None:
    assert len(CASES["cases"]) == 8
    for case in CASES["cases"]:
        candidate = _run(case)
        assert candidate["outcome"] == case["expected_outcome"], case["case_id"]
        assert candidate["decision"] == case["expected_outcome"], case["case_id"]
        assert candidate["reason_code"] == case["expected_reason_code"], case["case_id"]
        assert candidate["evidence_refs"] == case["expected_evidence_refs"], case["case_id"]


def test_all_emitted_candidates_match_current_decision_envelope_schema() -> None:
    Draft202012Validator.check_schema(DECISION_SCHEMA)
    for case in CASES["cases"]:
        errors = list(DECISION_VALIDATOR.iter_errors(_run(case)))
        assert errors == [], (case["case_id"], errors)


def test_is_deterministic_and_does_not_mutate_inputs() -> None:
    case = CASES["cases"][0]
    map_context = _load(str(case["map_context"]))
    drawer_payload = _load(str(case["drawer_payload"]))
    before_map = copy.deepcopy(map_context)
    before_drawer = copy.deepcopy(drawer_payload)

    first = build_map_context_evidence_drawer_admission_candidate(
        decision_id="decision:render:deterministic",
        evaluated_at=str(case["evaluated_at"]),
        map_context=map_context,
        drawer_payload=drawer_payload,
        allow_system_test=True,
    )
    second = build_map_context_evidence_drawer_admission_candidate(
        decision_id="decision:render:deterministic",
        evaluated_at=str(case["evaluated_at"]),
        map_context=map_context,
        drawer_payload=drawer_payload,
        allow_system_test=True,
    )

    assert first == second
    assert map_context == before_map
    assert drawer_payload == before_drawer


def test_output_is_closed_and_copies_no_drawer_content() -> None:
    for case_id in ("answer-aligned", "deny-sensitive", "error-upstream"):
        case = next(item for item in CASES["cases"] if item["case_id"] == case_id)
        payload = _load(str(case["drawer_payload"]))
        candidate = _run(case)
        rendered = json.dumps(candidate, sort_keys=True)

        assert set(candidate) == EXPECTED_FIELDS
        assert payload["title"] not in rendered
        assert payload["summary"] not in rendered
        for limitation in payload["limitations"]:
            assert limitation not in rendered
        for citation in payload["citations"]:
            assert citation["href"] not in rendered


def test_multiple_selections_abstain_without_choosing_one() -> None:
    case = CASES["cases"][0]
    context = _load(str(case["map_context"]))
    context["selections"].append(
        {
            "feature_id": "huc12:102600150101",
            "layer_id": "water-huc12",
            "evidence_refs": ["evidence:water:wbd"],
        }
    )
    candidate = build_map_context_evidence_drawer_admission_candidate(
        decision_id="decision:render:ambiguous",
        evaluated_at=str(case["evaluated_at"]),
        map_context=context,
        drawer_payload=_load(str(case["drawer_payload"])),
        allow_system_test=True,
    )
    assert candidate["outcome"] == "ABSTAIN"
    assert candidate["reason_code"] == "SELECTION_AMBIGUOUS"
    assert candidate["evidence_refs"] == []


def test_context_governance_overclaim_fails_safe() -> None:
    case = CASES["cases"][0]
    context = _load(str(case["map_context"]))
    context["governance"]["canonical_store_accessed"] = True
    candidate = build_map_context_evidence_drawer_admission_candidate(
        decision_id="decision:render:governance",
        evaluated_at=str(case["evaluated_at"]),
        map_context=context,
        drawer_payload=_load(str(case["drawer_payload"])),
        allow_system_test=True,
    )
    assert candidate["outcome"] == "ERROR"
    assert candidate["reason_code"] == "CONTEXT_GOVERNANCE_INVALID"


def test_unpublished_selected_layer_fails_safe() -> None:
    case = CASES["cases"][0]
    context = _load(str(case["map_context"]))
    context["layers"][0]["release_state"] = "UNRELEASED"
    candidate = build_map_context_evidence_drawer_admission_candidate(
        decision_id="decision:render:unpublished",
        evaluated_at=str(case["evaluated_at"]),
        map_context=context,
        drawer_payload=_load(str(case["drawer_payload"])),
        allow_system_test=True,
    )
    assert candidate["outcome"] == "ERROR"
    assert candidate["reason_code"] == "SELECTED_LAYER_NOT_PUBLISHED"


def test_held_evidence_requires_pending_unreleased_trust() -> None:
    case = CASES["cases"][0]
    context = _load(str(case["map_context"]))
    valid_payload = _load(
        "fixtures/ui/evidence_drawer_payload/valid/abstain-source-drift-review.json"
    )
    valid_candidate = build_map_context_evidence_drawer_admission_candidate(
        decision_id="decision:render:held-valid",
        evaluated_at=str(case["evaluated_at"]),
        map_context=context,
        drawer_payload=valid_payload,
        allow_system_test=True,
    )

    assert valid_candidate["outcome"] == "ABSTAIN"
    assert valid_candidate["reason_code"] == "HELD_EVIDENCE"
    assert valid_candidate["evidence_refs"] == []

    reviewed_payload = copy.deepcopy(valid_payload)
    reviewed_payload["trust_state"]["review"] = "REVIEWED"
    released_payload = _load(
        "fixtures/ui/evidence_drawer_payload/invalid/abstain-held-with-released-state.json"
    )
    current_payload = copy.deepcopy(valid_payload)
    current_payload["trust_state"]["freshness"] = "CURRENT"
    for label, payload in (
        ("reviewed", reviewed_payload),
        ("released", released_payload),
        ("current", current_payload),
    ):
        candidate = build_map_context_evidence_drawer_admission_candidate(
            decision_id=f"decision:render:held-invalid-{label}",
            evaluated_at=str(case["evaluated_at"]),
            map_context=context,
            drawer_payload=payload,
            allow_system_test=True,
        )

        assert candidate["outcome"] == "ERROR"
        assert candidate["reason_code"] == "DRAWER_TRUST_STATE_MISMATCH"
        assert candidate["evidence_refs"] == []


def test_upstream_error_cannot_be_reclassified_as_abstention() -> None:
    case = CASES["cases"][0]
    context = _load(str(case["map_context"]))
    payload = _load(
        "fixtures/ui/evidence_drawer_payload/invalid/abstain-upstream-error.json"
    )

    candidate = build_map_context_evidence_drawer_admission_candidate(
        decision_id="decision:render:abstain-upstream-invalid",
        evaluated_at=str(case["evaluated_at"]),
        map_context=context,
        drawer_payload=payload,
        allow_system_test=True,
    )

    assert candidate["outcome"] == "ERROR"
    assert candidate["reason_code"] == "DRAWER_TRUST_STATE_MISMATCH"
    assert candidate["evidence_refs"] == []
    assert "ABSTAIN_UPSTREAM_CANARY_d3b092" not in json.dumps(candidate)


@pytest.mark.parametrize(
    "reason_code",
    ("POLICY_DENIED", "RIGHTS_UNRESOLVED", "SENSITIVE_DETAIL_RESTRICTED"),
)
def test_denial_reason_cannot_be_reclassified_as_abstention(reason_code: str) -> None:
    case = CASES["cases"][0]
    context = _load(str(case["map_context"]))
    payload = _load(
        "fixtures/ui/evidence_drawer_payload/invalid/abstain-policy-denied.json"
    )
    payload["reason_code"] = reason_code

    candidate = build_map_context_evidence_drawer_admission_candidate(
        decision_id=f"decision:render:abstain-denial-invalid:{reason_code.lower()}",
        evaluated_at=str(case["evaluated_at"]),
        map_context=context,
        drawer_payload=payload,
        allow_system_test=True,
    )

    assert candidate["outcome"] == "ERROR"
    assert candidate["reason_code"] == "DRAWER_TRUST_STATE_MISMATCH"
    assert candidate["evidence_refs"] == []
    assert "ABSTAIN_DENIAL_CANARY_a40e61" not in json.dumps(candidate)


def test_rights_denial_uses_fixed_denial_copy_without_payload_reflection() -> None:
    case = CASES["cases"][0]
    context = _load(str(case["map_context"]))
    payload = _load(
        "fixtures/ui/evidence_drawer_payload/valid/deny-source-quarantined-rights.json"
    )

    candidate = build_map_context_evidence_drawer_admission_candidate(
        decision_id="decision:render:rights-denial-valid",
        evaluated_at=str(case["evaluated_at"]),
        map_context=context,
        drawer_payload=payload,
        allow_system_test=True,
    )

    assert candidate["outcome"] == "DENY"
    assert candidate["reason_code"] == "RIGHTS_UNRESOLVED"
    assert candidate["reasons"] == [
        "drawer payload denied because source rights are unresolved"
    ]
    assert candidate["obligations"] == ["DISPLAY_SAFE_DENIAL"]
    assert candidate["evidence_refs"] == []
    assert "STEWARD_ONLY_QUARANTINE" not in json.dumps(candidate)

    leaking_payload = _load(
        "fixtures/ui/evidence_drawer_payload/invalid/deny-history-leak.json"
    )
    rejected = build_map_context_evidence_drawer_admission_candidate(
        decision_id="decision:render:rights-denial-history-leak",
        evaluated_at=str(case["evaluated_at"]),
        map_context=context,
        drawer_payload=leaking_payload,
        allow_system_test=True,
    )
    assert rejected["outcome"] == "ERROR"
    assert rejected["reason_code"] == "DRAWER_TRUST_STATE_MISMATCH"
    assert rejected["evidence_refs"] == []
    assert "kfm:evidence:synthetic:denied-001" not in json.dumps(rejected)


@pytest.mark.parametrize(
    ("field", "value", "code"),
    [
        ("decision_id", "Bad ID", "DECISION_ID_INVALID"),
        ("evaluated_at", "2026-08-06T21:05:00", "DATETIME_INVALID"),
    ],
)
def test_rejects_unbuildable_local_identity_or_time(
    field: str,
    value: object,
    code: str,
) -> None:
    case = CASES["cases"][0]
    kwargs = {
        "decision_id": "decision:render:valid",
        "evaluated_at": str(case["evaluated_at"]),
        "map_context": _load(str(case["map_context"])),
        "drawer_payload": _load(str(case["drawer_payload"])),
        "allow_system_test": True,
    }
    kwargs[field] = value
    with pytest.raises(EnvelopeBuildError) as error:
        build_map_context_evidence_drawer_admission_candidate(**kwargs)
    assert error.value.code == code
    assert repr(value) not in str(error.value)


def test_no_network_execution() -> None:
    with mock.patch.object(
        socket,
        "create_connection",
        side_effect=AssertionError("network access attempted"),
    ), mock.patch.object(
        socket,
        "socket",
        side_effect=AssertionError("network access attempted"),
    ):
        first = [_run(case) for case in CASES["cases"]]
        second = [_run(case) for case in CASES["cases"]]
    assert first == second
