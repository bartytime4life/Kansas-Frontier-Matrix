#!/usr/bin/env python3
"""Validate fixture-only structured PolicyObligation records."""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_obligation.schema.json"
REGISTRY = ROOT / "policy/decision/vocabulary.v1.json"
FIXTURES = ROOT / "fixtures/contracts/v1/policy/policy_obligation"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
SCOPE = "policy-obligation-fixture-only"
ERROR_CODES = {
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED",
    "JSON_INVALID",
    "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
    "REGISTRY_UNAVAILABLE",
}


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


class DuplicateKeyError(ValueError):
    pass


class NonFiniteError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in items:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _nonfinite(_value: str) -> object:
    raise NonFiniteError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        raw = path.read_bytes()
        if len(raw) > 1_048_576:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [
            Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
            for error in sorted(
                validator.iter_errors(candidate),
                key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
            )
        ]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]


def _registry_entries() -> tuple[dict[str, Mapping[str, Any]] | None, list[Finding]]:
    registry, findings = _read(REGISTRY)
    if registry is None:
        return None, [Finding("REGISTRY_UNAVAILABLE", "/")]
    entries = registry.get("obligation_codes")
    if not isinstance(entries, list) or not all(isinstance(item, Mapping) for item in entries):
        return None, [Finding("REGISTRY_UNAVAILABLE", "/obligation_codes")]
    mapped: dict[str, Mapping[str, Any]] = {}
    for item in entries:
        code = item.get("code")
        if not isinstance(code, str) or code in mapped:
            return None, [Finding("REGISTRY_UNAVAILABLE", "/obligation_codes")]
        mapped[code] = item
    return mapped, findings


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _parse_datetime(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in candidate.items() if key != "spec_hash"}


def compute_record_spec_hash(candidate: Mapping[str, Any]) -> str:
    return compute_spec_hash(_projection(candidate))


