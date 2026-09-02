#!/usr/bin/env python3
"""Validate fixture-only DriftRegisterTriageAssessment candidates.

The validator checks caller-supplied synthetic declarations only. It never
reads or mutates the human drift register and never inspects affected paths or
resolves opaque refs.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / "schemas/contracts/v1/governance/drift_register_triage_assessment.schema.json"
FIXTURE_DIR = ROOT / "fixtures/contracts/v1/governance/drift_register_triage_assessment"
VALID_FIXTURE = FIXTURE_DIR / "valid.json"
CASES = FIXTURE_DIR / "cases.json"
IDENTITY_PREFIX = "kfm:drift-register-triage:"
MAX_BYTES = 1_048_576
MAX_FINDINGS = 100
ACTIVE_STATES = {"OPEN", "ACKNOWLEDGED", "BLOCKED_ADR", "CORRECTION_IN_PROGRESS"}
TERMINAL_STATES = {"RESOLVED", "WITHDRAWN"}
NON_EFFECTS = (
    "no_register_mutation",
    "no_path_inspection",
    "no_owner_assignment",
    "no_adr_approval",
    "no_correction_execution",
    "no_resolution_approval",
    "no_promotion",
    "no_release",
    "no_publication",
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _contains_surrogate(value: object) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if isinstance(value, Mapping):
        return any(_contains_surrogate(key) or _contains_surrogate(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


def read_json_object(path: Path) -> tuple[dict[str, object] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ROOT_NOT_OBJECT", "/"),)
    if _contains_surrogate(value):
        return None, (Finding("JSON_UNPAIRED_SURROGATE", "/"),)
    return value, ()


def canonical_bytes(value: object) -> bytes:
    if _contains_surrogate(value):
        raise UnicodeError("unpaired surrogate")
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def expected_id(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    return IDENTITY_PREFIX + hashlib.sha256(canonical_bytes(subject)).hexdigest()


def _pointer(parts: Iterable[object]) -> str:
    escaped = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(escaped) if escaped else "/"


def _schema_findings(candidate: object) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
                MAX_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, SchemaError):
        return (Finding("SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:MAX_FINDINGS]]
    if len(errors) > MAX_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _utc_time(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None


def _safe_relative_path(value: str) -> bool:
    if value.startswith("/") or "\\" in value or "//" in value:
        return False
    raw_parts = value.split("/")
    if any(part in {"", ".", ".."} for part in raw_parts):
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and path.as_posix() == value


def _semantic_findings(candidate: Mapping[str, object]) -> tuple[set[Finding], set[Finding]]:
    deny: set[Finding] = set()
    abstain: set[Finding] = set()
    entries = candidate["entries"]
    review = candidate["review"]
    effects = candidate["effects"]
    assert isinstance(entries, list) and isinstance(review, Mapping) and isinstance(effects, Mapping)

    observed_at = _utc_time(candidate["observed_at"])
    if observed_at is None:
        deny.add(Finding("OBSERVED_AT_NOT_UTC", "/observed_at"))

    typed_entries = [entry for entry in entries if isinstance(entry, Mapping)]
    ids = [str(entry["drift_id"]) for entry in typed_entries]
    if ids != sorted(set(ids)):
        deny.add(Finding("DRIFT_ENTRIES_NOT_CANONICAL", "/entries"))

    for index, entry in enumerate(typed_entries):
        state = str(entry["state"])
        owner_roles = entry["owner_roles"]
        affected_paths = entry["affected_paths"]
        evidence_refs = entry["evidence_refs"]
        for field, value in (("owner_roles", owner_roles), ("evidence_refs", evidence_refs)):
            if not _canonical_strings(value):
                deny.add(Finding("TRIAGE_ARRAY_NOT_CANONICAL", f"/entries/{index}/{field}"))
        if not _canonical_strings(affected_paths):
            deny.add(Finding("AFFECTED_PATHS_NOT_CANONICAL", f"/entries/{index}/affected_paths"))
        if isinstance(affected_paths, list):
            for path_index, value in enumerate(affected_paths):
                if isinstance(value, str) and not _safe_relative_path(value):
                    deny.add(Finding("AFFECTED_PATH_UNSAFE", f"/entries/{index}/affected_paths/{path_index}"))

        if state in ACTIVE_STATES:
            if not owner_roles:
                abstain.add(Finding("TRIAGE_OWNER_UNKNOWN", f"/entries/{index}/owner_roles"))
            if not evidence_refs:
                abstain.add(Finding("TRIAGE_EVIDENCE_UNKNOWN", f"/entries/{index}/evidence_refs"))
            next_review = _utc_time(entry["next_review_at"])
            if entry["next_review_at"] is None:
                abstain.add(Finding("NEXT_REVIEW_UNKNOWN", f"/entries/{index}/next_review_at"))
            elif next_review is None:
                deny.add(Finding("NEXT_REVIEW_NOT_UTC", f"/entries/{index}/next_review_at"))
            elif observed_at is not None and next_review <= observed_at:
                deny.add(Finding("NEXT_REVIEW_NOT_FUTURE", f"/entries/{index}/next_review_at"))

        if state == "OPEN":
            for field in ("candidate_adr_ref", "correction_ref", "resolution_ref", "rollback_ref"):
                if entry[field] is not None:
                    deny.add(Finding("OPEN_REMEDIATION_REFERENCE_FORBIDDEN", f"/entries/{index}/{field}"))
        elif state == "BLOCKED_ADR":
            if entry["candidate_adr_ref"] is None:
                deny.add(Finding("BLOCKED_ADR_REFERENCE_REQUIRED", f"/entries/{index}/candidate_adr_ref"))
            for field in ("correction_ref", "resolution_ref", "rollback_ref"):
                if entry[field] is not None:
                    deny.add(Finding("BLOCKED_ADR_REMEDIATION_FORBIDDEN", f"/entries/{index}/{field}"))
        elif state == "CORRECTION_IN_PROGRESS":
            if entry["correction_ref"] is None:
                deny.add(Finding("CORRECTION_REFERENCE_REQUIRED", f"/entries/{index}/correction_ref"))
            if entry["rollback_ref"] is None:
                deny.add(Finding("ROLLBACK_REFERENCE_REQUIRED", f"/entries/{index}/rollback_ref"))
            if entry["resolution_ref"] is not None:
                deny.add(Finding("IN_PROGRESS_RESOLUTION_FORBIDDEN", f"/entries/{index}/resolution_ref"))

        if state in TERMINAL_STATES:
            if not evidence_refs:
                deny.add(Finding("TERMINAL_EVIDENCE_REQUIRED", f"/entries/{index}/evidence_refs"))
            if entry["next_review_at"] is not None:
                deny.add(Finding("TERMINAL_NEXT_REVIEW_FORBIDDEN", f"/entries/{index}/next_review_at"))
            if entry["resolution_ref"] is None:
                deny.add(Finding("RESOLUTION_REFERENCE_REQUIRED", f"/entries/{index}/resolution_ref"))
        if state == "RESOLVED":
            if entry["correction_ref"] is None:
                deny.add(Finding("RESOLVED_CORRECTION_REQUIRED", f"/entries/{index}/correction_ref"))
            if entry["rollback_ref"] is None:
                deny.add(Finding("RESOLVED_ROLLBACK_REQUIRED", f"/entries/{index}/rollback_ref"))

    review_refs = review["record_refs"]
    if not _canonical_strings(review_refs):
        deny.add(Finding("REVIEW_RECORDS_NOT_CANONICAL", "/review/record_refs"))
    if review["state"] == "COMPLETE" and not review_refs:
        deny.add(Finding("REVIEW_RECORD_REQUIRED", "/review/record_refs"))
    elif review["state"] == "PENDING":
        abstain.add(Finding("REVIEW_PENDING", "/review/state"))
    elif review["state"] == "UNKNOWN":
        abstain.add(Finding("REVIEW_UNKNOWN", "/review/state"))

    if any(value is not False for value in effects.values()):
        deny.add(Finding("AUTHORITY_OVERREACH", "/effects"))
    return deny, abstain


def validate_candidate(candidate: object) -> Result:
    if not isinstance(candidate, Mapping):
        return Result("ERROR", (Finding("ROOT_NOT_OBJECT", "/"),))
    if _contains_surrogate(candidate):
        return Result("ERROR", (Finding("JSON_UNPAIRED_SURROGATE", "/"),))
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return Result("ERROR", schema_findings)
    try:
        identity = expected_id(candidate)
    except (TypeError, ValueError, UnicodeError, RecursionError):
        return Result("ERROR", (Finding("CANONICALIZATION_ERROR", "/"),))
    if candidate["assessment_id"] != identity:
        return Result("ERROR", (Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"),))
    deny, abstain = _semantic_findings(candidate)
    if deny:
        return Result("DENY", tuple(sorted(deny)))
    if abstain:
        return Result("ABSTAIN", tuple(sorted(abstain)))
    return Result("PASS", ())


def _replace(document: object, pointer: str, value: object) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]  # type: ignore[index]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(value)
    else:
        target[key] = copy.deepcopy(value)  # type: ignore[index]


def materialize_case(base: Mapping[str, object], case: Mapping[str, object]) -> dict[str, object]:
    candidate = copy.deepcopy(dict(base))
    for mutation in case.get("mutations", []):
        assert isinstance(mutation, Mapping)
        _replace(candidate, str(mutation["path"]), mutation.get("value"))
    if not case.get("preserve_identity", False):
        candidate["assessment_id"] = expected_id(candidate)
    return candidate


def _finding_records(result: Result) -> list[dict[str, str]]:
    return [{"code": finding.code, "path": finding.path} for finding in result.findings]


def validate_fixture_matrix() -> list[dict[str, object]]:
    base = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    for case in cases:
        result = validate_candidate(materialize_case(base, case))
        findings = _finding_records(result)
        results.append(
            {
                "name": case["name"],
                "outcome": result.outcome,
                "findings": findings,
                "suite_match": result.outcome == case["expected_outcome"]
                and findings == case["expected_findings"],
            }
        )
    return results


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": _finding_records(result),
            "non_effects": NON_EFFECTS,
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixtures() -> int:
    results = validate_fixture_matrix()
    for result in results:
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if all(result["suite_match"] for result in results) else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    candidate, findings = read_json_object(args.input)
    result = Result("ERROR", findings) if candidate is None else validate_candidate(candidate)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
