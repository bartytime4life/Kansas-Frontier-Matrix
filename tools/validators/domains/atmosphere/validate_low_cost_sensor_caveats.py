#!/usr/bin/env python3
"""Validate the frozen synthetic Atmosphere low-cost-sensor calibration profile.

This validator proves a narrow fixture-only qualification and anti-collapse
boundary. It does not train or apply a correction model, validate scientific
fitness, resolve evidence, admit a source, evaluate Rego policy, assess air
quality, issue guidance, or authorize promotion, release, or publication.
"""

from __future__ import annotations

from datetime import datetime
import hashlib
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
    is_nonempty_string,
    run_cli,
    validate_fixture_file,
)


PROFILE_ID = "kfm-atmosphere-low-cost-sensor-calibration-fixture-v1"
MAX_EVIDENCE_REFS = 32
MAX_LIMITATIONS = 16
SOURCE_DESCRIPTOR_REF = "fixture://source/atmosphere/low-cost-sensor"
REFERENCE_SOURCE_DESCRIPTOR_REF = "fixture://source/atmosphere/reference-monitor"
RAW_EVIDENCE_REF = "fixture://evidence/atmosphere/raw-observation"
REFERENCE_EVIDENCE_REF = "fixture://evidence/atmosphere/reference-collocation"
EVALUATION_EVIDENCE_REF = "fixture://evidence/atmosphere/held-out-evaluation"
MODEL_REF = (
    "fixture://artifact/atmosphere/model/"
    "synthetic-meteorology-aware-reference-correction@fixture-v1"
)
TRAINING_DATA_REF = (
    "fixture://artifact/atmosphere/training/"
    "synthetic-midcontinent-context@fixture-v1"
)
SPECIFICATION_REF = (
    "fixture://artifact/atmosphere/specification/"
    "low-cost-sensor-calibration@fixture-v1"
)
RAW_OBSERVATION_REF_BY_STATUS = {
    "UNCORRECTED_CONTEXT_ONLY": "fixture://observation/atmosphere/raw-context",
    "CORRECTED_WITH_LINEAGE": (
        "fixture://observation/atmosphere/raw-corrected-pair"
    ),
}
CORRECTED_OBSERVATION_REF = "fixture://observation/atmosphere/corrected-pair"
FIXTURE_COUNTY_FIPS = "99999"
HARDWARE_FAMILY = "synthetic-low-cost-optical-sensor"
SAMPLING_CADENCE = "hourly"
DEPLOYMENT_REGIME = "synthetic-midcontinent-context"
METHOD_ID = "synthetic-meteorology-aware-reference-correction"
METHOD_VERSION = "fixture-v1"

