#!/usr/bin/env python3
"""Validate the inactive unresolved-slot ThresholdPolicyRegistry candidate.

A PASS proves bounded local shape, identity, canonical ordering, repository
pressure-reference existence, and explicit non-effects only. It does not adopt a
threshold, evaluate policy, bind a watcher, activate a source, or authorize
promotion, release, publication, notification, or public use.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash


SCHEMA = ROOT / "schemas/contracts/v1/policy/threshold_policy_registry.schema.json"
REGISTRY = ROOT / "policy/thresholds/registry.v1.json"
FIXTURES = ROOT / "fixtures/contracts/v1/policy/threshold_policy_registry"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "threshold-policy-registry-unresolved-slots-only"
EXPECTED_REASONS = ["NO_VALUE_ADOPTED", "STEWARD_REVIEW_REQUIRED"]
PRESSURE_ROOTS = {"contracts", "docs", "policy", "tools"}
ERROR_CODES = {
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_COMPLEXITY_LIMIT",
    "JSON_DUPLICATE_KEY",
    "JSON_INVALID",
    "JSON_NONFINITE_NUMBER",
    "JSON_NOT_UTF8",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains NaN or infinity."""


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
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
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
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    subject = dict(candidate)
    subject.pop("spec_hash", None)
    return compute_spec_hash(subject)


def _canonical_strings(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _safe_pressure_path(value: str) -> Path | None:
    if not value or "\\" in value or value.startswith("/"):
        return None
    relative = PurePosixPath(value)
    if str(relative) != value or any(part in {"", ".", ".."} for part in relative.parts):
        return None
    if not relative.parts or relative.parts[0] not in PRESSURE_ROOTS:
        return None
    candidate = ROOT.joinpath(*relative.parts)
    current = ROOT
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            return None
    return candidate if candidate.is_file() else None


def semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        expected_hash = canonical_spec_hash(candidate)
    except CanonicalizationFailure:
        findings.append(Finding("CANONICALIZATION_ERROR", "/"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    thresholds = candidate.get("thresholds")
    items = thresholds if isinstance(thresholds, list) else []
    threshold_ids = [
        item.get("threshold_id")
        for item in items
        if isinstance(item, Mapping)
    ]
    if not all(isinstance(item, str) for item in threshold_ids) or threshold_ids != sorted(set(threshold_ids)):
        findings.append(Finding("THRESHOLD_IDS_NOT_CANONICAL", "/thresholds"))

    metric_keys: list[tuple[Any, Any]] = []
    for index, item in enumerate(items):
        if not isinstance(item, Mapping):
            continue
        metric_keys.append((item.get("domain"), item.get("metric")))
        for field in ("reason_codes", "steward_roles", "evidence_refs", "pressure_refs"):
            if not _canonical_strings(item.get(field)):
                findings.append(
                    Finding("ARRAY_NOT_CANONICAL", f"/thresholds/{index}/{field}")
                )
        if item.get("reason_codes") != EXPECTED_REASONS:
            findings.append(
                Finding("UNRESOLVED_REASONS_REQUIRED", f"/thresholds/{index}/reason_codes")
            )
        pressure_refs = item.get("pressure_refs")
        if isinstance(pressure_refs, list):
            for ref_index, ref in enumerate(pressure_refs):
                if not isinstance(ref, str) or _safe_pressure_path(ref) is None:
                    findings.append(
                        Finding(
                            "PRESSURE_REF_INVALID",
                            f"/thresholds/{index}/pressure_refs/{ref_index}",
                        )
                    )
    if len(metric_keys) != len(set(metric_keys)):
        findings.append(Finding("DOMAIN_METRIC_DUPLICATE", "/thresholds"))

    governance = candidate.get("governance")
    if isinstance(governance, Mapping) and any(value is not False for value in governance.values()):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(validate_payload(candidate).findings)
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize(path: Path, result: ValidationResult) -> str:
    outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
    return json.dumps(
        {
            "authority": "NONE",
            "file": _display(path),
            "findings": [
                {"code": item.code, "field": item.field} for item in result.findings
            ],
            "non_effects": [
                "no_threshold_value_adoption",
                "no_policy_evaluation_or_watcher_binding",
                "no_source_activation",
                "no_promotion_release_publication_or_notification",
            ],
            "outcome": outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> tuple[int, str]:
    valid = sorted((FIXTURES / "valid").glob("valid_*.json"))
    invalid = sorted((FIXTURES / "invalid").glob("invalid_*.json"))
    failures: list[str] = []
    for path in valid:
        if not validate_record(path).ok:
            failures.append(f"valid:{path.name}")
    for path in invalid:
        if validate_record(path).ok:
            failures.append(f"invalid:{path.name}")
    report = json.dumps(
        {
            "authority": "NONE",
            "failures": failures,
            "invalid_cases": len(invalid),
            "outcome": "PASS" if not failures and valid and invalid else "FAIL",
            "scope": SCOPE,
            "valid_cases": len(valid),
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    return (0 if not failures and valid and invalid else 1), report


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", nargs="*", type=Path)
    parser.add_argument("--registry", action="store_true")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.records or args.registry:
            parser.error("--fixtures cannot be combined with records or --registry")
        code, report = run_fixture_profile()
        print(report)
        return code

    records = list(args.records)
    if args.registry:
        records.append(REGISTRY)
    if not records:
        parser.error("provide records, --registry, or --fixtures")

    ok = True
    for path in records:
        result = validate_record(path)
        print(serialize(path, result))
        ok = ok and result.ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
