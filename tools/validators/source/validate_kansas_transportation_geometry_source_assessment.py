#!/usr/bin/env python3
"""Validate the fixture-only Kansas transportation geometry source assessment.

A PASS proves only deterministic internal coherence. This validator performs no
network access, credential resolution, source admission, lifecycle mutation,
release, publication, or public-use authorization.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/source/kansas_transportation_geometry_source_assessment.schema.json"
CASES = ROOT / "fixtures/contracts/v1/source/kansas_transportation_geometry_source_assessment/cases.json"
MAX_BYTES = 2 * 1024 * 1024
MAX_FINDINGS = 100
IDENTITY_PREFIX = "ks-transport-geometry-assessment:"
EXPECTED_LIMITATIONS = [
    "FIXTURE_ONLY_REFERENCES_UNRESOLVED",
    "NO_LIVE_ENDPOINT_OR_PAYLOAD_ACCESS",
    "NO_CANONICAL_ROAD_OR_CROSSWALK_AUTHORITY",
    "NO_SOURCE_EVIDENCE_POLICY_RELEASE_OR_PUBLIC_USE_AUTHORITY",
]
EXPECTED_LANE_ORDER = [
    "DASC_NG911_ROAD_CENTERLINE",
    "KDOT_KHUB_LRS",
    "KDOT_MOBILE_LIDAR",
    "DASC_SUPPORTING_PRODUCTS",
]
EXPECTED_LANES: dict[str, dict[str, Any]] = {
    "DASC_NG911_ROAD_CENTERLINE": {
        "source_role": "ROAD_GEOMETRY_REFERENCE",
        "interface_ref": "kfm://source-interface/dasc/ng911-road-centerline/mapserver/1",
        "layer_id": 1,
        "source_crs": "EPSG:3395",
        "max_record_count": 1000,
        "query_formats": ["GEOJSON", "JSON"],
        "authentication_posture": "PUBLIC_METADATA",
        "identifier_state": "VERIFIED_METADATA",
        "identifier_roles": [
            {"field": "LRSKEY", "semantic_role": "CROSSWALK_CANDIDATE"},
            {"field": "NGSEGID", "semantic_role": "NG911_SEGMENT_ID"},
        ],
        "rights_state": "UNRESOLVED",
        "sensitivity_state": "REVIEW_REQUIRED",
        "snapshot_identity_state": "UNRESOLVED",
        "public_precision_state": "UNREVIEWED",
        "precision_policy_ref": None,
        "declared_disposition": "ADMIT_REFERENCE_CANDIDATE",
        "blocking_codes": [
            "IDENTIFIER_LIFECYCLE_UNRESOLVED",
            "PUBLIC_PRECISION_REVIEW_REQUIRED",
            "REDISTRIBUTION_RIGHTS_UNRESOLVED",
            "SNAPSHOT_IDENTITY_UNRESOLVED",
            "UPDATE_SEMANTICS_UNRESOLVED",
        ],
    },
    "KDOT_KHUB_LRS": {
        "source_role": "LRS_ROUTE_REFERENCE",
        "interface_ref": "kfm://source-interface/kdot/state-system-kups/mapserver/0",
        "layer_id": 0,
        "source_crs": "ESRI:6923",
        "max_record_count": 2000,
        "query_formats": ["GEOJSON", "JSON", "PBF"],
        "authentication_posture": "PUBLIC_METADATA",
        "identifier_state": "VERIFIED_METADATA",
        "identifier_roles": [
            {"field": "EventID", "semantic_role": "KHUB_EVENT_ID"},
            {"field": "GlobalID", "semantic_role": "OBJECT_STORE_ID"},
            {"field": "RouteID", "semantic_role": "KHUB_ROUTE_ID"},
        ],
        "rights_state": "UNRESOLVED",
        "sensitivity_state": "REVIEW_REQUIRED",
        "snapshot_identity_state": "UNRESOLVED",
        "public_precision_state": "UNREVIEWED",
        "precision_policy_ref": None,
        "declared_disposition": "ADMIT_REFERENCE_CANDIDATE",
        "blocking_codes": [
            "AUTHORITATIVE_DESIGNATION_UNRESOLVED",
            "IDENTIFIER_SUPERSESSION_UNRESOLVED",
            "PUBLIC_DOWNLOAD_RIGHTS_UNRESOLVED",
            "SNAPSHOT_IDENTITY_UNRESOLVED",
            "UPDATE_SEMANTICS_UNRESOLVED",
        ],
    },
    "KDOT_MOBILE_LIDAR": {
        "source_role": "TRANSPORTATION_OBSERVATION_DERIVATIVE",
        "interface_ref": "kfm://source-interface/kdot/mobile-lidar/project-portal",
        "layer_id": None,
        "source_crs": "SOURCE_DEFINED",
        "max_record_count": None,
        "query_formats": [],
        "authentication_posture": "ACCOUNT_REQUIRED",
        "identifier_state": "UNRESOLVED",
        "identifier_roles": [],
        "rights_state": "UNRESOLVED",
        "sensitivity_state": "REVIEW_REQUIRED",
        "snapshot_identity_state": "UNRESOLVED",
        "public_precision_state": "UNREVIEWED",
        "precision_policy_ref": None,
        "declared_disposition": "HOLD",
        "blocking_codes": [
            "ACCOUNT_REQUIRED",
            "DERIVATIVE_METHOD_UNRESOLVED",
            "PRODUCT_RIGHTS_UNRESOLVED",
            "PUBLIC_PRECISION_REVIEW_REQUIRED",
            "SNAPSHOT_IDENTITY_UNRESOLVED",
        ],
    },
    "DASC_SUPPORTING_PRODUCTS": {
        "source_role": "CATALOG_STEWARDSHIP_REFERENCE",
        "interface_ref": "kfm://source-interface/dasc/supporting-products/catalog",
        "layer_id": None,
        "source_crs": "SOURCE_DEFINED",
        "max_record_count": None,
        "query_formats": [],
        "authentication_posture": "PRODUCT_SPECIFIC",
        "identifier_state": "PRODUCT_SPECIFIC_UNRESOLVED",
        "identifier_roles": [],
        "rights_state": "UNRESOLVED",
        "sensitivity_state": "REVIEW_REQUIRED",
        "snapshot_identity_state": "UNRESOLVED",
        "public_precision_state": "UNREVIEWED",
        "precision_policy_ref": None,
        "declared_disposition": "ADMIT_REFERENCE_CANDIDATE",
        "blocking_codes": [
            "AUTHORITATIVE_DESIGNATION_PER_PRODUCT",
            "PRODUCT_RIGHTS_UNRESOLVED",
            "SNAPSHOT_IDENTITY_UNRESOLVED",
        ],
    },
}
EXPECTED_CROSSWALK_ROLES = {
    "NGSEGID": "NG911_SEGMENT_ID",
    "LRSKEY": "CROSSWALK_CANDIDATE",
    "RouteID": "KHUB_ROUTE_ID",
    "EventID": "KHUB_EVENT_ID",
    "GlobalID": "OBJECT_STORE_ID",
}
EXPECTED_EFFECTS = {
    "network_accessed": False,
    "credentials_resolved": False,
    "source_admitted": False,
    "connector_created": False,
    "schedule_created": False,
    "lifecycle_mutated": False,
    "road_authority_decided": False,
    "crosswalk_authority_decided": False,
    "evidence_resolved": False,
    "policy_decided": False,
    "release_authorized": False,
    "published": False,
    "public_use_authorized": False,
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("TRANSPORT_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("TRANSPORT_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("TRANSPORT_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("TRANSPORT_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("TRANSPORT_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("TRANSPORT_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("TRANSPORT_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def identity_subject(value: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(value))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(value: Mapping[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(_canonical_json(identity_subject(value))).hexdigest()


def expected_assessment_id(value: Mapping[str, Any]) -> str:
    return IDENTITY_PREFIX + canonical_spec_hash(value).removeprefix("sha256:")[:24]


def assign_identity(value: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(value))
    result["spec_hash"] = canonical_spec_hash(result)
    result["assessment_id"] = expected_assessment_id(result)
    return result


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema, format_checker=FormatChecker()
                ).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("TRANSPORT_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("TRANSPORT_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("TRANSPORT_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _core_semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    lanes = value.get("lanes")
    if not isinstance(lanes, list):
        return ()

    lane_ids = [lane.get("lane_id") for lane in lanes if isinstance(lane, Mapping)]
    if lane_ids != EXPECTED_LANE_ORDER:
        findings.add(Finding("LANE_INVENTORY_OR_ORDER_MISMATCH", "/lanes"))

    observed_roles: list[str] = []
    for index, lane in enumerate(lanes):
        if not isinstance(lane, Mapping):
            continue
        lane_id = lane.get("lane_id")
        expected = EXPECTED_LANES.get(str(lane_id))
        if expected is None:
            findings.add(Finding("UNKNOWN_LANE", f"/lanes/{index}/lane_id"))
            continue
        observed_roles.append(str(lane.get("source_role")))
        for field, expected_value in expected.items():
            actual = lane.get(field)
            if field in {"query_formats", "blocking_codes"}:
                if not isinstance(actual, list) or actual != sorted(set(actual)):
                    findings.add(
                        Finding(
                            "CANONICAL_LIST_REQUIRED",
                            f"/lanes/{index}/{field}",
                        )
                    )
                if actual != expected_value:
                    findings.add(
                        Finding(
                            "QUERY_FORMATS_MISMATCH" if field == "query_formats" else "BLOCKING_CODES_MISMATCH",
                            f"/lanes/{index}/{field}",
                        )
                    )
                continue
            if field == "identifier_roles":
                if not isinstance(actual, list) or actual != sorted(
                    actual,
                    key=lambda item: (item.get("field", ""), item.get("semantic_role", "")),
                ):
                    findings.add(
                        Finding("IDENTIFIER_ROLES_NOT_CANONICAL", f"/lanes/{index}/identifier_roles")
                    )
                if actual != expected_value:
                    findings.add(
                        Finding("IDENTIFIER_ROLE_MISMATCH", f"/lanes/{index}/identifier_roles")
                    )
                continue
            if actual != expected_value:
                code = {
                    "source_role": "SOURCE_ROLE_MISMATCH",
                    "interface_ref": "ENDPOINT_IDENTITY_MISMATCH",
                    "layer_id": "LAYER_ID_MISMATCH",
                    "source_crs": "CRS_DECLARATION_MISMATCH",
                    "max_record_count": "PAGINATION_LIMIT_MISMATCH",
                    "authentication_posture": "AUTHENTICATION_POSTURE_MISMATCH",
                    "identifier_state": "IDENTIFIER_STATE_MISMATCH",
                    "rights_state": "RIGHTS_STATE_INCOHERENT",
                    "sensitivity_state": "SENSITIVITY_STATE_INCOHERENT",
                    "snapshot_identity_state": "SNAPSHOT_IDENTITY_STATE_INCOHERENT",
                    "public_precision_state": "PUBLIC_PRECISION_STATE_INCOHERENT",
                    "precision_policy_ref": "PRECISION_POLICY_REF_MISMATCH",
                    "declared_disposition": "DECLARED_DISPOSITION_MISMATCH",
                }[field]
                findings.add(Finding(code, f"/lanes/{index}/{field}"))

        precision_state = lane.get("public_precision_state")
        precision_ref = lane.get("precision_policy_ref")
        if precision_state in {"APPROVED", "GENERALIZED"} and precision_ref is None:
            findings.add(Finding("PRECISION_POLICY_REQUIRED", f"/lanes/{index}/precision_policy_ref"))
        if lane.get("rights_state") == "PROHIBITED":
            findings.add(Finding("RIGHTS_PROHIBITED", f"/lanes/{index}/rights_state"))

    if len(observed_roles) != len(set(observed_roles)):
        findings.add(Finding("SOURCE_ROLE_COLLAPSE", "/lanes"))

    crosswalk = value.get("crosswalk")
    if isinstance(crosswalk, Mapping):
        if crosswalk.get("proximity_only_match_allowed") is not False:
            findings.add(
                Finding("PROXIMITY_ONLY_CROSSWALK_DENIED", "/crosswalk/proximity_only_match_allowed")
            )
        if crosswalk.get("temporal_overlap_required") is not True:
            findings.add(Finding("TEMPORAL_OVERLAP_REQUIRED", "/crosswalk/temporal_overlap_required"))
        if crosswalk.get("geometry_tolerance_meters") is not None:
            findings.add(
                Finding("GEOMETRY_TOLERANCE_UNREVIEWED", "/crosswalk/geometry_tolerance_meters")
            )
        if crosswalk.get("split_merge_modelled") is not True:
            findings.add(Finding("SPLIT_MERGE_MODEL_REQUIRED", "/crosswalk/split_merge_modelled"))
        if crosswalk.get("identifier_roles") != EXPECTED_CROSSWALK_ROLES:
            findings.add(Finding("CROSSWALK_IDENTIFIER_ROLE_MISMATCH", "/crosswalk/identifier_roles"))

    if value.get("limitations") != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATIONS_MISMATCH", "/limitations"))
    if value.get("effects") != EXPECTED_EFFECTS:
        findings.add(Finding("GOVERNANCE_EFFECTS_MUST_REMAIN_FALSE", "/effects"))
    return tuple(sorted(findings))


def expected_lane_dispositions(value: Mapping[str, Any]) -> dict[str, str]:
    lanes = value.get("lanes")
    if not isinstance(lanes, list):
        return {key: "DENY" for key in EXPECTED_LANE_ORDER}
    result: dict[str, str] = {}
    for lane in lanes:
        if not isinstance(lane, Mapping):
            continue
        lane_id = lane.get("lane_id")
        if isinstance(lane_id, str) and lane_id in EXPECTED_LANES:
            disposition = lane.get("declared_disposition")
            result[lane_id] = disposition if isinstance(disposition, str) else "DENY"
    for lane_id in EXPECTED_LANE_ORDER:
        result.setdefault(lane_id, "DENY")
    return result


def recompute_decision(value: Mapping[str, Any]) -> dict[str, Any]:
    findings = _core_semantic_findings(value)
    if findings:
        return {
            "outcome": "DENY",
            "recommendation": "DENY",
            "review_state": "HOLD",
            "lane_dispositions": expected_lane_dispositions(value),
            "reason_codes": [findings[0].code],
        }
    return {
        "outcome": "PASS",
        "recommendation": "READY_FOR_REVIEW",
        "review_state": "HOLD",
        "lane_dispositions": {
            lane_id: EXPECTED_LANES[lane_id]["declared_disposition"]
            for lane_id in EXPECTED_LANE_ORDER
        },
        "reason_codes": [
            "FIXTURE_PROFILE_COHERENT",
            "LIVE_SNAPSHOT_REMAINS_HELD",
        ],
    }


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set(_core_semantic_findings(value))
    try:
        expected_hash = canonical_spec_hash(value)
        expected_id = expected_assessment_id(value)
    except (TypeError, ValueError, OverflowError):
        findings.add(Finding("CANONICALIZATION_ERROR", "/"))
    else:
        if value.get("spec_hash") != expected_hash:
            findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if value.get("assessment_id") != expected_id:
            findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if value.get("decision") != recompute_decision(value):
        findings.add(Finding("DECISION_MISMATCH", "/decision"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("ERROR", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        identity_codes = {"ASSESSMENT_ID_MISMATCH", "CANONICALIZATION_ERROR", "SPEC_HASH_MISMATCH"}
        outcome = "ERROR" if any(item.code in identity_codes for item in semantic_findings) else "DENY"
        return Result(outcome, semantic_findings)
    return Result("PASS", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", findings)
    return validate_payload(value)


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer[1:].split("/")
    ]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(CASES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["decision"] = copy.deepcopy(
        case.get("decision_override", recompute_decision(document))
    )
    document = assign_identity(document)
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "assessment_id_override" in case:
        document["assessment_id"] = case["assessment_id_override"]
    return document


def validate_fixture_manifest() -> list[dict[str, Any]]:
    manifest = load_fixtures()
    results: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual_findings = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        results.append(
            {
                "case_id": case["case_id"],
                "expected_outcome": case["expected_outcome"],
                "actual_outcome": result.outcome,
                "expected_findings": case["expected_findings"],
                "actual_findings": actual_findings,
                "ok": result.outcome == case["expected_outcome"]
                and actual_findings == case["expected_findings"],
            }
        )
    return results


def run_cases() -> int:
    results = validate_fixture_manifest()
    for result in results:
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if all(result["ok"] for result in results) else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY_NO_NETWORK",
            "file": path.as_posix() if path else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": [
                "no_endpoint_or_payload_access",
                "no_credentials_or_source_admission",
                "no_canonical_road_or_crosswalk_decision",
                "no_lifecycle_release_publication_or_public_use",
            ],
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--cases", action="store_true")
    args = parser.parse_args(argv)
    if args.cases:
        if args.input is not None:
            parser.error("--cases cannot be combined with input")
        return run_cases()
    if args.input is None:
        parser.error("input is required unless --cases is used")
    result = validate_file(args.input)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
