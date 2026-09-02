"""Validate fixture-only KFM Watcher/Planner/Executor operation envelopes."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import JsonInputError, load_json_file  # noqa: E402

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/agent_operation_envelope.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/agent_operation_envelope/cases.json"
)
BUILDER_PATH = (
    REPO_ROOT
    / "tools/generators/agent_operation_envelope/build_agent_operation_envelope.py"
)
SCOPE = "governance.agent_operation_envelope"


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_BUILDER = _load_module("kfm_agent_operation_envelope_builder", BUILDER_PATH)
GATE_ORDER = _BUILDER.GATE_ORDER
ROLE_INPUTS = {
    "WATCHER": ({"SOURCE_SNAPSHOT"}, {"SOURCE_SNAPSHOT"}),
    "PLANNER": (
        {"WATCHER_FACTS", "POLICY_BASELINE"},
        {"WATCHER_FACTS", "POLICY_BASELINE", "VALIDATION_EVIDENCE"},
    ),
    "EXECUTOR": (
        {"PLAN", "VALIDATION_EVIDENCE", "ATTESTATION"},
        {"PLAN", "VALIDATION_EVIDENCE", "ATTESTATION"},
    ),
}
ROLE_OUTPUTS = {
    "WATCHER": ({"FACTS"}, {"FACTS", "ALERTS"}),
    "PLANNER": (
        {"PLAN", "DIFF_CANDIDATE", "VALIDATION_EVIDENCE"},
        {"PLAN", "DIFF_CANDIDATE", "VALIDATION_EVIDENCE"},
    ),
    "EXECUTOR": (
        {"DRAFT_PR_METADATA", "EXECUTION_RECEIPT"},
        {"DRAFT_PR_METADATA", "EXECUTION_RECEIPT"},
    ),
}
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    operation_id: str | None = None
    declared_disposition: str | None = None


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _binding_key(binding: Mapping[str, object]) -> tuple[str, str]:
    return str(binding.get("kind", "")), str(binding.get("ref", ""))


def expected_identity(document: Mapping[str, Any]) -> tuple[str, str]:
    return _BUILDER.expected_identity(document)


def expected_idempotency_key(document: Mapping[str, Any]) -> str:
    return _BUILDER.expected_idempotency_key(document)


def expected_disposition(document: Mapping[str, Any]) -> tuple[str, list[str]]:
    return _BUILDER.expected_disposition(document)


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
    role = str(document["actor"]["role"])
    inputs = document["inputs"]
    outputs = document["outputs"]
    gates = document["gates"]
    evidence_refs = document["evidence_refs"]

    if inputs != sorted(inputs, key=_binding_key):
        findings.add(Finding("INPUT_BINDINGS_NOT_SORTED", "$.inputs"))
    input_kinds = [str(item["kind"]) for item in inputs]
    if len(input_kinds) != len(set(input_kinds)):
        findings.add(Finding("INPUT_KIND_DUPLICATE", "$.inputs"))

    required_inputs, allowed_inputs = ROLE_INPUTS[role]
    input_kind_set = set(input_kinds)
    for kind in sorted(required_inputs - input_kind_set):
        findings.add(Finding("REQUIRED_INPUT_KIND_MISSING", f"$.inputs.{kind}"))
    for kind in sorted(input_kind_set - allowed_inputs):
        findings.add(Finding("INPUT_KIND_NOT_ALLOWED", f"$.inputs.{kind}"))

    if outputs != sorted(outputs, key=_binding_key):
        findings.add(Finding("OUTPUT_BINDINGS_NOT_SORTED", "$.outputs"))
    output_kinds = [str(item["kind"]) for item in outputs]
    if len(output_kinds) != len(set(output_kinds)):
        findings.add(Finding("OUTPUT_KIND_DUPLICATE", "$.outputs"))

    required_outputs, allowed_outputs = ROLE_OUTPUTS[role]
    output_kind_set = set(output_kinds)
    for kind in sorted(required_outputs - output_kind_set):
        findings.add(Finding("REQUIRED_OUTPUT_KIND_MISSING", f"$.outputs.{kind}"))
    for kind in sorted(output_kind_set - allowed_outputs):
        findings.add(Finding("OUTPUT_KIND_NOT_ALLOWED", f"$.outputs.{kind}"))

    if tuple(str(gate["gate"]) for gate in gates) != GATE_ORDER:
        findings.add(Finding("GATE_ORDER_INVALID", "$.gates"))
    if evidence_refs != sorted(evidence_refs):
        findings.add(Finding("EVIDENCE_REFS_NOT_SORTED", "$.evidence_refs"))

    if document["operation"]["idempotency_key"] != expected_idempotency_key(document):
        findings.add(Finding("IDEMPOTENCY_KEY_MISMATCH", "$.operation.idempotency_key"))

    expected_spec_hash, expected_operation_id = expected_identity(document)
    if document["spec_hash"] != expected_spec_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    if document["operation_id"] != expected_operation_id:
        findings.add(Finding("OPERATION_ID_MISMATCH", "$.operation_id"))

    expected_outcome, expected_reasons = expected_disposition(document)
    disposition = document["disposition"]
    if disposition["outcome"] != expected_outcome:
        findings.add(Finding("DISPOSITION_MISMATCH", "$.disposition.outcome"))
    if disposition["reason_codes"] != expected_reasons:
        findings.add(Finding("REASON_CODES_MISMATCH", "$.disposition.reason_codes"))

    if role == "EXECUTOR" and document["target"]["base_branch"] == document["target"]["head_branch"]:
        findings.add(Finding("TARGET_BRANCH_COLLISION", "$.target.head_branch"))

    return ValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        operation_id=document.get("operation_id"),
        declared_disposition=str(disposition.get("outcome")),
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
            "authority": "NONE",
            "declared_disposition": result.declared_disposition,
            "execution_mode": "FIXTURE_ONLY_NO_EXTERNAL_EFFECT",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "operation_id": result.operation_id,
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
        expected_operation_id = case.get("expected_operation_id")
        identity_ok = expected_operation_id is None or document.get("operation_id") == expected_operation_id
        case_ok = (
            isinstance(expected, dict)
            and result.outcome == expected.get("validation_outcome")
            and actual_codes == expected.get("finding_codes")
            and identity_ok
        )
        ok = ok and case_ok
        cases.append(
            {
                "actual_findings": actual_codes,
                "actual_outcome": result.outcome,
                "case_id": case.get("case_id"),
                "declared_disposition": result.declared_disposition,
                "expected_findings": expected.get("finding_codes") if isinstance(expected, dict) else None,
                "expected_outcome": expected.get("validation_outcome") if isinstance(expected, dict) else None,
                "identity_ok": identity_ok,
                "ok": case_ok,
            }
        )
    return ok, {"cases": cases, "ok": ok, "scope": SCOPE}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only Watcher/Planner/Executor envelopes."
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
