#!/usr/bin/env python3
"""Validate proposed CitationValidationReport declarations without network access."""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = (
    ROOT
    / "schemas/contracts/v1/evidence/citation_validation_report.schema.json"
)
FIXTURES = (
    ROOT
    / "fixtures/contracts/v1/evidence/citation_validation_report/cases.json"
)
REPORT_PREFIX = "kfm:citation-validation-report:"
MAX_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
PUBLIC_SURFACES = frozenset(
    {
        "AI_ANSWER_CANDIDATE",
        "EXPORT_CANDIDATE",
        "FOCUS_CANDIDATE",
        "GOVERNED_API_CANDIDATE",
        "MAP_CANDIDATE",
    }
)
NON_EFFECTS = (
    "no_source_contact",
    "no_evidence_resolution",
    "no_policy_evaluation",
    "no_review_authentication",
    "no_release_verification",
    "no_lifecycle_mutation",
    "no_publication",
    "no_public_answer_authority",
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]
    report_outcome: str | None = None


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1") for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (
                Finding("CITATION_REPORT_INPUT_SYMLINK_DENIED", "/"),
            )
        if not path.is_file():
            return None, (Finding("CITATION_REPORT_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("CITATION_REPORT_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("CITATION_REPORT_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("CITATION_REPORT_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("CITATION_REPORT_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("CITATION_REPORT_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"report_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, REPORT_PREFIX + digest.split(":", 1)[1][:24]


def derive_citation(
    citation: Mapping[str, Any],
    subject: Mapping[str, Any],
) -> tuple[str, list[str]]:
    """Derive one finite citation outcome from declared upstream states."""

    errors: set[str] = set()
    denials: set[str] = set()
    abstentions: set[str] = set()

    citation_state = citation["citation_state"]
    if citation_state == "ERROR":
        errors.add("CITATION_STATE_ERROR")
    elif citation_state == "MISSING":
        abstentions.add("CITATION_MISSING")
    elif citation_state == "MALFORMED":
        abstentions.add("CITATION_MALFORMED")
    elif citation_state == "OUT_OF_SCOPE":
        abstentions.add("CITATION_OUT_OF_SCOPE")
    elif citation_state == "RIGHTS_BLOCKED":
        denials.add("CITATION_RIGHTS_BLOCKED")
    elif citation_state == "SENSITIVITY_BLOCKED":
        denials.add("CITATION_SENSITIVITY_BLOCKED")

    if citation_state == "USABLE" and citation["locator"]["kind"] == "NONE":
        abstentions.add("CITATION_LOCATOR_MISSING")
    if citation["source_role"] not in subject["allowed_source_roles"]:
        abstentions.add("CITATION_SOURCE_ROLE_NOT_ALLOWED")

    if subject["requires_current_support"]:
        if citation["freshness_state"] == "STALE":
            abstentions.add("CITATION_STALE")
        elif citation["freshness_state"] in {"UNKNOWN", "NOT_APPLICABLE"}:
            abstentions.add("CITATION_TIME_UNKNOWN")

    evidence_ref_state = citation["evidence_ref"]["state"]
    if evidence_ref_state == "ERROR":
        errors.add("CITATION_EVIDENCE_REF_ERROR")
    elif evidence_ref_state == "DENIED":
        denials.add("CITATION_EVIDENCE_REF_DENIED")
    elif citation_state == "USABLE" and evidence_ref_state in {
        "UNRESOLVED",
        "NOT_APPLICABLE",
    }:
        abstentions.add("CITATION_EVIDENCE_REF_UNRESOLVED")

    bundle_state = citation["evidence_bundle"]["state"]
    if bundle_state == "ERROR":
        errors.add("CITATION_BUNDLE_ERROR")
    elif bundle_state == "DENIED":
        denials.add("CITATION_BUNDLE_DENIED")
    elif citation_state == "USABLE" and bundle_state in {
        "INCOMPLETE",
        "NOT_APPLICABLE",
    }:
        abstentions.add("CITATION_BUNDLE_INCOMPLETE")

    rights_state = citation["rights_state"]
    if rights_state == "DENIED":
        denials.add("CITATION_RIGHTS_DENIED")
    elif rights_state == "UNKNOWN":
        abstentions.add("CITATION_RIGHTS_UNKNOWN")

    sensitivity_state = citation["sensitivity_state"]
    if sensitivity_state == "DENIED":
        denials.add("CITATION_SENSITIVITY_DENIED")
    elif sensitivity_state == "UNKNOWN":
        abstentions.add("CITATION_SENSITIVITY_UNKNOWN")

    policy_state = citation["policy_state"]
    if policy_state == "ERROR":
        errors.add("CITATION_POLICY_ERROR")
    elif policy_state == "DENY":
        denials.add("CITATION_POLICY_DENIED")
    elif policy_state == "RESTRICT":
        abstentions.add("CITATION_POLICY_NOT_READY")

    if citation["release_state"] == "WITHDRAWN":
        denials.add("CITATION_RELEASE_WITHDRAWN")

    if subject["surface"] in PUBLIC_SURFACES:
        if sensitivity_state == "RESTRICTED":
            denials.add("CITATION_SENSITIVITY_RESTRICTED_PUBLIC")
        if policy_state != "ALLOW" and policy_state not in {"DENY", "ERROR"}:
            abstentions.add("CITATION_POLICY_NOT_READY")
        if citation["review_state"] != "APPROVED":
            abstentions.add("CITATION_REVIEW_NOT_READY")
        if (
            citation["release_state"] != "RELEASED"
            and citation["release_state"] != "WITHDRAWN"
        ):
            abstentions.add("CITATION_RELEASE_NOT_READY")

    reasons = sorted(errors | denials | abstentions)
    if errors:
        return "ERROR", reasons
    if denials:
        return "DENY", reasons
    if abstentions:
        return "ABSTAIN", reasons
    return "PASS", ["CITATION_READY_FOR_DECLARED_SCOPE"]


def derive_summary(citations: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    outcomes = [citation["declared_outcome"] for citation in citations]
    counts = {
        outcome: outcomes.count(outcome)
        for outcome in ("PASS", "ABSTAIN", "DENY", "ERROR")
    }
    if counts["ERROR"]:
        outcome = "ERROR"
    elif counts["DENY"]:
        outcome = "DENY"
    elif counts["ABSTAIN"]:
        outcome = "ABSTAIN"
    else:
        outcome = "PASS"
    reasons = sorted(
        {
            reason
            for citation in citations
            for reason in citation["reason_codes"]
        }
    )
    remediations = sorted(
        {
            citation["remediation_ref"]
            for citation in citations
            if citation["remediation_ref"] is not None
        }
    )
    return {
        "outcome": outcome,
        "blocking": outcome != "PASS",
        "citation_count": len(citations),
        "pass_count": counts["PASS"],
        "abstain_count": counts["ABSTAIN"],
        "deny_count": counts["DENY"],
        "error_count": counts["ERROR"],
        "reason_codes": reasons,
        "remediation_refs": remediations,
    }


def _schema_finding(value: Mapping[str, Any]) -> Finding | None:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema,
                    format_checker=FormatChecker(),
                ).iter_errors(value),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except Exception:
        return Finding("CITATION_REPORT_SCHEMA_UNAVAILABLE", "/")
    if not errors:
        return None
    errors.sort(
        key=lambda error: (
            _pointer(error.absolute_path),
            str(error.validator),
        )
    )
    return Finding(
        "CITATION_REPORT_SCHEMA_INVALID",
        _pointer(errors[0].absolute_path),
    )


def _semantic_finding(value: Mapping[str, Any]) -> Finding | None:
    allowed_roles = value["subject"]["allowed_source_roles"]
    if allowed_roles != sorted(allowed_roles):
        return Finding(
            "CITATION_REPORT_SOURCE_ROLES_NOT_CANONICAL",
            "/subject/allowed_source_roles",
        )

    citations = value["citations"]
    citation_ids = [citation["citation_id"] for citation in citations]
    if len(citation_ids) != len(set(citation_ids)):
        return Finding(
            "CITATION_REPORT_CITATION_ID_DUPLICATE",
            "/citations",
        )
    if citation_ids != sorted(citation_ids):
        return Finding(
            "CITATION_REPORT_CITATIONS_NOT_CANONICAL",
            "/citations",
        )

    for index, citation in enumerate(citations):
        expected_outcome, expected_reasons = derive_citation(
            citation,
            value["subject"],
        )
        if citation["declared_outcome"] != expected_outcome:
            return Finding(
                "CITATION_REPORT_CITATION_OUTCOME_MISMATCH",
                f"/citations/{index}/declared_outcome",
            )
        if citation["reason_codes"] != expected_reasons:
            return Finding(
                "CITATION_REPORT_CITATION_REASONS_MISMATCH",
                f"/citations/{index}/reason_codes",
            )
        remediation = citation["remediation_ref"]
        if expected_outcome == "PASS" and remediation is not None:
            return Finding(
                "CITATION_REPORT_PASS_HAS_REMEDIATION",
                f"/citations/{index}/remediation_ref",
            )
        if expected_outcome != "PASS" and remediation is None:
            return Finding(
                "CITATION_REPORT_BLOCKING_REMEDIATION_MISSING",
                f"/citations/{index}/remediation_ref",
            )

        for binding in ("evidence_ref", "evidence_bundle"):
            state = citation[binding]["state"]
            reference = citation[binding]["ref"]
            if state in {"RESOLVED", "CLOSED"} and reference is None:
                return Finding(
                    "CITATION_REPORT_RESOLVED_BINDING_REF_MISSING",
                    f"/citations/{index}/{binding}/ref",
                )
            if state == "NOT_APPLICABLE" and reference is not None:
                return Finding(
                    "CITATION_REPORT_NOT_APPLICABLE_REF_PRESENT",
                    f"/citations/{index}/{binding}/ref",
                )

    if value["summary"] != derive_summary(citations):
        return Finding(
            "CITATION_REPORT_SUMMARY_MISMATCH",
            "/summary",
        )

    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        return Finding("CITATION_REPORT_CANONICALIZATION_ERROR", "/")
    if value["spec_hash"] != expected_hash:
        return Finding(
            "CITATION_REPORT_SPEC_HASH_MISMATCH",
            "/spec_hash",
        )
    if value["report_id"] != expected_id:
        return Finding(
            "CITATION_REPORT_ID_MISMATCH",
            "/report_id",
        )
    return None


def validate_payload(value: Mapping[str, Any]) -> Result:
    finding = _schema_finding(value)
    if finding is not None:
        return Result("DENY", (finding,))
    finding = _semantic_finding(value)
    if finding is not None:
        return Result("DENY", (finding,))
    report_outcome = value["summary"]["outcome"]
    return Result(report_outcome, (), report_outcome)


def _parts(pointer: str) -> list[str]:
    return [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer[1:].split("/")
    ]


def _target(document: Any, pointer: str) -> tuple[Any, str]:
    parts = _parts(pointer)
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    return target, parts[-1]


def _apply(document: dict[str, Any], operation: Mapping[str, Any]) -> None:
    target, key = _target(document, operation["path"])
    if operation["op"] == "set":
        if isinstance(target, list):
            target[int(key)] = copy.deepcopy(operation["value"])
        else:
            target[key] = copy.deepcopy(operation["value"])
    elif operation["op"] == "delete":
        if isinstance(target, list):
            del target[int(key)]
        else:
            del target[key]
    elif operation["op"] == "swap":
        container = target[int(key)] if isinstance(target, list) else target[key]
        first, second = operation["indexes"]
        container[first], container[second] = (
            container[second],
            container[first],
        )
    else:
        raise ValueError(f"unsupported fixture operation: {operation['op']}")


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(
    manifest: Mapping[str, Any],
    case: Mapping[str, Any],
) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for operation in case.get("operations", []):
        _apply(document, operation)
    if case.get("recompute_derived", True):
        for citation in document["citations"]:
            outcome, reasons = derive_citation(citation, document["subject"])
            citation["declared_outcome"] = outcome
            citation["reason_codes"] = reasons
        document["summary"] = derive_summary(document["citations"])
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["report_id"] = case.get("report_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual_findings = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        if (
            result.outcome != case["expected_status"]
            or result.report_outcome != case["expected_report_outcome"]
            or actual_findings != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_status": case["expected_status"],
                    "actual_status": result.outcome,
                    "expected_report_outcome": case[
                        "expected_report_outcome"
                    ],
                    "actual_report_outcome": result.report_outcome,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual_findings,
                }
            )
    print(
        json.dumps(
            {
                "cases": len(manifest["cases"]),
                "failures": failures,
                "suite_match": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "DECLARATION_VALIDATION_NO_NETWORK",
            "file": path.as_posix() if path else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": list(NON_EFFECTS),
            "outcome": result.outcome,
            "report_outcome": result.report_outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = (
        Result("ERROR", findings)
        if value is None
        else validate_payload(value)
    )
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
