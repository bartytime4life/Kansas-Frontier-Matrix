"""Hydrology promotion gate stub.

Creates minimal governed artifacts for a promotion decision run.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def emit_stub(run_id: str) -> None:
    root = Path(__file__).resolve().parents[3]
    decided_at = datetime.now(timezone.utc).isoformat()
    decision = {
        "id": f"promo:hydrology:{run_id}",
        "version": "v1",
        "domain": "hydrology",
        "run_id": run_id,
        "decision": "APPROVE",
        "evidence_ref": f"evidence:hydrology:bundle:{run_id}",
        "evidence_bundle_uri": f"data/proofs/hydrology/{run_id}.promotion_proof.json",
        "rollback_card_uri": f"release/rollback_cards/hydrology/{run_id}.md",
        "policy_bundle": "policy/promotion/hydrology@v1",
        "decided_at": decided_at,
        "review": {"reviewer": "automation-smoke", "ticket": "REL-SMOKE"},
    }
    out = root / "release" / "promotion_decisions" / "hydrology" / f"{run_id}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(decision, indent=2), encoding="utf-8")


if __name__ == "__main__":
    emit_stub("run-local-smoke")
