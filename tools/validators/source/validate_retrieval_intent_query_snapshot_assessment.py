#!/usr/bin/env python3
"""Validate fixture-only retrieval intent/query snapshot assessments.

PASS proves internal declaration coherence only. This module performs no
network access, secret resolution, reference resolution, source admission,
evidence decision, lifecycle mutation, release, publication, or public use.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/source/retrieval_intent_query_snapshot_assessment.schema.json"
CASES = ROOT / "fixtures/contracts/v1/source/retrieval_intent_query_snapshot_assessment/cases.json"
MAX_BYTES = 1_048_576
SCOPE = "retrieval-intent-query-snapshot-assessment-fixture-only-v1"
IDENTITY_PREFIX = "retrieval-query-assessment:"
SOURCE_IDEAS = ["KFM-CAND-0127", "KFM-CAND-0128", "KFM-CAND-0129"]
ABSTAIN_CODES = {"EXECUTION_INCOMPLETE", "RETRIEVAL_FAILED"}
ERROR_CODES = {
    "ASSESSMENT_ID_MISMATCH",
    "FILE_NOT_FOUND",
    "FILE_READ_ERROR",
    "FILE_TOO_LARGE",
    "FIXTURE_MANIFEST_INVALID",
    "INPUT_SYMLINK_DENIED",
    "JSON_DUPLICATE_KEY",
    "JSON_INVALID",
    "JSON_NONFINITE_NUMBER",
    "ROOT_NOT_OBJECT",
    "SCHEMA_INVALID",
    "SCHEMA_UNAVAILABLE",
    "SPEC_HASH_MISMATCH",
}
DEVIATION_FIELDS = (
    ("authentication_posture", "AUTHENTICATION_POSTURE_CHANGED"),
    ("exclusions", "EXCLUSIONS_CHANGED"),
    ("requested_fields", "FIELDS_CHANGED"),
    ("filters", "FILTERS_CHANGED"),
    ("geographic_scope", "GEOGRAPHIC_SCOPE_CHANGED"),
    ("pagination", "PAGINATION_CHANGED"),
    ("result_selection", "RESULT_SELECTION_CHANGED"),
    ("sampling", "SAMPLING_CHANGED"),
    ("temporal_scope", "TEMPORAL_SCOPE_CHANGED"),
)
FALSE_AUTHORITY = {
    "network": False,
    "secrets": False,
    "source_admission": False,
    "response_authentication": False,
    "completeness_proof": False,
    "evidence": False,
    "policy": False,
    "human_review": False,
    "lifecycle": False,
    "release": False,
    "publication": False,
    "public_use": False,
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _bad_number(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_bad_number,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except (OSError, UnicodeError, RecursionError, ValueError):
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
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:100]]


def _canonical_json(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def query_hash(candidate: Mapping[str, Any]) -> str:
    query = copy.deepcopy(candidate["query_snapshot"])
    query.pop("query_hash", None)
    return "sha256:" + hashlib.sha256(_canonical_json(query)).hexdigest()


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(_canonical_json(identity_subject(candidate))).hexdigest()


def expected_assessment_id(candidate: Mapping[str, Any]) -> str:
    return IDENTITY_PREFIX + canonical_spec_hash(candidate).removeprefix("sha256:")[:24]


def assign_identity(candidate: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(candidate))
    result["query_snapshot"]["query_hash"] = query_hash(result)
    result["spec_hash"] = canonical_spec_hash(result)
    result["assessment_id"] = expected_assessment_id(result)
    return result


def _time(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    return parsed if parsed.utcoffset() is not None and parsed.utcoffset().total_seconds() == 0 else None


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _canonical_filters(value: object) -> bool:
    if not isinstance(value, list) or not all(isinstance(item, Mapping) for item in value):
        return False
    keys = [(item.get("field"), item.get("operator"), item.get("value_digest")) for item in value]
    return all(all(isinstance(part, str) for part in key) for key in keys) and keys == sorted(set(keys))


def expected_deviations(candidate: Mapping[str, Any]) -> list[str]:
    intent = candidate.get("retrieval_intent")
    snapshot = candidate.get("query_snapshot")
    if not isinstance(intent, Mapping) or not isinstance(snapshot, Mapping):
        return []
    deviations: list[str] = []
    for field, code in DEVIATION_FIELDS:
        planned = intent.get(field)
        executed = snapshot.get(field)
        if field == "pagination" and isinstance(planned, Mapping) and isinstance(executed, Mapping):
            planned = planned.get("mode")
            executed = executed.get("mode")
        if planned != executed:
            deviations.append(code)
    return sorted(deviations)


def expected_receipt_outcome(candidate: Mapping[str, Any]) -> str:
    if expected_deviations(candidate):
        return "CHANGED_QUERY"
    snapshot = candidate.get("query_snapshot")
    if not isinstance(snapshot, Mapping):
        return "FAILED"
    if snapshot.get("execution_state") == "FAILED":
        return "FAILED"
    pagination = snapshot.get("pagination")
    if snapshot.get("execution_state") == "PARTIAL" or not isinstance(pagination, Mapping) or pagination.get("complete") is not True:
        return "INCOMPLETE"
    return "MATCHED_COMPLETE"


def expected_result_interpretation(candidate: Mapping[str, Any]) -> str:
    outcome = expected_receipt_outcome(candidate)
    if outcome == "CHANGED_QUERY":
        return "CHANGED_QUERY_NOT_ACCEPTED"
    if outcome == "FAILED":
        return "RETRIEVAL_FAILED_NO_CLAIM"
    if outcome == "INCOMPLETE":
        return "RESULT_INCOMPLETE_NO_CLAIM"
    return "ZERO_RECORDS_NO_CLAIM" if candidate["query_snapshot"].get("result_count") == 0 else "RESULT_SET_RECORDED"


def _scope_findings(scope: object, path: str, *, temporal: bool = False) -> list[Finding]:
    findings: list[Finding] = []
    if not isinstance(scope, Mapping):
        return findings
    if not temporal:
        mode = scope.get("mode")
        digest = scope.get("value_digest")
        if mode in {"WHOLE_SOURCE", "NOT_APPLICABLE"} and digest is not None:
            findings.append(Finding("GEOGRAPHIC_SCOPE_DIGEST_UNEXPECTED", path + "/value_digest"))
        if mode in {"ADMIN_AREA", "BOUNDING_BOX", "FEATURE_SET"} and digest is None:
            findings.append(Finding("GEOGRAPHIC_SCOPE_DIGEST_REQUIRED", path + "/value_digest"))
        return findings

    mode = scope.get("mode")
    semantics = scope.get("semantics")
    start = _time(scope.get("start"))
    end = _time(scope.get("end"))
    if mode in {"ALL_AVAILABLE", "NOT_APPLICABLE"} and (start is not None or end is not None):
        findings.append(Finding("TEMPORAL_BOUNDS_UNEXPECTED", path))
    if mode == "INTERVAL" and (start is None or end is None or end < start):
        findings.append(Finding("TEMPORAL_INTERVAL_INVALID", path))
    if mode == "AS_OF" and (start is not None or end is None):
        findings.append(Finding("TEMPORAL_AS_OF_INVALID", path))
    if (mode == "NOT_APPLICABLE") != (semantics == "NOT_APPLICABLE"):
        findings.append(Finding("TEMPORAL_SEMANTICS_INCOHERENT", path + "/semantics"))
    return findings


def _assessment_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: set[Finding] = set()
    intent = candidate.get("retrieval_intent")
    snapshot = candidate.get("query_snapshot")
    receipt = candidate.get("retrieval_receipt")
    if not isinstance(intent, Mapping) or not isinstance(snapshot, Mapping) or not isinstance(receipt, Mapping):
        return []

    assessed = _time(candidate.get("assessed_at"))
    started = _time(receipt.get("started_at"))
    finished = _time(receipt.get("finished_at"))
    if assessed is None or started is None or finished is None or not (started <= finished <= assessed):
        findings.add(Finding("RETRIEVAL_TIME_ORDER_INVALID", "/retrieval_receipt"))

    for owner, value in (("retrieval_intent", intent), ("query_snapshot", snapshot)):
        if not _canonical_strings(value.get("requested_fields")):
            findings.add(Finding("REQUESTED_FIELDS_NOT_CANONICAL", f"/{owner}/requested_fields"))
        if not _canonical_strings(value.get("exclusions")):
            findings.add(Finding("EXCLUSIONS_NOT_CANONICAL", f"/{owner}/exclusions"))
        if not _canonical_filters(value.get("filters")):
            findings.add(Finding("FILTERS_NOT_CANONICAL", f"/{owner}/filters"))
        findings.update(_scope_findings(value.get("geographic_scope"), f"/{owner}/geographic_scope"))
        findings.update(_scope_findings(value.get("temporal_scope"), f"/{owner}/temporal_scope", temporal=True))
        sampling = value.get("sampling")
        if isinstance(sampling, Mapping):
            if sampling.get("mode") == "NOT_APPLICABLE" and sampling.get("profile_ref") is not None:
                findings.add(Finding("SAMPLING_REFERENCE_UNEXPECTED", f"/{owner}/sampling/profile_ref"))
            if sampling.get("mode") not in {"COMPLETE", "NOT_APPLICABLE"} and sampling.get("profile_ref") is None:
                findings.add(Finding("SAMPLING_REFERENCE_REQUIRED", f"/{owner}/sampling/profile_ref"))

    planned_pagination = intent.get("pagination")
    if isinstance(planned_pagination, Mapping):
        if planned_pagination.get("mode") == "NONE" and planned_pagination.get("planned_unit_count") is not None:
            findings.add(Finding("PLANNED_UNIT_COUNT_UNEXPECTED", "/retrieval_intent/pagination/planned_unit_count"))

    execution_state = snapshot.get("execution_state")
    response_digest = snapshot.get("response_digest")
    result_count = snapshot.get("result_count")
    pagination = snapshot.get("pagination")
    pagination_complete = pagination.get("complete") if isinstance(pagination, Mapping) else None
    if execution_state == "COMPLETE":
        if response_digest is None:
            findings.add(Finding("COMPLETE_RESPONSE_DIGEST_REQUIRED", "/query_snapshot/response_digest"))
        if result_count is None:
            findings.add(Finding("COMPLETE_RESULT_COUNT_REQUIRED", "/query_snapshot/result_count"))
        if pagination_complete is not True:
            findings.add(Finding("COMPLETE_PAGINATION_REQUIRED", "/query_snapshot/pagination/complete"))
    elif execution_state == "PARTIAL":
        if pagination_complete is not False:
            findings.add(Finding("PARTIAL_PAGINATION_MUST_BE_OPEN", "/query_snapshot/pagination/complete"))
        else:
            findings.add(Finding("EXECUTION_INCOMPLETE", "/query_snapshot/execution_state"))
    elif execution_state == "FAILED":
        if response_digest is not None or result_count is not None:
            findings.add(Finding("FAILED_RESULT_MUST_BE_ABSENT", "/query_snapshot"))
        if pagination_complete is not False:
            findings.add(Finding("FAILED_PAGINATION_MUST_BE_OPEN", "/query_snapshot/pagination/complete"))
        if response_digest is None and result_count is None and pagination_complete is False:
            findings.add(Finding("RETRIEVAL_FAILED", "/query_snapshot/execution_state"))

    deviations = expected_deviations(candidate)
    for code in deviations:
        field = next(field for field, candidate_code in DEVIATION_FIELDS if candidate_code == code)
        findings.add(Finding(code, f"/query_snapshot/{field}"))
    if receipt.get("deviation_codes") != deviations:
        findings.add(Finding("DEVIATION_CODES_MISMATCH", "/retrieval_receipt/deviation_codes"))
    expected_outcome = expected_receipt_outcome(candidate)
    if receipt.get("outcome") != expected_outcome:
        findings.add(Finding("RECEIPT_OUTCOME_MISMATCH", "/retrieval_receipt/outcome"))
    if receipt.get("pagination_complete") != pagination_complete:
        findings.add(Finding("RECEIPT_PAGINATION_MISMATCH", "/retrieval_receipt/pagination_complete"))
    if receipt.get("result_interpretation") != expected_result_interpretation(candidate):
        findings.add(Finding("RESULT_INTERPRETATION_MISMATCH", "/retrieval_receipt/result_interpretation"))
    return sorted(findings)


def _recommendation(findings: Sequence[Finding], candidate: Mapping[str, Any]) -> str:
    outcome = expected_receipt_outcome(candidate)
    non_status = [finding for finding in findings if finding.code not in ABSTAIN_CODES]
    if non_status or outcome == "CHANGED_QUERY":
        return "DENY"
    if outcome in {"INCOMPLETE", "FAILED"}:
        return "HOLD"
    return "READY_FOR_REVIEW"


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if findings:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))

    findings = _assessment_findings(candidate)
    decision = candidate.get("decision")
    recommendation = decision.get("recommendation") if isinstance(decision, Mapping) else None
    if recommendation != _recommendation(findings, candidate):
        findings.append(Finding("RECOMMENDATION_MISMATCH", "/decision/recommendation"))
    if candidate.get("query_snapshot", {}).get("query_hash") != query_hash(candidate):
        findings.append(Finding("QUERY_HASH_MISMATCH", "/query_snapshot/query_hash"))
    if candidate.get("spec_hash") != canonical_spec_hash(candidate):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    if candidate.get("assessment_id") != expected_assessment_id(candidate):
        findings.append(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))

    ordered = tuple(sorted(set(findings)))
    if not ordered:
        return ValidationResult("PASS", ordered)
    if any(finding.code in ERROR_CODES or finding.code == "QUERY_HASH_MISMATCH" for finding in ordered):
        return ValidationResult("ERROR", ordered)
    if all(finding.code in ABSTAIN_CODES for finding in ordered):
        return ValidationResult("ABSTAIN", ordered)
    return ValidationResult("DENY", ordered)


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _set(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.lstrip("/").split("/") if part]
    current: Any = candidate
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    if not parts:
        raise ValueError("root replacement is not supported")
    leaf = parts[-1]
    if isinstance(current, list):
        current[int(leaf)] = copy.deepcopy(value)
    else:
        current[leaf] = copy.deepcopy(value)


def _fixture_document(path: Path = CASES) -> dict[str, Any]:
    document, findings = _read(path)
    if (
        document is None
        or findings
        or document.get("profile") != "kfm.source.retrieval-intent-query-snapshot-assessment-fixtures.v1"
        or document.get("source_idea_ids") != SOURCE_IDEAS
        or not isinstance(document.get("base"), dict)
        or not isinstance(document.get("cases"), list)
    ):
        raise ValueError("invalid fixture manifest")
    return document


def _derive_receipt(candidate: dict[str, Any]) -> None:
    receipt = candidate["retrieval_receipt"]
    receipt["deviation_codes"] = expected_deviations(candidate)
    receipt["outcome"] = expected_receipt_outcome(candidate)
    receipt["pagination_complete"] = candidate["query_snapshot"]["pagination"]["complete"]
    receipt["result_interpretation"] = expected_result_interpretation(candidate)


def materialize_case(document: Mapping[str, Any], definition: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(document["base"])
    for mutation in definition.get("mutations", []):
        _set(candidate, mutation["path"], mutation["value"])
    _derive_receipt(candidate)
    receipt_mode = definition.get("receipt_mode", "DERIVE")
    if receipt_mode == "MISMATCH_OUTCOME":
        candidate["retrieval_receipt"]["outcome"] = "FAILED"
    elif receipt_mode == "MISMATCH_DEVIATIONS":
        candidate["retrieval_receipt"]["deviation_codes"] = []
    elif receipt_mode == "MISMATCH_INTERPRETATION":
        candidate["retrieval_receipt"]["result_interpretation"] = "ZERO_RECORDS_NO_CLAIM"
    elif receipt_mode == "MISMATCH_PAGINATION":
        candidate["retrieval_receipt"]["pagination_complete"] = not candidate["retrieval_receipt"]["pagination_complete"]
    elif receipt_mode != "DERIVE":
        raise ValueError("unknown receipt mode")
    findings = _assessment_findings(candidate)
    candidate["decision"]["recommendation"] = _recommendation(findings, candidate)
    if definition.get("recommendation_mode") == "MISMATCH":
        candidate["decision"]["recommendation"] = "HOLD" if candidate["decision"]["recommendation"] != "HOLD" else "DENY"
    candidate = assign_identity(candidate)
    identity_mode = definition.get("identity_mode", "RECOMPUTE")
    if identity_mode == "MISMATCH_QUERY_HASH":
        candidate["query_snapshot"]["query_hash"] = "sha256:" + "0" * 64
        candidate["spec_hash"] = canonical_spec_hash(candidate)
        candidate["assessment_id"] = expected_assessment_id(candidate)
    elif identity_mode == "MISMATCH_SPEC_HASH":
        candidate["spec_hash"] = "sha256:" + "0" * 64
    elif identity_mode == "MISMATCH_ID":
        candidate["assessment_id"] = IDENTITY_PREFIX + "0" * 24
    elif identity_mode != "RECOMPUTE":
        raise ValueError("unknown identity mode")
    return candidate


def load_fixture_cases(path: Path = CASES) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _fixture_document(path)
    output: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for raw in document["cases"]:
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str) or raw["name"] in names:
            raise ValueError("invalid fixture case")
        names.add(raw["name"])
        output.append((raw, materialize_case(document, raw)))
    return output


def _serialize(result: ValidationResult, *, path: Path | None = None, case: str | None = None) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        "scope": SCOPE,
        "authority": FALSE_AUTHORITY,
    }
    if path is not None:
        try:
            payload["file"] = path.resolve().relative_to(ROOT.resolve()).as_posix()
        except (OSError, ValueError):
            payload["file"] = path.name
    if case is not None:
        payload["case"] = case
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def replay_fixtures(path: Path = CASES) -> int:
    try:
        cases = load_fixture_cases(path)
    except (OSError, UnicodeError, ValueError, KeyError, TypeError):
        print(_serialize(ValidationResult("ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),))))
        return 1
    failed = False
    outcomes: set[str] = set()
    for definition, candidate in cases:
        result = validate_payload(candidate)
        actual = {
            "outcome": result.outcome,
            "findings": [{"code": finding.code, "path": finding.path} for finding in result.findings],
        }
        expected = {"outcome": definition["expected_outcome"], "findings": definition["expected_findings"]}
        print(_serialize(result, case=definition["name"]))
        failed |= actual != expected
        outcomes.add(result.outcome)
    failed |= outcomes != {"PASS", "ABSTAIN", "DENY", "ERROR"}
    if not failed:
        print(f"CONFIRMED: {len(cases)} retrieval intent/query snapshot cases passed exact polarity.")
    return 1 if failed else 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.print_usage()
            return 2
        return replay_fixtures()
    if not args.files:
        parser.print_usage()
        return 2
    failed = False
    for path in args.files:
        result = validate_file(path)
        print(_serialize(result, path=path))
        failed |= not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
