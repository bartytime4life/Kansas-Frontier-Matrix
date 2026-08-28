"""Validate fixture-only GateAttemptCoverageAssessment candidates."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import JsonInputError, load_json_file  # noqa: E402

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/validation/gate_attempt_coverage_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/validation/gate_attempt_coverage_assessment/cases.json"
BUILDER_PATH = REPO_ROOT / "tools/generators/gate_attempt_coverage_assessment/build_gate_attempt_coverage_assessment.py"
SCOPE = "validation.gate_attempt_coverage_assessment"
ALL_CLASSES = ("ADMITTED", "ERROR", "REFUSED", "UNOBSERVED")
CLASS_PATHS = {
    "ADMITTED": "admitted",
    "ERROR": "error",
    "REFUSED": "refused",
    "UNOBSERVED": "unobserved",
}
EXPECTED_SIGNATURE_DOMAINS = {
    "ADMITTED": "kfm.gate.attempt.admitted.v1",
    "ERROR": "kfm.gate.attempt.error.v1",
    "REFUSED": "kfm.gate.attempt.refused.v1",
    "UNOBSERVED": "kfm.gate.attempt.unobserved.v1",
}
EXPECTED_CLASS_SEMANTICS = {
    "ADMITTED": {"guarded_action_occurrence": "CONFIRMED", "same_gate_feedback_allowed": True},
    "ERROR": {"guarded_action_occurrence": "NOT_CONFIRMED", "same_gate_feedback_allowed": False},
    "REFUSED": {"guarded_action_occurrence": "DID_NOT_OCCUR", "same_gate_feedback_allowed": False},
    "UNOBSERVED": {"guarded_action_occurrence": "UNKNOWN", "same_gate_feedback_allowed": False},
}


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_BUILDER = _load_module("kfm_gate_attempt_coverage_assessment_builder", BUILDER_PATH)
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    assessment_id: str | None = None


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _schema_findings(document: object) -> list[Finding]:
    errors = sorted(_VALIDATOR.iter_errors(document), key=lambda error: tuple(str(p) for p in error.absolute_path))
    return [Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path))) for error in errors]


def validate_document(document: object) -> ValidationResult:
    schema_findings = _schema_findings(document)
    if schema_findings or not isinstance(document, dict):
        return ValidationResult("DENY", tuple(sorted(set(schema_findings))))

    findings: set[Finding] = set()
    counts = document["counts"]
    classes = document["attempt_classes"]

    declared_terminal_sum = counts["admitted"] + counts["error"] + counts["refused"] + counts["unobserved"]
    if counts["attempted"] != declared_terminal_sum:
        findings.add(Finding("ATTEMPT_COUNT_MISMATCH", "$.counts.attempted"))

    attempt_refs: list[str] = []
    record_refs: list[str] = []
    for class_name in ALL_CLASSES:
        path_name = CLASS_PATHS[class_name]
        rows = classes[path_name]
        if counts[path_name] != len(rows):
            findings.add(Finding("CLASS_COUNT_MISMATCH", f"$.attempt_classes.{path_name}"))
        if rows != sorted(rows, key=lambda row: row["attempt_ref"]):
            findings.add(Finding("CLASS_ROWS_NOT_CANONICAL", f"$.attempt_classes.{path_name}"))
        for index, row in enumerate(rows):
            attempt_refs.append(row["attempt_ref"])
            if "record_ref" in row:
                record_refs.append(row["record_ref"])
            if row["signature_domain"] != EXPECTED_SIGNATURE_DOMAINS[class_name]:
                findings.add(Finding("SIGNATURE_DOMAIN_MISMATCH", f"$.attempt_classes.{path_name}[{index}].signature_domain"))

    if len(attempt_refs) != len(set(attempt_refs)):
        findings.add(Finding("ATTEMPT_REFS_NOT_UNIQUE", "$.attempt_classes"))
    if len(record_refs) != len(set(record_refs)):
        findings.add(Finding("RECORD_REFS_NOT_UNIQUE", "$.attempt_classes"))
    if set(attempt_refs).intersection(record_refs):
        findings.add(Finding("REFERENCE_ROLE_COLLISION", "$.attempt_classes"))

    window = document["window"]
    if window["opens_at"] >= window["closes_at"]:
        findings.add(Finding("WINDOW_NOT_ORDERED", "$.window"))

    policies = document["denominator_policies"]
    if policies != sorted(policies, key=lambda policy: policy["metric_id"]):
        findings.add(Finding("DENOMINATOR_POLICIES_NOT_CANONICAL", "$.denominator_policies"))
    metric_ids = [policy["metric_id"] for policy in policies]
    if len(metric_ids) != len(set(metric_ids)):
        findings.add(Finding("DENOMINATOR_METRIC_IDS_NOT_UNIQUE", "$.denominator_policies"))
    class_counts = {class_name: counts[CLASS_PATHS[class_name]] for class_name in ALL_CLASSES}
    for index, policy in enumerate(policies):
        included = policy["included_classes"]
        excluded = policy["excluded_classes"]
        if included != sorted(included) or excluded != sorted(excluded):
            findings.add(Finding("DENOMINATOR_CLASSES_NOT_CANONICAL", f"$.denominator_policies[{index}]"))
        included_set = set(included)
        excluded_set = set(excluded)
        if included_set.intersection(excluded_set) or included_set.union(excluded_set) != set(ALL_CLASSES):
            findings.add(Finding("DENOMINATOR_CLASS_PARTITION_MISMATCH", f"$.denominator_policies[{index}]"))
        expected_count = sum(class_counts[class_name] for class_name in included)
        if policy["denominator_count"] != expected_count:
            findings.add(Finding("DENOMINATOR_COUNT_MISMATCH", f"$.denominator_policies[{index}].denominator_count"))

    semantics = document["class_semantics"]
    refusal = semantics["REFUSED"]
    if refusal["guarded_action_occurrence"] != "DID_NOT_OCCUR":
        findings.add(Finding("REFUSAL_ACTION_EVIDENCE_PROHIBITED", "$.class_semantics.REFUSED.guarded_action_occurrence"))
    if refusal["same_gate_feedback_allowed"] is not False:
        findings.add(Finding("REFUSAL_FEEDBACK_PROHIBITED", "$.class_semantics.REFUSED.same_gate_feedback_allowed"))
    for class_name in ("ADMITTED", "ERROR", "UNOBSERVED"):
        if semantics[class_name] != EXPECTED_CLASS_SEMANTICS[class_name]:
            findings.add(Finding("CLASS_SEMANTICS_MISMATCH", f"$.class_semantics.{class_name}"))

    expected_coverage_state = "COMPLETE" if counts["unobserved"] == 0 else "INCOMPLETE"
    if document["terminal_coverage_state"] != expected_coverage_state:
        findings.add(Finding("TERMINAL_COVERAGE_STATE_MISMATCH", "$.terminal_coverage_state"))

    expected_spec_hash, expected_assessment_id = _BUILDER.expected_identity(document)
    if document["spec_hash"] != expected_spec_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    if document["assessment_id"] != expected_assessment_id:
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "$.assessment_id"))

    return ValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        assessment_id=document.get("assessment_id"),
    )


def validate_file(path: Path) -> ValidationResult:
    try:
        document = load_json_file(path)
    except JsonInputError:
        return ValidationResult("ERROR", (Finding("INPUT_JSON_INVALID", "$"),))
    return validate_document(document)


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        suite = load_json_file(FIXTURE_PATH)
    except JsonInputError:
        return False, {"cases": [], "ok": False, "scope": SCOPE}
    cases: list[dict[str, object]] = []
    ok = True
    for case in suite.get("cases", []):
        try:
            document = _BUILDER.build_case(case)
            result = validate_document(document)
            actual_codes = sorted({finding.code for finding in result.findings})
            expected = case["expected"]
            case_ok = result.outcome == expected["validation_outcome"] and actual_codes == expected["finding_codes"]
        except (KeyError, TypeError, ValueError):
            result = ValidationResult("ERROR", (Finding("FIXTURE_BUILD_ERROR", "$"),))
            actual_codes = ["FIXTURE_BUILD_ERROR"]
            case_ok = False
        ok = ok and case_ok
        cases.append(
            {
                "case_id": case.get("case_id"),
                "actual_outcome": result.outcome,
                "actual_findings": actual_codes,
                "ok": case_ok,
            }
        )
    return ok, {"cases": cases, "ok": ok, "scope": SCOPE}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate GateAttemptCoverageAssessment candidates.")
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.candidate is not None:
            parser.error("--fixtures cannot be combined with --candidate")
        ok, report = run_fixture_suite()
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if args.candidate is None:
        parser.error("--candidate is required unless --fixtures is used")
    result = validate_file(args.candidate)
    print(
        json.dumps(
            {
                "assessment_id": result.assessment_id,
                "authority": "NONE",
                "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
                "outcome": result.outcome,
                "scope": SCOPE,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
