#!/usr/bin/env python3
"""Validate fixture-only field-capture evidence-handoff assessments.

The validator checks bounded metadata, acquisition semantics, geometry posture,
rights and sensitivity closure, evidence/review references, deterministic
identity, and explicit non-authority. It performs no capture, coordinate
processing, reference resolution, evidence creation, policy evaluation,
review, lifecycle transition, release, or publication operation.
"""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for import_root in (REPO_ROOT, HASHING_SRC):
    if str(import_root) not in sys.path:
        sys.path.insert(0, str(import_root))

from hashing import compute_spec_hash  # noqa: E402

SCHEMA = REPO_ROOT / "schemas/contracts/v1/evidence/field_capture_evidence_handoff.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/evidence/field_capture_evidence_handoff/cases.json"
PROFILE = "kfm.field-capture-evidence-handoff.fixture.v1"
PREFIX = "kfm:field-capture-handoff:"
MAX_BYTES = 2 * 1024 * 1024
MAX_FINDINGS = 100
LIMITATIONS = (
    "CAPTURE_REMAINS_CANDIDATE",
    "FIXTURE_ONLY",
    "NO_EVIDENCE_CREATION",
    "NO_POLICY_OR_REVIEW_AUTHORITY",
    "NO_RAW_COORDINATES",
    "NO_RELEASE_OR_PUBLICATION_AUTHORITY",
)
NON_EFFECTS = (
    "no_capture_or_coordinate_processing",
    "no_source_or_network_access",
    "no_reference_resolution_or_evidence_creation",
    "no_policy_review_or_lifecycle_decision",
    "no_release_publication_or_public_use_authority",
)
METHOD_BY_KIND = {
    "DRONE_CAPTURE": "UAS_SENSOR",
    "FIELD_OBSERVATION": "HUMAN_RECORDED",
    "GNSS_POINT": "GNSS_RECEIVER",
    "LIDAR": "LIDAR_SENSOR",
    "MANUAL_POINT": "MANUAL_MAP_PLACEMENT",
    "PHOTOGRAMMETRY": "CAMERA_RIG",
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
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(item).replace("~", "~0").replace("/", "~1") for item in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("FIELD_CAPTURE_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("FIELD_CAPTURE_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("FIELD_CAPTURE_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("FIELD_CAPTURE_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("FIELD_CAPTURE_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("FIELD_CAPTURE_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("FIELD_CAPTURE_JSON_ROOT_INVALID", "/"),)
    return value, ()


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    errors = sorted(
        islice(_schema_validator().iter_errors(value), MAX_FINDINGS),
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )
    return tuple(
        sorted(
            {
                Finding("FIELD_CAPTURE_SCHEMA_INVALID", _pointer(error.absolute_path))
                for error in errors
            }
        )
    )


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = copy.deepcopy(dict(value))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.removeprefix("sha256:")[:24]


def _spatially_ready(value: Mapping[str, Any]) -> bool:
    capture = value["capture"]
    processing = value["processing"]
    posture = capture["geometry_posture"]
    if posture == "WITHHELD":
        return capture["geometry_ref"] is None and processing["public_transform_receipt_ref"] is None
    common = bool(
        capture["geometry_ref"] is not None
        and capture["crs_ref"] is not None
        and capture["accuracy_class"] != "UNKNOWN"
        and processing["georeference_validation_ref"] is not None
    )
    if posture == "EXACT_RESTRICTED":
        return bool(
            common
            and capture["sensitivity"] == "SENSITIVE"
            and processing["public_transform_receipt_ref"] is None
        )
    return bool(
        common
        and capture["sensitivity"] == "PUBLIC_SAFE"
        and processing["public_transform_receipt_ref"] is not None
    )


def expected_disposition(value: Mapping[str, Any]) -> tuple[str, dict[str, Any]]:
    capture = value["capture"]
    evidence = value["evidence"]
    if capture["rights_status"] == "DENIED" or evidence["review_state"] == "DENIED":
        return "DENIED", {"outcome": "DENY", "reason_codes": ["HANDOFF_DENIED"]}
    authorization_ready = (
        capture["capture_kind"] != "DRONE_CAPTURE"
        or capture["capture_authorization_ref"] is not None
    )
    ready = bool(
        capture["rights_status"] == "VERIFIED"
        and capture["sensitivity"] != "UNKNOWN"
        and evidence["evidence_bundle_ref"] is not None
        and evidence["review_state"] == "APPROVED"
        and authorization_ready
        and _spatially_ready(value)
    )
    if ready:
        return "READY", {
            "outcome": "PASS",
            "reason_codes": ["READY_FOR_EVIDENCE_HANDOFF"],
        }
    return "HELD", {"outcome": "ABSTAIN", "reason_codes": ["HANDOFF_HELD"]}


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    capture = value["capture"]
    processing = value["processing"]
    evidence = value["evidence"]

    if capture["acquisition_method"] != METHOD_BY_KIND[capture["capture_kind"]]:
        findings.add(Finding("FIELD_CAPTURE_ACQUISITION_METHOD_MISMATCH", "/capture/acquisition_method"))

    acquired = _time(capture["acquired_at"])
    assessed = _time(value["assessed_at"])
    if acquired is None or assessed is None or assessed < acquired:
        findings.add(Finding("FIELD_CAPTURE_TIME_ORDER_INVALID", "/assessed_at"))

    if capture["capture_kind"] == "DRONE_CAPTURE":
        if capture["capture_authorization_ref"] is None:
            findings.add(Finding("FIELD_CAPTURE_AUTHORIZATION_REF_REQUIRED", "/capture/capture_authorization_ref"))
    elif capture["capture_authorization_ref"] is not None:
        findings.add(Finding("FIELD_CAPTURE_AUTHORIZATION_REF_UNEXPECTED", "/capture/capture_authorization_ref"))

    posture = capture["geometry_posture"]
    if posture == "WITHHELD":
        if capture["geometry_ref"] is not None:
            findings.add(Finding("FIELD_CAPTURE_WITHHELD_GEOMETRY_REF_FORBIDDEN", "/capture/geometry_ref"))
        if processing["public_transform_receipt_ref"] is not None:
            findings.add(Finding("FIELD_CAPTURE_WITHHELD_TRANSFORM_REF_FORBIDDEN", "/processing/public_transform_receipt_ref"))
    else:
        if capture["geometry_ref"] is None:
            findings.add(Finding("FIELD_CAPTURE_GEOMETRY_REF_REQUIRED", "/capture/geometry_ref"))
        if capture["crs_ref"] is None:
            findings.add(Finding("FIELD_CAPTURE_CRS_REF_REQUIRED", "/capture/crs_ref"))
        if capture["accuracy_class"] == "UNKNOWN":
            findings.add(Finding("FIELD_CAPTURE_ACCURACY_REQUIRED", "/capture/accuracy_class"))
        if processing["georeference_validation_ref"] is None:
            findings.add(Finding("FIELD_CAPTURE_GEOREFERENCE_VALIDATION_REQUIRED", "/processing/georeference_validation_ref"))
        if posture == "EXACT_RESTRICTED":
            if capture["sensitivity"] != "SENSITIVE":
                findings.add(Finding("FIELD_CAPTURE_EXACT_GEOMETRY_MUST_BE_SENSITIVE", "/capture/sensitivity"))
            if processing["public_transform_receipt_ref"] is not None:
                findings.add(Finding("FIELD_CAPTURE_EXACT_PUBLIC_TRANSFORM_FORBIDDEN", "/processing/public_transform_receipt_ref"))
        else:
            if capture["sensitivity"] != "PUBLIC_SAFE":
                findings.add(Finding("FIELD_CAPTURE_GENERALIZED_PUBLIC_MUST_BE_SAFE", "/capture/sensitivity"))
            if processing["public_transform_receipt_ref"] is None:
                findings.add(Finding("FIELD_CAPTURE_PUBLIC_TRANSFORM_REQUIRED", "/processing/public_transform_receipt_ref"))

    expected_state, expected_decision = expected_disposition(value)
    if evidence["handoff_state"] != expected_state:
        findings.add(Finding("FIELD_CAPTURE_HANDOFF_STATE_MISMATCH", "/evidence/handoff_state"))
    if value["decision"] != expected_decision:
        findings.add(Finding("FIELD_CAPTURE_DECISION_MISMATCH", "/decision"))
    if value["limitations"] != list(LIMITATIONS):
        findings.add(Finding("FIELD_CAPTURE_LIMITATIONS_MISMATCH", "/limitations"))

    expected_hash, expected_id = canonical_identity(value)
    if value["spec_hash"] != expected_hash:
        findings.add(Finding("FIELD_CAPTURE_SPEC_HASH_MISMATCH", "/spec_hash"))
    if value["assessment_id"] != expected_id:
        findings.add(Finding("FIELD_CAPTURE_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    return tuple(sorted(findings))


def validate_payload(value: object) -> Result:
    if not isinstance(value, Mapping):
        return Result("DENY", (Finding("FIELD_CAPTURE_SCHEMA_INVALID", "/"),))
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    findings = _semantic_findings(value)
    return Result("DENY" if findings else value["decision"]["outcome"], findings)


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest must be an object")
    return value


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [
        item.replace("~1", "/").replace("~0", "~")
        for item in pointer.removeprefix("/").split("/")
    ]
    target: Any = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    value = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _set_pointer(value, mutation["path"], mutation["value"])
    handoff_state, decision = expected_disposition(value)
    value["evidence"]["handoff_state"] = handoff_state
    value["decision"] = decision
    value["spec_hash"], value["assessment_id"] = canonical_identity(value)
    for mutation in case.get("assertion_mutations", []):
        _set_pointer(value, mutation["path"], mutation["value"])
    return value


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if findings:
        return Result("ERROR", findings)
    return validate_payload(value)


def serialize(path: Path, result: Result) -> str:
    payload = {
        "authority": "NONE",
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ],
        "input": path.name,
        "non_effects": list(NON_EFFECTS),
        "outcome": result.outcome,
        "profile": PROFILE,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def _run_fixtures() -> int:
    manifest = load_fixtures()
    rows: list[dict[str, Any]] = []
    suite_match = True
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        match = result.outcome == case["expected_outcome"] and actual == case["expected_findings"]
        suite_match = suite_match and match
        rows.append({"case_id": case["case_id"], "match": match, "outcome": result.outcome})
    print(
        json.dumps(
            {
                "authority": "NONE",
                "case_count": len(rows),
                "cases": rows,
                "non_effects": list(NON_EFFECTS),
                "profile": PROFILE,
                "suite_match": suite_match,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if suite_match else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            parser.error("path cannot be combined with --fixtures")
        return _run_fixtures()
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(serialize(args.path, result))
    return 0 if result.outcome in {"PASS", "ABSTAIN"} else 2 if result.outcome == "ERROR" else 1


if __name__ == "__main__":
    raise SystemExit(main())
