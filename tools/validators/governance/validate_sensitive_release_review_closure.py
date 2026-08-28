"""Validate fixture-only T3/T4 sensitive-release review closure records."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker
from referencing.exceptions import Unresolvable

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import CanonicalizationFailure, JsonInputError, compute_spec_hash, load_json_file  # noqa: E402
from tools.validators._common.local_resolver import build_registry  # noqa: E402

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/sensitive_release_review_closure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/sensitive_release_review_closure/cases.json"
SCOPE = "governance.sensitive_release_review_closure"


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError("module could not be loaded")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_REVIEW = _load_module(
    "kfm_review_authority_binding_for_sensitive_release",
    REPO_ROOT / "tools/validators/governance/validate_review_authority_binding.py",
)
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(_SCHEMA)
_VALIDATOR = Draft202012Validator(
    _SCHEMA,
    registry=build_registry(REPO_ROOT),
    format_checker=FormatChecker(),
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    closure_outcome: str | None
    findings: tuple[Finding, ...]
    closure_id: str | None = None


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _sorted_unique(values: list[object]) -> bool:
    encoded = [json.dumps(value, sort_keys=True, separators=(",", ":")) for value in values]
    return encoded == sorted(encoded) and len(encoded) == len(set(encoded))


def _set_path(document: dict[str, Any], path: str, value: object) -> None:
    parts = path.split(".")
    target: dict[str, Any] = document
    for part in parts[:-1]:
        nested = target.get(part)
        if not isinstance(nested, dict):
            raise ValueError("mutation path must traverse objects")
        target = nested
    target[parts[-1]] = value


def _identity(document: Mapping[str, Any]) -> tuple[str, str]:
    projection = {
        key: value
        for key, value in document.items()
        if key not in {"closure_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(projection)
    return (
        "kfm:sensitive-release-review-closure:"
        + spec_hash.removeprefix("sha256:"),
        spec_hash,
    )


def _derive(document: Mapping[str, Any]) -> tuple[dict[str, bool], str, list[str]]:
    subject = document["subject"]
    context = document["release_context"]
    binding = document["review_binding"]
    review = binding["review"]
    assignment = binding["assignment"]
    binding_subject = binding["subject"]

    binding_result = _REVIEW.validate_document(binding)
    binding_valid = binding_result.status == "PASS"
    review_bound = binding_valid and binding_result.binding_outcome == "BOUND"
    subject_bound = subject["ref"] == binding_subject["ref"]
    author_bound = subject["author_actor_ref"] == binding_subject["author_actor_ref"]
    role_chain = subject["author_role_chain_actor_refs"]
    author_in_role_chain = subject["author_actor_ref"] in role_chain
    author_reviewer_distinct = subject["author_actor_ref"] != review["reviewer_actor_ref"]
    reviewer_outside_role_chain = review["reviewer_actor_ref"] not in role_chain
    release_review_responsibility = "RELEASE_REVIEW" in assignment["responsibility_actions"]
    policy_allows = context["policy_outcome"] == "ALLOW"
    evidence_present = bool(context["evidence_bundle_refs"])
    correction_present = bool(context["correction_path_ref"])
    rollback_present = bool(context["rollback_card_ref"])
    permissions = document["permissions"]
    no_authority = document["authority"] == "NONE" and all(
        value is False for value in permissions.values()
    )

    checks = {
        "review_binding_valid": binding_valid,
        "review_bound": review_bound,
        "subject_bound": subject_bound,
        "author_bound": author_bound,
        "author_in_role_chain": author_in_role_chain,
        "author_reviewer_distinct": author_reviewer_distinct,
        "reviewer_outside_author_role_chain": reviewer_outside_role_chain,
        "release_review_responsibility": release_review_responsibility,
        "policy_allows": policy_allows,
        "evidence_present": evidence_present,
        "correction_path_present": correction_present,
        "rollback_present": rollback_present,
        "no_authority": no_authority,
    }

    reasons = {
        "AUTHOR_BOUND" if author_bound else "AUTHOR_MISMATCH",
        "AUTHOR_IN_ROLE_CHAIN" if author_in_role_chain else "AUTHOR_NOT_IN_ROLE_CHAIN",
        "CORRECTION_PATH_PRESENT",
        "EVIDENCE_PRESENT",
        "INDEPENDENT_REVIEWER"
        if author_reviewer_distinct and reviewer_outside_role_chain
        else (
            "SELF_REVIEW_DENIED"
            if not author_reviewer_distinct
            else "REVIEWER_IN_AUTHOR_ROLE_CHAIN"
        ),
        "NO_AUTHORITY",
        "RELEASE_REVIEW_RESPONSIBILITY"
        if release_review_responsibility
        else "RELEASE_REVIEW_RESPONSIBILITY_MISSING",
        "ROLLBACK_PRESENT",
        "SUBJECT_BOUND" if subject_bound else "SUBJECT_MISMATCH",
    }

    policy = context["policy_outcome"]
    reasons.add(
        {
            "ALLOW": "POLICY_ALLOWS",
            "HOLD": "POLICY_HOLDS",
            "DENY": "POLICY_DENIES",
            "ABSTAIN": "POLICY_ABSTAINS",
        }[policy]
    )
    if not binding_valid:
        reasons.add("REVIEW_BINDING_INVALID")
    elif binding_result.binding_outcome == "BOUND":
        reasons.add("REVIEW_BOUND")
    elif binding_result.binding_outcome == "HOLD":
        reasons.add("REVIEW_BINDING_HOLD")
    else:
        reasons.add("REVIEW_BINDING_DENY")

    hard_failure = (
        not binding_valid
        or binding_result.binding_outcome == "DENY"
        or policy == "DENY"
        or not subject_bound
        or not author_bound
        or not author_in_role_chain
        or not author_reviewer_distinct
        or not reviewer_outside_role_chain
        or not release_review_responsibility
        or not evidence_present
        or not correction_present
        or not rollback_present
        or not no_authority
    )
    if hard_failure:
        outcome = "DENY"
    elif binding_result.binding_outcome == "HOLD" or policy in {"HOLD", "ABSTAIN"}:
        outcome = "HOLD"
    elif review_bound and policy_allows:
        outcome = "CLOSED_FOR_SEPARATE_RELEASE_GATE"
    else:
        outcome = "DENY"
    return checks, outcome, sorted(reasons)


def _finalize_document(document: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(dict(document))
    checks, outcome, reasons = _derive(candidate)
    candidate["checks"] = checks
    candidate["outcome"] = outcome
    candidate["reason_codes"] = reasons
    closure_id, spec_hash = _identity(candidate)
    candidate["closure_id"] = closure_id
    candidate["spec_hash"] = spec_hash
    return candidate


def materialize_case(base_document: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(dict(base_document))
    review_case = {"mutations": copy.deepcopy(case.get("review_mutations", []))}
    candidate["review_binding"] = _REVIEW.materialize_case(
        candidate["review_binding"], review_case
    )
    mutations = case.get("mutations", [])
    if not isinstance(mutations, list):
        raise ValueError("mutations must be a list")
    for mutation in mutations:
        if not isinstance(mutation, dict) or not isinstance(mutation.get("path"), str):
            raise ValueError("invalid mutation")
        _set_path(candidate, mutation["path"], copy.deepcopy(mutation.get("value")))
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
    try:
        schema_errors = sorted(
            _VALIDATOR.iter_errors(document),
            key=lambda error: tuple(str(part) for part in error.absolute_path),
        )
    except (OSError, UnicodeError, ValueError, RecursionError, Unresolvable):
        return ValidationResult("ERROR", None, (Finding("SCHEMA_UNAVAILABLE", "$"),))
    for error in schema_errors:
        findings.add(Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path))))
    if schema_errors or not isinstance(document, dict):
        return ValidationResult("DENY", None, tuple(sorted(findings)))

    for path, values in (
        ("$.subject.author_role_chain_actor_refs", document["subject"]["author_role_chain_actor_refs"]),
        ("$.release_context.evidence_bundle_refs", document["release_context"]["evidence_bundle_refs"]),
        ("$.reason_codes", document["reason_codes"]),
    ):
        if not _sorted_unique(values):
            findings.add(Finding("ORDER_OR_DUPLICATE_INVALID", path))

    binding = document["review_binding"]
    binding_result = _REVIEW.validate_document(binding)
    if binding_result.status != "PASS":
        findings.add(Finding("REVIEW_BINDING_INVALID", "$.review_binding"))

    subject = document["subject"]
    binding_subject = binding["subject"]
    reviewer = binding["review"]["reviewer_actor_ref"]
    role_chain = subject["author_role_chain_actor_refs"]
    if subject["ref"] != binding_subject["ref"]:
        findings.add(Finding("SUBJECT_MISMATCH", "$.review_binding.subject.ref"))
    if subject["author_actor_ref"] != binding_subject["author_actor_ref"]:
        findings.add(Finding("AUTHOR_MISMATCH", "$.review_binding.subject.author_actor_ref"))
    if subject["author_actor_ref"] not in role_chain:
        findings.add(Finding("AUTHOR_NOT_IN_ROLE_CHAIN", "$.subject.author_role_chain_actor_refs"))
    if binding_subject["author_actor_ref"] == reviewer:
        findings.add(Finding("SELF_REVIEW_DENIED", "$.review_binding.review.reviewer_actor_ref"))
    elif reviewer in role_chain:
        findings.add(Finding("REVIEWER_IN_AUTHOR_ROLE_CHAIN", "$.subject.author_role_chain_actor_refs"))
    if "RELEASE_REVIEW" not in binding["assignment"]["responsibility_actions"]:
        findings.add(Finding("RELEASE_REVIEW_RESPONSIBILITY_MISSING", "$.review_binding.assignment.responsibility_actions"))

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
    if document["closure_id"] != expected_id:
        findings.add(Finding("CLOSURE_ID_MISMATCH", "$.closure_id"))
    if document["spec_hash"] != expected_hash:
        findings.add(Finding("CLOSURE_SPEC_HASH_MISMATCH", "$.spec_hash"))

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
        return ValidationResult("ERROR", None, (Finding("CLOSURE_JSON_INVALID", "$"),))
    return validate_document(document)


def _serialize(result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "closure_id": result.closure_id,
            "closure_outcome": result.closure_outcome,
            "execution_mode": "FIXTURE_ONLY",
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "scope": SCOPE,
            "status": result.status,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        suite = load_json_file(FIXTURE_PATH)
    except JsonInputError:
        return False, {"cases": [], "ok": False, "scope": SCOPE}
    if not isinstance(suite, dict) or not isinstance(suite.get("base_document"), dict):
        return False, {"cases": [], "ok": False, "scope": SCOPE}

    reports: list[dict[str, object]] = []
    ok = True
    for case in suite.get("cases", []):
        if not isinstance(case, dict):
            ok = False
            continue
        try:
            document = materialize_case(suite["base_document"], case)
            result = validate_document(document)
        except (KeyError, TypeError, ValueError, CanonicalizationFailure):
            ok = False
            continue
        actual_codes = sorted({finding.code for finding in result.findings})
        expected = case.get("expected", {})
        case_ok = (
            isinstance(expected, dict)
            and result.status == expected.get("status")
            and result.closure_outcome == expected.get("closure_outcome")
            and actual_codes == expected.get("finding_codes")
        )
        ok = ok and case_ok
        reports.append(
            {
                "actual_findings": actual_codes,
                "actual_outcome": result.closure_outcome,
                "actual_status": result.status,
                "case_id": case.get("case_id"),
                "expected_findings": expected.get("finding_codes") if isinstance(expected, dict) else None,
                "expected_outcome": expected.get("closure_outcome") if isinstance(expected, dict) else None,
                "expected_status": expected.get("status") if isinstance(expected, dict) else None,
                "ok": case_ok,
            }
        )
    return bool(reports) and ok, {"cases": reports, "ok": bool(reports) and ok, "scope": SCOPE}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.path is not None:
            parser.error("--fixtures cannot be combined with a path")
        ok, report = run_fixture_suite()
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 0 if ok else 1
    if args.path is None:
        parser.error("path is required unless --fixtures is used")
    result = validate_file(args.path)
    print(_serialize(result))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
