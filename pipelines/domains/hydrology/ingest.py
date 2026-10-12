"""Hydrology ingestion is held until a governed source-admission path is reviewed.

This entry point deliberately reads no source and writes no RAW, WORK, or QUARANTINE artifact.
The bounded USGS water pilot uses its own connector in connectors/usgs/water_data/ and does not route through here.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "INGEST_NOT_IMPLEMENTED",
        "ingestion_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
