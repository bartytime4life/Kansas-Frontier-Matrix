#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REQUIRED_KEYS = ("receipt_ref", "proof_ref", "release_ref")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_report(*, source_ref: str, payload: dict[str, Any]) -> dict[str, Any]:
    refs = payload.get("refs") if isinstance(payload.get("refs"), dict) else {}
    missing = [key for key in REQUIRED_KEYS if not isinstance(refs.get(key), str) or not refs.get(key).strip()]

    status = "OBSERVED" if not missing else "CHANGED"

    return {
        "probe_id": "kfm.probes.catalog_release_refs.v1",
        "question": "Are required release trust references present in the catalog payload?",
        "checked_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "inputs": {"source_ref": source_ref, "required_refs": list(REQUIRED_KEYS)},
        "status": status,
        "observations": {
            "present_refs": {key: refs.get(key) for key in REQUIRED_KEYS if key in refs},
            "missing_refs": missing,
        },
        "refs": {
            "receipt_ref": refs.get("receipt_ref"),
            "proof_ref": refs.get("proof_ref"),
            "evidence_ref": None,
        },
        "warnings": ["missing required release refs"] if missing else [],
        "errors": [],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Probe catalog payload for release reference presence.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(source_ref=args.source_ref, payload=_read_json(args.input))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if report["status"] == "OBSERVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
