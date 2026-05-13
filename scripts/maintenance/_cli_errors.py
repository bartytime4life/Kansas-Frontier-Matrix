from __future__ import annotations

import json


def emit_structured_error(check: str, error: Exception | str) -> int:
    print(json.dumps({"check": check, "result": "error", "error": str(error)}))
    return 2
