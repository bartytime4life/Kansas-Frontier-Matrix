#!/usr/bin/env python3
"""Validate fixture-only historic-map scan-lineage assessment candidates.

A PASS proves bounded synthetic declaration consistency only. It does not
activate a source, decide rights, georeference a scan, admit evidence, release,
or publish.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/evidence/historic_map_scan_lineage_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/historic_map_scan_lineage_assessment/cases.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:historic-map-scan-lineage:"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    assessment_state: str | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
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
            return None, (Finding("HISTORIC_MAP_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("HISTORIC_MAP_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("HISTORIC_MAP_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("HISTORIC_MAP_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("HISTORIC_MAP_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("HISTORIC_MAP_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("HISTORIC_MAP_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("HISTORIC_MAP_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"assessment_id", "spec_hash"}}
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def expected_summary(value: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "rights_state": value["original_map"]["rights_status"],
        "georeference_state": value["georeference"]["status"],
        "permitted_use_count": len(value["derivative_use"]["permitted_uses"]),
        "assessment_state": "REVIEW_REQUIRED",
        "source_activated": False,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("HISTORIC_MAP_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("HISTORIC_MAP_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("HISTORIC_MAP_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _semantic_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    original = value["original_map"]
    scan = value["scan"]
    georeference = value["georeference"]
    use = value["derivative_use"]
    evidence_refs = value["evidence"]["evidence_refs"]

    if original["original_map_ref"] == scan["scan_artifact_ref"]:
        findings.add(Finding("HISTORIC_MAP_ORIGINAL_SCAN_REF_COLLISION", "/scan/scan_artifact_ref"))
    derivative_ref = georeference["derivative_artifact_ref"]
    if derivative_ref is not None and derivative_ref in {original["original_map_ref"], scan["scan_artifact_ref"]}:
        findings.add(Finding("HISTORIC_MAP_DERIVATIVE_REF_COLLISION", "/georeference/derivative_artifact_ref"))

    if original["citation_ref"] is None:
        findings.add(Finding("HISTORIC_MAP_ORIGINAL_CITATION_REQUIRED", "/original_map/citation_ref"))
    if original["rights_review_ref"] is None:
        findings.add(Finding("HISTORIC_MAP_RIGHTS_REVIEW_REQUIRED", "/original_map/rights_review_ref"))
    if scan["scan_receipt_ref"] is None:
        findings.add(Finding("HISTORIC_MAP_SCAN_RECEIPT_REQUIRED", "/scan/scan_receipt_ref"))

    if evidence_refs != sorted(evidence_refs):
        findings.add(Finding("HISTORIC_MAP_EVIDENCE_REFS_NOT_CANONICAL", "/evidence/evidence_refs"))
    if use["permitted_uses"] != sorted(use["permitted_uses"]):
        findings.add(Finding("HISTORIC_MAP_PERMITTED_USES_NOT_CANONICAL", "/derivative_use/permitted_uses"))
    if use["derivative_use_limits"] != sorted(use["derivative_use_limits"]):
        findings.add(Finding("HISTORIC_MAP_USE_LIMITS_NOT_CANONICAL", "/derivative_use/derivative_use_limits"))

    if georeference["status"] == "ASSESSABLE":
        required = {
            "control_point_set_ref": "HISTORIC_MAP_CONTROL_POINTS_REQUIRED",
            "transform_quality_ref": "HISTORIC_MAP_TRANSFORM_QUALITY_REQUIRED",
            "rms_error_meters": "HISTORIC_MAP_RMS_ERROR_REQUIRED",
            "reality_boundary_note_ref": "HISTORIC_MAP_REALITY_BOUNDARY_REQUIRED",
            "derivative_artifact_ref": "HISTORIC_MAP_DERIVATIVE_REF_REQUIRED",
        }
        if georeference["method"] in {"NONE", "UNKNOWN"}:
            findings.add(Finding("HISTORIC_MAP_GEOREFERENCE_METHOD_REQUIRED", "/georeference/method"))
        if georeference["gcp_count"] < 3:
            findings.add(Finding("HISTORIC_MAP_GCP_COUNT_INSUFFICIENT", "/georeference/gcp_count"))
        for field, code in required.items():
            if georeference[field] is None:
                findings.add(Finding(code, f"/georeference/{field}"))
    elif georeference["status"] == "NOT_ATTEMPTED":
        if georeference["method"] != "NONE":
            findings.add(Finding("HISTORIC_MAP_NOT_ATTEMPTED_METHOD_INVALID", "/georeference/method"))
        if georeference["gcp_count"] != 0:
            findings.add(Finding("HISTORIC_MAP_NOT_ATTEMPTED_GCP_COUNT_INVALID", "/georeference/gcp_count"))
        nullable_fields = (
            "control_point_set_ref",
            "transform_quality_ref",
            "rms_error_meters",
            "reality_boundary_note_ref",
            "derivative_artifact_ref",
        )
        for field in nullable_fields:
            if georeference[field] is not None:
                findings.add(Finding("HISTORIC_MAP_NOT_ATTEMPTED_DETAIL_PRESENT", f"/georeference/{field}"))

    context_requested = use["requested_use"] == "CONTEXT_OVERLAY"
    context_permitted = "CONTEXT_OVERLAY" in use["permitted_uses"]
    if (context_requested or context_permitted) and georeference["status"] != "ASSESSABLE":
        findings.add(Finding("HISTORIC_MAP_CONTEXT_REQUIRES_ASSESSABLE_GEOREFERENCE", "/georeference/status"))
    if (context_requested or context_permitted) and original["rights_status"] != "CLEARED":
        findings.add(Finding("HISTORIC_MAP_CONTEXT_REQUIRES_CLEARED_RIGHTS", "/original_map/rights_status"))
    if use["requested_use"] == "POSITIONAL_EVIDENCE":
        findings.add(Finding("HISTORIC_MAP_POSITIONAL_USE_DENIED", "/derivative_use/requested_use"))
    elif use["requested_use"] not in use["permitted_uses"]:
        findings.add(Finding("HISTORIC_MAP_REQUESTED_USE_NOT_PERMITTED", "/derivative_use/requested_use"))
    if "POSITIONAL_EVIDENCE" in use["permitted_uses"]:
        findings.add(Finding("HISTORIC_MAP_POSITIONAL_PERMISSION_DENIED", "/derivative_use/permitted_uses"))

    if value["summary"] != expected_summary(value):
        findings.add(Finding("HISTORIC_MAP_SUMMARY_MISMATCH", "/summary"))
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)
    findings = _semantic_findings(value)
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("HISTORIC_MAP_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("HISTORIC_MAP_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("HISTORIC_MAP_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    return Result("PASS", "REVIEW_REQUIRED", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", None, findings)
    return validate_payload(value)


def _set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.removeprefix("/").split("/")]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    last = parts[-1]
    if isinstance(cursor, list):
        cursor[int(last)] = replacement
    else:
        cursor[last] = replacement


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if not case.get("preserve_summary", False):
        document["summary"] = expected_summary(document)
    document["spec_hash"], document["assessment_id"] = canonical_identity(document)
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "assessment_id_override" in case:
        document["assessment_id"] = case["assessment_id_override"]
    return document


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    if not isinstance(value, dict):
        raise ValueError("fixture root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": finding.code, "path": finding.path} for finding in result.findings]
        if (
            result.outcome != case["expected_outcome"]
            or result.assessment_state != case["expected_assessment_state"]
            or actual != case["expected_findings"]
        ):
            failures.append({
                "case_id": case["case_id"],
                "expected_outcome": case["expected_outcome"],
                "actual_outcome": result.outcome,
                "expected_assessment_state": case["expected_assessment_state"],
                "actual_assessment_state": result.assessment_state,
                "expected_findings": case["expected_findings"],
                "actual_findings": actual,
            })
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps({
        "authority": {
            "activates_source": False,
            "decides_rights": False,
            "executes_georeference": False,
            "admits_evidence": False,
            "authorizes_release": False,
            "publishes": False,
        },
        "execution_mode": "FIXTURE_ONLY",
        "file": path.as_posix(),
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "outcome": result.outcome,
        "assessment_state": result.assessment_state,
    }, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.input is None:
        raise SystemExit("input is required unless --fixtures is used")
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
