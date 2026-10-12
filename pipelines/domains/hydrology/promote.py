"""Hydrology promotion is held until a governed decision path is implemented.

The historical automation-smoke record is not evidence of review or approval.
This entry point deliberately creates no release or lifecycle artifact.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "PROMOTION_NOT_IMPLEMENTED",
        "promotion_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
