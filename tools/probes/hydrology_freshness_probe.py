#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _parse_iso8601(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_report(*, source_ref: str, payload: dict[str, Any], checked_at: datetime, freshness_threshold_seconds: int) -> dict[str, Any]:
    observed_at_raw = payload.get("observed_at") or payload.get("updated")
    observed_at = _parse_iso8601(observed_at_raw) if isinstance(observed_at_raw, str) else None

    errors: list[str] = []
    warnings: list[str] = []

    lag_seconds: int | None = None
    reachable = True
    status = "OBSERVED"

    if observed_at is None:
        status = "ERROR"
        errors.append("missing or invalid observed_at/updated timestamp")
    else:
        lag_seconds = int((checked_at - observed_at.astimezone(timezone.utc)).total_seconds())
        if lag_seconds > freshness_threshold_seconds:
            status = "STALE"
            warnings.append("observed timestamp exceeds freshness threshold")

    return {
        "probe_id": "kfm.probes.hydrology_freshness.v1",
        "question": "Is the declared hydrology source fresh enough for review?",
        "checked_at": checked_at.isoformat().replace("+00:00", "Z"),
        "inputs": {
            "source_ref": source_ref,
            "freshness_threshold_seconds": freshness_threshold_seconds,
        },
        "status": status,
        "observations": {
            "reachable": reachable,
            "observed_at": observed_at_raw,
            "lag_seconds": lag_seconds,
        },
        "refs": {"receipt_ref": None, "proof_ref": None, "evidence_ref": None},
        "warnings": warnings,
        "errors": errors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Probe hydrology source freshness from a JSON payload.")
    parser.add_argument("--input", type=Path, required=True, help="Hydrology payload JSON path.")
    parser.add_argument("--source-ref", required=True, help="Logical source reference identifier.")
    parser.add_argument("--freshness-threshold-seconds", type=int, default=86_400)
    parser.add_argument("--checked-at", default=None, help="Override check time with ISO8601 UTC timestamp.")
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    checked_at = _parse_iso8601(args.checked_at) if args.checked_at else datetime.now(timezone.utc)
    if checked_at is None:
        raise SystemExit("invalid --checked-at timestamp")

    report = build_report(
        source_ref=args.source_ref,
        payload=_read_json(args.input),
        checked_at=checked_at.astimezone(timezone.utc),
        freshness_threshold_seconds=args.freshness_threshold_seconds,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if report["status"] == "ERROR":
        return 2
    if report["status"] == "STALE":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
