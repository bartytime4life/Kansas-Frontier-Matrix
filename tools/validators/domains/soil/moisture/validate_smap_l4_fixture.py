#!/usr/bin/env python3
"""Validate the frozen, synthetic SMAP L4 anti-collapse fixture profile.

The profile is deliberately local and noncanonical. It proves that modeled L4
grid candidates cannot silently become raw, station, field, or released truth.
It does not fetch SMAP, admit a source, define a production schema, or publish.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[5]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    find_undeclared_fields,
    is_finite_number,
    is_nonempty_string,
    run_cli,
    validate_fixture_file,
)

PROFILE_ID = "kfm-smap-l4-anti-collapse-fixture-v1"
SCOPE = "soil-smap-l4-anti-collapse-fixture"
SPEC_HASH = "sha256:d0545d945f8f425bbce408002273b71725da27595e6a89831ab5cab7ebf82cd9"
UTC_RE = re.compile(
    r"^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])"
    r"T(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]Z$"
)

TOP_FIELDS = frozenset(
    {
        "fixture_id",
        "profile_id",
        "fixture_only",
        "domain",
        "object_family",
        "source_descriptor_ref",
        "source_role",
        "support_type",
        "product",
        "observation",
        "spatial_support",
        "assimilation",
        "anti_collapse",
        "time",
        "evidence_refs",
        "run_receipt_ref",
        "spec_hash",
        "governance",
        "limitations",
    }
)
PRODUCT_FIELDS = frozenset({"product_family", "processing_level", "dataset_version", "cadence_class"})
OBSERVATION_FIELDS = frozenset(
    {
        "moisture_layer",
        "measurement_type",
        "measure",
        "value",
        "unit",
        "observed_time",
        "qa_flags",
        "uncertainty",
        "uncertainty_unit",
        "preliminary",
    }
)
SPATIAL_FIELDS = frozenset({"kind", "native_grid", "grid_cell_id", "source_resolution_m"})
ASSIMILATION_FIELDS = frozenset({"kind", "model"})
ANTI_COLLAPSE_FIELDS = frozenset(
    {"raw_observation_truth", "station_observation", "field_truth", "surface_is_root_zone", "merged_with_in_situ"}
)
TIME_FIELDS = frozenset({"source_updated_at", "retrieved_at"})
GOVERNANCE_FIELDS = frozenset(
    {"rights_state", "sensitivity_state", "review_state", "release_state", "promotion_eligible", "rollback_state"}
)
REQUIRED_LIMITATIONS = frozenset(
    {"model_assimilated_not_raw_observation", "satellite_grid_not_station_or_field_truth", "synthetic_fixture_only"}
)


def _object(
    findings: set[Finding], candidate: dict[str, object], field: str, code: str
) -> dict[str, object] | None:
    value = candidate.get(field)
    if not isinstance(value, dict):
        add_finding(findings, code, f"$.{field}")
        return None
    return value


def _canonical_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or UTC_RE.fullmatch(value) is None:
        return None
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return None
    return parsed.replace(tzinfo=timezone.utc)


def _fixture_ref(value: object, prefix: str) -> bool:
    return (
        is_nonempty_string(value)
        and isinstance(value, str)
        and value.startswith(prefix)
        and bool(value.removeprefix(prefix).strip())
    )


def _validate_string_list(
    findings: set[Finding], value: object, path: str, code: str, *, prefix: str | None = None
) -> list[str] | None:
    if not isinstance(value, list) or not value:
        add_finding(findings, code, path)
        return None
    if any(not is_nonempty_string(item) for item in value):
        add_finding(findings, code, path)
        return None
    strings = [item for item in value if isinstance(item, str)]
    if len(strings) != len(set(strings)):
        add_finding(findings, code, path)
    if prefix is not None and any(not _fixture_ref(item, prefix) for item in strings):
        add_finding(findings, code, path)
    return strings


def validate_candidate(candidate: object) -> list[Finding]:
    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("ROOT_OBJECT_REQUIRED", "$")]

    find_undeclared_fields(findings, candidate, TOP_FIELDS, "UNDECLARED_FIELD", "$")

    if not _fixture_ref(candidate.get("fixture_id"), "fixture://soil/smap_l4/"):
        add_finding(findings, "FIXTURE_ID_INVALID", "$.fixture_id")
    if candidate.get("profile_id") != PROFILE_ID:
        add_finding(findings, "PROFILE_ID_INVALID", "$.profile_id")
    if candidate.get("fixture_only") is not True:
        add_finding(findings, "FIXTURE_ONLY_REQUIRED", "$.fixture_only")
    if candidate.get("domain") != "soil":
        add_finding(findings, "DOMAIN_INVALID", "$.domain")
    if candidate.get("object_family") != "SoilMoistureObservation":
        add_finding(findings, "OBJECT_FAMILY_INVALID", "$.object_family")
    if candidate.get("source_descriptor_ref") != "fixture://source/nasa-smap-l4":
        add_finding(findings, "SOURCE_DESCRIPTOR_REF_INVALID", "$.source_descriptor_ref")
    if candidate.get("source_role") != "model_assimilated_reference":
        add_finding(findings, "SOURCE_ROLE_COLLAPSE", "$.source_role")
    if candidate.get("support_type") != "satellite_grid_soil_moisture":
        add_finding(findings, "SUPPORT_TYPE_COLLAPSE", "$.support_type")

    product = _object(findings, candidate, "product", "PRODUCT_OBJECT_REQUIRED")
    cadence: object = None
    if product is not None:
        find_undeclared_fields(findings, product, PRODUCT_FIELDS, "UNDECLARED_FIELD", "$.product")
        if product.get("product_family") != "SMAP":
            add_finding(findings, "PRODUCT_FAMILY_INVALID", "$.product.product_family")
        if product.get("processing_level") != "L4":
            add_finding(findings, "PROCESSING_LEVEL_INVALID", "$.product.processing_level")
        version = product.get("dataset_version")
        if not is_nonempty_string(version) or str(version).strip().upper() in {"TODO", "TBD", "UNKNOWN"}:
            add_finding(findings, "PRODUCT_VERSION_REQUIRED", "$.product.dataset_version")
        cadence = product.get("cadence_class")
        if cadence not in {"nrt", "standard_quality", "reprocessed"}:
            add_finding(findings, "CADENCE_CLASS_INVALID", "$.product.cadence_class")

    observation = _object(findings, candidate, "observation", "OBSERVATION_OBJECT_REQUIRED")
    observed_time: datetime | None = None
    if observation is not None:
        find_undeclared_fields(findings, observation, OBSERVATION_FIELDS, "UNDECLARED_FIELD", "$.observation")
        if observation.get("moisture_layer") not in {"surface", "root_zone"}:
            add_finding(findings, "MOISTURE_LAYER_INVALID", "$.observation.moisture_layer")
        if observation.get("measurement_type") != "modeled_estimate":
            add_finding(findings, "MODEL_ASSIMILATION_MISSING", "$.observation.measurement_type")
        if observation.get("measure") != "volumetric_water_content":
            add_finding(findings, "MEASURE_INVALID", "$.observation.measure")
        value = observation.get("value")
        if not is_finite_number(value) or not 0 <= value <= 1:
            add_finding(findings, "VALUE_OUT_OF_RANGE", "$.observation.value")
        if observation.get("unit") != "m3/m3":
            add_finding(findings, "UNIT_INVALID", "$.observation.unit")
        observed_time = _canonical_utc(observation.get("observed_time"))
        if observed_time is None:
            add_finding(findings, "OBSERVED_TIME_INVALID", "$.observation.observed_time")
        _validate_string_list(findings, observation.get("qa_flags"), "$.observation.qa_flags", "QA_FLAGS_REQUIRED")
        uncertainty = observation.get("uncertainty")
        if not is_finite_number(uncertainty) or not 0 <= uncertainty <= 1:
            add_finding(findings, "UNCERTAINTY_REQUIRED", "$.observation.uncertainty")
        if observation.get("uncertainty_unit") != "m3/m3":
            add_finding(findings, "UNCERTAINTY_UNIT_INVALID", "$.observation.uncertainty_unit")
        preliminary = observation.get("preliminary")
        if not isinstance(preliminary, bool):
            add_finding(findings, "PRELIMINARY_FLAG_REQUIRED", "$.observation.preliminary")
        elif cadence in {"nrt", "standard_quality", "reprocessed"} and preliminary is not (cadence == "nrt"):
            add_finding(findings, "CADENCE_POSTURE_INVALID", "$.observation.preliminary")

    spatial = _object(findings, candidate, "spatial_support", "SPATIAL_SUPPORT_OBJECT_REQUIRED")
    if spatial is not None:
        find_undeclared_fields(findings, spatial, SPATIAL_FIELDS, "UNDECLARED_FIELD", "$.spatial_support")
        if spatial.get("kind") != "satellite_grid_cell":
            add_finding(findings, "GRID_STATION_COLLAPSE", "$.spatial_support.kind")
        if not is_nonempty_string(spatial.get("native_grid")):
            add_finding(findings, "GRID_NATIVE_REQUIRED", "$.spatial_support.native_grid")
        if not _fixture_ref(spatial.get("grid_cell_id"), "fixture://grid/cell/"):
            add_finding(findings, "GRID_CELL_ID_REQUIRED", "$.spatial_support.grid_cell_id")
        resolution = spatial.get("source_resolution_m")
        if not is_finite_number(resolution) or not 0 < resolution <= 1_000_000:
            add_finding(findings, "GRID_RESOLUTION_REQUIRED", "$.spatial_support.source_resolution_m")

    assimilation = _object(findings, candidate, "assimilation", "ASSIMILATION_OBJECT_REQUIRED")
    if assimilation is not None:
        find_undeclared_fields(findings, assimilation, ASSIMILATION_FIELDS, "UNDECLARED_FIELD", "$.assimilation")
        if assimilation.get("kind") != "model_assimilated":
            add_finding(findings, "MODEL_ASSIMILATION_MISSING", "$.assimilation.kind")
        if not is_nonempty_string(assimilation.get("model")):
            add_finding(findings, "ASSIMILATION_MODEL_REQUIRED", "$.assimilation.model")

    anti = _object(findings, candidate, "anti_collapse", "ANTI_COLLAPSE_OBJECT_REQUIRED")
    if anti is not None:
        find_undeclared_fields(findings, anti, ANTI_COLLAPSE_FIELDS, "UNDECLARED_FIELD", "$.anti_collapse")
        expected_false = {
            "raw_observation_truth": "RAW_OBSERVATION_TRUTH_FORBIDDEN",
            "station_observation": "GRID_STATION_COLLAPSE",
            "field_truth": "GROUND_TRUTH_FORBIDDEN",
            "surface_is_root_zone": "SURFACE_ROOT_ZONE_COLLAPSE",
            "merged_with_in_situ": "IN_SITU_MERGE_FORBIDDEN",
        }
        for field, code in expected_false.items():
            if anti.get(field) is not False:
                add_finding(findings, code, f"$.anti_collapse.{field}")

    time_block = _object(findings, candidate, "time", "TIME_OBJECT_REQUIRED")
    source_updated: datetime | None = None
    retrieved: datetime | None = None
    if time_block is not None:
        find_undeclared_fields(findings, time_block, TIME_FIELDS, "UNDECLARED_FIELD", "$.time")
        source_updated = _canonical_utc(time_block.get("source_updated_at"))
        retrieved = _canonical_utc(time_block.get("retrieved_at"))
        if source_updated is None:
            add_finding(findings, "SOURCE_UPDATED_TIME_INVALID", "$.time.source_updated_at")
        if retrieved is None:
            add_finding(findings, "RETRIEVED_TIME_INVALID", "$.time.retrieved_at")
    if observed_time is not None and source_updated is not None and observed_time > source_updated:
        add_finding(findings, "TEMPORAL_ORDER_INVALID", "$.time.source_updated_at")
    if source_updated is not None and retrieved is not None and source_updated > retrieved:
        add_finding(findings, "TEMPORAL_ORDER_INVALID", "$.time.retrieved_at")

    _validate_string_list(
        findings,
        candidate.get("evidence_refs"),
        "$.evidence_refs",
        "EVIDENCE_REFS_REQUIRED",
        prefix="fixture://evidence/",
    )
    if not _fixture_ref(candidate.get("run_receipt_ref"), "fixture://receipt/"):
        add_finding(findings, "RUN_RECEIPT_REF_REQUIRED", "$.run_receipt_ref")
    if candidate.get("spec_hash") != SPEC_HASH:
        add_finding(findings, "SPEC_HASH_INVALID", "$.spec_hash")

    governance = _object(findings, candidate, "governance", "GOVERNANCE_OBJECT_REQUIRED")
    if governance is not None:
        find_undeclared_fields(findings, governance, GOVERNANCE_FIELDS, "UNDECLARED_FIELD", "$.governance")
        expected = {
            "rights_state": ("fixture_only", "GOVERNANCE_RIGHTS_STATE_INVALID"),
            "sensitivity_state": ("public_safe_fixture", "GOVERNANCE_SENSITIVITY_STATE_INVALID"),
            "review_state": ("fixture_only", "GOVERNANCE_REVIEW_STATE_INVALID"),
            "release_state": ("not_released", "GOVERNANCE_RELEASE_STATE_INVALID"),
            "promotion_eligible": (False, "GOVERNANCE_PROMOTION_STATE_INVALID"),
            "rollback_state": ("fixture_only", "GOVERNANCE_ROLLBACK_STATE_INVALID"),
        }
        for field, (value, code) in expected.items():
            if governance.get(field) != value or type(governance.get(field)) is not type(value):
                add_finding(findings, code, f"$.governance.{field}")

    limitations = _validate_string_list(
        findings,
        candidate.get("limitations"),
        "$.limitations",
        "LIMITATIONS_REQUIRED",
    )
    if limitations is not None and (
        set(limitations) != REQUIRED_LIMITATIONS
        or len(limitations) != len(REQUIRED_LIMITATIONS)
    ):
        add_finding(findings, "LIMITATIONS_REQUIRED", "$.limitations")

    return sorted(findings)


def validate_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_candidate)


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(
        argv=argv,
        description="Validate frozen synthetic SMAP L4 anti-collapse fixtures",
        scope=SCOPE,
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
