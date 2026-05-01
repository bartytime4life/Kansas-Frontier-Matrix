#!/usr/bin/env python3
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

VALIDATOR_VERSION = "promotion-gate-v1"
BLOCKED_SOURCE_STATES = {"RAW", "WORK", "QUARANTINE"}


def _required_field_errors(candidate: dict) -> list[str]:
    required = [
        "schema_version", "object_type", "candidate_id", "source_state", "target_state",
        "evidencebundle_ref", "evidencebundle_spec_hash", "run_receipt_ref",
        "run_receipt_bundle_ref", "rights_status", "sensitivity", "public_release", "reviewer"
    ]
    return [f"missing_required_field:{name}" for name in required if name not in candidate]


def evaluate(candidate: dict) -> dict:
    reasons = _required_field_errors(candidate)
    if candidate.get("object_type") != "PromotionCandidate":
        reasons.append("invalid_object_type")
    if not candidate.get("evidencebundle_spec_hash"):
        reasons.append("missing_evidencebundle_spec_hash")
    if not candidate.get("run_receipt_ref"):
        reasons.append("missing_run_receipt_ref")
    if not candidate.get("run_receipt_bundle_ref"):
        reasons.append("missing_run_receipt_bundle_ref")
    if candidate.get("rights_status") == "unknown":
        reasons.append("rights_unknown_fail_closed")

    public_release = bool(candidate.get("public_release"))
    source_state = candidate.get("source_state")
    if public_release and source_state in BLOCKED_SOURCE_STATES:
        reasons.append("public_release_blocked_from_private_lifecycle_state")

    if candidate.get("target_state") == "PUBLISHED" and not str(candidate.get("reviewer", "")).strip():
        reasons.append("published_target_requires_reviewer")

    if candidate.get("sensitivity") == "restricted" and public_release:
        reasons.append("restricted_sensitivity_cannot_be_public")

    if public_release and candidate.get("cosign_receipt_verified") is not True:
        reasons.append("cosign_receipt_not_verified")

    if public_release and candidate.get("gatehouse_registration_posture") != "registered":
        reasons.append("gatehouse_registration_not_registered")

    decision = "DENY" if reasons else "APPROVE"
    return {
        "object_type": "PromotionDecision",
        "decision": decision,
        "reasons": reasons,
        "candidate_id": candidate.get("candidate_id", "unknown"),
        "timestamp_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "validator_version": VALIDATOR_VERSION,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_promotion_candidate.py <promotion_candidate.json>", file=sys.stderr)
        return 2
    candidate = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    decision = evaluate(candidate)
    print(json.dumps(decision, indent=2))
    return 0 if decision["decision"] == "APPROVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
