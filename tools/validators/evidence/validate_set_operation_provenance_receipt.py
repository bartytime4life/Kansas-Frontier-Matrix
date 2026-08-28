"""Validate fixture-only set-operation provenance receipt candidates.

The validator checks declaration coherence and safe row-count bounds only. It
does not execute a query, inspect records, infer cross-engine equivalence,
resolve evidence, decide policy or review, catalog, release, or publish.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/set_operation_provenance_receipt.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/set_operation_provenance_receipt/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"EXECUTION_INCOMPLETE", "REFERENCE_UNRESOLVED"}
EXPECTED_LIMITATIONS = [
    "DECLARATION_ONLY",
    "NO_EVIDENCE_RESOLUTION",
    "NO_PUBLICATION_AUTHORITY",
    "NO_QUERY_EXECUTION",
]
EXPECTED_DUPLICATE_POLICY = {
    "UNION_DISTINCT": "DISTINCT",
    "UNION_ALL": "RETAIN_ALL",
    "INTERSECT": "DISTINCT",
    "EXCEPT": "DISTINCT",
    "SYMMETRIC_DIFFERENCE": "DISTINCT",
    "CUSTOM": "CUSTOM",
}
PUBLIC_USE = "PUBLIC_CLAIM_SUPPORT_CANDIDATE"


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


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


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding(
            "SCHEMA_INVALID",
            "/" + "/".join(str(part) for part in error.absolute_path),
        )
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


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    limitations = candidate["limitations"]
    operator = candidate["operator"]
    inputs = candidate["inputs"]
    output = candidate["output"]
    evidence = candidate["evidence"]
    assert isinstance(operator, Mapping)
    assert isinstance(inputs, list)
    assert isinstance(output, Mapping)
    assert isinstance(evidence, Mapping)

    if not _canonical_strings(limitations):
        findings.add(Finding("LIMITATIONS_NOT_CANONICAL", "/limitations"))
    if limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))
    for field in ("evidence_bundle_refs", "review_record_refs"):
        if not _canonical_strings(evidence.get(field)):
            findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/evidence/{field}"))

    for field in ("null_semantics", "method_definition"):
        reference = operator[field]
        assert isinstance(reference, Mapping)
        if reference.get("resolution") == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/operator/{field}/resolution"))
    for field in ("query_plan", "reconciliation_rule"):
        reference = evidence[field]
        assert isinstance(reference, Mapping)
        if reference.get("resolution") == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/evidence/{field}/resolution"))

    input_refs: list[str] = []
    ordinals: list[int] = []
    for index, item in enumerate(inputs):
        assert isinstance(item, Mapping)
        ref = item.get("ref")
        ordinal = item.get("ordinal")
        assert isinstance(ref, str)
        assert isinstance(ordinal, int)
        input_refs.append(ref)
        ordinals.append(ordinal)
        if item.get("resolution") == "UNRESOLVED":
            findings.add(Finding("REFERENCE_UNRESOLVED", f"/inputs/{index}/resolution"))
    if input_refs != list(dict.fromkeys(input_refs)):
        findings.add(Finding("INPUT_REFERENCE_DUPLICATE", "/inputs"))
    if ordinals != list(range(len(inputs))):
        findings.add(Finding("INPUT_ORDER_NOT_CANONICAL", "/inputs"))
    if output.get("ref") in set(input_refs):
        findings.add(Finding("OUTPUT_INPUT_REFERENCE_COLLISION", "/output/ref"))

    execution_state = candidate.get("execution_state")
    if execution_state == "ERROR":
        findings.add(Finding("EXECUTION_ERROR", "/execution_state"))
        return sorted(findings)
    if execution_state == "INCOMPLETE":
        findings.add(Finding("EXECUTION_INCOMPLETE", "/execution_state"))
        return sorted(findings)

    operation_type = operator.get("operation_type")
    duplicate_policy = operator.get("duplicate_policy")
    expected_policy = EXPECTED_DUPLICATE_POLICY[str(operation_type)]
    if duplicate_policy != expected_policy:
        findings.add(Finding("DUPLICATE_POLICY_MISMATCH", "/operator/duplicate_policy"))

    if any(
        operator.get(field) == "CUSTOM"
        for field in ("execution_family", "operation_type", "duplicate_policy", "alignment_policy")
    ) and operator.get("rationale_ref") is None:
        findings.add(Finding("CUSTOM_RATIONALE_REQUIRED", "/operator/rationale_ref"))

    roles = [item["role"] for item in inputs]
    if operation_type == "EXCEPT":
        if len(inputs) != 2 or roles != ["MINUEND", "SUBTRAHEND"]:
            findings.add(Finding("EXCEPT_INPUT_ROLES_INVALID", "/inputs"))
    elif operation_type == "SYMMETRIC_DIFFERENCE":
        if len(inputs) != 2 or any(role != "MEMBER" for role in roles):
            findings.add(Finding("SYMMETRIC_DIFFERENCE_INPUTS_INVALID", "/inputs"))
    elif any(role != "MEMBER" for role in roles):
        findings.add(Finding("SET_INPUT_ROLES_INVALID", "/inputs"))

    input_counts = [item["row_count"] for item in inputs]
    output_count = output.get("row_count")
    if output_count is None or any(count is None for count in input_counts):
        findings.add(Finding("COMPLETE_ROW_COUNT_REQUIRED", "/output/row_count"))
    else:
        counts = [int(count) for count in input_counts]
        observed = int(output_count)
        if operation_type == "UNION_ALL" and observed != sum(counts):
            findings.add(Finding("UNION_ALL_COUNT_MISMATCH", "/output/row_count"))
        elif operation_type == "UNION_DISTINCT" and observed > sum(counts):
            findings.add(Finding("UNION_DISTINCT_COUNT_BOUND_EXCEEDED", "/output/row_count"))
        elif operation_type == "INTERSECT" and observed > min(counts):
            findings.add(Finding("INTERSECT_COUNT_BOUND_EXCEEDED", "/output/row_count"))
        elif operation_type == "EXCEPT" and observed > counts[0]:
            findings.add(Finding("EXCEPT_COUNT_BOUND_EXCEEDED", "/output/row_count"))
        elif operation_type == "SYMMETRIC_DIFFERENCE" and observed > sum(counts):
            findings.add(Finding("SYMMETRIC_DIFFERENCE_COUNT_BOUND_EXCEEDED", "/output/row_count"))

    if candidate.get("intended_use") == PUBLIC_USE:
        if not evidence.get("evidence_bundle_refs"):
            findings.add(Finding("PUBLIC_EVIDENCE_REFERENCE_REQUIRED", "/evidence/evidence_bundle_refs"))
        if not evidence.get("review_record_refs"):
            findings.add(Finding("PUBLIC_REVIEW_REFERENCE_REQUIRED", "/evidence/review_record_refs"))
        caveat = evidence.get("public_interpretation_caveat")
        if not isinstance(caveat, str) or caveat.strip() != caveat:
            findings.add(Finding("PUBLIC_INTERPRETATION_CAVEAT_REQUIRED", "/evidence/public_interpretation_caveat"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if "EXECUTION_ERROR" in codes:
        outcome = "ERROR"
    elif not codes:
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
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {
                    "outcome": "ERROR",
                    "codes": sorted({finding.code for finding in load_findings}),
                },
            }
        ]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        assert isinstance(entry, Mapping)
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append(
            {
                "name": entry["name"],
                "ok": observed == expected,
                "expected": expected,
                "observed": observed,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only set-operation provenance receipts."
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
    print(
        json.dumps(
            {"outcome": result.outcome, "codes": result.codes},
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
