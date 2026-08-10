#!/usr/bin/env python3
"""Validate the bounded KFM SpatialGeometry carrier without network access.

A passing result proves only the proposed schema shape plus this validator's
declared geometry-structure, dimensionality, EPSG identifier, ring, and
EPSG:4326 bounds profile. It does not repair or transform geometry, establish
source or survey authority, evaluate sensitivity or policy, authorize release,
or permit public use.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/spatial_geometry.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/spatial_geometry/cases.json"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
MAX_POSITIONS = 10_000
SCOPE = "spatial-geometry-carrier-structure-only"
SUPPORTED_TYPES = {
    "Point",
    "MultiPoint",
    "LineString",
    "MultiLineString",
    "Polygon",
    "MultiPolygon",
}
EPSG_IDENTIFIER = re.compile(r"^EPSG:[1-9][0-9]*$")


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(
            finding.code
            in {
                "FILE_NOT_FOUND",
                "FILE_READ_ERROR",
                "FILE_TOO_LARGE",
                "INPUT_SYMLINK_DENIED",
                "JSON_COMPLEXITY_LIMIT",
                "JSON_DUPLICATE_KEY",
                "JSON_INVALID",
                "JSON_NONFINITE_NUMBER",
                "JSON_NOT_UTF8",
                "ROOT_NOT_OBJECT",
                "SCHEMA_UNAVAILABLE",
            }
            for finding in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_non_finite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_non_finite,
                parse_float=_parse_finite_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]

    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema).iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]

    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _position(
    value: Any,
    field: str,
    *,
    epsg4326: bool,
) -> tuple[tuple[float, ...] | None, list[Finding]]:
    if not isinstance(value, list) or len(value) not in {2, 3}:
        return None, [Finding("GEOMETRY_POSITION_INVALID", field)]
    if not all(_is_number(item) and math.isfinite(item) for item in value):
        return None, [Finding("GEOMETRY_POSITION_INVALID", field)]

    position = tuple(float(item) for item in value)
    findings: list[Finding] = []
    if epsg4326 and not (-180.0 <= position[0] <= 180.0 and -90.0 <= position[1] <= 90.0):
        findings.append(Finding("COORDINATE_OUT_OF_BOUNDS", field))
    return position, findings


def _position_array(
    value: Any,
    field: str,
    *,
    minimum: int,
    epsg4326: bool,
) -> tuple[list[tuple[float, ...]], list[Finding]]:
    if not isinstance(value, list):
        return [], [Finding("GEOMETRY_COORDINATES_MALFORMED", field)]

    findings: list[Finding] = []
    positions: list[tuple[float, ...]] = []
    for index, item in enumerate(value):
        position, item_findings = _position(
            item,
            f"{field}/{index}",
            epsg4326=epsg4326,
        )
        findings.extend(item_findings)
        if position is not None:
            positions.append(position)

    if len(value) < minimum:
        findings.append(Finding("GEOMETRY_DEGENERATE", field))
    if any(left == right for left, right in zip(positions, positions[1:])):
        findings.append(Finding("GEOMETRY_DEGENERATE", field))
    return positions, findings


def _orientation(a: Sequence[float], b: Sequence[float], c: Sequence[float]) -> int:
    value = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return 0 if value == 0 else (1 if value > 0 else -1)


def _on_segment(a: Sequence[float], b: Sequence[float], c: Sequence[float]) -> bool:
    return (
        min(a[0], c[0]) <= b[0] <= max(a[0], c[0])
        and min(a[1], c[1]) <= b[1] <= max(a[1], c[1])
    )


def _segments_intersect(
    a: Sequence[float],
    b: Sequence[float],
    c: Sequence[float],
    d: Sequence[float],
) -> bool:
    o1 = _orientation(a, b, c)
    o2 = _orientation(a, b, d)
    o3 = _orientation(c, d, a)
    o4 = _orientation(c, d, b)
    if o1 != o2 and o3 != o4:
        return True
    return (
        (o1 == 0 and _on_segment(a, c, b))
        or (o2 == 0 and _on_segment(a, d, b))
        or (o3 == 0 and _on_segment(c, a, d))
        or (o4 == 0 and _on_segment(c, b, d))
    )


def _ring_findings(positions: list[tuple[float, ...]], field: str) -> list[Finding]:
    if len(positions) < 4:
        return []

    findings: list[Finding] = []
    if positions[0] != positions[-1]:
        findings.append(Finding("POLYGON_RING_OPEN", field))
        return findings

    if len(set(positions[:-1])) < 3:
        findings.append(Finding("GEOMETRY_DEGENERATE", field))

    area_twice = sum(
        left[0] * right[1] - right[0] * left[1]
        for left, right in zip(positions, positions[1:])
    )
    if area_twice == 0:
        findings.append(Finding("GEOMETRY_DEGENERATE", field))

    segment_count = len(positions) - 1
    for first in range(segment_count):
        for second in range(first + 1, segment_count):
            if second == first + 1 or (first == 0 and second == segment_count - 1):
                continue
            if _segments_intersect(
                positions[first],
                positions[first + 1],
                positions[second],
                positions[second + 1],
            ):
                findings.append(Finding("POLYGON_SELF_INTERSECTION", field))
                return findings
    return findings


def _geometry_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    geometry = candidate.get("geometry")
    if not isinstance(geometry, Mapping):
        return []

    geometry_type = geometry.get("type")
    coordinates = geometry.get("coordinates")
    crs = candidate.get("crs")
    findings: list[Finding] = []
    dimensions: set[int] = set()
    position_count = 0

    if not isinstance(crs, str) or EPSG_IDENTIFIER.fullmatch(crs) is None:
        findings.append(Finding("CRS_IDENTIFIER_UNSUPPORTED", "/crs"))
    epsg4326 = crs == "EPSG:4326"

    if geometry_type not in SUPPORTED_TYPES:
        findings.append(Finding("GEOMETRY_TYPE_UNSUPPORTED", "/geometry/type"))
        return findings

    def positions(value: Any, field: str, minimum: int) -> list[tuple[float, ...]]:
        nonlocal position_count
        parsed, parsed_findings = _position_array(
            value,
            field,
            minimum=minimum,
            epsg4326=epsg4326,
        )
        findings.extend(parsed_findings)
        position_count += len(parsed)
        dimensions.update(len(item) for item in parsed)
        return parsed

    def lines(value: Any, field: str) -> None:
        if not isinstance(value, list) or not value:
            findings.append(Finding("GEOMETRY_COORDINATES_MALFORMED", field))
            return
        for index, item in enumerate(value):
            positions(item, f"{field}/{index}", 2)

    def polygon(value: Any, field: str) -> None:
        if not isinstance(value, list) or not value:
            findings.append(Finding("GEOMETRY_COORDINATES_MALFORMED", field))
            return
        for index, item in enumerate(value):
            ring_field = f"{field}/{index}"
            ring = positions(item, ring_field, 4)
            findings.extend(_ring_findings(ring, ring_field))

    if geometry_type == "Point":
        point, point_findings = _position(
            coordinates,
            "/geometry/coordinates",
            epsg4326=epsg4326,
        )
        findings.extend(point_findings)
        if point is not None:
            dimensions.add(len(point))
            position_count = 1
    elif geometry_type in {"MultiPoint", "LineString"}:
        minimum = 1 if geometry_type == "MultiPoint" else 2
        positions(coordinates, "/geometry/coordinates", minimum)
    elif geometry_type == "MultiLineString":
        lines(coordinates, "/geometry/coordinates")
    elif geometry_type == "Polygon":
        polygon(coordinates, "/geometry/coordinates")
    elif geometry_type == "MultiPolygon":
        if not isinstance(coordinates, list) or not coordinates:
            findings.append(
                Finding("GEOMETRY_COORDINATES_MALFORMED", "/geometry/coordinates")
            )
        else:
            for index, item in enumerate(coordinates):
                polygon(item, f"/geometry/coordinates/{index}")

    if len(dimensions) > 1:
        findings.append(Finding("GEOMETRY_DIMENSION_MIXED", "/geometry/coordinates"))
    if position_count > MAX_POSITIONS:
        findings.append(Finding("GEOMETRY_TOO_COMPLEX", "/geometry/coordinates"))
    return findings


def validate_candidate(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not any(finding.code == "SCHEMA_UNAVAILABLE" for finding in findings):
        findings.extend(_geometry_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_spatial_geometry(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_candidate(candidate)


def _serialize(source: str, result: ValidationResult) -> str:
    outcome = "ERROR" if result.error else ("PASS" if result.ok else "FAIL")
    payload = {
        "source": source,
        "outcome": outcome,
        "scope": SCOPE,
        "findings": [
            {"code": finding.code, "field": finding.field}
            for finding in result.findings
        ],
        "non_effects": [
            "no_geometry_repair_or_transformation",
            "no_source_survey_or_domain_truth",
            "no_policy_review_release_or_publication_authority",
        ],
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _fixture_lines() -> tuple[list[str], bool]:
    try:
        payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        cases = payload["cases"]
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError):
        result = ValidationResult((Finding("FIXTURE_PROFILE_INVALID", "/"),))
        return [_serialize(FIXTURE_PATH.name, result)], False

    lines: list[str] = []
    profile_ok = True
    for case in cases:
        try:
            case_id = case["case_id"]
            candidate = case["candidate"]
            expected_outcome = case["expected_outcome"]
            expected_codes = sorted(case["expected_codes"])
            if not isinstance(case_id, str) or not isinstance(candidate, dict):
                raise TypeError
        except (KeyError, TypeError):
            result = ValidationResult((Finding("FIXTURE_PROFILE_INVALID", "/"),))
            lines.append(_serialize("invalid-fixture-case", result))
            profile_ok = False
            continue

        result = validate_candidate(candidate)
        actual_outcome = "ERROR" if result.error else ("PASS" if result.ok else "FAIL")
        actual_codes = sorted({finding.code for finding in result.findings})
        if actual_outcome != expected_outcome or actual_codes != expected_codes:
            result = ValidationResult(
                tuple(sorted(set(result.findings + (Finding("FIXTURE_POLARITY_ERROR", "/"),))))
            )
            profile_ok = False
        lines.append(_serialize(case_id, result))
    return lines, profile_ok


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="Replay the synthetic reviewed fixture profile.",
    )
    args = parser.parse_args(argv)

    if args.fixtures:
        lines, profile_ok = _fixture_lines()
        for line in lines:
            print(line)
        return 0 if profile_ok else 1
    if not args.paths:
        parser.error("provide one or more candidate paths or --fixtures")

    results = [(path, validate_spatial_geometry(path)) for path in args.paths]
    for path, result in results:
        print(_serialize(path.name, result))
    return 0 if all(result.ok for _, result in results) else 1


if __name__ == "__main__":
    sys.exit(main())
