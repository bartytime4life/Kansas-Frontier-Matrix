#!/usr/bin/env python3
"""Validate fixture-only KFM PolicyObligationSet candidates.

A PASS proves closed candidate shape, canonical ordering, kind/parameter
coherence, deterministic identity, and explicit non-authority only. It does not
run policy, authenticate references, enforce duties, modify evidence, promote,
release, publish, or authorize public use.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import stat
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_obligation_set.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/policy/policy_obligation_set"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "policy-obligation-set-candidate-only"
PARAMETER_KEYS = (
    "attribution_ref",
    "share_alike_license",
    "retention_days",
    "minimum_aggregation_count",
    "embargo_until",
    "notice_ref",
    "consent_ref",
)
REQUIRED_PARAMETER = {
    "AGGREGATION_ONLY": "minimum_aggregation_count",
    "ATTRIBUTION_REQUIRED": "attribution_ref",
    "CONSENT_REQUIRED": "consent_ref",
    "EMBARGO": "embargo_until",
    "NO_REDISTRIBUTION": None,
    "NOTICE_REQUIRED": "notice_ref",
    "RETENTION_LIMIT": "retention_days",
    "SHARE_ALIKE_REQUIRED": "share_alike_license",
}
ERROR_CODES = frozenset(
    {
        "INPUT_NOT_FILE",
        "INPUT_READ_ERROR",
        "INPUT_SYMLINK_DENIED",
        "INPUT_TOO_LARGE",
        "JSON_DUPLICATE_KEY",
        "JSON_INVALID",
        "JSON_NONFINITE_NUMBER",
        "JSON_NOT_UTF8",
        "ROOT_NOT_OBJECT",
        "SCHEMA_INVALID",
        "SCHEMA_UNAVAILABLE",
    }
)


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
    def outcome(self) -> str:
        if any(item.code in ERROR_CODES for item in self.findings):
            return "ERROR"
        return "PASS" if not self.findings else "FAIL"

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                return None, [Finding("INPUT_NOT_FILE", "/")]
            with os.fdopen(descriptor, "rb") as stream:
                descriptor = -1
                raw = stream.read(MAX_JSON_BYTES + 1)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
        if len(raw) > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_nonfinite,
            parse_float=_finite,
        )
    except FileNotFoundError:
        return None, [Finding("INPUT_NOT_FILE", "/")]
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema, format_checker=FormatChecker()
                ).iter_errors(value),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_INVALID", "/"))
    return findings


def _canonical(values: Any) -> bool:
    return isinstance(values, list) and values == sorted(set(values))


def _parameters_valid(obligation: Mapping[str, Any]) -> bool:
    kind = obligation.get("kind")
    parameters = obligation.get("parameters")
    if kind not in REQUIRED_PARAMETER or not isinstance(parameters, dict):
        return False
    required = REQUIRED_PARAMETER[kind]
    for key in PARAMETER_KEYS:
        value = parameters.get(key)
        if key == required:
            if value is None:
                return False
        elif value is not None:
            return False
    if kind == "NO_REDISTRIBUTION":
        applies_to = obligation.get("applies_to")
        if not isinstance(applies_to, list) or "REDISTRIBUTE" not in applies_to:
            return False
    return True


def _semantic(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    obligations = value.get("obligations")
    if not isinstance(obligations, list):
        return findings
    obligation_ids = [
        item.get("obligation_id") for item in obligations if isinstance(item, dict)
    ]
    if obligation_ids != sorted(obligation_ids):
        findings.append(Finding("OBLIGATIONS_NOT_CANONICAL", "/obligations"))
    if len(obligation_ids) != len(set(obligation_ids)):
        findings.append(Finding("OBLIGATION_ID_DUPLICATE", "/obligations"))

    referenced_policy_ids: list[str] = []
    for index, obligation in enumerate(obligations):
        if not isinstance(obligation, dict):
            continue
        if not _canonical(obligation.get("applies_to")):
            findings.append(Finding("APPLIES_TO_NOT_CANONICAL", f"/obligations/{index}/applies_to"))
        if not _canonical(obligation.get("reason_codes")):
            findings.append(Finding("REASON_CODES_NOT_CANONICAL", f"/obligations/{index}/reason_codes"))
        if not _parameters_valid(obligation):
            findings.append(Finding("PARAMETERS_INVALID", f"/obligations/{index}/parameters"))
        policy_ref = obligation.get("policy_decision_ref")
        if isinstance(policy_ref, str):
            referenced_policy_ids.append(policy_ref)

    policy_refs = value.get("policy_decision_refs")
    expected_refs = sorted(set(referenced_policy_ids))
    if not _canonical(policy_refs) or policy_refs != expected_refs:
        findings.append(Finding("POLICY_REFS_MISMATCH", "/policy_decision_refs"))

    governance = value.get("governance")
    if isinstance(governance, dict) and any(item is not False for item in governance.values()):
        findings.append(Finding("AUTHORITY_OVERREACH", "/governance"))

    projection = {
        key: item
        for key, item in value.items()
        if key not in {"spec_hash", "obligation_set_id"}
    }
    actual_hash = compute_spec_hash(projection)
    if value.get("spec_hash") != actual_hash:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    expected_id = "kfm://policy/obligation-set/" + actual_hash.split(":", 1)[1][:24]
    if value.get("obligation_set_id") != expected_id:
        findings.append(Finding("OBLIGATION_SET_ID_MISMATCH", "/obligation_set_id"))
    return findings


def validate(path: Path) -> ValidationResult:
    value, findings = _read(path)
    if value is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(value))
    if not findings:
        findings.extend(_semantic(value))
    return ValidationResult(tuple(sorted(set(findings))))


def serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "outcome": result.outcome,
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "scope": SCOPE,
            "authority_created": False,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixtures() -> int:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cases = manifest["cases"]
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError):
        return 1
    passed = True
    for case in cases:
        path = FIXTURES / case["input"]
        result = validate(path)
        codes = sorted({finding.code for finding in result.findings})
        matched = (
            result.outcome == case["expected_outcome"]
            and codes == case["expected_findings"]
        )
        print(
            json.dumps(
                {
                    "case_id": case["case_id"],
                    "outcome": result.outcome,
                    "findings": codes,
                    "suite_match": matched,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        passed = passed and matched
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only PolicyObligationSet candidates."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with files")
        return run_fixtures()
    files = args.files or [FIXTURES / "valid/valid_obligation_set.json"]
    failed = False
    for path in sorted(files, key=lambda candidate: candidate.as_posix()):
        result = validate(path)
        print(serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
