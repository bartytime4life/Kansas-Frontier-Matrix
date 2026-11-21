"""Roads/Rail/Trade STB Class I weekly snapshot capture is held until source admission for STB Class I weekly snapshots is reviewed.

This entry point fetches nothing and writes no RAW capture.
Planned in docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "STB_CLASS1_INGEST_NOT_IMPLEMENTED",
        "source_admission_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
