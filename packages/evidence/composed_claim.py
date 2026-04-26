from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from .evidence_ref_resolver import (
    APPROVED_RELEASE_STATES,
    ERROR_CODES as REF_ERROR_CODES,
    load_json,
    resolve_evidence_ref,
    EvidenceRefResult,
)


ERROR_CODES = {
    "schema_invalid": "CLAIM_SCHEMA_INVALID",
    "evidence_ref_unresolved": "CLAIM_EVIDENCE_REF_UNRESOLVED",
    "composed_ref_unresolved": "CLAIM_COMPOSED_REF_UNRESOLVED",
    "render_mismatch": "CLAIM_RENDER_MISMATCH",
    "internal_error": "CLAIM_INTERNAL_ERROR",
}


@dataclass(frozen=True)
class ComposedClaimResult:
    render: bool
    decision: str
    claim_id: str
    unresolved_refs: list[str]
    unresolved_evidence_refs: list[str]
    error_code: str | None
    reason: str | None


def validate_claim_envelope_schema(
    *,
    claim_envelope: dict[str, Any],
    schema_path: Path,
) -> list[str]:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    return [
        f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
        for error in sorted(
            validator.iter_errors(claim_envelope),
            key=lambda item: list(item.path),
        )
    ]


def resolve_composed_claim(
    *,
    claim_envelope: dict[str, Any],
    claim_schema_path: Path,
    evidence_ref_schema_path: Path,
    resolved_claim_ids: set[str] | None = None,
) -> ComposedClaimResult:
    """
    Resolve a ClaimEnvelope, checking that all required evidence_refs and
    composed_claim_refs are resolved.

    Core invariant:
    - all required composed-claim refs resolved -> render=true
    - any required composed-claim ref unresolved -> render=false
    """
    if resolved_claim_ids is None:
        resolved_claim_ids = set()

    claim_id = claim_envelope.get("claim_id", "<unknown>")

    schema_errors = validate_claim_envelope_schema(
        claim_envelope=claim_envelope,
        schema_path=claim_schema_path,
    )

    if schema_errors:
        return ComposedClaimResult(
            render=False,
            decision="abstain",
            claim_id=claim_id,
            unresolved_refs=[],
            unresolved_evidence_refs=[],
            error_code=ERROR_CODES["schema_invalid"],
            reason=f"claim_envelope schema invalid: {schema_errors[0]}",
        )

    evidence_refs = claim_envelope.get("evidence_refs", [])
    composed_claim_refs = claim_envelope.get("composed_claim_refs", [])

    unresolved_evidence_refs: list[str] = []

    for ref_obj in evidence_refs:
        if not isinstance(ref_obj, dict):
            unresolved_evidence_refs.append("<non-object evidence_ref>")
            continue

        result = resolve_evidence_ref(
            evidence_ref=ref_obj,
            schema_path=evidence_ref_schema_path,
        )

        if not result.render:
            unresolved_evidence_refs.append(result.evidence_ref_id)

    unresolved_composed_refs: list[str] = []

    for ref_id in composed_claim_refs:
        if ref_id not in resolved_claim_ids:
            unresolved_composed_refs.append(ref_id)

    all_resolved = (
        not unresolved_evidence_refs and not unresolved_composed_refs
    )

    if not all_resolved:
        unresolved_all = unresolved_evidence_refs + unresolved_composed_refs
        return ComposedClaimResult(
            render=False,
            decision="abstain",
            claim_id=claim_id,
            unresolved_refs=unresolved_composed_refs,
            unresolved_evidence_refs=unresolved_evidence_refs,
            error_code=(
                ERROR_CODES["composed_ref_unresolved"]
                if unresolved_composed_refs
                else ERROR_CODES["evidence_ref_unresolved"]
            ),
            reason=f"unresolved refs: {unresolved_all}",
        )

    return ComposedClaimResult(
        render=True,
        decision="cite",
        claim_id=claim_id,
        unresolved_refs=[],
        unresolved_evidence_refs=[],
        error_code=None,
        reason=None,
    )
