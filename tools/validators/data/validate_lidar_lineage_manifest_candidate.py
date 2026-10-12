#!/usr/bin/env python3
"""Validate fixture-only LiDAR lineage manifest candidates.

A PASS proves bounded synthetic declaration consistency only. It does not open
LiDAR bytes, activate a source, authorize a transform, release, or publish.
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

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/data/lidar_lineage_manifest_candidate.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/data/lidar_lineage_manifest_candidate/cases.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:lidar-lineage-manifest:"
ROLE_BY_KIND = {
    "POINT_CLOUD_COPC": "DERIVED_POINT_CLOUD",
    "TERRAIN_COG": "DERIVED_TERRAIN",
    "TERRAIN_PMTILES": "DERIVED_TERRAIN",
    "SCENE_DERIVATIVE": "DERIVED_SCENE",
}


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
    manifest_state: str | None
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
            return None, (Finding("LIDAR_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("LIDAR_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("LIDAR_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("LIDAR_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("LIDAR_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("LIDAR_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("LIDAR_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("LIDAR_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"manifest_id", "spec_hash"}}
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _time(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")


def expected_summary(value: Mapping[str, Any]) -> dict[str, Any]:
    artifacts = value["derived_artifacts"]
    source_vertical = value["source_asset"]["vertical_crs"]
    transform_required = any(item["vertical_crs"] != source_vertical for item in artifacts)
    return {
        "derived_artifact_count": len(artifacts),
        "scene_artifact_count": sum(1 for item in artifacts if item["artifact_kind"] == "SCENE_DERIVATIVE"),
        "vertical_transform_required": transform_required,
        "manifest_state": "REVIEW_REQUIRED",
        "source_activated": False,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("LIDAR_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [Finding("LIDAR_SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("LIDAR_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _semantic_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    source = value["source_asset"]
    processing = value["processing"]
    artifacts = value["derived_artifacts"]
    evidence = value["evidence"]

    if _time(source["acquired_from"]) > _time(source["acquired_to"]):
        findings.add(Finding("LIDAR_ACQUISITION_WINDOW_REVERSED", "/source_asset/acquired_from"))

    available = source["available_class_codes"]
    selected = processing["selected_class_codes"]
    if available != sorted(set(available)):
        findings.add(Finding("LIDAR_AVAILABLE_CLASSES_NOT_CANONICAL", "/source_asset/available_class_codes"))
    if selected != sorted(set(selected)):
        findings.add(Finding("LIDAR_SELECTED_CLASSES_NOT_CANONICAL", "/processing/selected_class_codes"))
    available_set = set(available)
    for index, code in enumerate(selected):
        if code not in available_set:
            findings.add(Finding("LIDAR_SELECTED_CLASS_UNAVAILABLE", f"/processing/selected_class_codes/{index}"))

    artifact_ids = [item["artifact_id"] for item in artifacts]
    if artifact_ids != sorted(artifact_ids):
        findings.add(Finding("LIDAR_ARTIFACT_ORDER_INVALID", "/derived_artifacts"))
    if len(artifact_ids) != len(set(artifact_ids)):
        findings.add(Finding("LIDAR_ARTIFACT_ID_DUPLICATE", "/derived_artifacts"))

    for index, item in enumerate(artifacts):
        expected_role = ROLE_BY_KIND[item["artifact_kind"]]
        if item["representation_role"] != expected_role:
            findings.add(Finding("LIDAR_ARTIFACT_ROLE_MISMATCH", f"/derived_artifacts/{index}/representation_role"))

    transform = processing["vertical_transform"]
    source_vertical = source["vertical_crs"]
    target_verticals = {item["vertical_crs"] for item in artifacts}
    transform_required = any(target != source_vertical for target in target_verticals)
    if transform_required and transform["applied"] is not True:
        findings.add(Finding("LIDAR_VERTICAL_TRANSFORM_REQUIRED", "/processing/vertical_transform/applied"))
    if transform["source_vertical_crs"] != source_vertical:
        findings.add(Finding("LIDAR_VERTICAL_TRANSFORM_SOURCE_MISMATCH", "/processing/vertical_transform/source_vertical_crs"))
    if transform["applied"]:
        if transform["target_vertical_crs"] == source_vertical:
            findings.add(Finding("LIDAR_VERTICAL_TRANSFORM_TARGET_UNCHANGED", "/processing/vertical_transform/target_vertical_crs"))
        if transform["operation_ref"] is None:
            findings.add(Finding("LIDAR_VERTICAL_TRANSFORM_OPERATION_REQUIRED", "/processing/vertical_transform/operation_ref"))
        if transform["parameters_digest"] is None:
            findings.add(Finding("LIDAR_VERTICAL_TRANSFORM_PARAMETERS_REQUIRED", "/processing/vertical_transform/parameters_digest"))
        for index, item in enumerate(artifacts):
            if item["vertical_crs"] != transform["target_vertical_crs"]:
                findings.add(Finding("LIDAR_ARTIFACT_VERTICAL_TARGET_MISMATCH", f"/derived_artifacts/{index}/vertical_crs"))
    else:
        if transform["target_vertical_crs"] != source_vertical:
            findings.add(Finding("LIDAR_UNAPPLIED_VERTICAL_TARGET_MISMATCH", "/processing/vertical_transform/target_vertical_crs"))
        if transform["operation_ref"] is not None or transform["parameters_digest"] is not None:
            findings.add(Finding("LIDAR_UNAPPLIED_VERTICAL_TRANSFORM_HAS_PARAMETERS", "/processing/vertical_transform"))

    if any(item["artifact_kind"] == "SCENE_DERIVATIVE" for item in artifacts) and evidence["reality_boundary_note_ref"] is None:
        findings.add(Finding("LIDAR_SCENE_REALITY_BOUNDARY_REQUIRED", "/evidence/reality_boundary_note_ref"))

    if value["summary"] != expected_summary(value):
        findings.add(Finding("LIDAR_SUMMARY_MISMATCH", "/summary"))
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)
    findings = _semantic_findings(value)
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("LIDAR_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("LIDAR_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["manifest_id"] != expected_id:
            findings.add(Finding("LIDAR_MANIFEST_ID_MISMATCH", "/manifest_id"))
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
    document["spec_hash"], document["manifest_id"] = canonical_identity(document)
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "manifest_id_override" in case:
        document["manifest_id"] = case["manifest_id_override"]
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
        if result.outcome != case["expected_outcome"] or result.manifest_state != case["expected_manifest_state"] or actual != case["expected_findings"]:
            failures.append({
                "case_id": case["case_id"],
                "expected_outcome": case["expected_outcome"], "actual_outcome": result.outcome,
                "expected_manifest_state": case["expected_manifest_state"], "actual_manifest_state": result.manifest_state,
                "expected_findings": case["expected_findings"], "actual_findings": actual,
            })
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps({
        "authority": {
            "activates_source": False, "opens_lidar_bytes": False,
            "authorizes_transform": False, "evaluates_sensitivity_policy": False,
            "authorizes_release": False, "publishes": False,
        },
        "execution_mode": "FIXTURE_ONLY", "file": path.as_posix(),
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "outcome": result.outcome, "manifest_state": result.manifest_state,
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
