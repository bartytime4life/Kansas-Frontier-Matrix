"""Validate the canonical KWO RAC geometry and county-crosswalk records.

The validator is deterministic and no-network.  It checks checked-in bytes and
their registry metadata; source refresh and spatial derivation are separate
operations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


DATASET_RECORD_PATH = Path(
    "data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json"
)
CROSSWALK_RECORD_PATH = Path(
    "data/registry/crosswalks/water_planning/"
    "kwo_rac_counties_2026-06-24__tiger2025.json"
)
GEOMETRY_PATH = Path(
    "data/processed/water_planning/rac_regions/"
    "kwo_rac_regions_2026-06-24.geojson"
)
KWO_SOURCE_RECORD_PATH = Path(
    "data/registry/sources/water_planning/"
    "kwo_rac_feature_service.source.json"
)
CENSUS_SOURCE_RECORD_PATH = Path(
    "data/registry/sources/water_planning/"
    "census_tigerweb_counties_2025.source.json"
)

EXPECTED_REGION_NAMES = (
    "Cimarron",
    "Equus-Walnut",
    "Great Bend Prairie",
    "Kansas",
    "Marais des Cygnes",
    "Missouri",
    "Neosho",
    "Red Hills",
    "Smoky Hill-Saline",
    "Solomon-Republican",
    "Upper Arkansas",
    "Upper Republican",
    "Upper Smoky Hill",
    "Verdigris",
)
EXPECTED_REGION_IDS = tuple(
    f"kwo-rac-{number:02d}" for number in range(1, 15)
)
EXPECTED_REGION_NAME_BY_ID = dict(zip(EXPECTED_REGION_IDS, EXPECTED_REGION_NAMES))
EXPECTED_COUNTY_GEOIDS = tuple(f"20{number:03d}" for number in range(1, 210, 2))

DATASET_ID = "kfm:dataset:water-planning:kwo-rac-regions"
DATASET_VERSION_ID = (
    "kfm:dataset-version:water-planning:kwo-rac-regions:2026-06-24"
)
CROSSWALK_ID = (
    "kfm:crosswalk:water-planning:kwo-rac-to-county:2026-06-24:tiger-2025"
)
GEOMETRY_AUTHORITY_ID = (
    "kwo:geometry:regional-planning-areas:"
    "cd87ef7a0bb34cc4a7f57e662d73ec0f:0"
)
RPA_SOURCE_SHA256 = (
    "sha256:872b53126963b9f580dc07f53b89b307678c37ee09af2c51dec5600afddd245a"
)
COUNTY_SOURCE_SHA256 = (
    "sha256:3cf20296abdd36e189d77b32997887dc8c77efbb5d9960d32870cf53a929d694"
)
EXPECTED_MAPPING_DIGEST = (
    "sha256:2f1c713d996cca97bc6cc3b553e25e2045d986399b6232378d69f9b903f08c74"
)
EXPECTED_MAPPING_COUNT = 209
EXPECTED_OVERLAP_CLASS_COUNTS = {
    "dominant": 50,
    "material-partial": 122,
    "boundary-sliver": 37,
}
EXPECTED_EXCLUDED_SLIVER_COUNT = 5

EXPECTED_GEOMETRY_SHA256 = (
    "sha256:545b18b1b49a68c6359fefb80f8e8b80f885a94381dc87e0ef942eb8829cb738"
)
EXPECTED_GEOMETRY_BYTE_COUNT = 9_995_739

DIGEST_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
DATETIME_PATTERN = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\+00:00$"
)
REGION_ID_PATTERN = re.compile(r"^kwo-rac-(0[1-9]|1[0-4])$")
COUNTY_GEOID_PATTERN = re.compile(r"^20[0-9]{3}$")
MAX_RECORD_BYTES = 1_000_000
MAX_GEOMETRY_BYTES = 12_000_000

DATASET_FIELDS = frozenset(
    {
        "record_type",
        "schema_version",
        "dataset_id",
        "dataset_version_id",
        "record_status",
        "release_status",
        "authority_kind",
        "source",
        "payload",
        "identity_authority_ref",
        "region_ids",
        "crosswalk_refs",
        "rights_status",
        "sensitivity_status",
        "correction_status",
        "supersedes_ref",
    }
)
DATASET_SOURCE_FIELDS = frozenset(
    {
        "descriptor_ref",
        "authority_id",
        "agency",
        "source_role",
        "item_id",
        "item_owner",
        "item_url",
        "layer_url",
        "query_url",
        "source_modified_at",
        "source_observed_at",
        "source_geojson_sha256",
        "source_license_statement",
    }
)
PAYLOAD_FIELDS = frozenset(
    {
        "path",
        "media_type",
        "coordinate_reference_system",
        "sha256",
        "byte_count",
        "feature_count",
    }
)
CROSSWALK_FIELDS = frozenset(
    {
        "record_type",
        "schema_version",
        "crosswalk_id",
        "record_status",
        "release_status",
        "mapping_semantics",
        "region_dataset_ref",
        "county_source",
        "derivation",
        "mapping_digest",
        "mapping_count",
        "county_count",
        "region_count",
        "mappings",
        "correction_status",
        "supersedes_ref",
    }
)
COUNTY_SOURCE_FIELDS = frozenset(
    {
        "descriptor_ref",
        "authority_id",
        "agency",
        "layer_name",
        "vintage",
        "layer_url",
        "query_url",
        "source_geojson_sha256",
        "source_observed_at",
    }
)
DERIVATION_FIELDS = frozenset(
    {
        "method",
        "area_crs",
        "geometry_engine",
        "projection_engine",
        "minimum_intersection_area_sq_m",
        "minimum_county_area_share",
        "material_county_minimum_area_share",
        "dominant_county_minimum_area_share",
        "line_or_point_touches_included",
        "excluded_sliver_count",
    }
)
MAPPING_FIELDS = frozenset(
    {
        "county_geoid",
        "county_name",
        "region_ref",
        "relation",
        "overlap_class",
        "county_area_share",
        "region_area_share",
        "intersection_area_sq_km",
    }
)
GEOMETRY_FIELDS = frozenset(
    {"type", "bbox", "kfm_provenance", "features"}
)
GEOMETRY_PROVENANCE_FIELDS = frozenset(
    {
        "authority_id",
        "source_item_id",
        "source_item_owner",
        "source_layer_id",
        "source_modified_at",
        "coordinate_reference_system",
        "coordinate_transformation",
        "property_projection",
    }
)
FEATURE_FIELDS = frozenset({"type", "id", "properties", "geometry"})
FEATURE_PROPERTY_FIELDS = frozenset(
    {
        "region_id",
        "name",
        "rac_number",
        "source_feature_id",
        "source_name",
        "source_abbreviation",
    }
)


@dataclass(frozen=True)
class Finding:
    """Finite, stable, non-echoing validation result."""

    code: str
    path: str


def canonical_json_bytes(value: Any, *, trailing_newline: bool = False) -> bytes:
    data = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return data + (b"\n" if trailing_newline else b"")


def _add(findings: list[Finding], code: str, path: str) -> None:
    findings.append(Finding(code=code, path=path))


def _finish(findings: Iterable[Finding]) -> tuple[Finding, ...]:
    return tuple(
        sorted(set(findings), key=lambda finding: (finding.path, finding.code))
    )


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _is_sequence(value: Any) -> bool:
    return isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    )


def _exact_fields(
    value: Any,
    expected: frozenset[str],
    path: str,
    findings: list[Finding],
) -> bool:
    if not _is_mapping(value):
        _add(findings, "OBJECT_REQUIRED", path)
        return False
    for key in sorted(expected - set(value)):
        _add(findings, "FIELD_REQUIRED", f"{path}.{key}")
    for key in sorted(set(value) - expected):
        _add(findings, "UNEXPECTED_FIELD", f"{path}.{key}")
    return True


def _expect(
    actual: Any,
    expected: Any,
    code: str,
    path: str,
    findings: list[Finding],
) -> None:
    if actual != expected:
        _add(findings, code, path)


def _valid_digest(value: Any) -> bool:
    return isinstance(value, str) and DIGEST_PATTERN.fullmatch(value) is not None


def _valid_share(value: Any) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
        and 0 < value <= 1
    )


def _expected_overlap_class(county_share: float) -> str:
    if county_share >= 0.999:
        return "dominant"
    if county_share >= 0.001:
        return "material-partial"
    return "boundary-sliver"


def _validate_dataset(
    dataset: Any,
    geometry_bytes: bytes,
    findings: list[Finding],
) -> None:
    if not _exact_fields(dataset, DATASET_FIELDS, "$.dataset", findings):
        return
    _expect(
        dataset.get("record_type"),
        "water-planning-rac-geometry-dataset",
        "DATASET_RECORD_TYPE_INVALID",
        "$.dataset.record_type",
        findings,
    )
    _expect(
        dataset.get("schema_version"),
        "1.0.0",
        "SCHEMA_VERSION_INVALID",
        "$.dataset.schema_version",
        findings,
    )
    _expect(
        dataset.get("dataset_id"),
        DATASET_ID,
        "DATASET_ID_INVALID",
        "$.dataset.dataset_id",
        findings,
    )
    _expect(
        dataset.get("dataset_version_id"),
        DATASET_VERSION_ID,
        "DATASET_VERSION_ID_INVALID",
        "$.dataset.dataset_version_id",
        findings,
    )
    for field, expected, code in (
        ("record_status", "current", "RECORD_STATUS_INVALID"),
        ("release_status", "not-released", "RELEASE_STATUS_INVALID"),
        (
            "authority_kind",
            "regional-planning-area-boundary",
            "AUTHORITY_KIND_INVALID",
        ),
        (
            "identity_authority_ref",
            "kwo:rac:regional-advisory-committees",
            "IDENTITY_AUTHORITY_REF_INVALID",
        ),
        (
            "rights_status",
            "source-statement-recorded-review-pending",
            "RIGHTS_STATUS_INVALID",
        ),
        (
            "sensitivity_status",
            "public-administrative-boundary",
            "SENSITIVITY_STATUS_INVALID",
        ),
        ("correction_status", "current", "CORRECTION_STATUS_INVALID"),
        ("supersedes_ref", None, "SUPERSEDES_REF_INVALID"),
    ):
        _expect(
            dataset.get(field),
            expected,
            code,
            f"$.dataset.{field}",
            findings,
        )
    _expect(
        dataset.get("region_ids"),
        list(EXPECTED_REGION_IDS),
        "REGION_ID_INVENTORY_INVALID",
        "$.dataset.region_ids",
        findings,
    )
    _expect(
        dataset.get("crosswalk_refs"),
        [CROSSWALK_ID],
        "CROSSWALK_REF_INVALID",
        "$.dataset.crosswalk_refs",
        findings,
    )

    source = dataset.get("source")
    if _exact_fields(source, DATASET_SOURCE_FIELDS, "$.dataset.source", findings):
        expected_source_values = {
            "descriptor_ref": "kfm://source/kansas/kwo/regional-planning-areas",
            "authority_id": GEOMETRY_AUTHORITY_ID,
            "agency": "Kansas Water Office",
            "source_role": "official-administrative-planning-boundary",
            "item_id": "cd87ef7a0bb34cc4a7f57e662d73ec0f",
            "item_owner": "ks_wateroffice",
            "item_url": (
                "https://www.arcgis.com/home/item.html"
                "?id=cd87ef7a0bb34cc4a7f57e662d73ec0f"
            ),
            "layer_url": (
                "https://services1.arcgis.com/q2CglofYX6ACNEeu/arcgis/rest/"
                "services/Regional_Planning_Area/FeatureServer/0"
            ),
            "source_modified_at": "2026-06-24T15:17:37+00:00",
            "source_geojson_sha256": RPA_SOURCE_SHA256,
        }
        for field, expected in expected_source_values.items():
            _expect(
                source.get(field),
                expected,
                "DATASET_SOURCE_INVALID",
                f"$.dataset.source.{field}",
                findings,
            )
        observed = source.get("source_observed_at")
        if not isinstance(observed, str) or DATETIME_PATTERN.fullmatch(observed) is None:
            _add(
                findings,
                "SOURCE_OBSERVED_AT_INVALID",
                "$.dataset.source.source_observed_at",
            )
        query_url = source.get("query_url")
        if not isinstance(query_url, str) or not query_url.startswith(
            expected_source_values["layer_url"] + "/query?"
        ):
            _add(findings, "DATASET_SOURCE_INVALID", "$.dataset.source.query_url")
        if not isinstance(source.get("source_license_statement"), str) or not source[
            "source_license_statement"
        ].strip():
            _add(
                findings,
                "SOURCE_LICENSE_STATEMENT_REQUIRED",
                "$.dataset.source.source_license_statement",
            )

    payload = dataset.get("payload")
    if _exact_fields(payload, PAYLOAD_FIELDS, "$.dataset.payload", findings):
        expected_payload_values = {
            "path": GEOMETRY_PATH.as_posix(),
            "media_type": "application/geo+json",
            "coordinate_reference_system": "OGC:CRS84",
            "feature_count": 14,
        }
        for field, expected in expected_payload_values.items():
            _expect(
                payload.get(field),
                expected,
                "PAYLOAD_METADATA_INVALID",
                f"$.dataset.payload.{field}",
                findings,
            )
        digest = "sha256:" + hashlib.sha256(geometry_bytes).hexdigest()
        _expect(
            payload.get("sha256"),
            digest,
            "GEOMETRY_DIGEST_MISMATCH",
            "$.dataset.payload.sha256",
            findings,
        )
        _expect(
            payload.get("sha256"),
            EXPECTED_GEOMETRY_SHA256,
            "GEOMETRY_BASELINE_DIGEST_INVALID",
            "$.dataset.payload.sha256",
            findings,
        )
        _expect(
            payload.get("byte_count"),
            len(geometry_bytes),
            "GEOMETRY_BYTE_COUNT_MISMATCH",
            "$.dataset.payload.byte_count",
            findings,
        )
        _expect(
            payload.get("byte_count"),
            EXPECTED_GEOMETRY_BYTE_COUNT,
            "GEOMETRY_BASELINE_SIZE_INVALID",
            "$.dataset.payload.byte_count",
            findings,
        )


def _validate_geometry(
    geometry: Any,
    findings: list[Finding],
) -> None:
    if not _exact_fields(geometry, GEOMETRY_FIELDS, "$.geometry", findings):
        return
    _expect(
        geometry.get("type"),
        "FeatureCollection",
        "GEOMETRY_COLLECTION_TYPE_INVALID",
        "$.geometry.type",
        findings,
    )
    provenance = geometry.get("kfm_provenance")
    if _exact_fields(
        provenance,
        GEOMETRY_PROVENANCE_FIELDS,
        "$.geometry.kfm_provenance",
        findings,
    ):
        expected = {
            "authority_id": GEOMETRY_AUTHORITY_ID,
            "source_item_id": "cd87ef7a0bb34cc4a7f57e662d73ec0f",
            "source_item_owner": "ks_wateroffice",
            "source_layer_id": 0,
            "source_modified_at": "2026-06-24T15:17:37+00:00",
            "coordinate_reference_system": "OGC:CRS84",
            "coordinate_transformation": (
                "ArcGIS outSR=4326; coordinates otherwise preserved"
            ),
            "property_projection": (
                "KFM identity plus source FID, name, and abbreviation"
            ),
        }
        for field, value in expected.items():
            _expect(
                provenance.get(field),
                value,
                "GEOMETRY_PROVENANCE_INVALID",
                f"$.geometry.kfm_provenance.{field}",
                findings,
            )

    features = geometry.get("features")
    if not _is_sequence(features):
        _add(findings, "FEATURE_ARRAY_REQUIRED", "$.geometry.features")
        return
    if len(features) != 14:
        _add(findings, "FEATURE_COUNT_NOT_14", "$.geometry.features")

    seen_ids: list[str] = []
    coordinate_bounds = [math.inf, math.inf, -math.inf, -math.inf]

    def scan_coordinates(value: Any, path: str) -> None:
        if not _is_sequence(value) or not value:
            _add(findings, "COORDINATE_ARRAY_INVALID", path)
            return
        if all(
            isinstance(item, (int, float)) and not isinstance(item, bool)
            for item in value
        ):
            if len(value) != 2 or not all(math.isfinite(item) for item in value):
                _add(findings, "COORDINATE_POSITION_INVALID", path)
                return
            lon, lat = value
            if not (-180 <= lon <= 180) or not (-90 <= lat <= 90):
                _add(findings, "COORDINATE_OUT_OF_RANGE", path)
                return
            coordinate_bounds[0] = min(coordinate_bounds[0], lon)
            coordinate_bounds[1] = min(coordinate_bounds[1], lat)
            coordinate_bounds[2] = max(coordinate_bounds[2], lon)
            coordinate_bounds[3] = max(coordinate_bounds[3], lat)
            return
        for index, child in enumerate(value):
            scan_coordinates(child, f"{path}[{index}]")

    for index, feature in enumerate(features):
        path = f"$.geometry.features[{index}]"
        if not _exact_fields(feature, FEATURE_FIELDS, path, findings):
            continue
        _expect(
            feature.get("type"),
            "Feature",
            "FEATURE_TYPE_INVALID",
            f"{path}.type",
            findings,
        )
        properties = feature.get("properties")
        if not _exact_fields(
            properties, FEATURE_PROPERTY_FIELDS, f"{path}.properties", findings
        ):
            continue
        region_id = properties.get("region_id")
        seen_ids.append(region_id)
        expected_id = EXPECTED_REGION_IDS[index] if index < 14 else None
        _expect(
            region_id,
            expected_id,
            "FEATURE_ORDER_OR_ID_INVALID",
            f"{path}.properties.region_id",
            findings,
        )
        _expect(
            feature.get("id"),
            region_id,
            "FEATURE_ID_REF_MISMATCH",
            f"{path}.id",
            findings,
        )
        if region_id in EXPECTED_REGION_NAME_BY_ID:
            _expect(
                properties.get("name"),
                EXPECTED_REGION_NAME_BY_ID[region_id],
                "FEATURE_NAME_INVALID",
                f"{path}.properties.name",
                findings,
            )
            _expect(
                properties.get("source_name"),
                EXPECTED_REGION_NAME_BY_ID[region_id],
                "FEATURE_SOURCE_NAME_INVALID",
                f"{path}.properties.source_name",
                findings,
            )
            _expect(
                properties.get("rac_number"),
                EXPECTED_REGION_IDS.index(region_id) + 1,
                "FEATURE_RAC_NUMBER_INVALID",
                f"{path}.properties.rac_number",
                findings,
            )
        elif not isinstance(region_id, str) or REGION_ID_PATTERN.fullmatch(
            region_id
        ) is None:
            _add(
                findings,
                "FEATURE_REGION_ID_INVALID",
                f"{path}.properties.region_id",
            )
        if not isinstance(properties.get("source_feature_id"), int):
            _add(
                findings,
                "SOURCE_FEATURE_ID_INVALID",
                f"{path}.properties.source_feature_id",
            )
        if not isinstance(properties.get("source_abbreviation"), str) or not properties[
            "source_abbreviation"
        ].strip():
            _add(
                findings,
                "SOURCE_ABBREVIATION_INVALID",
                f"{path}.properties.source_abbreviation",
            )

        feature_geometry = feature.get("geometry")
        if not _is_mapping(feature_geometry):
            _add(findings, "FEATURE_GEOMETRY_REQUIRED", f"{path}.geometry")
            continue
        if set(feature_geometry) != {"type", "coordinates"}:
            _add(findings, "FEATURE_GEOMETRY_SHAPE_INVALID", f"{path}.geometry")
        if feature_geometry.get("type") not in {"Polygon", "MultiPolygon"}:
            _add(
                findings,
                "FEATURE_GEOMETRY_TYPE_INVALID",
                f"{path}.geometry.type",
            )
        scan_coordinates(
            feature_geometry.get("coordinates"),
            f"{path}.geometry.coordinates",
        )

    if seen_ids != list(EXPECTED_REGION_IDS):
        _add(findings, "FEATURE_REGION_INVENTORY_INVALID", "$.geometry.features")
    if len(seen_ids) != len(set(seen_ids)):
        _add(findings, "FEATURE_REGION_ID_DUPLICATE", "$.geometry.features")

    bbox = geometry.get("bbox")
    if (
        not _is_sequence(bbox)
        or len(bbox) != 4
        or not all(
            isinstance(item, (int, float))
            and not isinstance(item, bool)
            and math.isfinite(item)
            for item in bbox
        )
    ):
        _add(findings, "BBOX_INVALID", "$.geometry.bbox")
    elif all(math.isfinite(item) for item in coordinate_bounds):
        for index, (actual, expected) in enumerate(zip(bbox, coordinate_bounds)):
            if actual != expected:
                _add(findings, "BBOX_COORDINATE_MISMATCH", f"$.geometry.bbox[{index}]")


def _validate_crosswalk(crosswalk: Any, findings: list[Finding]) -> None:
    if not _exact_fields(crosswalk, CROSSWALK_FIELDS, "$.crosswalk", findings):
        return
    expected_values = {
        "record_type": "water-planning-rac-county-crosswalk",
        "schema_version": "1.0.0",
        "crosswalk_id": CROSSWALK_ID,
        "record_status": "current",
        "release_status": "not-released",
        "region_dataset_ref": DATASET_VERSION_ID,
        "mapping_digest": EXPECTED_MAPPING_DIGEST,
        "mapping_count": EXPECTED_MAPPING_COUNT,
        "county_count": 105,
        "region_count": 14,
        "correction_status": "current",
        "supersedes_ref": None,
    }
    for field, expected in expected_values.items():
        _expect(
            crosswalk.get(field),
            expected,
            "CROSSWALK_METADATA_INVALID",
            f"$.crosswalk.{field}",
            findings,
        )
    semantics = crosswalk.get("mapping_semantics")
    if (
        not isinstance(semantics, str)
        or "do not claim political, administrative, or governance membership"
        not in semantics
    ):
        _add(
            findings,
            "MAPPING_SEMANTICS_WEAKENED",
            "$.crosswalk.mapping_semantics",
        )

    source = crosswalk.get("county_source")
    if _exact_fields(
        source, COUNTY_SOURCE_FIELDS, "$.crosswalk.county_source", findings
    ):
        expected_source = {
            "descriptor_ref": (
                "kfm://source/us/census/tigerweb/state-county-2025"
            ),
            "authority_id": "census:tigerweb:state-county:2025",
            "agency": "U.S. Census Bureau",
            "layer_name": "Counties",
            "vintage": "2025-01-01",
            "layer_url": (
                "https://tigerweb.geo.census.gov/arcgis/rest/services/"
                "TIGERweb/State_County/MapServer/1"
            ),
            "source_geojson_sha256": COUNTY_SOURCE_SHA256,
        }
        for field, expected in expected_source.items():
            _expect(
                source.get(field),
                expected,
                "COUNTY_SOURCE_INVALID",
                f"$.crosswalk.county_source.{field}",
                findings,
            )
        observed = source.get("source_observed_at")
        if not isinstance(observed, str) or DATETIME_PATTERN.fullmatch(observed) is None:
            _add(
                findings,
                "SOURCE_OBSERVED_AT_INVALID",
                "$.crosswalk.county_source.source_observed_at",
            )
        query_url = source.get("query_url")
        if not isinstance(query_url, str) or not query_url.startswith(
            expected_source["layer_url"] + "/query?"
        ):
            _add(
                findings,
                "COUNTY_SOURCE_INVALID",
                "$.crosswalk.county_source.query_url",
            )

    derivation = crosswalk.get("derivation")
    if _exact_fields(
        derivation, DERIVATION_FIELDS, "$.crosswalk.derivation", findings
    ):
        expected_derivation = {
            "method": "polygon-intersection",
            "area_crs": "EPSG:5070",
            "geometry_engine": "shapely-2.1.1",
            "projection_engine": "pyproj-3.7.1",
            "minimum_intersection_area_sq_m": 10000.0,
            "minimum_county_area_share": 0.000001,
            "material_county_minimum_area_share": 0.001,
            "dominant_county_minimum_area_share": 0.999,
            "line_or_point_touches_included": False,
            "excluded_sliver_count": EXPECTED_EXCLUDED_SLIVER_COUNT,
        }
        for field, expected in expected_derivation.items():
            _expect(
                derivation.get(field),
                expected,
                "DERIVATION_METADATA_INVALID",
                f"$.crosswalk.derivation.{field}",
                findings,
            )

    mappings = crosswalk.get("mappings")
    if not _is_sequence(mappings):
        _add(findings, "MAPPING_ARRAY_REQUIRED", "$.crosswalk.mappings")
        return
    if len(mappings) != EXPECTED_MAPPING_COUNT:
        _add(findings, "MAPPING_COUNT_INVALID", "$.crosswalk.mappings")
    if crosswalk.get("mapping_count") != len(mappings):
        _add(findings, "MAPPING_COUNT_MISMATCH", "$.crosswalk.mapping_count")
    mapping_digest = "sha256:" + hashlib.sha256(
        canonical_json_bytes(mappings)
    ).hexdigest()
    if crosswalk.get("mapping_digest") != mapping_digest:
        _add(findings, "MAPPING_DIGEST_MISMATCH", "$.crosswalk.mapping_digest")

    keys: list[tuple[str, str]] = []
    county_geoids: set[str] = set()
    region_ids: set[str] = set()
    overlap_classes: Counter[str] = Counter()
    for index, row in enumerate(mappings):
        path = f"$.crosswalk.mappings[{index}]"
        if not _exact_fields(row, MAPPING_FIELDS, path, findings):
            continue
        county_geoid = row.get("county_geoid")
        region_id = row.get("region_ref")
        if (
            not isinstance(county_geoid, str)
            or COUNTY_GEOID_PATTERN.fullmatch(county_geoid) is None
        ):
            _add(findings, "COUNTY_GEOID_INVALID", f"{path}.county_geoid")
        else:
            county_geoids.add(county_geoid)
        if region_id not in EXPECTED_REGION_IDS:
            _add(findings, "REGION_REF_INVALID", f"{path}.region_ref")
        else:
            region_ids.add(region_id)
        if isinstance(county_geoid, str) and isinstance(region_id, str):
            keys.append((county_geoid, region_id))
        if not isinstance(row.get("county_name"), str) or not row[
            "county_name"
        ].strip():
            _add(findings, "COUNTY_NAME_INVALID", f"{path}.county_name")
        _expect(
            row.get("relation"),
            "spatial-intersection",
            "RELATION_INVALID",
            f"{path}.relation",
            findings,
        )
        county_share = row.get("county_area_share")
        region_share = row.get("region_area_share")
        if not _valid_share(county_share):
            _add(findings, "COUNTY_AREA_SHARE_INVALID", f"{path}.county_area_share")
        if not _valid_share(region_share):
            _add(findings, "REGION_AREA_SHARE_INVALID", f"{path}.region_area_share")
        area = row.get("intersection_area_sq_km")
        if (
            not isinstance(area, (int, float))
            or isinstance(area, bool)
            or not math.isfinite(area)
            or area <= 0
        ):
            _add(
                findings,
                "INTERSECTION_AREA_INVALID",
                f"{path}.intersection_area_sq_km",
            )
        overlap_class = row.get("overlap_class")
        overlap_classes[overlap_class] += 1
        if _valid_share(county_share) and overlap_class != _expected_overlap_class(
            county_share
        ):
            _add(
                findings,
                "OVERLAP_CLASS_MISMATCH",
                f"{path}.overlap_class",
            )

    if keys != sorted(keys):
        _add(findings, "MAPPING_ORDER_INVALID", "$.crosswalk.mappings")
    if len(keys) != len(set(keys)):
        _add(findings, "MAPPING_KEY_DUPLICATE", "$.crosswalk.mappings")
    if tuple(sorted(county_geoids)) != EXPECTED_COUNTY_GEOIDS:
        _add(findings, "COUNTY_INVENTORY_INVALID", "$.crosswalk.mappings")
    if tuple(sorted(region_ids)) != EXPECTED_REGION_IDS:
        _add(findings, "REGION_INVENTORY_INVALID", "$.crosswalk.mappings")
    if dict(overlap_classes) != EXPECTED_OVERLAP_CLASS_COUNTS:
        _add(findings, "OVERLAP_CLASS_COUNTS_INVALID", "$.crosswalk.mappings")


def _validate_source_descriptor(
    descriptor: Any,
    *,
    path: str,
    expected_source_id: str,
    expected_digest: str,
    expected_upstream_version: str,
    expected_registry_path: str,
    findings: list[Finding],
) -> None:
    if not _is_mapping(descriptor):
        _add(findings, "SOURCE_DESCRIPTOR_OBJECT_REQUIRED", path)
        return
    expected = {
        "object_type": "SourceDescriptor",
        "schema_version": "v1",
        "source_id": expected_source_id,
        "descriptor_version": "1.0.0",
        "source_type": "official_government_dataset",
        "source_role": "authoritative_for_claim",
        "authority_rank": "primary_authority",
        "review_state": "needs_review",
        "release_state": "not_released",
    }
    for field, value in expected.items():
        _expect(
            descriptor.get(field),
            value,
            "SOURCE_DESCRIPTOR_METADATA_INVALID",
            f"{path}.{field}",
            findings,
        )
    rights = descriptor.get("rights")
    if not _is_mapping(rights):
        _add(findings, "SOURCE_RIGHTS_OBJECT_REQUIRED", f"{path}.rights")
    else:
        _expect(
            rights.get("rights_status"),
            "noassertion",
            "SOURCE_RIGHTS_STATUS_INVALID",
            f"{path}.rights.rights_status",
            findings,
        )
    release = descriptor.get("public_release")
    if not _is_mapping(release):
        _add(findings, "SOURCE_PUBLIC_RELEASE_OBJECT_REQUIRED", f"{path}.public_release")
    else:
        _expect(
            release.get("allowed"),
            False,
            "SOURCE_PUBLIC_RELEASE_MUST_BE_FALSE",
            f"{path}.public_release.allowed",
            findings,
        )
        _expect(
            release.get("requires_review"),
            True,
            "SOURCE_RELEASE_REVIEW_REQUIRED",
            f"{path}.public_release.requires_review",
            findings,
        )
    connectors = descriptor.get("connectors")
    if not _is_mapping(connectors):
        _add(findings, "SOURCE_CONNECTOR_STATE_REQUIRED", f"{path}.connectors")
    else:
        _expect(
            connectors.get("activation_state"),
            "disabled",
            "SOURCE_CONNECTOR_MUST_BE_DISABLED",
            f"{path}.connectors.activation_state",
            findings,
        )
    lifecycle = descriptor.get("lifecycle")
    if not _is_mapping(lifecycle):
        _add(findings, "SOURCE_LIFECYCLE_OBJECT_REQUIRED", f"{path}.lifecycle")
    else:
        _expect(
            lifecycle.get("registry_state"),
            "proposed",
            "SOURCE_REGISTRY_STATE_INVALID",
            f"{path}.lifecycle.registry_state",
            findings,
        )
    source_head = descriptor.get("source_head")
    if not _is_mapping(source_head):
        _add(findings, "SOURCE_HEAD_REQUIRED", f"{path}.source_head")
    else:
        content_identity = source_head.get("content_identity")
        if not _is_mapping(content_identity):
            _add(
                findings,
                "SOURCE_CONTENT_IDENTITY_REQUIRED",
                f"{path}.source_head.content_identity",
            )
        else:
            _expect(
                content_identity.get("content_sha256"),
                expected_digest.removeprefix("sha256:"),
                "SOURCE_CONTENT_DIGEST_INVALID",
                f"{path}.source_head.content_identity.content_sha256",
                findings,
            )
            _expect(
                content_identity.get("upstream_version"),
                expected_upstream_version,
                "SOURCE_UPSTREAM_VERSION_INVALID",
                f"{path}.source_head.content_identity.upstream_version",
                findings,
            )
    governance = descriptor.get("governance_refs")
    if not _is_mapping(governance):
        _add(findings, "SOURCE_GOVERNANCE_REF_REQUIRED", f"{path}.governance_refs")
    else:
        _expect(
            governance.get("source_registry_ref"),
            expected_registry_path,
            "SOURCE_REGISTRY_PATH_INVALID",
            f"{path}.governance_refs.source_registry_ref",
            findings,
        )


def validate_documents(
    dataset: Any,
    crosswalk: Any,
    geometry: Any,
    geometry_bytes: bytes,
    kwo_source_descriptor: Any,
    census_source_descriptor: Any,
) -> tuple[Finding, ...]:
    """Validate already-loaded canonical records and geometry."""

    findings: list[Finding] = []
    _validate_dataset(dataset, geometry_bytes, findings)
    _validate_geometry(geometry, findings)
    _validate_crosswalk(crosswalk, findings)
    _validate_source_descriptor(
        kwo_source_descriptor,
        path="$.sources.kwo",
        expected_source_id="kfm://source/kansas/kwo/regional-planning-areas",
        expected_digest=RPA_SOURCE_SHA256,
        expected_upstream_version="2026-06-24T15:17:37+00:00",
        expected_registry_path=KWO_SOURCE_RECORD_PATH.as_posix(),
        findings=findings,
    )
    _validate_source_descriptor(
        census_source_descriptor,
        path="$.sources.census",
        expected_source_id="kfm://source/us/census/tigerweb/state-county-2025",
        expected_digest=COUNTY_SOURCE_SHA256,
        expected_upstream_version="2025-01-01",
        expected_registry_path=CENSUS_SOURCE_RECORD_PATH.as_posix(),
        findings=findings,
    )
    if _is_mapping(dataset) and _is_mapping(crosswalk):
        if dataset.get("dataset_version_id") != crosswalk.get("region_dataset_ref"):
            _add(
                findings,
                "DATASET_CROSSWALK_REF_MISMATCH",
                "$.crosswalk.region_dataset_ref",
            )
        crosswalk_refs = dataset.get("crosswalk_refs")
        if (
            not _is_sequence(crosswalk_refs)
            or crosswalk.get("crosswalk_id") not in crosswalk_refs
        ):
            _add(
                findings,
                "CROSSWALK_DATASET_BACKREF_MISSING",
                "$.dataset.crosswalk_refs",
            )
        dataset_source = dataset.get("source")
        kwo_source_id = (
            kwo_source_descriptor.get("source_id")
            if _is_mapping(kwo_source_descriptor)
            else None
        )
        if (
            not _is_mapping(dataset_source)
            or dataset_source.get("descriptor_ref")
            != kwo_source_id
        ):
            _add(
                findings,
                "DATASET_SOURCE_DESCRIPTOR_REF_UNRESOLVED",
                "$.dataset.source.descriptor_ref",
            )
        county_source = crosswalk.get("county_source")
        census_source_id = (
            census_source_descriptor.get("source_id")
            if _is_mapping(census_source_descriptor)
            else None
        )
        if (
            not _is_mapping(county_source)
            or county_source.get("descriptor_ref")
            != census_source_id
        ):
            _add(
                findings,
                "COUNTY_SOURCE_DESCRIPTOR_REF_UNRESOLVED",
                "$.crosswalk.county_source.descriptor_ref",
            )
    return _finish(findings)


def _resolve_path(repo_root: Path, value: Path) -> Path:
    return value if value.is_absolute() else repo_root / value


def _read_json(
    path: Path, max_bytes: int, path_label: str, findings: list[Finding]
) -> tuple[Any | None, bytes | None]:
    if not path.is_file():
        _add(findings, "FILE_MISSING", path_label)
        return None, None
    size = path.stat().st_size
    if size <= 0 or size > max_bytes:
        _add(findings, "FILE_SIZE_INVALID", path_label)
        return None, None
    data = path.read_bytes()
    try:
        return json.loads(data), data
    except (UnicodeDecodeError, json.JSONDecodeError):
        _add(findings, "JSON_INVALID", path_label)
        return None, data


def validate_repository(
    repo_root: Path,
    *,
    dataset_record_path: Path = DATASET_RECORD_PATH,
    crosswalk_record_path: Path = CROSSWALK_RECORD_PATH,
    geometry_path: Path = GEOMETRY_PATH,
    kwo_source_record_path: Path = KWO_SOURCE_RECORD_PATH,
    census_source_record_path: Path = CENSUS_SOURCE_RECORD_PATH,
) -> tuple[Finding, ...]:
    """Load and validate the repository-owned RAC registry slice."""

    load_findings: list[Finding] = []
    dataset, _ = _read_json(
        _resolve_path(repo_root, dataset_record_path),
        MAX_RECORD_BYTES,
        "$.dataset",
        load_findings,
    )
    crosswalk, _ = _read_json(
        _resolve_path(repo_root, crosswalk_record_path),
        MAX_RECORD_BYTES,
        "$.crosswalk",
        load_findings,
    )
    geometry, geometry_bytes = _read_json(
        _resolve_path(repo_root, geometry_path),
        MAX_GEOMETRY_BYTES,
        "$.geometry",
        load_findings,
    )
    kwo_source, _ = _read_json(
        _resolve_path(repo_root, kwo_source_record_path),
        MAX_RECORD_BYTES,
        "$.sources.kwo",
        load_findings,
    )
    census_source, _ = _read_json(
        _resolve_path(repo_root, census_source_record_path),
        MAX_RECORD_BYTES,
        "$.sources.census",
        load_findings,
    )
    if load_findings:
        return _finish(load_findings)
    assert dataset is not None
    assert crosswalk is not None
    assert geometry is not None
    assert geometry_bytes is not None
    assert kwo_source is not None
    assert census_source is not None
    return validate_documents(
        dataset,
        crosswalk,
        geometry,
        geometry_bytes,
        kwo_source,
        census_source,
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[4],
    )
    parser.add_argument("--dataset-record", type=Path, default=DATASET_RECORD_PATH)
    parser.add_argument(
        "--crosswalk-record", type=Path, default=CROSSWALK_RECORD_PATH
    )
    parser.add_argument("--geometry", type=Path, default=GEOMETRY_PATH)
    parser.add_argument(
        "--kwo-source", type=Path, default=KWO_SOURCE_RECORD_PATH
    )
    parser.add_argument(
        "--census-source", type=Path, default=CENSUS_SOURCE_RECORD_PATH
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    findings = validate_repository(
        args.repo_root,
        dataset_record_path=args.dataset_record,
        crosswalk_record_path=args.crosswalk_record,
        geometry_path=args.geometry,
        kwo_source_record_path=args.kwo_source,
        census_source_record_path=args.census_source,
    )
    if findings:
        for finding in findings:
            print(f"{finding.code}\t{finding.path}")
        return 1
    print(
        "RAC_REGISTRY_OK "
        f"regions={len(EXPECTED_REGION_IDS)} "
        f"counties={len(EXPECTED_COUNTY_GEOIDS)} "
        f"mappings={EXPECTED_MAPPING_COUNT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
