"""Deterministic semantic validator for synthetic water-planning status collapses."""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence


MAX_FIXTURE_BYTES = 1_000_000

RECORD_TYPE = "water_planning_status_collapse_candidate"

ALLOWED_TOP_LEVEL_KEYS = frozenset(
    {
        "record_type",
        "fixture_id",
        "fixture_only",
        "network_access",
        "status_collapse_claims",
        "resolution_state",
        "amount_facts",
        "lineage",
        "blocked_behaviors",
    }
)

STATUS_COLLAPSE_RULES = {
    "meeting_is_approval": "MEETING_IS_NOT_APPROVAL",
    "application_is_recommendation": "APPLICATION_IS_NOT_RECOMMENDATION",
    "application_is_award": "APPLICATION_IS_NOT_AWARD",
    "recommendation_is_award": "RECOMMENDATION_IS_NOT_AWARD",
    "award_is_payment": "AWARD_IS_NOT_PAYMENT",
    "payment_is_construction": "PAYMENT_IS_NOT_CONSTRUCTION",
    "construction_is_completion": "CONSTRUCTION_IS_NOT_COMPLETION",
    "scoring_matrix_is_project_outcome": "SCORING_MATRIX_IS_NOT_PROJECT_OUTCOME",
    "program_version_is_project_outcome": "PROGRAM_VERSION_IS_NOT_PROJECT_OUTCOME",
}

RESOLUTION_STATE_RULES = {
    "applicant_identity": "APPLICANT_IDENTITY_GUESS_FORBIDDEN",
    "recipient_identity": "RECIPIENT_IDENTITY_GUESS_FORBIDDEN",
    "project_geometry": "PROJECT_GEOMETRY_GUESS_FORBIDDEN",
    "regional_geometry": "REGIONAL_GEOMETRY_GUESS_FORBIDDEN",
}

AMOUNT_FACT_KEYS = (
    "requested_amount",
    "recommended_amount",
    "awarded_amount",
    "paid_amount",
)

LINEAGE_KEYS = (
    "correction_or_withdrawal_ref",
    "supersedes_ref",
    "superseded_by_ref",
)

