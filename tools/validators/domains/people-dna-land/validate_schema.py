from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_ROOT = REPO_ROOT / "schemas/contracts/v1/domains/people-dna-land"


class DuplicateKeyError(ValueError):
    """Raised when a schema object repeats a JSON member name."""


def _unique_object(pairs):
    candidate = {}
    for key, value in pairs:
        if key in candidate:
            raise DuplicateKeyError(f"duplicate JSON object key: {key}")
        candidate[key] = value
    return candidate


def _reject_nonfinite_constant(raw_value):
    raise ValueError(f"non-finite JSON number: {raw_value}")


def _finite_float(raw_value):
    value = float(raw_value)
    if not math.isfinite(value):
        raise ValueError("non-finite JSON number")
    return value


def _load_schema(path: Path):
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_unique_object,
        parse_constant=_reject_nonfinite_constant,
        parse_float=_finite_float,
    )


def _schema_paths(explicit_paths: list[str]) -> list[Path]:
    if explicit_paths:
        return [Path(path) for path in explicit_paths]
    return sorted(SCHEMA_ROOT.rglob("*.schema.json"))


def validate_schema_file(path: Path) -> bool:
    try:
        schema = _load_schema(path)
        if not isinstance(schema, dict):
            raise ValueError("schema document must be a JSON object")
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        print(f"FAIL {path}: {exc}")
        return False

    print(f"OK {path}")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate People/DNA/Land JSON Schema documents against Draft 2020-12."
    )
    parser.add_argument(
        "schemas",
        nargs="*",
        help=(
            "Schema files to validate. With no paths, validate every *.schema.json "
            "under the canonical People/DNA/Land schema root."
        ),
    )
    args = parser.parse_args(argv)

    paths = _schema_paths(args.schemas)
    if not paths:
        print(f"No People/DNA/Land schemas found under {SCHEMA_ROOT}", file=sys.stderr)
        return 2

    ok = True
    for path in paths:
        ok = validate_schema_file(path) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
