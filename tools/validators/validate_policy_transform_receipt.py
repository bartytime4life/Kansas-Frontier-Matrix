#!/usr/bin/env python3
"""Validate fixture-only PolicyTransformReceiptCandidate records.

A green result proves deterministic fixture binding only. It does not execute or verify
transforms, inspect runtime artifact bytes, evaluate current policy, authenticate review,
authorize release, publish, or permit public use.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = ROOT / "schemas/contracts/v1/receipts/policy_transform_receipt.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/receipts/policy_transform_receipt"
SOURCE_ROOT = ROOT / "fixtures/contracts/v1/policy/policy_transform_plan_simulation/valid"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
SCOPE = "policy-transform-receipt-fixture-only"
MAX_BYTES = 1_048_576
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "JSON_INVALID", "JSON_DUPLICATE_KEY", "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE", "SOURCE_FIXTURE_NOT_FOUND", "SOURCE_FIXTURE_SYMLINK_DENIED",
    "SOURCE_FIXTURE_INVALID",
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(item.code in ERROR_CODES for item in self.findings)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise DuplicateKeyError(key)
        output[key] = value
    return output


def _reject_constant(value: str) -> None:
    raise NonFiniteNumberError(value)


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError(value)
    return parsed


def _read_regular_object(path: Path, *, source: bool = False) -> tuple[dict[str, Any] | None, list[Finding]]:
    prefix = "SOURCE_FIXTURE_" if source else ""
    try:
        if path.is_symlink():
            return None, [Finding(prefix + "SYMLINK_DENIED" if source else "INPUT_SYMLINK_DENIED", "/")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        try:
            mode = os.fstat(descriptor).st_mode
            if not stat.S_ISREG(mode):
                return None, [Finding(prefix + "NOT_FOUND" if source else "FILE_NOT_FOUND", "/")]
            with os.fdopen(descriptor, "rb") as stream:
                descriptor = -1
                raw = stream.read(MAX_BYTES + 1)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
        if len(raw) > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except FileNotFoundError:
        return None, [Finding(prefix + "NOT_FOUND" if source else "FILE_NOT_FOUND", "/")]
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding(prefix + "INVALID" if source else "FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in validator.iter_errors(candidate)]


def _snapshot_hash(artifact_ref: str, kind: str) -> str:
    return compute_spec_hash({"artifact_ref": artifact_ref, "fixture_kind": kind})


def _operation(index: int, name: str, algorithm_id: str, parameters: dict[str, Any]) -> dict[str, Any]:
    core = {"index": index, "operation": name, "algorithm_id": algorithm_id, "parameters": parameters}
    return {**core, "operation_spec_hash": compute_spec_hash(core)}


def derive_operations(plan: Mapping[str, Any]) -> list[dict[str, Any]]:
    declarations: list[tuple[str, str, dict[str, Any]]] = []
    distance = plan.get("generalize_distance_m")
    if isinstance(distance, int) and distance > 0:
        declarations.append(("GENERALIZE_GEOMETRY", "kfm.fixture.generalize-geometry-declaration.v1", {"meters": distance}))
    days = plan.get("date_fuzz_days")
    if isinstance(days, int) and days > 0:
        declarations.append(("FUZZ_DATE", "kfm.fixture.fuzz-date-declaration.v1", {"days": days}))
    if plan.get("geometry_action") == "SUPPRESS":
        declarations.append(("SUPPRESS_GEOMETRY", "kfm.fixture.suppress-geometry-declaration.v1", {}))
    if plan.get("record_action") == "SUPPRESS":
        declarations.append(("SUPPRESS_RECORD", "kfm.fixture.suppress-record-declaration.v1", {}))
    embargo = plan.get("embargo_until")
    if isinstance(embargo, str):
        declarations.append(("APPLY_EMBARGO", "kfm.fixture.apply-embargo-declaration.v1", {"until": embargo}))
    return [_operation(index, name, algorithm, parameters) for index, (name, algorithm, parameters) in enumerate(declarations)]


def compute_receipt_spec_hash(candidate: Mapping[str, Any]) -> str:
    return compute_spec_hash({key: value for key, value in candidate.items() if key not in {"receipt_id", "spec_hash"}})


def compute_receipt_id(candidate: Mapping[str, Any]) -> str:
    digest = compute_receipt_spec_hash(candidate)
    return "policy-transform-receipt:" + digest[7:31]


def _source_path(value: Any) -> Path | None:
    if not isinstance(value, str) or "\\" in value or value.startswith("/"):
        return None
    path = PurePosixPath(value)
    expected_prefix = PurePosixPath("fixtures/contracts/v1/policy/policy_transform_plan_simulation/valid")
    if str(path) != value or any(part in {".", ".."} for part in path.parts):
        return None
    if path.parent != expected_prefix or not path.name.startswith("valid_") or path.suffix != ".json":
        return None
    return ROOT.joinpath(*path.parts)


def _source_binding_findings(candidate: Mapping[str, Any]) -> tuple[list[Finding], dict[str, Any] | None]:
    source_meta = candidate.get("source_simulation")
    if not isinstance(source_meta, dict):
        return [], None
    path = _source_path(source_meta.get("fixture_ref"))
    if path is None:
        return [Finding("SOURCE_FIXTURE_PATH_INVALID", "/source_simulation/fixture_ref")], None
    source, read_findings = _read_regular_object(path, source=True)
    if source is None:
        return read_findings, None
    findings: list[Finding] = []
    assessment = source.get("assessment")
    if not isinstance(assessment, dict) or assessment.get("outcome") != "SATISFIES":
        findings.append(Finding("SOURCE_SIMULATION_NOT_SATISFYING", "/source_simulation/assessment_outcome"))
    plan = source.get("plan")
    reduction = source.get("source_reduction")
    if not isinstance(plan, dict) or not isinstance(reduction, dict):
        findings.append(Finding("SOURCE_FIXTURE_INVALID", "/source_simulation"))
        return findings, source
    expected = {
        "fixture_ref": source_meta.get("fixture_ref"),
        "simulation_id": source.get("simulation_id"),
        "spec_hash": source.get("spec_hash"),
        "assessment_outcome": "SATISFIES",
        "lifecycle_phase": source.get("lifecycle_phase"),
        "plan_spec_hash": compute_spec_hash(plan),
        "source_reduction_id": reduction.get("reduction_id"),
        "source_reduction_spec_hash": reduction.get("spec_hash"),
    }
    if source_meta != expected:
        findings.append(Finding("SOURCE_SIMULATION_BINDING_MISMATCH", "/source_simulation"))
    preconditions = plan.get("preconditions")
    if not isinstance(preconditions, dict) or any(preconditions.get(field) is not True for field in (
        "input_spec_hash_verified", "output_spec_hash_required", "policy_recheck_required",
        "review_required", "rollback_target_required", "transform_receipt_required",
    )):
        findings.append(Finding("SOURCE_PRECONDITION_MISSING", "/source_simulation"))
    return findings, source


def _semantic_findings(candidate: Mapping[str, Any], source: Mapping[str, Any] | None) -> list[Finding]:
    if source is None:
        return []
    findings: list[Finding] = []
    plan = source.get("plan")
    if not isinstance(plan, dict):
        return [Finding("SOURCE_FIXTURE_INVALID", "/source_simulation")]
    input_snapshot = candidate.get("input")
    output_snapshot = candidate.get("output")
    if isinstance(input_snapshot, dict):
        expected_input = {"artifact_ref": plan.get("input_artifact_ref"), "snapshot_hash": _snapshot_hash(str(plan.get("input_artifact_ref")), "declared-input")}
        if input_snapshot != expected_input:
            findings.append(Finding("INPUT_SNAPSHOT_MISMATCH", "/input"))
    if isinstance(output_snapshot, dict):
        expected_output = {"artifact_ref": plan.get("planned_output_ref"), "snapshot_hash": _snapshot_hash(str(plan.get("planned_output_ref")), "declared-output")}
        if output_snapshot != expected_output:
            findings.append(Finding("OUTPUT_SNAPSHOT_MISMATCH", "/output"))
    if isinstance(input_snapshot, dict) and isinstance(output_snapshot, dict) and input_snapshot.get("snapshot_hash") == output_snapshot.get("snapshot_hash"):
        findings.append(Finding("OUTPUT_NO_EFFECT", "/output/snapshot_hash"))
    operations = candidate.get("applied_operations")
    expected_operations = derive_operations(plan)
    if isinstance(operations, list):
        stripped_actual = [{key: value for key, value in item.items() if key != "operation_spec_hash"} for item in operations if isinstance(item, dict)]
        stripped_expected = [{key: value for key, value in item.items() if key != "operation_spec_hash"} for item in expected_operations]
        if stripped_actual != stripped_expected:
            findings.append(Finding("OPERATION_SEQUENCE_MISMATCH", "/applied_operations"))
        if any(not isinstance(item, dict) or item.get("operation_spec_hash") != compute_spec_hash({key: value for key, value in item.items() if key != "operation_spec_hash"}) for item in operations):
            findings.append(Finding("OPERATION_HASH_MISMATCH", "/applied_operations"))
    expected_binding = {
        "obligation_ids": plan.get("covered_obligation_ids"),
        "source_policy_refs": plan.get("source_policy_refs"),
        "reason_codes": plan.get("reason_codes"),
    }
    if candidate.get("obligation_binding") != expected_binding:
        findings.append(Finding("OBLIGATION_BINDING_MISMATCH", "/obligation_binding"))
    if candidate.get("rollback_target") != candidate.get("input"):
        findings.append(Finding("ROLLBACK_TARGET_MISMATCH", "/rollback_target"))
    declared_hash = candidate.get("spec_hash")
    actual_hash = compute_receipt_spec_hash(candidate)
    if isinstance(declared_hash, str) and declared_hash != actual_hash:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("receipt_id") != compute_receipt_id(candidate):
        findings.append(Finding("RECEIPT_ID_MISMATCH", "/receipt_id"))
    return findings


def validate_record(path: Path) -> ValidationResult:
    candidate, read_findings = _read_regular_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(read_findings))))
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult(tuple(sorted(set(schema_findings))))
    source_findings, source = _source_binding_findings(candidate)
    semantic = _semantic_findings(candidate, source)
    return ValidationResult(tuple(sorted(set(source_findings + semantic))))


def _serialize(path: Path, result: ValidationResult) -> str:
    outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
    return json.dumps({"file": path.as_posix(), "findings": [{"code": item.code, "field": item.field} for item in result.findings], "outcome": outcome, "scope": SCOPE}, sort_keys=True, separators=(",", ":"))


def validate_fixture_suite() -> tuple[bool, list[str]]:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return False, []
    lines: list[str] = []
    ok = True
    for case in manifest.get("cases", []):
        path = FIXTURES / case["record"]
        result = validate_record(path)
        outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
        codes = sorted({item.code for item in result.findings})
        match = outcome == case["expected_outcome"] and codes == case["expected_findings"]
        lines.append(json.dumps({"case_id": case["case_id"], "expected_findings": case["expected_findings"], "expected_outcome": case["expected_outcome"], "findings": codes, "outcome": outcome, "suite_match": match}, sort_keys=True, separators=(",", ":")))
        ok = ok and match
    return ok, lines


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only policy transform receipt candidates.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        ok, lines = validate_fixture_suite()
        for line in lines:
            print(line)
        return 0 if ok else 1
    if not args.files:
        parser.error("provide files or --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_record(path)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
