import asyncio
import inspect
import os
import re
from datetime import datetime, timezone

_STUB_SPEC_HASH = "sha256:" + "a" * 64
_SAFE_CORRELATION_ID = re.compile(r"^[a-z0-9_-]{1,64}$")
_SAFE_ENVELOPE_ID = re.compile(r"^[a-z][a-z0-9_:.-]*$")
_SAFE_SPEC_HASH = re.compile(r"^sha256:[a-f0-9]{64}$")
_SAFE_VERSION = re.compile(r"^[a-z0-9][a-z0-9_.-]{0,63}$")
_SAFE_REASON_CODE = re.compile(r"^[A-Z][A-Z0-9_]{0,63}$")
_SAFE_STATE = re.compile(r"^[a-z][a-z0-9_-]{0,63}$")
_NEGATIVE_OUTCOMES = frozenset({"ABSTAIN", "DENY", "ERROR"})
_NEGATIVE_ENVELOPE_KEYS = frozenset(
    {
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
)

# Fixture-only translation profile. These names are local to this proof slice;
# they are not a public registry or a new envelope shape.
_FAILURE_PROFILE = {
    "malformed_input": ("ERROR", "INVALID_REQUEST"),
    "unsupported_scope": ("ABSTAIN", "UNSUPPORTED_SCOPE"),
    "missing_evidence": ("ABSTAIN", "MISSING_EVIDENCE"),
    "policy_denial": ("DENY", "POLICY_DENIED"),
    "stale_dependency": ("ABSTAIN", "SOURCE_STALE"),
    "dependency_unavailable": ("ERROR", "DEPENDENCY_UNAVAILABLE"),
    "timeout": ("ERROR", "REQUEST_TIMEOUT"),
    "cancellation": ("ABSTAIN", "REQUEST_CANCELLED"),
    "invalid_response": ("ERROR", "INVALID_RESPONSE"),
    "internal_defect": ("ERROR", "SAFE_RUNTIME_ERROR"),
}


def _issued_at() -> str:
    return os.getenv("GOVERNED_API_ISSUED_AT") or datetime.now(timezone.utc).isoformat()


def make_abstain_envelope(route: str) -> dict:
    route_id = route.removeprefix("/")
    return {
        "id": f"stub:{route_id}",
        "spec_hash": _STUB_SPEC_HASH,
        "version": "v1-stub",
        "issued_at": _issued_at(),
        "outcome": "ABSTAIN",
        "reason_code": "NOT_IMPLEMENTED",
        "evidence_refs": [],
        "policy_state": "baseline",
        "freshness": "current",
        "correction_state": "none",
    }


def make_error_envelope(error_id: str) -> dict:
    """Return the schema-backed fail-closed ERROR shape used by the scaffold."""

    return {
        "id": f"stub:error:{error_id}",
        "spec_hash": _STUB_SPEC_HASH,
        "version": "v1-stub",
        "issued_at": _issued_at(),
        "outcome": "ERROR",
        "reason_code": "SAFE_RUNTIME_ERROR",
        "evidence_refs": [],
        "policy_state": "unknown_fail_closed",
        "freshness": "unknown_fail_closed",
        "correction_state": "none",
    }


def make_fixture_failure_envelope(kind: str, correlation_id: str) -> dict:
    """Translate one deterministic negative fixture without adding a route.

    The existing RuntimeResponseEnvelope schema has no correlation field.
    The safe fixture identifier is therefore bound to its existing id field,
    and untrusted correlation input is replaced with unavailable.
    """

    try:
        outcome, reason_code = _FAILURE_PROFILE[kind]
    except KeyError as exc:
        raise ValueError(f"unknown fixture failure kind: {kind}") from exc

    candidate = correlation_id.strip() if isinstance(correlation_id, str) else ""
    safe_correlation = candidate if _SAFE_CORRELATION_ID.fullmatch(candidate) else "unavailable"
    policy_state = "denied" if outcome == "DENY" else "unknown_fail_closed"
    freshness = "stale" if kind == "stale_dependency" else "unknown_fail_closed"
    return {
        "id": f"fixture:failure:{kind}:{safe_correlation}",
        "spec_hash": _STUB_SPEC_HASH,
        "version": "v1-stub-fixture",
        "issued_at": _issued_at(),
        "outcome": outcome,
        "reason_code": reason_code,
        "evidence_refs": [],
        "policy_state": policy_state,
        "freshness": freshness,
        "correction_state": "none",
    }


def _has_closed_negative_shape(payload: object) -> bool:
    """Apply the scaffold's bounded negative-envelope guard.

    This is intentionally narrower than the canonical JSON Schema validator:
    the current route registry cannot emit ANSWER, and runtime code does not
    acquire a validator dependency. Schema validation remains the test and CI
    authority for the complete RuntimeResponseEnvelope shape.
    """

    if not isinstance(payload, dict) or set(payload) != _NEGATIVE_ENVELOPE_KEYS:
        return False
    if payload.get("outcome") not in _NEGATIVE_OUTCOMES:
        return False
    if not isinstance(payload.get("id"), str) or not _SAFE_ENVELOPE_ID.fullmatch(payload["id"]):
        return False
    if not isinstance(payload.get("spec_hash"), str) or not _SAFE_SPEC_HASH.fullmatch(payload["spec_hash"]):
        return False
    if payload.get("evidence_refs") != []:
        return False
    version = payload.get("version")
    reason_code = payload.get("reason_code")
    if not isinstance(version, str) or not _SAFE_VERSION.fullmatch(version):
        return False
    if not isinstance(reason_code, str) or not _SAFE_REASON_CODE.fullmatch(reason_code):
        return False
    if any(
        not isinstance(payload.get(field), str) or not _SAFE_STATE.fullmatch(payload[field])
        for field in ("policy_state", "freshness", "correction_state")
    ):
        return False
    issued_at = payload.get("issued_at")
    if not isinstance(issued_at, str):
        return False
    try:
        parsed_issued_at = datetime.fromisoformat(issued_at.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed_issued_at.tzinfo is not None


def _resolve_fixture_result(result: object, correlation_id: str) -> tuple[dict, str | None]:
    if _has_closed_negative_shape(result):
        return result, None
    return make_fixture_failure_envelope("invalid_response", correlation_id), "invalid_response"


def invoke_sync_fixture_operation(operation, correlation_id: str) -> tuple[dict, str | None]:
    """Invoke one synchronous scaffold operation and fail closed.

    The second tuple item is a safe failure class for transport selection. It
    is ``None`` only when the operation returned a closed negative envelope.
    """

    try:
        result = operation()
    except asyncio.CancelledError:
        return make_fixture_failure_envelope("cancellation", correlation_id), "cancellation"
    except TimeoutError:
        return make_fixture_failure_envelope("timeout", correlation_id), "timeout"
    except Exception:
        return make_fixture_failure_envelope("internal_defect", correlation_id), "internal_defect"

    if inspect.isawaitable(result):
        close = getattr(result, "close", None)
        if callable(close):
            close()
        return make_fixture_failure_envelope("invalid_response", correlation_id), "invalid_response"
    return _resolve_fixture_result(result, correlation_id)


async def invoke_fixture_operation(operation, correlation_id: str) -> tuple[dict, str | None]:
    """Exercise synchronous or asynchronous negative paths without I/O."""

    try:
        result = operation()
        if inspect.isawaitable(result):
            result = await result
    except asyncio.CancelledError:
        return make_fixture_failure_envelope("cancellation", correlation_id), "cancellation"
    except TimeoutError:
        return make_fixture_failure_envelope("timeout", correlation_id), "timeout"
    except Exception:
        return make_fixture_failure_envelope("internal_defect", correlation_id), "internal_defect"
    return _resolve_fixture_result(result, correlation_id)
