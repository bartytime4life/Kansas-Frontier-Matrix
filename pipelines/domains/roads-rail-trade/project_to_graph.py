"""Roads/Rail/Trade derived, non-canonical graph projection is held until the derived graph projection is reviewed; the graph is never canonical.

This entry point reads no PROCESSED record and writes no graph.
Planned in docs/domains/roads-rail-trade/MISSING_OR_PLANNED_FILES.md.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "GRAPH_PROJECTION_NOT_IMPLEMENTED",
        "graph_projection_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
