"""Build and validate fixture-only optimistic conditional-write preflights.

No target is contacted, no request is emitted, and no write, lifecycle, policy,
review, promotion, release, publication, or public-use authority is created.
"""
from __future__ import annotations

import argparse, json, sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
for p in (REPO_ROOT, REPO_ROOT / "packages/hashing/src"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
from hashing import CanonicalizationFailure, JsonInputError, compute_spec_hash, load_json_file

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/release/conditional_write_preflight.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/release/conditional_write_preflight"
CASES_PATH = FIXTURE_ROOT / "cases.json"
VALID_PATH = FIXTURE_ROOT / "valid/valid_propose_write.json"
INVALID_PATH = FIXTURE_ROOT / "invalid/invalid_authority_overreach.json"
PROFILE = "kfm.release.conditional-write-preflight.v1"
OBJECT_TYPE = "ConditionalWritePreflightCandidate"
EXECUTION_MODE = "FIXTURE_ONLY"
SCOPE = "release.conditional_write_preflight_candidate"
NON_EFFECTS = (
    "no_network_access", "no_external_state_resolution", "no_write_request_emission",
    "no_write_or_lifecycle_mutation", "no_policy_review_or_promotion_authority",
    "no_release_deployment_publication_or_public_use",
)

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str

@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    intent_id: str | None = None

def _m(value: object, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{label} must be an object")
    return value

def _s(value: object, label: str, optional: bool = False) -> str | None:
    if optional and value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")
    return value.strip()

def _i(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{label} must be a positive integer")
    return value

def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())

def _path(parts: Sequence[object]) -> str:
    out = "$"
    for part in parts:
        out += f"[{part}]" if isinstance(part, int) else "." + str(part)
    return out

def _keys(target: Mapping[str, Any], request: Mapping[str, Any]) -> tuple[str, str]:
    idem = compute_spec_hash({
        "target_ref": target["target_ref"], "operation": target["operation"],
        "proposed_content_digest": request["proposed_content_digest"],
    })
    condition = compute_spec_hash({
        "target_ref": target["target_ref"], "operation": target["operation"],
        "observed_state": target["observed_state"], "observed_etag": target["observed_etag"],
        "expected_etag": request["expected_etag"],
    })
    return idem, condition

def _derive(target: Mapping[str, Any], request: Mapping[str, Any], upstream: Mapping[str, Any]) -> dict[str, object]:
    op = _s(target.get("operation"), "target.operation")
    state = _s(target.get("observed_state"), "target.observed_state")
    observed_etag = _s(target.get("observed_etag"), "target.observed_etag", True)
    observed_digest = _s(target.get("observed_content_digest"), "target.observed_content_digest", True)
    expected_etag = _s(request.get("expected_etag"), "request.expected_etag", True)
    proposed_digest = _s(request.get("proposed_content_digest"), "request.proposed_content_digest")
    _i(request.get("proposed_content_length"), "request.proposed_content_length")
    if op not in {"CREATE_IF_ABSENT", "REPLACE_IF_MATCH"} or state not in {"ABSENT", "PRESENT"}:
        raise ValueError("unsupported target declaration")
    if state == "ABSENT" and (observed_etag is not None or observed_digest is not None):
        raise ValueError("ABSENT target cannot carry observed identity")
    if state == "PRESENT" and (observed_etag is None or observed_digest is None):
        raise ValueError("PRESENT target requires observed identity")
    if op == "CREATE_IF_ABSENT" and expected_etag is not None:
        raise ValueError("CREATE_IF_ABSENT cannot carry expected_etag")
    if op == "REPLACE_IF_MATCH" and expected_etag is None:
        raise ValueError("REPLACE_IF_MATCH requires expected_etag")

    blockers = set()
    if upstream.get("policy_outcome") != "ALLOW": blockers.add("POLICY_NOT_ALLOWED")
    if upstream.get("review_state") != "APPROVED": blockers.add("REVIEW_NOT_APPROVED")
    if upstream.get("promotion_state") != "APPROVED": blockers.add("PROMOTION_NOT_APPROVED")
    if upstream.get("release_manifest_candidate_ref") is None: blockers.add("RELEASE_MANIFEST_MISSING")
    if upstream.get("rollback_ref") is None: blockers.add("ROLLBACK_TARGET_MISSING")

    if blockers:
        outcome, reasons = "HOLD", sorted(blockers)
    elif state == "PRESENT" and observed_digest == proposed_digest:
        outcome, reasons = "NO_ACTION", ["CONTENT_ALREADY_PRESENT"]
    elif op == "CREATE_IF_ABSENT":
        outcome, reasons = (("PROPOSE_WRITE", ["CONDITION_SATISFIED"]) if state == "ABSENT"
                            else ("CONFLICT", ["TARGET_EXISTS"]))
    elif state == "ABSENT":
        outcome, reasons = "CONFLICT", ["TARGET_ABSENT"]
    elif observed_etag != expected_etag:
        outcome, reasons = "CONFLICT", ["ETAG_MISMATCH"]
    else:
        outcome, reasons = "PROPOSE_WRITE", ["CONDITION_SATISFIED"]
    headers = ({"if_match": None, "if_none_match": "*"} if op == "CREATE_IF_ABSENT"
               else {"if_match": expected_etag, "if_none_match": None})
    return {"outcome": outcome, "reason_codes": reasons, "request_headers": headers,
            "condition_fingerprint": _keys(target, request)[1]}

def build_candidate(case: Mapping[str, Any]) -> dict[str, object]:
    tr, rr, ur = _m(case.get("target"), "target"), _m(case.get("request"), "request"), _m(case.get("upstream"), "upstream")
    target = {
        "target_ref": _s(tr.get("target_ref"), "target.target_ref"),
        "operation": _s(tr.get("operation"), "target.operation"),
        "observed_state": _s(tr.get("observed_state"), "target.observed_state"),
        "observed_etag": _s(tr.get("observed_etag"), "target.observed_etag", True),
        "observed_content_digest": _s(tr.get("observed_content_digest"), "target.observed_content_digest", True),
    }
    request = {
        "expected_etag": _s(rr.get("expected_etag"), "request.expected_etag", True),
        "proposed_content_digest": _s(rr.get("proposed_content_digest"), "request.proposed_content_digest"),
        "proposed_content_length": _i(rr.get("proposed_content_length"), "request.proposed_content_length"),
        "content_type": _s(rr.get("content_type"), "request.content_type"), "idempotency_key": "",
    }
    upstream = {
        "policy_decision_ref": _s(ur.get("policy_decision_ref"), "upstream.policy_decision_ref"),
        "policy_outcome": _s(ur.get("policy_outcome"), "upstream.policy_outcome"),
        "review_record_ref": _s(ur.get("review_record_ref"), "upstream.review_record_ref"),
        "review_state": _s(ur.get("review_state"), "upstream.review_state"),
        "promotion_decision_ref": _s(ur.get("promotion_decision_ref"), "upstream.promotion_decision_ref"),
        "promotion_state": _s(ur.get("promotion_state"), "upstream.promotion_state"),
        "release_manifest_candidate_ref": _s(ur.get("release_manifest_candidate_ref"), "upstream.release_manifest_candidate_ref", True),
        "rollback_ref": _s(ur.get("rollback_ref"), "upstream.rollback_ref", True),
    }
    request["idempotency_key"] = _keys(target, request)[0]
    candidate: dict[str, Any] = {
        "schema_version": "1.0.0", "object_type": OBJECT_TYPE, "profile": PROFILE,
        "execution_mode": EXECUTION_MODE, "intent_id": "", "target": target,
        "request": request, "upstream": upstream, "preflight": _derive(target, request, upstream),
        "spec_hash": "", "claims": {
            "deterministic_preflight": True, "network_accessed": False,
            "external_state_resolved": False, "upstream_authority_verified": False,
            "write_request_emitted": False, "write_performed": False,
            "lifecycle_write_performed": False, "release_created": False,
            "published": False, "public_use_authorized": False,
        },
    }
    projection = {k: v for k, v in candidate.items() if k not in {"intent_id", "spec_hash"}}
    try:
        digest = compute_spec_hash(projection)
    except CanonicalizationFailure as exc:
        raise ValueError("candidate could not be canonicalized") from exc
    candidate["spec_hash"] = digest
    candidate["intent_id"] = "kfm:conditional-write-intent:" + digest.removeprefix("sha256:")
    return candidate