BLOCKED_BEHAVIOR_RULES = {
    "authenticated_portal": "AUTHENTICATED_PORTAL_BEHAVIOR_FORBIDDEN",
    "personal_data": "PERSONAL_DATA_BEHAVIOR_FORBIDDEN",
    "real_applicant": "REAL_APPLICANT_BEHAVIOR_FORBIDDEN",
    "real_project": "REAL_PROJECT_BEHAVIOR_FORBIDDEN",
    "connector": "CONNECTOR_BEHAVIOR_FORBIDDEN",
    "proof": "PROOF_BEHAVIOR_FORBIDDEN",
    "release": "RELEASE_BEHAVIOR_FORBIDDEN",
    "publication": "PUBLICATION_BEHAVIOR_FORBIDDEN",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


def _add(findings: list[Finding], code: str, path: str) -> None:
    finding = Finding(code=code, path=path)
    if finding not in findings:
        findings.append(finding)


def _is_finite_number(value: object) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    if isinstance(value, float):
        return math.isfinite(value)
    return False


def validate_candidate(candidate: object) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    if not isinstance(candidate, Mapping):
        return (Finding("DOCUMENT_NOT_OBJECT", "$"),)

    if candidate.get("record_type") != RECORD_TYPE:
        _add(findings, "RECORD_TYPE_INVALID", "$.record_type")
    if candidate.get("fixture_only") is not True:
        _add(findings, "FIXTURE_ONLY_REQUIRED", "$.fixture_only")
    if candidate.get("network_access") != "forbidden":
        _add(findings, "NETWORK_ACCESS_NOT_FORBIDDEN", "$.network_access")

    status_collapse_claims = candidate.get("status_collapse_claims")
    if not isinstance(status_collapse_claims, Mapping):
        _add(
            findings,
            "STATUS_COLLAPSE_CLAIMS_NOT_OBJECT",
            "$.status_collapse_claims",
        )
    else:
        for field, finding_code in STATUS_COLLAPSE_RULES.items():
            claim = status_collapse_claims.get(field)
            if not isinstance(claim, bool):
                _add(
                    findings,
                    "STATUS_COLLAPSE_CLAIM_NOT_BOOLEAN",
                    f"$.status_collapse_claims.{field}",
                )
                continue
            if claim:
                _add(findings, finding_code, f"$.status_collapse_claims.{field}")

    resolution_state = candidate.get("resolution_state")
    if not isinstance(resolution_state, Mapping):
        _add(findings, "RESOLUTION_STATE_NOT_OBJECT", "$.resolution_state")
    else:
        for field, finding_code in RESOLUTION_STATE_RULES.items():
            state = resolution_state.get(field)
            if state != "unresolved":
                _add(findings, finding_code, f"$.resolution_state.{field}")

    amount_facts = candidate.get("amount_facts")
    if not isinstance(amount_facts, Mapping):
        _add(findings, "AMOUNT_FACTS_NOT_OBJECT", "$.amount_facts")
    else:
        if "amount" in amount_facts:
            _add(findings, "COLLAPSED_AMOUNT_FIELD_FORBIDDEN", "$.amount_facts.amount")
        for key in AMOUNT_FACT_KEYS:
            if key not in amount_facts:
                _add(findings, "AMOUNT_FACT_MISSING", f"$.amount_facts.{key}")
                continue
            value = amount_facts[key]
            if value is not None and not _is_finite_number(value):
                _add(findings, "AMOUNT_FACT_NOT_NUMERIC_OR_NULL", f"$.amount_facts.{key}")

    lineage = candidate.get("lineage")
    if not isinstance(lineage, Mapping):
        _add(findings, "LINEAGE_NOT_OBJECT", "$.lineage")
    else:
        for key in LINEAGE_KEYS:
            if key not in lineage:
                _add(findings, "LINEAGE_FIELD_MISSING", f"$.lineage.{key}")
                continue
            value = lineage[key]
            if value is not None and not isinstance(value, str):
                _add(findings, "LINEAGE_REF_NOT_STRING_OR_NULL", f"$.lineage.{key}")

    blocked_behaviors = candidate.get("blocked_behaviors")
    if not isinstance(blocked_behaviors, Mapping):
        _add(findings, "BLOCKED_BEHAVIORS_NOT_OBJECT", "$.blocked_behaviors")
    else:
        for field, finding_code in BLOCKED_BEHAVIOR_RULES.items():
            value = blocked_behaviors.get(field)
            if value is True:
                _add(findings, finding_code, f"$.blocked_behaviors.{field}")
            elif value is not False:
                _add(
                    findings,
                    "BLOCKED_BEHAVIOR_FLAG_NOT_BOOLEAN",
                    f"$.blocked_behaviors.{field}",
                )

    for key in sorted(set(candidate) - ALLOWED_TOP_LEVEL_KEYS):
        _add(findings, "UNDECLARED_TOP_LEVEL_FIELD", f"$.{key}")

    return tuple(sorted(findings))


def validate_file(path: Path) -> tuple[Finding, ...]:
    try:
        if path.stat().st_size > MAX_FIXTURE_BYTES:
            return (Finding("FIXTURE_TOO_LARGE", "$"),)
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return (Finding("FIXTURE_JSON_INVALID", "$"),)
    return validate_candidate(payload)


def _serialize(path: Path, findings: Sequence[Finding]) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in findings
            ],
            "outcome": "PASS" if not findings else "FAIL",
            "scope": "synthetic-water-planning-status-collapse-only",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate synthetic water-planning status-collapse fixtures."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)

    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        findings = validate_file(path)
        print(_serialize(path, findings))
        failed = failed or bool(findings)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
