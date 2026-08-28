"""Validate fixture-only TemporalQueryDisclosure candidates without network access."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/temporal_query_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/temporal_query_disclosure/cases.json"
BUILDER_PATH = REPO_ROOT / "tools/generators/temporal_query_disclosure/build.py"
SCOPE = "governance.temporal_query_disclosure"
ALLOWED_BASES = {
    "CURRENT_STATE": {"VALID_TIME", "BITEMPORAL", "RELEASE_TIME"},
    "PRIOR_STATE": {"VALID_TIME", "BITEMPORAL"},
    "SEQUENCED": {"VALID_TIME", "BITEMPORAL"},
    "NONSEQUENCED": {"TRANSACTION_TIME", "BITEMPORAL"},
    "TRACKING_LOG": {"TRANSACTION_TIME", "BITEMPORAL"},
}


def _load_builder():
    spec = importlib.util.spec_from_file_location("temporal_query_disclosure_builder", BUILDER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("builder unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILDER = _load_builder()
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
SCHEMA_VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]


def _schema_findings(value: object) -> set[Finding]:
    findings: set[Finding] = set()
    for error in SCHEMA_VALIDATOR.iter_errors(value):
        path = "$" + "".join(
            f"[{part}]" if isinstance(part, int) else f".{part}"
            for part in error.absolute_path
        )
        findings.add(Finding("SCHEMA_INVALID", path))
    return findings


def _utc_second(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    if parsed.microsecond or parsed.utcoffset() != timedelta(0):
        return None
    return parsed


def _sorted_unique(value: object) -> bool:
    return isinstance(value, list) and value == sorted(value) and len(value) == len(set(value))


def validate_disclosure(value: object) -> ValidationResult:
    findings = _schema_findings(value)
    if findings or not isinstance(value, dict):
        return ValidationResult("DENY", tuple(sorted(findings)))

    for path, collection in (("$.snapshot_refs", value["snapshot_refs"]), ("$.evidence_refs", value["evidence_refs"])):
        if not _sorted_unique(collection):
            findings.add(Finding("COLLECTION_NOT_SORTED_UNIQUE", path))

    for path in ("evaluated_at", "requested_as_of", "transaction_cutoff"):
        candidate = value[path]
        if candidate is not None and _utc_second(candidate) is None:
            findings.add(Finding("TIME_FORMAT_INVALID", f"$.{path}"))

    interval = value["valid_interval"]
    if isinstance(interval, dict):
        start = _utc_second(interval.get("start"))
        end = _utc_second(interval.get("end"))
        if start is None or end is None:
            findings.add(Finding("TIME_FORMAT_INVALID", "$.valid_interval"))
        elif start >= end:
            findings.add(Finding("VALID_INTERVAL_REVERSED", "$.valid_interval"))

    query_type = value["temporal_query_type"]
    basis = value["time_basis"]
    if basis not in ALLOWED_BASES[query_type]:
        findings.add(Finding("TIME_BASIS_INCOMPATIBLE", "$.time_basis"))

    requested = value["requested_as_of"]
    cutoff = value["transaction_cutoff"]
    snapshots = value["snapshot_refs"]
    if query_type == "CURRENT_STATE":
        if requested is not None or interval is not None or cutoff is not None:
            findings.add(Finding("CURRENT_STATE_FIELDS_INVALID", "$"))
        if len(snapshots) != 1:
            findings.add(Finding("CURRENT_STATE_SNAPSHOT_COUNT_INVALID", "$.snapshot_refs"))
    elif query_type == "PRIOR_STATE":
        if requested is None or interval is not None or cutoff is not None:
            findings.add(Finding("PRIOR_STATE_FIELDS_INVALID", "$"))
        if len(snapshots) != 1:
            findings.add(Finding("PRIOR_STATE_SNAPSHOT_COUNT_INVALID", "$.snapshot_refs"))
    elif query_type == "SEQUENCED":
        if requested is not None or interval is None or cutoff is not None:
            findings.add(Finding("SEQUENCED_FIELDS_INVALID", "$"))
        if len(snapshots) < 2:
            findings.add(Finding("SEQUENCE_REQUIRES_MULTIPLE_SNAPSHOTS", "$.snapshot_refs"))
    elif query_type == "NONSEQUENCED":
        if requested is not None or interval is not None or cutoff is None:
            findings.add(Finding("NONSEQUENCED_FIELDS_INVALID", "$"))
        if len(snapshots) < 2:
            findings.add(Finding("SEQUENCE_REQUIRES_MULTIPLE_SNAPSHOTS", "$.snapshot_refs"))
    elif query_type == "TRACKING_LOG":
        if requested is not None or interval is not None or cutoff is None:
            findings.add(Finding("TRACKING_LOG_FIELDS_INVALID", "$"))
        if len(snapshots) < 2:
            findings.add(Finding("SEQUENCE_REQUIRES_MULTIPLE_SNAPSHOTS", "$.snapshot_refs"))

    expected_code = BUILDER.EXPLANATION_CODES[query_type]
    if value["public_explanation_code"] != expected_code:
        findings.add(Finding("PUBLIC_EXPLANATION_CODE_MISMATCH", "$.public_explanation_code"))
    if value["spec_hash"] != BUILDER.compute_spec_hash(value):
        findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    if value["disclosure_id"] != BUILDER.compute_disclosure_id(value):
        findings.add(Finding("DISCLOSURE_ID_MISMATCH", "$.disclosure_id"))
    return ValidationResult("DENY" if findings else "PASS", tuple(sorted(findings)))


def _mutate(candidate: dict[str, object], mutation: Mapping[str, object]) -> dict[str, object]:
    result = copy.deepcopy(candidate)
    path = mutation.get("path")
    if not isinstance(path, list):
        raise ValueError("mutation path must be a list")
    parent: Any = result
    for part in path[:-1]:
        parent = parent[part]
    key = path[-1]
    if mutation.get("operation") == "set":
        parent[key] = mutation.get("value")
    elif mutation.get("operation") == "delete":
        del parent[key]
    else:
        raise ValueError("unsupported mutation")
    return result


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    suite = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    entries = suite.get("cases", []) if isinstance(suite, dict) else []
    report: list[dict[str, object]] = []
    ok = isinstance(entries, list) and bool(entries)
    for case in entries if isinstance(entries, list) else []:
        try:
            candidate = BUILDER.build_disclosure(
                query_run_ref=str(case["query_run_ref"]),
                temporal_query_type=str(case["temporal_query_type"]),
                time_basis=str(case["time_basis"]),
                evaluated_at=str(case["evaluated_at"]),
                requested_as_of=case.get("requested_as_of"),
                valid_start=case.get("valid_start"),
                valid_end=case.get("valid_end"),
                transaction_cutoff=case.get("transaction_cutoff"),
                snapshot_refs=case["snapshot_refs"],
                evidence_refs=case["evidence_refs"],
            )
            for mutation in case.get("mutations", []):
                candidate = _mutate(candidate, mutation)
            result = validate_disclosure(candidate)
            actual_codes = sorted({finding.code for finding in result.findings})
            expected = case["expected"]
            case_ok = result.outcome == expected["outcome"] and actual_codes == expected["finding_codes"]
        except (KeyError, TypeError, ValueError, OSError, json.JSONDecodeError):
            result = ValidationResult("ERROR", (Finding("FIXTURE_INPUT_ERROR", "$"),))
            actual_codes = ["FIXTURE_INPUT_ERROR"]
            expected = case.get("expected", {})
            case_ok = expected.get("outcome") == "ERROR" and expected.get("finding_codes") == actual_codes
        ok = ok and case_ok
        report.append({
            "case_id": case.get("case_id"),
            "actual_outcome": result.outcome,
            "actual_findings": actual_codes,
            "expected_outcome": expected.get("outcome"),
            "expected_findings": expected.get("finding_codes"),
            "ok": case_ok,
        })
    return ok, {"scope": SCOPE, "ok": ok, "cases": report}


def _serialize(result: ValidationResult) -> str:
    return json.dumps({
        "authority": "NONE",
        "outcome": result.outcome,
        "scope": SCOPE,
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
    }, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures == (args.input is not None):
        parser.error("select exactly one of --fixtures or --input")
    if args.fixtures:
        ok, report = run_fixture_suite()
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    assert args.input is not None
    try:
        value = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        result = ValidationResult("ERROR", (Finding("INPUT_ERROR", "$"),))
        print(_serialize(result))
        return 1
    result = validate_disclosure(value)
    print(_serialize(result))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
