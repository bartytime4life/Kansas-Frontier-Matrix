#!/usr/bin/env python3
"""Ecology validator: validate_taxa.py."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def validate(bundle: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    value = bundle.get("taxa_refs")
    if not isinstance(value, list) or not value:
        errors.append("taxa_refs_required")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate taxa_refs in ecology bundle")
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
