"""Agriculture catalog emission is held until CatalogMatrix, STAC, DCAT, and PROV closure semantics are reviewed.

This entry point reads no PROCESSED artifact and writes no CATALOG or TRIPLET record.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "CATALOG_NOT_IMPLEMENTED",
        "catalog_emission_authorized": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
