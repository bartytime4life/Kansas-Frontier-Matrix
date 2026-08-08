#!/usr/bin/env python3
"""Validate fixture-first SourceIntakeRecord and DriftSummary candidates.

PASS proves closed schema shape plus bounded cross-field invariants only. It does
not activate a source, admit RAW, resolve evidence authenticity, approve policy,
promote, release, publish, or authorize a watcher.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import stat
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
INTAKE_SCHEMA = ROOT / "schemas/contracts/v1/source/source_intake_record.schema.json"
DRIFT_SCHEMA = ROOT / "schemas/contracts/v1/source/drift_summary.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_intake_record"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
MAX_JSON_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "source-intake-record-fixture-first-candidate-only"

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str

@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    @property
    def ok(self) -> bool: return not self.findings
    @property
    def outcome(self) -> str: return "PASS" if self.ok else "ERROR"

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out: raise DuplicateKeyError(key)
        out[key] = value
    return out

def _reject(_value: str) -> None: raise NonFiniteNumberError

def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed

def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink(): return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(path, flags)
        try:
            if not stat.S_ISREG(os.fstat(fd).st_mode): return None, [Finding("INPUT_NOT_FILE", "/")]
            with os.fdopen(fd, "rb") as stream:
                fd = -1; raw = stream.read(MAX_JSON_BYTES + 1)
        finally:
            if fd >= 0: os.close(fd)
        if len(raw) > MAX_JSON_BYTES: return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique, parse_constant=_reject, parse_float=_finite)
    except FileNotFoundError: return None, [Finding("INPUT_NOT_FILE", "/")]
    except UnicodeDecodeError: return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError: return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError: return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError: return None, [Finding("JSON_INVALID", "/")]
    except OSError: return None, [Finding("INPUT_READ_ERROR", "/")]
    if not isinstance(value, dict): return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []

def _ptr(parts: Iterable[Any]) -> str:
    values = [str(p).replace("~", "~0").replace("/", "~1") for p in parts]
    return "/" + "/".join(values) if values else "/"

def _validator() -> Draft202012Validator:
    intake = json.loads(INTAKE_SCHEMA.read_text(encoding="utf-8"))
    drift = json.loads(DRIFT_SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(intake); Draft202012Validator.check_schema(drift)
    registry = Registry().with_resource(drift["$id"], Resource.from_contents(drift))
    return Draft202012Validator(intake, registry=registry, format_checker=FormatChecker())

def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    errors = list(islice(_validator().iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    findings = [Finding("SCHEMA_INVALID", _ptr(e.absolute_path)) for e in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors) > MAX_SCHEMA_FINDINGS: findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings

def _utc(value: object) -> datetime | None:
    if not isinstance(value, str): return None
    try: return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError: return None

def _semantic(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    reasons = value.get("reason_codes")
    if isinstance(reasons, list) and reasons != sorted(set(reasons)):
        findings.append(Finding("REASON_CODES_NOT_CANONICAL", "/reason_codes"))
    drift = value.get("drift_summary") if isinstance(value.get("drift_summary"), dict) else {}
    codes = drift.get("change_codes")
    fields = drift.get("changed_fields")
    if isinstance(codes, list) and codes != sorted(set(codes)):
        findings.append(Finding("CHANGE_CODES_NOT_CANONICAL", "/drift_summary/change_codes"))
    if isinstance(fields, list) and fields != sorted(set(fields)):
        findings.append(Finding("CHANGED_FIELDS_NOT_CANONICAL", "/drift_summary/changed_fields"))
    window = drift.get("comparison_window")
    if isinstance(window, dict):
        prior, current = _utc(window.get("prior_observed_at")), _utc(window.get("current_observed_at"))
        if prior and current and prior > current:
            findings.append(Finding("COMPARISON_WINDOW_REVERSED", "/drift_summary/comparison_window"))
    kind, materiality = drift.get("drift_kind"), drift.get("materiality")
    if kind == "NONE" and (materiality != "NONE" or codes != ["NO_CHANGE"] or fields != []):
        findings.append(Finding("NO_CHANGE_DECLARATION_INVALID", "/drift_summary"))
    if kind != "NONE" and not fields and not drift.get("metrics"):
        findings.append(Finding("DRIFT_DETAIL_REQUIRED", "/drift_summary"))
    if drift.get("sensitive_implication") != "NONE" and drift.get("public_detail_allowed") is not False:
        findings.append(Finding("SENSITIVE_PUBLIC_DETAIL_DENIED", "/drift_summary/public_detail_allowed"))
    disposition = value.get("disposition")
    state = value.get("publication_state")
    candidate = value.get("candidate_delta_ref")
    if candidate is not None and disposition != "PROPOSED_WORK_RECORD":
        findings.append(Finding("CANDIDATE_DELTA_DISPOSITION_INVALID", "/candidate_delta_ref"))
    if disposition == "NO_MATERIAL_CHANGE":
        if materiality not in {"NONE", "BELOW_THRESHOLD"} or candidate is not None:
            findings.append(Finding("NO_MATERIAL_CHANGE_INVALID", "/disposition"))
    if disposition == "PROPOSED_WORK_RECORD" and materiality != "REVIEW_REQUIRED":
        findings.append(Finding("WORK_RECORD_MATERIALITY_INVALID", "/drift_summary/materiality"))
    if disposition == "QUARANTINED":
        if state != "QUARANTINE" or materiality != "BLOCKING":
            findings.append(Finding("QUARANTINE_MATERIALITY_INVALID", "/drift_summary/materiality"))
        if value.get("policy_review_required") is not True:
            findings.append(Finding("QUARANTINE_POLICY_REVIEW_REQUIRED", "/policy_review_required"))
    if materiality == "BLOCKING" and (state != "QUARANTINE" or disposition != "QUARANTINED"):
        findings.append(Finding("BLOCKING_DRIFT_NOT_QUARANTINED", "/publication_state"))
    return findings

def validate(path: Path) -> ValidationResult:
    value, findings = _read(path)
    if value is None: return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(value))
    if not findings: findings.extend(_semantic(value))
    return ValidationResult(tuple(sorted(set(findings))))

def run_fixtures() -> int:
    try: manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError): return 1
    passed = True
    for case in manifest["cases"]:
        path = FIXTURES / case["input"]; result = validate(path)
        codes = sorted({f.code for f in result.findings})
        match = result.outcome == case["expected_outcome"] and codes == case["expected_findings"]
        print(json.dumps({"case_id":case["case_id"],"outcome":result.outcome,"findings":codes,"suite_match":match}, sort_keys=True, separators=(",",":")))
        passed = passed and match
    return 0 if passed else 1

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path); parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files: parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    files = args.files or [FIXTURES / "valid/valid_proposed_work_record.json"]
    failed = False
    for path in sorted(files, key=lambda p:p.as_posix()):
        result = validate(path)
        print(json.dumps({"file":path.as_posix(),"outcome":result.outcome,"findings":[{"code":f.code,"field":f.field} for f in result.findings],"scope":SCOPE}, sort_keys=True, separators=(",",":")))
        failed = failed or not result.ok
    return 1 if failed else 0

if __name__ == "__main__": raise SystemExit(main())
