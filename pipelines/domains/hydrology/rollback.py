"""Hydrology rollback is held until a governed release and rollback-card path is implemented.

This entry point deliberately changes no release state and writes no correction or rollback artifact.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "ROLLBACK_NOT_IMPLEMENTED",
        "rollback_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
