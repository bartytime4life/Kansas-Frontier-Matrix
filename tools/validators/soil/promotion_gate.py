#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED_POLICY_LABELS = {"public", "publication", "public_safe", "public_reviewed"}


def evaluate_gate(receipt: dict[str, object]) -> dict[str, object]:
    reasons: list[str] = []

    validation_summary = receipt.get("validation_summary")
    if not isinstance(validation_summary, dict):
        reasons.append("missing validation_summary")
    elif validation_summary.get("decision") != "pass":
        reasons.append("validation_summary.decision must be pass")

    if not receipt.get("evidence_bundle_ref"):
        reasons.append("missing evidence_bundle_ref")
    if not receipt.get("signatures"):
        reasons.append("missing signatures")

    policy_label = receipt.get("policy_label")
    if policy_label is not None and str(policy_label) not in ALLOWED_POLICY_LABELS:
        reasons.append(f"policy_label not allowed: {policy_label}")

    allowed = len(reasons) == 0
    return {
        "validator": "soil.promotion_gate",
        "promotion_allowed": allowed,
        "gate": "pass" if allowed else "block",
        "message": "promotion allowed" if allowed else "Gate C review required",
        "reasons": reasons,
    }


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print(json.dumps({"error": "usage: promotion_gate.py <run_receipt.json>"}))
        return 2
    path = Path(args[0])
    if not path.exists():
        print(json.dumps({"error": f"missing file: {path}"}))
        return 2

    try:
        receipt = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(receipt, dict):
            raise ValueError("run receipt must be a JSON object")
        result = evaluate_gate(receipt)
    except Exception as exc:  # PROPOSED: deterministic fail-closed parsing behavior.
        print(json.dumps({"validator": "soil.promotion_gate", "promotion_allowed": False, "error": str(exc)}))
        return 2

    print(json.dumps(result, sort_keys=True))
    return 0 if result["promotion_allowed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
