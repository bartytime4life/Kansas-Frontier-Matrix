"""Hydrology triplet emission is held until catalog closure and evidence binding are implemented.

This entry point deliberately emits no triplet and writes no CATALOG or TRIPLET artifact.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "TRIPLETS_NOT_IMPLEMENTED",
        "triplet_emission_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
