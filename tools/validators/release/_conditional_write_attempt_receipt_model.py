"""Build fixture-only conditional-write attempt receipt candidates.

This module consumes an exact preflight candidate and a declared transcript. It
contacts no target and authenticates no request, response, write, lifecycle,
release, publication, or public-use effect.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
for candidate_path in (REPO_ROOT, REPO_ROOT / "packages/hashing/src"):
    if str(candidate_path) not in sys.path:
        sys.path.insert(0, str(candidate_path))

from hashing import CanonicalizationFailure, compute_spec_hash
from tools.validators.release._conditional_write_preflight_model import (
    build_candidate as build_preflight_candidate,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/conditional_write_attempt_receipt.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/release/conditional_write_attempt_receipt"
CASES_PATH = FIXTURE_ROOT / "cases.json"
VALID_PATH = FIXTURE_ROOT / "valid/valid_applied.json"
INVALID_PATH = FIXTURE_ROOT / "invalid/invalid_authority_overreach.json"
PROFILE = "kfm.release.conditional-write-attempt-receipt.v1"
OBJECT_TYPE = "ConditionalWriteAttemptReceiptCandidate"
EXECUTION_MODE = "FIXTURE_ONLY_DECLARATION"
SCOPE = "release.conditional_write_attempt_receipt_candidate"
NON_EFFECTS = (
    "no_network_access",
    "no_external_state_authentication",
    "no_request_or_write_execution",
    "no_lifecycle_mutation",
    "no_release_deployment_publication_or_public_use",
)

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str

@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    receipt_id: str | None = None

def _mapping(value: object, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{label} must be an object")
    return value

def _string(value: object, label: str, *, optional: bool = False) -> str | None:
    if optional and value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")
    return value.strip()

def _integer(value: object, label: str, *, optional: bool = False) -> int | None:
    if optional and value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{label} must be an integer")
    return value

def _attempt_fingerprint(preflight: Mapping[str, Any], attempt: Mapping[str, Any]) -> str:
    return compute_spec_hash(
        {
            "preflight_intent_id": preflight["intent_id"],
            "preflight_spec_hash": preflight["spec_hash"],
            "target_ref": preflight["target"]["target_ref"],
            "condition_fingerprint": preflight["preflight"]["condition_fingerprint"],
            "idempotency_key": preflight["request"]["idempotency_key"],
            "attempt": attempt,
        }
    )

def _empty_wire(attempt: Mapping[str, Any]) -> bool:
    return (
        attempt["transport"] == "NONE"
        and attempt["request_emitted"] is False
        and attempt["method"] is None
        and attempt["request_headers"] == {"if_match": None, "if_none_match": None}
        and attempt["request_content_digest"] is None
        and attempt["request_content_length"] is None
        and attempt["response_status"] is None
        and attempt["response_etag"] is None
        and attempt["response_content_digest"] is None
        and attempt["transport_error"] is None
    )

def _after_state_coherent(after: Mapping[str, Any]) -> bool:
    state = after["state"]
    if state == "PRESENT":
        return after["etag"] is not None and after["content_digest"] is not None
    return after["etag"] is None and after["content_digest"] is None

def derive_result(preflight: Mapping[str, Any], attempt: Mapping[str, Any]) -> dict[str, object]:
    if not _after_state_coherent(_mapping(attempt["after_state"], "attempt.after_state")):
        outcome, reasons = "ERROR", ["RESPONSE_INCONSISTENT"]
    else:
        preflight_outcome = preflight["preflight"]["outcome"]
        after = attempt["after_state"]
        request = preflight["request"]
        expected_headers = preflight["preflight"]["request_headers"]

        if preflight_outcome == "HOLD":
            coherent = _empty_wire(attempt) and after["state"] == "UNKNOWN"
            outcome, reasons = (("HOLD", ["UPSTREAM_HOLD"]) if coherent else ("ERROR", ["REQUEST_DECLARATION_MISMATCH"]))
        elif preflight_outcome == "CONFLICT":
            observed = preflight["target"]
            expected_after = {
                "state": observed["observed_state"],
                "etag": observed["observed_etag"],
                "content_digest": observed["observed_content_digest"],
            }
            coherent = _empty_wire(attempt) and after == expected_after
            outcome, reasons = (("CONFLICT", ["PREFLIGHT_CONFLICT"]) if coherent else ("ERROR", ["REQUEST_DECLARATION_MISMATCH"]))
        elif preflight_outcome == "NO_ACTION":
            coherent = (
                _empty_wire(attempt)
                and after["state"] == "PRESENT"
                and after["content_digest"] == request["proposed_content_digest"]
            )
            outcome, reasons = (("NO_ACTION", ["CONTENT_ALREADY_PRESENT"]) if coherent else ("ERROR", ["RESPONSE_INCONSISTENT"]))
        else:
            request_matches = (
                attempt["request_emitted"] is True
                and attempt["transport"] in {"HTTP", "OBJECT_STORE"}
                and attempt["method"] == "PUT"
                and attempt["request_headers"] == expected_headers
                and attempt["request_content_digest"] == request["proposed_content_digest"]
                and attempt["request_content_length"] == request["proposed_content_length"]
            )
            if not request_matches:
                outcome, reasons = "ERROR", ["ATTEMPT_NOT_RECORDED" if attempt["request_emitted"] is False else "REQUEST_DECLARATION_MISMATCH"]
            elif attempt["transport_error"] is not None:
                coherent = (
                    attempt["response_status"] is None
                    and attempt["response_etag"] is None
                    and attempt["response_content_digest"] is None
                    and after["state"] == "UNKNOWN"
                )
                outcome, reasons = (("ERROR", ["TRANSPORT_ERROR"]) if coherent else ("ERROR", ["RESPONSE_INCONSISTENT"]))
            elif attempt["response_status"] in {409, 412}:
                coherent = (
                    attempt["response_etag"] is None
                    and attempt["response_content_digest"] is None
                    and after["state"] == "UNKNOWN"
                )
                outcome, reasons = (("CONFLICT", ["PRECONDITION_FAILED"]) if coherent else ("ERROR", ["RESPONSE_INCONSISTENT"]))
            elif attempt["response_status"] in {200, 201, 204}:
                coherent = (
                    attempt["response_etag"] is not None
                    and attempt["response_content_digest"] == request["proposed_content_digest"]
                    and after["state"] == "PRESENT"
                    and after["etag"] == attempt["response_etag"]
                    and after["content_digest"] == request["proposed_content_digest"]
                )
                outcome, reasons = (("APPLIED", ["WRITE_APPLIED"]) if coherent else ("ERROR", ["RESPONSE_INCONSISTENT"]))
            else:
                outcome, reasons = "ERROR", ["RESPONSE_INCONSISTENT"]

    return {
        "outcome": outcome,
        "reason_codes": reasons,
        "attempt_fingerprint": _attempt_fingerprint(preflight, attempt),
    }

def build_candidate(case: Mapping[str, Any]) -> dict[str, object]:
    preflight = build_preflight_candidate(_mapping(case.get("preflight_case"), "preflight_case"))
    raw = _mapping(case.get("attempt"), "attempt")
    headers = _mapping(raw.get("request_headers"), "attempt.request_headers")
    after = _mapping(raw.get("after_state"), "attempt.after_state")
    attempt = {
        "attempted_at": _string(raw.get("attempted_at"), "attempt.attempted_at"),
        "adapter_id": _string(raw.get("adapter_id"), "attempt.adapter_id"),
        "transport": _string(raw.get("transport"), "attempt.transport"),
        "request_emitted": raw.get("request_emitted"),
        "method": _string(raw.get("method"), "attempt.method", optional=True),
        "request_headers": {
            "if_match": _string(headers.get("if_match"), "attempt.request_headers.if_match", optional=True),
            "if_none_match": _string(headers.get("if_none_match"), "attempt.request_headers.if_none_match", optional=True),
        },
        "request_content_digest": _string(raw.get("request_content_digest"), "attempt.request_content_digest", optional=True),
        "request_content_length": _integer(raw.get("request_content_length"), "attempt.request_content_length", optional=True),
        "response_status": _integer(raw.get("response_status"), "attempt.response_status", optional=True),
        "response_etag": _string(raw.get("response_etag"), "attempt.response_etag", optional=True),
        "response_content_digest": _string(raw.get("response_content_digest"), "attempt.response_content_digest", optional=True),
        "transport_error": _string(raw.get("transport_error"), "attempt.transport_error", optional=True),
        "after_state": {
            "state": _string(after.get("state"), "attempt.after_state.state"),
            "etag": _string(after.get("etag"), "attempt.after_state.etag", optional=True),
            "content_digest": _string(after.get("content_digest"), "attempt.after_state.content_digest", optional=True),
        },
    }
    if not isinstance(attempt["request_emitted"], bool):
        raise ValueError("attempt.request_emitted must be Boolean")
    candidate: dict[str, Any] = {
        "schema_version": "1.0.0",
        "object_type": OBJECT_TYPE,
        "profile": PROFILE,
        "execution_mode": EXECUTION_MODE,
        "receipt_id": "",
        "preflight_candidate": preflight,
        "attempt": attempt,
        "result": derive_result(preflight, attempt),
        "spec_hash": "",
        "claims": {
            "deterministic_assessment": True,
            "validator_network_accessed": False,
            "external_state_authenticated": False,
            "preflight_authority_verified": False,
            "subject_execution_authenticated": False,
            "write_verified": False,
            "lifecycle_write_verified": False,
            "release_created": False,
            "published": False,
            "public_use_authorized": False,
        },
    }
    projection = {key: value for key, value in candidate.items() if key not in {"receipt_id", "spec_hash"}}
    try:
        digest = compute_spec_hash(projection)
    except CanonicalizationFailure as exc:
        raise ValueError("receipt candidate could not be canonicalized") from exc
    candidate["spec_hash"] = digest
    candidate["receipt_id"] = "kfm:conditional-write-attempt-receipt:" + digest.removeprefix("sha256:")
    return candidate
