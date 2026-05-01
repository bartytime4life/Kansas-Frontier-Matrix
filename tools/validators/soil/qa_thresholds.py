#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

PASS = "pass"
REVIEW = "review"
QUARANTINE = "quarantine"
FAIL = "fail"


def _to_float(value: object, field: str) -> float:
    if not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be numeric")
    return float(value)


def evaluate_receipt(receipt: dict[str, object]) -> dict[str, object]:
    errors: list[str] = []
    notes: list[str] = []

    if "schema_version" not in receipt:
        errors.append("missing schema_version")
    if "validation_summary" not in receipt:
        errors.append("missing validation_summary")
    if "flags" not in receipt:
        errors.append("missing flags")
    if "decision" not in receipt:
        errors.append("missing decision")

    metrics_obj = receipt.get("metrics")
    if not isinstance(metrics_obj, dict):
        errors.append("missing metrics object")
        metrics_obj = {}

    try:
        masked_pct = _to_float(metrics_obj.get("masked_pct"), "metrics.masked_pct")
    except ValueError as exc:
        errors.append(str(exc))
        masked_pct = None

    try:
        zscore_30d_max = _to_float(metrics_obj.get("zscore_30d_max"), "metrics.zscore_30d_max")
    except ValueError as exc:
        errors.append(str(exc))
        zscore_30d_max = None

    try:
        station_grid_residual_max = _to_float(
            metrics_obj.get("station_grid_residual_max"),
            "metrics.station_grid_residual_max",
        )
    except ValueError as exc:
        errors.append(str(exc))
        station_grid_residual_max = None

    flags_obj = receipt.get("flags") if isinstance(receipt.get("flags"), dict) else {}
    residual_sustained = bool(flags_obj.get("residual_sustained", False))

    decision = PASS
    if errors:
        decision = FAIL
    else:
        assert masked_pct is not None and zscore_30d_max is not None and station_grid_residual_max is not None
        if abs(zscore_30d_max) > 2.0:
            decision = QUARANTINE
            notes.append("zscore threshold exceeded")
        if station_grid_residual_max > 0.10 and residual_sustained:
            decision = QUARANTINE
            notes.append("station-grid residual sustained threshold exceeded")
        if masked_pct > 30.0:
            decision = QUARANTINE
            notes.append("masked_pct exceeded fail threshold")
        elif 15.0 <= masked_pct <= 30.0 and decision == PASS:
            decision = REVIEW
            notes.append("masked_pct in review range")

    summary = {
        "validator": "soil.qa_thresholds",
        "status": PASS if decision == PASS else "blocked",
        "decision": decision,
        "errors": errors,
        "notes": notes,
    }
    return summary


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print(json.dumps({"error": "usage: qa_thresholds.py <run_receipt.json>"}))
        return 2

    receipt_path = Path(args[0])
    if not receipt_path.exists():
        print(json.dumps({"error": f"missing file: {receipt_path}"}))
        return 2

    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        if not isinstance(receipt, dict):
            raise ValueError("run receipt must be a JSON object")
        summary = evaluate_receipt(receipt)
    except Exception as exc:  # PROPOSED: keep deterministic fail-closed exception surface.
        print(json.dumps({"validator": "soil.qa_thresholds", "status": "error", "error": str(exc)}))
        return 2

    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["decision"] == PASS else 1


if __name__ == "__main__":
    raise SystemExit(main())
