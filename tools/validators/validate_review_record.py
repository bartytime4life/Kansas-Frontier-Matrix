#!/usr/bin/env python3
"""Validate the fixture-only ReviewRecord projection used by promotion Gate G.

This module deliberately validates only repository-owned synthetic promotion
fixtures.  It composes the existing proposed ReviewRecord shape with bounded
IdentityToken and StewardshipAssignment projections, but it does not change or
claim authority for any canonical contract, schema, actor registry, policy,
review, promotion, release, or publication record.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (
    Finding,
    add_finding,
    is_nonempty_string,
    validate_fixture_file,
)


FIXTURES_ROOT = REPO_ROOT / "fixtures/release/promotion_gate"
SCOPE = "release.review_record.fixture_profile"
EXPECTED_REVIEW_SCOPE = "release.promotion_gate"
STATUS_PRECEDENCE = {"PASS": 0, "ABSTAIN": 1, "DENY": 2, "ERROR": 3}
HASH_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")

REVIEW_FIELDS = frozenset(
    {
        "record",
        "author_identity",
        "reviewer_identity",
        "authority",
        "scope",
        "valid_until",
        "superseded_by_review_id",
        "spec_hash",
        "artifact_digests",
    }
)
RECORD_FIELDS = frozenset(
    {
        "review_id",
        "subject_ref",
        "reviewer_role",
        "decision",
        "reasons",
        "obligations",
        "reviewed_at",
    }
)
IDENTITY_FIELDS = frozenset({"id", "kind", "issued_at", "issuer"})
AUTHORITY_FIELDS = frozenset(
    {
        "assignment_id",
        "assigned_to",
        "role",
        "scope",
        "status",
        "starts_at",
        "expires_at",
        "authority_basis_refs",
    }
)

CODE_STATUS: dict[str, str] = {
    "FIXTURE_JSON_INVALID": "ERROR",
    "FIXTURE_TOO_LARGE": "ERROR",
    "RR_INPUT_DOCUMENT_INVALID": "ERROR",
    "RR_CONTEXT_INVALID": "ERROR",
    "RR_UNDECLARED_FIELD": "DENY",
    "RR_RECORD_INVALID": "DENY",
    "RR_DECISION_NOT_APPROVED": "DENY",
    "RR_IDENTITY_INVALID": "DENY",
    "RR_SELF_REVIEW": "DENY",
    "RR_AUTHORITY_MISSING": "ABSTAIN",
    "RR_AUTHORITY_INVALID": "DENY",
    "RR_TEMPORAL_INVALID": "DENY",
    "RR_REVIEW_STALE": "DENY",
    "RR_REVIEW_SUPERSEDED": "DENY",
    "RR_SCOPE_MISMATCH": "DENY",
    "RR_SUBJECT_MISMATCH": "DENY",
    "RR_SPEC_HASH_UNBOUND": "DENY",
    "RR_ARTIFACT_HASH_UNBOUND": "DENY",
}


def _add(findings: set[Finding], code: str, path: str) -> None:
    if code not in CODE_STATUS:
        raise AssertionError(f"unregistered ReviewRecord code: {code}")
    add_finding(findings, code, path)


def _unknown_fields(
    findings: set[Finding],
    candidate: Mapping[object, object],
    allowed: frozenset[str],
    *,
    path: str,
) -> None:
    if any(key not in allowed for key in candidate):
        # Never echo an untrusted member name into a finding or result payload.
        _add(findings, "RR_UNDECLARED_FIELD", path)


def _strict_utc_timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return None
    return parsed.replace(tzinfo=timezone.utc)


def _valid_hash(value: object) -> bool:
    return isinstance(value, str) and HASH_PATTERN.fullmatch(value) is not None


def _string_list(value: object, *, allow_empty: bool = False) -> list[str] | None:
    if not isinstance(value, list) or not all(is_nonempty_string(item) for item in value):
        return None
    items = [item for item in value if isinstance(item, str)]
    return items if allow_empty or items else None


def _validate_identity(
    value: object,
    findings: set[Finding],
    *,
    path: str,
) -> str | None:
    if not isinstance(value, dict):
        _add(findings, "RR_IDENTITY_INVALID", path)
        return None
    _unknown_fields(findings, value, IDENTITY_FIELDS, path=path)
    actor_id = value.get("id")
    if (
        not is_nonempty_string(actor_id)
        or value.get("kind") != "actor"
        or _strict_utc_timestamp(value.get("issued_at")) is None
        or ("issuer" in value and not is_nonempty_string(value.get("issuer")))
    ):
        _add(findings, "RR_IDENTITY_INVALID", path)
        return None
    return actor_id if isinstance(actor_id, str) else None


def _validate_record(
    value: object,
    findings: set[Finding],
    *,
    path: str,
) -> tuple[dict[str, object] | None, datetime | None]:
    if not isinstance(value, dict):
        _add(findings, "RR_RECORD_INVALID", path)
        return None, None
    _unknown_fields(findings, value, RECORD_FIELDS, path=path)
    reasons = _string_list(value.get("reasons"))
    obligations = _string_list(value.get("obligations"), allow_empty=True)
    reviewed_at = _strict_utc_timestamp(value.get("reviewed_at"))
    if (
        not is_nonempty_string(value.get("review_id"))
        or not is_nonempty_string(value.get("subject_ref"))
        or value.get("reviewer_role") not in {"steward", "reviewer", "auditor"}
        or reasons is None
        or obligations is None
        or reviewed_at is None
    ):
        _add(findings, "RR_RECORD_INVALID", path)
    if value.get("decision") != "approve":
        _add(findings, "RR_DECISION_NOT_APPROVED", f"{path}.decision")
    return value, reviewed_at


def _validate_authority(
    value: object,
    findings: set[Finding],
    *,
    reviewer_id: str | None,
    reviewer_role: object,
    expected_scope: str,
    reviewed_at: datetime | None,
    path: str,
) -> None:
    if value is None:
        _add(findings, "RR_AUTHORITY_MISSING", path)
        return
    if not isinstance(value, dict):
        _add(findings, "RR_AUTHORITY_INVALID", path)
        return
    _unknown_fields(findings, value, AUTHORITY_FIELDS, path=path)
    starts_at = _strict_utc_timestamp(value.get("starts_at"))
    expires_at = _strict_utc_timestamp(value.get("expires_at"))
    basis_refs = _string_list(value.get("authority_basis_refs"))
    if (
        not is_nonempty_string(value.get("assignment_id"))
        or value.get("assigned_to") != reviewer_id
        or value.get("role") != reviewer_role
        or value.get("scope") != expected_scope
        or value.get("status") != "ACTIVE"
        or starts_at is None
        or expires_at is None
        or basis_refs is None
    ):
        _add(findings, "RR_AUTHORITY_INVALID", path)
    if (
        starts_at is None
        or expires_at is None
        or reviewed_at is None
        or not starts_at <= reviewed_at <= expires_at
    ):
        _add(findings, "RR_TEMPORAL_INVALID", path)


def validate_review(
    review: object,
    *,
    expected_subject_ref: str,
    expected_author_actor_id: str,
    expected_scope: str,
    expected_spec_hash: str,
    expected_artifact_digests: Sequence[str],
    evaluated_at: datetime,
) -> list[Finding]:
    """Validate one embedded, synthetic ReviewRecord fixture projection."""

    findings: set[Finding] = set()
    if not isinstance(review, dict):
        _add(findings, "RR_RECORD_INVALID", "$.review")
        return sorted(findings)
    _unknown_fields(findings, review, REVIEW_FIELDS, path="$.review")

    record, reviewed_at = _validate_record(
        review.get("record"), findings, path="$.review.record"
    )
    author_id = _validate_identity(
        review.get("author_identity"), findings, path="$.review.author_identity"
    )
    reviewer_id = _validate_identity(
        review.get("reviewer_identity"), findings, path="$.review.reviewer_identity"
    )

    reviewer_role = record.get("reviewer_role") if record is not None else None
    _validate_authority(
        review.get("authority"),
        findings,
        reviewer_id=reviewer_id,
        reviewer_role=reviewer_role,
        expected_scope=expected_scope,
        reviewed_at=reviewed_at,
        path="$.review.authority",
    )

    if author_id != expected_author_actor_id:
        _add(findings, "RR_IDENTITY_INVALID", "$.review.author_identity")
    if author_id is not None and reviewer_id is not None and author_id == reviewer_id:
        _add(findings, "RR_SELF_REVIEW", "$.review.reviewer_identity")

    if review.get("scope") != expected_scope:
        _add(findings, "RR_SCOPE_MISMATCH", "$.review.scope")
    if record is not None and record.get("subject_ref") != expected_subject_ref:
        _add(findings, "RR_SUBJECT_MISMATCH", "$.review.record.subject_ref")

    valid_until = _strict_utc_timestamp(review.get("valid_until"))
    if reviewed_at is None or valid_until is None or reviewed_at > evaluated_at:
        _add(findings, "RR_TEMPORAL_INVALID", "$.review.valid_until")
    elif evaluated_at > valid_until:
        _add(findings, "RR_REVIEW_STALE", "$.review.valid_until")

    superseded_by = review.get("superseded_by_review_id")
    if superseded_by is not None:
        if not is_nonempty_string(superseded_by):
            _add(findings, "RR_RECORD_INVALID", "$.review.superseded_by_review_id")
        else:
            _add(findings, "RR_REVIEW_SUPERSEDED", "$.review.superseded_by_review_id")

    if not _valid_hash(review.get("spec_hash")) or review.get(
        "spec_hash"
    ) != expected_spec_hash:
        _add(findings, "RR_SPEC_HASH_UNBOUND", "$.review.spec_hash")

    artifact_digests = _string_list(review.get("artifact_digests"))
    if (
        artifact_digests is None
        or not all(_valid_hash(item) for item in artifact_digests)
        or len(artifact_digests) != len(set(artifact_digests))
        or sorted(artifact_digests) != sorted(expected_artifact_digests)
    ):
        _add(findings, "RR_ARTIFACT_HASH_UNBOUND", "$.review.artifact_digests")

    return sorted(findings)


def review_context_from_packet(
    candidate: Mapping[str, object],
) -> dict[str, object] | None:
    manifest = candidate.get("release_manifest")
    if not isinstance(manifest, dict):
        return None
    artifact_digests = _string_list(manifest.get("artifact_digests"))
    evaluated_at = _strict_utc_timestamp(candidate.get("gate_evaluated_at"))
    required_strings = (
        candidate.get("candidate_id"),
        candidate.get("candidate_author"),
        candidate.get("spec_hash"),
    )
    if (
        not all(is_nonempty_string(item) for item in required_strings)
        or not _valid_hash(candidate.get("spec_hash"))
        or artifact_digests is None
        or not all(_valid_hash(item) for item in artifact_digests)
        or evaluated_at is None
    ):
        return None
    return {
        "expected_subject_ref": candidate["candidate_id"],
        "expected_author_actor_id": candidate["candidate_author"],
        "expected_scope": EXPECTED_REVIEW_SCOPE,
        "expected_spec_hash": candidate["spec_hash"],
        "expected_artifact_digests": artifact_digests,
        "evaluated_at": evaluated_at,
    }


def validate_packet_document(candidate: object) -> list[Finding]:
    """Validate only the ReviewRecord projection inside a promotion fixture."""

    if not isinstance(candidate, dict):
        return [Finding("RR_INPUT_DOCUMENT_INVALID", "$")]
    context = review_context_from_packet(candidate)
    if context is None:
        return [Finding("RR_CONTEXT_INVALID", "$")]
    return validate_review(candidate.get("review"), **context)  # type: ignore[arg-type]


def validate_packet_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_packet_document)


def status_for(findings: Iterable[Finding]) -> str:
    statuses = [CODE_STATUS[finding.code] for finding in findings]
    return max(statuses, key=STATUS_PRECEDENCE.get, default="PASS")


def result_payload(path: Path | str, findings: Sequence[Finding]) -> dict[str, object]:
    return {
        "file": str(path),
        "findings": [
            {
                "code": finding.code,
                "path": finding.path,
                "status": CODE_STATUS[finding.code],
            }
            for finding in sorted(findings)
        ],
        "scope": SCOPE,
        "status": status_for(findings),
    }


def serialize_result(path: Path | str, findings: Sequence[Finding]) -> str:
    return json.dumps(
        result_payload(path, findings), sort_keys=True, separators=(",", ":")
    )


def _review_fixture_paths() -> list[Path]:
    paths = [FIXTURES_ROOT / "valid/pass__complete_candidate.json"]
    paths.extend(sorted((FIXTURES_ROOT / "invalid").glob("*review*.json")))
    return paths


def _expected_fixture_status(path: Path) -> str | None:
    prefix = path.name.split("__", 1)[0].upper()
    return prefix if prefix in STATUS_PRECEDENCE else None


def _run_fixture_suite() -> int:
    ok = True
    files = _review_fixture_paths()
    if not files or any(not path.is_file() for path in files):
        print("FAIL: ReviewRecord fixture profile is incomplete")
        return 1
    for path in files:
        expected = _expected_fixture_status(path)
        findings = validate_packet_file(path)
        actual = status_for(findings)
        if expected is not None and actual == expected:
            label = "OK" if actual == "PASS" else f"EXPECTED_{actual}"
            print(f"{label} {path}")
        else:
            print(serialize_result(path, findings))
            print(f"FAIL {path}: expected {expected}, got {actual}")
            ok = False
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate fixture-only ReviewRecord projections without creating review "
            "or release authority."
        )
    )
    parser.add_argument("files", nargs="*", type=Path, help="promotion fixture JSON")
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="verify the repository-owned synthetic ReviewRecord fixture matrix",
    )
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with file arguments")
        return _run_fixture_suite()
    if not args.files:
        parser.error("at least one promotion fixture or --fixtures is required")

    exit_code = 0
    for path in sorted(args.files, key=lambda item: str(item)):
        findings = validate_packet_file(path)
        status = status_for(findings)
        print(serialize_result(path, findings))
        exit_code = max(
            exit_code, 2 if status == "ERROR" else 1 if status != "PASS" else 0
        )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
