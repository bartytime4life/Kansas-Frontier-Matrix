"""Test-only soil-moisture candidate-to-runtime-envelope mapping.

This module proves a bounded outward mapping over the existing synthetic fixture
validator. It is not a production route, source adapter, evidence resolver,
policy engine, release gate, or publisher. The current fixture profile is
explicitly ``fixture_only`` and ``not_released``; therefore this mapper never
returns ``ANSWER``.
"""

from __future__ import annotations

import hashlib
import json

from envelopes import build_runtime_response_candidate
from tools.validators.domains.soil.moisture.validate_soil_moisture import (
    Finding,
    validate_candidate,
)


PROFILE_VERSION = "soil-moisture-runtime-proof-v1"
PROFILE_SPEC_HASH = "sha256:" + hashlib.sha256(
    b"kfm:runtime-proof:soil-moisture-fixture:v1"
).hexdigest()
SUPPORT_INCOMPLETE_CODES = frozenset(
    {
        "EVIDENCE_REFS_INVALID",
        "SOURCE_DESCRIPTOR_REF_MISSING",
        "RUN_RECEIPT_REF_MISSING",
    }
)


def _canonical_digest(candidate: object) -> str:
    try:
        encoded = json.dumps(
            candidate,
            allow_nan=False,
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError, RecursionError):
        encoded = f"unsupported:{type(candidate).__name__}".encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _response_id(candidate: object) -> str:
    return f"runtime:soil-moisture:{_canonical_digest(candidate)[:24]}"


def _project_evidence_refs(candidate: object) -> list[dict[str, str]]:
    if not isinstance(candidate, dict):
        return []
    raw_refs = candidate.get("evidence_refs")
    if not isinstance(raw_refs, list):
        return []

    projected: list[dict[str, str]] = []
    seen: set[str] = set()
    for raw_ref in raw_refs:
        if not isinstance(raw_ref, str) or not raw_ref.strip() or raw_ref in seen:
            continue
        seen.add(raw_ref)
        projected.append({"ref": raw_ref, "kind": "measurement"})
    return projected


def _classify(findings: list[Finding]) -> tuple[str, str, str, str]:
    if any(finding.code == "CANDIDATE_NOT_OBJECT" for finding in findings):
        return (
            "ERROR",
            "SOIL_MOISTURE_INPUT_ERROR",
            "runtime_error",
            "not_evaluated",
        )
    if findings and all(
        finding.code in SUPPORT_INCOMPLETE_CODES for finding in findings
    ):
        return (
            "ABSTAIN",
            "SOIL_MOISTURE_SUPPORT_INCOMPLETE",
            "support_incomplete",
            "not_evaluated",
        )
    if findings:
        return (
            "DENY",
            "SOIL_MOISTURE_VALIDATION_DENIED",
            "validation_denied",
            "not_evaluated",
        )
    return (
        "ABSTAIN",
        "SOIL_MOISTURE_FIXTURE_NOT_RELEASED",
        "fixture_only_not_released",
        "fixture_only",
    )


def build_soil_moisture_runtime_response(
    candidate: object,
    *,
    issued_at: str,
) -> dict[str, object]:
    """Map one decoded candidate to a closed fixture-only runtime envelope."""

    findings = validate_candidate(candidate)
    outcome, reason_code, policy_state, freshness = _classify(findings)
    evidence_refs = (
        _project_evidence_refs(candidate)
        if outcome == "ABSTAIN" and reason_code == "SOIL_MOISTURE_FIXTURE_NOT_RELEASED"
        else []
    )

    return build_runtime_response_candidate(
        response_id=_response_id(candidate),
        spec_hash=PROFILE_SPEC_HASH,
        version=PROFILE_VERSION,
        issued_at=issued_at,
        outcome=outcome,
        reason_code=reason_code,
        evidence_refs=evidence_refs,
        policy_state=policy_state,
        freshness=freshness,
        correction_state="not_applicable",
    )


__all__ = [
    "PROFILE_SPEC_HASH",
    "PROFILE_VERSION",
    "build_soil_moisture_runtime_response",
]
