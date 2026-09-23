import asyncio
import json
import os
import types
from pathlib import Path

import pytest

from governed_api.main import app
from governed_api.routes.registry import ROUTES
from governed_api.stub import (
    invoke_fixture_operation,
    invoke_sync_fixture_operation,
    make_abstain_envelope,
    make_fixture_failure_envelope,
)
from schema_assert import assert_jsonschema_subset

ROOT = Path(__file__).resolve().parents[3]
FIXTURES = ROOT / "apps" / "governed-api" / "tests" / "fixtures" / "api_failure_cases.json"
SCHEMA = ROOT / "schemas" / "contracts" / "v1" / "runtime" / "runtime_response_envelope.schema.json"


def test_failure_fixtures_are_deterministic_and_schema_valid() -> None:
    cases = json.loads(FIXTURES.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    previous = os.environ.get("GOVERNED_API_ISSUED_AT")
    os.environ["GOVERNED_API_ISSUED_AT"] = "2026-09-12T00:00:00+00:00"
    try:
        for case in cases:
            first = make_fixture_failure_envelope(case["kind"], case["correlation_id"])
            second = make_fixture_failure_envelope(case["kind"], case["correlation_id"])
            assert first == second
            assert first["outcome"] == case["outcome"]
            assert first["reason_code"] == case["reason_code"]
            assert first["id"].endswith(f":{case['correlation_id']}")
            assert set(first) == set(schema["required"])
            assert_jsonschema_subset(first, schema)
    finally:
        if previous is None:
            os.environ.pop("GOVERNED_API_ISSUED_AT", None)
        else:
            os.environ["GOVERNED_API_ISSUED_AT"] = previous


def test_abstain_and_deny_are_not_collapsed_to_error() -> None:
    cases = {case["kind"]: case for case in json.loads(FIXTURES.read_text(encoding="utf-8"))}
    assert make_fixture_failure_envelope("missing_evidence", cases["missing_evidence"]["correlation_id"])["outcome"] == "ABSTAIN"
    assert make_fixture_failure_envelope("policy_denial", cases["policy_denial"]["correlation_id"])["outcome"] == "DENY"


def test_invalid_correlation_is_not_reflected() -> None:
    payload = make_fixture_failure_envelope("internal_defect", "secret/path?stack=trace&token=redacted")
    assert payload["id"] == "fixture:failure:internal_defect:unavailable"
    assert "secret" not in json.dumps(payload)
    assert "stack" not in json.dumps(payload)
    assert "token" not in json.dumps(payload)


def test_correlation_id_cannot_make_the_envelope_schema_invalid() -> None:
    payload = make_fixture_failure_envelope("internal_defect", "UPPERCASE")
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert payload["id"] == "fixture:failure:internal_defect:unavailable"
    assert_jsonschema_subset(payload, schema)


@pytest.mark.parametrize(
    ("kind", "expected_reason"),
    [
        ("malformed_input", "INVALID_REQUEST"),
        ("dependency_unavailable", "DEPENDENCY_UNAVAILABLE"),
        ("timeout", "REQUEST_TIMEOUT"),
        ("cancellation", "REQUEST_CANCELLED"),
        ("invalid_response", "INVALID_RESPONSE"),
    ],
)
def test_operational_failure_classes_have_safe_codes(kind: str, expected_reason: str) -> None:
    payload = make_fixture_failure_envelope(kind, "fixture-operational-001")
    assert payload["reason_code"] == expected_reason
    assert payload["outcome"] in {"ABSTAIN", "ERROR"}


def test_sync_exception_and_invalid_response_fail_closed_without_leaks() -> None:
    def raises_secret() -> dict:
        raise RuntimeError("/private/store token=never-reflect")

    error, error_kind = invoke_sync_fixture_operation(raises_secret, "fixture-sync-001")
    invalid, invalid_kind = invoke_sync_fixture_operation(lambda: {"outcome": "ANSWER"}, "fixture-invalid-001")

    assert (error_kind, error["outcome"], error["reason_code"]) == (
        "internal_defect",
        "ERROR",
        "SAFE_RUNTIME_ERROR",
    )
    assert (invalid_kind, invalid["outcome"], invalid["reason_code"]) == (
        "invalid_response",
        "ERROR",
        "INVALID_RESPONSE",
    )
    rendered = json.dumps([error, invalid])
    assert "/private/store" not in rendered
    assert "never-reflect" not in rendered


@pytest.mark.parametrize(
    "invalid_payload",
    [
        {"outcome": "ANSWER"},
        {**make_abstain_envelope("evidence"), "extra": "not-closed"},
        {**make_abstain_envelope("evidence"), "evidence_refs": [{"secret": "not-validated"}]},
        {**make_abstain_envelope("evidence"), "issued_at": "not-a-date"},
        {**make_abstain_envelope("evidence"), "issued_at": "2026-W37-6T00:00:00+00:00"},
        {**make_abstain_envelope("evidence"), "issued_at": "2026-09-12 00:00:00+00:00"},
    ],
)
def test_operation_boundary_rejects_non_closed_negative_shapes(invalid_payload: dict) -> None:
    payload, failure_kind = invoke_sync_fixture_operation(lambda: invalid_payload, "fixture-invalid-002")
    assert failure_kind == "invalid_response"
    assert payload["reason_code"] == "INVALID_RESPONSE"
    assert "secret" not in json.dumps(payload)


def test_rejected_async_work_timeout_and_cancellation_are_finite() -> None:
    async def rejects() -> dict:
        raise RuntimeError("secret async detail")

    async def times_out() -> dict:
        raise TimeoutError("private dependency")

    async def cancels() -> dict:
        raise asyncio.CancelledError

    rejected = asyncio.run(invoke_fixture_operation(rejects, "fixture-async-001"))
    timed_out = asyncio.run(invoke_fixture_operation(times_out, "fixture-timeout-002"))
    cancelled = asyncio.run(invoke_fixture_operation(cancels, "fixture-cancelled-002"))

    assert (rejected[1], rejected[0]["reason_code"]) == ("internal_defect", "SAFE_RUNTIME_ERROR")
    assert (timed_out[1], timed_out[0]["reason_code"]) == ("timeout", "REQUEST_TIMEOUT")
    assert (cancelled[1], cancelled[0]["reason_code"]) == ("cancellation", "REQUEST_CANCELLED")
    assert "secret" not in json.dumps([rejected[0], timed_out[0], cancelled[0]])
    assert "private" not in json.dumps([rejected[0], timed_out[0], cancelled[0]])


def test_intentional_negative_outcomes_survive_operation_boundary() -> None:
    abstain_payload = make_abstain_envelope("evidence")
    abstain = asyncio.run(invoke_fixture_operation(lambda: abstain_payload, "fixture-abstain-001"))
    deny_payload = make_fixture_failure_envelope("policy_denial", "fixture-deny-001")
    deny = asyncio.run(invoke_fixture_operation(lambda: deny_payload, "fixture-deny-001"))

    assert abstain == (abstain_payload, None)
    assert deny == (deny_payload, None)


@pytest.mark.parametrize("outcome", [[], {}, None, True, 1, 1.0])
def test_malformed_json_outcomes_fail_closed_in_sync_async_and_wsgi(outcome, monkeypatch) -> None:
    invalid = {**make_abstain_envelope("evidence"), "outcome": outcome}
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    async def malformed_async() -> dict:
        return invalid

    for payload, failure_kind in (
        invoke_sync_fixture_operation(lambda: invalid, "fixture-malformed-001"),
        asyncio.run(invoke_fixture_operation(malformed_async, "fixture-malformed-001")),
    ):
        assert failure_kind == "invalid_response"
        assert payload["outcome"] == "ERROR"
        assert payload["reason_code"] == "INVALID_RESPONSE"
        assert payload["evidence_refs"] == []
        assert_jsonschema_subset(payload, schema)

    monkeypatch.setitem(ROUTES, "/evidence", lambda: invalid)
    response = {}

    def start_response(status, headers):
        response["status"] = status
        response["headers"] = dict(headers)

    body = b"".join(app({"PATH_INFO": "/evidence", "REQUEST_METHOD": "GET"}, start_response))
    payload = json.loads(body)
    assert response["status"] == "500 Internal Server Error"
    assert response["headers"]["Content-Type"] == "application/json"
    assert int(response["headers"]["Content-Length"]) == len(body)
    assert payload["reason_code"] == "INVALID_RESPONSE"
    assert_jsonschema_subset(payload, schema)


def test_provider_defined_object_behavior_cannot_cross_json_guard() -> None:
    class UnsafeMapping(dict):
        def get(self, *args):
            raise AssertionError("provider mapping behavior must not run")

    class UnsafeString(str):
        def __hash__(self):
            raise AssertionError("provider hash behavior must not run")

    class UnsafeList(list):
        def __eq__(self, other):
            raise AssertionError("provider equality behavior must not run")

    valid = make_abstain_envelope("evidence")
    for invalid in (
        UnsafeMapping(valid),
        {**valid, "outcome": UnsafeString("ABSTAIN")},
        {**valid, "evidence_refs": UnsafeList()},
    ):
        payload, failure_kind = invoke_sync_fixture_operation(lambda: invalid, "fixture-object-001")
        assert failure_kind == "invalid_response"
        assert payload["reason_code"] == "INVALID_RESPONSE"


@pytest.mark.parametrize("outcome", ["ABSTAIN", "DENY", "ERROR"])
def test_plain_negative_json_envelopes_remain_unchanged(outcome) -> None:
    expected = {**make_abstain_envelope("evidence"), "outcome": outcome}
    assert invoke_sync_fixture_operation(lambda: expected, "fixture-negative-001") == (expected, None)


def _pending_coroutine_with_cleanup_failure(error_type):
    @types.coroutine
    def suspend():
        yield

    async def pending():
        try:
            await suspend()
        finally:
            raise error_type("synthetic-cleanup-detail")

    result = pending()
    result.send(None)
    return result


def _assert_invalid_sync_result(operation, surface, correlation_id, monkeypatch) -> None:
    if surface == "sync":
        payload, failure_kind = invoke_sync_fixture_operation(operation, correlation_id)
        assert failure_kind == "invalid_response"
    else:
        monkeypatch.setitem(ROUTES, "/evidence", operation)
        response = {}

        def start_response(status, headers):
            response["status"] = status
            response["headers"] = dict(headers)

        body = b"".join(app({
            "PATH_INFO": "/evidence",
            "REQUEST_METHOD": "GET",
            "kfm.correlation_id": correlation_id,
        }, start_response))
        payload = json.loads(body)
        assert response["status"] == "500 Internal Server Error"
        assert response["headers"]["Content-Type"] == "application/json"
        assert int(response["headers"]["Content-Length"]) == len(body)
        assert response["headers"]["Cache-Control"] == "no-store"
        assert response["headers"]["X-Content-Type-Options"] == "nosniff"

    safe_id = correlation_id if correlation_id == "fixture-cleanup-001" else "unavailable"
    assert payload["id"] == f"fixture:failure:invalid_response:{safe_id}"
    assert payload["outcome"] == "ERROR"
    assert payload["reason_code"] == "INVALID_RESPONSE"
    assert payload["evidence_refs"] == []
    rendered = json.dumps(payload)
    assert "synthetic-cleanup-detail" not in rendered
    assert "synthetic-correlation-secret" not in rendered
    assert_jsonschema_subset(payload, json.loads(SCHEMA.read_text(encoding="utf-8")))


@pytest.mark.parametrize("surface", ["sync", "wsgi"])
@pytest.mark.parametrize("error_type", [RuntimeError, TimeoutError, asyncio.CancelledError])
@pytest.mark.parametrize("correlation_id", ["fixture-cleanup-001", "synthetic-correlation-secret/path"])
def test_invalid_coroutine_cleanup_retains_safe_response(
    surface, error_type, correlation_id, monkeypatch
) -> None:
    result = _pending_coroutine_with_cleanup_failure(error_type)
    _assert_invalid_sync_result(lambda: result, surface, correlation_id, monkeypatch)
    assert result.cr_frame is None


@pytest.mark.parametrize("surface", ["sync", "wsgi"])
@pytest.mark.parametrize("stage", ["inspection", "close_lookup"])
def test_invalid_result_inspection_and_cleanup_lookup_fail_closed(surface, stage, monkeypatch) -> None:
    class InspectionFailure:
        @property
        def __class__(self):
            raise RuntimeError("synthetic-cleanup-detail")

    class CleanupLookupFailure:
        def __await__(self):
            raise AssertionError("a synchronous route must not await the result")

        @property
        def close(self):
            raise RuntimeError("synthetic-cleanup-detail")

    result = InspectionFailure() if stage == "inspection" else CleanupLookupFailure()
    _assert_invalid_sync_result(lambda: result, surface, "fixture-cleanup-001", monkeypatch)


def test_unstarted_coroutine_is_closed_without_executing_it() -> None:
    async def unexpected():
        raise AssertionError("a synchronous route must not execute the coroutine")

    result = unexpected()
    try:
        payload, failure_kind = invoke_sync_fixture_operation(lambda: result, "fixture-cleanup-001")
        assert failure_kind == "invalid_response"
        assert payload["reason_code"] == "INVALID_RESPONSE"
        assert result.cr_frame is None
    finally:
        result.close()


@pytest.mark.parametrize("error_type", [KeyboardInterrupt, SystemExit, GeneratorExit])
@pytest.mark.parametrize("stage", ["operation", "cleanup"])
def test_process_control_exceptions_are_not_converted_to_responses(error_type, stage) -> None:
    class InterruptedCleanup:
        def __await__(self):
            raise AssertionError("a synchronous route must not await the result")

        def close(self):
            raise error_type("synthetic-cleanup-detail")

    def operation():
        if stage == "operation":
            raise error_type("synthetic-cleanup-detail")
        return InterruptedCleanup()

    with pytest.raises(error_type):
        invoke_sync_fixture_operation(operation, "fixture-cleanup-001")
