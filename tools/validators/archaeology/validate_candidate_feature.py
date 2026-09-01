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
KFM_REFERENCE_PATTERN = re.compile(r"^kfm://[A-Za-z0-9][A-Za-z0-9._~/-]*$")


def _is_opaque_kfm_ref(value: Any) -> bool:
    """Return whether a value is an opaque governed reference, not a locator."""

    return isinstance(value, str) and KFM_REFERENCE_PATTERN.fullmatch(value) is not None


def _validate_refs(value: Any, field: str, *, required: bool = False) -> list[str]:
    if not isinstance(value, list):
        return [f"{field} must be an array"]
    if required and not value:
        return [f"{field} must contain at least one reference"]
    errors: list[str] = []
    if len(value) != len(set(value)):
        errors.append(f"{field} must not contain duplicate references")
    for ref in value:
        if not _is_opaque_kfm_ref(ref):
            errors.append(
                f"{field} entries must be opaque kfm:// references without query, "
                "fragment, or encoded locator material"
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
    if candidate_type is not None and candidate_type not in CANDIDATE_TYPES:
        errors.append("candidate_type is not in the bounded vocabulary")
    if payload.get("origin_method") not in ORIGIN_METHODS:
        errors.append("origin_method is not in the bounded vocabulary")
    if payload.get("review_state") not in REVIEW_STATES:
        errors.append("review_state cannot imply confirmation or publication")
    if payload.get("sensitivity_class") not in SENSITIVITY_CLASSES:
        errors.append("sensitivity_class is not in the bounded vocabulary")
    spatial_precision_class = payload.get("spatial_precision_class")
    if (
        spatial_precision_class is not None
        and spatial_precision_class not in SPATIAL_PRECISION_CLASSES
    ):
        errors.append("spatial_precision_class is not in the bounded vocabulary")
    if payload.get("lifecycle_state") not in LIFECYCLE_STATES:
        errors.append("lifecycle_state cannot be PUBLISHED for CandidateFeature")

    if "source_refs" in payload:
        errors.extend(_validate_refs(payload["source_refs"], "source_refs", required=True))
    evidence_binding_required = (
        payload.get("review_state") in EVIDENCE_BOUND_REVIEW_STATES
        or payload.get("lifecycle_state") in EVIDENCE_BOUND_LIFECYCLE_STATES
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
    for field in ("evidence_refs", "observation_refs", "correction_refs"):
        if field in payload:
            errors.extend(_validate_refs(payload[field], field))
    geometry_ref = payload.get("candidate_geometry_ref")
    if geometry_ref is not None and not _is_opaque_kfm_ref(geometry_ref):
        errors.append(
            "candidate_geometry_ref must be an opaque governed kfm:// reference "
            "without query, fragment, or encoded locator material"
        )
    if "candidate_geometry_ref" in payload and spatial_precision_class is None:
        errors.append(
            "spatial_precision_class is required with candidate_geometry_ref"
        )

    return errors


def _load(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_fixture_suite() -> int:
    valid_path = FIXTURE_ROOT / "valid.json"
    deny_paths = {
        FIXTURE_ROOT / "sensitive_geometry_deny.json": "inline location fields are denied",
        FIXTURE_ROOT / "location_bearing_reference_deny.json": "opaque kfm:// references",
        FIXTURE_ROOT / "unbound_catalog_candidate_deny.json": "evidence_refs are required",
        FIXTURE_ROOT / "superseded_without_correction_deny.json": "correction_refs are required",
        FIXTURE_ROOT / "malformed_candidate_id_deny.json": "candidate_feature_id must match",
        FIXTURE_ROOT / "unsupported_candidate_type_deny.json": "candidate_type is not in",
        FIXTURE_ROOT / "unsupported_spatial_precision_deny.json": "spatial_precision_class is not in",
        FIXTURE_ROOT / "unclassified_geometry_reference_deny.json": "spatial_precision_class is required",
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
