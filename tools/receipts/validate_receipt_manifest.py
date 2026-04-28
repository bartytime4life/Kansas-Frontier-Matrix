from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema.exceptions import SchemaError

from .ecology_manifest_builder import validate_manifest


EXIT_PASS = 0
EXIT_FAILURE = 1
EXIT_MISSING_MANIFEST = 2
EXIT_MISSING_SCHEMA = 3
EXIT_INTERNAL_ERROR = 5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m tools.receipts.validate_receipt_manifest",
        description="Validate an existing KFM ecology receipt manifest against schema.",
    )

    parser.add_argument(
        "--manifest",
        required=True,
        help="Path to an ecology receipt manifest JSON file.",
    )

    parser.add_argument(
        "--schema",
        default="schemas/ecology/ecology_receipt_manifest.schema.json",
        help="Path to ecology receipt manifest schema.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    manifest_path = Path(args.manifest)
    schema_path = Path(args.schema)

    if not manifest_path.exists():
        print(f"missing manifest: {manifest_path}", file=sys.stderr)
        return EXIT_MISSING_MANIFEST

    if not schema_path.exists():
        print(f"missing schema: {schema_path}", file=sys.stderr)
        return EXIT_MISSING_SCHEMA

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        errors = validate_manifest(
            manifest=manifest,
            schema_path=schema_path,
        )
    except json.JSONDecodeError as exc:
        print(f"invalid manifest json: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except SchemaError as exc:
        print(f"invalid manifest schema: {exc}", file=sys.stderr)
        return EXIT_MISSING_SCHEMA
    except Exception as exc:
        print(f"internal manifest validation error: {exc}", file=sys.stderr)
        return EXIT_INTERNAL_ERROR

    if errors:
        for error in errors:
            print(f"manifest schema invalid: {error}", file=sys.stderr)
        return EXIT_FAILURE

    print("manifest schema valid")
    return EXIT_PASS


if __name__ == "__main__":
    raise SystemExit(main())
