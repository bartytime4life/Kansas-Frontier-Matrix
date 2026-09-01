#!/usr/bin/env python3
"""Validate the bounded Archaeology CandidateFeature projection.

This validator is deterministic, standard-library only, and performs no network
access. It intentionally validates a narrow safety boundary rather than the full
draft semantic contract.
"""

from __future__ import annotations

import argparse
import json
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
SENSITIVITY_CLASSES = frozenset(
    {"RESTRICTED", "WITHHELD", "PUBLIC_SAFE_GENERALIZED"}
)
LIFECYCLE_STATES = frozenset({"WORK", "QUARANTINE", "PROCESSED", "CATALOG"})


def _validate_refs(value: Any, field: str, *, required: bool = False) -> list[str]:
    if not isinstance(value, list):
        return [f"{field} must be an array"]
    if required and not value:
        return [f"{field} must contain at least one reference"]
    errors: list[str] = []
    if len(value) != len(set(value)):
        errors.append(f"{field} must not contain duplicate references")
    for ref in value:
        if not isinstance(ref, str) or not ref.startswith("kfm://"):
            errors.append(f"{field} entries must be kfm:// references")
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
    if not isinstance(candidate_id, str) or not candidate_id.startswith("arc-candidate-"):
        errors.append("candidate_feature_id must start with arc-candidate-")
    if payload.get("object_type") != "CandidateFeature":
        errors.append("object_type must be CandidateFeature")
    if payload.get("truth_state") != "CANDIDATE":
        errors.append("truth_state must remain CANDIDATE")
    if payload.get("origin_method") not in ORIGIN_METHODS:
        errors.append("origin_method is not in the bounded vocabulary")
    if payload.get("review_state") not in REVIEW_STATES:
        errors.append("review_state cannot imply confirmation or publication")
    if payload.get("sensitivity_class") not in SENSITIVITY_CLASSES:
        errors.append("sensitivity_class is not in the bounded vocabulary")
    if payload.get("lifecycle_state") not in LIFECYCLE_STATES:
        errors.append("lifecycle_state cannot be PUBLISHED for CandidateFeature")

    if "source_refs" in payload:
        errors.extend(_validate_refs(payload["source_refs"], "source_refs", required=True))
    for field in ("evidence_refs", "observation_refs", "correction_refs"):
        if field in payload:
            errors.extend(_validate_refs(payload[field], field))
    geometry_ref = payload.get("candidate_geometry_ref")
    if geometry_ref is not None and (
        not isinstance(geometry_ref, str) or not geometry_ref.startswith("kfm://")
    ):
        errors.append("candidate_geometry_ref must be a governed kfm:// reference")

    return errors


def _load(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_fixture_suite() -> int:
    valid_path = FIXTURE_ROOT / "valid.json"
    deny_path = FIXTURE_ROOT / "sensitive_geometry_deny.json"
    valid_errors = validate_candidate_feature(_load(valid_path))
    deny_errors = validate_candidate_feature(_load(deny_path))
    if valid_errors:
        print(f"FAIL {valid_path}: {'; '.join(valid_errors)}")
        return 1
    if not deny_errors:
        print(f"FAIL {deny_path}: expected fail-closed denial")
        return 1
    print(f"PASS {valid_path}")
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
