"""Validate fixture-only analytical query cost profiles.

This validator checks closed shape, deterministic identity, safe plan metadata,
input and index assumptions, resource budgets, measured observations, and
disclosure posture. It never executes a query, reads a database catalog,
authenticates telemetry, decides policy or review, or grants release authority.
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

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/analytical_query_cost_profile.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/analytical_query_cost_profile/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "COST_POSTURE_UNRESOLVED",
    "DISCLOSURE_INCOMPLETE",
    "DISCLOSURE_UNKNOWN",
    "ENGINE_UNRESOLVED",
    "INDEX_ASSUMPTIONS_UNRESOLVED",
    "INPUT_SCOPE_UNRESOLVED",
    "OBSERVATION_NOT_RUN",
    "OBSERVATION_UNRESOLVED",
    "PLAN_CAPTURE_MISSING",
    "PLAN_CAPTURE_UNRESOLVED",
    "PORTABILITY_UNRESOLVED",
}
BUDGET_TO_OBSERVATION = {
    "max_duration_ms": "duration_ms",
    "max_rows_read": "rows_read",
    "max_bytes_read": "bytes_read",
    "max_peak_memory_bytes": "peak_memory_bytes",
}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


class UnpairedSurrogateError(ValueError):
    """Raised when text cannot be represented as Unicode scalar values."""


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


def _contains_surrogate(value: object) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if isinstance(value, Mapping):
        return any(_contains_surrogate(key) or _contains_surrogate(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


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
    if _contains_surrogate(value):
        return None, [Finding("JSON_UNPAIRED_SURROGATE", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    if _contains_surrogate(value):
        raise UnpairedSurrogateError
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


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
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
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _engine_findings(engine: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    kind = engine.get("kind")
    profile_ref = engine.get("profile_ref")
    portability = engine.get("portability")
    if kind == "UNRESOLVED":
        findings.add(Finding("ENGINE_UNRESOLVED", "/engine/kind"))
        if profile_ref is not None:
            findings.add(Finding("ENGINE_PROFILE_INCOHERENT", "/engine/profile_ref"))
    elif profile_ref is None:
        findings.add(Finding("ENGINE_PROFILE_REQUIRED", "/engine/profile_ref"))
    if portability == "UNRESOLVED":
        findings.add(Finding("PORTABILITY_UNRESOLVED", "/engine/portability"))
    return findings


def _input_findings(input_scope: Mapping[str, object], budget: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    if not _canonical_strings(input_scope.get("dataset_refs")):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/input_scope/dataset_refs"))
    if input_scope.get("basis") == "UNRESOLVED":
        findings.add(Finding("INPUT_SCOPE_UNRESOLVED", "/input_scope/basis"))
    elif input_scope.get("estimated_rows") is None and input_scope.get("estimated_bytes") is None:
        findings.add(Finding("INPUT_SIZE_REQUIRED", "/input_scope"))
    if (
        input_scope.get("estimated_rows") is not None
        and budget.get("max_rows_read") is not None
        and input_scope["estimated_rows"] > budget["max_rows_read"]
    ):
        findings.add(Finding("INPUT_ESTIMATE_EXCEEDS_BUDGET", "/input_scope/estimated_rows"))
    if (
        input_scope.get("estimated_bytes") is not None
        and budget.get("max_bytes_read") is not None
        and input_scope["estimated_bytes"] > budget["max_bytes_read"]
    ):
        findings.add(Finding("INPUT_ESTIMATE_EXCEEDS_BUDGET", "/input_scope/estimated_bytes"))
    return findings


def _plan_findings(plan: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    if not _canonical_strings(plan.get("parameter_names")):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/plan_capture/parameter_names"))
    state = plan.get("state")
    captured = plan.get("format") != "NONE" and plan.get("plan_digest") is not None
    if state == "CAPTURED" and not captured:
        findings.add(Finding("PLAN_CAPTURE_INCOHERENT", "/plan_capture"))
    elif state == "NOT_CAPTURED":
        findings.add(Finding("PLAN_CAPTURE_MISSING", "/plan_capture/state"))
        if plan.get("format") != "NONE" or plan.get("plan_digest") is not None:
            findings.add(Finding("PLAN_CAPTURE_INCOHERENT", "/plan_capture"))
    elif state == "UNRESOLVED":
        findings.add(Finding("PLAN_CAPTURE_UNRESOLVED", "/plan_capture/state"))
        if plan.get("format") != "NONE" or plan.get("plan_digest") is not None:
            findings.add(Finding("PLAN_CAPTURE_INCOHERENT", "/plan_capture"))
    return findings


def _index_findings(section: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    items = section.get("items")
    assert isinstance(items, list)
    names = [item.get("logical_name") for item in items if isinstance(item, Mapping)]
    if names != sorted(set(names)):
        findings.add(Finding("INDEX_ITEMS_NOT_CANONICAL", "/index_assumptions/items"))
    for index, item in enumerate(items):
        assert isinstance(item, Mapping)
        if not _canonical_strings(item.get("field_names")):
            findings.add(Finding("ARRAY_NOT_CANONICAL", f"/index_assumptions/items/{index}/field_names"))
    state = section.get("state")
    if state == "DECLARED" and not items:
        findings.add(Finding("INDEX_STATE_INCOHERENT", "/index_assumptions"))
    elif state == "NONE" and items:
        findings.add(Finding("INDEX_STATE_INCOHERENT", "/index_assumptions"))
    elif state == "UNRESOLVED":
        findings.add(Finding("INDEX_ASSUMPTIONS_UNRESOLVED", "/index_assumptions/state"))
        if items:
            findings.add(Finding("INDEX_STATE_INCOHERENT", "/index_assumptions"))
    return findings


def _budget_findings(budget: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    posture = budget.get("cost_posture")
    billing_ref = budget.get("billing_profile_ref")
    if posture == "RESOURCE_BUDGET_ONLY" and billing_ref is not None:
        findings.add(Finding("BILLING_PROFILE_INCOHERENT", "/budget/billing_profile_ref"))
    elif posture == "BILLING_PROFILE_REFERENCED" and billing_ref is None:
        findings.add(Finding("BILLING_PROFILE_REQUIRED", "/budget/billing_profile_ref"))
    elif posture == "UNRESOLVED":
        findings.add(Finding("COST_POSTURE_UNRESOLVED", "/budget/cost_posture"))
        if billing_ref is not None:
            findings.add(Finding("BILLING_PROFILE_INCOHERENT", "/budget/billing_profile_ref"))
    return findings


def _observation_findings(
    budget: Mapping[str, object], observation: Mapping[str, object]
) -> set[Finding]:
    findings: set[Finding] = set()
    state = observation.get("state")
    measurements = [observation.get(field) for field in BUDGET_TO_OBSERVATION.values()]
    if state == "NOT_RUN":
        findings.add(Finding("OBSERVATION_NOT_RUN", "/observation/state"))
        expected_result = "NOT_RUN"
        if any(value is not None for value in measurements):
            findings.add(Finding("OBSERVATION_STATE_INCOHERENT", "/observation"))
    elif state == "UNRESOLVED":
        findings.add(Finding("OBSERVATION_UNRESOLVED", "/observation/state"))
        expected_result = "UNRESOLVED"
        if any(value is not None for value in measurements):
            findings.add(Finding("OBSERVATION_STATE_INCOHERENT", "/observation"))
    elif state == "ERROR":
        findings.add(Finding("OBSERVATION_RECORDED_ERROR", "/observation/state"))
        expected_result = "ERROR"
        if any(value is not None for value in measurements):
            findings.add(Finding("OBSERVATION_STATE_INCOHERENT", "/observation"))
    else:
        exceeded = False
        for limit_field, observed_field in BUDGET_TO_OBSERVATION.items():
            limit = budget.get(limit_field)
            observed = observation.get(observed_field)
            if limit is not None and observed is None:
                findings.add(Finding("OBSERVATION_INCOMPLETE", f"/observation/{observed_field}"))
            elif limit is not None and observed is not None and observed > limit:
                exceeded = True
        if observation.get("run_receipt_ref") is None:
            findings.add(Finding("MEASUREMENT_RECEIPT_REQUIRED", "/observation/run_receipt_ref"))
        expected_result = "EXCEEDED" if exceeded else "WITHIN_BUDGET"
        if exceeded:
            findings.add(Finding("BUDGET_EXCEEDED", "/observation/budget_result"))
    if observation.get("budget_result") != expected_result:
        findings.add(Finding("BUDGET_RESULT_MISMATCH", "/observation/budget_result"))
    return findings


def _disclosure_findings(disclosure: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    if not _canonical_strings(disclosure.get("review_record_refs")):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/disclosure/review_record_refs"))
    state = disclosure.get("state")
    if state == "INCOMPLETE":
        findings.add(Finding("DISCLOSURE_INCOMPLETE", "/disclosure/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("DISCLOSURE_UNKNOWN", "/disclosure/state"))
    elif disclosure.get("summary") is None:
        findings.add(Finding("DISCLOSURE_SUMMARY_REQUIRED", "/disclosure/summary"))
    if disclosure.get("intended_use") == "PUBLIC_CANDIDATE" and not disclosure.get("review_record_refs"):
        findings.add(Finding("PUBLIC_DISCLOSURE_REVIEW_REQUIRED", "/disclosure/review_record_refs"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    engine = candidate["engine"]
    input_scope = candidate["input_scope"]
    plan = candidate["plan_capture"]
    indexes = candidate["index_assumptions"]
    budget = candidate["budget"]
    observation = candidate["observation"]
    disclosure = candidate["disclosure"]
    assert all(
        isinstance(value, Mapping)
        for value in (engine, input_scope, plan, indexes, budget, observation, disclosure)
    )
    findings.update(_engine_findings(engine))
    findings.update(_input_findings(input_scope, budget))
    findings.update(_plan_findings(plan))
    findings.update(_index_findings(indexes))
    findings.update(_budget_findings(budget))
    findings.update(_observation_findings(budget, observation))
    findings.update(_disclosure_findings(disclosure))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    if _contains_surrogate(candidate):
        return ValidationResult("ERROR", (Finding("JSON_UNPAIRED_SURROGATE", "/"),))
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif "OBSERVATION_RECORDED_ERROR" in codes:
        outcome = "ERROR"
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
        target[key] = None if value is None else _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {
                "outcome": "ERROR",
                "codes": sorted({item.code for item in load_findings}),
            },
        }]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({
            "name": entry["name"],
            "ok": observed == expected,
            "expected": expected,
            "observed": observed,
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only analytical query cost profiles."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
