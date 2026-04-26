from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema.exceptions import SchemaError

from .validator import validate_file


EXIT_PASS = 0
EXIT_VALIDATION_FAILURE = 1
EXIT_MISSING_INPUT = 2
EXIT_MISSING_SCHEMA = 3
EXIT_UNRESOLVED_EVIDENCE = 4
EXIT_INTERNAL_ERROR = 5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m tools.validators.ecology_index",
        description="Validate KFM ecology cross-domain join-index rows.",
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the kfm_eco_index JSON object to validate.",
    )

    parser.add_argument(
        "--schema",
        default="schemas/ecology/kfm_eco_index.schema.json",
        help="Path or reference to the kfm_eco_index schema.",
    )

    parser.add_argument(
        "--receipt-out",
        default=None,
        help="Optional path for writing validator receipt JSON.",
    )

    parser.add_argument(
        "--strict",
        action="store_true",
        help="Reserved for future strict validation behavior.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    input_path = Path(args.input)
    schema_path = Path(args.schema)
    receipt_out = Path(args.receipt_out) if args.receipt_out else None

    if not input_path.exists():
        print(f"missing input: {input_path}", file=sys.stderr)
        return EXIT_MISSING_INPUT

    if not schema_path.exists():
        print(f"missing schema: {schema_path}", file=sys.stderr)
        return EXIT_MISSING_SCHEMA

    try:
        result = validate_file(
            input_path=input_path,
            schema_ref=str(schema_path),
            receipt_out=receipt_out,
        )
    except json.JSONDecodeError as exc:
        print(f"invalid json: {exc}", file=sys.stderr)
        return EXIT_VALIDATION_FAILURE
    except ValueError as exc:
        print(f"invalid input: {exc}", file=sys.stderr)
        return EXIT_VALIDATION_FAILURE
    except SchemaError as exc:
        print(f"invalid schema: {exc.message}", file=sys.stderr)
        return EXIT_MISSING_SCHEMA
    except Exception as exc:  # fail closed
        print(f"internal validator error: {exc}", file=sys.stderr)
        return EXIT_INTERNAL_ERROR

    if not result.ok:
        for error in result.errors:
            print(f"{error.code}: {error.message}", file=sys.stderr)
        return EXIT_VALIDATION_FAILURE

    print(f"valid: {input_path}")
    return EXIT_PASS


if __name__ == "__main__":
    raise SystemExit(main())