def _parameter_findings(code: str, parameters: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    def require(field: str, predicate: bool = True) -> None:
        if not predicate or parameters.get(field) is None:
            findings.append(Finding("REQUIRED_PARAMETER_MISSING", f"/parameters/{field}"))

    if code == "ATTACH_CITATIONS":
        refs = parameters.get("required_evidence_refs")
        require("required_evidence_refs", isinstance(refs, list) and len(refs) > 0)
    elif code == "ATTACH_RIGHTS_NOTICE":
        require("required_notice_ref")
    elif code == "DELAY_PUBLICATION":
        require("embargo_until")
    elif code == "GENERALIZE_GEOMETRY":
        distance = parameters.get("generalize_distance_m")
        require("generalize_distance_m", isinstance(distance, int) and distance > 0)
    elif code == "REDACT_EXACT_LOCATION":
        require("suppress_geometry", parameters.get("suppress_geometry") is True)
    elif code == "REQUIRE_STEWARD_REVIEW":
        require("review_role")
    elif code == "VERIFY_ROLLBACK_TARGET":
        require("rollback_target_ref")
    elif code == "WITHHOLD_EXPORT":
        require("export_allowed", parameters.get("export_allowed") is False)
    elif code == "AGGREGATE_ONLY":
        group_size = parameters.get("minimum_group_size")
        unit_ref = parameters.get("aggregation_unit_ref")
        if not ((isinstance(group_size, int) and group_size >= 2) or isinstance(unit_ref, str)):
            findings.append(Finding("REQUIRED_PARAMETER_MISSING", "/parameters"))
    elif code == "RETAIN_UNTIL":
        require("retain_until")
    elif code == "SHARE_ALIKE":
        require("share_alike_license_ref")
    return findings


def semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    registry, registry_findings = _registry_entries()
    findings.extend(registry_findings)
    if registry is None:
        return findings

    code = candidate.get("code")
    family = candidate.get("policy_family")
    entry = registry.get(str(code))
    if entry is None:
        findings.append(Finding("OBLIGATION_CODE_UNKNOWN", "/code"))
    else:
        families = entry.get("policy_families")
        if not isinstance(families, list) or family not in families:
            findings.append(Finding("POLICY_FAMILY_NOT_ALLOWED", "/policy_family"))

    for field in ("audiences", "reason_codes"):
        if not _canonical_strings(candidate.get(field)):
            findings.append(Finding("ARRAY_NOT_CANONICAL", f"/{field}"))

    parameters = candidate.get("parameters")
    if isinstance(parameters, Mapping):
        if not _canonical_strings(parameters.get("required_evidence_refs")):
            findings.append(Finding("ARRAY_NOT_CANONICAL", "/parameters/required_evidence_refs"))
        if isinstance(code, str):
            findings.extend(_parameter_findings(code, parameters))

    valid_time = candidate.get("valid_time")
    if isinstance(valid_time, Mapping):
        start = _parse_datetime(valid_time.get("effective_from"))
        end_value = valid_time.get("effective_until")
        end = _parse_datetime(end_value) if end_value is not None else None
        if start is not None and end is not None and end < start:
            findings.append(Finding("VALID_TIME_REVERSED", "/valid_time/effective_until"))

    enforcement = candidate.get("enforcement")
    if isinstance(enforcement, Mapping):
        if not _canonical_strings(enforcement.get("evidence_refs")):
            findings.append(Finding("ARRAY_NOT_CANONICAL", "/enforcement/evidence_refs"))
        state = enforcement.get("state")
        evaluator_ref = enforcement.get("evaluator_ref")
        evaluated_at = enforcement.get("evaluated_at")
        evidence_refs = enforcement.get("evidence_refs")
        waiver_ref = enforcement.get("waiver_ref")
        if state == "PENDING":
            if evaluator_ref is not None or evaluated_at is not None or waiver_ref is not None:
                findings.append(Finding("ENFORCEMENT_STATE_INCOHERENT", "/enforcement"))
        elif state in {"SATISFIED", "UNSATISFIED", "CONFLICTED"}:
            if not isinstance(evaluator_ref, str) or not isinstance(evaluated_at, str) or not isinstance(evidence_refs, list) or not evidence_refs or waiver_ref is not None:
                findings.append(Finding("ENFORCEMENT_STATE_INCOHERENT", "/enforcement"))
        elif state == "WAIVED":
            if not isinstance(evaluator_ref, str) or not isinstance(evaluated_at, str) or not isinstance(waiver_ref, str):
                findings.append(Finding("ENFORCEMENT_STATE_INCOHERENT", "/enforcement"))

    governance = candidate.get("governance")
    if isinstance(governance, Mapping) and any(value is not False for value in governance.values()):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    try:
        if candidate.get("spec_hash") != compute_record_spec_hash(candidate):
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    except (TypeError, ValueError, OverflowError):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
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
            "file": _display(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": outcome,
            "scope": SCOPE,
            "authority": {
                "policy_evaluation": False,
                "obligation_enforcement": False,
                "promotion": False,
                "release": False,
                "publication": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _fixture_path(relative: object) -> Path | None:
    if not isinstance(relative, str) or not relative or "\\" in relative:
        return None
    pure = PurePosixPath(relative)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        return None
    return FIXTURES.joinpath(*pure.parts)


def validate_fixture_suite() -> tuple[bool, list[str]]:
    manifest, errors = _read(MANIFEST)
    if manifest is None:
        return False, [serialize(MANIFEST, ValidationResult(tuple(errors)))]
    cases = manifest.get("cases")
    if not isinstance(cases, list):
        result = ValidationResult((Finding("FIXTURE_MANIFEST_INVALID", "/cases"),))
        return False, [serialize(MANIFEST, result)]
    ok, lines, seen = True, [], set()
    for case in cases:
        if not isinstance(case, Mapping):
            ok = False
            continue
        case_id = case.get("case_id")
        expected = case.get("expected_outcome")
        codes = case.get("expected_findings")
        path = _fixture_path(case.get("record"))
        if not isinstance(case_id, str) or case_id in seen or path is None or expected not in {"PASS", "FAIL", "ERROR"} or not isinstance(codes, list):
            ok = False
            continue
        seen.add(case_id)
        result = validate_record(path)
        actual = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
        actual_codes = sorted({finding.code for finding in result.findings})
        match = actual == expected and actual_codes == sorted(set(str(code) for code in codes))
        ok = ok and match
        lines.append(json.dumps({
            "case_id": case_id,
            "file": _display(path),
            "finding_codes": actual_codes,
            "outcome": actual,
            "scope": SCOPE,
            "suite_match": match,
        }, sort_keys=True, separators=(",", ":")))
    return ok, lines


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate structured PolicyObligation records.")
    parser.add_argument("records", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        ok, lines = validate_fixture_suite()
        print(*lines, sep="\n")
        return 0 if ok else 1
    if not args.records:
        parser.error("provide records or --fixtures")
    ok = True
    for path in args.records:
        result = validate_record(path)
        print(serialize(path, result))
        ok = ok and result.ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
