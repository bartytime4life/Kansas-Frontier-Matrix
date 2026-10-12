#!/usr/bin/env python3
"""Deterministic, no-network validation for the proposed ClaimEnvelope.

PASS proves local shape and bounded semantics only. It does not resolve evidence,
decide policy, authenticate review, release, publish, or authorize public use.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import stat
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas/contracts/v1/evidence/claim_envelope.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/claim_envelope"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
MAX_BYTES = 256 * 1024
DENIED_PREFIXES = ("raw:", "work:", "quarantine:", "internal:", "canonical:", "model:")
REF_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._~:/#?=&%+@-]{0,319}$")
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "JSON_INVALID", "JSON_DUPLICATE_KEY", "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE", "MANIFEST_INVALID",
}

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str

@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    @property
    def ok(self) -> bool: return not self.findings
    @property
    def error(self) -> bool: return any(item.code in ERROR_CODES for item in self.findings)
    @property
    def outcome(self) -> str: return "PASS" if self.ok else ("ERROR" if self.error else "FAIL")

def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value: raise DuplicateKeyError
        value[key] = item
    return value

def _constant(_: str) -> object: raise NonFiniteNumberError

def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed

def _read(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    fd: int | None = None
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/", "symbolic links are denied")]
        fd = os.open(path, os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0))
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            return None, [Finding("FILE_NOT_FOUND", "/", "input is not a regular file")]
        if info.st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/", "input exceeds 256 KiB")]
        with os.fdopen(fd, "rb") as stream:
            fd = None
            raw = stream.read(MAX_BYTES + 1)
        value = json.loads(raw.decode(), object_pairs_hook=_pairs, parse_constant=_constant, parse_float=_float)
    except FileNotFoundError:
        return None, [Finding("FILE_NOT_FOUND", "/", "input file was not found")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/", "duplicate members are denied")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/", "numbers must be finite")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/", "input is not valid JSON")]
    except (OSError, UnicodeError, RecursionError, ValueError):
        return None, [Finding("FILE_READ_ERROR", "/", "input could not be read safely")]
    finally:
        if fd is not None: os.close(fd)
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/", "JSON root must be an object")]
    return value, []

def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(p).replace("~", "~0").replace("/", "~1") for p in parts]
    return "/" + "/".join(encoded) if encoded else "/"

def _schema_findings(value: Mapping[str, object]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text())
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/", "schema could not be loaded safely")]
    errors = sorted(validator.iter_errors(value), key=lambda e: (_pointer(e.absolute_path), str(e.validator)))
    return [Finding("SCHEMA_INVALID", _pointer(e.absolute_path), f"schema constraint failed: {e.validator}") for e in errors[:50]]

def _time(value: object) -> datetime | None:
    try: return datetime.fromisoformat(str(value).replace("Z", "+00:00")) if value is not None else None
    except ValueError: return None

def _refs(value: object, field: str, canonical_code: str) -> list[Finding]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value): return []
    findings: list[Finding] = []
    if value != sorted(set(value)):
        findings.append(Finding(canonical_code, field, "references must be sorted and unique"))
    if any(not REF_RE.fullmatch(item) for item in value):
        findings.append(Finding("REFERENCE_INVALID", field, "reference violates the bounded grammar"))
    if any(item.casefold().startswith(DENIED_PREFIXES) for item in value):
        findings.append(Finding("INTERNAL_REFERENCE_DENIED", field, "lifecycle-private references are denied"))
    return findings

def _semantic(value: Mapping[str, object]) -> list[Finding]:
    findings = _refs(value.get("evidence_refs"), "/evidence_refs", "EVIDENCE_REFS_NOT_CANONICAL")
    findings += _refs(value.get("source_refs"), "/source_refs", "SOURCE_REFS_NOT_CANONICAL")
    temporal = value.get("temporal_scope")
    if isinstance(temporal, dict):
        start, end = _time(temporal.get("valid_from")), _time(temporal.get("valid_to"))
        observed, as_of = _time(temporal.get("observed_at")), _time(temporal.get("as_of"))
        if start and end and end < start:
            findings.append(Finding("TEMPORAL_ORDER_INVALID", "/temporal_scope/valid_to", "valid_to precedes valid_from"))
        if observed and as_of and observed > as_of:
            findings.append(Finding("TEMPORAL_ORDER_INVALID", "/temporal_scope/observed_at", "observed_at follows as_of"))
    if value.get("release_state") == "PUBLISHED":
        rules = [
            (value.get("support_state") != "SUPPORTED", "PUBLISHED_SUPPORT_INVALID", "/support_state"),
            (value.get("policy_state") != "ALLOW", "PUBLISHED_POLICY_INVALID", "/policy_state"),
            (value.get("review_state") != "APPROVED", "PUBLISHED_REVIEW_INVALID", "/review_state"),
            (not value.get("evidence_refs"), "PUBLISHED_EVIDENCE_REQUIRED", "/evidence_refs"),
            (not value.get("source_refs"), "PUBLISHED_SOURCE_REQUIRED", "/source_refs"),
            (not value.get("release_ref"), "PUBLISHED_RELEASE_REQUIRED", "/release_ref"),
            (not value.get("correction_path_ref"), "PUBLISHED_CORRECTION_REQUIRED", "/correction_path_ref"),
            (not value.get("rollback_ref"), "PUBLISHED_ROLLBACK_REQUIRED", "/rollback_ref"),
            (value.get("knowledge_character") == "AI_PROPOSAL", "AI_PROPOSAL_PUBLICATION_DENIED", "/knowledge_character"),
        ]
        findings += [Finding(code, field, "published claim invariant failed") for failed, code, field in rules if failed]
    return sorted(set(findings))

def validate_value(value: Mapping[str, object]) -> ValidationResult:
    schema = _schema_findings(value)
    return ValidationResult(tuple(sorted(set(schema or _semantic(value)))))

def validate(path: Path) -> ValidationResult:
    value, findings = _read(path)
    return ValidationResult(tuple(findings)) if value is None else validate_value(value)

def run_fixtures() -> int:
    manifest, findings = _read(MANIFEST)
    if manifest is None or findings or not isinstance(manifest.get("cases"), list):
        print("CLAIM_ENVELOPE_FIXTURES_ERROR code=MANIFEST_INVALID")
        return 2
    failures: list[str] = []
    cases = manifest["cases"]
    for case in cases:
        result = validate(FIXTURES / case["path"])
        actual = sorted({item.code for item in result.findings})
        if result.outcome != case["expected_outcome"] or actual != sorted(case["expected_findings"]):
            failures.append(case["case_id"])
        print(f"CLAIM_ENVELOPE_FIXTURE case={case['case_id']} outcome={result.outcome} findings={','.join(actual) if actual else '-'}")
    if failures:
        for case_id in failures: print(f"CLAIM_ENVELOPE_FIXTURE_MISMATCH case={case_id}")
        return 1
    print(f"CLAIM_ENVELOPE_FIXTURES_VALID cases={len(cases)} no_network=true authority=validation-only")
    return 0

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures: return run_fixtures()
    if args.path is None: parser.error("path is required unless --fixtures is used")
    result = validate(args.path)
    for finding in result.findings:
        print(f"CLAIM_ENVELOPE_{result.outcome} code={finding.code} field={finding.field} detail={finding.detail}")
    if result.ok:
        print(f"CLAIM_ENVELOPE_PASS path={args.path} authority=validation-only")
        return 0
    return 2 if result.error else 1

if __name__ == "__main__":
    sys.exit(main())
