"""Validate exact, inactive, fixture-only DEM source asset candidates."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import (
    CanonicalizationFailure,
    JsonInputError,
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/spatial-foundation/dem_source_asset_candidate.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/spatial-foundation/dem_source_asset_candidate/cases.json"
PROJECTION_SNAPSHOT_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/spatial-foundation/dem_source_asset_candidate/evidence-projection-snapshot.json"
)
SCOPE = "spatial-foundation.dem-source-asset-candidate"
ZERO_DIGEST = "sha256:" + ("0" * 64)
JCS_SAFE_INTEGER_MAX = 9_007_199_254_740_991
EXPECTED_PROJECT = "KS_Statewide_2018_A18"
EXPECTED_PROJECT_ID = 76296
EXPECTED_TILE = "USGS_1M_14_x56y429_KS_Statewide_2018_A18"
EXPECTED_RASTER_LOCATOR = (
    "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/"
    "KS_Statewide_2018_A18/TIFF/"
    "USGS_1M_14_x56y429_KS_Statewide_2018_A18.tif"
)
EXPECTED_METADATA_LOCATOR = (
    "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/1m/Projects/"
    "KS_Statewide_2018_A18/metadata/"
    "USGS_1M_14_x56y429_KS_Statewide_2018_A18.xml"
)
EXPECTED_3DEP_INDEX_LOCATOR = (
    "https://index.nationalmap.gov/arcgis/rest/services/3DEPElevationIndex/"
    "MapServer/24/query?where=project+%3D+%27KS_Statewide_2018_A18%27&"
    "geometry=-98.31032245799997%2C38.66581613100004%2C-98.19437523299996%2C"
    "38.75666181200006&geometryType=esriGeometryEnvelope&inSR=4326&"
    "spatialRel=esriSpatialRelIntersects&outFields=%2A&returnGeometry=false&f=json"
)
EXPECTED_CENSUS_POINT_LOCATOR = (
    "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/"
    "MapServer/0/query?where=STUSAB%3D%27KS%27&geometry=-98.23%2C38.73&"
    "geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&"
    "outFields=GEOID%2CSTATE%2CSTUSAB%2CNAME&returnGeometry=false&f=json"
)
EXPECTED_CENSUS_COUNTY_POINT_LOCATOR = (
    "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/"
    "MapServer/1/query?where=STATE%3D%2720%27&geometry=-98.23%2C38.73&"
    "geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&"
    "outFields=GEOID%2CSTATE%2CCOUNTY%2CNAME&returnGeometry=false&f=json"
)
EXPECTED_CENSUS_METADATA_LOCATOR = (
    "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/"
    "MapServer/0?f=pjson"
)
EXPECTED_CAPTURE_BYTES = {
    "three_dep_index_query": (
        5003,
        "sha256:add44226c3e31c2f459cba04e6d66e5de06eb177b26cb79dd0f793a37bc35fd7",
    ),
    "census_state_point_query": (
        503,
        "sha256:26c87451192736bc8e0c265973b4fa80e9f5c7373fbad4d4842653c994f930e3",
    ),
    "census_county_point_query": (
        513,
        "sha256:2758b570dc4fd857948295be3a8c339ebe26db23bc573cd197e5e09e1f7fa452",
    ),
    "census_states_layer_metadata": (
        7696,
        "sha256:eb955e5bc73a565ca5249c6b7401aa003a87c4578b12169619c3d1a62c7205d2",
    ),
}
EXPECTED_PROJECTION_SNAPSHOT = (
    (
        "fixtures/contracts/v1/spatial-foundation/dem_source_asset_candidate/"
        "evidence-projection-snapshot.json"
    ),
    2_717,
    "sha256:e6d42da0f85c86b86bb7cdff682a95ad8247851d00e259ef3d2eb5bf2b9d134d",
)
EXPECTED_CAPTURE_SESSION = {
    "capture_completed_at": "2026-09-09T21:19:42Z",
    "candidate_frozen_at": "2026-09-09T22:15:51Z",
    "clock": "UTC",
    "all_capture_times_equal_completed": True,
}
EXPECTED_ASSET_BYTES = {
    "raster_tiff": (
        297_030_205,
        "sha256:8d923dc122ee99303201acb07c9fc49c190b19545a75768384f49ccb4e975cd7",
    ),
    "metadata_xml": (
        14_400,
        "sha256:b2125a3c069284a48feef0e1d9935b13ae1426ce5e7aab3e3e914c23cec00d00",
    ),
}
EXPECTED_ACCURACY_REPORT = (
    (
        "https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/metadata/"
        "KS_Statewide_2018_A18/vertical_accuracy/USGS/14/"
        "USGS_USGS_KS_Statewide_2018_UTM14_VA.txt"
    ),
    200_101,
    "sha256:21660a5f497c64430e7a8dda1613de9bd6e7329ab84f20183fc9490682f1f06e",
)
EXPECTED_INDEX_PROJECTION = {
    "feature_count": 1,
    "query_envelope": {
        "west": -98.31032245799997,
        "south": 38.66581613100004,
        "east": -98.19437523299996,
        "north": 38.75666181200006,
    },
    "project": "KS_Statewide_2018_A18",
    "project_id": 76296,
    "work_unit": "KS_Statewide_B10_2018",
    "work_unit_id": 209920,
    "collection_start": "2018-04-30",
    "collection_end": "2019-03-20",
    "quality_level": "QL 2",
    "specification": "USGS Lidar Base Specification 1.2",
    "acquisition_method": "linear-mode lidar",
    "dem_gsd_meters": 1,
    "horizontal_crs_code": 3744,
    "vertical_crs_code": 5703,
    "geoid": "GEOID12B",
    "source_dem_publication_date": "2021-07-06",
    "one_meter_category": "Meets",
}
EXPECTED_CENSUS_POINT_PROJECTION = {
    "feature_count": 1,
    "longitude": -98.23,
    "latitude": 38.73,
    "state_geoid": "20",
    "state_code": "20",
    "state_abbreviation": "KS",
    "state_name": "Kansas",
}
EXPECTED_CENSUS_COUNTY_PROJECTION = {
    "feature_count": 1,
    "longitude": -98.23,
    "latitude": 38.73,
    "county_geoid": "20053",
    "state_code": "20",
    "county_code": "053",
    "county_name": "Ellsworth County",
}
EXPECTED_ACCURACY_FACTS = (
    708,
    0.0864,
    0.1694,
    492,
    0.2397,
    True,
    "NOT_ESTABLISHED",
)
EXPECTED_GRID_FACTS = (
    10012,
    10012,
    [1, 0, 559994.0000061383, 0, -1, 4290006.000008625],
    -999999,
)
EXPECTED_SAMPLE_FACTS = (
    -98.23,
    38.73,
    566928.7523695905,
    4287096.470552446,
    2909,
    6934,
    469.4603271484375,
    [129, 213, 118],
    469.4609375,
)

GRS80_A = 6_378_137.0
GRS80_F = 1 / 298.257222101
GRS80_E2 = GRS80_F * (2 - GRS80_F)
GRS80_EP2 = GRS80_E2 / (1 - GRS80_E2)
UTM_SCALE = 0.9996
UTM_FALSE_EASTING = 500_000.0
UTM14_CENTRAL_MERIDIAN_RADIANS = math.radians(-99.0)

_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(_SCHEMA)
_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    review_outcome: str | None
    findings: tuple[Finding, ...]
    candidate_id: str | None = None


def _unsafe_numeric_findings(value: object, path: str = "$") -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    pending = [(value, path)]
    while pending:
        item, item_path = pending.pop()
        if isinstance(item, bool) or item is None:
            continue
        if isinstance(item, int):
            if abs(item) > JCS_SAFE_INTEGER_MAX:
                findings.add(Finding("NUMERIC_DOMAIN_INVALID", item_path))
        elif isinstance(item, float):
            if not math.isfinite(item) or abs(item) > JCS_SAFE_INTEGER_MAX:
                findings.add(Finding("NUMERIC_DOMAIN_INVALID", item_path))
        elif isinstance(item, list):
            pending.extend(
                (child, f"{item_path}[{index}]")
                for index, child in enumerate(item)
            )
        elif isinstance(item, dict):
            pending.extend(
                (child, f"{item_path}.{key}") for key, child in item.items()
            )
    return tuple(sorted(findings))


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _set_path(document: object, path: str, value: object) -> None:
    parts = path.split(".")
    target: object = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]  # type: ignore[index]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = value
    else:
        target[final] = value  # type: ignore[index]


def _delete_path(document: object, path: str) -> None:
    parts = path.split(".")
    target: object = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]  # type: ignore[index]
    final = parts[-1]
    if isinstance(target, list):
        del target[int(final)]
    else:
        del target[final]  # type: ignore[index]


def _identity(document: Mapping[str, Any]) -> tuple[str, str]:
    projection = {
        key: value
        for key, value in document.items()
        if key not in {"candidate_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(projection)
    return (
        "kfm:dem-source-asset-candidate:" + spec_hash.removeprefix("sha256:"),
        spec_hash,
    )


def finalize_document(document: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(dict(document))
    candidate_id, spec_hash = _identity(candidate)
    candidate["candidate_id"] = candidate_id
    candidate["spec_hash"] = spec_hash
    return candidate


def materialize_case(base_candidate: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate: dict[str, Any] = copy.deepcopy(dict(base_candidate))
    identity_inputs_changed = bool(case.get("deletions") or case.get("mutations"))
    for deletion in case.get("deletions", []):
        if not isinstance(deletion, str):
            raise TypeError("invalid deletion")
        _delete_path(candidate, deletion)
    for mutation in case.get("mutations", []):
        if not isinstance(mutation, dict) or not isinstance(mutation.get("path"), str):
            raise TypeError("invalid mutation")
        _set_path(candidate, mutation["path"], copy.deepcopy(mutation.get("value")))
    if identity_inputs_changed:
        candidate = finalize_document(candidate)
    for mutation in case.get("tamper", []):
        if not isinstance(mutation, dict) or not isinstance(mutation.get("path"), str):
            raise TypeError("invalid tamper")
        _set_path(candidate, mutation["path"], copy.deepcopy(mutation.get("value")))
    return candidate


def _date(value: object) -> date | None:
    if not isinstance(value, str):
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


def _date_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def _expected_blockers(document: Mapping[str, Any]) -> list[str]:
    blockers = {"HUMAN_REVIEW_REQUIRED"}
    temporal = document["temporal_identity"]["source_observation_interval"]
    if temporal["status"] == "UNRESOLVED":
        blockers.add("SOURCE_OBSERVATION_INTERVAL_UNRESOLVED")
    if document["delivered_crs"]["status"] == "UNRESOLVED":
        blockers.add("HORIZONTAL_CRS_REALIZATION_UNRESOLVED")
    if document["vertical_reference"]["delivered_tile_geoid"]["status"] == "UNRESOLVED":
        blockers.add("GEOID_MODEL_UNRESOLVED")
    if document["vertical_accuracy"]["status"] == "UNRESOLVED":
        blockers.add("VERTICAL_ACCURACY_UNRESOLVED")
    if document["lineage"]["status"] == "UNRESOLVED":
        blockers.add("SOURCE_LINEAGE_UNRESOLVED")
    return sorted(blockers)


def _inside(longitude: float, latitude: float, bbox: Mapping[str, float]) -> bool:
    return (
        bbox["west"] <= longitude <= bbox["east"]
        and bbox["south"] <= latitude <= bbox["north"]
    )


def _load_projection_snapshot() -> tuple[dict[str, Any] | None, bool]:
    """Load and verify the repository-owned minimized evidence projection snapshot."""

    try:
        if PROJECTION_SNAPSHOT_PATH.is_symlink() or not PROJECTION_SNAPSHOT_PATH.is_file():
            return None, False
        payload = PROJECTION_SNAPSHOT_PATH.read_bytes()
        expected_path, expected_length, expected_digest = EXPECTED_PROJECTION_SNAPSHOT
        if PROJECTION_SNAPSHOT_PATH.relative_to(REPO_ROOT).as_posix() != expected_path:
            return None, False
        if len(payload) != expected_length:
            return None, False
        if "sha256:" + hashlib.sha256(payload).hexdigest() != expected_digest:
            return None, False
        parsed = json.loads(payload)
        if not isinstance(parsed, dict):
            return None, False
        return parsed, True
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError):
        return None, False


def _utm14_forward(longitude: float, latitude: float) -> tuple[float, float]:
    """Apply the declared GRS80 UTM zone 14N null-datum approximation."""

    phi = math.radians(latitude)
    delta_lambda = math.radians(longitude) - UTM14_CENTRAL_MERIDIAN_RADIANS
    sin_phi = math.sin(phi)
    cos_phi = math.cos(phi)
    tan_phi = math.tan(phi)
    radius = GRS80_A / math.sqrt(1 - GRS80_E2 * sin_phi**2)
    tangent = tan_phi**2
    second_eccentricity = GRS80_EP2 * cos_phi**2
    series = cos_phi * delta_lambda
    meridian = GRS80_A * (
        (1 - GRS80_E2 / 4 - 3 * GRS80_E2**2 / 64 - 5 * GRS80_E2**3 / 256)
        * phi
        - (3 * GRS80_E2 / 8 + 3 * GRS80_E2**2 / 32 + 45 * GRS80_E2**3 / 1024)
        * math.sin(2 * phi)
        + (15 * GRS80_E2**2 / 256 + 45 * GRS80_E2**3 / 1024)
        * math.sin(4 * phi)
        - (35 * GRS80_E2**3 / 3072) * math.sin(6 * phi)
    )
    easting = UTM_FALSE_EASTING + UTM_SCALE * radius * (
        series
        + (1 - tangent + second_eccentricity) * series**3 / 6
        + (
            5
            - 18 * tangent
            + tangent**2
            + 72 * second_eccentricity
            - 58 * GRS80_EP2
        )
        * series**5
        / 120
    )
    northing = UTM_SCALE * (
        meridian
        + radius
        * tan_phi
        * (
            series**2 / 2
            + (5 - tangent + 9 * second_eccentricity + 4 * second_eccentricity**2)
            * series**4
            / 24
            + (
                61
                - 58 * tangent
                + tangent**2
                + 600 * second_eccentricity
                - 330 * GRS80_EP2
            )
            * series**6
            / 720
        )
    )
    return easting, northing


def _utm14_inverse(easting: float, northing: float) -> tuple[float, float]:
    """Invert the declared GRS80 UTM zone 14N null-datum approximation."""

    meridian = northing / UTM_SCALE
    mu = meridian / (
        GRS80_A
        * (1 - GRS80_E2 / 4 - 3 * GRS80_E2**2 / 64 - 5 * GRS80_E2**3 / 256)
    )
    e1 = (1 - math.sqrt(1 - GRS80_E2)) / (1 + math.sqrt(1 - GRS80_E2))
    footprint_latitude = (
        mu
        + (3 * e1 / 2 - 27 * e1**3 / 32) * math.sin(2 * mu)
        + (21 * e1**2 / 16 - 55 * e1**4 / 32) * math.sin(4 * mu)
        + (151 * e1**3 / 96) * math.sin(6 * mu)
        + (1097 * e1**4 / 512) * math.sin(8 * mu)
    )
    sin_phi = math.sin(footprint_latitude)
    cos_phi = math.cos(footprint_latitude)
    tan_phi = math.tan(footprint_latitude)
    radius = GRS80_A / math.sqrt(1 - GRS80_E2 * sin_phi**2)
    curvature = GRS80_A * (1 - GRS80_E2) / (1 - GRS80_E2 * sin_phi**2) ** 1.5
    tangent = tan_phi**2
    second_eccentricity = GRS80_EP2 * cos_phi**2
    series = (easting - UTM_FALSE_EASTING) / (radius * UTM_SCALE)
    latitude = footprint_latitude - (radius * tan_phi / curvature) * (
        series**2 / 2
        - (5 + 3 * tangent + 10 * second_eccentricity - 4 * second_eccentricity**2 - 9 * GRS80_EP2)
        * series**4
        / 24
        + (
            61
            + 90 * tangent
            + 298 * second_eccentricity
            + 45 * tangent**2
            - 252 * GRS80_EP2
            - 3 * second_eccentricity**2
        )
        * series**6
        / 720
    )
    longitude = UTM14_CENTRAL_MERIDIAN_RADIANS + (
        series
        - (1 + 2 * tangent + second_eccentricity) * series**3 / 6
        + (
            5
            - 2 * second_eccentricity
            + 28 * tangent
            - 3 * second_eccentricity**2
            + 8 * GRS80_EP2
            + 24 * tangent**2
        )
        * series**5
        / 120
    ) / cos_phi
    return math.degrees(longitude), math.degrees(latitude)


def validate_document(document: object) -> ValidationResult:
    findings: set[Finding] = set()
    numeric_findings = _unsafe_numeric_findings(document)
    if numeric_findings:
        review_outcome = None
        if isinstance(document, dict) and isinstance(document.get("review"), dict):
            outcome = document["review"].get("outcome")
            if isinstance(outcome, str):
                review_outcome = outcome
        return ValidationResult("DENY", review_outcome, numeric_findings)
    try:
        schema_errors = sorted(
            _VALIDATOR.iter_errors(document),
            key=lambda error: tuple(str(part) for part in error.absolute_path),
        )
    except (OSError, UnicodeError, ValueError, RecursionError):
        return ValidationResult("ERROR", None, (Finding("SCHEMA_UNAVAILABLE", "$"),))
    for error in schema_errors:
        findings.add(Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path))))
    if schema_errors or not isinstance(document, dict):
        return ValidationResult("DENY", None, tuple(sorted(findings)))

    source = document["source_identity"]
    assets = document["assets"]
    tile_id = source["tile_id"]
    raster = assets["raster_tiff"]
    metadata = assets["metadata_xml"]
    if (
        source["project_id"] != EXPECTED_PROJECT
        or source["project_numeric_id"] != EXPECTED_PROJECT_ID
        or tile_id != EXPECTED_TILE
        or not tile_id.endswith("_" + source["project_id"])
    ):
        findings.add(Finding("PROJECT_IDENTITY_MISMATCH", "$.source_identity"))
    if (
        raster["filename"] != f"{tile_id}.tif"
        or metadata["filename"] != f"{tile_id}.xml"
        or raster["locator"].rsplit("/", 1)[-1] != raster["filename"]
        or metadata["locator"].rsplit("/", 1)[-1] != metadata["filename"]
    ):
        findings.add(Finding("ASSET_TILE_ID_MISMATCH", "$.assets"))
    if (
        raster["locator"] != EXPECTED_RASTER_LOCATOR
        or metadata["locator"] != EXPECTED_METADATA_LOCATOR
    ):
        findings.add(Finding("ASSET_LOCATOR_MISMATCH", "$.assets"))
    for name, asset in assets.items():
        if asset["content_sha256"] == ZERO_DIGEST:
            findings.add(Finding("DIGEST_PLACEHOLDER", f"$.assets.{name}.content_sha256"))
        expected_length, expected_digest = EXPECTED_ASSET_BYTES[name]
        if (
            asset["byte_length"] != expected_length
            or asset["content_sha256"] != expected_digest
        ):
            findings.add(Finding("ASSET_BYTES_MISMATCH", f"$.assets.{name}"))
        retrieved_at = _date_time(asset["retrieved_at"])
        last_modified = _date_time(asset["http_last_modified"])
        if (
            retrieved_at is not None
            and last_modified is not None
            and retrieved_at < last_modified
        ):
            findings.add(
                Finding(
                    "ASSET_RETRIEVAL_BEFORE_LAST_MODIFIED",
                    f"$.assets.{name}.retrieved_at",
                )
            )

    rights_evidence = source["rights_evidence"]
    if (
        source["rights"] != "PUBLIC_DOMAIN_WITH_USGS_METADATA_CONSTRAINTS"
        or rights_evidence["classification"] != source["rights"]
        or rights_evidence["evidence_asset_ref"] != "assets.metadata_xml"
        or rights_evidence["evidence_content_sha256"] != metadata["content_sha256"]
        or rights_evidence["public_domain_xpath"]
        != "/metadata/idinfo/descript/abstract"
        or rights_evidence["public_domain_assertion"]
        != "ALL_3DEP_PRODUCTS_PUBLIC_DOMAIN"
        or rights_evidence["access_constraints_xpath"] != "/metadata/idinfo/accconst"
        or rights_evidence["access_constraints_assertion"]
        != "NONE_SUBJECT_TO_USGS_STANDARD_DISCLAIMER"
        or rights_evidence["use_constraints_xpath"] != "/metadata/idinfo/useconst"
        or rights_evidence["use_constraints_assertion"]
        != "NO_ACCURACY_WARRANTY_AND_NO_ENDORSEMENT_IMPLICATION"
    ):
        findings.add(Finding("RIGHTS_EVIDENCE_MISMATCH", "$.source_identity.rights_evidence"))

    captures = document["evidence_captures"]
    expected_capture_locators = {
        "three_dep_index_query": EXPECTED_3DEP_INDEX_LOCATOR,
        "census_state_point_query": EXPECTED_CENSUS_POINT_LOCATOR,
        "census_county_point_query": EXPECTED_CENSUS_COUNTY_POINT_LOCATOR,
        "census_states_layer_metadata": EXPECTED_CENSUS_METADATA_LOCATOR,
    }
    for name, capture in captures.items():
        expected_length, expected_digest = EXPECTED_CAPTURE_BYTES[name]
        if (
            capture["locator"] != expected_capture_locators[name]
            or capture["byte_length"] != expected_length
            or capture["content_sha256"] != expected_digest
        ):
            findings.add(Finding("EVIDENCE_CAPTURE_BYTES_MISMATCH", f"$.evidence_captures.{name}"))

    capture_session = document["evidence_capture_session"]
    capture_completed_at = _date_time(capture_session["capture_completed_at"])
    candidate_frozen_at = _date_time(capture_session["candidate_frozen_at"])
    if capture_session != EXPECTED_CAPTURE_SESSION:
        findings.add(
            Finding(
                "EVIDENCE_CAPTURE_SESSION_MISMATCH",
                "$.evidence_capture_session",
            )
        )
    if (
        capture_completed_at is None
        or candidate_frozen_at is None
        or capture_completed_at > candidate_frozen_at
        or any(
            capture["retrieved_at"] != capture_session["capture_completed_at"]
            for capture in captures.values()
        )
    ):
        findings.add(
            Finding(
                "EVIDENCE_CAPTURE_CHRONOLOGY_INVALID",
                "$.evidence_captures",
            )
        )
    if candidate_frozen_at is not None and any(
        (retrieved := _date_time(capture["retrieved_at"])) is None
        or retrieved > candidate_frozen_at
        for capture in captures.values()
    ):
        findings.add(
            Finding(
                "EVIDENCE_CAPTURE_AFTER_AUTHORING_CUTOFF",
                "$.evidence_captures",
            )
        )
    if candidate_frozen_at is not None and any(
        (retrieved := _date_time(asset["retrieved_at"])) is None
        or retrieved > candidate_frozen_at
        for asset in assets.values()
    ):
        findings.add(
            Finding(
                "ASSET_RETRIEVAL_AFTER_AUTHORING_CUTOFF",
                "$.assets",
            )
        )

    projection_snapshot, projection_snapshot_valid = _load_projection_snapshot()
    expected_snapshot_path, expected_snapshot_length, expected_snapshot_digest = (
        EXPECTED_PROJECTION_SNAPSHOT
    )
    if not projection_snapshot_valid or projection_snapshot is None:
        findings.add(Finding("EVIDENCE_PROJECTION_SNAPSHOT_UNAVAILABLE", "$.evidence_captures"))
    else:
        if projection_snapshot.get("source_response_disposition") != (
            "REMOTE_BYTES_NOT_STORED_AUTHOR_TIME_OBSERVATION_ONLY"
        ):
            findings.add(Finding("EVIDENCE_PROJECTION_SNAPSHOT_MISMATCH", "$.evidence_captures"))
        if projection_snapshot.get("capture_session") != capture_session:
            findings.add(
                Finding(
                    "EVIDENCE_CAPTURE_SESSION_MISMATCH",
                    "$.evidence_capture_session",
                )
            )
        projections = projection_snapshot.get("projections")
        snapshot_rights = projection_snapshot.get("rights_assertion")
        if not isinstance(projections, dict):
            findings.add(Finding("EVIDENCE_PROJECTION_SNAPSHOT_MISMATCH", "$.evidence_captures"))
        else:
            for name, capture in captures.items():
                snapshot_ref = capture["projection_snapshot"]
                if (
                    snapshot_ref["repository_path"] != expected_snapshot_path
                    or snapshot_ref["byte_length"] != expected_snapshot_length
                    or snapshot_ref["content_sha256"] != expected_snapshot_digest
                    or snapshot_ref["json_pointer"] != f"/projections/{name}"
                    or projections.get(name) != capture["captured_projection"]
                ):
                    findings.add(
                        Finding(
                            "EVIDENCE_PROJECTION_SNAPSHOT_MISMATCH",
                            f"$.evidence_captures.{name}.projection_snapshot",
                        )
                    )
        if snapshot_rights != rights_evidence:
            findings.add(Finding("RIGHTS_EVIDENCE_MISMATCH", "$.source_identity.rights_evidence"))

    temporal = document["temporal_identity"]
    publication = _date(temporal["tile_publication_date"])
    xml_range = temporal["tile_metadata_temporal_range"]
    xml_start, xml_end = _date(xml_range["start"]), _date(xml_range["end"])
    if xml_start is not None and xml_end is not None and xml_start > xml_end:
        findings.add(Finding("TILE_METADATA_TEMPORAL_RANGE_INVALID", "$.temporal_identity.tile_metadata_temporal_range"))
    if (
        temporal["tile_publication_date"] != "2023-06-12"
        or xml_range["start"] != "2017-12-14"
        or xml_range["end"] != "2020-07-25"
        or xml_range["currentness_basis"] != "publication date"
    ):
        findings.add(Finding("TILE_METADATA_TEMPORAL_IDENTITY_MISMATCH", "$.temporal_identity"))

    observation = temporal["source_observation_interval"]
    if observation["status"] == "VERIFIED":
        observed_start, observed_end = _date(observation["start"]), _date(observation["end"])
        if observed_start is not None and observed_end is not None and observed_start > observed_end:
            findings.add(Finding("SOURCE_OBSERVATION_INTERVAL_INVALID", "$.temporal_identity.source_observation_interval"))
        if publication is not None and observed_start == publication and observed_end == publication:
            findings.add(Finding("TEMPORAL_IDENTITY_CONFLATED", "$.temporal_identity"))
        elif publication is not None and observed_end is not None and observed_end > publication:
            findings.add(Finding("SOURCE_OBSERVATION_AFTER_PUBLICATION", "$.temporal_identity.source_observation_interval.end"))

    delivered_crs = document["delivered_crs"]
    if (
        delivered_crs["authority"],
        delivered_crs["code"],
        delivered_crs["name"],
        delivered_crs["datum"],
        delivered_crs["axis_units"],
    ) != (
        "EPSG",
        26914,
        "NAD83 / UTM zone 14N",
        "North American Datum of 1983",
        "metre",
    ):
        findings.add(Finding("DELIVERED_CRS_IDENTITY_MISMATCH", "$.delivered_crs"))

    coverage = document["spatial_coverage"]
    bbox = coverage["wgs84_bbox"]
    bounds_valid = bbox["west"] < bbox["east"] and bbox["south"] < bbox["north"]
    if not bounds_valid:
        findings.add(Finding("COVERAGE_BOUNDS_INVALID", "$.spatial_coverage.wgs84_bbox"))
    nominal_bounds = coverage["nominal_projected_bounds"]
    nominal_bounds_valid = (
        nominal_bounds["x_min"] < nominal_bounds["x_max"]
        and nominal_bounds["y_min"] < nominal_bounds["y_max"]
    )
    if not nominal_bounds_valid:
        findings.add(
            Finding(
                "COVERAGE_BOUNDS_INVALID",
                "$.spatial_coverage.nominal_projected_bounds",
            )
        )

    pilot = coverage["public_safe_pilot_point"]
    sample = document["inspection_sample"]
    if (
        not _inside(pilot["longitude"], pilot["latitude"], bbox)
        or not _inside(sample["longitude"], sample["latitude"], bbox)
        or pilot["longitude"] != sample["longitude"]
        or pilot["latitude"] != sample["latitude"]
    ):
        findings.add(Finding("COVERAGE_POINT_OUTSIDE_TILE", "$.spatial_coverage.public_safe_pilot_point"))

    lineage = document["lineage"]
    index_projection = captures["three_dep_index_query"]["captured_projection"]
    if index_projection != EXPECTED_INDEX_PROJECTION:
        findings.add(
            Finding(
                "EVIDENCE_CAPTURE_PROJECTION_MISMATCH",
                "$.evidence_captures.three_dep_index_query.captured_projection",
            )
        )
    if index_projection["query_envelope"] != bbox:
        findings.add(
            Finding(
                "METADATA_INDEX_ENVELOPE_MISMATCH",
                "$.evidence_captures.three_dep_index_query.captured_projection.query_envelope",
            )
        )
    if (
        source["project_id"] != index_projection["project"]
        or source["project_numeric_id"] != index_projection["project_id"]
        or lineage["matched_feature_count"] != index_projection["feature_count"]
        or lineage["work_unit"] != index_projection["work_unit"]
        or lineage["work_unit_id"] != index_projection["work_unit_id"]
        or lineage["collection_start"] != index_projection["collection_start"]
        or lineage["collection_end"] != index_projection["collection_end"]
        or lineage["quality_level"] != index_projection["quality_level"].replace(" ", "")
        or lineage["specification"] != index_projection["specification"]
        or lineage["acquisition_method"] != index_projection["acquisition_method"]
        or lineage["dem_gsd_meters"] != index_projection["dem_gsd_meters"]
        or lineage["source_horizontal_crs"]["code"]
        != index_projection["horizontal_crs_code"]
        or lineage["source_vertical_crs"]["code"]
        != index_projection["vertical_crs_code"]
        or lineage["source_geoid"] != index_projection["geoid"]
        or lineage["source_dem_publication_date"]
        != index_projection["source_dem_publication_date"]
    ):
        findings.add(Finding("INDEX_CAPTURE_LINEAGE_MISMATCH", "$.lineage"))
    if (
        observation["start"] != index_projection["collection_start"]
        or observation["end"] != index_projection["collection_end"]
    ):
        findings.add(
            Finding(
                "SOURCE_OBSERVATION_LINEAGE_MISMATCH",
                "$.temporal_identity.source_observation_interval",
            )
        )

    vertical = document["vertical_reference"]
    if (
        lineage["source_vertical_crs"]["code"] != vertical["datum_code"]
        or lineage["source_geoid"] != vertical["source_work_unit_geoid"]["model"]
    ):
        findings.add(Finding("VERTICAL_LINEAGE_MISMATCH", "$.vertical_reference"))

    census_projection = captures["census_state_point_query"]["captured_projection"]
    county_projection = captures["census_county_point_query"]["captured_projection"]
    census_metadata = captures["census_states_layer_metadata"]["captured_projection"]
    kansas = coverage["kansas_state_point_intersection"]
    ellsworth = coverage["ellsworth_county_point_intersection"]
    census_vintage = _date(census_metadata["vintage"])
    census_metadata_retrieved_at = _date_time(
        captures["census_states_layer_metadata"]["retrieved_at"]
    )
    if (
        census_vintage is None
        or census_metadata_retrieved_at is None
        or census_vintage > census_metadata_retrieved_at.date()
    ):
        findings.add(
            Finding(
                "CENSUS_VINTAGE_AFTER_CAPTURE",
                "$.evidence_captures.census_states_layer_metadata",
            )
        )
    if census_projection != EXPECTED_CENSUS_POINT_PROJECTION:
        findings.add(
            Finding(
                "EVIDENCE_CAPTURE_PROJECTION_MISMATCH",
                "$.evidence_captures.census_state_point_query.captured_projection",
            )
        )
    if (
        census_projection["longitude"] != pilot["longitude"]
        or census_projection["latitude"] != pilot["latitude"]
        or census_projection["state_geoid"] != kansas["state_geoid"]
        or census_projection["state_abbreviation"] != kansas["state_abbreviation"]
        or census_projection["state_name"] != kansas["state_name"]
        or census_metadata["vintage"] != kansas["boundary_vintage"]
    ):
        findings.add(
            Finding(
                "KANSAS_COVERAGE_EVIDENCE_MISMATCH",
                "$.spatial_coverage.kansas_state_point_intersection",
            )
        )
    if county_projection != EXPECTED_CENSUS_COUNTY_PROJECTION:
        findings.add(
            Finding(
                "EVIDENCE_CAPTURE_PROJECTION_MISMATCH",
                "$.evidence_captures.census_county_point_query.captured_projection",
            )
        )
    if (
        county_projection["longitude"] != pilot["longitude"]
        or county_projection["latitude"] != pilot["latitude"]
        or county_projection["county_geoid"] != ellsworth["county_geoid"]
        or county_projection["state_code"] != ellsworth["state_code"]
        or county_projection["county_code"] != ellsworth["county_code"]
        or county_projection["county_name"] != ellsworth["county_name"]
        or census_projection["state_code"] != county_projection["state_code"]
    ):
        findings.add(
            Finding(
                "ELLSWORTH_COVERAGE_EVIDENCE_MISMATCH",
                "$.spatial_coverage.ellsworth_county_point_intersection",
            )
        )

    transform = coverage["coordinate_transform"]
    if nominal_bounds_valid and bounds_valid:
        projected_corners = (
            (nominal_bounds["x_min"], nominal_bounds["y_min"]),
            (nominal_bounds["x_min"], nominal_bounds["y_max"]),
            (nominal_bounds["x_max"], nominal_bounds["y_min"]),
            (nominal_bounds["x_max"], nominal_bounds["y_max"]),
        )
        try:
            geographic_corners = tuple(
                _utm14_inverse(*corner) for corner in projected_corners
            )
        except (OverflowError, ValueError, ZeroDivisionError):
            findings.add(
                Finding(
                    "COVERAGE_CRS_TRANSFORM_ERROR",
                    "$.spatial_coverage.nominal_projected_bounds",
                )
            )
        else:
            calculated_bbox = {
                "west": min(point[0] for point in geographic_corners),
                "south": min(point[1] for point in geographic_corners),
                "east": max(point[0] for point in geographic_corners),
                "north": max(point[1] for point in geographic_corners),
            }
            if any(
                not math.isfinite(calculated_bbox[key])
                or not math.isclose(
                    bbox[key],
                    calculated_bbox[key],
                    rel_tol=0.0,
                    abs_tol=transform["bbox_tolerance_degrees"],
                )
                for key in ("west", "south", "east", "north")
            ):
                findings.add(
                    Finding(
                        "COVERAGE_CRS_TRANSFORM_MISMATCH",
                        "$.spatial_coverage.wgs84_bbox",
                    )
                )

    try:
        transformed_sample = _utm14_forward(sample["longitude"], sample["latitude"])
    except (OverflowError, ValueError, ZeroDivisionError):
        findings.add(
            Finding("SAMPLE_CRS_TRANSFORM_ERROR", "$.inspection_sample")
        )
    else:
        if (
            not math.isclose(
                sample["projected_x"],
                transformed_sample[0],
                rel_tol=0.0,
                abs_tol=transform["point_tolerance_m"],
            )
            or not math.isclose(
                sample["projected_y"],
                transformed_sample[1],
                rel_tol=0.0,
                abs_tol=transform["point_tolerance_m"],
            )
        ):
            findings.add(
                Finding("SAMPLE_CRS_TRANSFORM_MISMATCH", "$.inspection_sample")
            )

    grid = document["raster_grid"]
    a, b, c, d, e, f = grid["affine_transform"]
    if (
        grid["width"],
        grid["height"],
        grid["affine_transform"],
        grid["nodata"]["value"],
    ) != EXPECTED_GRID_FACTS:
        findings.add(Finding("RASTER_INSPECTION_FACTS_MISMATCH", "$.raster_grid"))
    expected_storage_bounds = (
        c,
        f + e * grid["height"],
        c + a * grid["width"],
        f,
    )
    storage_bounds = grid["storage_bounds"]
    actual_storage_bounds = (
        storage_bounds["x_min"],
        storage_bounds["y_min"],
        storage_bounds["x_max"],
        storage_bounds["y_max"],
    )
    if (
        not math.isclose(a, grid["cell_size_x"], rel_tol=0.0, abs_tol=1e-9)
        or not math.isclose(e, -grid["cell_size_y"], rel_tol=0.0, abs_tol=1e-9)
        or b != 0
        or d != 0
        or any(
            not math.isclose(left, right, rel_tol=0.0, abs_tol=1e-6)
            for left, right in zip(expected_storage_bounds, actual_storage_bounds)
        )
    ):
        findings.add(Finding("RASTER_GRID_BOUNDS_MISMATCH", "$.raster_grid.affine_transform"))
    if not (
        storage_bounds["x_min"] <= nominal_bounds["x_min"]
        < nominal_bounds["x_max"] <= storage_bounds["x_max"]
        and storage_bounds["y_min"] <= nominal_bounds["y_min"]
        < nominal_bounds["y_max"] <= storage_bounds["y_max"]
    ):
        findings.add(
            Finding(
                "NOMINAL_COVERAGE_OUTSIDE_RASTER_STORAGE",
                "$.spatial_coverage.nominal_projected_bounds",
            )
        )

    if sample["row"] >= grid["height"] or sample["column"] >= grid["width"]:
        findings.add(Finding("SAMPLE_CELL_OUTSIDE_RASTER", "$.inspection_sample"))
    elif a > 0 and e < 0:
        expected_column = math.floor((sample["projected_x"] - c) / a)
        expected_row = math.floor((f - sample["projected_y"]) / abs(e))
        if sample["column"] != expected_column or sample["row"] != expected_row:
            findings.add(Finding("SAMPLE_PIXEL_LOCATION_MISMATCH", "$.inspection_sample"))

    if sample["source_elevation"]["value"] == grid["nodata"]["value"]:
        findings.add(Finding("SAMPLE_NODATA_MISLABELED", "$.inspection_sample.source_elevation"))
    fixture_encoding = sample["fixture_encoding"]
    if (
        sample["longitude"],
        sample["latitude"],
        sample["projected_x"],
        sample["projected_y"],
        sample["row"],
        sample["column"],
        sample["source_elevation"]["value"],
        fixture_encoding["rgb"],
        fixture_encoding["decoded_value_m"],
    ) != EXPECTED_SAMPLE_FACTS:
        findings.add(
            Finding("SAMPLE_INSPECTION_FACTS_MISMATCH", "$.inspection_sample")
        )
    if (
        fixture_encoding["source_nodata_value"] != grid["nodata"]["value"]
        or fixture_encoding["validity_mask_value"] != 1
    ):
        findings.add(
            Finding(
                "SAMPLE_VALIDITY_MASK_MISMATCH",
                "$.inspection_sample.fixture_encoding",
            )
        )
    red, green, blue = fixture_encoding["rgb"]
    decoded = red * 256 + green + blue / 256 - 32768
    declared_decoded = fixture_encoding["decoded_value_m"]
    error = abs(declared_decoded - sample["source_elevation"]["value"])
    if (
        not math.isclose(decoded, declared_decoded, rel_tol=0.0, abs_tol=1e-12)
        or not math.isclose(
            error,
            fixture_encoding["quantization_error_m"],
            rel_tol=0.0,
            abs_tol=1e-12,
        )
        or error > 1 / 256
    ):
        findings.add(Finding("SAMPLE_ENCODING_MISMATCH", "$.inspection_sample.fixture_encoding"))

    accuracy = document["vertical_accuracy"]
    project_report = accuracy["available_project_report"]
    if project_report["content_sha256"] == ZERO_DIGEST:
        findings.add(Finding("DIGEST_PLACEHOLDER", "$.vertical_accuracy.available_project_report.content_sha256"))
    expected_report_locator, expected_report_length, expected_report_digest = (
        EXPECTED_ACCURACY_REPORT
    )
    if (
        project_report["locator"] != expected_report_locator
        or project_report["byte_length"] != expected_report_length
        or project_report["content_sha256"] != expected_report_digest
    ):
        findings.add(
            Finding(
                "ACCURACY_REPORT_BYTES_MISMATCH",
                "$.vertical_accuracy.available_project_report",
            )
        )
    report_retrieved_at = _date_time(project_report["retrieved_at"])
    report_last_modified = _date_time(project_report["http_last_modified"])
    if (
        report_retrieved_at is not None
        and report_last_modified is not None
        and report_retrieved_at < report_last_modified
    ):
        findings.add(
            Finding(
                "ACCURACY_REPORT_RETRIEVAL_BEFORE_LAST_MODIFIED",
                "$.vertical_accuracy.available_project_report.retrieved_at",
            )
        )
    if (
        candidate_frozen_at is not None
        and (
            report_retrieved_at is None
            or report_retrieved_at > candidate_frozen_at
        )
    ):
        findings.add(
            Finding(
                "ACCURACY_REPORT_RETRIEVAL_AFTER_AUTHORING_CUTOFF",
                "$.vertical_accuracy.available_project_report.retrieved_at",
            )
        )
    expected_nva_95 = project_report["nva_rmsez"] * 1.96
    if (
        project_report["nva_checkpoint_count"],
        project_report["nva_rmsez"],
        project_report["nva_accuracy_95"],
        project_report["vva_checkpoint_count"],
        project_report["vva_percentile_95"],
        project_report["includes_source_work_unit"],
        project_report["applicability_to_delivered_tile"],
    ) != EXPECTED_ACCURACY_FACTS:
        findings.add(
            Finding(
                "ACCURACY_REPORT_FACTS_MISMATCH",
                "$.vertical_accuracy.available_project_report",
            )
        )
    if not math.isclose(
        expected_nva_95,
        project_report["nva_accuracy_95"],
        rel_tol=0.0,
        abs_tol=0.0001,
    ):
        findings.add(Finding("ACCURACY_REPORT_INTERNAL_MISMATCH", "$.vertical_accuracy.available_project_report.nva_accuracy_95"))

    if document["blockers"] != sorted(set(document["blockers"])):
        findings.add(Finding("BLOCKER_ORDER_OR_DUPLICATE_INVALID", "$.blockers"))
    if document["blockers"] != _expected_blockers(document):
        findings.add(Finding("BLOCKER_SET_MISMATCH", "$.blockers"))

    try:
        expected_id, expected_hash = _identity(document)
    except CanonicalizationFailure:
        findings.add(Finding("CANONICALIZATION_ERROR", "$"))
        return ValidationResult("DENY", document["review"]["outcome"], tuple(sorted(findings)))
    if document["candidate_id"] != expected_id:
        findings.add(Finding("CANDIDATE_ID_MISMATCH", "$.candidate_id"))
    if document["spec_hash"] != expected_hash:
        findings.add(Finding("CANDIDATE_SPEC_HASH_MISMATCH", "$.spec_hash"))

    return ValidationResult(
        "DENY" if findings else "PASS",
        document["review"]["outcome"],
        tuple(sorted(findings)),
        expected_id,
    )


def validate_file(path: Path) -> ValidationResult:
    try:
        document = load_json_file(path)
    except JsonInputError:
        return ValidationResult("ERROR", None, (Finding("CANDIDATE_JSON_INVALID", "$"),))
    return validate_document(document)


def _serialize(result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "candidate_id": result.candidate_id,
            "execution_mode": "FIXTURE_ONLY",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "review_outcome": result.review_outcome,
            "scope": SCOPE,
            "status": result.status,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        suite = load_json_file(FIXTURE_PATH)
    except JsonInputError:
        return False, {"cases": [], "ok": False, "scope": SCOPE}
    if not isinstance(suite, dict) or not isinstance(suite.get("base_candidate"), dict):
        return False, {"cases": [], "ok": False, "scope": SCOPE}

    reports: list[dict[str, object]] = []
    ok = True
    for case in suite.get("cases", []):
        if not isinstance(case, dict):
            ok = False
            continue
        try:
            candidate = materialize_case(suite["base_candidate"], case)
            result = validate_document(candidate)
        except (KeyError, IndexError, TypeError, ValueError, CanonicalizationFailure):
            ok = False
            continue
        actual_codes = sorted({finding.code for finding in result.findings})
        expected = case.get("expected", {})
        case_ok = (
            isinstance(expected, dict)
            and result.status == expected.get("status")
            and result.review_outcome == expected.get("review_outcome")
            and actual_codes == expected.get("finding_codes")
        )
        ok = ok and case_ok
        reports.append(
            {
                "actual_findings": actual_codes,
                "actual_review_outcome": result.review_outcome,
                "actual_status": result.status,
                "case_id": case.get("case_id"),
                "expected_findings": expected.get("finding_codes") if isinstance(expected, dict) else None,
                "expected_review_outcome": expected.get("review_outcome") if isinstance(expected, dict) else None,
                "expected_status": expected.get("status") if isinstance(expected, dict) else None,
                "ok": case_ok,
            }
        )
    return bool(reports) and ok, {
        "cases": reports,
        "ok": bool(reports) and ok,
        "scope": SCOPE,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            parser.error("--fixtures cannot be combined with a path")
        ok, report = run_fixture_suite()
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(_serialize(result))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
