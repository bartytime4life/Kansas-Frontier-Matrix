"""Hydrology publication is held until release, review, and rollback gates are implemented.

This entry point deliberately publishes no layer and writes no release or PUBLISHED artifact.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "PUBLISH_NOT_IMPLEMENTED",
        "publication_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
