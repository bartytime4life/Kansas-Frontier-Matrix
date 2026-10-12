"""Validate fixture-only KFM remote-sensing lineage activities."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import JsonInputError, load_json_file  # noqa: E402


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/telemetry/remote_sensing_lineage_activity.schema.json"
)
OPENLINEAGE_SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/telemetry/openlineage_run_event_projection.schema.json"
)
RUN_RECEIPT_SCHEMA_PATH = (
    REPO_ROOT / "schemas/contracts/v1/runtime/run_receipt.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/telemetry/remote_sensing_lineage_activity/cases.json"
)
BUILDER_PATH = (
    REPO_ROOT
    / "tools/generators/telemetry/build_remote_sensing_lineage_activity.py"
)
OPENLINEAGE_VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/telemetry/validate_openlineage_run_event_projection.py"
)
SCOPE = "telemetry.remote_sensing_lineage_activity"

_BUILDER = _load_module("kfm_remote_sensing_lineage_builder", BUILDER_PATH)
_OPENLINEAGE_VALIDATOR = _load_module(
    "kfm_remote_sensing_source_openlineage_validator",
    OPENLINEAGE_VALIDATOR_PATH,
)
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_OPENLINEAGE_SCHEMA = json.loads(
    OPENLINEAGE_SCHEMA_PATH.read_text(encoding="utf-8")
)
_RUN_RECEIPT_SCHEMA = json.loads(
    RUN_RECEIPT_SCHEMA_PATH.read_text(encoding="utf-8")
)
_REGISTRY = Registry()
for resource_schema in (_OPENLINEAGE_SCHEMA, _RUN_RECEIPT_SCHEMA):
    _REGISTRY = _REGISTRY.with_resource(
        resource_schema["$id"], Resource.from_contents(resource_schema)
    )
_SCHEMA_VALIDATOR = Draft202012Validator(
    _SCHEMA,
    registry=_REGISTRY,
    format_checker=FormatChecker(),
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    activity_id: str | None = None
    declared_decision: str | None = None


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _schema_findings(document: object) -> list[Finding]:
    errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(document),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    return [
        Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path)))
        for error in errors
    ]


def validate_document(document: object) -> ValidationResult:
    schema_findings = _schema_findings(document)
    if schema_findings or not isinstance(document, dict):
        return ValidationResult("DENY", tuple(sorted(set(schema_findings))))

    findings: set[Finding] = set()
    source_result = _OPENLINEAGE_VALIDATOR.validate_document(
        document["source_openlineage_projection"]
    )
    if source_result.outcome != "PASS":
        findings.add(
            Finding(
                "SOURCE_PROJECTION_INVALID",
                "$.source_openlineage_projection",
            )
        )

    if document["source_links"] != sorted(document["source_links"]):
        findings.add(Finding("SOURCE_LINKS_NOT_SORTED", "$.source_links"))

    metrics = document["metrics"]
    if metrics["scene_count"] != (
        metrics["processed_scene_count"] + metrics["failed_scene_count"]
    ):
        expected_outcome, _ = _BUILDER.expected_decision(document)
        if expected_outcome != "DENY":
            findings.add(
                Finding("SCENE_COUNT_DECISION_MISMATCH", "$.decision.outcome")
            )

    decision = document["decision"]
    if decision["reason_codes"] != sorted(decision["reason_codes"]):
        findings.add(
            Finding("REASON_CODES_NOT_SORTED", "$.decision.reason_codes")
        )
    expected_outcome, expected_reasons = _BUILDER.expected_decision(document)
    if decision["outcome"] != expected_outcome:
        findings.add(
            Finding("DECISION_OUTCOME_MISMATCH", "$.decision.outcome")
        )
    if decision["reason_codes"] != expected_reasons:
        findings.add(
            Finding("REASON_CODES_MISMATCH", "$.decision.reason_codes")
        )

    if document["remote_sensing_facet"] != _BUILDER.expected_facet(document):
        findings.add(
            Finding(
                "REMOTE_SENSING_FACET_MISMATCH",
                "$.remote_sensing_facet",
            )
        )
    if document["prov_activity"] != _BUILDER.expected_prov_activity(document):
        findings.add(Finding("PROV_ACTIVITY_MISMATCH", "$.prov_activity"))
    if document["non_effects"] != _BUILDER.NON_EFFECTS:
        findings.add(Finding("NON_EFFECTS_MISMATCH", "$.non_effects"))

    expected_spec_hash, expected_activity_id = _BUILDER.expected_identity(document)
    if document["spec_hash"] != expected_spec_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    if document["activity_id"] != expected_activity_id:
        findings.add(Finding("ACTIVITY_ID_MISMATCH", "$.activity_id"))

    return ValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        activity_id=str(document.get("activity_id")),
        declared_decision=str(decision.get("outcome")),
    )


def validate_file(path: Path) -> ValidationResult:
    try:
        document = load_json_file(path)
    except JsonInputError:
        return ValidationResult("ERROR", (Finding("INPUT_JSON_INVALID", "$"),))
    return validate_document(document)


def _serialize_result(result: ValidationResult) -> str:
    return json.dumps(
        {
            "activity_id": result.activity_id,
            "authority": "NONE",
            "declared_decision": result.declared_decision,
            "execution_mode": "FIXTURE_ONLY_NO_NETWORK",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        suite = load_json_file(FIXTURE_PATH)
    except JsonInputError:
        return False, {"cases": [], "ok": False, "scope": SCOPE}

    entries = suite.get("cases", []) if isinstance(suite, dict) else []
    cases: list[dict[str, object]] = []
    ok = True
    for case in entries:
        if not isinstance(case, dict):
            ok = False
            continue
        try:
            document = _BUILDER.build_case(case)
        except (KeyError, TypeError, ValueError):
            ok = False
            continue
        result = validate_document(document)
        actual_codes = sorted({finding.code for finding in result.findings})
        expected = case.get("expected", {})
        declared_ok = (
            not isinstance(expected, dict)
            or expected.get("declared_decision") is None
            or result.declared_decision == expected.get("declared_decision")
        )
        case_ok = (
            isinstance(expected, dict)
            and result.outcome == expected.get("validation_outcome")
            and actual_codes == expected.get("finding_codes")
            and declared_ok
        )
        ok = ok and case_ok
        cases.append(
            {
                "actual_findings": actual_codes,
                "actual_outcome": result.outcome,
                "case_id": case.get("case_id"),
                "declared_decision": result.declared_decision,
                "ok": case_ok,
            }
        )
    return ok, {"cases": cases, "ok": ok, "scope": SCOPE}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only remote-sensing lineage activities."
    )
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
    print(_serialize_result(result))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
