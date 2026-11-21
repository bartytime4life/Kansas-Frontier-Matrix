"""Roads/Rail/Trade Historic Route Claim normalization, with generalization is held until Historic Route Claim normalization and its generalization rules are reviewed.

This entry point reads no source claim and writes no PROCESSED record.
Planned in docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "HISTORIC_ROUTE_CLAIM_BUILD_NOT_IMPLEMENTED",
        "processed_write_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
