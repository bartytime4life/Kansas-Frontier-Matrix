#!/usr/bin/env python3
"""Ecology validator for sensitivity and public-safe geometry handling."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def validate(bundle: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    sensitivity = bundle.get("sensitivity")
    if sensitivity not in {"public", "restricted", "sensitive", "public-safe"}:
        errors.append("invalid_sensitivity")

    if sensitivity in {"restricted", "sensitive"} and bundle.get("exact_geometry_present") is True:
        errors.append("restricted_exact_geometry_not_allowed")

    if sensitivity in {"restricted", "sensitive"} and not bundle.get("geoprivacy_receipt_ref"):
        errors.append("missing_geoprivacy_receipt_ref")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ecology sensitivity posture")
    parser.add_argument("bundle", help="Path to bundle JSON file")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    bundle = json.loads(Path(args.bundle).read_text(encoding="utf-8"))
    errors = validate(bundle)
    result = {"decision": "pass" if not errors else "fail", "errors": errors}

    if args.json:
        print(json.dumps(result))
    else:
        print(f"decision={result['decision']}")
        for error in errors:
            print(f"error={error}")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
