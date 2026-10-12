#!/usr/bin/env python3
"""Validate the frozen synthetic Geology resource-class fixture profile.

This validator proves a narrow anti-collapse and public-safety boundary for
repository fixtures. It does not define a canonical resource-classification
scheme, certify a deposit, estimate or reserve, resolve evidence, evaluate
policy, admit a source, or authorize promotion, release or publication.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import sys
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    find_undeclared_fields,
    is_nonempty_string,
    run_cli,
    validate_fixture_file,
)


PROFILE_ID = "kfm-geology-resource-class-fixture-v1"
MAX_EVIDENCE_REFS = 32
MAX_ASSUMPTION_REFS = 32
MAX_LIMITATIONS = 32

ALLOWED_TOP_LEVEL_FIELDS = frozenset(
    {
        "fixture_id",
        "profile_id",
        "object_family",
        "resource_character",
        "source_role",
        "source_descriptor_ref",
        "evidence_refs",
        "claim",
        "spatial_support",
        "governance",
        "limitations",
    }
)
ALLOWED_CLAIM_FIELDS = frozenset(
    {
        "kind",
        "commodity",
        "intended_use",
        "classification_scheme_ref",
        "method_ref",
        "estimate_date",
        "confidence_class",
        "assumption_refs",
    }
)
ALLOWED_SPATIAL_SUPPORT_FIELDS = frozenset({"kind", "county_fips"})
ALLOWED_GOVERNANCE_FIELDS = frozenset(
    {
        "rights_state",
        "sensitivity_state",
        "review_state",
        "release_state",
        "promotion_eligible",
        "rollback_state",
    }
)
FORBIDDEN_LOCATION_ALIASES = frozenset(
    {
        "lat",
        "latitude",
        "lon",
        "lng",
        "longitude",
        "x",
        "y",
        "bbox",
        "centroid",
        "coordinates",
        "easting",
        "northing",
        "site_coordinates",
        "mine_coordinates",
        "borehole_coordinates",
    }
)
EXPECTED_GOVERNANCE = {
    "rights_state": "fixture_only",
    "sensitivity_state": "public_safe_fixture",
    "review_state": "fixture_only",
    "release_state": "not_released",
    "promotion_eligible": False,
    "rollback_state": "fixture_only",
}


@dataclass(frozen=True)
class FixtureResourceRule:
    """One non-authoritative pairing in the frozen synthetic profile."""

    object_family: str
    source_role: str
    claim_kind: str
    intended_use: str
    limitations: frozenset[str]
    requires_estimate_support: bool = False


FIXTURE_RESOURCE_RULES = {
    "MINERAL_OCCURRENCE": FixtureResourceRule(
        object_family="MineralOccurrence",
        source_role="observed",
        claim_kind="reported_presence",
        intended_use="occurrence_context",
        limitations=frozenset(
            {
                "not_a_deposit",
                "not_an_estimate",
                "not_a_reserve",
                "synthetic_fixture_only",
            }
        ),
    ),
    "RESOURCE_DEPOSIT": FixtureResourceRule(
        object_family="ResourceDeposit",
        source_role="aggregate",
        claim_kind="delineated_body",
        intended_use="deposit_context",
        limitations=frozenset(
            {
                "not_an_estimate",
                "not_a_permit_or_ownership_record",
                "not_a_reserve",
                "synthetic_fixture_only",
            }
        ),
    ),
    "RESOURCE_ESTIMATE": FixtureResourceRule(
        object_family="ResourceEstimate",
        source_role="modeled",
        claim_kind="modeled_quantity",
        intended_use="estimate_context",
        limitations=frozenset(
            {
                "not_direct_observation",
                "not_economic_viability",
                "not_a_reserve",
                "synthetic_fixture_only",
            }
        ),
        requires_estimate_support=True,
    ),
}


def _string_list_is_valid(value: object, *, maximum: int) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and len(value) <= maximum
        and all(is_nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


def _resource_character(
    candidate: dict[object, object], findings: set[Finding]
) -> str | None:
    value = candidate.get("resource_character")
    if "resource_character" not in candidate:
        add_finding(
            findings,
            "RESOURCE_CHARACTER_MISSING",
            "$.resource_character",
        )
        return None
    if isinstance(value, list) and len(value) > 1:
        add_finding(
            findings,
            "RESOURCE_CHARACTER_MULTIPLE",
            "$.resource_character",
        )
        return None
    if not is_nonempty_string(value):
        add_finding(
            findings,
            "RESOURCE_CHARACTER_INVALID",
            "$.resource_character",
        )
        return None
    if value not in FIXTURE_RESOURCE_RULES:
        add_finding(
            findings,
            "RESOURCE_CHARACTER_UNKNOWN",
            "$.resource_character",
        )
        return None
    return value


def _collapse_code(
    resource_character: str,
    source_role: object,
    claim: dict[object, object],
) -> str | None:
    kind = claim.get("kind")
    intended_use = claim.get("intended_use")

    if kind in {"reserve", "proven_reserve", "probable_reserve"} or (
        intended_use == "reserve_certification"
    ):
        return "RESERVE_CLAIM_DENIED"
    if resource_character == "MINERAL_OCCURRENCE" and (
        kind in {"delineated_body", "modeled_quantity"}
        or intended_use in {"deposit_context", "estimate_context"}
    ):
        return "OCCURRENCE_AS_RESOURCE_DENIED"
    if resource_character == "RESOURCE_DEPOSIT" and (
        source_role == "modeled" or kind == "modeled_potential"
    ):
        return "MODELED_POTENTIAL_AS_DEPOSIT_DENIED"
    if resource_character == "RESOURCE_DEPOSIT" and (
        kind == "production_record" or intended_use == "physical_deposit_proof"
    ):
        return "PRODUCTION_AS_DEPOSIT_DENIED"
    if resource_character == "RESOURCE_DEPOSIT" and (
        source_role in {"administrative", "regulatory"}
        or kind in {"permit", "permit_authorization"}
    ):
        return "PERMIT_AS_DEPOSIT_DENIED"
    if resource_character == "RESOURCE_ESTIMATE" and (
        source_role == "observed" or kind in {"observation", "direct_observation"}
    ):
        return "ESTIMATE_AS_OBSERVATION_DENIED"
    return None


def _is_iso_date(value: object) -> bool:
    if not is_nonempty_string(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _validate_estimate_support(
    findings: set[Finding],
    claim: dict[object, object],
    resource_character: str,
) -> None:
    estimate_fields = {
        "classification_scheme_ref": "ESTIMATE_CLASSIFICATION_SCHEME_MISSING",
        "method_ref": "ESTIMATE_METHOD_REF_MISSING",
        "confidence_class": "ESTIMATE_CONFIDENCE_CLASS_MISSING",
    }
    if resource_character == "RESOURCE_ESTIMATE":
        for field, code in estimate_fields.items():
            if not is_nonempty_string(claim.get(field)):
                add_finding(findings, code, f"$.claim.{field}")
        if not _is_iso_date(claim.get("estimate_date")):
            add_finding(
                findings,
                "ESTIMATE_DATE_INVALID",
                "$.claim.estimate_date",
            )
        assumption_refs = claim.get("assumption_refs")
        if not _string_list_is_valid(
            assumption_refs, maximum=MAX_ASSUMPTION_REFS
        ):
            code = (
                "ESTIMATE_ASSUMPTION_REF_COUNT_EXCEEDED"
                if isinstance(assumption_refs, list)
                and len(assumption_refs) > MAX_ASSUMPTION_REFS
                else "ESTIMATE_ASSUMPTION_REFS_INVALID"
            )
            add_finding(findings, code, "$.claim.assumption_refs")
        return

    for field in (*estimate_fields, "estimate_date", "assumption_refs"):
        if field in claim:
            add_finding(
                findings,
                "ESTIMATE_SUPPORT_NOT_ALLOWED",
                f"$.claim.{field}",
            )


def _validate_claim(
    findings: set[Finding],
    claim: object,
    source_role: object,
    resource_character: str | None,
) -> None:
    if not isinstance(claim, dict):
        add_finding(findings, "CLAIM_INVALID", "$.claim")
        return

    find_undeclared_fields(
        findings,
        claim,
        ALLOWED_CLAIM_FIELDS,
        "UNDECLARED_CLAIM_FIELD",
        "$.claim",
    )
    if resource_character is None:
        return

    collapse_code = _collapse_code(resource_character, source_role, claim)
    if collapse_code is not None:
        add_finding(findings, collapse_code, "$.claim")
        return

    expected = FIXTURE_RESOURCE_RULES[resource_character]
    for field, expected_value, code in (
        ("kind", expected.claim_kind, "CLAIM_KIND_INVALID"),
        ("commodity", "synthetic_commodity", "CLAIM_COMMODITY_INVALID"),
        (
            "intended_use",
            expected.intended_use,
            "CLAIM_INTENDED_USE_INVALID",
        ),
    ):
        if claim.get(field) != expected_value:
            add_finding(findings, code, f"$.claim.{field}")

    _validate_estimate_support(findings, claim, resource_character)


def _validate_spatial_support(
    findings: set[Finding], spatial_support: object
) -> None:
    if not isinstance(spatial_support, dict):
        add_finding(findings, "SPATIAL_SUPPORT_INVALID", "$.spatial_support")
        return

    find_undeclared_fields(
        findings,
        spatial_support,
        ALLOWED_SPATIAL_SUPPORT_FIELDS,
        "UNDECLARED_SPATIAL_SUPPORT_FIELD",
        "$.spatial_support",
    )
    for key in spatial_support:
        if isinstance(key, str) and key.casefold() in FORBIDDEN_LOCATION_ALIASES:
            add_finding(
                findings,
                "SENSITIVE_RESOURCE_LOCATION_DENIED",
                f"$.spatial_support.{key}",
            )
    spatial_kind = spatial_support.get("kind")
    if spatial_kind in {
        "exact_site",
        "exact_resource_location",
        "point",
        "coordinates",
    }:
        add_finding(
            findings,
            "SENSITIVE_RESOURCE_LOCATION_DENIED",
            "$.spatial_support.kind",
        )
    if spatial_kind != "generalized_county":
        add_finding(
            findings,
            "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE",
            "$.spatial_support.kind",
        )
    county_fips = spatial_support.get("county_fips")
    if (
        not isinstance(county_fips, str)
        or len(county_fips) != 5
        or not county_fips.isascii()
        or not county_fips.isdigit()
    ):
        add_finding(
            findings,
            "COUNTY_FIPS_INVALID",
            "$.spatial_support.county_fips",
        )


def _validate_governance(findings: set[Finding], governance: object) -> None:
    if not isinstance(governance, dict):
        add_finding(findings, "GOVERNANCE_INVALID", "$.governance")
        return

    find_undeclared_fields(
        findings,
        governance,
        ALLOWED_GOVERNANCE_FIELDS,
        "UNDECLARED_GOVERNANCE_FIELD",
        "$.governance",
    )
    for field, expected in EXPECTED_GOVERNANCE.items():
        actual = governance.get(field)
        matches = actual is False if expected is False else actual == expected
        if not matches:
            add_finding(
                findings,
                "GOVERNANCE_STATE_INVALID",
                f"$.governance.{field}",
            )


def validate_candidate(candidate: object) -> list[Finding]:
    """Return sorted, non-echoing findings for one decoded fixture candidate."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("CANDIDATE_NOT_OBJECT", "$")]

    find_undeclared_fields(
        findings,
        candidate,
        ALLOWED_TOP_LEVEL_FIELDS,
        "UNDECLARED_TOP_LEVEL_FIELD",
        "$",
    )
    if not is_nonempty_string(candidate.get("fixture_id")):
        add_finding(findings, "FIXTURE_ID_MISSING", "$.fixture_id")
    if candidate.get("profile_id") != PROFILE_ID:
        add_finding(findings, "PROFILE_ID_INVALID", "$.profile_id")

    resource_character = _resource_character(candidate, findings)
    source_role = candidate.get("source_role")
    if not is_nonempty_string(source_role):
        add_finding(findings, "SOURCE_ROLE_MISSING", "$.source_role")

    if resource_character is not None:
        expected = FIXTURE_RESOURCE_RULES[resource_character]
        if candidate.get("object_family") != expected.object_family:
            add_finding(findings, "OBJECT_FAMILY_INVALID", "$.object_family")
        collapse = _collapse_code(
            resource_character,
            source_role,
            candidate.get("claim") if isinstance(candidate.get("claim"), dict) else {},
        )
        if source_role != expected.source_role and collapse is None:
            add_finding(findings, "SOURCE_ROLE_INVALID", "$.source_role")

    if not is_nonempty_string(candidate.get("source_descriptor_ref")):
        add_finding(
            findings,
            "SOURCE_DESCRIPTOR_REF_MISSING",
            "$.source_descriptor_ref",
        )

    evidence_refs = candidate.get("evidence_refs")
    if not _string_list_is_valid(evidence_refs, maximum=MAX_EVIDENCE_REFS):
        code = (
            "EVIDENCE_REF_COUNT_EXCEEDED"
            if isinstance(evidence_refs, list)
            and len(evidence_refs) > MAX_EVIDENCE_REFS
            else "EVIDENCE_REFS_INVALID"
        )
        add_finding(findings, code, "$.evidence_refs")

    _validate_claim(
        findings,
        candidate.get("claim"),
        source_role,
        resource_character,
    )
    _validate_spatial_support(findings, candidate.get("spatial_support"))
    _validate_governance(findings, candidate.get("governance"))

    limitations = candidate.get("limitations")
    if not _string_list_is_valid(limitations, maximum=MAX_LIMITATIONS):
        code = (
            "LIMITATION_COUNT_EXCEEDED"
            if isinstance(limitations, list) and len(limitations) > MAX_LIMITATIONS
            else "LIMITATIONS_INVALID"
        )
        add_finding(findings, code, "$.limitations")
    elif resource_character is not None:
        expected_limitations = FIXTURE_RESOURCE_RULES[
            resource_character
        ].limitations
        if set(limitations) != expected_limitations or len(limitations) != len(
            expected_limitations
        ):
            add_finding(findings, "LIMITATIONS_INVALID", "$.limitations")

    return sorted(findings)


def validate_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_candidate)


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(
        argv=argv,
        description=(
            "Validate the frozen synthetic Geology resource-class "
            "anti-collapse fixture profile."
        ),
        scope="geology-resource-class-fixture",
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
