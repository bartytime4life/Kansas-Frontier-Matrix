#!/usr/bin/env python3
"""
Generate a KFM Ecology PromotionDecision artifact from a policy decision.

Mapping:
  allow -> PROMOTE
  hold  -> REVIEW
  deny  -> DENY
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


POLICY_TO_PROMOTION = {
    "allow": "PROMOTE",
    "hold": "REVIEW",
    "deny": "DENY",
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR: file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {path}: {exc}")


def stable_suffix(*parts: str) -> str:
    material = "|".join(parts).encode("utf-8")
    return hashlib.sha256(material).hexdigest()[:24]


def normalize_reasons(value: Any) -> list[str]:
    if value is None:
        return []

    if isinstance(value, list):
        return sorted(str(item) for item in value)

    if isinstance(value, set):
        return sorted(str(item) for item in value)

    return [str(value)]


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def generate_promotion_decision(
    *,
    policy_decision: str,
    candidate: str,
    receipt_ref: str,
    reasons: list[str],
    evidence_bundle_url: str | None = None,
    decided_at: str | None = None,
) -> dict[str, Any]:
    if policy_decision not in POLICY_TO_PROMOTION:
        raise ValueError(
            f"unsupported policy decision: {policy_decision}; "
            f"expected one of {sorted(POLICY_TO_PROMOTION)}"
        )

    promotion_decision = POLICY_TO_PROMOTION[policy_decision]
    decided_at = decided_at or utc_now()

    decision_id = (
        "kfm://promotion/ecology/"
        + stable_suffix(candidate, receipt_ref, policy_decision)
    )

    artifact: dict[str, Any] = {
        "schema_version": "v1",
        "object_type": "PromotionDecision",
        "decision_id": decision_id,
        "candidate": candidate,
        "decision": promotion_decision,
        "reasons": reasons,
        "requires_steward": promotion_decision == "REVIEW",
        "receipt_ref": receipt_ref,
        "decided_at": decided_at,
    }

    if evidence_bundle_url:
        artifact["evidence_bundle_url"] = evidence_bundle_url

    return artifact


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a KFM Ecology PromotionDecision artifact."
    )
    parser.add_argument("--policy-decision", required=True, choices=sorted(POLICY_TO_PROMOTION))
    parser.add_argument("--candidate", required=True)
    parser.add_argument("--receipt-ref", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--reasons-json", type=Path)
    parser.add_argument("--evidence-bundle-url")
    parser.add_argument("--decided-at")
    args = parser.parse_args()

    reasons: list[str] = []
    if args.reasons_json:
        payload = load_json(args.reasons_json)
        reasons = normalize_reasons(
            payload.get(
                "reasons",
                payload.get(
                    "deny_reasons",
                    payload.get("hold_reasons", payload.get("generalize_reasons", [])),
                ),
            )
        )

    try:
        artifact = generate_promotion_decision(
            policy_decision=args.policy_decision,
            candidate=args.candidate,
            receipt_ref=args.receipt_ref,
            reasons=reasons,
            evidence_bundle_url=args.evidence_bundle_url,
            decided_at=args.decided_at,
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(artifact, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
