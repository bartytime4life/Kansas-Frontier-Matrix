#!/usr/bin/env python3
"""Validate deterministic synthetic GCP spatial-distribution quality.

This validator inspects only committed JSON declarations. It does not fetch
imagery, georeference maps, transform coordinates, evaluate policy, or authorize
promotion/release/publication.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_EVEN, localcontext
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/georeference_spatial_distribution.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/map/georeference_spatial_distribution/cases.json"
MAX_FILE_BYTES = 1_048_576
Q = Decimal("0.000001")
EPS = Decimal("1e-24")


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True)
class Metrics:
    hull_vertex_count: int
    hull_area_ratio: Decimal
    max_extrapolation_ratio: Decimal
    centroid_offset_ratio: Decimal
    occupied_quadrants: int


@dataclass(frozen=True)
class Result:
    outcome: str
    reasons: tuple[str, ...]


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError(key)
        out[key] = value
    return out


def _nonfinite(_: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[Any | None, str | None]:
    try:
        if path.is_symlink():
            return None, "INPUT_SYMLINK_DENIED"
        if not path.is_file():
            return None, "FILE_NOT_FOUND"
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, "FILE_TOO_LARGE"
        with path.open("r", encoding="utf-8") as stream:
            return (
                json.load(
                    stream,
                    object_pairs_hook=_pairs,
                    parse_constant=_nonfinite,
                    parse_float=_finite_float,
                ),
                None,
            )
    except UnicodeDecodeError:
        return None, "JSON_NOT_UTF8"
    except DuplicateKeyError:
        return None, "JSON_DUPLICATE_KEY"
    except NonFiniteNumberError:
        return None, "JSON_NONFINITE_NUMBER"
    except json.JSONDecodeError:
        return None, "JSON_INVALID"
    except OSError:
        return None, "FILE_READ_ERROR"
    except (RecursionError, ValueError):
        return None, "JSON_COMPLEXITY_LIMIT"


def _schema_errors(candidate: Mapping[str, Any]) -> list[str]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [str(item.validator) for item in list(validator.iter_errors(candidate))[:100]]
    except Exception:
        return ["SCHEMA_UNAVAILABLE"]


def _d(value: Any) -> Decimal:
    return Decimal(str(value))


def _point(value: Sequence[Any]) -> tuple[Decimal, Decimal]:
    return _d(value[0]), _d(value[1])


def _cross(o: tuple[Decimal, Decimal], a: tuple[Decimal, Decimal], b: tuple[Decimal, Decimal]) -> Decimal:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def _convex_hull(points: Sequence[tuple[Decimal, Decimal]]) -> list[tuple[Decimal, Decimal]]:
    ordered = sorted(set(points))
    if len(ordered) < 3:
        raise ValueError("GCP_HULL_DEGENERATE")
    lower: list[tuple[Decimal, Decimal]] = []
    for point in ordered:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], point) <= EPS:
            lower.pop()
        lower.append(point)
    upper: list[tuple[Decimal, Decimal]] = []
    for point in reversed(ordered):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], point) <= EPS:
            upper.pop()
        upper.append(point)
    hull = lower[:-1] + upper[:-1]
    if len(hull) < 3 or _polygon_area(hull + [hull[0]]) <= EPS:
        raise ValueError("GCP_HULL_DEGENERATE")
    return hull


def _polygon_area(closed: Sequence[tuple[Decimal, Decimal]]) -> Decimal:
    total = Decimal(0)
    for first, second in zip(closed, closed[1:]):
        total += first[0] * second[1] - second[0] * first[1]
    return abs(total) / Decimal(2)


def _polygon_centroid(closed: Sequence[tuple[Decimal, Decimal]]) -> tuple[Decimal, Decimal]:
    signed_twice_area = Decimal(0)
    cx = Decimal(0)
    cy = Decimal(0)
    for first, second in zip(closed, closed[1:]):
        cross = first[0] * second[1] - second[0] * first[1]
        signed_twice_area += cross
        cx += (first[0] + second[0]) * cross
        cy += (first[1] + second[1]) * cross
    if abs(signed_twice_area) <= EPS:
        raise ValueError("RESOURCE_MASK_DEGENERATE")
    factor = Decimal(3) * signed_twice_area
    return cx / factor, cy / factor


def _orientation(a: tuple[Decimal, Decimal], b: tuple[Decimal, Decimal], c: tuple[Decimal, Decimal]) -> int:
    value = _cross(a, b, c)
    if abs(value) <= EPS:
        return 0
    return 1 if value > 0 else -1


def _on_segment(a: tuple[Decimal, Decimal], b: tuple[Decimal, Decimal], p: tuple[Decimal, Decimal]) -> bool:
    return (
        _orientation(a, b, p) == 0
        and min(a[0], b[0]) - EPS <= p[0] <= max(a[0], b[0]) + EPS
        and min(a[1], b[1]) - EPS <= p[1] <= max(a[1], b[1]) + EPS
    )


def _segments_intersect(a: tuple[Decimal, Decimal], b: tuple[Decimal, Decimal], c: tuple[Decimal, Decimal], d: tuple[Decimal, Decimal]) -> bool:
    o1 = _orientation(a, b, c)
    o2 = _orientation(a, b, d)
    o3 = _orientation(c, d, a)
    o4 = _orientation(c, d, b)
    if o1 * o2 < 0 and o3 * o4 < 0:
        return True
    return (
        (o1 == 0 and _on_segment(a, b, c))
        or (o2 == 0 and _on_segment(a, b, d))
        or (o3 == 0 and _on_segment(c, d, a))
        or (o4 == 0 and _on_segment(c, d, b))
    )


def _mask_is_simple(closed: Sequence[tuple[Decimal, Decimal]]) -> bool:
    segments = list(zip(closed, closed[1:]))
    count = len(segments)
    for i, first in enumerate(segments):
        for j in range(i + 1, count):
            if j == i + 1 or (i == 0 and j == count - 1):
                continue
            if _segments_intersect(first[0], first[1], segments[j][0], segments[j][1]):
                return False
    return True


def _point_in_polygon(point: tuple[Decimal, Decimal], closed: Sequence[tuple[Decimal, Decimal]]) -> bool:
    for a, b in zip(closed, closed[1:]):
        if _on_segment(a, b, point):
            return True
    x, y = point
    inside = False
    for a, b in zip(closed, closed[1:]):
        ay, by = a[1], b[1]
        if (ay > y) == (by > y):
            continue
        with localcontext() as ctx:
            ctx.prec = 50
            x_intersection = a[0] + (y - ay) * (b[0] - a[0]) / (by - ay)
        if x_intersection > x:
            inside = not inside
    return inside


def _point_in_convex(point: tuple[Decimal, Decimal], hull: Sequence[tuple[Decimal, Decimal]]) -> bool:
    signs: set[int] = set()
    closed = list(hull) + [hull[0]]
    for a, b in zip(closed, closed[1:]):
        sign = _orientation(a, b, point)
        if sign:
            signs.add(sign)
            if len(signs) > 1:
                return False
    return True


def _distance(a: tuple[Decimal, Decimal], b: tuple[Decimal, Decimal]) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = 50
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2).sqrt()


def _point_segment_distance(point: tuple[Decimal, Decimal], a: tuple[Decimal, Decimal], b: tuple[Decimal, Decimal]) -> Decimal:
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    length2 = dx * dx + dy * dy
    if length2 <= EPS:
        return _distance(point, a)
    t = ((point[0] - a[0]) * dx + (point[1] - a[1]) * dy) / length2
    t = max(Decimal(0), min(Decimal(1), t))
    projection = (a[0] + t * dx, a[1] + t * dy)
    return _distance(point, projection)


def _distance_to_hull(point: tuple[Decimal, Decimal], hull: Sequence[tuple[Decimal, Decimal]]) -> Decimal:
    if _point_in_convex(point, hull):
        return Decimal(0)
    closed = list(hull) + [hull[0]]
    return min(_point_segment_distance(point, a, b) for a, b in zip(closed, closed[1:]))


def _round(value: Decimal) -> float:
    return float(value.quantize(Q, rounding=ROUND_HALF_EVEN))


def compute_metrics(candidate: Mapping[str, Any]) -> Metrics:
    support = candidate["support"]
    mask = [_point(item) for item in support["resource_mask"]]
    if mask[0] != mask[-1]:
        raise ValueError("RESOURCE_MASK_OPEN")
    if len(set(mask[:-1])) < 3 or _polygon_area(mask) <= EPS:
        raise ValueError("RESOURCE_MASK_DEGENERATE")
    if not _mask_is_simple(mask):
        raise ValueError("RESOURCE_MASK_SELF_INTERSECTION")

    width = _d(support["resource_width_px"])
    height = _d(support["resource_height_px"])
    if any(x < -EPS or x > width + EPS or y < -EPS or y > height + EPS for x, y in mask[:-1]):
        raise ValueError("RESOURCE_MASK_OUT_OF_BOUNDS")

    gcps = candidate["gcps"]
    resources = [_point(item["resource"]) for item in gcps]
    if len(set(resources)) != len(resources):
        raise ValueError("DUPLICATE_RESOURCE_GCP")
    if any(not _point_in_polygon(point, mask) for point in resources):
        raise ValueError("GCP_OUTSIDE_RESOURCE_MASK")

    hull = _convex_hull(resources)
    support_area = _polygon_area(mask)
    hull_area = _polygon_area(hull + [hull[0]])
    hull_ratio = hull_area / support_area

    min_x = min(point[0] for point in mask[:-1])
    max_x = max(point[0] for point in mask[:-1])
    min_y = min(point[1] for point in mask[:-1])
    max_y = max(point[1] for point in mask[:-1])
    diagonal = _distance((min_x, min_y), (max_x, max_y))
    if diagonal <= EPS:
        raise ValueError("RESOURCE_MASK_DEGENERATE")
    extrapolation = max(_distance_to_hull(point, hull) for point in mask[:-1]) / diagonal

    support_centroid = _polygon_centroid(mask)
    gcp_centroid = (
        sum((point[0] for point in resources), Decimal(0)) / Decimal(len(resources)),
        sum((point[1] for point in resources), Decimal(0)) / Decimal(len(resources)),
    )
    centroid_offset = _distance(support_centroid, gcp_centroid) / diagonal

    quadrants: set[tuple[int, int]] = set()
    for x, y in resources:
        dx = x - support_centroid[0]
        dy = y - support_centroid[1]
        if abs(dx) <= EPS or abs(dy) <= EPS:
            continue
        quadrants.add((1 if dx > 0 else -1, 1 if dy > 0 else -1))

    return Metrics(
        hull_vertex_count=len(hull),
        hull_area_ratio=hull_ratio,
        max_extrapolation_ratio=extrapolation,
        centroid_offset_ratio=centroid_offset,
        occupied_quadrants=len(quadrants),
    )


def _declared(metrics: Metrics) -> dict[str, Any]:
    return {
        "hull_vertex_count": metrics.hull_vertex_count,
        "hull_area_ratio": _round(metrics.hull_area_ratio),
        "max_extrapolation_ratio": _round(metrics.max_extrapolation_ratio),
        "centroid_offset_ratio": _round(metrics.centroid_offset_ratio),
        "occupied_quadrants": metrics.occupied_quadrants,
    }


def derive(candidate: Mapping[str, Any]) -> Result:
    if candidate["gcp_count"] != len(candidate["gcps"]):
        return Result("ERROR", ("GCP_COUNT_MISMATCH",))
    try:
        metrics = compute_metrics(candidate)
    except ValueError as exc:
        return Result("ERROR", (str(exc),))
    if candidate["computed"] != _declared(metrics):
        return Result("ERROR", ("METRIC_MISMATCH",))

    thresholds = candidate["thresholds"]
    reasons: list[str] = []
    if candidate["gcp_count"] < thresholds["minimum_gcps"]:
        reasons.append("INSUFFICIENT_GCPS")
    if metrics.hull_area_ratio < _d(thresholds["min_hull_area_ratio"]):
        reasons.append("HULL_COVERAGE_LOW")
    if metrics.max_extrapolation_ratio > _d(thresholds["max_extrapolation_ratio"]):
        reasons.append("EXTRAPOLATION_RISK_HIGH")
    if metrics.centroid_offset_ratio > _d(thresholds["max_centroid_offset_ratio"]):
        reasons.append("CENTROID_OFFSET_HIGH")
    if metrics.occupied_quadrants < thresholds["minimum_occupied_quadrants"]:
        reasons.append("QUADRANT_COVERAGE_LOW")
    if reasons:
        return Result("HOLD", tuple(sorted(reasons)))
    return Result("READY", ("GCP_SPATIAL_DISTRIBUTION_READY",))


def validate_candidate(candidate: Any) -> Result:
    if not isinstance(candidate, Mapping):
        return Result("ERROR", ("ROOT_NOT_OBJECT",))
    if _schema_errors(candidate):
        return Result("ERROR", ("SCHEMA_INVALID",))
    result = derive(candidate)
    decision = candidate["decision"]
    if decision["outcome"] != result.outcome or decision["reasons"] != list(result.reasons):
        return Result("ERROR", ("DECISION_MISMATCH",))
    return result


def _parts(pointer: str) -> list[str]:
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ValueError("invalid pointer")
    if pointer == "/":
        return []
    return [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]


def _set(obj: dict[str, Any], pointer: str, value: Any) -> None:
    parts = _parts(pointer)
    target: Any = obj
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    leaf = parts[-1]
    if isinstance(target, list):
        target[int(leaf)] = copy.deepcopy(value)
    else:
        target[leaf] = copy.deepcopy(value)


def _truncate(obj: dict[str, Any], pointer: str, length: int) -> None:
    target: Any = obj
    for part in _parts(pointer):
        target = target[int(part)] if isinstance(target, list) else target[part]
    if not isinstance(target, list) or not isinstance(length, int) or length < 0:
        raise ValueError("invalid truncate mutation")
    del target[length:]


def materialize_case(manifest: Mapping[str, Any], entry: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(manifest["base_candidate"])
    for mutation in entry.get("mutations", []):
        operation = mutation.get("op", "set")
        if operation == "set":
            _set(candidate, mutation["path"], mutation["value"])
        elif operation == "truncate":
            _truncate(candidate, mutation["path"], mutation["length"])
        else:
            raise ValueError("unsupported mutation")
    if entry.get("recompute", False):
        candidate["gcp_count"] = len(candidate["gcps"])
        try:
            candidate["computed"] = _declared(compute_metrics(candidate))
        except ValueError:
            pass
    if "decision" in entry:
        candidate["decision"] = copy.deepcopy(entry["decision"])
    return candidate


def validate_fixtures() -> int:
    value, error = _read(FIXTURE_PATH)
    if error or not isinstance(value, dict) or not isinstance(value.get("cases"), list):
        print("ERROR: fixture manifest invalid")
        return 1
    failed = False
    outcomes: set[str] = set()
    for entry in value["cases"]:
        candidate = materialize_case(value, entry)
        result = validate_candidate(candidate)
        actual = {"outcome": result.outcome, "reasons": list(result.reasons)}
        print(json.dumps({"case_id": entry["case_id"], **actual}, sort_keys=True, separators=(",", ":")))
        if actual != entry["expected"]:
            failed = True
        outcomes.add(result.outcome)
    if outcomes != {"READY", "HOLD", "ERROR"}:
        failed = True
    if failed:
        return 1
    print(f"CONFIRMED: {len(value['cases'])} georeference spatial-distribution cases passed exact polarity.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only GCP spatial distribution.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        return validate_fixtures()
    if not args.files:
        parser.error("provide files or --fixtures")
    failed = False
    for path in args.files:
        value, error = _read(path)
        result = Result("ERROR", (error,)) if error else validate_candidate(value)
        print(json.dumps({"file": path.name, "outcome": result.outcome, "reasons": list(result.reasons)}, sort_keys=True, separators=(",", ":")))
        failed = failed or result.outcome != "READY"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
