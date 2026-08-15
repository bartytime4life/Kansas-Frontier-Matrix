from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/review_coverage_snapshot.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/review_coverage_snapshot/cases.json"
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(_SCHEMA)
_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())

COUNTED_STATES = {"APPROVED", "CHANGES_REQUESTED", "SUBMITTED"}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    coverage_outcome: str | None
    findings: tuple[Finding, ...]


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _sorted_unique(values: list[object]) -> bool:
    encoded = [json.dumps(value, sort_keys=True, separators=(",", ":")) for value in values]
    return encoded == sorted(encoded) and len(encoded) == len(set(encoded))


def derive(document: Mapping[str, Any]) -> tuple[dict[str, bool], str, list[str]]:
    head_sha = document["pull_request"]["head_sha"]
    required_roles = set(document["requirements"]["required_roles"])
    independence_required = document["requirements"]["independence_required"]
    reviews = document["reviews"]

    counted = [review for review in reviews if review["state"] in COUNTED_STATES]
    all_exact = all(review["reviewed_head_sha"] == head_sha for review in counted)

    approving_current = [
        review
        for review in reviews
        if review["state"] == "APPROVED" and review["reviewed_head_sha"] == head_sha
    ]
    approved_roles = {review["reviewer_role"] for review in approving_current}
    required_roles_covered = required_roles.issubset(approved_roles)

    independence_satisfied = True
    if independence_required:
        for role in required_roles:
            role_reviews = [review for review in approving_current if review["reviewer_role"] == role]
            if not role_reviews or not any(review["independent"] for review in role_reviews):
                independence_satisfied = False
                break

    checks = {
        "all_counted_reviews_exact_head": all_exact,
        "required_roles_covered": required_roles_covered,
        "independence_satisfied": independence_satisfied,
    }

    reasons = {
        "ALL_COUNTED_REVIEWS_EXACT_HEAD" if all_exact else "STALE_COUNTED_REVIEW_PRESENT",
        "REQUIRED_ROLES_COVERED" if required_roles_covered else "REQUIRED_ROLES_MISSING",
        "INDEPENDENCE_SATISFIED" if independence_satisfied else "INDEPENDENCE_INCOMPLETE",
    }

    if not all_exact:
        outcome = "STALE"
    elif not required_roles_covered or not independence_satisfied:
        outcome = "HOLD"
    else:
        outcome = "CURRENT"
    return checks, outcome, sorted(reasons)


def finalize(document: Mapping[str, Any]) -> dict[str, Any]:
    candidate = json.loads(json.dumps(document))
    checks, outcome, reasons = derive(candidate)
    candidate["checks"] = checks
    candidate["outcome"] = outcome
    candidate["reason_codes"] = reasons
    return candidate


def validate_document(document: object) -> ValidationResult:
    findings: set[Finding] = set()
    schema_errors = sorted(
        _VALIDATOR.iter_errors(document),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        findings.add(Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path))))
    if schema_errors or not isinstance(document, dict):
        return ValidationResult("DENY", None, tuple(sorted(findings)))

    if not _sorted_unique(document["requirements"]["required_roles"]):
        findings.add(Finding("ORDER_OR_DUPLICATE_INVALID", "$.requirements.required_roles"))
    if not _sorted_unique(document["reason_codes"]):
        findings.add(Finding("ORDER_OR_DUPLICATE_INVALID", "$.reason_codes"))

    review_refs = [review["review_ref"] for review in document["reviews"]]
    if len(review_refs) != len(set(review_refs)):
        findings.add(Finding("DUPLICATE_REVIEW_REF", "$.reviews"))

    expected_checks, expected_outcome, expected_reasons = derive(document)
    if document["checks"] != expected_checks:
        findings.add(Finding("DERIVED_CHECKS_MISMATCH", "$.checks"))
    if document["outcome"] != expected_outcome:
        findings.add(Finding("DERIVED_OUTCOME_MISMATCH", "$.outcome"))
    if document["reason_codes"] != expected_reasons:
        findings.add(Finding("DERIVED_REASONS_MISMATCH", "$.reason_codes"))

    if findings:
        return ValidationResult("DENY", expected_outcome, tuple(sorted(findings)))
    return ValidationResult("PASS", expected_outcome, ())


def load_cases(path: Path = FIXTURE_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_fixture_cases(path: Path = FIXTURE_PATH) -> list[str]:
    payload = load_cases(path)
    base = payload["base"]
    failures: list[str] = []
    for case in payload["cases"]:
        candidate = json.loads(json.dumps(base))
        for mutation in case.get("mutations", []):
            target: Any = candidate
            parts = mutation["path"].split(".")
            for part in parts[:-1]:
                target = target[int(part)] if isinstance(target, list) else target[part]
            last = parts[-1]
            if isinstance(target, list):
                target[int(last)] = mutation["value"]
            else:
                target[last] = mutation["value"]
        candidate = finalize(candidate)
        for tamper in case.get("tamper", []):
            target = candidate
            parts = tamper["path"].split(".")
            for part in parts[:-1]:
                target = target[int(part)] if isinstance(target, list) else target[part]
            last = parts[-1]
            if isinstance(target, list):
                target[int(last)] = tamper["value"]
            else:
                target[last] = tamper["value"]
        result = validate_document(candidate)
        if result.status != case["expect_status"] or result.coverage_outcome != case["expect_outcome"]:
            failures.append(
                f"{case['id']}: expected {case['expect_status']}/{case['expect_outcome']} "
                f"got {result.status}/{result.coverage_outcome}"
            )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate KFM ReviewCoverageSnapshot fixtures or one JSON document.")
    parser.add_argument("document", nargs="?", type=Path)
    args = parser.parse_args()

    if args.document is None:
        failures = run_fixture_cases()
        if failures:
            for failure in failures:
                print(f"FAIL {failure}")
            return 1
        print("PASS review-coverage-snapshot fixtures")
        return 0

    document = json.loads(args.document.read_text(encoding="utf-8"))
    result = validate_document(document)
    print(json.dumps({
        "status": result.status,
        "coverage_outcome": result.coverage_outcome,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
    }, sort_keys=True))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
