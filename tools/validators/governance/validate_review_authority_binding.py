from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import CanonicalizationFailure, JsonInputError, compute_spec_hash, load_json_file  # noqa: E402

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/review_authority_binding.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/review_authority_binding/cases.json"
SCOPE = "governance.review_authority_binding"
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(_SCHEMA)
_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    binding_outcome: str | None
    findings: tuple[Finding, ...]
    binding_id: str | None = None


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _parse_aware(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timezone required")
    return parsed


def _sorted_unique(values: list[object]) -> bool:
    encoded = [json.dumps(value, sort_keys=True, separators=(",", ":")) for value in values]
    return encoded == sorted(encoded) and len(encoded) == len(set(encoded))


def _identity(document: Mapping[str, Any]) -> tuple[str, str]:
    projection = {
        key: value
        for key, value in document.items()
        if key not in {"binding_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(projection)
    return (
        "kfm:review-authority-binding:" + spec_hash.removeprefix("sha256:"),
        spec_hash,
    )


def _derive(document: Mapping[str, Any]) -> tuple[dict[str, bool], str, list[str]]:
    subject = document["subject"]
    review = document["review"]
    assignment = document["assignment"]

    actor_match = review["reviewer_actor_ref"] == assignment["steward_actor_ref"]
    role_match = review["reviewer_role"] == assignment["steward_role"]
    subject_match = subject["ref"] == assignment["target_ref"]

    try:
        reviewed_at = _parse_aware(review["reviewed_at"])
        starts_at = _parse_aware(assignment["starts_at"])
        expires_at = (
            _parse_aware(assignment["expires_at"])
            if assignment["expires_at"] is not None
            else None
        )
        effective_window_match = reviewed_at >= starts_at and (
            expires_at is None or reviewed_at < expires_at
        )
    except ValueError:
        effective_window_match = False

    active_assignment = assignment["status"] == "ACTIVE"
    approved_review = review["disposition"] == "APPROVE"
    actual_distinct = subject["author_actor_ref"] != review["reviewer_actor_ref"]
    sod_satisfied = (
        not review["independent_review_required"]
        or (review["author_reviewer_distinct"] and actual_distinct)
    )

    checks = {
        "actor_match": actor_match,
        "role_match": role_match,
        "subject_match": subject_match,
        "effective_window_match": effective_window_match,
        "active_assignment": active_assignment,
        "approved_review": approved_review,
        "separation_of_duties_satisfied": sod_satisfied,
    }

    reasons = {
        "ACTOR_MATCH" if actor_match else "ACTOR_MISMATCH",
        "ROLE_MATCH" if role_match else "ROLE_MISMATCH",
        "SUBJECT_MATCH" if subject_match else "SUBJECT_MISMATCH",
        "EFFECTIVE_WINDOW_MATCH" if effective_window_match else "EFFECTIVE_WINDOW_MISMATCH",
        "SOD_SATISFIED" if sod_satisfied else "SOD_FAILED",
    }
    status = assignment["status"]
    if status == "ACTIVE":
        reasons.add("ACTIVE_ASSIGNMENT")
    elif status == "PROVISIONAL":
        reasons.add("ASSIGNMENT_PROVISIONAL")
    elif status == "EXPIRED":
        reasons.add("ASSIGNMENT_EXPIRED")
    else:
        reasons.add("ASSIGNMENT_NOT_ACTIVE")

    disposition = review["disposition"]
    if disposition == "APPROVE":
        reasons.add("APPROVED_REVIEW")
    elif disposition == "APPROVE_WITH_CONDITIONS":
        reasons.add("REVIEW_CONDITIONAL")
    else:
        reasons.add("REVIEW_NOT_APPROVED")

    hard_failure = (
        not actor_match
        or not role_match
        or not subject_match
        or not effective_window_match
        or not sod_satisfied
        or status in {"EXPIRED", "SUPERSEDED", "REVOKED", "UNKNOWN"}
    )
    if hard_failure:
        outcome = "DENY"
    elif status == "PROVISIONAL" or disposition != "APPROVE":
        outcome = "HOLD"
    else:
        outcome = "BOUND"
    return checks, outcome, sorted(reasons)


def _set_path(document: dict[str, Any], path: str, value: object) -> None:
    parts = path.split(".")
    target: dict[str, Any] = document
    for part in parts[:-1]:
        nested = target.get(part)
        if not isinstance(nested, dict):
            raise ValueError("mutation path must traverse objects")
        target = nested
    target[parts[-1]] = value


def _finalize_document(document: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(dict(document))
    checks, outcome, reasons = _derive(candidate)
    candidate["checks"] = checks
    candidate["outcome"] = outcome
    candidate["reason_codes"] = reasons
    binding_id, spec_hash = _identity(candidate)
    candidate["binding_id"] = binding_id
    candidate["spec_hash"] = spec_hash
    return candidate


def materialize_case(base_document: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(dict(base_document))
    mutations = case.get("mutations", [])
    if not isinstance(mutations, list):
        raise ValueError("mutations must be a list")
    for mutation in mutations:
        if not isinstance(mutation, dict) or not isinstance(mutation.get("path"), str):
            raise ValueError("invalid mutation")
        _set_path(candidate, mutation["path"], copy.deepcopy(mutation.get("value")))
    if case.get("recompute", True):
        candidate = _finalize_document(candidate)
    tamper = case.get("tamper", [])
    if not isinstance(tamper, list):
        raise ValueError("tamper must be a list")
    for mutation in tamper:
        if not isinstance(mutation, dict) or not isinstance(mutation.get("path"), str):
            raise ValueError("invalid tamper")
        _set_path(candidate, mutation["path"], copy.deepcopy(mutation.get("value")))
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

    review = document["review"]
    assignment = document["assignment"]
    for prefix, fields in (
        ("review", ("conditions", "basis_refs", "policy_context_refs")),
        (
            "assignment",
            (
                "authority_basis_refs",
                "responsibility_actions",
                "required_partner_roles",
            ),
        ),
        ("root", ("reason_codes",)),
    ):
        target = document if prefix == "root" else document[prefix]
        for field in fields:
            if not _sorted_unique(target[field]):
                path = f"$.{field}" if prefix == "root" else f"$.{prefix}.{field}"
                findings.add(Finding("ORDER_OR_DUPLICATE_INVALID", path))

    actual_distinct = (
        document["subject"]["author_actor_ref"] != review["reviewer_actor_ref"]
    )
    if actual_distinct != review["author_reviewer_distinct"]:
        findings.add(
            Finding(
                "AUTHOR_REVIEWER_DISTINCT_MISMATCH",
                "$.review.author_reviewer_distinct",
            )
        )
    if review["independent_review_required"] and not actual_distinct:
        findings.add(Finding("SELF_REVIEW_DENIED", "$.review.reviewer_actor_ref"))

    if review["disposition"] == "APPROVE" and review["conditions"]:
        findings.add(Finding("APPROVAL_CONDITIONS_INVALID", "$.review.conditions"))
    if (
        review["disposition"] == "APPROVE_WITH_CONDITIONS"
        and not review["conditions"]
    ):
        findings.add(Finding("APPROVAL_CONDITIONS_REQUIRED", "$.review.conditions"))

    if assignment["steward_role"] in assignment["required_partner_roles"]:
        findings.add(
            Finding("PARTNER_ROLE_COLLAPSE", "$.assignment.required_partner_roles")
        )
    if (
        assignment["status"] == "PROVISIONAL"
        and assignment["expires_at"] is None
    ):
        findings.add(
            Finding("PROVISIONAL_EXPIRY_REQUIRED", "$.assignment.expires_at")
        )
    if "PREFLIGHT_WORK_APPLY" not in assignment["responsibility_actions"]:
        findings.add(
            Finding(
                "PREFLIGHT_RESPONSIBILITY_REQUIRED",
                "$.assignment.responsibility_actions",
            )
        )

    checks, expected_outcome, expected_reasons = _derive(document)
    if document["checks"] != checks:
        findings.add(Finding("CHECK_PROJECTION_MISMATCH", "$.checks"))
    if document["outcome"] != expected_outcome:
        findings.add(Finding("OUTCOME_MISMATCH", "$.outcome"))
    if document["reason_codes"] != expected_reasons:
        findings.add(Finding("REASON_CODES_MISMATCH", "$.reason_codes"))

    try:
        expected_id, expected_hash = _identity(document)
    except CanonicalizationFailure:
        findings.add(Finding("CANONICALIZATION_ERROR", "$"))
        return ValidationResult("DENY", expected_outcome, tuple(sorted(findings)))

    if document["binding_id"] != expected_id:
        findings.add(Finding("BINDING_ID_MISMATCH", "$.binding_id"))
    if document["spec_hash"] != expected_hash:
        findings.add(Finding("BINDING_SPEC_HASH_MISMATCH", "$.spec_hash"))

    return ValidationResult(
        "DENY" if findings else "PASS",
        expected_outcome,
        tuple(sorted(findings)),
        expected_id,
    )


def validate_file(path: Path) -> ValidationResult:
    try:
        document = load_json_file(path)
    except JsonInputError:
        return ValidationResult(
            "ERROR",
            None,
            (Finding("BINDING_JSON_INVALID", "$"),),
        )
    return validate_document(document)


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        fixture = load_json_file(FIXTURE_PATH)
    except JsonInputError:
        return False, {"cases": [], "ok": False, "scope": SCOPE}
    cases = fixture.get("cases", []) if isinstance(fixture, dict) else []
    results: list[dict[str, object]] = []
    ok = bool(cases)
    for case in cases:
        if not isinstance(case, dict) or not isinstance(case.get("expected"), dict):
            ok = False
            continue
        base_document = fixture.get("base_document")
        if not isinstance(base_document, dict):
            return False, {"cases": [], "ok": False, "scope": SCOPE}
        try:
            document = materialize_case(base_document, case)
        except (ValueError, CanonicalizationFailure):
            ok = False
            continue
        result = validate_document(document)
        actual_codes = sorted({finding.code for finding in result.findings})
        expected = case["expected"]
        case_ok = (
            result.status == expected.get("status")
            and result.binding_outcome == expected.get("binding_outcome")
            and actual_codes == expected.get("finding_codes")
        )
        ok = ok and case_ok
        results.append(
            {
                "actual_binding_outcome": result.binding_outcome,
                "actual_findings": actual_codes,
                "actual_status": result.status,
                "case_id": case.get("case_id"),
                "expected_binding_outcome": expected.get("binding_outcome"),
                "expected_findings": expected.get("finding_codes"),
                "expected_status": expected.get("status"),
                "ok": case_ok,
            }
        )
    return ok, {"cases": results, "ok": ok, "scope": SCOPE}


def _serialize(result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "binding_id": result.binding_id,
            "binding_outcome": result.binding_outcome,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": [
                "does_not_authenticate_actor_or_platform_identity",
                "does_not_authorize_apply_or_emit_write_request",
                "does_not_create_policy_promotion_or_release_authority",
                "does_not_merge_release_deploy_or_publish",
                "does_not_write_repository_or_lifecycle_state",
            ],
            "scope": SCOPE,
            "status": result.status,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only KFM ReviewAuthorityBinding objects."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with explicit files")
        ok, report = run_fixture_suite()
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda value: value.as_posix()):
        result = validate_file(path)
        print(_serialize(result))
        failed = failed or result.status != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
