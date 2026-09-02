#!/usr/bin/env python3
"""Validate the bounded Archaeology CandidateFeature projection.

This validator is deterministic, standard-library only, and performs no network
access. It intentionally validates a narrow safety boundary rather than the full
draft semantic contract.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/archaeology/synthetic_candidate_feature"

REQUIRED_FIELDS = frozenset(
    {
        "candidate_feature_id",
        "object_type",
        "truth_state",
        "origin_method",
        "source_refs",
        "review_state",
        "sensitivity_class",
        "lifecycle_state",
    }
)
ALLOWED_FIELDS = REQUIRED_FIELDS | frozenset(
    {
        "candidate_type",
        "evidence_refs",
        "observation_refs",
        "candidate_geometry_ref",
        "spatial_precision_class",
        "confidence_statement",
        "correction_refs",
        "spec_hash",
    }
)
FORBIDDEN_INLINE_LOCATION_FIELDS = frozenset(
    {
        "geometry",
        "coordinates",
        "latitude",
        "longitude",
        "lat",
        "lon",
        "lng",
        "bbox",
        "geohash",
        "wkt",
        "public_geometry",
    }
)
FORBIDDEN_SITE_CLAIM_FIELDS = frozenset(
    {
        "archaeological_site_id",
        "site_id",
        "confirmed",
        "confirmation_state",
        "site_status",
    }
)
CANDIDATE_TYPES = frozenset(
    {
        "ANOMALY",
        "ARCHIVAL_LEAD",
        "EARTHWORK",
        "FIELD_OBSERVATION",
        "LANDSCAPE_TRACE",
        "MATERIAL_SCATTER",
        "STRUCTURE_TRACE",
        "OTHER",
    }
)
ORIGIN_METHODS = frozenset(
    {
        "ARCHIVAL",
        "CROSS_DOMAIN_CONTEXT",
        "FIELD_SURVEY",
        "GEOPHYSICS",
        "HISTORICAL_MAP_COMPARISON",
        "LIDAR",
        "REMOTE_SENSING",
        "STEWARD_SUBMISSION",
        "OTHER",
    }
)
REVIEW_STATES = frozenset(
    {
        "INTAKE",
        "NEEDS_REVIEW",
        "UNDER_REVIEW",
        "RETAINED",
        "REJECTED",
        "QUARANTINED",
        "SUPERSEDED",
    }
)
EVIDENCE_BOUND_REVIEW_STATES = frozenset({"UNDER_REVIEW", "RETAINED"})
SENSITIVITY_CLASSES = frozenset(
    {"RESTRICTED", "WITHHELD", "PUBLIC_SAFE_GENERALIZED"}
)
SPATIAL_PRECISION_CLASSES = frozenset(
    {"WITHHELD", "GENERALIZED", "PUBLIC_SAFE_GENERALIZED"}
)
LIFECYCLE_STATES = frozenset({"WORK", "QUARANTINE", "PROCESSED", "CATALOG"})
EVIDENCE_BOUND_LIFECYCLE_STATES = frozenset({"PROCESSED", "CATALOG"})
CANDIDATE_ID_PATTERN = re.compile(r"^arc-candidate-[a-z0-9][a-z0-9-]*$")
# Opaque reference paths must not become a second channel for protected
# geometry. Keep this expression ECMAScript-compatible for JSON Schema and
# spell case-insensitive locator tokens with character classes because schema
# patterns do not carry flags.
KFM_REFERENCE_PATTERN = re.compile(
    r"^(?!.*[/._~-](?:[Ll][Aa][Tt](?:[Ii][Tt][Uu][Dd][Ee])?|"
    r"[Ll][Oo][Nn](?:[Gg][Ii][Tt][Uu][Dd][Ee])?|[Ll][Nn][Gg]|"
    r"[Cc][Oo][Oo][Rr][Dd][Ii][Nn][Aa][Tt][Ee][Ss]?|[Bb][Bb][Oo][Xx]|"
    r"[Gg][Ee][Oo][Hh][Aa][Ss][Hh]|[Ww][Kk][Tt]|[Ee][Aa][Ss][Tt][Ii][Nn][Gg]|"
    r"[Nn][Oo][Rr][Tt][Hh][Ii][Nn][Gg]|[Uu][Tt][Mm]|[Mm][Gg][Rr][Ss])"
    r"(?:$|[/._~-]))kfm://[A-Za-z0-9][A-Za-z0-9._~/-]*$"
)
REFERENCE_FAMILY_PATTERNS = {
    "source_refs": re.compile(r"^kfm://(?:source|source-descriptor|source-record)/"),
    "evidence_refs": re.compile(r"^kfm://(?:evidence|evidence-ref|evidence-bundle)/"),
    "observation_refs": re.compile(r"^kfm://observation/"),
    "correction_refs": re.compile(r"^kfm://(?:correction|correction-notice|rollback)/"),
    "candidate_geometry_ref": re.compile(r"^kfm://geometry/"),
}
SPEC_HASH_PATTERN = re.compile(r"^sha256:[a-f0-9]{64}$")
CONFIDENCE_STATEMENT_MAX_LENGTH = 1000
# Keep this ECMAScript-compatible for the Draft 2020-12 schema.  Requiring a
# non-surrogate BMP content code point makes supplementary-only strings fail
# closed while preserving supplementary characters alongside ordinary text.
# The excluded BMP set covers Unicode 15.0 Cc/Cf/separator code points plus
# BMP Default_Ignorable_Code_Point ranges that are not already in those
# categories.
CONFIDENCE_CONTENT_PATTERN = re.compile(
    r"(?=[\u0000-\uFFFF])"
    r"[^\u0000-\u0020\u007F-\u00A0\u00AD\u034F\u0600-\u0605"
    r"\u061C\u06DD\u070F\u0890-\u0891\u08E2\u115F-\u1160"
    r"\u1680\u17B4-\u17B5\u180B-\u180F\u2000-\u200F"
    r"\u2028-\u202F\u205F-\u206F\u3000\u3164\uD800-\uDFFF"
    r"\uFE00-\uFE0F\uFEFF\uFFA0\uFFF0-\uFFFB]"
)


def _is_bounded_string(value: Any, allowed: frozenset[str]) -> bool:
    """Return whether a value is a string in a bounded vocabulary."""

    return isinstance(value, str) and value in allowed


def _is_opaque_kfm_ref(value: Any) -> bool:
    """Return whether a value is an opaque governed reference, not a locator."""

    return isinstance(value, str) and KFM_REFERENCE_PATTERN.fullmatch(value) is not None


def _validate_refs(value: Any, field: str, *, required: bool = False) -> list[str]:
    if not isinstance(value, list):
        return [f"{field} must be an array"]
    if required and not value:
        return [f"{field} must contain at least one reference"]
    errors: list[str] = []
    string_refs = [ref for ref in value if isinstance(ref, str)]
    if len(string_refs) != len(set(string_refs)):
        errors.append(f"{field} must not contain duplicate references")
    for ref in value:
        if not _is_opaque_kfm_ref(ref):
            errors.append(
                f"{field} entries must be opaque kfm:// references without query, "
                "fragment, or protected locator material"
            )
            continue
        if REFERENCE_FAMILY_PATTERNS[field].match(ref) is None:
            errors.append(
                f"{field} entries must use the allowed governed reference family"
            )
    return errors


def validate_candidate_feature(payload: Any) -> list[str]:
    """Return finite validation errors for a bounded candidate payload."""

    if not isinstance(payload, dict):
        return ["payload must be an object"]

    errors: list[str] = []
    keys = set(payload)
    missing = sorted(REQUIRED_FIELDS - keys)
    if missing:
        errors.append("missing required fields: " + ", ".join(missing))

    inline_location = sorted(FORBIDDEN_INLINE_LOCATION_FIELDS & keys)
    if inline_location:
        errors.append("inline location fields are denied: " + ", ".join(inline_location))

    site_claims = sorted(FORBIDDEN_SITE_CLAIM_FIELDS & keys)
    if site_claims:
        errors.append("confirmed-site claim fields are denied: " + ", ".join(site_claims))

    unknown = sorted(keys - ALLOWED_FIELDS - FORBIDDEN_INLINE_LOCATION_FIELDS - FORBIDDEN_SITE_CLAIM_FIELDS)
    if unknown:
        errors.append("unknown fields are denied: " + ", ".join(unknown))

    candidate_id = payload.get("candidate_feature_id")
    if (
        not isinstance(candidate_id, str)
        or CANDIDATE_ID_PATTERN.fullmatch(candidate_id) is None
    ):
        errors.append(
            "candidate_feature_id must match "
            "^arc-candidate-[a-z0-9][a-z0-9-]*$"
        )
    if payload.get("object_type") != "CandidateFeature":
        errors.append("object_type must be CandidateFeature")
    if payload.get("truth_state") != "CANDIDATE":
        errors.append("truth_state must remain CANDIDATE")
    candidate_type = payload.get("candidate_type")
    if "candidate_type" in payload and not _is_bounded_string(
        candidate_type, CANDIDATE_TYPES
    ):
        errors.append("candidate_type is not in the bounded vocabulary")
    if not _is_bounded_string(payload.get("origin_method"), ORIGIN_METHODS):
        errors.append("origin_method is not in the bounded vocabulary")
    if not _is_bounded_string(payload.get("review_state"), REVIEW_STATES):
        errors.append("review_state cannot imply confirmation or publication")
    if not _is_bounded_string(
        payload.get("sensitivity_class"), SENSITIVITY_CLASSES
    ):
        errors.append("sensitivity_class is not in the bounded vocabulary")
    spatial_precision_class = payload.get("spatial_precision_class")
    if "spatial_precision_class" in payload and not _is_bounded_string(
        spatial_precision_class, SPATIAL_PRECISION_CLASSES
    ):
        errors.append("spatial_precision_class is not in the bounded vocabulary")
    if not _is_bounded_string(payload.get("lifecycle_state"), LIFECYCLE_STATES):
        errors.append("lifecycle_state cannot be PUBLISHED for CandidateFeature")

    if "source_refs" in payload:
        errors.extend(_validate_refs(payload["source_refs"], "source_refs", required=True))
    evidence_binding_required = (
        _is_bounded_string(
            payload.get("review_state"), EVIDENCE_BOUND_REVIEW_STATES
        )
        or _is_bounded_string(
            payload.get("lifecycle_state"), EVIDENCE_BOUND_LIFECYCLE_STATES
        )
    )
    evidence_refs = payload.get("evidence_refs")
    if evidence_binding_required and (
        not isinstance(evidence_refs, list) or not evidence_refs
    ):
        errors.append(
            "evidence_refs are required before review or processed/catalog lifecycle"
        )
    correction_refs = payload.get("correction_refs")
    if payload.get("review_state") == "SUPERSEDED" and (
        not isinstance(correction_refs, list) or not correction_refs
    ):
        errors.append("correction_refs are required for superseded candidates")
    nonempty_when_present = frozenset({"evidence_refs", "correction_refs"})
    for field in ("evidence_refs", "observation_refs", "correction_refs"):
        if field in payload:
            errors.extend(
                _validate_refs(
                    payload[field],
                    field,
                    required=field in nonempty_when_present,
                )
            )
    geometry_ref = payload.get("candidate_geometry_ref")
    if "candidate_geometry_ref" in payload and not _is_opaque_kfm_ref(
        geometry_ref
    ):
        errors.append(
            "candidate_geometry_ref must be an opaque governed kfm:// reference "
            "without query, fragment, or protected locator material"
        )
    elif (
        "candidate_geometry_ref" in payload
        and REFERENCE_FAMILY_PATTERNS["candidate_geometry_ref"].match(
            geometry_ref
        )
        is None
    ):
        errors.append("candidate_geometry_ref must use the kfm://geometry/ family")
    if "candidate_geometry_ref" in payload and spatial_precision_class is None:
        errors.append(
            "spatial_precision_class is required with candidate_geometry_ref"
        )
    spec_hash = payload.get("spec_hash")
    if "spec_hash" in payload and (
        not isinstance(spec_hash, str)
        or SPEC_HASH_PATTERN.fullmatch(spec_hash) is None
    ):
        errors.append("spec_hash must match ^sha256:[a-f0-9]{64}$")
    confidence_statement = payload.get("confidence_statement")
    if (
        "confidence_statement" in payload
        and (
            not isinstance(confidence_statement, str)
            or not 1 <= len(confidence_statement) <= CONFIDENCE_STATEMENT_MAX_LENGTH
            or CONFIDENCE_CONTENT_PATTERN.search(confidence_statement) is None
        )
    ):
        errors.append("confidence_statement must contain 1 to 1000 characters")

    return errors


def _load(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_fixture_suite() -> int:
    valid_path = FIXTURE_ROOT / "valid.json"
    deny_paths = {
        FIXTURE_ROOT / "sensitive_geometry_deny.json": "inline location fields are denied",
        FIXTURE_ROOT / "location_bearing_reference_deny.json": "opaque kfm:// references",
        FIXTURE_ROOT / "path_locator_reference_deny.json": "protected locator material",
        FIXTURE_ROOT / "misbound_reference_family_deny.json": "allowed governed reference family",
        FIXTURE_ROOT / "unbound_catalog_candidate_deny.json": "evidence_refs are required",
        FIXTURE_ROOT / "superseded_without_correction_deny.json": "correction_refs are required",
        FIXTURE_ROOT / "malformed_candidate_id_deny.json": "candidate_feature_id must match",
        FIXTURE_ROOT / "unsupported_candidate_type_deny.json": "candidate_type is not in",
        FIXTURE_ROOT / "unsupported_spatial_precision_deny.json": "spatial_precision_class is not in",
        FIXTURE_ROOT / "unclassified_geometry_reference_deny.json": "spatial_precision_class is required",
        FIXTURE_ROOT / "non_string_reference_deny.json": "opaque kfm:// references",
        FIXTURE_ROOT / "empty_evidence_refs_deny.json": "evidence_refs must contain",
        FIXTURE_ROOT / "non_string_vocabulary_deny.json": "candidate_type is not in",
        FIXTURE_ROOT / "malformed_spec_hash_deny.json": "spec_hash must match",
        FIXTURE_ROOT / "null_optional_scalars_deny.json": "candidate_type is not in",
        FIXTURE_ROOT / "malformed_confidence_statement_deny.json": "confidence_statement must contain",
        FIXTURE_ROOT / "unicode_invisible_confidence_deny.json": "confidence_statement must contain",
    }
    valid_errors = validate_candidate_feature(_load(valid_path))
    if valid_errors:
        print(f"FAIL {valid_path}: {'; '.join(valid_errors)}")
        return 1
    print(f"PASS {valid_path}")
    for deny_path, expected_error in deny_paths.items():
        deny_errors = validate_candidate_feature(_load(deny_path))
        if not any(expected_error in error for error in deny_errors):
            print(
                f"FAIL {deny_path}: expected {expected_error!r}; "
                f"received {'; '.join(deny_errors) or 'no errors'}"
            )
            return 1
        print(f"EXPECTED_FAIL {deny_path}: {'; '.join(deny_errors)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return validate_fixture_suite()
    if not args.paths:
        parser.error("provide JSON paths or --fixtures")

    failed = False
    for path in args.paths:
        errors = validate_candidate_feature(_load(path))
        if errors:
            failed = True
            print(f"FAIL {path}: {'; '.join(errors)}")
        else:
            print(f"PASS {path}")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
