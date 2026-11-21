"""Roads/Rail/Trade RAW to PROCESSED normalization for Road Segment is held until the Road Segment contract, an admitted RAW source and its fixtures are reviewed.

This entry point reads no RAW capture and writes no PROCESSED record.
Planned in docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "ROAD_SEGMENT_NORMALIZATION_NOT_IMPLEMENTED",
        "processed_write_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
