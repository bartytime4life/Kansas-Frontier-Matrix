#!/usr/bin/env python3
"""Project an accepted fixture GCP set into spatial-distribution input.

The adapter binds the spatial projection to the upstream resource-space point
identity and embeds an unchanged v1 ``GeoreferenceSpatialDistributionAssessment``
candidate. It performs no network access, image work, coordinate transform,
policy evaluation, release, or publication. Filesystem output requires
``--write``.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators.map import validate_georeference_control_point_set as set_validator
from tools.validators.map import validate_georeference_spatial_distribution as spatial_validator

MAX_INPUT_BYTES = 2 * 1024 * 1024
RFC3339_UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
REQUEST_KEYS = {
    "assessed_at",
    "fixture_only",
    "network_access",
    "object_type",
    "resource_mask",
    "schema_version",
    "thresholds",
    "transform_quality_ref",
}
THRESHOLD_KEYS = {
    "max_centroid_offset_ratio",
    "max_extrapolation_ratio",
    "min_hull_area_ratio",
    "minimum_gcps",
    "minimum_occupied_quadrants",
}
RATIO_THRESHOLD_KEYS = {
    "max_centroid_offset_ratio",
    "max_extrapolation_ratio",
    "min_hull_area_ratio",
}
GOVERNANCE = {
    "authority_created": False,
    "policy_evaluated": False,
    "promotion_authorized": False,
    "public_use_allowed": False,
    "publication_authorized": False,
    "release_authorized": False,
    "release_ref": None,
}


class DuplicateKeyError(ValueError):
    """Input JSON repeated an object key."""


class NonFiniteNumberError(ValueError):
    """Input JSON contained a non-standard or non-finite number."""


@dataclass(frozen=True)
class ProjectionFailure(ValueError):
    code: str

    def __str__(self) -> str:
        return self.code


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def read_json_object(path: Path) -> dict[str, Any]:
    try:
        if path.is_symlink():
            raise ProjectionFailure("INPUT_SYMLINK_DENIED")
        if not path.is_file():
            raise ProjectionFailure("INPUT_NOT_FILE")
        if path.stat().st_size > MAX_INPUT_BYTES:
            raise ProjectionFailure("INPUT_TOO_LARGE")
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except ProjectionFailure:
        raise
    except DuplicateKeyError as exc:
        raise ProjectionFailure("JSON_DUPLICATE_KEY") from exc
    except NonFiniteNumberError as exc:
        raise ProjectionFailure("JSON_NONFINITE_NUMBER") from exc
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ProjectionFailure("JSON_INVALID") from exc
    except OSError as exc:
        raise ProjectionFailure("INPUT_READ_ERROR") from exc
    if not isinstance(value, dict):
        raise ProjectionFailure("ROOT_NOT_OBJECT")
    return value


def _is_finite_number(value: Any) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and math.isfinite(value)
    )


def validate_request(request: Mapping[str, Any]) -> None:
    if set(request) != REQUEST_KEYS:
        raise ProjectionFailure("REQUEST_FIELDS_INVALID")
    if request.get("object_type") != "GeoreferenceSpatialDistributionProjectionRequest":
        raise ProjectionFailure("REQUEST_OBJECT_TYPE_INVALID")
    if request.get("schema_version") != "1.0.0":
        raise ProjectionFailure("REQUEST_SCHEMA_VERSION_INVALID")
    if request.get("fixture_only") is not True or request.get("network_access") != "forbidden":
        raise ProjectionFailure("FIXTURE_BOUNDARY_INVALID")

    assessed_at = request.get("assessed_at")
    if not isinstance(assessed_at, str) or not RFC3339_UTC_RE.fullmatch(assessed_at):
        raise ProjectionFailure("ASSESSED_AT_INVALID")
    try:
        datetime.fromisoformat(assessed_at.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ProjectionFailure("ASSESSED_AT_INVALID") from exc

    transform_quality_ref = request.get("transform_quality_ref")
    if not isinstance(transform_quality_ref, str) or not 1 <= len(transform_quality_ref) <= 256:
        raise ProjectionFailure("TRANSFORM_QUALITY_REF_INVALID")

    resource_mask = request.get("resource_mask")
    if not isinstance(resource_mask, list) or not 4 <= len(resource_mask) <= 257:
        raise ProjectionFailure("RESOURCE_MASK_INVALID")
    for point in resource_mask:
        if (
            not isinstance(point, list)
            or len(point) != 2
            or not all(_is_finite_number(value) for value in point)
        ):
            raise ProjectionFailure("RESOURCE_MASK_INVALID")

    thresholds = request.get("thresholds")
    if not isinstance(thresholds, dict) or set(thresholds) != THRESHOLD_KEYS:
        raise ProjectionFailure("THRESHOLDS_INVALID")
    if thresholds.get("minimum_gcps") != 4:
        raise ProjectionFailure("MINIMUM_GCPS_INVALID")
    minimum_quadrants = thresholds.get("minimum_occupied_quadrants")
    if (
        isinstance(minimum_quadrants, bool)
        or not isinstance(minimum_quadrants, int)
        or not 1 <= minimum_quadrants <= 4
    ):
        raise ProjectionFailure("MINIMUM_OCCUPIED_QUADRANTS_INVALID")
    for field in RATIO_THRESHOLD_KEYS:
        value = thresholds.get(field)
        if not _is_finite_number(value) or not 0 <= value <= 1:
            raise ProjectionFailure("THRESHOLDS_INVALID")


def project(
    control_point_set: Mapping[str, Any], request: Mapping[str, Any]
) -> dict[str, Any]:
    validate_request(request)
    source_result = set_validator.validate_candidate(control_point_set)
    if source_result.outcome != "VALID":
        raise ProjectionFailure("CONTROL_POINT_SET_INVALID")

    candidate = {
        "assessed_at": request["assessed_at"],
        "computed": {},
        "decision": {"outcome": "ERROR", "reasons": ["PROJECTION_PENDING"]},
        "fixture_only": True,
        "gcp_count": control_point_set["control_point_count"],
        "gcps": [
            {"id": point["id"], "resource": copy.deepcopy(point["resource"])}
            for point in control_point_set["control_points"]
        ],
        "governance": copy.deepcopy(GOVERNANCE),
        "network_access": "forbidden",
        "object_type": "GeoreferenceSpatialDistributionAssessment",
        "profile": "kfm.georeference.spatial-distribution.v1",
        "schema_version": "1.0.0",
        "support": {
            "resource_height_px": control_point_set["resource_space"]["height_px"],
            "resource_mask": copy.deepcopy(request["resource_mask"]),
            "resource_width_px": control_point_set["resource_space"]["width_px"],
        },
        "thresholds": copy.deepcopy(request["thresholds"]),
        "transform_quality_ref": request["transform_quality_ref"],
    }
    try:
        candidate["computed"] = spatial_validator._declared(
            spatial_validator.compute_metrics(candidate)
        )
    except (ArithmeticError, IndexError, KeyError, TypeError, ValueError) as exc:
        raise ProjectionFailure("SPATIAL_COMPUTATION_INVALID") from exc
    decision = spatial_validator.derive(candidate)
    candidate["decision"] = {
        "outcome": decision.outcome,
        "reasons": list(decision.reasons),
    }
    validated = spatial_validator.validate_candidate(candidate)
    if validated.outcome not in {"READY", "HOLD"}:
        raise ProjectionFailure("GENERATED_SPATIAL_CANDIDATE_INVALID")

    return {
        "governance": copy.deepcopy(GOVERNANCE),
        "object_type": "GeoreferenceSpatialDistributionProjection",
        "schema_version": "1.0.0",
        "source_control_point_set": {
            "resource_set_hash": control_point_set["resource_set_hash"],
        },
        "spatial_distribution_candidate": candidate,
        "status": "CANDIDATE",
    }


def _encoded(value: Mapping[str, Any]) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def write_projection(
    value: Mapping[str, Any], path: Path, *, force: bool = False
) -> None:
    if path.is_symlink():
        raise ProjectionFailure("OUTPUT_SYMLINK_DENIED")
    if path.exists() and not force:
        raise ProjectionFailure("OUTPUT_EXISTS")
    if path.exists() and not path.is_file():
        raise ProjectionFailure("OUTPUT_NOT_FILE")
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(_encoded(value), encoding="utf-8")
    except OSError as exc:
        raise ProjectionFailure("OUTPUT_WRITE_ERROR") from exc


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Project a fixture GCP set into spatial-distribution input."
    )
    parser.add_argument("control_point_set", type=Path)
    parser.add_argument("request", type=Path)
    parser.add_argument("--write", type=Path, metavar="PATH")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    if args.force and args.write is None:
        parser.error("--force requires --write")
    try:
        result = project(
            read_json_object(args.control_point_set),
            read_json_object(args.request),
        )
        if args.write is None:
            sys.stdout.write(_encoded(result))
        else:
            write_projection(result, args.write, force=args.force)
            print(
                json.dumps(
                    {"outcome": "generated", "path": args.write.as_posix()},
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
    except ProjectionFailure as exc:
        print(
            json.dumps(
                {"outcome": "blocked", "reason": exc.code},
                sort_keys=True,
                separators=(",", ":"),
            ),
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
