#!/usr/bin/env python3
"""Validate the bounded Atmosphere observed-versus-modeled profile.

This standard-library validator checks synthetic AirObservation and
ForecastContext candidates. It preserves source role, knowledge character,
time, units, model-run identity, DERIVED_FROM lineage, uncertainty, evidence,
and non-release boundaries. It does not fetch a source, assess current air
quality, resolve live evidence, execute policy, issue an alert, or authorize
promotion, release, or publication.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    find_undeclared_fields,
    is_finite_number,
    is_nonempty_string,
    validate_fixture_file,
)


PROFILE_ID = "kfm-atmosphere-observed-modeled-separation-v1"
MAX_REFS = 32
MAX_LIMITATIONS = 32

COMMON_FIELDS = frozenset(
    {
        "_fixture_meta",
        "object_type",
        "schema_version",
        "knowledge_character",
        "source_role",
        "source_descriptor_ref",
        "source_resolution_status",
        "temporal_scope",
        "measurement",
        "evidence_refs",
        "evidence_resolution_status",
        "rights_status",
        "sensitivity",
        "release_posture",
        "not_for_life_safety",
        "limitations",
    }
)
OBSERVATION_FIELDS = COMMON_FIELDS | frozenset(
    {
        "observation_id",
        "air_station_ref",
        "qa_state",
        "low_cost_sensor_caveat",
        "confidence_statement",
        "model_run_ref",
        "model_identity",
        "generated_at",
        "valid_at",
        "derived_from_refs",
    }
)
MODEL_FIELDS = COMMON_FIELDS | frozenset(
    {
        "model_context_id",
        "model_run_ref",
        "model_identity",
        "spatial_support",
        "lineage",
        "uncertainty",
        "air_station_ref",
        "observed_at",
        "qa_state",
        "observed_value",
    }
)
OBS_TEMPORAL_FIELDS = frozenset({"observed_at", "retrieved_at"})
MODEL_TEMPORAL_FIELDS = frozenset({"generated_at", "valid_at", "valid_until"})
OBS_MEASUREMENT_FIELDS = frozenset(
    {"parameter", "value", "unit", "averaging_period_minutes"}
)
MODEL_MEASUREMENT_FIELDS = frozenset({"parameter", "value", "unit"})
MODEL_IDENTITY_FIELDS = frozenset({"name", "version"})
SPATIAL_SUPPORT_FIELDS = frozenset({"kind", "support_ref"})
LINEAGE_FIELDS = frozenset({"relationship", "derived_from_refs"})
UNCERTAINTY_FIELDS = frozenset({"state", "statement"})

FORBIDDEN_OBSERVATION_FIELDS = frozenset(
    {"model_run_ref", "model_identity", "generated_at", "valid_at", "derived_from_refs"}
)
FORBIDDEN_MODEL_FIELDS = frozenset(
    {"air_station_ref", "observed_at", "qa_state", "observed_value"}
)

ABSTAIN_CODES = frozenset(
    {
        "EVIDENCE_UNRESOLVED",
        "QA_NOT_REVIEWED",
        "RIGHTS_UNRESOLVED",
        "SOURCE_UNRESOLVED",
        "UNCERTAINTY_UNRESOLVED",
    }
)
ERROR_CODES = frozenset({"FIXTURE_JSON_INVALID", "FIXTURE_TOO_LARGE"})


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]


def _parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed if parsed.utcoffset() is not None else None


def _string_list_is_valid(value: object, *, allow_empty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and len(value) <= MAX_REFS
        and all(is_nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


def _validate_common(candidate: dict[object, object], findings: set[Finding]) -> None:
    if candidate.get("schema_version") != "1.0.0":
        add_finding(findings, "SCHEMA_VERSION_INVALID", "$.schema_version")

    source_state = candidate.get("source_resolution_status")
    source_ref = candidate.get("source_descriptor_ref")
    if source_state == "bound":
        if not is_nonempty_string(source_ref):
            add_finding(findings, "SOURCE_DESCRIPTOR_REF_MISSING", "$.source_descriptor_ref")
    elif source_state == "unresolved":
        if source_ref is not None:
            add_finding(findings, "UNRESOLVED_SOURCE_REF_MUST_BE_NULL", "$.source_descriptor_ref")
        add_finding(findings, "SOURCE_UNRESOLVED", "$.source_resolution_status")
    else:
        add_finding(findings, "SOURCE_RESOLUTION_STATUS_INVALID", "$.source_resolution_status")

    evidence_state = candidate.get("evidence_resolution_status")
    evidence_refs = candidate.get("evidence_refs")
    if evidence_state == "bound":
        if not _string_list_is_valid(evidence_refs):
            add_finding(findings, "EVIDENCE_REFS_INVALID", "$.evidence_refs")
    elif evidence_state == "unresolved":
        if not _string_list_is_valid(evidence_refs, allow_empty=True) or evidence_refs:
            add_finding(findings, "UNRESOLVED_EVIDENCE_REFS_MUST_BE_EMPTY", "$.evidence_refs")
        add_finding(findings, "EVIDENCE_UNRESOLVED", "$.evidence_resolution_status")
    else:
        add_finding(findings, "EVIDENCE_RESOLUTION_STATUS_INVALID", "$.evidence_resolution_status")

    rights_status = candidate.get("rights_status")
    if rights_status not in {"cleared_open", "public_domain", "restricted", "unknown"}:
        add_finding(findings, "RIGHTS_STATUS_INVALID", "$.rights_status")
    elif rights_status == "unknown":
        add_finding(findings, "RIGHTS_UNRESOLVED", "$.rights_status")

    if candidate.get("sensitivity") not in {"public", "internal", "restricted", "sensitive"}:
        add_finding(findings, "SENSITIVITY_INVALID", "$.sensitivity")
    if candidate.get("release_posture") not in {"not_released", "candidate"}:
        add_finding(findings, "RELEASE_POSTURE_DENIED", "$.release_posture")
    if candidate.get("not_for_life_safety") is not True:
        add_finding(findings, "LIFE_SAFETY_BOUNDARY_REQUIRED", "$.not_for_life_safety")

    limitations = candidate.get("limitations")
    if (
        not isinstance(limitations, list)
        or not limitations
        or len(limitations) > MAX_LIMITATIONS
        or any(not is_nonempty_string(item) for item in limitations)
        or len(limitations) != len(set(limitations))
    ):
        add_finding(findings, "LIMITATIONS_INVALID", "$.limitations")


def _validate_measurement(
    measurement: object,
    findings: set[Finding],
    *,
    modeled: bool,
) -> None:
    if not isinstance(measurement, dict):
        add_finding(findings, "MEASUREMENT_INVALID", "$.measurement")
        return
    allowed = MODEL_MEASUREMENT_FIELDS if modeled else OBS_MEASUREMENT_FIELDS
    find_undeclared_fields(
        findings,
        measurement,
        allowed,
        "UNDECLARED_MEASUREMENT_FIELD",
        "$.measurement",
    )
    for field in ("parameter", "unit"):
        if not is_nonempty_string(measurement.get(field)):
            add_finding(findings, f"MEASUREMENT_{field.upper()}_INVALID", f"$.measurement.{field}")
    if not is_finite_number(measurement.get("value")):
        add_finding(findings, "MEASUREMENT_VALUE_INVALID", "$.measurement.value")
    if not modeled:
        period = measurement.get("averaging_period_minutes")
        if (
            not isinstance(period, int)
            or isinstance(period, bool)
            or not 1 <= period <= 10_080
        ):
            add_finding(
                findings,
                "AVERAGING_PERIOD_INVALID",
                "$.measurement.averaging_period_minutes",
            )


def _validate_observation(candidate: dict[object, object], findings: set[Finding]) -> None:
    find_undeclared_fields(
        findings,
        candidate,
        OBSERVATION_FIELDS,
        "UNDECLARED_TOP_LEVEL_FIELD",
        "$",
    )
    for field in FORBIDDEN_OBSERVATION_FIELDS:
        if field in candidate:
            add_finding(findings, "MODEL_AS_OBSERVATION_DENIED", f"$.{field}")
    if not is_nonempty_string(candidate.get("observation_id")):
        add_finding(findings, "OBSERVATION_ID_MISSING", "$.observation_id")
    if candidate.get("knowledge_character") != "OBSERVED_SENSOR":
        add_finding(findings, "OBSERVATION_CHARACTER_INVALID", "$.knowledge_character")
    source_role = candidate.get("source_role")
    if source_role not in {"observed", "low_cost_sensor"}:
        add_finding(findings, "OBSERVATION_SOURCE_ROLE_INVALID", "$.source_role")
    if not is_nonempty_string(candidate.get("air_station_ref")):
        add_finding(findings, "AIR_STATION_REF_MISSING", "$.air_station_ref")

    temporal = candidate.get("temporal_scope")
    if not isinstance(temporal, dict):
        add_finding(findings, "TEMPORAL_SCOPE_INVALID", "$.temporal_scope")
    else:
        find_undeclared_fields(
            findings,
            temporal,
            OBS_TEMPORAL_FIELDS,
            "UNDECLARED_TEMPORAL_FIELD",
            "$.temporal_scope",
        )
        observed = _parse_utc(temporal.get("observed_at"))
        retrieved = _parse_utc(temporal.get("retrieved_at"))
        if observed is None:
            add_finding(findings, "OBSERVED_TIME_INVALID", "$.temporal_scope.observed_at")
        if retrieved is None:
            add_finding(findings, "RETRIEVAL_TIME_INVALID", "$.temporal_scope.retrieved_at")
        if observed is not None and retrieved is not None and retrieved < observed:
            add_finding(findings, "TEMPORAL_ORDER_INVALID", "$.temporal_scope")

    _validate_measurement(candidate.get("measurement"), findings, modeled=False)

    qa_state = candidate.get("qa_state")
    if qa_state not in {"reviewed", "provisional", "unknown", "rejected"}:
        add_finding(findings, "QA_STATE_INVALID", "$.qa_state")
    elif qa_state in {"provisional", "unknown"}:
        add_finding(findings, "QA_NOT_REVIEWED", "$.qa_state")
    elif qa_state == "rejected":
        add_finding(findings, "QA_STATE_REJECTED", "$.qa_state")

    if source_role == "low_cost_sensor":
        if not is_nonempty_string(candidate.get("low_cost_sensor_caveat")):
            add_finding(findings, "LOW_COST_SENSOR_CAVEAT_REQUIRED", "$.low_cost_sensor_caveat")
        if not is_nonempty_string(candidate.get("confidence_statement")):
            add_finding(findings, "CONFIDENCE_STATEMENT_REQUIRED", "$.confidence_statement")


def _validate_model(candidate: dict[object, object], findings: set[Finding]) -> None:
    find_undeclared_fields(
        findings,
        candidate,
        MODEL_FIELDS,
        "UNDECLARED_TOP_LEVEL_FIELD",
        "$",
    )
    for field in FORBIDDEN_MODEL_FIELDS:
        if field in candidate:
            add_finding(findings, "OBSERVATION_AS_MODEL_DENIED", f"$.{field}")
    if not is_nonempty_string(candidate.get("model_context_id")):
        add_finding(findings, "MODEL_CONTEXT_ID_MISSING", "$.model_context_id")
    if candidate.get("knowledge_character") != "ATMOSPHERIC_MODEL_FIELD":
        add_finding(findings, "MODEL_CHARACTER_INVALID", "$.knowledge_character")
    if candidate.get("source_role") != "modeled":
        add_finding(findings, "MODEL_SOURCE_ROLE_INVALID", "$.source_role")
    if not is_nonempty_string(candidate.get("model_run_ref")):
        add_finding(findings, "MODEL_RUN_REF_MISSING", "$.model_run_ref")

    identity = candidate.get("model_identity")
    if not isinstance(identity, dict):
        add_finding(findings, "MODEL_IDENTITY_INVALID", "$.model_identity")
    else:
        find_undeclared_fields(
            findings,
            identity,
            MODEL_IDENTITY_FIELDS,
            "UNDECLARED_MODEL_IDENTITY_FIELD",
            "$.model_identity",
        )
        for field in MODEL_IDENTITY_FIELDS:
            if not is_nonempty_string(identity.get(field)):
                add_finding(findings, "MODEL_IDENTITY_INVALID", f"$.model_identity.{field}")

    temporal = candidate.get("temporal_scope")
    if not isinstance(temporal, dict):
        add_finding(findings, "TEMPORAL_SCOPE_INVALID", "$.temporal_scope")
    else:
        find_undeclared_fields(
            findings,
            temporal,
            MODEL_TEMPORAL_FIELDS,
            "UNDECLARED_TEMPORAL_FIELD",
            "$.temporal_scope",
        )
        generated = _parse_utc(temporal.get("generated_at"))
        valid_at = _parse_utc(temporal.get("valid_at"))
        valid_until_raw = temporal.get("valid_until")
        valid_until = None if valid_until_raw is None else _parse_utc(valid_until_raw)
        if generated is None:
            add_finding(findings, "GENERATED_TIME_INVALID", "$.temporal_scope.generated_at")
        if valid_at is None:
            add_finding(findings, "VALID_TIME_INVALID", "$.temporal_scope.valid_at")
        if valid_until_raw is not None and valid_until is None:
            add_finding(findings, "VALID_UNTIL_INVALID", "$.temporal_scope.valid_until")
        if generated is not None and valid_at is not None and valid_at < generated:
            add_finding(findings, "TEMPORAL_ORDER_INVALID", "$.temporal_scope")
        if valid_at is not None and valid_until is not None and valid_until < valid_at:
            add_finding(findings, "TEMPORAL_ORDER_INVALID", "$.temporal_scope")

    spatial = candidate.get("spatial_support")
    if not isinstance(spatial, dict):
        add_finding(findings, "SPATIAL_SUPPORT_INVALID", "$.spatial_support")
    else:
        find_undeclared_fields(
            findings,
            spatial,
            SPATIAL_SUPPORT_FIELDS,
            "UNDECLARED_SPATIAL_SUPPORT_FIELD",
            "$.spatial_support",
        )
        if spatial.get("kind") not in {"generalized_county", "statewide", "governed_grid_cell"}:
            add_finding(findings, "SPATIAL_SUPPORT_INVALID", "$.spatial_support.kind")
        if not is_nonempty_string(spatial.get("support_ref")):
            add_finding(findings, "SPATIAL_SUPPORT_REF_MISSING", "$.spatial_support.support_ref")

    _validate_measurement(candidate.get("measurement"), findings, modeled=True)

    lineage = candidate.get("lineage")
    if not isinstance(lineage, dict):
        add_finding(findings, "MODEL_LINEAGE_REQUIRED", "$.lineage")
    else:
        find_undeclared_fields(
            findings,
            lineage,
            LINEAGE_FIELDS,
            "UNDECLARED_LINEAGE_FIELD",
            "$.lineage",
        )
        if lineage.get("relationship") != "DERIVED_FROM":
            add_finding(findings, "DERIVED_FROM_RELATION_REQUIRED", "$.lineage.relationship")
        if not _string_list_is_valid(lineage.get("derived_from_refs")):
            add_finding(findings, "DERIVED_FROM_REFS_REQUIRED", "$.lineage.derived_from_refs")

    uncertainty = candidate.get("uncertainty")
    if not isinstance(uncertainty, dict):
        add_finding(findings, "UNCERTAINTY_REQUIRED", "$.uncertainty")
    else:
        find_undeclared_fields(
            findings,
            uncertainty,
            UNCERTAINTY_FIELDS,
            "UNDECLARED_UNCERTAINTY_FIELD",
            "$.uncertainty",
        )
        state = uncertainty.get("state")
        if state not in {"quantified", "qualitative", "unknown"}:
            add_finding(findings, "UNCERTAINTY_STATE_INVALID", "$.uncertainty.state")
        elif state == "unknown":
            add_finding(findings, "UNCERTAINTY_UNRESOLVED", "$.uncertainty.state")
        if not is_nonempty_string(uncertainty.get("statement")):
            add_finding(findings, "UNCERTAINTY_STATEMENT_REQUIRED", "$.uncertainty.statement")

    limitations = candidate.get("limitations")
    if isinstance(limitations, list) and "not_an_observation" not in limitations:
        add_finding(findings, "NOT_AN_OBSERVATION_LIMIT_REQUIRED", "$.limitations")


def validate_candidate(candidate: object) -> list[Finding]:
    """Return stable, sorted, non-echoing findings for one decoded candidate."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("CANDIDATE_NOT_OBJECT", "$")]

    object_type = candidate.get("object_type")
    if object_type == "AirObservation":
        _validate_common(candidate, findings)
        _validate_observation(candidate, findings)
    elif object_type == "ForecastContext":
        _validate_common(candidate, findings)
        _validate_model(candidate, findings)
    else:
        add_finding(findings, "OBJECT_TYPE_UNKNOWN", "$.object_type")
    return sorted(findings)


def outcome_for_findings(findings: Sequence[Finding]) -> str:
    codes = {finding.code for finding in findings}
    if not codes:
        return "PASS"
    if codes & ERROR_CODES:
        return "ERROR"
    if codes <= ABSTAIN_CODES:
        return "ABSTAIN"
    return "DENY"


def validate_file(path: Path | str) -> ValidationResult:
    findings = tuple(validate_fixture_file(path, validate_candidate))
    return ValidationResult(outcome_for_findings(findings), findings)


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": str(path),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "scope": "atmosphere-observed-modeled-separation",
            "status": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate bounded Atmosphere observed-versus-modeled candidates."
    )
    parser.add_argument("files", nargs="*", type=Path)
    args = parser.parse_args(argv)
    if not args.files:
        print("at least one fixture file is required", file=sys.stderr)
        return 2

    failed = False
    for path in sorted(args.files, key=lambda item: str(item)):
        result = validate_file(path)
        failed = failed or result.outcome in {"DENY", "ERROR"}
        print(_serialize(path, result))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
