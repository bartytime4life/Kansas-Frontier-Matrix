#!/usr/bin/env python3
"""Validate one bounded synthetic Flora public-safe fixture profile.

This validator proves fixture conformance only. It does not validate botanical
truth, source admission, rights, policy, stewardship, EvidenceBundle closure,
proof construction, release readiness, or publication.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (
    MAX_DOCUMENT_DEPTH,
    MAX_DOCUMENT_NODES,
    MAX_FIXTURE_BYTES,
    MAX_JSON_INTEGER_DIGITS,
    Finding,
    add_finding,
    find_undeclared_fields,
    is_nonempty_string,
    run_cli,
    validate_fixture_file,
)


SCOPE = "flora-public-safe-fixture"

TOP_LEVEL_FIELDS = frozenset(
    {
        "record_id",
        "record_type",
        "fixture_only",
        "network_access",
        "taxon_ref",
        "taxon_concept_state",
        "source_descriptor_ref",
        "source_role",
        "rights_state",
        "evidence_refs",
        "spatial_support",
        "sensitivity",
        "public_representation",
        "governance",
        "public_caveats",
    }
)
SPATIAL_SUPPORT_FIELDS = frozenset({"kind", "area_ref", "precision_state"})
SENSITIVITY_FIELDS = frozenset(
    {
        "state",
        "exact_location_present",
        "reverse_engineerable_location",
        "private_land_join",
        "cultural_knowledge_present",
        "stewardship_review_state",
    }
)
PUBLIC_REPRESENTATION_FIELDS = frozenset(
    {
        "geometry_state",
        "redaction_receipt_ref",
        "review_record_ref",
        "release_surface",
    }
)
GOVERNANCE_FIELDS = frozenset(
    {
        "evidence_state",
        "policy_state",
        "review_state",
        "release_state",
        "promotion_eligible",
        "correction_state",
        "rollback_state",
    }
)

FORBIDDEN_LOCATION_ALIASES = frozenset(
    {
        "address",
        "bbox",
        "coordinates",
        "geometry",
        "geohash",
        "lat",
        "latitude",
        "lng",
        "locality",
        "location_notes",
        "lon",
        "longitude",
        "parcel_id",
        "private_land_parcel",
        "site",
        "utm",
        "wkt",
        "x",
        "y",
        "access_route",
        "collection_route",
    }
)
FORBIDDEN_TRANSFORM_ALIASES = frozenset(
    {
        "generalization_threshold",
        "jitter_seed",
        "precision_meters",
        "redaction_offset",
        "transform_parameters",
    }
)

_REQUIRED_CAVEATS = frozenset(
    {
        "synthetic fixture only",
        "not a botanical occurrence claim",
        "not released",
    }
)
_URL_RE = re.compile(r"(?i)(?:https?://|ftp://|www\.)")
_COORDINATE_PAIR_RE = re.compile(
    r"(?<![0-9])[-+]?[0-9]{1,3}(?:\.[0-9]+)?\s*,\s*"
    r"[-+]?[0-9]{1,3}(?:\.[0-9]+)?(?![0-9])"
)
_WKT_RE = re.compile(r"(?i)\b(?:POINT|LINESTRING|POLYGON|MULTIPOINT)\s*\(")


def _has_fixture_prefix(value: object, prefix: str) -> bool:
    return is_nonempty_string(value) and str(value).startswith(prefix)


def _matches_exact(value: object, expected: object) -> bool:
    return type(value) is type(expected) and value == expected


def _check_exact_value(
    findings: set[Finding],
    candidate: dict[str, object],
    field: str,
    expected: object,
    code: str,
    parent_path: str = "$",
) -> None:
    if not _matches_exact(candidate.get(field), expected):
        add_finding(findings, code, f"{parent_path}.{field}")


def _scan_for_sensitive_material(
    findings: set[Finding], value: object, path: str = "$"
) -> None:
    if isinstance(value, dict):
        for key in sorted(value, key=lambda item: (type(item).__name__, repr(item))):
            child_path = f"{path}.{key}"
            normalized = key.casefold() if isinstance(key, str) else ""
            if normalized in FORBIDDEN_LOCATION_ALIASES:
                add_finding(
                    findings,
                    "SENSITIVE_LOCATION_FIELD_FORBIDDEN",
                    child_path,
                )
            if normalized in FORBIDDEN_TRANSFORM_ALIASES:
                add_finding(
                    findings,
                    "TRANSFORM_SECRET_FIELD_FORBIDDEN",
                    child_path,
                )
            _scan_for_sensitive_material(findings, value[key], child_path)
        return

    if isinstance(value, list):
        for index, child in enumerate(value):
            _scan_for_sensitive_material(findings, child, f"{path}[{index}]")
        return

    if isinstance(value, bool) or value is None:
        return

    if isinstance(value, (int, float)):
        add_finding(findings, "NUMERIC_VALUE_FORBIDDEN", path)
        return

    if isinstance(value, str):
        if _URL_RE.search(value):
            add_finding(findings, "EXTERNAL_REFERENCE_FORBIDDEN", path)
        if _COORDINATE_PAIR_RE.search(value) or _WKT_RE.search(value):
            add_finding(findings, "COORDINATE_LIKE_VALUE_FORBIDDEN", path)


def _validate_reference_list(
    findings: set[Finding],
    value: object,
    *,
    path: str,
    prefix: str,
    code: str,
) -> None:
    if not isinstance(value, list) or not value:
        add_finding(findings, code, path)
        return
    if len(value) != len(set(item for item in value if isinstance(item, str))):
        add_finding(findings, code, path)
    for index, item in enumerate(value):
        if not _has_fixture_prefix(item, prefix):
            add_finding(findings, code, f"{path}[{index}]")


def validate_candidate(candidate: object) -> list[Finding]:
    """Validate the frozen synthetic Flora public-safe fixture profile."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("CANDIDATE_NOT_OBJECT", "$")]

    find_undeclared_fields(
        findings,
        candidate,
        TOP_LEVEL_FIELDS,
        "UNDECLARED_TOP_LEVEL_FIELD",
        "$",
    )

    if not _has_fixture_prefix(candidate.get("record_id"), "fixture:flora:public-safe:"):
        add_finding(findings, "RECORD_ID_INVALID", "$.record_id")
    _check_exact_value(
        findings,
        candidate,
        "record_type",
        "flora_public_safe_validation_candidate",
        "RECORD_TYPE_INVALID",
    )
    if candidate.get("fixture_only") is not True:
        add_finding(findings, "FIXTURE_MARKER_INVALID", "$.fixture_only")
    _check_exact_value(
        findings,
        candidate,
        "network_access",
        "forbidden",
        "NETWORK_ACCESS_INVALID",
    )
    if not _has_fixture_prefix(candidate.get("taxon_ref"), "fixture:taxon:flora:"):
        add_finding(findings, "TAXON_REF_INVALID", "$.taxon_ref")
    _check_exact_value(
        findings,
        candidate,
        "taxon_concept_state",
        "synthetic_resolved",
        "TAXON_CONCEPT_STATE_INVALID",
    )
    if not _has_fixture_prefix(
        candidate.get("source_descriptor_ref"), "fixture:source:flora:"
    ):
        add_finding(
            findings,
            "SOURCE_DESCRIPTOR_REF_INVALID",
            "$.source_descriptor_ref",
        )
    _check_exact_value(
        findings,
        candidate,
        "source_role",
        "synthetic_occurrence",
        "SOURCE_ROLE_INVALID",
    )
    _check_exact_value(
        findings,
        candidate,
        "rights_state",
        "fixture_only",
        "RIGHTS_STATE_INVALID",
    )
    _validate_reference_list(
        findings,
        candidate.get("evidence_refs"),
        path="$.evidence_refs",
        prefix="fixture:evidence:flora:",
        code="EVIDENCE_REFS_INVALID",
    )

    spatial_support = candidate.get("spatial_support")
    if not isinstance(spatial_support, dict):
        add_finding(findings, "SPATIAL_SUPPORT_INVALID", "$.spatial_support")
    else:
        find_undeclared_fields(
            findings,
            spatial_support,
            SPATIAL_SUPPORT_FIELDS,
            "UNDECLARED_SPATIAL_SUPPORT_FIELD",
            "$.spatial_support",
        )
        if spatial_support.get("kind") != "generalized_fixture_area":
            add_finding(
                findings,
                "SPATIAL_SUPPORT_INVALID",
                "$.spatial_support.kind",
            )
        if not _has_fixture_prefix(
            spatial_support.get("area_ref"), "fixture:area:flora:"
        ):
            add_finding(
                findings,
                "SPATIAL_SUPPORT_INVALID",
                "$.spatial_support.area_ref",
            )
        if spatial_support.get("precision_state") != "generalized_fixture":
            add_finding(
                findings,
                "SPATIAL_SUPPORT_INVALID",
                "$.spatial_support.precision_state",
            )

    sensitivity = candidate.get("sensitivity")
    if not isinstance(sensitivity, dict):
        add_finding(findings, "SENSITIVITY_STATE_INVALID", "$.sensitivity")
    else:
        find_undeclared_fields(
            findings,
            sensitivity,
            SENSITIVITY_FIELDS,
            "UNDECLARED_SENSITIVITY_FIELD",
            "$.sensitivity",
        )
        expected_sensitivity = {
            "state": "public_safe_fixture",
            "exact_location_present": False,
            "reverse_engineerable_location": False,
            "private_land_join": False,
            "cultural_knowledge_present": False,
            "stewardship_review_state": "fixture_only",
        }
        for field, expected in expected_sensitivity.items():
            if not _matches_exact(sensitivity.get(field), expected):
                add_finding(
                    findings,
                    "SENSITIVITY_STATE_INVALID",
                    f"$.sensitivity.{field}",
                )

    public_representation = candidate.get("public_representation")
    if not isinstance(public_representation, dict):
        add_finding(
            findings,
            "PUBLIC_REPRESENTATION_INVALID",
            "$.public_representation",
        )
    else:
        find_undeclared_fields(
            findings,
            public_representation,
            PUBLIC_REPRESENTATION_FIELDS,
            "UNDECLARED_PUBLIC_REPRESENTATION_FIELD",
            "$.public_representation",
        )
        if public_representation.get("geometry_state") != "generalized_fixture":
            add_finding(
                findings,
                "PUBLIC_REPRESENTATION_INVALID",
                "$.public_representation.geometry_state",
            )
        if not _has_fixture_prefix(
            public_representation.get("redaction_receipt_ref"),
            "fixture:receipt:redaction:flora:",
        ):
            add_finding(
                findings,
                "PUBLIC_REPRESENTATION_INVALID",
                "$.public_representation.redaction_receipt_ref",
            )
        if not _has_fixture_prefix(
            public_representation.get("review_record_ref"),
            "fixture:review:flora:",
        ):
            add_finding(
                findings,
                "PUBLIC_REPRESENTATION_INVALID",
                "$.public_representation.review_record_ref",
            )
        if public_representation.get("release_surface") != "not_released":
            add_finding(
                findings,
                "PUBLIC_REPRESENTATION_INVALID",
                "$.public_representation.release_surface",
            )

    governance = candidate.get("governance")
    if not isinstance(governance, dict):
        add_finding(findings, "GOVERNANCE_STATE_INVALID", "$.governance")
    else:
        find_undeclared_fields(
            findings,
            governance,
            GOVERNANCE_FIELDS,
            "UNDECLARED_GOVERNANCE_FIELD",
            "$.governance",
        )
        expected_governance = {
            "evidence_state": "fixture_only",
            "policy_state": "not_evaluated_fixture",
            "review_state": "fixture_only",
            "release_state": "not_released",
            "promotion_eligible": False,
            "correction_state": "fixture_only",
            "rollback_state": "fixture_only",
        }
        for field, expected in expected_governance.items():
            if not _matches_exact(governance.get(field), expected):
                add_finding(
                    findings,
                    "GOVERNANCE_STATE_INVALID",
                    f"$.governance.{field}",
                )

    caveats = candidate.get("public_caveats")
    if (
        not isinstance(caveats, list)
        or any(not is_nonempty_string(item) or len(str(item)) > 160 for item in caveats)
        or not _REQUIRED_CAVEATS.issubset(
            {str(item) for item in caveats if isinstance(item, str)}
        )
    ):
        add_finding(findings, "PUBLIC_CAVEATS_INVALID", "$.public_caveats")

    _scan_for_sensitive_material(findings, candidate)
    return sorted(findings)


def validate_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_candidate)


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(
        argv=argv,
        description=(
            "Validate bounded synthetic Flora public-safe fixture candidates. "
            "A PASS is fixture conformance only."
        ),
        scope=SCOPE,
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
