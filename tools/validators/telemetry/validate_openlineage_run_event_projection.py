"""Validate fixture-only KFM OpenLineage terminal RunEvent projections."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import JsonInputError, load_json_file  # noqa: E402

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/telemetry/"
    "openlineage_run_event_projection.schema.json"
)
RUN_RECEIPT_SCHEMA_PATH = (
    REPO_ROOT / "schemas/contracts/v1/runtime/run_receipt.schema.json"
)
FIXTURE_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/telemetry/"
    "openlineage_run_event_projection/cases.json"
)
BUILDER_PATH = (
    REPO_ROOT
    / "tools/generators/telemetry/"
    "build_openlineage_run_event_projection.py"
)
SCOPE = "telemetry.openlineage_run_event_projection"


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_BUILDER = _load_module("kfm_openlineage_projection_builder", BUILDER_PATH)
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_RUN_RECEIPT_SCHEMA = json.loads(
    RUN_RECEIPT_SCHEMA_PATH.read_text(encoding="utf-8")
)
_REGISTRY = Registry().with_resource(
    _RUN_RECEIPT_SCHEMA["$id"], Resource.from_contents(_RUN_RECEIPT_SCHEMA)
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
    projection_id: str | None = None
    declared_decision: str | None = None
    event_type: str | None = None


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


def _dataset_key(dataset: Mapping[str, object]) -> tuple[str, str]:
    return str(dataset.get("role", "")), str(dataset.get("ref", ""))


def _resolution_key(resolution: Mapping[str, object]) -> str:
    return str(resolution.get("evidence_ref", ""))


def _event_findings(
    actual: Mapping[str, Any], expected: Mapping[str, Any]
) -> set[Finding]:
    findings: set[Finding] = set()
    checks = (
        ("eventType", "EVENT_TYPE_MISMATCH"),
        ("eventTime", "EVENT_TIME_MISMATCH"),
        ("producer", "EVENT_PRODUCER_MISMATCH"),
        ("schemaURL", "EVENT_SCHEMA_URL_MISMATCH"),
    )
    for field, code in checks:
        if actual.get(field) != expected.get(field):
            findings.add(Finding(code, f"$.event.{field}"))

    actual_run = actual.get("run")
    expected_run = expected.get("run")
    if not isinstance(actual_run, dict) or not isinstance(expected_run, dict):
        findings.add(Finding("EVENT_RUN_MISMATCH", "$.event.run"))
    else:
        if actual_run.get("runId") != expected_run.get("runId"):
            findings.add(Finding("EVENT_RUN_ID_MISMATCH", "$.event.run.runId"))
        if actual_run.get("facets") != expected_run.get("facets"):
            findings.add(Finding("EVENT_RUN_FACETS_MISMATCH", "$.event.run.facets"))

    if actual.get("job") != expected.get("job"):
        findings.add(Finding("EVENT_JOB_MISMATCH", "$.event.job"))
    if actual.get("inputs") != expected.get("inputs"):
        findings.add(Finding("EVENT_INPUTS_MISMATCH", "$.event.inputs"))
    if actual.get("outputs") != expected.get("outputs"):
        findings.add(Finding("EVENT_OUTPUTS_MISMATCH", "$.event.outputs"))
    return findings


def validate_document(document: object) -> ValidationResult:
    schema_findings = _schema_findings(document)
    if schema_findings or not isinstance(document, dict):
        return ValidationResult("DENY", tuple(sorted(set(schema_findings))))

    findings: set[Finding] = set()
    receipt = document["source_run_receipt"]
    datasets = document["datasets"]
    resolutions = document["evidence_resolutions"]
    decision = document["decision"]

    for field in (
        "inputs",
        "outputs",
        "source_descriptor_refs",
        "validation_refs",
    ):
        values = receipt[field]
        if values != sorted(values):
            findings.add(
                Finding(
                    f"RUN_RECEIPT_{field.upper()}_NOT_SORTED",
                    f"$.source_run_receipt.{field}",
                )
            )
        if len(values) != len(set(values)):
            findings.add(
                Finding(
                    f"RUN_RECEIPT_{field.upper()}_DUPLICATE",
                    f"$.source_run_receipt.{field}",
                )
            )

    if datasets != sorted(datasets, key=_dataset_key):
        findings.add(Finding("DATASETS_NOT_SORTED", "$.datasets"))
    dataset_refs = [str(item["ref"]) for item in datasets]
    if len(dataset_refs) != len(set(dataset_refs)):
        findings.add(Finding("DATASET_REF_DUPLICATE", "$.datasets"))
    dataset_names = [
        (str(item["role"]), str(item["namespace"]), str(item["name"]))
        for item in datasets
    ]
    if len(dataset_names) != len(set(dataset_names)):
        findings.add(Finding("DATASET_IDENTITY_DUPLICATE", "$.datasets"))
    for index, dataset in enumerate(datasets):
        if dataset["evidence_refs"] != sorted(dataset["evidence_refs"]):
            findings.add(
                Finding(
                    "DATASET_EVIDENCE_REFS_NOT_SORTED",
                    f"$.datasets[{index}].evidence_refs",
                )
            )

    if resolutions != sorted(resolutions, key=_resolution_key):
        findings.add(
            Finding("EVIDENCE_RESOLUTIONS_NOT_SORTED", "$.evidence_resolutions")
        )
    resolution_refs = [str(item["evidence_ref"]) for item in resolutions]
    if len(resolution_refs) != len(set(resolution_refs)):
        findings.add(
            Finding("EVIDENCE_RESOLUTION_DUPLICATE", "$.evidence_resolutions")
        )

    declared_inputs = {
        str(item["ref"]) for item in datasets if item["role"] == "INPUT"
    }
    declared_outputs = {
        str(item["ref"]) for item in datasets if item["role"] == "OUTPUT"
    }
    if declared_inputs != set(receipt["inputs"]):
        findings.add(
            Finding(
                "INPUT_DATASET_BINDING_MISMATCH",
                "$.source_run_receipt.inputs",
            )
        )
    if declared_outputs != set(receipt["outputs"]):
        findings.add(
            Finding(
                "OUTPUT_DATASET_BINDING_MISMATCH",
                "$.source_run_receipt.outputs",
            )
        )

    used_evidence = {
        str(evidence_ref)
        for dataset in datasets
        for evidence_ref in dataset["evidence_refs"]
    }
    if used_evidence != set(resolution_refs):
        findings.add(
            Finding(
                "EVIDENCE_RESOLUTION_SET_MISMATCH",
                "$.evidence_resolutions",
            )
        )

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
        findings.add(Finding("REASON_CODES_MISMATCH", "$.decision.reason_codes"))

    event = document["event"]
    if expected_outcome == "PASS":
        if not isinstance(event, dict):
            findings.add(Finding("EVENT_PRESENCE_MISMATCH", "$.event"))
        else:
            findings.update(_event_findings(event, _BUILDER.expected_event(document)))
    elif event is not None:
        findings.add(Finding("EVENT_PRESENCE_MISMATCH", "$.event"))

    if document["non_effects"] != _BUILDER.NON_EFFECTS:
        findings.add(Finding("NON_EFFECTS_MISMATCH", "$.non_effects"))

    expected_spec_hash, expected_projection_id = _BUILDER.expected_identity(document)
    if document["spec_hash"] != expected_spec_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    if document["projection_id"] != expected_projection_id:
        findings.add(Finding("PROJECTION_ID_MISMATCH", "$.projection_id"))

    event_type = event.get("eventType") if isinstance(event, dict) else None
    return ValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        projection_id=str(document.get("projection_id")),
        declared_decision=str(decision.get("outcome")),
        event_type=str(event_type) if event_type is not None else None,
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
            "declared_decision": result.declared_decision,
            "event_type": result.event_type,
            "execution_mode": "FIXTURE_ONLY_NO_NETWORK",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "projection_id": result.projection_id,
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
        expected_projection_id = case.get("expected_projection_id")
        identity_ok = (
            expected_projection_id is None
            or document.get("projection_id") == expected_projection_id
        )
        declared_decision_ok = (
            not isinstance(expected, dict)
            or expected.get("declared_decision") is None
            or result.declared_decision == expected.get("declared_decision")
        )
        event_type_ok = (
            not isinstance(expected, dict)
            or expected.get("event_type") is None
            or result.event_type == expected.get("event_type")
        )
        case_ok = (
            isinstance(expected, dict)
            and result.outcome == expected.get("validation_outcome")
            and actual_codes == expected.get("finding_codes")
            and identity_ok
            and declared_decision_ok
            and event_type_ok
        )
        ok = ok and case_ok
        cases.append(
            {
                "actual_findings": actual_codes,
                "actual_outcome": result.outcome,
                "case_id": case.get("case_id"),
                "declared_decision": result.declared_decision,
                "event_type": result.event_type,
                "expected_findings": (
                    expected.get("finding_codes")
                    if isinstance(expected, dict)
                    else None
                ),
                "expected_outcome": (
                    expected.get("validation_outcome")
                    if isinstance(expected, dict)
                    else None
                ),
                "identity_ok": identity_ok,
                "ok": case_ok,
            }
        )
    return ok, {"cases": cases, "ok": ok, "scope": SCOPE}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only OpenLineage terminal RunEvent projections."
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
