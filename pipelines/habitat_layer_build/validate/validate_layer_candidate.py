"""Validation helpers for habitat layer candidate fixtures."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = ("layer_id", "source_id", "source_role", "support_resolution_m", "crs")


def validate_candidate(candidate: dict) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in candidate:
            errors.append(f"missing field: {field}")
    if candidate.get("source_role") == "modeled_as_critical":
        errors.append("source_role modeled_as_critical is denied in build lane")
    return errors


def validate_file(path: Path) -> list[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return validate_candidate(payload)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixtures", type=Path, required=True)
    args = parser.parse_args()

    invalid = 0
    for fixture in sorted(args.fixtures.rglob("*.json")):
        errors = validate_file(fixture)
        if errors:
            invalid += 1
            print(f"INVALID {fixture}: {'; '.join(errors)}")
        else:
            print(f"VALID {fixture}")
    return 1 if invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
