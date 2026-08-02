#!/usr/bin/env python3
"""Validate the frozen synthetic Atmosphere knowledge-character fixture profile.

This validator proves a narrow anti-collapse boundary for repository fixtures.
It does not define the canonical knowledge-character enum or registry, evaluate
Rego policy, resolve evidence, admit a source, assess air quality, issue an
alert, or authorize promotion, release, or publication.
"""

from __future__ import annotations

from dataclasses import dataclass
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


PROFILE_ID = "kfm-atmosphere-knowledge-character-fixture-v1"
MAX_EVIDENCE_REFS = 32
MAX_LIMITATIONS = 32

ALLOWED_TOP_LEVEL_FIELDS = frozenset(
    {
        "fixture_id",
        "profile_id",
        "object_family",
        "knowledge_character",
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
    {"kind", "parameter", "unit", "intended_use"}
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
        "easting",
        "northing",
        "station_coordinates",
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
class FixtureCharacterRule:
    """One non-authoritative pairing in the frozen synthetic fixture profile."""

    object_family: str
    source_role: str
    claim_kind: str
    parameter: str
    unit: str
    intended_use: str
    limitations: frozenset[str]


FIXTURE_CHARACTER_RULES = {
    "OBSERVED_SENSOR": FixtureCharacterRule(
        object_family="PM25Observation",
        source_role="observed",
        claim_kind="ground_concentration",
        parameter="pm2_5_mass_concentration",
        unit="ug/m3",
        intended_use="measurement_context",
        limitations=frozenset({"synthetic_fixture_only"}),
    ),
    "PUBLIC_AQI_REPORT": FixtureCharacterRule(
        object_family="PM25Observation",
        source_role="regulatory",
        claim_kind="air_quality_index",
        parameter="air_quality_index",
        unit="index",
        intended_use="public_context",
        limitations=frozenset(
            {"not_a_concentration", "synthetic_fixture_only"}
        ),
    ),
    "ATMOSPHERIC_MODEL_FIELD": FixtureCharacterRule(
        object_family="ForecastContext",
        source_role="modeled",
        claim_kind="modeled_field",
        parameter="pm2_5_mass_concentration",
        unit="ug/m3",
        intended_use="forecast_context",
        limitations=frozenset(
            {"not_an_observation", "synthetic_fixture_only"}
        ),
    ),
    "REMOTE_SENSING_MASK": FixtureCharacterRule(
        object_family="AODRaster",
        source_role="observed_remote_sensing",
        claim_kind="aerosol_optical_depth",
        parameter="aerosol_optical_depth",
        unit="1",
        intended_use="proxy_context",
        limitations=frozenset(
            {"not_ground_pm2_5", "synthetic_fixture_only"}
        ),
    ),
    "ALERT_AND_ADVISORY_CONTEXT": FixtureCharacterRule(
        object_family="AdvisoryContext",
        source_role="regulatory",
        claim_kind="advisory_context",
        parameter="air_quality_advisory",
        unit="categorical",
        intended_use="referral_context",
        limitations=frozenset(
            {
                "not_an_alert",
                "not_life_safety_guidance",
                "synthetic_fixture_only",
            }
        ),
    ),
    "NETWORK_AND_SITE_CONTEXT": FixtureCharacterRule(
        object_family="AirStation",
        source_role="administrative",
        claim_kind="site_context",
        parameter="station_metadata",
        unit="none",
        intended_use="metadata_context",
        limitations=frozenset(
            {
                "generalized_location_only",
                "not_an_observation",
                "synthetic_fixture_only",
            }
        ),
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


def _knowledge_character(candidate: dict[object, object], findings: set[Finding]) -> str | None:
    value = candidate.get("knowledge_character")
    if "knowledge_character" not in candidate:
        add_finding(findings, "KNOWLEDGE_CHARACTER_MISSING", "$.knowledge_character")
        return None
    if isinstance(value, list) and len(value) > 1:
        add_finding(findings, "KNOWLEDGE_CHARACTER_MULTIPLE", "$.knowledge_character")
        return None
    if not is_nonempty_string(value):
        add_finding(findings, "KNOWLEDGE_CHARACTER_INVALID", "$.knowledge_character")
        return None
    if value not in FIXTURE_CHARACTER_RULES:
        add_finding(findings, "KNOWLEDGE_CHARACTER_UNKNOWN", "$.knowledge_character")
        return None
    return value


def _collapse_code(
    knowledge_character: str,
    source_role: object,
    claim: dict[object, object],
) -> str | None:
    kind = claim.get("kind")
    parameter = claim.get("parameter")
    unit = claim.get("unit")
    intended_use = claim.get("intended_use")

    if knowledge_character == "ATMOSPHERIC_MODEL_FIELD" and (
        source_role == "observed"
        or kind in {"ground_concentration", "ground_observation"}
        or intended_use == "measurement_context"
    ):
        return "MODEL_AS_OBSERVATION_DENIED"
    if knowledge_character == "PUBLIC_AQI_REPORT" and (
        kind == "ground_concentration"
        or parameter in {"pm2_5_mass_concentration", "ozone_concentration"}
        or unit in {"ug/m3", "ppb", "ppm"}
    ):
        return "AQI_AS_CONCENTRATION_DENIED"
    if knowledge_character == "REMOTE_SENSING_MASK" and (
        kind == "ground_concentration"
        or parameter == "pm2_5_mass_concentration"
        or unit == "ug/m3"
    ):
        return "AOD_AS_PM25_DENIED"
    if knowledge_character == "ALERT_AND_ADVISORY_CONTEXT" and (
        kind == "official_alert" or intended_use == "life_safety"
    ):
        return "ADVISORY_AS_LIFE_SAFETY_DENIED"
    return None


def _validate_claim(
    findings: set[Finding],
    claim: object,
    source_role: object,
    knowledge_character: str | None,
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
    if knowledge_character is None:
        return

    collapse_code = _collapse_code(knowledge_character, source_role, claim)
    if collapse_code is not None:
        add_finding(findings, collapse_code, "$.claim")
        return

    expected = FIXTURE_CHARACTER_RULES[knowledge_character]
    for field, expected_value, code in (
        ("kind", expected.claim_kind, "CLAIM_KIND_INVALID"),
        ("parameter", expected.parameter, "CLAIM_PARAMETER_INVALID"),
        ("unit", expected.unit, "CLAIM_UNIT_INVALID"),
        ("intended_use", expected.intended_use, "CLAIM_INTENDED_USE_INVALID"),
    ):
        if claim.get(field) != expected_value:
            add_finding(findings, code, f"$.claim.{field}")


def _validate_spatial_support(findings: set[Finding], spatial_support: object) -> None:
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
                "PRECISE_SITE_EXPOSURE_DENIED",
                f"$.spatial_support.{key}",
            )
    spatial_kind = spatial_support.get("kind")
    if spatial_kind in {"exact_site", "exact_station", "point", "coordinates"}:
        add_finding(
            findings,
            "PRECISE_SITE_EXPOSURE_DENIED",
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
            add_finding(findings, "GOVERNANCE_STATE_INVALID", f"$.governance.{field}")


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

    knowledge_character = _knowledge_character(candidate, findings)
    source_role = candidate.get("source_role")
    if not is_nonempty_string(source_role):
        add_finding(findings, "SOURCE_ROLE_MISSING", "$.source_role")

    if knowledge_character is not None:
        expected = FIXTURE_CHARACTER_RULES[knowledge_character]
        if candidate.get("object_family") != expected.object_family:
            add_finding(findings, "OBJECT_FAMILY_INVALID", "$.object_family")
        if source_role != expected.source_role and not (
            knowledge_character == "ATMOSPHERIC_MODEL_FIELD"
            and source_role == "observed"
        ):
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
            if isinstance(evidence_refs, list) and len(evidence_refs) > MAX_EVIDENCE_REFS
            else "EVIDENCE_REFS_INVALID"
        )
        add_finding(findings, code, "$.evidence_refs")

    _validate_claim(
        findings,
        candidate.get("claim"),
        source_role,
        knowledge_character,
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
    elif knowledge_character is not None:
        expected_limitations = FIXTURE_CHARACTER_RULES[knowledge_character].limitations
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
            "Validate the frozen synthetic Atmosphere knowledge-character "
            "anti-collapse fixture profile."
        ),
        scope="atmosphere-knowledge-character-fixture",
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
