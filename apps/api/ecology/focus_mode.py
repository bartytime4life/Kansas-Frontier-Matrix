#!/usr/bin/env python3
"""Minimal governed Ecology Focus Mode runtime.

No-network runtime. It reads released ecology artifacts only.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]

CLAIMS_DIR = REPO_ROOT / "data/triplets/ecology"
PROCESSED_DIR = REPO_ROOT / "data/processed/ecology"
PUBLISHED_DIR = REPO_ROOT / "data/published/ecology"

FINITE_OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _hash_response(payload: dict[str, Any]) -> str:
    stable = {k: v for k, v in payload.items() if k != "spec_hash"}
    material = json.dumps(stable, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(material).hexdigest()


def _find_claims() -> list[dict[str, Any]]:
    if not CLAIMS_DIR.exists():
        return []
    return [_load_json(path) for path in sorted(CLAIMS_DIR.glob("*.json"))]


def _find_decisions() -> list[dict[str, Any]]:
    if not PROCESSED_DIR.exists():
        return []
    return [_load_json(path) for path in sorted(PROCESSED_DIR.glob("decision*.json"))]


def _find_releases() -> list[dict[str, Any]]:
    if not PUBLISHED_DIR.exists():
        return []
    return [_load_json(path) for path in sorted(PUBLISHED_DIR.glob("*.json"))]


def _requested_refs(request: dict[str, Any], key: str) -> list[str]:
    value = request.get(key, [])
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def _make_base(request: dict[str, Any]) -> dict[str, Any]:
    request_id = request.get("request_id", "kfm://request/ecology/unknown")
    surface = request.get("surface", "public")

    return {
        "schema_version": "v1",
        "object_type": "FocusModeResponse",
        "response_id": request_id.replace("kfm://request/", "kfm://response/"),
        "request_id": request_id,
        "surface": surface,
        "outcome": "ERROR",
        "visible_outcome": "ERROR",
        "answer": None,
        "reasons": [],
        "claim_refs": [],
        "evidence_bundle_refs": [],
        "decision_refs": [],
        "redaction_receipt_refs": [],
        "limitations": [],
    }


def _finish(base: dict[str, Any], outcome: str, reasons: list[str], answer: str | None = None) -> dict[str, Any]:
    if outcome not in FINITE_OUTCOMES:
        outcome = "ERROR"
        reasons = [*reasons, "invalid_runtime_outcome"]

    base["outcome"] = outcome
    base["visible_outcome"] = outcome
    base["answer"] = answer
    base["reasons"] = reasons
    base["spec_hash"] = _hash_response(base)
    return base


def _is_sensitive_request(request: dict[str, Any]) -> bool:
    geometry_ref = request.get("geometry_ref")

    return (
        request.get("sensitivity") == "restricted"
        or request.get("public_visibility") == "internal_only"
        or request.get("exact_geometry_present") is True
        or (isinstance(geometry_ref, str) and geometry_ref.startswith("kfm://restricted/"))
    )


def _claim_matches_request(claim: dict[str, Any], request: dict[str, Any]) -> bool:
    requested_claims = set(_requested_refs(request, "claim_refs"))
    requested_evidence = set(_requested_refs(request, "evidence_bundle_refs"))

    if requested_claims and claim.get("claim_id") not in requested_claims:
        return False

    if requested_evidence and claim.get("evidence_bundle_ref") not in requested_evidence:
        return False

    return True


def answer_focus_request(request: dict[str, Any]) -> dict[str, Any]:
    base = _make_base(request)

    surface = request.get("surface", "public")
    requested_evidence = _requested_refs(request, "evidence_bundle_refs")

    if surface != "public":
        return _finish(base, "DENY", ["non_public_surface_not_enabled_in_demo_runtime"])

    if _is_sensitive_request(request):
        return _finish(base, "DENY", ["restricted_or_exact_sensitive_geometry_not_publishable"])

    if request.get("rights_status") == "unknown":
        return _finish(base, "DENY", ["unknown_rights"])

    if request.get("policy_label") == "internal":
        return _finish(base, "DENY", ["internal_policy_label_not_publishable"])

    if request.get("options", {}).get("require_evidence") is True and not requested_evidence:
        return _finish(base, "ABSTAIN", ["missing_required_evidence_bundle_refs"])

    if any(ref.endswith("/missing") or ref == "kfm://evidence/ecology/missing" for ref in requested_evidence):
        base["evidence_bundle_refs"] = requested_evidence
        return _finish(base, "ABSTAIN", ["requested_evidence_bundle_not_resolved"])

    releases = _find_releases()
    claims = _find_claims()
    decisions = _find_decisions()

    published_releases = [
        release
        for release in releases
        if release.get("release_state") == "published"
        and release.get("surface") == "public"
        and release.get("policy_pass") is True
    ]

    if not published_releases:
        return _finish(base, "ABSTAIN", ["no_public_release_manifest"])

    safe_decisions = [
        decision
        for decision in decisions
        if decision.get("decision") in {"allow", "generalize"}
        and decision.get("surface") == "public"
    ]

    if not safe_decisions:
        return _finish(base, "DENY", ["no_public_safe_decision"])

    matching_claims = [claim for claim in claims if _claim_matches_request(claim, request)]

    if not matching_claims:
        base["evidence_bundle_refs"] = requested_evidence
        return _finish(base, "ABSTAIN", ["no_matching_claims_available"])

    claim = matching_claims[0]
    decision = safe_decisions[0]

    if claim.get("claim_status") == "CONFIRMED" and claim.get("knowledge_character") in {"derived", "modeled"}:
        return _finish(base, "DENY", ["derived_claim_marked_confirmed"])

    base["claim_refs"] = [claim.get("claim_id")]
    base["evidence_bundle_refs"] = [claim.get("evidence_bundle_ref")]
    base["decision_refs"] = [claim.get("decision_ref")]

    if decision.get("redaction_receipt_ref"):
        base["redaction_receipt_refs"] = [decision["redaction_receipt_ref"]]

    base["limitations"] = claim.get("limitations", [])

    return _finish(base, "ANSWER", ["released_public_evidence_resolved"], claim.get("statement"))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run Ecology Focus Mode against a request JSON file")
    parser.add_argument("request")
    args = parser.parse_args()

    response = answer_focus_request(_load_json(Path(args.request)))
    print(json.dumps(response, indent=2, sort_keys=True))
