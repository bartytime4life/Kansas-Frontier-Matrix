"""Validate fixture-only PrecommittedEvaluationRecord candidates."""

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

from hashing import JsonInputError, compute_spec_hash, load_json_file  # noqa: E402

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/validation/precommitted_evaluation_record.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/validation/precommitted_evaluation_record/cases.json"
BUILDER_PATH = REPO_ROOT / "tools/generators/precommitted_evaluation_record/build_precommitted_evaluation_record.py"
SCOPE = "validation.precommitted_evaluation_record"


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_BUILDER = _load_module("kfm_precommitted_evaluation_record_builder", BUILDER_PATH)
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
    evaluation_id: str | None = None


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _schema_findings(document: object) -> list[Finding]:
    errors = sorted(_VALIDATOR.iter_errors(document), key=lambda error: tuple(str(p) for p in error.absolute_path))
    return [Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path))) for error in errors]


def _ids(items: Sequence[Mapping[str, Any]]) -> list[str]:
    return [str(item["prediction_id"]) for item in items]


def validate_document(document: object) -> ValidationResult:
    schema_findings = _schema_findings(document)
    if schema_findings or not isinstance(document, dict):
        return ValidationResult("DENY", tuple(sorted(set(schema_findings))))
    findings: set[Finding] = set()
    payload = document["sealed_payload"]
    seal = document["seal"]
    predictions = payload["predictions"]
    outcomes = document["observed_outcomes"]
    score_rows = document["score"]["per_prediction"]
    prediction_ids = _ids(predictions)
    outcome_ids = _ids(outcomes)
    score_ids = _ids(score_rows)

    if prediction_ids != sorted(prediction_ids) or len(prediction_ids) != len(set(prediction_ids)):
        findings.add(Finding("PREDICTIONS_NOT_CANONICAL", "$.sealed_payload.predictions"))
    if outcome_ids != sorted(outcome_ids) or len(outcome_ids) != len(set(outcome_ids)):
        findings.add(Finding("OUTCOMES_NOT_CANONICAL", "$.observed_outcomes"))
    if score_ids != sorted(score_ids) or len(score_ids) != len(set(score_ids)):
        findings.add(Finding("SCORE_ROWS_NOT_CANONICAL", "$.score.per_prediction"))
    if set(outcome_ids) != set(prediction_ids):
        findings.add(Finding("OUTCOME_COVERAGE_MISMATCH", "$.observed_outcomes"))
    if set(score_ids) != set(prediction_ids):
        findings.add(Finding("SCORE_COVERAGE_MISMATCH", "$.score.per_prediction"))

    if seal["commitment"] != compute_spec_hash(payload):
        findings.add(Finding("SEAL_MISMATCH", "$.seal.commitment"))
    if seal["published_at"] >= payload["window"]["opens_at"]:
        findings.add(Finding("REGISTRATION_NOT_PRECOMMITTED", "$.seal.published_at"))
    if seal["revealed_at"] < payload["window"]["closes_at"]:
        findings.add(Finding("REVEAL_BEFORE_WINDOW_CLOSE", "$.seal.revealed_at"))

    interventions = document["interventions"]
    if interventions != sorted(interventions, key=lambda item: (item["at"], item["kind"], item["evidence_ref"])):
        findings.add(Finding("INTERVENTIONS_NOT_SORTED", "$.interventions"))
    for index, intervention in enumerate(interventions):
        if intervention["at"] < seal["published_at"] or intervention["at"] > seal["revealed_at"]:
            findings.add(Finding("INTERVENTION_OUTSIDE_RECORD", f"$.interventions[{index}].at"))

    if set(outcome_ids) == set(prediction_ids):
        if document["score"] != _BUILDER.expected_score(document):
            findings.add(Finding("SCORE_MISMATCH", "$.score"))

    expected_spec_hash, expected_evaluation_id = _BUILDER.expected_identity(document)
    if document["spec_hash"] != expected_spec_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    if document["evaluation_id"] != expected_evaluation_id:
        findings.add(Finding("EVALUATION_ID_MISMATCH", "$.evaluation_id"))

    return ValidationResult("DENY" if findings else "PASS", tuple(sorted(findings)), evaluation_id=document.get("evaluation_id"))


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
        cases.append({"case_id": case.get("case_id"), "actual_outcome": result.outcome, "actual_findings": actual_codes, "ok": case_ok})
    return ok, {"cases": cases, "ok": ok, "scope": SCOPE}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate PrecommittedEvaluationRecord candidates.")
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
    print(json.dumps(
        {
            "authority": "NONE",
            "evaluation_id": result.evaluation_id,
            "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    ))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
