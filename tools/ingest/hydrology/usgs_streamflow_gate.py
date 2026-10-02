"""The USGS streamflow ingest gate is held until a governed source-admission path is reviewed.

This entry point contacts no provider and writes no RAW, WORK, or QUARANTINE artifact.
The bounded USGS water pilot uses its own connector in connectors/usgs/water_data/.
Planned in docs/domains/hydrology/EXPANSION_BACKLOG.md.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "USGS_STREAMFLOW_GATE_NOT_IMPLEMENTED",
        "source_admission_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
