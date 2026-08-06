from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import (  # noqa: E402
    CanonicalizationFailure,
    JsonInputError,
    compute_spec_hash,
    load_json_file,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/query_run_record.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/query_run_record"
FIXTURE_PATHS = (
    FIXTURE_ROOT / "valid_cases.json",
    FIXTURE_ROOT / "schema_invalid_cases.json",
    FIXTURE_ROOT / "semantic_identity_cases.json",
    FIXTURE_ROOT / "semantic_resolution_cases.json",
)
SCOPE = "governance.query_run_record"
NON_EFFECTS = sorted(
    [
        "does_not_apply_candidate_changes",
        "does_not_create_public_use_authority",
        "does_not_evaluate_policy_or_create_review",
        "does_not_promote_release_deploy_or_publish",
        "does_not_resolve_evidence_or_admit_sources",
        "does_not_store_raw_query_model_output_or_chain_of_thought",
        "does_not_write_lifecycle_or_repository_state",
    ]
)
PERMISSION_KEYS = (
    "repository_mutation_allowed",
    "source_activation_allowed",
    "lifecycle_write_allowed",
    "policy_decision_creation_allowed",
    "review_creation_allowed",
    "promotion_allowed",
    "release_allowed",
    "deployment_allowed",
    "publication_allowed",
    "public_use_allowed",
)
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    query_run_id: str | None = None
    query_hash: str | None = None
    context_hash: str | None = None
    output_hash: str | None = None
    spec_hash: str | None = None
    run_hash: str | None = None


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _query_projection(document: Mapping[str, Any]) -> dict[str, object]:
    return {
        "actor_class": document["actor_class"],
        "query_summary": document["query_summary"],
        "scope": document["scope"],
    }


def _context_projection(document: Mapping[str, Any]) -> dict[str, object]:
    return {
        "allowed_evidence_classes": document["allowed_evidence_classes"],
        "evidence_resolution": document["evidence_resolution"],
    }


def _output_projection(document: Mapping[str, Any]) -> dict[str, object]:
    return {
        "candidate_proposal_refs": document["candidate_proposal_refs"],
        "outcome": document["outcome"],
        "reason_codes": document["reason_codes"],
    }


def _expected_hashes(document: Mapping[str, Any]) -> dict[str, str]:
    query_hash = compute_spec_hash(_query_projection(document))
    context_hash = compute_spec_hash(_context_projection(document))
    output_hash = compute_spec_hash(_output_projection(document))
    spec_hash = compute_spec_hash(
        {
            "schema_version": document["schema_version"],
            "profile": document["profile"],
            "profile_status": document["profile_status"],
            "execution_mode": document["execution_mode"],
            "authority": document["authority"],
            "query_hash": query_hash,
            "context_hash": context_hash,
            "output_hash": output_hash,
            "target_stage": document["target_stage"],
            "permissions": document["permissions"],
            "non_effects": document["non_effects"],
        }
    )
    run_hash = compute_spec_hash(
        {
            "created_at": document["created_at"],
            "query_hash": query_hash,
            "context_hash": context_hash,
            "output_hash": output_hash,
            "spec_hash": spec_hash,
        }
    )
    return {
        "query_hash": query_hash,
        "context_hash": context_hash,
        "output_hash": output_hash,
        "spec_hash": spec_hash,
        "run_hash": run_hash,
    }


def _expected_query_run_id(run_hash: str) -> str:
    return "kfm:query-run:" + run_hash.removeprefix("sha256:")


def _expected_summary(items: list[Mapping[str, Any]]) -> str:
    states = {item["status"] for item in items}
    if "ERROR" in states:
        return "ERROR"
    if "DENIED" in states:
        return "DENIED"
    if "CONFLICTED" in states:
        return "CONFLICTED"
    if "UNRESOLVED" in states:
        return "PARTIAL"
    return "COMPLETE"


def _expected_outcome(summary: str) -> str:
    return {
        "COMPLETE": "ANSWER",
        "PARTIAL": "ABSTAIN",
        "CONFLICTED": "ABSTAIN",
        "DENIED": "DENY",
        "ERROR": "ERROR",
    }[summary]


def _expected_reason_codes(summary: str, candidate_refs: list[str]) -> list[str]:
    evidence_code = {
        "COMPLETE": "EVIDENCE_RESOLVED",
        "PARTIAL": "EVIDENCE_UNRESOLVED",
        "CONFLICTED": "EVIDENCE_CONFLICTED",
        "DENIED": "EVIDENCE_DENIED",
        "ERROR": "VALIDATION_ERROR",
    }[summary]
    return sorted(
        [
            "FIXTURE_ONLY",
            "QUERY_VALIDATED",
            evidence_code,
            "CANDIDATE_PROPOSED" if candidate_refs else "NO_CANDIDATE_DELTA",
        ]
    )


def _sorted_unique(values: list[str]) -> bool:
    return values == sorted(values) and len(values) == len(set(values))


def validate_document(document: object) -> ValidationResult:
    findings: set[Finding] = set()
    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(document),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        findings.add(Finding("SCHEMA_INVALID", _json_path(tuple(error.absolute_path))))
    if schema_errors or not isinstance(document, dict):
        return ValidationResult("DENY", tuple(sorted(findings)))

    ordered_arrays = {
        "$.scope.domain_refs": document["scope"]["domain_refs"],
        "$.scope.geography_refs": document["scope"]["geography_refs"],
        "$.allowed_evidence_classes": document["allowed_evidence_classes"],
        "$.candidate_proposal_refs": document["candidate_proposal_refs"],
        "$.reason_codes": document["reason_codes"],
        "$.non_effects": document["non_effects"],
    }
    for path, values in ordered_arrays.items():
        if not _sorted_unique(values):
            findings.add(Finding("REFERENCE_ORDER_INVALID", path))

    items = document["evidence_resolution"]["items"]
    evidence_refs = [item["evidence_ref"] for item in items]
    if not _sorted_unique(evidence_refs):
        findings.add(Finding("EVIDENCE_ITEM_ORDER_INVALID", "$.evidence_resolution.items"))
    bundle_refs = [
        item["evidence_bundle_ref"]
        for item in items
        if item["evidence_bundle_ref"] is not None
    ]
    if len(bundle_refs) != len(set(bundle_refs)):
        findings.add(
            Finding(
                "EVIDENCE_BUNDLE_REF_DUPLICATE",
                "$.evidence_resolution.items",
            )
        )

    expected_summary = _expected_summary(items)
    if document["evidence_resolution"]["summary"] != expected_summary:
        findings.add(
            Finding(
                "EVIDENCE_SUMMARY_MISMATCH",
                "$.evidence_resolution.summary",
            )
        )

    expected_outcome = _expected_outcome(expected_summary)
    if document["outcome"] != expected_outcome:
        findings.add(Finding("OUTCOME_MISMATCH", "$.outcome"))

    expected_reasons = _expected_reason_codes(
        expected_summary,
        document["candidate_proposal_refs"],
    )
    if document["reason_codes"] != expected_reasons:
        findings.add(Finding("REASON_CODES_MISMATCH", "$.reason_codes"))

    if document["non_effects"] != NON_EFFECTS:
        findings.add(Finding("NON_EFFECTS_MISMATCH", "$.non_effects"))
    if document["target_stage"] != "WORK" or any(
        document["permissions"][key] for key in PERMISSION_KEYS
    ):
        findings.add(Finding("AUTHORITY_BOUNDARY_MISMATCH", "$.permissions"))

    try:
        expected_hashes = _expected_hashes(document)
    except CanonicalizationFailure:
        findings.add(Finding("CANONICALIZATION_ERROR", "$"))
        return ValidationResult("DENY", tuple(sorted(findings)))

    for name, expected in expected_hashes.items():
        if document["hashes"][name] != expected:
            findings.add(Finding(f"{name.upper()}_MISMATCH", f"$.hashes.{name}"))

    expected_id = _expected_query_run_id(expected_hashes["run_hash"])
    if document["query_run_id"] != expected_id:
        findings.add(Finding("QUERY_RUN_ID_MISMATCH", "$.query_run_id"))

    return ValidationResult(
        "DENY" if findings else "PASS",
        tuple(sorted(findings)),
        query_run_id=expected_id,
        query_hash=expected_hashes["query_hash"],
        context_hash=expected_hashes["context_hash"],
        output_hash=expected_hashes["output_hash"],
        spec_hash=expected_hashes["spec_hash"],
        run_hash=expected_hashes["run_hash"],
    )


def validate_file(path: Path) -> ValidationResult:
    try:
        document = load_json_file(path)
    except JsonInputError:
        return ValidationResult(
            "ERROR",
            (Finding("QUERY_RUN_JSON_INVALID", "$"),),
        )
    return validate_document(document)


def _serialize_result(result: ValidationResult, path: Path | None = None) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": str(path) if path else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": NON_EFFECTS,
            "outcome": result.outcome,
            "query_run_id": result.query_run_id,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    loaded_cases: list[object] = []
    for fixture_path in FIXTURE_PATHS:
        try:
            fixture_document = load_json_file(fixture_path)
        except JsonInputError:
            return False, {"cases": [], "ok": False, "scope": SCOPE}
        if not isinstance(fixture_document, dict) or not isinstance(
            fixture_document.get("cases"), list
        ):
            return False, {"cases": [], "ok": False, "scope": SCOPE}
        loaded_cases.extend(fixture_document["cases"])

    results: list[dict[str, object]] = []
    ok = True
    for case in loaded_cases:
        if not isinstance(case, dict) or not isinstance(case.get("expected"), dict):
            ok = False
            continue
        result = validate_document(case.get("record"))
        actual_codes = sorted({finding.code for finding in result.findings})
        expected = case["expected"]
        case_ok = (
            result.outcome == expected.get("outcome")
            and actual_codes == expected.get("finding_codes")
        )
        ok = ok and case_ok
        results.append(
            {
                "actual_findings": actual_codes,
                "actual_outcome": result.outcome,
                "case_id": case.get("case_id"),
                "expected_findings": expected.get("finding_codes"),
                "expected_outcome": expected.get("outcome"),
                "ok": case_ok,
            }
        )
    return ok, {"cases": results, "ok": ok, "scope": SCOPE}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only KFM QueryRunRecord objects."
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
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_file(path)
        print(_serialize_result(result, path))
        failed = failed or result.outcome != "PASS"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
