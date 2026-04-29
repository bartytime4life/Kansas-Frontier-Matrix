"""Soil & air quality watcher scaffolding runner."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--receipt", default="data/work/soil_air/scaffold_receipt.json")
    args = parser.parse_args()

    receipt = {
        "watcher_id": "soil_air_quality",
        "status": "noop",
        "dry_run": args.dry_run,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    out = Path(args.receipt)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
