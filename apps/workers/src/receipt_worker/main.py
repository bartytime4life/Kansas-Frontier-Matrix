"""The Receipt Worker is held until a governed receipt-support job contract is reviewed.

This entry point consumes no queue and validates, writes, indexes, or attests no receipt.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "RECEIPT_WORKER_NOT_IMPLEMENTED",
        "receipt_emission_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
