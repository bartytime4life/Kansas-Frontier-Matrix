"""The Quarantine Review Worker is held until a governed review-preparation job contract is reviewed.

This entry point consumes no queue, routes no review, and moves nothing between lifecycle zones.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "QUARANTINE_REVIEW_WORKER_NOT_IMPLEMENTED",
        "review_routing_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
