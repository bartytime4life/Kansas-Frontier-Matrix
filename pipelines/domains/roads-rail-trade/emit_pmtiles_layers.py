"""Roads/Rail/Trade PMTiles per layer for the published surface is held until layer generalization, release and the published surface are reviewed.

This entry point reads no PROCESSED or CATALOG artifact and writes no tiles.
Planned in docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "PMTILES_EMISSION_NOT_IMPLEMENTED",
        "tile_build_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
