"""The root CatalogMatrix validator is held until the CatalogMatrix contract fields are reviewed.

This entry point inspects nothing and never reports a pass, so it cannot stand in for validation.
Closure checks live in tools/validators/validate_catalog_matrix_closure.py; domain checks live
under tools/validators/domains/<domain>/validate_catalog_matrix.py.
"""
from __future__ import annotations

import json


def main() -> int:
    print(json.dumps({
        "outcome": "HOLD",
        "reason_code": "CATALOG_MATRIX_VALIDATOR_NOT_IMPLEMENTED",
        "catalog_matrix_validated": False,
    }, sort_keys=True, separators=(",", ":")))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
