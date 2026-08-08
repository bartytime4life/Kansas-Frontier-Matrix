"""Conservative projection from evidence-candidate status to runtime posture.

This module prevents the internal resolver status ``RESOLVED`` from being
misread as a public ``ANSWER`` or render authorization. It performs no I/O,
policy evaluation, review, release lookup, citation validation, or publication.
"""

from __future__ import annotations

import json
from dataclasses import dataclass

from .core import ResolutionCandidate


STATUS_TO_DISPOSITION = {
    "RESOLVED": ("CONTINUE_GOVERNED_CHECKS", "candidate/resolved"),
    "UNRESOLVED": ("ABSTAIN", "evidence/unresolved"),
    "DENIED": ("DENY", "evidence/denied"),
    "ERROR": ("ERROR", "evidence/error"),
}

REQUIRED_NEXT_CHECKS = (
    "evidence_authority",
    "rights",
    "sensitivity",
    "policy",
    "review",
    "release",
    "citation",
    "correction",
)

LIMITATIONS = (
    "not_a_public_answer",
    "not_render_authority",
    "not_policy_clearance",
    "not_review_or_release_approval",
    "not_publication_authority",
)


@dataclass(frozen=True)
class RuntimePosture:
    """Internal, non-authoritative next-step projection."""

    candidate_status: str
    disposition: str
    reason_code: str
    bundle_id: str | None
    required_next_checks: tuple[str, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "candidate_status": self.candidate_status,
            "disposition": self.disposition,
            "authoritative": False,
            "renderable": False,
            "bundle_id": self.bundle_id,
            "reason_code": self.reason_code,
            "required_next_checks": list(self.required_next_checks),
            "limitations": list(LIMITATIONS),
        }


def project_runtime_posture(result: ResolutionCandidate) -> RuntimePosture:
    """Project a candidate result without granting public-answer authority.

    ``RESOLVED`` may continue to the remaining governed checks. Every other
    candidate status maps to a finite fail-closed runtime posture. Candidate
    shape inconsistencies raise ``ValueError`` rather than being normalized.
    """

    if result.status not in STATUS_TO_DISPOSITION:
        raise ValueError("candidate/status-unsupported")

    if result.status == "RESOLVED":
        if result.bundle_id is None:
            raise ValueError("candidate/resolved-bundle-missing")
        next_checks = REQUIRED_NEXT_CHECKS
        bundle_id = result.bundle_id
    else:
        if result.bundle_id is not None:
            raise ValueError("candidate/nonresolved-bundle-present")
        next_checks = ()
        bundle_id = None

    disposition, reason_code = STATUS_TO_DISPOSITION[result.status]
    return RuntimePosture(
        candidate_status=result.status,
        disposition=disposition,
        reason_code=reason_code,
        bundle_id=bundle_id,
        required_next_checks=next_checks,
    )


def posture_json(posture: RuntimePosture) -> str:
    """Serialize the projection deterministically for tests and adapters."""

    return json.dumps(
        posture.as_dict(),
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    )
