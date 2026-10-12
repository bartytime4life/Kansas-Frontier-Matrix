#!/usr/bin/env python3
"""Project an accepted fixture GCP set into affine-quality candidate input.

The adapter preserves the upstream control-point-set identity in a wrapper and
embeds an unchanged v1 ``GeoreferenceTransformQualityAssessment`` candidate.
It performs no network access, image work, reprojection, policy evaluation,
release, or publication. Filesystem output requires ``--write``.
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
from tools.validators.map import validate_georeference_transform_quality as quality_validator

MAX_INPUT_BYTES = 2 * 1024 * 1024
RFC3339_UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
REQUEST_KEYS = {
    "assessed_at",
    "fixture_only",
    "network_access",
    "object_type",
    "schema_version",
    "thresholds",
}
THRESHOLD_KEYS = {
    "max_loo_residual",
    "max_loo_rms",
    "max_residual",
    "max_rms",
    "minimum_gcps",
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


def validate_request(request: Mapping[str, Any]) -> None:
    if set(request) != REQUEST_KEYS:
        raise ProjectionFailure("REQUEST_FIELDS_INVALID")
    if request.get("object_type") != "GeoreferenceTransformQualityProjectionRequest":
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
    thresholds = request.get("thresholds")
    if not isinstance(thresholds, dict) or set(thresholds) != THRESHOLD_KEYS:
        raise ProjectionFailure("THRESHOLDS_INVALID")
    if thresholds.get("minimum_gcps") != 4:
        raise ProjectionFailure("MINIMUM_GCPS_INVALID")
    for field in THRESHOLD_KEYS - {"minimum_gcps"}:
        value = thresholds.get(field)
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
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
        "gcps": copy.deepcopy(control_point_set["control_points"]),
        "governance": copy.deepcopy(GOVERNANCE),
        "network_access": "forbidden",
        "object_type": "GeoreferenceTransformQualityAssessment",
        "profile": "kfm.georeference.affine-quality.v1",
        "schema_version": "1.0.0",
        "target_unit": control_point_set["target_space"]["unit"],
        "thresholds": copy.deepcopy(request["thresholds"]),
    }
    try:
        candidate["computed"] = quality_validator._declared(
            quality_validator.compute_quality(candidate["gcps"])
        )
    except (quality_validator.DegenerateGeometry, ValueError) as exc:
        raise ProjectionFailure("QUALITY_COMPUTATION_INVALID") from exc
    decision = quality_validator.derive(candidate)
    candidate["decision"] = {
        "outcome": decision.outcome,
        "reasons": list(decision.reasons),
    }
    validated = quality_validator.validate_candidate(candidate)
    if validated.outcome not in {"READY", "HOLD"}:
        raise ProjectionFailure("GENERATED_QUALITY_CANDIDATE_INVALID")

    return {
        "governance": copy.deepcopy(GOVERNANCE),
        "object_type": "GeoreferenceTransformQualityProjection",
        "schema_version": "1.0.0",
        "source_control_point_set": {
            "resource_set_hash": control_point_set["resource_set_hash"],
            "set_id": control_point_set["set_id"],
            "target_set_hash": control_point_set["target_set_hash"],
        },
        "status": "CANDIDATE",
        "transform_quality_candidate": candidate,
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
        description="Project a fixture GCP set into transform-quality input."
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
