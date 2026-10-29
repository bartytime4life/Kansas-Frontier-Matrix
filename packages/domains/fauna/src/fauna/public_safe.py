"""Allowlisted internal review projection; no public release path."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping

from .validation import Finding, validate_candidate


@dataclass(frozen=True)
class ProjectionResult:
    outcome: str
    payload: dict[str, Any] | None = field(default=None, repr=False)
    findings: tuple[Finding, ...] = ()


def prepare_public_candidate(
    candidate: object, *, schema: Mapping[str, Any]
) -> ProjectionResult:
    """Prepare metadata for internal review of a non-sensitive candidate only.

    All held, sensitive, obscured and private occurrences produce no payload.
    Even the positive case has no geometry, date, observer, source identifiers,
    free text or links, and is explicitly unreleased. This is not an
    OccurrencePublic object, a geoprivacy transform or a release decision.
    """
    checked = validate_candidate(candidate, schema=schema)
    if not checked.ok:
        return ProjectionResult("ERROR", findings=checked.findings)
    assert isinstance(candidate, Mapping)
    sensitivity = candidate["sensitivity"]
    geometry = candidate["geometry"]
    if (
        candidate["validation"]["validator_result"] != "pass"
        or candidate["source_role"] == "candidate"
        or candidate["rights"]["redistribution_allowed"] is not True
    ):
        return ProjectionResult("HOLD")
    if (
        sensitivity["sensitive_species_flag"]
        or sensitivity["review_required"]
        or sensitivity["withhold_required"]
        or sensitivity["generalization_required"]
        or geometry["geoprivacy_status"] != "open"
        or not sensitivity["exact_location_public_safe"]
    ):
        return ProjectionResult("WITHHELD")
    return ProjectionResult("CANDIDATE", {
        "object_type": "fauna_review_candidate",
        "publication_state": "unreleased",
        "audience": "internal",
        "source_role": candidate["source_role"],
        "accepted_scientific_name": candidate["taxon"]["accepted_scientific_name"],
        "taxon_rank": candidate["taxon"]["taxon_rank"],
        "geometry": None,
        "evidence_state": "not_resolved_by_helper",
        "release_state": "not_verified",
    })