ALLOWED_TOP_LEVEL_FIELDS = frozenset(
    {
        "fixture_id",
        "profile_id",
        "object_family",
        "knowledge_character",
        "source_role",
        "source_descriptor_ref",
        "evidence_refs",
        "calibration",
        "assessment",
        "spatial_support",
        "governance",
        "limitations",
    }
)
ALLOWED_CALIBRATION_FIELDS = frozenset(
    {
        "status",
        "method_id",
        "method_version",
        "model_sha256",
        "training_data_sha256",
        "specification_sha256",
        "model_ref",
        "training_data_ref",
        "specification_ref",
        "raw_observation_ref",
        "raw_evidence_ref",
        "corrected_observation_ref",
        "reference_collocation",
        "meteorology_inputs",
        "applicability",
        "evaluation",
    }
)
ALLOWED_REFERENCE_COLLOCATION_FIELDS = frozenset(
    {
        "state",
        "source_descriptor_ref",
        "evidence_ref",
        "period_start",
        "period_end",
    }
)
ALLOWED_APPLICABILITY_FIELDS = frozenset(
    {
        "hardware_family",
        "sampling_cadence",
        "deployment_regime",
        "transfer_state",
        "drift_state",
    }
)
ALLOWED_EVALUATION_FIELDS = frozenset(
    {
        "state",
        "evidence_ref",
        "metric_names",
        "uncertainty_state",
        "validity_bound",
    }
)
ALLOWED_ASSESSMENT_FIELDS = frozenset(
    {
        "caveat",
        "confidence_state",
        "reference_grade",
        "regulatory_use",
        "public_release_eligible",
    }
)
ALLOWED_SPATIAL_SUPPORT_FIELDS = frozenset({"kind", "county_fips"})
ALLOWED_GOVERNANCE_FIELDS = frozenset(
    {
        "rights_state",
        "sensitivity_state",
        "review_state",
        "release_state",
        "promotion_eligible",
        "rollback_state",
    }
)
FORBIDDEN_LOCATION_ALIASES = frozenset(
    {
        "lat",
        "latitude",
        "lon",
        "lng",
        "longitude",
        "x",
        "y",
        "bbox",
        "centroid",
        "easting",
        "northing",
        "station_coordinates",
    }
)
ALLOWED_METEOROLOGY_INPUTS = frozenset(
    {
        "air_temperature",
        "relative_humidity",
        "pressure",
        "wind_speed",
        "wind_direction",
    }
)
EXPECTED_GOVERNANCE = {
    "rights_state": "fixture_only",
    "sensitivity_state": "public_safe_fixture",
    "review_state": "fixture_only",
    "release_state": "not_released",
    "promotion_eligible": False,
    "rollback_state": "fixture_only",
}
BASE_LIMITATIONS = frozenset(
    {
        "not_reference_grade",
        "not_regulatory_use",
        "not_life_safety_guidance",
        "synthetic_fixture_only",
    }
)
STATUS_LIMITATION = {
    "UNCORRECTED_CONTEXT_ONLY": "uncorrected_context_only",
    "CORRECTED_WITH_LINEAGE": "correction_not_scientifically_validated",
}
CONFIDENCE_BY_STATUS = {
    "UNCORRECTED_CONTEXT_ONLY": "CAVEATED_CONTEXT_ONLY",
    "CORRECTED_WITH_LINEAGE": "SYNTHETIC_VALIDATION_ONLY",
}
EXPECTED_EVIDENCE_REFS = {
    "UNCORRECTED_CONTEXT_ONLY": frozenset({RAW_EVIDENCE_REF}),
    "CORRECTED_WITH_LINEAGE": frozenset(
        {
            RAW_EVIDENCE_REF,
            REFERENCE_EVIDENCE_REF,
            EVALUATION_EVIDENCE_REF,
            MODEL_REF,
            TRAINING_DATA_REF,
            SPECIFICATION_REF,
        }
    ),
}


def _identity_digest(value: str) -> str:
    """Pin an exact fixture identity; this is not an artifact-content digest."""

    return f"sha256:{hashlib.sha256(value.encode('utf-8')).hexdigest()}"


EXPECTED_IDENTITY_FIELDS = {
    "model_ref": (MODEL_REF, "model_sha256", _identity_digest(MODEL_REF)),
    "training_data_ref": (
        TRAINING_DATA_REF,
        "training_data_sha256",
        _identity_digest(TRAINING_DATA_REF),
    ),
    "specification_ref": (
        SPECIFICATION_REF,
        "specification_sha256",
        _identity_digest(SPECIFICATION_REF),
    ),
}


