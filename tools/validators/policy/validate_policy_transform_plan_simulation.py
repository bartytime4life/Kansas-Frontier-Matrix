#!/usr/bin/env python3
"""Validate deterministic, fixture-only policy transform-plan simulations."""
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

SCHEMA = ROOT / "schemas/contracts/v1/policy/policy_transform_plan_simulation.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/policy/policy_transform_plan_simulation"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
SCOPE = "policy-transform-plan-simulation-fixture-only"
PROFILE = "kfm.policy.policy-transform-plan-simulation.v1"
RANK = {"NONE": 0, "FUZZ_DATE": 1, "GENERALIZE": 2, "SUPPRESS": 3}
FINDING_ORDER = (
    "TRANSFORM_TOO_WEAK",
    "GENERALIZE_DISTANCE_TOO_SMALL",
    "DATE_FUZZ_TOO_SMALL",
    "GEOMETRY_SUPPRESSION_REQUIRED",
    "EMBARGO_TOO_EARLY",
    "CONTRIBUTOR_SET_MISMATCH",
    "POLICY_REF_SET_MISMATCH",
    "REASON_CODE_SET_MISMATCH",
)
DIMENSION_BY_FINDING = {
    "TRANSFORM_TOO_WEAK": "TRANSFORM",
    "GENERALIZE_DISTANCE_TOO_SMALL": "GENERALIZATION_DISTANCE",
    "DATE_FUZZ_TOO_SMALL": "DATE_FUZZ",
    "GEOMETRY_SUPPRESSION_REQUIRED": "GEOMETRY_SUPPRESSION",
    "EMBARGO_TOO_EARLY": "EMBARGO",
    "CONTRIBUTOR_SET_MISMATCH": "CONTRIBUTORS",
    "POLICY_REF_SET_MISMATCH": "POLICY_REFS",
    "REASON_CODE_SET_MISMATCH": "REASON_CODES",
}
DIMENSION_ORDER = (
    "TRANSFORM",
    "GENERALIZATION_DISTANCE",
    "DATE_FUZZ",
    "GEOMETRY_SUPPRESSION",
    "EMBARGO",
    "CONTRIBUTORS",
    "POLICY_REFS",
    "REASON_CODES",
)
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


def _projection(candidate: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in candidate.items() if key not in {"spec_hash", "simulation_id"}}


def compute_record_spec_hash(candidate: Mapping[str, Any]) -> str:
    return compute_spec_hash(_projection(candidate))


def compute_simulation_id(candidate: Mapping[str, Any]) -> str:
    return "policy-transform-plan-simulation:" + compute_record_spec_hash(candidate).removeprefix("sha256:")[:24]


def compute_source_reduction_id(source_spec_hash: str) -> str:
    return "policy-obligation-reduction:" + source_spec_hash.removeprefix("sha256:")[:24]


def compute_required_result_spec_hash(required: Mapping[str, Any]) -> str:
    return compute_spec_hash(dict(required))


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _canonical_ordered_strings(value: object, order: Sequence[str]) -> bool:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        return False
    unique = set(value)
    return len(unique) == len(value) and unique <= set(order) and value == [item for item in order if item in unique]


def _normalized_strings(value: object) -> list[str]:
    if not isinstance(value, list):
        return []
    return sorted({str(item) for item in value})


def _required_coherent(required: Mapping[str, Any]) -> bool:
    transform = str(required.get("transform"))
    distance = required.get("generalize_distance_m")
    fuzz = required.get("date_fuzz_days")
    if transform not in RANK or not isinstance(distance, int) or not isinstance(fuzz, int):
        return False
    if transform == "GENERALIZE" and distance <= 0:
        return False
    if transform == "FUZZ_DATE" and fuzz <= 0:
        return False
    if distance > 0 and RANK[transform] < RANK["GENERALIZE"]:
        return False
    if fuzz > 0 and RANK[transform] < RANK["FUZZ_DATE"]:
        return False
    return True


def _effective_transform(plan: Mapping[str, Any]) -> str:
    if plan.get("record_action") == "SUPPRESS":
        return "SUPPRESS"
    if plan.get("geometry_action") in {"GENERALIZE", "SUPPRESS"}:
        return "GENERALIZE"
    if plan.get("date_action") == "FUZZ":
        return "FUZZ_DATE"
    return "NONE"


def assess_plan(candidate: Mapping[str, Any]) -> dict[str, Any]:
    source = candidate.get("source_reduction")
    plan = candidate.get("plan")
    if not isinstance(source, Mapping) or not isinstance(plan, Mapping):
        raise ValueError("source_reduction and plan are required")
    required = source.get("required")
    if not isinstance(required, Mapping):
        raise ValueError("source_reduction.required is required")

    codes: list[str] = []
    effective = _effective_transform(plan)
    required_transform = str(required.get("transform"))
    if RANK.get(effective, -1) < RANK.get(required_transform, 99):
        codes.append("TRANSFORM_TOO_WEAK")
    if int(plan.get("generalize_distance_m", -1)) < int(required.get("generalize_distance_m", 0)):
        codes.append("GENERALIZE_DISTANCE_TOO_SMALL")
    if int(plan.get("date_fuzz_days", -1)) < int(required.get("date_fuzz_days", 0)):
        codes.append("DATE_FUZZ_TOO_SMALL")
    if bool(required.get("suppress_geometry")) and plan.get("record_action") != "SUPPRESS" and plan.get("geometry_action") != "SUPPRESS":
        codes.append("GEOMETRY_SUPPRESSION_REQUIRED")

    required_embargo = required.get("embargo_until")
    planned_embargo = plan.get("embargo_until")
    if isinstance(required_embargo, str) and (not isinstance(planned_embargo, str) or planned_embargo < required_embargo):
        codes.append("EMBARGO_TOO_EARLY")

    if _normalized_strings(plan.get("covered_obligation_ids")) != _normalized_strings(required.get("contributing_obligation_ids")):
        codes.append("CONTRIBUTOR_SET_MISMATCH")
    if _normalized_strings(plan.get("source_policy_refs")) != _normalized_strings(required.get("source_policy_refs")):
        codes.append("POLICY_REF_SET_MISMATCH")
    if _normalized_strings(plan.get("reason_codes")) != _normalized_strings(required.get("reason_codes")):
        codes.append("REASON_CODE_SET_MISMATCH")

    ordered_codes = [code for code in FINDING_ORDER if code in codes]
    unmet = [dimension for dimension in DIMENSION_ORDER if any(DIMENSION_BY_FINDING[code] == dimension for code in ordered_codes)]
    return {
        "outcome": "SATISFIES" if not ordered_codes else "INSUFFICIENT",
        "finding_codes": ordered_codes,
        "unmet_dimensions": unmet,
    }


