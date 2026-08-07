"""Deterministic structural digests for GeoJSON Feature records.

The ``kfm-geojson-feature-digest-v1`` profile makes the caller declare a CRS,
quantizes finite coordinates with a versioned precision, strips GeoJSON foreign
members from the geometry hash domain, and hashes RFC 8785 JCS subjects with the
current ``sha256:<hex>`` grammar.

This profile intentionally does *not* reproject, repair topology, rotate polygon
rings, canonicalize line direction, sort collections, or prove spatial equality.
Those operations require a separately governed geospatial normalization contract.
Digest equality establishes only equality under this declared structural profile;
it creates no source, evidence, policy, review, promotion, release, publication,
or public-use authority.
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN, localcontext
from typing import Any

from .core import SpecHashError, compute_spec_hash

GEOJSON_DIGEST_PROFILE = "kfm-geojson-feature-digest-v1"
DEFAULT_COORDINATE_PRECISION = 7
MIN_COORDINATE_PRECISION = 0
MAX_COORDINATE_PRECISION = 15
MAX_COORDINATE_VALUES = 1_000_000
MAX_GEOMETRY_DEPTH = 32

_GEOMETRY_COORDINATE_DEPTH = {
    "Point": 1,
    "MultiPoint": 2,
    "LineString": 2,
    "MultiLineString": 3,
    "Polygon": 3,
    "MultiPolygon": 4,
}


class GeoJSONDigestError(SpecHashError):
    """Raised when a GeoJSON value cannot enter the structural digest profile."""


@dataclass(frozen=True)
class GeoJSONFeatureDigests:
    """Digest result and replay parameters for one GeoJSON Feature."""

    profile: str
    crs: str
    coordinate_precision: int
    geometry_sha256: str
    record_sha256: str
    excluded_property_keys: tuple[str, ...]
    feature_id_included: bool

    def as_dict(self) -> dict[str, object]:
        """Return a deterministic JSON-compatible report payload."""

        return {
            "profile": self.profile,
            "crs": self.crs,
            "coordinate_precision": self.coordinate_precision,
            "geometry_sha256": self.geometry_sha256,
            "record_sha256": self.record_sha256,
            "excluded_property_keys": list(self.excluded_property_keys),
            "feature_id_included": self.feature_id_included,
        }


@dataclass
class _CoordinateBudget:
    consumed: int = 0

    def add(self, amount: int) -> None:
        self.consumed += amount
        if self.consumed > MAX_COORDINATE_VALUES:
            raise GeoJSONDigestError(
                "GeoJSON geometry exceeds the coordinate-value validation budget"
            )


def _validated_precision(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise GeoJSONDigestError("coordinate precision must be an integer")
    if not MIN_COORDINATE_PRECISION <= value <= MAX_COORDINATE_PRECISION:
        raise GeoJSONDigestError(
            "coordinate precision must be between 0 and 15 decimal places"
        )
    return value


def _validated_crs(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise GeoJSONDigestError("a non-empty declared CRS is required")
    return value.strip()


def _validated_exclusions(values: Iterable[str]) -> tuple[str, ...]:
    exclusions: set[str] = set()
    for value in values:
        if not isinstance(value, str) or not value:
            raise GeoJSONDigestError(
                "excluded property keys must be non-empty strings"
            )
        exclusions.add(value)
    return tuple(sorted(exclusions))


def _quantize_coordinate(value: object, precision: int) -> int | float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise GeoJSONDigestError("GeoJSON positions must contain only JSON numbers")
    numeric = float(value)
    if not math.isfinite(numeric):
        raise GeoJSONDigestError("GeoJSON coordinates must be finite")

    try:
        with localcontext() as context:
            context.prec = 64
            quantum = Decimal(1).scaleb(-precision)
            quantized = Decimal(str(value)).quantize(
                quantum, rounding=ROUND_HALF_EVEN
            )
    except (InvalidOperation, ValueError) as exc:
        raise GeoJSONDigestError("GeoJSON coordinate could not be quantized") from exc

    if quantized == 0:
        return 0
    if quantized == quantized.to_integral_value():
        return int(quantized)
    return float(quantized)


def _normalize_position(
    value: object,
    *,
    precision: int,
    budget: _CoordinateBudget,
) -> list[int | float]:
    if not isinstance(value, list) or len(value) < 2:
        raise GeoJSONDigestError(
            "GeoJSON positions must be arrays containing at least two numbers"
        )
    budget.add(len(value))
    return [_quantize_coordinate(item, precision) for item in value]


def _normalize_coordinates(
    value: object,
    *,
    depth: int,
    precision: int,
    budget: _CoordinateBudget,
) -> object:
    if depth == 1:
        return _normalize_position(value, precision=precision, budget=budget)
    if not isinstance(value, list):
        raise GeoJSONDigestError("GeoJSON coordinate nesting does not match its type")
    return [
        _normalize_coordinates(
            item,
            depth=depth - 1,
            precision=precision,
            budget=budget,
        )
        for item in value
    ]


def _normalize_geojson_geometry(
    geometry: object,
    *,
    precision: int,
    budget: _CoordinateBudget,
    depth: int,
) -> dict[str, object] | None:
    if depth > MAX_GEOMETRY_DEPTH:
        raise GeoJSONDigestError("GeoJSON geometry exceeds the nesting limit")
    if geometry is None:
        return None
    if not isinstance(geometry, Mapping):
        raise GeoJSONDigestError("GeoJSON geometry must be an object or null")

    geometry_type = geometry.get("type")
    if not isinstance(geometry_type, str):
        raise GeoJSONDigestError("GeoJSON geometry type must be a string")

    if geometry_type == "GeometryCollection":
        members = geometry.get("geometries")
        if not isinstance(members, list):
            raise GeoJSONDigestError(
                "GeometryCollection must contain a geometries array"
            )
        normalized_members: list[dict[str, object]] = []
        for member in members:
            normalized_member = _normalize_geojson_geometry(
                member,
                precision=precision,
                budget=budget,
                depth=depth + 1,
            )
            if normalized_member is None:
                raise GeoJSONDigestError(
                    "GeometryCollection members must be geometry objects"
                )
            normalized_members.append(normalized_member)
        return {"type": geometry_type, "geometries": normalized_members}

    coordinate_depth = _GEOMETRY_COORDINATE_DEPTH.get(geometry_type)
    if coordinate_depth is None:
        raise GeoJSONDigestError(f"unsupported GeoJSON geometry type: {geometry_type}")
    if "coordinates" not in geometry:
        raise GeoJSONDigestError("GeoJSON geometry is missing coordinates")

    return {
        "type": geometry_type,
        "coordinates": _normalize_coordinates(
            geometry["coordinates"],
            depth=coordinate_depth,
            precision=precision,
            budget=budget,
        ),
    }


def normalize_geojson_geometry(
    geometry: object,
    *,
    coordinate_precision: int = DEFAULT_COORDINATE_PRECISION,
) -> dict[str, object] | None:
    """Normalize one GeoJSON geometry under the structural v1 profile.

    ``None`` is retained as a deterministic missing-geometry value. Geometry
    foreign members, including ``bbox``, are deliberately outside this hash
    domain. Coordinate and collection ordering remains significant.
    """

    precision = _validated_precision(coordinate_precision)
    return _normalize_geojson_geometry(
        geometry,
        precision=precision,
        budget=_CoordinateBudget(),
        depth=0,
    )


def _geometry_subject(
    normalized_geometry: dict[str, object] | None,
    *,
    crs: str,
    coordinate_precision: int,
) -> dict[str, object]:
    return {
        "profile": GEOJSON_DIGEST_PROFILE,
        "crs": crs,
        "coordinate_precision": coordinate_precision,
        "geometry": normalized_geometry,
    }


def compute_geojson_geometry_hash(
    geometry: object,
    *,
    crs: str,
    coordinate_precision: int = DEFAULT_COORDINATE_PRECISION,
) -> str:
    """Compute a structural geometry digest bound to CRS and precision."""

    precision = _validated_precision(coordinate_precision)
    declared_crs = _validated_crs(crs)
    normalized = normalize_geojson_geometry(
        geometry, coordinate_precision=precision
    )
    return compute_spec_hash(
        _geometry_subject(
            normalized,
            crs=declared_crs,
            coordinate_precision=precision,
        )
    )


def compute_geojson_feature_digests(
    feature: object,
    *,
    crs: str,
    coordinate_precision: int = DEFAULT_COORDINATE_PRECISION,
    excluded_property_keys: Iterable[str] = (),
    include_feature_id: bool = False,
) -> GeoJSONFeatureDigests:
    """Compute separate structural geometry and feature-record digests.

    The record hash binds the geometry hash to the Feature's top-level
    ``properties`` after only caller-declared exclusions. Feature ``id`` is
    excluded by default and can be admitted explicitly. Foreign Feature members
    are outside the v1 hash domain.
    """

    if not isinstance(feature, Mapping) or feature.get("type") != "Feature":
        raise GeoJSONDigestError("input must be a GeoJSON Feature object")
    if "geometry" not in feature:
        raise GeoJSONDigestError("GeoJSON Feature is missing geometry")
    if "properties" not in feature:
        raise GeoJSONDigestError("GeoJSON Feature is missing properties")

    properties = feature.get("properties")
    if properties is not None and not isinstance(properties, Mapping):
        raise GeoJSONDigestError("GeoJSON Feature properties must be an object or null")
    if not isinstance(include_feature_id, bool):
        raise GeoJSONDigestError("include_feature_id must be boolean")

    precision = _validated_precision(coordinate_precision)
    declared_crs = _validated_crs(crs)
    exclusions = _validated_exclusions(excluded_property_keys)

    normalized_geometry = normalize_geojson_geometry(
        feature["geometry"], coordinate_precision=precision
    )
    geometry_sha256 = compute_spec_hash(
        _geometry_subject(
            normalized_geometry,
            crs=declared_crs,
            coordinate_precision=precision,
        )
    )

    filtered_properties: dict[str, Any] | None
    if properties is None:
        filtered_properties = None
    else:
        if any(not isinstance(key, str) for key in properties):
            raise GeoJSONDigestError("GeoJSON property keys must be strings")
        filtered_properties = {
            key: value for key, value in properties.items() if key not in exclusions
        }

    record_subject: dict[str, object] = {
        "profile": GEOJSON_DIGEST_PROFILE,
        "crs": declared_crs,
        "coordinate_precision": precision,
        "geometry_sha256": geometry_sha256,
        "properties": filtered_properties,
    }
    if include_feature_id:
        record_subject["feature_id"] = feature.get("id")

    return GeoJSONFeatureDigests(
        profile=GEOJSON_DIGEST_PROFILE,
        crs=declared_crs,
        coordinate_precision=precision,
        geometry_sha256=geometry_sha256,
        record_sha256=compute_spec_hash(record_subject),
        excluded_property_keys=exclusions,
        feature_id_included=include_feature_id,
    )