def _string_list_is_valid(value: object, *, maximum: int, allow_empty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (allow_empty or bool(value))
        and len(value) <= maximum
        and all(is_nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


def _is_fixture_ref(value: object) -> bool:
    return is_nonempty_string(value) and value.startswith("fixture://")


def _canonical_utc(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return None


def _validate_reference_collocation(
    findings: set[Finding],
    value: object,
    *,
    evidence_refs: object,
    corrected: bool,
) -> None:
    path = "$.calibration.reference_collocation"
    if not isinstance(value, dict):
        add_finding(findings, "REFERENCE_COLLOCATION_INVALID", path)
        return

    find_undeclared_fields(
        findings,
        value,
        ALLOWED_REFERENCE_COLLOCATION_FIELDS,
        "UNDECLARED_REFERENCE_COLLOCATION_FIELD",
        path,
    )
    if not corrected:
        expected = {
            "state": "NOT_CLAIMED",
            "source_descriptor_ref": None,
            "evidence_ref": None,
            "period_start": None,
            "period_end": None,
        }
        if any(value.get(field) != expected_value for field, expected_value in expected.items()):
            add_finding(findings, "UNCORRECTED_REFERENCE_CLAIM_INVALID", path)
        return

    if value.get("state") != "SYNTHETIC_EVIDENCE_BOUND":
        add_finding(findings, "REFERENCE_COLLOCATION_REQUIRED", path)
        return

    source_ref = value.get("source_descriptor_ref")
    evidence_ref = value.get("evidence_ref")
    if not is_nonempty_string(source_ref):
        add_finding(
            findings,
            "REFERENCE_SOURCE_DESCRIPTOR_REF_MISSING",
            f"{path}.source_descriptor_ref",
        )
    elif source_ref != REFERENCE_SOURCE_DESCRIPTOR_REF:
        add_finding(
            findings,
            "REFERENCE_SOURCE_DESCRIPTOR_REF_INVALID",
            f"{path}.source_descriptor_ref",
        )
    if not is_nonempty_string(evidence_ref):
        add_finding(findings, "REFERENCE_EVIDENCE_REF_MISSING", f"{path}.evidence_ref")
    elif evidence_ref != REFERENCE_EVIDENCE_REF:
        add_finding(
            findings,
            "REFERENCE_EVIDENCE_REF_INVALID",
            f"{path}.evidence_ref",
        )
    elif not isinstance(evidence_refs, list) or evidence_ref not in evidence_refs:
        add_finding(findings, "REFERENCE_EVIDENCE_REF_UNBOUND", f"{path}.evidence_ref")

    start = _canonical_utc(value.get("period_start"))
    end = _canonical_utc(value.get("period_end"))
    if start is None:
        add_finding(findings, "REFERENCE_COLLOCATION_TIME_INVALID", f"{path}.period_start")
    if end is None:
        add_finding(findings, "REFERENCE_COLLOCATION_TIME_INVALID", f"{path}.period_end")
    if start is not None and end is not None and start >= end:
        add_finding(findings, "REFERENCE_COLLOCATION_TIME_ORDER_INVALID", path)


def _validate_applicability(
    findings: set[Finding],
    value: object,
    *,
    corrected: bool,
) -> None:
    path = "$.calibration.applicability"
    if not isinstance(value, dict):
        add_finding(findings, "APPLICABILITY_INVALID", path)
        return

    find_undeclared_fields(
        findings,
        value,
        ALLOWED_APPLICABILITY_FIELDS,
        "UNDECLARED_APPLICABILITY_FIELD",
        path,
    )
    for field, expected, code in (
        ("hardware_family", HARDWARE_FAMILY, "HARDWARE_FAMILY_INVALID"),
        ("sampling_cadence", SAMPLING_CADENCE, "SAMPLING_CADENCE_INVALID"),
        ("deployment_regime", DEPLOYMENT_REGIME, "DEPLOYMENT_REGIME_INVALID"),
    ):
        if value.get(field) != expected:
            add_finding(findings, code, f"{path}.{field}")

    expected_transfer = "SYNTHETIC_BOUND_ONLY" if corrected else "NOT_ASSESSED"
    expected_drift = "SYNTHETIC_CHECKED" if corrected else "NOT_ASSESSED"
    if value.get("transfer_state") != expected_transfer:
        add_finding(findings, "TRANSFER_STATE_INVALID", f"{path}.transfer_state")
    if value.get("drift_state") != expected_drift:
        add_finding(findings, "DRIFT_STATE_INVALID", f"{path}.drift_state")


def _validate_evaluation(
    findings: set[Finding],
    value: object,
    *,
    evidence_refs: object,
    corrected: bool,
) -> None:
    path = "$.calibration.evaluation"
    if not isinstance(value, dict):
        add_finding(findings, "EVALUATION_INVALID", path)
        return

    find_undeclared_fields(
        findings,
        value,
        ALLOWED_EVALUATION_FIELDS,
        "UNDECLARED_EVALUATION_FIELD",
        path,
    )
    expected = (
        {
            "state": "SYNTHETIC_HELD_OUT",
            "evidence_ref": EVALUATION_EVIDENCE_REF,
            "metric_names": ["bias", "mae"],
            "uncertainty_state": "SYNTHETIC_NOT_QUANTITATIVE",
            "validity_bound": "DECLARED_DEPLOYMENT_REGIME_ONLY",
        }
        if corrected
        else {
            "state": "NOT_CLAIMED",
            "evidence_ref": None,
            "metric_names": [],
            "uncertainty_state": "NOT_ASSESSED",
            "validity_bound": "NOT_ASSESSED",
        }
    )
    for field, expected_value in expected.items():
        if value.get(field) != expected_value:
            add_finding(findings, "EVALUATION_STATE_INVALID", f"{path}.{field}")
    evidence_ref = value.get("evidence_ref")
    if corrected and (
        not isinstance(evidence_refs, list) or evidence_ref not in evidence_refs
    ):
        add_finding(findings, "EVALUATION_EVIDENCE_REF_UNBOUND", f"{path}.evidence_ref")


def _validate_calibration(
    findings: set[Finding],
    value: object,
    *,
    evidence_refs: object,
) -> str | None:
    path = "$.calibration"
    if not isinstance(value, dict):
        add_finding(findings, "CALIBRATION_INVALID", path)
        return None

    find_undeclared_fields(
        findings,
        value,
        ALLOWED_CALIBRATION_FIELDS,
        "UNDECLARED_CALIBRATION_FIELD",
        path,
    )
    status = value.get("status")
    if status not in STATUS_LIMITATION:
        add_finding(findings, "CALIBRATION_STATUS_INVALID", f"{path}.status")
        return None
    corrected = status == "CORRECTED_WITH_LINEAGE"

    raw_ref = value.get("raw_observation_ref")
    raw_evidence_ref = value.get("raw_evidence_ref")
    corrected_ref = value.get("corrected_observation_ref")
    if not is_nonempty_string(raw_ref):
        add_finding(findings, "RAW_OBSERVATION_REF_MISSING", f"{path}.raw_observation_ref")
    elif raw_ref != RAW_OBSERVATION_REF_BY_STATUS[status]:
        add_finding(
            findings,
            "RAW_OBSERVATION_REF_INVALID",
            f"{path}.raw_observation_ref",
        )
    if raw_evidence_ref != RAW_EVIDENCE_REF:
        add_finding(findings, "RAW_EVIDENCE_REF_INVALID", f"{path}.raw_evidence_ref")
    if not isinstance(evidence_refs, list) or raw_evidence_ref not in evidence_refs:
        add_finding(findings, "RAW_EVIDENCE_REF_UNBOUND", f"{path}.raw_evidence_ref")

    lineage_fields = (
        "method_id",
        "method_version",
        "model_ref",
        "model_sha256",
        "training_data_ref",
        "training_data_sha256",
        "specification_ref",
        "specification_sha256",
    )
    if corrected:
        if value.get("method_id") != METHOD_ID:
            add_finding(findings, "CORRECTION_METHOD_ID_INVALID", f"{path}.method_id")
        if value.get("method_version") != METHOD_VERSION:
            add_finding(
                findings,
                "CORRECTION_METHOD_VERSION_INVALID",
                f"{path}.method_version",
            )
        for reference_field, (
            expected_reference,
            digest_field,
            expected_digest,
        ) in EXPECTED_IDENTITY_FIELDS.items():
            reference = value.get(reference_field)
            if reference != expected_reference:
                add_finding(
                    findings,
                    "CALIBRATION_IDENTITY_REF_INVALID",
                    f"{path}.{reference_field}",
                )
            elif not isinstance(evidence_refs, list) or reference not in evidence_refs:
                add_finding(
                    findings,
                    "CALIBRATION_IDENTITY_REF_UNBOUND",
                    f"{path}.{reference_field}",
                )
            if value.get(digest_field) != expected_digest:
                add_finding(
                    findings,
                    "CALIBRATION_IDENTITY_DIGEST_INVALID",
                    f"{path}.{digest_field}",
                )
        if not is_nonempty_string(corrected_ref):
            add_finding(
                findings,
                "CORRECTED_OBSERVATION_REF_MISSING",
                f"{path}.corrected_observation_ref",
            )
        elif corrected_ref == raw_ref:
            add_finding(
                findings,
                "RAW_CORRECTED_PAIR_COLLAPSED",
                f"{path}.corrected_observation_ref",
            )
        elif corrected_ref != CORRECTED_OBSERVATION_REF:
            add_finding(
                findings,
                "CORRECTED_OBSERVATION_REF_INVALID",
                f"{path}.corrected_observation_ref",
            )
    else:
        for field in lineage_fields:
            if value.get(field) is not None:
                add_finding(findings, "UNCORRECTED_LINEAGE_CONFLICT", f"{path}.{field}")
        if corrected_ref is not None:
            add_finding(
                findings,
                "UNCORRECTED_LINEAGE_CONFLICT",
                f"{path}.corrected_observation_ref",
            )

    _validate_reference_collocation(
        findings,
        value.get("reference_collocation"),
        evidence_refs=evidence_refs,
        corrected=corrected,
    )
    _validate_evaluation(
        findings,
        value.get("evaluation"),
        evidence_refs=evidence_refs,
        corrected=corrected,
    )

    meteorology_inputs = value.get("meteorology_inputs")
    if not _string_list_is_valid(
        meteorology_inputs,
        maximum=len(ALLOWED_METEOROLOGY_INPUTS),
        allow_empty=not corrected,
    ):
        add_finding(
            findings,
            "METEOROLOGY_INPUTS_REQUIRED" if corrected else "METEOROLOGY_INPUTS_INVALID",
            f"{path}.meteorology_inputs",
        )
    elif isinstance(meteorology_inputs, list):
        if any(item not in ALLOWED_METEOROLOGY_INPUTS for item in meteorology_inputs):
            add_finding(findings, "METEOROLOGY_INPUTS_INVALID", f"{path}.meteorology_inputs")
        elif corrected and not {"air_temperature", "relative_humidity"}.issubset(
            meteorology_inputs
        ):
            add_finding(
                findings,
                "METEOROLOGY_INPUTS_REQUIRED",
                f"{path}.meteorology_inputs",
            )

    _validate_applicability(findings, value.get("applicability"), corrected=corrected)
    return status


def _validate_assessment(
    findings: set[Finding],
    value: object,
    *,
    status: str | None,
) -> None:
    path = "$.assessment"
    if not isinstance(value, dict):
        add_finding(findings, "ASSESSMENT_INVALID", path)
        return

    find_undeclared_fields(
        findings,
        value,
        ALLOWED_ASSESSMENT_FIELDS,
        "UNDECLARED_ASSESSMENT_FIELD",
        path,
    )
    if "caveat" not in value:
        add_finding(findings, "CAVEAT_MISSING", f"{path}.caveat")
    elif value.get("caveat") != "LOW_COST_SENSOR_NOT_REFERENCE_GRADE":
        add_finding(findings, "CAVEAT_INVALID", f"{path}.caveat")

    expected_confidence = CONFIDENCE_BY_STATUS.get(status)
    if expected_confidence is None or value.get("confidence_state") != expected_confidence:
        add_finding(findings, "CONFIDENCE_STATE_INVALID", f"{path}.confidence_state")

    if value.get("reference_grade") is not False:
        add_finding(
            findings,
            "REFERENCE_GRADE_OVERCLAIM_DENIED",
            f"{path}.reference_grade",
        )
    if value.get("regulatory_use") is not False:
        add_finding(findings, "REGULATORY_USE_DENIED", f"{path}.regulatory_use")
    if value.get("public_release_eligible") is not False:
        add_finding(
            findings,
            "PUBLIC_RELEASE_ELIGIBILITY_DENIED",
            f"{path}.public_release_eligible",
        )


def _validate_spatial_support(findings: set[Finding], value: object) -> None:
    path = "$.spatial_support"
    if not isinstance(value, dict):
        add_finding(findings, "SPATIAL_SUPPORT_INVALID", path)
        return
    find_undeclared_fields(
        findings,
        value,
        ALLOWED_SPATIAL_SUPPORT_FIELDS,
        "UNDECLARED_SPATIAL_SUPPORT_FIELD",
        path,
    )
    for key in value:
        if isinstance(key, str) and key.casefold() in FORBIDDEN_LOCATION_ALIASES:
            add_finding(findings, "PRECISE_SITE_EXPOSURE_DENIED", f"{path}.{key}")
    if value.get("kind") in {"exact_site", "exact_station", "point", "coordinates"}:
        add_finding(findings, "PRECISE_SITE_EXPOSURE_DENIED", f"{path}.kind")
    if value.get("kind") != "generalized_county":
        add_finding(findings, "SPATIAL_SUPPORT_NOT_PUBLIC_SAFE", f"{path}.kind")
    if value.get("county_fips") != FIXTURE_COUNTY_FIPS:
        add_finding(findings, "COUNTY_FIPS_INVALID", f"{path}.county_fips")


def _validate_governance(findings: set[Finding], value: object) -> None:
    path = "$.governance"
    if not isinstance(value, dict):
        add_finding(findings, "GOVERNANCE_INVALID", path)
        return
    find_undeclared_fields(
        findings,
        value,
        ALLOWED_GOVERNANCE_FIELDS,
        "UNDECLARED_GOVERNANCE_FIELD",
        path,
    )
    for field, expected in EXPECTED_GOVERNANCE.items():
        actual = value.get(field)
        matches = actual is False if expected is False else actual == expected
        if not matches:
            add_finding(findings, "GOVERNANCE_STATE_INVALID", f"{path}.{field}")


def validate_candidate(candidate: object) -> list[Finding]:
    """Return sorted, non-echoing findings for one decoded fixture candidate."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return [Finding("CANDIDATE_NOT_OBJECT", "$")]

    find_undeclared_fields(
        findings,
        candidate,
        ALLOWED_TOP_LEVEL_FIELDS,
        "UNDECLARED_TOP_LEVEL_FIELD",
        "$",
    )
    if not is_nonempty_string(candidate.get("fixture_id")):
        add_finding(findings, "FIXTURE_ID_MISSING", "$.fixture_id")
    if candidate.get("profile_id") != PROFILE_ID:
        add_finding(findings, "PROFILE_ID_INVALID", "$.profile_id")
    if candidate.get("object_family") != "PM25Observation":
        add_finding(findings, "OBJECT_FAMILY_INVALID", "$.object_family")
    if candidate.get("knowledge_character") != "LOW_COST_SENSOR":
        add_finding(findings, "KNOWLEDGE_CHARACTER_INVALID", "$.knowledge_character")
    if candidate.get("source_role") != "observed":
        add_finding(findings, "SOURCE_ROLE_INVALID", "$.source_role")
    if not is_nonempty_string(candidate.get("source_descriptor_ref")):
        add_finding(
            findings,
            "SOURCE_DESCRIPTOR_REF_MISSING",
            "$.source_descriptor_ref",
        )
    elif candidate.get("source_descriptor_ref") != SOURCE_DESCRIPTOR_REF:
        add_finding(
            findings,
            "SOURCE_DESCRIPTOR_REF_INVALID",
            "$.source_descriptor_ref",
        )

    evidence_refs = candidate.get("evidence_refs")
    if not _string_list_is_valid(evidence_refs, maximum=MAX_EVIDENCE_REFS):
        code = (
            "EVIDENCE_REF_COUNT_EXCEEDED"
            if isinstance(evidence_refs, list) and len(evidence_refs) > MAX_EVIDENCE_REFS
            else "EVIDENCE_REFS_INVALID"
        )
        add_finding(findings, code, "$.evidence_refs")
    elif isinstance(evidence_refs, list):
        for index, evidence_ref in enumerate(evidence_refs):
            if not _is_fixture_ref(evidence_ref):
                add_finding(
                    findings,
                    "EVIDENCE_REF_NOT_FIXTURE_LOCAL",
                    f"$.evidence_refs[{index}]",
                )

    status = _validate_calibration(
        findings,
        candidate.get("calibration"),
        evidence_refs=evidence_refs,
    )
    if status in EXPECTED_EVIDENCE_REFS and isinstance(evidence_refs, list):
        expected_refs = EXPECTED_EVIDENCE_REFS[status]
        if set(evidence_refs) != expected_refs or len(evidence_refs) != len(expected_refs):
            add_finding(findings, "EVIDENCE_REF_SET_INVALID", "$.evidence_refs")
    _validate_assessment(findings, candidate.get("assessment"), status=status)
    _validate_spatial_support(findings, candidate.get("spatial_support"))
    _validate_governance(findings, candidate.get("governance"))

    limitations = candidate.get("limitations")
    if not _string_list_is_valid(limitations, maximum=MAX_LIMITATIONS):
        code = (
            "LIMITATION_COUNT_EXCEEDED"
            if isinstance(limitations, list) and len(limitations) > MAX_LIMITATIONS
            else "LIMITATIONS_INVALID"
        )
        add_finding(findings, code, "$.limitations")
    elif status in STATUS_LIMITATION:
        expected = BASE_LIMITATIONS | {STATUS_LIMITATION[status]}
        if set(limitations) != expected or len(limitations) != len(expected):
            add_finding(findings, "LIMITATIONS_INVALID", "$.limitations")

    return sorted(findings)


def validate_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_candidate)


def main(argv: Sequence[str] | None = None) -> int:
    return run_cli(
        argv=argv,
        description=(
            "Validate the frozen synthetic Atmosphere low-cost-sensor "
            "calibration-qualification fixture profile."
        ),
        scope="atmosphere-low-cost-sensor-calibration-fixture",
        validator=validate_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
