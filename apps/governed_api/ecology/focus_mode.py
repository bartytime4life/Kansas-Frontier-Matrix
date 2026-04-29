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


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _hash_response(payload: dict[str, Any]) -> str:
    material = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(material).hexdigest()


def _find_claims() -> list[dict[str, Any]]:
    if not CLAIMS_DIR.exists():
        return []
    return [_load_json(path) for path in sorted(CLAIMS_DIR.glob("*.json"))]


def _find_decisions() -> list[dict[str, Any]]:
    if not PROCESSED_DIR.exists():
        return []
    return [
        _load_json(path)
        for path in sorted(PROCESSED_DIR.glob("decision*.json"))
    ]


def _find_releases() -> list[dict[str, Any]]:
    if not PUBLISHED_DIR.exists():
        return []
    return [_load_json(path) for path in sorted(PUBLISHED_DIR.glob("*.json"))]


def answer_focus_request(request: dict[str, Any]) -> dict[str, Any]:
    request_id = request.get("request_id", "kfm://request/ecology/unknown")
    surface = request.get("surface", "public")

    base: dict[str, Any] = {
        "schema_version": "v1",
        "object_type": "FocusModeResponse",
        "response_id": request_id.replace("kfm://request/", "kfm://response/"),
        "request_id": request_id,
        "surface": surface,
        "answer": None,
        "reasons": [],
        "claim_refs": [],
        "evidence_bundle_refs": [],
        "decision_refs": [],
        "redaction_receipt_refs": [],
        "limitations": []
    }

    if surface != "public":
        base["outcome"] = "DENY"
        base["reasons"] = ["non_public_surface_not_enabled_in_demo_runtime"]
        base["spec_hash"] = _hash_response(base)
        return base

    releases = _find_releases()
    claims = _find_claims()
    decisions = _find_decisions()

    published_releases = [
        release for release in releases
        if release.get("release_state") == "published"
        and release.get("surface") == "public"
        and release.get("policy_pass") is True
    ]

    if not published_releases:
        base["outcome"] = "ABSTAIN"
        base["reasons"] = ["no_public_release_manifest"]
        base["spec_hash"] = _hash_response(base)
        return base

    safe_decisions = [
        decision for decision in decisions
        if decision.get("decision") in {"allow", "generalize"}
        and decision.get("surface") == "public"
    ]

    if not safe_decisions:
        base["outcome"] = "DENY"
        base["reasons"] = ["no_public_safe_decision"]
        base["spec_hash"] = _hash_response(base)
        return base

    if not claims:
        base["outcome"] = "ABSTAIN"
        base["reasons"] = ["no_claims_available"]
        base["spec_hash"] = _hash_response(base)
        return base

    claim = claims[0]
    decision = safe_decisions[0]

    if claim.get("claim_status") == "CONFIRMED" and claim.get("knowledge_character") in {"derived", "modeled"}:
        base["outcome"] = "DENY"
        base["reasons"] = ["derived_claim_marked_confirmed"]
        base["spec_hash"] = _hash_response(base)
        return base

    base["outcome"] = "ANSWER"
    base["answer"] = claim.get("statement")
    base["claim_refs"] = [claim.get("claim_id")]
    base["evidence_bundle_refs"] = [claim.get("evidence_bundle_ref")]
    base["decision_refs"] = [claim.get("decision_ref")]
    if decision.get("redaction_receipt_ref"):
        base["redaction_receipt_refs"] = [decision["redaction_receipt_ref"]]
    base["limitations"] = claim.get("limitations", [])

    base["spec_hash"] = _hash_response(base)
    return base


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run Ecology Focus Mode against a request JSON file")
    parser.add_argument("request")
    args = parser.parse_args()

    response = answer_focus_request(_load_json(Path(args.request)))
    print(json.dumps(response, indent=2, sort_keys=True))
