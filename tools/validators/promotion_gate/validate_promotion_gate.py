#!/usr/bin/env python3
"""Evaluate a synthetic or assembled promotion packet without promoting it.

The validator is deliberately side-effect free. It checks declared closure and
cross-field consistency, emits finite readiness findings, and never writes a
PromotionDecision, release record, receipt, proof, or published artifact.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (
    Finding,
    add_finding,
    is_finite_number,
    is_nonempty_string,
    validate_fixture_file,
)


FIXTURES_ROOT = REPO_ROOT / "fixtures/release/promotion_gate"
SCOPE = "release.promotion_gate"
GATE_ORDER = ("A", "B", "C", "D", "E", "F", "G")
STATUS_PRECEDENCE = {"PASS": 0, "ABSTAIN": 1, "DENY": 2, "ERROR": 3}
HASH_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")

TOP_LEVEL_FIELDS = frozenset(
    {
        "profile_version",
        "candidate_id",
        "candidate_author",
        "spec_hash",
        "lifecycle",
        "release_manifest",
        "run_receipt",
        "geometry",
        "temporal",
        "policy_context",
        "evidence_refs",
        "attestation_refs",
        "catalog_refs",
        "review",
        "rollback",
        "ai_mediation",
        "correction",
    }
)

CODE_META: dict[str, tuple[str, str]] = {
    "FIXTURE_JSON_INVALID": ("INPUT", "ERROR"),
    "FIXTURE_TOO_LARGE": ("INPUT", "ERROR"),
    "PG_INPUT_DOCUMENT_INVALID": ("INPUT", "ERROR"),
    "PG_A_UNDECLARED_FIELD": ("A", "DENY"),
    "PG_A_PROFILE_VERSION_INVALID": ("A", "DENY"),
    "PG_A_CANDIDATE_ID_MISSING": ("A", "DENY"),
    "PG_A_CANDIDATE_AUTHOR_MISSING": ("A", "DENY"),
    "PG_A_SPEC_HASH_INVALID": ("A", "DENY"),
    "PG_A_LIFECYCLE_BOUNDARY_INVALID": ("A", "DENY"),
    "PG_A_RELEASE_MANIFEST_MISSING": ("A", "DENY"),
    "PG_A_RELEASE_MANIFEST_INVALID": ("A", "DENY"),
    "PG_B_UNDECLARED_FIELD": ("B", "DENY"),
    "PG_B_RUN_RECEIPT_MISSING": ("B", "DENY"),
    "PG_B_RUN_RECEIPT_INVALID": ("B", "DENY"),
    "PG_B_SPEC_HASH_MISMATCH": ("B", "DENY"),
    "PG_B_ARTIFACT_DIGEST_INVALID": ("B", "DENY"),
    "PG_B_ARTIFACT_DIGEST_DUPLICATE": ("B", "DENY"),
    "PG_B_ARTIFACT_SET_MISMATCH": ("B", "DENY"),
    "PG_C_UNDECLARED_FIELD": ("C", "DENY"),
    "PG_C_GEOMETRY_INVALID": ("C", "DENY"),
    "PG_C_GEOMETRY_NONDETERMINISTIC": ("C", "DENY"),
    "PG_C_CRS_INVALID": ("C", "DENY"),
    "PG_C_BBOX_INVALID": ("C", "DENY"),
    "PG_D_UNDECLARED_FIELD": ("D", "DENY"),
    "PG_D_TEMPORAL_INVALID": ("D", "DENY"),
    "PG_D_TEMPORAL_ORDER_INVALID": ("D", "DENY"),
    "PG_E_UNDECLARED_FIELD": ("E", "DENY"),
    "PG_E_POLICY_CONTEXT_INVALID": ("E", "DENY"),
    "PG_E_POLICY_PROFILE_UNKNOWN": ("E", "DENY"),
    "PG_E_POLICY_LABEL_UNKNOWN": ("E", "DENY"),
    "PG_E_PUBLIC_SAFE_LABEL_INVALID": ("E", "DENY"),
    "PG_E_POLICY_DENY": ("E", "DENY"),
    "PG_E_POLICY_EVALUATION_ERROR": ("E", "ERROR"),
    "PG_F_UNDECLARED_FIELD": ("F", "DENY"),
    "PG_F_EVIDENCE_REF_MISSING": ("F", "ABSTAIN"),
    "PG_F_ATTESTATION_REF_MISSING": ("F", "DENY"),
    "PG_F_CATALOG_CLOSURE_MISSING": ("F", "DENY"),
    "PG_F_AI_RECEIPT_MISSING": ("F", "DENY"),
    "PG_G_UNDECLARED_FIELD": ("G", "DENY"),
    "PG_G_REVIEW_INVALID": ("G", "DENY"),
    "PG_G_REVIEW_NOT_APPROVED": ("G", "DENY"),
    "PG_G_SEPARATION_OF_DUTIES_INVALID": ("G", "DENY"),
    "PG_G_ROLLBACK_INVALID": ("G", "DENY"),
    "PG_G_ROLLBACK_TARGET_INVALID": ("G", "DENY"),
    "PG_G_CORRECTION_LINK_MISSING": ("G", "ABSTAIN"),
}


def _add(findings: set[Finding], code: str, path: str) -> None:
    if code not in CODE_META:
        raise AssertionError(f"unregistered promotion-gate code: {code}")
    add_finding(findings, code, path)


def _unknown_fields(
    findings: set[Finding],
    candidate: dict[object, object],
    allowed: frozenset[str],
    *,
    path: str,
    code: str,
) -> None:
    for key in sorted(candidate, key=lambda value: (type(value).__name__, repr(value))):
        if key not in allowed:
            # The untrusted key itself may contain sensitive text. Report only
            # the bounded parent path; multiple unknown keys collapse safely.
            _add(findings, code, path)


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


def _string_list(value: object) -> list[str] | None:
    if not isinstance(value, list):
        return None
    if not all(is_nonempty_string(item) for item in value):
        return None
    return [item for item in value if isinstance(item, str)]


def _validate_identity(candidate: dict[str, object], findings: set[Finding]) -> None:
    _unknown_fields(
        findings,
        candidate,
        TOP_LEVEL_FIELDS,
        path="$",
        code="PG_A_UNDECLARED_FIELD",
    )
    if candidate.get("profile_version") != "v1":
        _add(findings, "PG_A_PROFILE_VERSION_INVALID", "$.profile_version")
    if not is_nonempty_string(candidate.get("candidate_id")):
        _add(findings, "PG_A_CANDIDATE_ID_MISSING", "$.candidate_id")
    if not is_nonempty_string(candidate.get("candidate_author")):
        _add(findings, "PG_A_CANDIDATE_AUTHOR_MISSING", "$.candidate_author")
    if not _valid_hash(candidate.get("spec_hash")):
        _add(findings, "PG_A_SPEC_HASH_INVALID", "$.spec_hash")

    lifecycle = candidate.get("lifecycle")
    if not isinstance(lifecycle, dict):
        _add(findings, "PG_A_LIFECYCLE_BOUNDARY_INVALID", "$.lifecycle")
    else:
        _unknown_fields(
            findings,
            lifecycle,
            frozenset({"from", "to"}),
            path="$.lifecycle",
            code="PG_A_UNDECLARED_FIELD",
        )
        if lifecycle.get("from") not in {"CATALOG", "TRIPLET"} or lifecycle.get(
            "to"
        ) != "PUBLISHED":
            _add(findings, "PG_A_LIFECYCLE_BOUNDARY_INVALID", "$.lifecycle")

    manifest = candidate.get("release_manifest")
    if manifest is None:
        _add(findings, "PG_A_RELEASE_MANIFEST_MISSING", "$.release_manifest")
    elif not isinstance(manifest, dict):
        _add(findings, "PG_A_RELEASE_MANIFEST_INVALID", "$.release_manifest")
    else:
        _unknown_fields(
            findings,
            manifest,
            frozenset({"id", "spec_hash", "artifact_digests"}),
            path="$.release_manifest",
            code="PG_A_UNDECLARED_FIELD",
        )
        if not is_nonempty_string(manifest.get("id")) or not _valid_hash(
            manifest.get("spec_hash")
        ):
            _add(findings, "PG_A_RELEASE_MANIFEST_INVALID", "$.release_manifest")


def _validate_integrity(candidate: dict[str, object], findings: set[Finding]) -> None:
    receipt = candidate.get("run_receipt")
    if receipt is None:
        _add(findings, "PG_B_RUN_RECEIPT_MISSING", "$.run_receipt")
        return
    if not isinstance(receipt, dict):
        _add(findings, "PG_B_RUN_RECEIPT_INVALID", "$.run_receipt")
        return
    _unknown_fields(
        findings,
        receipt,
        frozenset({"id", "spec_hash", "output_digests"}),
        path="$.run_receipt",
        code="PG_B_UNDECLARED_FIELD",
    )
    if not is_nonempty_string(receipt.get("id")) or not _valid_hash(
        receipt.get("spec_hash")
    ):
        _add(findings, "PG_B_RUN_RECEIPT_INVALID", "$.run_receipt")

    candidate_hash = candidate.get("spec_hash")
    manifest = candidate.get("release_manifest")
    manifest_hash = manifest.get("spec_hash") if isinstance(manifest, dict) else None
    receipt_hash = receipt.get("spec_hash")
    if _valid_hash(candidate_hash) and (
        manifest_hash != candidate_hash or receipt_hash != candidate_hash
    ):
        _add(findings, "PG_B_SPEC_HASH_MISMATCH", "$.spec_hash")

    manifest_digests = (
        _string_list(manifest.get("artifact_digests"))
        if isinstance(manifest, dict)
        else None
    )
    receipt_digests = _string_list(receipt.get("output_digests"))
    for path, digests in (
        ("$.release_manifest.artifact_digests", manifest_digests),
        ("$.run_receipt.output_digests", receipt_digests),
    ):
        if not digests or not all(_valid_hash(digest) for digest in digests):
            _add(findings, "PG_B_ARTIFACT_DIGEST_INVALID", path)
        elif len(digests) != len(set(digests)):
            _add(findings, "PG_B_ARTIFACT_DIGEST_DUPLICATE", path)
    if manifest_digests and receipt_digests and sorted(manifest_digests) != sorted(
        receipt_digests
    ):
        _add(findings, "PG_B_ARTIFACT_SET_MISMATCH", "$.run_receipt.output_digests")


def _validate_geometry(candidate: dict[str, object], findings: set[Finding]) -> None:
    geometry = candidate.get("geometry")
    if not isinstance(geometry, dict):
        _add(findings, "PG_C_GEOMETRY_INVALID", "$.geometry")
        return
    _unknown_fields(
        findings,
        geometry,
        frozenset({"valid", "deterministic", "crs", "bbox"}),
        path="$.geometry",
        code="PG_C_UNDECLARED_FIELD",
    )
    if geometry.get("valid") is not True:
        _add(findings, "PG_C_GEOMETRY_INVALID", "$.geometry.valid")
    if geometry.get("deterministic") is not True:
        _add(findings, "PG_C_GEOMETRY_NONDETERMINISTIC", "$.geometry.deterministic")
    if geometry.get("crs") != "EPSG:4326":
        _add(findings, "PG_C_CRS_INVALID", "$.geometry.crs")
    bbox = geometry.get("bbox")
    valid_bbox = (
        isinstance(bbox, list)
        and len(bbox) == 4
        and all(is_finite_number(value) for value in bbox)
    )
    if valid_bbox:
        min_x, min_y, max_x, max_y = bbox
        valid_bbox = (
            -180 <= min_x < max_x <= 180 and -90 <= min_y < max_y <= 90
        )
    if not valid_bbox:
        _add(findings, "PG_C_BBOX_INVALID", "$.geometry.bbox")


def _validate_temporal(candidate: dict[str, object], findings: set[Finding]) -> None:
    temporal = candidate.get("temporal")
    if not isinstance(temporal, dict):
        _add(findings, "PG_D_TEMPORAL_INVALID", "$.temporal")
        return
    _unknown_fields(
        findings,
        temporal,
        frozenset({"start", "end"}),
        path="$.temporal",
        code="PG_D_UNDECLARED_FIELD",
    )
    start = _strict_utc_timestamp(temporal.get("start"))
    end = _strict_utc_timestamp(temporal.get("end"))
    if start is None or end is None:
        _add(findings, "PG_D_TEMPORAL_INVALID", "$.temporal")
    elif start > end:
        _add(findings, "PG_D_TEMPORAL_ORDER_INVALID", "$.temporal")


def _validate_policy(candidate: dict[str, object], findings: set[Finding]) -> None:
    context = candidate.get("policy_context")
    if not isinstance(context, dict):
        _add(findings, "PG_E_POLICY_CONTEXT_INVALID", "$.policy_context")
        return
    _unknown_fields(
        findings,
        context,
        frozenset({"profile", "labels", "evaluation", "policy_bundle"}),
        path="$.policy_context",
        code="PG_E_UNDECLARED_FIELD",
    )
    profile = context.get("profile")
    if profile not in {"public-safe", "internal", "restricted"}:
        _add(findings, "PG_E_POLICY_PROFILE_UNKNOWN", "$.policy_context.profile")
    labels = _string_list(context.get("labels"))
    known_labels = {"public", "internal", "restricted", "sensitive"}
    if labels is None or any(label not in known_labels for label in labels):
        _add(findings, "PG_E_POLICY_LABEL_UNKNOWN", "$.policy_context.labels")
    elif profile == "public-safe" and set(labels) != {"public"}:
        _add(findings, "PG_E_PUBLIC_SAFE_LABEL_INVALID", "$.policy_context.labels")
    if not is_nonempty_string(context.get("policy_bundle")):
        _add(findings, "PG_E_POLICY_CONTEXT_INVALID", "$.policy_context.policy_bundle")
    evaluation = context.get("evaluation")
    if evaluation == "ERROR":
        _add(findings, "PG_E_POLICY_EVALUATION_ERROR", "$.policy_context.evaluation")
    elif evaluation == "DENY":
        _add(findings, "PG_E_POLICY_DENY", "$.policy_context.evaluation")
    elif evaluation != "PASS":
        _add(findings, "PG_E_POLICY_CONTEXT_INVALID", "$.policy_context.evaluation")


def _validate_proof_closure(candidate: dict[str, object], findings: set[Finding]) -> None:
    evidence_refs = _string_list(candidate.get("evidence_refs"))
    if not evidence_refs:
        _add(findings, "PG_F_EVIDENCE_REF_MISSING", "$.evidence_refs")
    attestation_refs = _string_list(candidate.get("attestation_refs"))
    if not attestation_refs:
        _add(findings, "PG_F_ATTESTATION_REF_MISSING", "$.attestation_refs")

    catalog_refs = candidate.get("catalog_refs")
    if not isinstance(catalog_refs, dict):
        _add(findings, "PG_F_CATALOG_CLOSURE_MISSING", "$.catalog_refs")
    else:
        _unknown_fields(
            findings,
            catalog_refs,
            frozenset({"stac", "dcat", "prov"}),
            path="$.catalog_refs",
            code="PG_F_UNDECLARED_FIELD",
        )
        for key in ("stac", "dcat", "prov"):
            if not _string_list(catalog_refs.get(key)):
                _add(
                    findings,
                    "PG_F_CATALOG_CLOSURE_MISSING",
                    f"$.catalog_refs.{key}",
                )

    ai_mediation = candidate.get("ai_mediation")
    if not isinstance(ai_mediation, dict):
        _add(findings, "PG_F_AI_RECEIPT_MISSING", "$.ai_mediation")
    else:
        _unknown_fields(
            findings,
            ai_mediation,
            frozenset({"used", "receipt_ref"}),
            path="$.ai_mediation",
            code="PG_F_UNDECLARED_FIELD",
        )
        used = ai_mediation.get("used")
        if not isinstance(used, bool) or (
            used and not is_nonempty_string(ai_mediation.get("receipt_ref"))
        ):
            _add(findings, "PG_F_AI_RECEIPT_MISSING", "$.ai_mediation.receipt_ref")


def _validate_review_and_rollback(
    candidate: dict[str, object], findings: set[Finding]
) -> None:
    review = candidate.get("review")
    if not isinstance(review, dict):
        _add(findings, "PG_G_REVIEW_INVALID", "$.review")
    else:
        _unknown_fields(
            findings,
            review,
            frozenset({"status", "reviewer", "ticket"}),
            path="$.review",
            code="PG_G_UNDECLARED_FIELD",
        )
        if review.get("status") != "APPROVED":
            _add(findings, "PG_G_REVIEW_NOT_APPROVED", "$.review.status")
        if not is_nonempty_string(review.get("reviewer")) or not is_nonempty_string(
            review.get("ticket")
        ):
            _add(findings, "PG_G_REVIEW_INVALID", "$.review")
        if is_nonempty_string(candidate.get("candidate_author")) and review.get(
            "reviewer"
        ) == candidate.get("candidate_author"):
            _add(findings, "PG_G_SEPARATION_OF_DUTIES_INVALID", "$.review.reviewer")

    rollback = candidate.get("rollback")
    if not isinstance(rollback, dict):
        _add(findings, "PG_G_ROLLBACK_INVALID", "$.rollback")
    else:
        _unknown_fields(
            findings,
            rollback,
            frozenset({"card_ref", "target_spec_hash"}),
            path="$.rollback",
            code="PG_G_UNDECLARED_FIELD",
        )
        if not is_nonempty_string(rollback.get("card_ref")) or not _valid_hash(
            rollback.get("target_spec_hash")
        ):
            _add(findings, "PG_G_ROLLBACK_INVALID", "$.rollback")
        elif rollback.get("target_spec_hash") == candidate.get("spec_hash"):
            _add(
                findings,
                "PG_G_ROLLBACK_TARGET_INVALID",
                "$.rollback.target_spec_hash",
            )

    correction = candidate.get("correction")
    if not isinstance(correction, dict):
        _add(findings, "PG_G_CORRECTION_LINK_MISSING", "$.correction")
    else:
        _unknown_fields(
            findings,
            correction,
            frozenset({"supersedes_prior", "notice_ref"}),
            path="$.correction",
            code="PG_G_UNDECLARED_FIELD",
        )
        supersedes = correction.get("supersedes_prior")
        if not isinstance(supersedes, bool) or (
            supersedes and not is_nonempty_string(correction.get("notice_ref"))
        ):
            _add(
                findings,
                "PG_G_CORRECTION_LINK_MISSING",
                "$.correction.notice_ref",
            )


def validate_document(candidate: object) -> list[Finding]:
    """Validate one declared promotion packet with stable, value-free findings."""

    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        _add(findings, "PG_INPUT_DOCUMENT_INVALID", "$")
        return sorted(findings)
    _validate_identity(candidate, findings)
    _validate_integrity(candidate, findings)
    _validate_geometry(candidate, findings)
    _validate_temporal(candidate, findings)
    _validate_policy(candidate, findings)
    _validate_proof_closure(candidate, findings)
    _validate_review_and_rollback(candidate, findings)
    return sorted(findings)


def validate_candidate_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def _status_for(findings: Iterable[Finding]) -> str:
    statuses = [CODE_META[finding.code][1] for finding in findings]
    return max(statuses, key=STATUS_PRECEDENCE.get, default="PASS")


def result_payload(path: Path | str, findings: list[Finding]) -> dict[str, object]:
    status = _status_for(findings)
    gate_findings = {
        gate: [finding for finding in findings if CODE_META[finding.code][0] == gate]
        for gate in GATE_ORDER
    }
    input_error = any(CODE_META[finding.code][0] == "INPUT" for finding in findings)
    gates = []
    for gate in GATE_ORDER:
        gate_status = "NOT_EVALUATED" if input_error else _status_for(gate_findings[gate])
        gates.append({"gate": gate, "status": gate_status})
    return {
        "file": str(path),
        "findings": [
            {
                "code": finding.code,
                "gate": CODE_META[finding.code][0],
                "path": finding.path,
                "status": CODE_META[finding.code][1],
            }
            for finding in sorted(findings)
        ],
        "gates": gates,
        "readiness": "APPROVE_READY" if status == "PASS" else "BLOCKED",
        "scope": SCOPE,
        "status": status,
    }


def serialize_result(path: Path | str, findings: list[Finding]) -> str:
    return json.dumps(
        result_payload(path, findings),
        sort_keys=True,
        separators=(",", ":"),
    )


def _expected_fixture_status(path: Path) -> str | None:
    prefix = path.name.split("__", 1)[0].upper()
    return prefix if prefix in STATUS_PRECEDENCE else None


def _run_fixture_suite() -> int:
    ok = True
    files = sorted(FIXTURES_ROOT.glob("*/*.json"))
    if not files:
        print(f"FAIL {FIXTURES_ROOT}: no JSON fixtures found")
        return 1
    for path in files:
        expected = _expected_fixture_status(path)
        if expected is None:
            print(f"FAIL {path}: fixture filename must start with a finite status")
            ok = False
            continue
        findings = validate_candidate_file(path)
        actual = _status_for(findings)
        if actual == expected:
            label = "OK" if actual == "PASS" else f"EXPECTED_{actual}"
            print(f"{label} {path}")
        else:
            print(serialize_result(path, findings))
            print(f"FAIL {path}: expected {expected}, got {actual}")
            ok = False
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate KFM promotion-gate readiness without promoting anything."
    )
    parser.add_argument("files", nargs="*", type=Path, help="promotion packet JSON")
    parser.add_argument(
        "--fixtures",
        action="store_true",
        help="verify the repository-owned synthetic fixture matrix",
    )
    args = parser.parse_args(sys.argv[1:] if argv is None else argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures cannot be combined with file arguments")
        return _run_fixture_suite()
    if not args.files:
        parser.error("at least one promotion packet or --fixtures is required")

    exit_code = 0
    for path in sorted(args.files, key=lambda item: str(item)):
        findings = validate_candidate_file(path)
        status = _status_for(findings)
        print(serialize_result(path, findings))
        exit_code = max(exit_code, 2 if status == "ERROR" else 1 if status != "PASS" else 0)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
