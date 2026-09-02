#!/usr/bin/env python3
"""Validate fixture-only, non-authoritative policy-obligation reductions."""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_obligation_reduction.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/policy/policy_obligation_reduction"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
SCOPE = "policy-obligation-reduction-fixture-only"
RANK = {"NONE": 0, "FUZZ_DATE": 1, "GENERALIZE": 2, "SUPPRESS": 3}
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "JSON_INVALID", "JSON_DUPLICATE_KEY", "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE",
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
    result = float(value)
    if not math.isfinite(result):
        raise NonFiniteError
    return result


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.exists():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        raw = path.read_bytes()
        if len(raw) > 1_048_576:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"), object_pairs_hook=_pairs,
            parse_constant=_nonfinite, parse_float=_float,
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
    encoded = [str(p).replace("~", "~0").replace("/", "~1") for p in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [
            Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
            for error in sorted(validator.iter_errors(candidate), key=lambda e: _pointer(e.absolute_path))
        ]
    except (OSError, json.JSONDecodeError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]


def reduce_obligations(obligations: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    if not obligations:
        raise ValueError("at least one obligation is required")
    transforms = [str(item["transform"]) for item in obligations]
    embargoes = [str(item["embargo_until"]) for item in obligations if item.get("embargo_until") is not None]
    return {
        "transform": max(transforms, key=lambda value: RANK[value]),
        "generalize_distance_m": max(int(item["generalize_distance_m"]) for item in obligations),
        "date_fuzz_days": max(int(item["date_fuzz_days"]) for item in obligations),
        "suppress_geometry": any(bool(item["suppress_geometry"]) for item in obligations),
        "embargo_until": max(embargoes) if embargoes else None,
        "contributing_obligation_ids": sorted({str(item["obligation_id"]) for item in obligations}),
        "source_policy_refs": sorted({str(item["policy_decision_ref"]) for item in obligations}),
        "reason_codes": sorted({str(code) for item in obligations for code in item["reason_codes"]}),
    }


def _projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in candidate.items() if key not in {"spec_hash", "reduction_id"}}


def compute_record_spec_hash(candidate: Mapping[str, Any]) -> str:
    return compute_spec_hash(_projection(candidate))


def compute_reduction_id(candidate: Mapping[str, Any]) -> str:
    return "policy-obligation-reduction:" + compute_record_spec_hash(candidate).removeprefix("sha256:")[:24]


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _coherent(item: Mapping[str, Any]) -> bool:
    transform = item.get("transform")
    distance = item.get("generalize_distance_m")
    fuzz = item.get("date_fuzz_days")
    if transform == "GENERALIZE" and not isinstance(distance, int):
        return False
    if transform == "GENERALIZE" and distance <= 0:
        return False
    if transform == "FUZZ_DATE" and (not isinstance(fuzz, int) or fuzz <= 0):
        return False
    if transform == "NONE" and (distance != 0 or fuzz != 0):
        return False
    if isinstance(distance, int) and distance > 0 and RANK.get(str(transform), -1) < RANK["GENERALIZE"]:
        return False
    if isinstance(fuzz, int) and fuzz > 0 and RANK.get(str(transform), -1) < RANK["FUZZ_DATE"]:
        return False
    return True


def _semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    inputs = candidate.get("inputs")
    if not isinstance(inputs, list) or not all(isinstance(item, Mapping) for item in inputs):
        return findings
    obligations = [dict(item) for item in inputs]
    ids = [str(item.get("obligation_id", "")) for item in obligations]
    if ids != sorted(ids):
        findings.append(Finding("INPUT_ORDER_NOT_CANONICAL", "/inputs"))
    if len(ids) != len(set(ids)):
        findings.append(Finding("DUPLICATE_OBLIGATION_ID", "/inputs"))
    for index, item in enumerate(obligations):
        if not _canonical_strings(item.get("reason_codes")):
            findings.append(Finding("OBLIGATION_REASONS_NOT_CANONICAL", f"/inputs/{index}/reason_codes"))
        if not _coherent(item):
            findings.append(Finding("OBLIGATION_INCOHERENT", f"/inputs/{index}"))
    if findings:
        return findings
    expected = reduce_obligations(obligations)
    result = candidate.get("result")
    if isinstance(result, Mapping):
        if result.get("contributing_obligation_ids") != expected["contributing_obligation_ids"]:
            findings.append(Finding("CONTRIBUTOR_SET_MISMATCH", "/result/contributing_obligation_ids"))
        if dict(result) != expected:
            findings.append(Finding("RESULT_MISMATCH", "/result"))
    provenance = candidate.get("provenance")
    if isinstance(provenance, Mapping) and provenance.get("input_refs") != sorted(set(ids)):
        findings.append(Finding("PROVENANCE_INPUT_REFS_MISMATCH", "/provenance/input_refs"))
    try:
        if candidate.get("spec_hash") != compute_record_spec_hash(candidate):
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("reduction_id") != compute_reduction_id(candidate):
            findings.append(Finding("REDUCTION_ID_MISMATCH", "/reduction_id"))
    except (TypeError, ValueError, OverflowError):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    governance = candidate.get("governance")
    if isinstance(governance, Mapping) and any(value is not False for value in governance.values()):
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return findings


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    schema_findings = _schema_findings(candidate)
    findings.extend(schema_findings)
    if not schema_findings:
        findings.extend(_semantic(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    outcome = "PASS" if result.ok else ("ERROR" if result.error else "FAIL")
    return json.dumps(
        {"file": _display(path), "findings": [{"code": f.code, "field": f.field} for f in result.findings], "outcome": outcome, "scope": SCOPE},
        sort_keys=True, separators=(",", ":"),
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
        return False, [_serialize(MANIFEST, ValidationResult(tuple(errors)))]
    cases = manifest.get("cases")
    if not isinstance(cases, list):
        result = ValidationResult((Finding("FIXTURE_MANIFEST_INVALID", "/cases"),))
        return False, [_serialize(MANIFEST, result)]
    ok, lines, seen = True, [], set()
    for case in cases:
        if not isinstance(case, Mapping):
            ok = False
            continue
        case_id, expected, codes = case.get("case_id"), case.get("expected_outcome"), case.get("expected_findings")
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
        lines.append(json.dumps({"case_id": case_id, "file": _display(path), "finding_codes": actual_codes, "outcome": actual, "scope": SCOPE, "suite_match": match}, sort_keys=True, separators=(",", ":")))
    return ok, lines


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
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
        print(_serialize(path, result))
        ok = ok and result.ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
