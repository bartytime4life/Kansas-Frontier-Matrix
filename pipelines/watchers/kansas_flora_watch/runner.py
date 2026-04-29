"""Kansas flora watcher scaffolding.

Roadmap-only lane: this runner provides a deterministic no-op dry-run surface
until full ingestion wiring lands.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def build_receipt(dry_run: bool) -> dict:
    return {
        "watcher_id": "kansas_flora_watch",
        "status": "noop",
        "dry_run": dry_run,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "message": "Scaffold runner executed; implementation pending.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="run one cycle")
    parser.add_argument("--dry-run", action="store_true", help="no writes outside local receipt")
    parser.add_argument("--receipt", default="data/work/flora/scaffold_receipt.json")
    args = parser.parse_args()

    receipt = build_receipt(dry_run=args.dry_run)
    out = Path(args.receipt)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
