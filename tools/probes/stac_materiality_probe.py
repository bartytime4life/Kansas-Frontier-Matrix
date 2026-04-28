#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _normalize_items(payload: dict[str, Any]) -> list[dict[str, Any]]:
    features = payload.get("features")
    if isinstance(features, list):
        return [item for item in features if isinstance(item, dict)]
    if payload.get("type") == "Feature":
        return [payload]
    return []


def _digest_items(items: list[dict[str, Any]]) -> str:
    canonical = json.dumps(items, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def build_report(*, source_ref: str, baseline: dict[str, Any], candidate: dict[str, Any], max_count_delta: int) -> dict[str, Any]:
    base_items = _normalize_items(baseline)
    cand_items = _normalize_items(candidate)

    base_count = len(base_items)
    cand_count = len(cand_items)
    count_delta = cand_count - base_count
    digest_changed = _digest_items(base_items) != _digest_items(cand_items)

    changed = abs(count_delta) > max_count_delta or digest_changed
    status = "CHANGED" if changed else "UNCHANGED"

    return {
        "probe_id": "kfm.probes.stac_materiality.v1",
        "question": "Did the candidate STAC surface drift materially from baseline?",
        "checked_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "inputs": {
            "source_ref": source_ref,
            "max_count_delta": max_count_delta,
        },
        "status": status,
        "observations": {
            "baseline_count": base_count,
            "candidate_count": cand_count,
            "count_delta": count_delta,
            "digest_changed": digest_changed,
        },
        "refs": {"receipt_ref": None, "proof_ref": None, "evidence_ref": None},
        "warnings": ["material drift observed"] if changed else [],
        "errors": [],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Probe STAC materiality between baseline and candidate payloads.")
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--max-count-delta", type=int, default=0)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(
        source_ref=args.source_ref,
        baseline=_read_json(args.baseline),
        candidate=_read_json(args.candidate),
        max_count_delta=args.max_count_delta,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if report["status"] == "UNCHANGED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
