"""The Tile Worker is held until a governed tile-candidate job contract is reviewed.

This entry point consumes no queue, builds no tile, and writes no cache, candidate, or receipt.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "TILE_WORKER_NOT_IMPLEMENTED",
        "tile_build_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
