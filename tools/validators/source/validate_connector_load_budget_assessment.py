"""Validate fixture-only connector load-budget assessments.

The validator compares declared execution demand with one declared per-source
budget. It performs no network request, retry, sleep, scheduling, connector
execution, source activation, lifecycle write, policy decision, or publication.
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
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/connector_load_budget_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/source/connector_load_budget_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "CONDUCT_ASSESSMENT_UNRESOLVED",
    "LOAD_BUDGET_UNRESOLVED",
    "REVIEW_PENDING",
    "REVIEW_UNKNOWN",
    "SOURCE_POLICY_RESOLUTION_REQUIRED",
}
REQUIRED_STOP_CONDITIONS = {
    "BUDGET_EXHAUSTED",
    "MANUAL_CANCEL",
    "SOURCE_THROTTLE",
    "TERMS_CHANGE",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (tuple(str(part) for part in error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path))
        for error in errors[:100]
    ]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _conduct_findings(value: Mapping[str, object]) -> set[Finding]:
    outcome = value["outcome"]
    if outcome in {"ABSTAIN", "UNRESOLVED"}:
        return {Finding("CONDUCT_ASSESSMENT_UNRESOLVED", "/conduct_assessment/outcome")}
    if outcome == "DENY":
        return {Finding("CONDUCT_ASSESSMENT_DENIED", "/conduct_assessment/outcome")}
    return set()


def _execution_findings(execution: Mapping[str, object], budget: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    mode = execution["mode"]
    workers = execution["worker_count"]
    requested = execution["requested_concurrency"]
    share_key = budget["distributed_share_key"]
    if requested > workers:
        findings.add(Finding("REQUESTED_CONCURRENCY_EXCEEDS_WORKERS", "/execution/requested_concurrency"))
    if mode == "SINGLE_WORKER":
        if workers != 1 or requested != 1:
            findings.add(Finding("EXECUTION_MODE_INCOHERENT", "/execution"))
    elif workers < 2 or requested < 2:
        findings.add(Finding("EXECUTION_MODE_INCOHERENT", "/execution"))
    if mode == "DISTRIBUTED":
        if share_key is None:
            findings.add(Finding("DISTRIBUTED_SHARE_KEY_REQUIRED", "/budget/distributed_share_key"))
    elif share_key is not None:
        findings.add(Finding("DISTRIBUTED_SHARE_KEY_UNEXPECTED", "/budget/distributed_share_key"))
    return findings


def _retry_findings(retry: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    strategy = retry["strategy"]
    attempts = retry["max_attempts"]
    base = retry["base_delay_ms"]
    cap = retry["cap_delay_ms"]
    if not retry["honor_retry_after"]:
        findings.add(Finding("RETRY_AFTER_MUST_BE_HONORED", "/budget/retry/honor_retry_after"))
    if strategy == "NONE":
        if attempts != 0 or base != 0 or cap != 0:
            findings.add(Finding("RETRY_DECLARATION_INCOHERENT", "/budget/retry"))
    else:
        if attempts < 1 or base < 1 or cap < base:
            findings.add(Finding("RETRY_BACKOFF_INCOHERENT", "/budget/retry"))
    return findings


def _budget_findings(execution: Mapping[str, object], budget: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    state = budget["state"]
    detail_fields = (
        budget["max_concurrency"],
        budget["minimum_delay_ms"],
        budget["window_seconds"],
        budget["max_requests_per_window"],
        budget["retry"],
    )
    if state == "UNRESOLVED":
        findings.add(Finding("LOAD_BUDGET_UNRESOLVED", "/budget/state"))
        if budget["policy_ref"] is not None or budget["scope"] != "UNRESOLVED" or any(item is not None for item in detail_fields) or budget["stop_conditions"]:
            findings.add(Finding("UNRESOLVED_BUDGET_INCOHERENT", "/budget"))
        return findings
    if state == "SOURCE_POLICY":
        findings.add(Finding("SOURCE_POLICY_RESOLUTION_REQUIRED", "/budget/state"))
        if budget["policy_ref"] is None or budget["scope"] != "UNRESOLVED" or any(item is not None for item in detail_fields) or budget["stop_conditions"]:
            findings.add(Finding("SOURCE_POLICY_DECLARATION_INCOHERENT", "/budget"))
        return findings

    if budget["policy_ref"] is None or budget["scope"] == "UNRESOLVED" or any(item is None for item in detail_fields):
        findings.add(Finding("DECLARED_BUDGET_INCOHERENT", "/budget"))
        return findings
    if budget["scope"] != "PER_SOURCE":
        findings.add(Finding("PER_SOURCE_SCOPE_REQUIRED", "/budget/scope"))
    maximum = budget["max_concurrency"]
    assert isinstance(maximum, int)
    if execution["requested_concurrency"] > maximum:
        findings.add(Finding("REQUESTED_CONCURRENCY_EXCEEDS_BUDGET", "/execution/requested_concurrency"))
    retry = budget["retry"]
    assert isinstance(retry, Mapping)
    findings.update(_retry_findings(retry))
    stops = budget["stop_conditions"]
    if not _canonical_strings(stops):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/budget/stop_conditions"))
    if not REQUIRED_STOP_CONDITIONS.issubset(set(stops)):
        findings.add(Finding("REQUIRED_STOP_CONDITION_MISSING", "/budget/stop_conditions"))
    return findings


def _review_findings(review: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    refs = review["review_record_refs"]
    if not _canonical_strings(refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/review/review_record_refs"))
    state = review["state"]
    if state == "COMPLETE" and not refs:
        findings.add(Finding("COMPLETE_REVIEW_REFERENCE_REQUIRED", "/review/review_record_refs"))
    elif state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/review/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/review/state"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate["profile_spec_hash"] != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate["observed_at"]):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))
    conduct = candidate["conduct_assessment"]
    execution = candidate["execution"]
    budget = candidate["budget"]
    review = candidate["review"]
    assert all(isinstance(item, Mapping) for item in (conduct, execution, budget, review))
    findings.update(_conduct_findings(conduct))
    findings.update(_execution_findings(execution, budget))
    findings.update(_budget_findings(execution, budget))
    findings.update(_review_findings(review))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{"name": "fixture_manifest", "ok": False, "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})}}]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({"name": entry["name"], "ok": observed == expected, "expected": expected, "observed": observed})
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only connector load-budget assessments.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = ValidationResult("ERROR", tuple(sorted(findings))) if candidate is None else validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
