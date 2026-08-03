#!/usr/bin/env python3
"""Validate the bounded Flora public-safe fixture profile.

This validator accepts only synthetic, fixture-only candidates with withheld
spatial support that are explicitly ineligible for promotion or publication.
It is not an OccurrencePublic validator and does not establish botanical truth,
taxonomic identity, source admission, rights clearance, sensitivity review,
evidence closure, policy approval, geoprivacy transformation, release readiness,
or safe public use.

The profile is deterministic, standard-library only, and performs no network
access. Findings contain stable codes and JSON paths, never candidate values.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path
from typing import Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    is_finite_number,
    is_nonempty_string,
    run_cli,
    validate_fixture_file,
)


SCOPE = "synthetic-public-safe-fixture-only"
SAFE_SPATIAL_KINDS = frozenset({"withheld"})
ALLOWED_TOP_LEVEL_FIELDS = frozenset(
    {
        "evidence_refs",
        "fixture_id",
        "fixture_only",
        "governance",
        "network_access",
        "public_caveats",
        "reality_boundary",
        "record_type",
        "rights_state",
        "sensitivity_state",
        "source_descriptor_ref",
        "source_role",
        "spatial_support",
        "taxon_ref",
        "taxonomy_state",
    }
)
ALLOWED_SPATIAL_FIELDS = frozenset({"kind", "label"})
ALLOWED_GOVERNANCE_FIELDS = frozenset(
    {
        "correction_state",
        "evidence_state",
        "geoprivacy_state",
        "policy_state",
        "promotion_state",
        "release_state",
        "review_state",
        "rollback_state",
    }
)
SAFE_DIAGNOSTIC_KEYS = (
    ALLOWED_TOP_LEVEL_FIELDS
    | ALLOWED_SPATIAL_FIELDS
    | ALLOWED_GOVERNANCE_FIELDS
)
FORBIDDEN_LOCATION_KEYS = frozenset(
    {
        "address",
        "bbox",
        "bounding_box",
        "bounds",
        "center",
        "centre",
        "centroid",
        "collection_site",
        "coordinates",
        "decimal_latitude",
        "decimal_longitude",
        "easting",
        "exact_location",
        "geojson",
        "geocode",
        "geohash",
        "geom",
        "geometry",
        "lat",
        "latitude",
        "lng",
        "locality",
        "location",
        "location_hint",
        "location_id",
        "lon",
        "long",
        "longitude",
        "northing",
        "occurrence_coordinates",
        "place",
        "place_name",
        "point",
        "polygon",
        "site",
        "site_coordinates",
        "site_id",
        "utm",
        "verbatim_coordinates",
        "wkt",
        "x",
        "y",
    }
)

ALLOWED_PUBLIC_CAVEATS = frozenset(
    {
        "not-released-or-promotion-eligible",
        "synthetic-fixture-no-real-occurrence-or-location",
    }
)
ALLOWED_PROFILE_STRINGS = frozenset(
    {
        "flora_public_safe_validation_candidate",
        "fixture:flora:valid:withheld-occurrence",
        "fixture:flora:invalid:missing-source-descriptor",
        "fixture:flora:invalid:precision-hint",
        "fixture:flora:invalid:encoded-location-clue",
        "fixture:flora:invalid:unresolved-taxonomy",
        "fixture:flora:invalid:unresolved-governance",
        "synthetic-test-fixture",
        "forbidden",
        "fixture:source:flora:synthetic-alpha",
        "synthetic",
        "fixture-only",
        "unresolved",
        "fixture:taxon:flora:synthetic-alpha",
        "fixture:taxon:flora:unresolved",
        "synthetic-resolved",
        "public-safe-synthetic",
        "sensitive-unresolved",
        "withheld",
        "exact-point",
        "synthetic-area-alpha",
        "SYNTHETIC-ONLY",
        "fixture:evidence:flora:synthetic-alpha",
        "fixture:evidence:flora:synthetic-missing-source",
        "fixture:evidence:flora:synthetic-precision-hint",
        "fixture:evidence:flora:synthetic-encoded-location-clue",
        "fixture:evidence:flora:synthetic-unresolved-taxonomy",
        "not-evaluated-fixture",
        "not-applicable-no-location",
        "not-released",
        "not-eligible",
        *ALLOWED_PUBLIC_CAVEATS,
    }
)

SAFE_IDENTIFIER_RE = re.compile(r"^[a-z0-9][a-z0-9:-]{0,159}$")
COORDINATE_NUMBER_PATTERN = (
    r"[-+]?(?:\d{1,6}(?:\.\d+)?|\.\d+)(?:[eE][-+]?\d{1,3})?"
)
COORDINATE_PAIR_RE = re.compile(
    rf"(?<![\w.]){COORDINATE_NUMBER_PATTERN}"
    rf"(?:\s*[,;/]\s*|\s+){COORDINATE_NUMBER_PATTERN}(?![\w.])"
)
MAX_CAVEAT_ITEMS = 16
MAX_CAVEAT_LENGTH = 512
MAX_EVIDENCE_REFS = 16


def _normalize_key(key: str) -> str:
    camel_split = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", key)
    normalized = unicodedata.normalize("NFKC", camel_split).strip().casefold()
    normalized = "".join(
        character
        for character in normalized
        if unicodedata.category(character) != "Cf"
    )
    return re.sub(r"[\s-]+", "_", normalized)


def _safe_key_segment(key: object, ordinal: int) -> str:
    if isinstance(key, int):
        return str(key)
    if isinstance(key, str):
        if key in SAFE_DIAGNOSTIC_KEYS:
            return key
        normalized = _normalize_key(key)
        if normalized in FORBIDDEN_LOCATION_KEYS:
            return normalized
    return f"field_{ordinal}"


def _find_undeclared_fields(
    findings: set[Finding],
    candidate: dict[object, object],
    allowed_fields: frozenset[str],
    code: str,
    parent_path: str,
) -> None:
    unknown_keys = sorted(
        (key for key in candidate if key not in allowed_fields),
        key=lambda key: (type(key).__name__, repr(key)),
    )
    for ordinal, key in enumerate(unknown_keys):
        segment = _safe_key_segment(key, ordinal)
        add_finding(findings, code, f"{parent_path}.{segment}")


def _is_safe_identifier(value: object) -> bool:
    return bool(
        is_nonempty_string(value)
        and SAFE_IDENTIFIER_RE.fullmatch(value.strip())
    )


def _validate_identifier(
    findings: set[Finding],
    value: object,
    *,
    path: str,
    prefix: str,
    missing_code: str,
    prefix_code: str,
    format_code: str,
) -> None:
    if not is_nonempty_string(value):
        add_finding(findings, missing_code, path)
        return
    normalized = value.strip()
    if not normalized.startswith(prefix):
        add_finding(findings, prefix_code, path)
    if not _is_safe_identifier(normalized):
        add_finding(findings, format_code, path)


def _contains_finite_number(value: object) -> bool:
    pending = [value]
    visited: set[int] = set()
    while pending:
        item = pending.pop()
        if is_finite_number(item):
            return True
        if isinstance(item, (dict, list)):
            identity = id(item)
            if identity in visited:
                continue
            visited.add(identity)
            pending.extend(item.values() if isinstance(item, dict) else item)
    return False


def _compact_url_value(value: str) -> str:
    return "".join(
        character
        for character in value.casefold()
        if not character.isspace() and unicodedata.category(character) != "Cf"
    )


def _walk(candidate: object):
    pending: list[tuple[object, tuple[str, ...]]] = [(candidate, ())]
    visited: set[int] = set()
    while pending:
        parent, parent_path = pending.pop()
        if not isinstance(parent, (dict, list)):
            continue
        identity = id(parent)
        if identity in visited:
            continue
        visited.add(identity)
        if isinstance(parent, dict):
            children = sorted(
                parent.items(),
                key=lambda item: (type(item[0]).__name__, repr(item[0])),
            )
        else:
            children = list(enumerate(parent))
        safe_children = [
            (_safe_key_segment(key, ordinal), key, value)
            for ordinal, (key, value) in enumerate(children)
        ]
        for safe_key, key, value in safe_children:
            path = (*parent_path, safe_key)
            yield path, key, value
        for safe_key, _key, value in reversed(safe_children):
            if isinstance(value, (dict, list)):
                pending.append((value, (*parent_path, safe_key)))


def _validate_public_caveats(
    findings: set[Finding], candidate: Mapping[object, object]
) -> None:
    if "public_caveats" not in candidate:
        return
    caveats = candidate["public_caveats"]
    if not isinstance(caveats, list) or not caveats:
        add_finding(findings, "PUBLIC_CAVEATS_INVALID", "$.public_caveats")
        return
    if len(caveats) > MAX_CAVEAT_ITEMS:
        add_finding(findings, "PUBLIC_CAVEATS_TOO_MANY", "$.public_caveats")
    seen_caveats: set[str] = set()
    for index, caveat in enumerate(caveats[:MAX_CAVEAT_ITEMS]):
        path = f"$.public_caveats.{index}"
        if not is_nonempty_string(caveat):
            add_finding(findings, "PUBLIC_CAVEAT_INVALID", path)
        elif len(caveat) > MAX_CAVEAT_LENGTH:
            add_finding(findings, "PUBLIC_CAVEAT_TOO_LONG", path)
        elif caveat not in ALLOWED_PUBLIC_CAVEATS:
            add_finding(findings, "PUBLIC_CAVEAT_NOT_PROFILE_TOKEN", path)
        elif caveat in seen_caveats:
            add_finding(findings, "PUBLIC_CAVEAT_DUPLICATE", path)
        if isinstance(caveat, str):
            seen_caveats.add(caveat)


def validate_candidate(candidate: object) -> list[Finding]:
    """Return deterministic findings for one synthetic Flora fixture candidate."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("DOCUMENT_NOT_OBJECT", "$")]

    if candidate.get("record_type") != "flora_public_safe_validation_candidate":
        add_finding(findings, "RECORD_TYPE_INVALID", "$.record_type")

    _validate_identifier(
        findings,
        candidate.get("fixture_id"),
        path="$.fixture_id",
        prefix="fixture:flora:",
        missing_code="FIXTURE_ID_MISSING",
        prefix_code="FIXTURE_ID_NOT_SYNTHETIC",
        format_code="FIXTURE_ID_FORMAT_INVALID",
    )
    if candidate.get("fixture_only") is not True:
        add_finding(findings, "FIXTURE_ONLY_REQUIRED", "$.fixture_only")
    if candidate.get("reality_boundary") != "synthetic-test-fixture":
        add_finding(findings, "REALITY_BOUNDARY_REQUIRED", "$.reality_boundary")
    if candidate.get("network_access") != "forbidden":
        add_finding(
            findings,
            "NETWORK_ACCESS_NOT_FORBIDDEN",
            "$.network_access",
        )

    _validate_identifier(
        findings,
        candidate.get("source_descriptor_ref"),
        path="$.source_descriptor_ref",
        prefix="fixture:source:flora:",
        missing_code="SOURCE_DESCRIPTOR_REF_MISSING",
        prefix_code="SOURCE_DESCRIPTOR_REF_NOT_SYNTHETIC",
        format_code="SOURCE_DESCRIPTOR_REF_FORMAT_INVALID",
    )
    if candidate.get("source_role") != "synthetic":
        add_finding(findings, "SOURCE_ROLE_NOT_SYNTHETIC", "$.source_role")
    if candidate.get("rights_state") != "fixture-only":
        add_finding(findings, "RIGHTS_STATE_UNRESOLVED", "$.rights_state")

    _validate_identifier(
        findings,
        candidate.get("taxon_ref"),
        path="$.taxon_ref",
        prefix="fixture:taxon:flora:",
        missing_code="TAXON_REF_MISSING",
        prefix_code="TAXON_REF_NOT_SYNTHETIC",
        format_code="TAXON_REF_FORMAT_INVALID",
    )
    if candidate.get("taxonomy_state") != "synthetic-resolved":
        add_finding(findings, "TAXONOMY_UNRESOLVED", "$.taxonomy_state")
    if candidate.get("sensitivity_state") != "public-safe-synthetic":
        add_finding(
            findings,
            "SENSITIVITY_NOT_PUBLIC_SAFE",
            "$.sensitivity_state",
        )

    spatial_support = candidate.get("spatial_support")
    if not isinstance(spatial_support, dict):
        add_finding(findings, "SPATIAL_SUPPORT_NOT_OBJECT", "$.spatial_support")
    else:
        _find_undeclared_fields(
            findings,
            spatial_support,
            ALLOWED_SPATIAL_FIELDS,
            "UNDECLARED_SPATIAL_FIELD",
            "$.spatial_support",
        )
        if spatial_support.get("kind") not in SAFE_SPATIAL_KINDS:
            add_finding(
                findings,
                "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE",
                "$.spatial_support.kind",
            )
        label = spatial_support.get("label")
        if not (
            is_nonempty_string(label)
            and label.strip().startswith("synthetic-area-")
            and _is_safe_identifier(label)
        ):
            add_finding(
                findings,
                "SPATIAL_SUPPORT_LABEL_INVALID",
                "$.spatial_support.label",
            )

    evidence_refs = candidate.get("evidence_refs")
    if not isinstance(evidence_refs, list) or not evidence_refs:
        add_finding(findings, "EVIDENCE_REF_MISSING", "$.evidence_refs")
    else:
        if len(evidence_refs) > MAX_EVIDENCE_REFS:
            add_finding(findings, "EVIDENCE_REFS_TOO_MANY", "$.evidence_refs")
        seen_refs: set[str] = set()
        for index, evidence_ref in enumerate(evidence_refs[:MAX_EVIDENCE_REFS]):
            path = f"$.evidence_refs.{index}"
            if not (
                is_nonempty_string(evidence_ref)
                and evidence_ref.strip().startswith("fixture:evidence:flora:")
            ):
                add_finding(findings, "EVIDENCE_REF_NOT_SYNTHETIC", path)
            if not _is_safe_identifier(evidence_ref):
                add_finding(findings, "EVIDENCE_REF_FORMAT_INVALID", path)
            if isinstance(evidence_ref, str):
                normalized_ref = evidence_ref.strip()
                if normalized_ref in seen_refs:
                    add_finding(findings, "EVIDENCE_REF_DUPLICATE", path)
                seen_refs.add(normalized_ref)

    _validate_public_caveats(findings, candidate)

    governance = candidate.get("governance")
    if not isinstance(governance, dict):
        add_finding(findings, "GOVERNANCE_STATE_MISSING", "$.governance")
    else:
        _find_undeclared_fields(
            findings,
            governance,
            ALLOWED_GOVERNANCE_FIELDS,
            "UNDECLARED_GOVERNANCE_FIELD",
            "$.governance",
        )
        required_states = {
            "evidence_state": ("fixture-only", "EVIDENCE_STATE_UNRESOLVED"),
            "policy_state": (
                "not-evaluated-fixture",
                "POLICY_STATE_UNRESOLVED",
            ),
            "geoprivacy_state": (
                "not-applicable-no-location",
                "GEOPRIVACY_STATE_UNRESOLVED",
            ),
            "review_state": ("fixture-only", "REVIEW_STATE_NOT_FIXTURE_ONLY"),
            "release_state": ("not-released", "RELEASE_STATE_NOT_HELD"),
            "promotion_state": ("not-eligible", "PROMOTION_STATE_NOT_HELD"),
            "correction_state": (
                "fixture-only",
                "CORRECTION_STATE_NOT_FIXTURE_ONLY",
            ),
            "rollback_state": (
                "fixture-only",
                "ROLLBACK_STATE_NOT_FIXTURE_ONLY",
            ),
        }
        for field, (expected, code) in required_states.items():
            if governance.get(field) != expected:
                add_finding(findings, code, f"$.governance.{field}")

    _find_undeclared_fields(
        findings,
        candidate,
        ALLOWED_TOP_LEVEL_FIELDS,
        "UNDECLARED_TOP_LEVEL_FIELD",
        "$",
    )

    for path_parts, key, value in _walk(candidate):
        path = "$." + ".".join(path_parts)
        if isinstance(key, str) and _normalize_key(key) in FORBIDDEN_LOCATION_KEYS:
            add_finding(findings, "PRECISE_LOCATION_FIELD_FORBIDDEN", path)
            if _contains_finite_number(value):
                add_finding(findings, "LOCATION_NUMERIC_VALUE_FORBIDDEN", path)
        if isinstance(value, str):
            if (
                not path.startswith("$.public_caveats.")
                and value not in ALLOWED_PROFILE_STRINGS
            ):
                add_finding(findings, "STRING_VALUE_NOT_PROFILE_TOKEN", path)
            compact = _compact_url_value(value)
            if (
                "http://" in compact
                or "https://" in compact
                or "www." in compact
                or "//" in compact
            ):
                add_finding(findings, "LIVE_URL_FORBIDDEN", path)
            if any(ord(character) < 32 or ord(character) == 127 for character in value):
                add_finding(findings, "CONTROL_CHARACTER_FORBIDDEN", path)
            if COORDINATE_PAIR_RE.search(value.strip()):
                add_finding(findings, "COORDINATE_PATTERN_FORBIDDEN", path)

    return sorted(findings)


def validate_file(path: Path | str) -> list[Finding]:
    """Load and validate one bounded, duplicate-free UTF-8 JSON fixture."""

    return validate_fixture_file(path, validate_candidate)


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(
        argv=argv,
        description="Validate synthetic Flora public-safe fixtures.",
        scope=SCOPE,
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
