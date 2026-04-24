```python
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PASS_DECISIONS = {
    "ready_for_promotion",
    "proof_complete",
}

HOLD_DECISIONS = {
    "hold",
    "proof_required",
}

FAIL_DECISIONS = {
    "not_ready",
    "quarantine",
}


@dataclass(frozen=True)
class PromotionManifestDecision:
    gate: str
    decision: str
    manifest_ref: str
    candidate_id: str | None
    spec_hash: str | None
    errors: list[str]
    warnings: list[str]

    @property
    def ok(self) -> bool:
        return self.decision == "pass"


def load_manifest(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))

    if not isinstance(value, dict):
        raise ValueError("Receipt manifest must be a JSON object.")

    return value


def evaluate_ecology_receipt_manifest(path: Path) -> PromotionManifestDecision:
    manifest = load_manifest(path)

    manifest_decision = str(manifest.get("decision", ""))
    candidate_id = manifest.get("candidate_id")
    spec_hash = manifest.get("spec_hash")

    errors: list[str] = []
    warnings: list[str] = []

    if manifest_decision in PASS_DECISIONS:
        decision = "pass"
    elif manifest_decision in HOLD_DECISIONS:
        decision = "hold"
        warnings.append(f"manifest decision requires review: {manifest_decision}")
    elif manifest_decision in FAIL_DECISIONS:
        decision = "fail"
        errors.append(f"manifest decision blocks promotion: {manifest_decision}")
    else:
        decision = "fail"
        errors.append(f"unknown manifest decision: {manifest_decision}")

    if not candidate_id:
        decision = "fail"
        errors.append("manifest missing candidate_id")

    if not spec_hash:
        decision = "fail"
        errors.append("manifest missing spec_hash")

    return PromotionManifestDecision(
        gate="ecology_receipt_manifest",
        decision=decision,
        manifest_ref=str(path),
        candidate_id=str(candidate_id) if candidate_id else None,
        spec_hash=str(spec_hash) if spec_hash else None,
        errors=errors,
        warnings=warnings,
    )


def decision_to_dict(decision: PromotionManifestDecision) -> dict[str, Any]:
    return {
        "gate": decision.gate,
        "decision": decision.decision,
        "manifest_ref": decision.manifest_ref,
        "candidate_id": decision.candidate_id,
        "spec_hash": decision.spec_hash,
        "errors": decision.errors,
        "warnings": decision.warnings,
    }
```
