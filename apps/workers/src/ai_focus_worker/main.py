"""The Governed AI Focus Worker is held until a governed focus-job contract is reviewed.

This entry point consumes no queue, calls no model, and writes no answer, candidate, or receipt.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "AI_FOCUS_WORKER_NOT_IMPLEMENTED",
        "ai_focus_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