def _semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    source = candidate.get("source_reduction")
    plan = candidate.get("plan")
    assessment = candidate.get("assessment")
    provenance = candidate.get("provenance")

    if isinstance(source, Mapping):
        required = source.get("required")
        if isinstance(required, Mapping):
            if not _required_coherent(required):
                findings.append(Finding("SOURCE_REQUIREMENT_INCOHERENT", "/source_reduction/required"))
            try:
                if source.get("reduction_id") != compute_source_reduction_id(str(source.get("spec_hash"))):
                    findings.append(Finding("SOURCE_REDUCTION_ID_MISMATCH", "/source_reduction/reduction_id"))
                if source.get("result_spec_hash") != compute_required_result_spec_hash(required):
                    findings.append(Finding("SOURCE_RESULT_SPEC_HASH_MISMATCH", "/source_reduction/result_spec_hash"))
            except (TypeError, ValueError, OverflowError):
                findings.append(Finding("SOURCE_RESULT_SPEC_HASH_MISMATCH", "/source_reduction/result_spec_hash"))
            for field, code in (
                ("contributing_obligation_ids", "REQUIRED_CONTRIBUTORS_NOT_CANONICAL"),
                ("source_policy_refs", "REQUIRED_POLICY_REFS_NOT_CANONICAL"),
                ("reason_codes", "REQUIRED_REASON_CODES_NOT_CANONICAL"),
            ):
                if not _canonical_strings(required.get(field)):
                    findings.append(Finding(code, f"/source_reduction/required/{field}"))

    if isinstance(plan, Mapping):
        for field, code in (
            ("covered_obligation_ids", "PLAN_CONTRIBUTORS_NOT_CANONICAL"),
            ("source_policy_refs", "PLAN_POLICY_REFS_NOT_CANONICAL"),
            ("reason_codes", "PLAN_REASON_CODES_NOT_CANONICAL"),
        ):
            if not _canonical_strings(plan.get(field)):
                findings.append(Finding(code, f"/plan/{field}"))

    if isinstance(assessment, Mapping):
        if not _canonical_ordered_strings(assessment.get("finding_codes"), FINDING_ORDER):
            findings.append(Finding("ASSESSMENT_FINDINGS_NOT_CANONICAL", "/assessment/finding_codes"))
        if not _canonical_ordered_strings(assessment.get("unmet_dimensions"), DIMENSION_ORDER):
            findings.append(Finding("ASSESSMENT_DIMENSIONS_NOT_CANONICAL", "/assessment/unmet_dimensions"))

    if not findings:
        try:
            expected = assess_plan(candidate)
            if dict(assessment) != expected:
                findings.append(Finding("ASSESSMENT_MISMATCH", "/assessment"))
        except (TypeError, ValueError, OverflowError):
            findings.append(Finding("ASSESSMENT_MISMATCH", "/assessment"))

    if isinstance(source, Mapping) and isinstance(provenance, Mapping):
        expected_inputs = [str(source.get("reduction_id", ""))]
        if (
            provenance.get("source_reduction_ref") != source.get("reduction_id")
            or provenance.get("source_reduction_spec_hash") != source.get("spec_hash")
            or provenance.get("simulation_profile") != PROFILE
            or provenance.get("input_refs") != expected_inputs
        ):
            findings.append(Finding("PROVENANCE_MISMATCH", "/provenance"))

    try:
        if candidate.get("spec_hash") != compute_record_spec_hash(candidate):
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("simulation_id") != compute_simulation_id(candidate):
            findings.append(Finding("SIMULATION_ID_MISMATCH", "/simulation_id"))
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


def _assess_file(path: Path) -> tuple[bool, str]:
    candidate, findings = _read(path)
    if candidate is None:
        return False, _serialize(path, ValidationResult(tuple(findings)))
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return False, _serialize(path, ValidationResult(tuple(schema_findings)))
    try:
        assessment = assess_plan(candidate)
    except (TypeError, ValueError, OverflowError):
        return False, _serialize(path, ValidationResult((Finding("ASSESSMENT_UNAVAILABLE", "/assessment"),)))
    return True, json.dumps({"assessment": assessment, "file": _display(path), "scope": SCOPE}, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("records", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--assess", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        ok, lines = validate_fixture_suite()
        print(*lines, sep="\n")
        return 0 if ok else 1
    if not args.records:
        parser.error("provide records or --fixtures")
    ok = True
    for path in args.records:
        if args.assess:
            item_ok, line = _assess_file(path)
            print(line)
            ok = ok and item_ok
        else:
            result = validate_record(path)
            print(_serialize(path, result))
            ok = ok and result.ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
