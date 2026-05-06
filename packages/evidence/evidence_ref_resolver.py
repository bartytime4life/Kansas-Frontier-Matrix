from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


APPROVED_RELEASE_STATES = {"PUBLISHED", "CATALOG"}

ERROR_CODES = {
    "missing": "EVREF_MISSING",
    "invalid_schema": "EVREF_INVALID_SCHEMA",
    "release_state_not_approved": "EVREF_RELEASE_STATE_NOT_APPROVED",
    "digest_mismatch": "EVREF_DIGEST_MISMATCH",
    "approval_required": "EVREF_APPROVAL_REQUIRED",
    "internal_error": "EVREF_INTERNAL_ERROR",
}


@dataclass(frozen=True)
class EvidenceRefResult:
    render: bool
    decision: str
    error_code: str | None
    reason: str | None
    evidence_ref_id: str
    release_state: str | None = None


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(value, dict):
        raise ValueError("EvidenceRef document must be a JSON object.")

    return value


def validate_evidence_ref_schema(
    *,
    evidence_ref: dict[str, Any],
    schema_path: Path,
) -> list[str]:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    return [
        f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
        for error in sorted(
            validator.iter_errors(evidence_ref),
            key=lambda item: list(item.path),
        )
    ]


def resolve_evidence_ref(
    *,
    evidence_ref: dict[str, Any],
    schema_path: Path,
    expected_digest: str | None = None,
) -> EvidenceRefResult:
    """
    Resolve a single EvidenceRef object.

    Core invariant:
    - valid promoted evidence (PUBLISHED or CATALOG) -> render allowed
    - missing / invalid / mismatched / unapproved evidence -> abstain
    """
    evidence_ref_id = evidence_ref.get("evidence_ref_id", "<unknown>")

    schema_errors = validate_evidence_ref_schema(
        evidence_ref=evidence_ref,
        schema_path=schema_path,
    )

    if schema_errors:
        return EvidenceRefResult(
            render=False,
            decision="abstain",
            error_code=ERROR_CODES["invalid_schema"],
            reason=f"evidence_ref schema invalid: {schema_errors[0]}",
            evidence_ref_id=evidence_ref_id,
        )

    release_state = evidence_ref.get("release_state")

    if release_state not in APPROVED_RELEASE_STATES:
        return EvidenceRefResult(
            render=False,
            decision="abstain",
            error_code=ERROR_CODES["release_state_not_approved"],
            reason=f"release_state not approved for public citation: {release_state}",
            evidence_ref_id=evidence_ref_id,
            release_state=release_state,
        )

    if expected_digest is not None:
        actual_digest = evidence_ref.get("digest")
        if actual_digest != expected_digest:
            return EvidenceRefResult(
                render=False,
                decision="abstain",
                error_code=ERROR_CODES["digest_mismatch"],
                reason="evidence_ref digest does not match expected digest",
                evidence_ref_id=evidence_ref_id,
                release_state=release_state,
            )

    return EvidenceRefResult(
        render=True,
        decision="cite",
        error_code=None,
        reason=None,
        evidence_ref_id=evidence_ref_id,
        release_state=release_state,
    )


def resolve_evidence_ref_from_file(
    *,
    evidence_ref_path: Path,
    schema_path: Path,
    expected_digest: str | None = None,
) -> EvidenceRefResult:
    """
    Resolve an EvidenceRef from a file path.

    Returns abstain if the file is missing or unparseable.
    """
    if not evidence_ref_path.exists():
        return EvidenceRefResult(
            render=False,
            decision="abstain",
            error_code=ERROR_CODES["missing"],
            reason=f"evidence_ref file not found: {evidence_ref_path}",
            evidence_ref_id=str(evidence_ref_path),
        )

    try:
        evidence_ref = load_json(evidence_ref_path)
    except Exception:
        return EvidenceRefResult(
            render=False,
            decision="abstain",
            error_code=ERROR_CODES["internal_error"],
            reason=f"could not load evidence_ref file: {evidence_ref_path}",
            evidence_ref_id=str(evidence_ref_path),
        )

    return resolve_evidence_ref(
        evidence_ref=evidence_ref,
        schema_path=schema_path,
        expected_digest=expected_digest,
    )
