```python
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema.exceptions import SchemaError

from .ecology_proof_pack_builder import (
    build_proof_pack,
    load_json,
    validate_proof_pack,
    write_proof_pack,
)


EXIT_PASS = 0
EXIT_FAILURE = 1
EXIT_MISSING_INPUT = 2
EXIT_MISSING_SCHEMA = 3
EXIT_INTERNAL_ERROR = 5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m tools.proofs.ecology_proof_pack",
        description="Build a KFM ecology proof pack from a receipt manifest and catalog refs.",
    )

    parser.add_argument(
        "--manifest",
        required=True,
        help="Path to ecology receipt manifest JSON.",
    )

    parser.add_argument(
        "--catalog-refs",
        required=True,
        help="Path to catalog refs JSON containing dcat/stac/prov arrays.",
    )

    parser.add_argument(
        "--schema",
        default="schemas/ecology/ecology_proof_pack.schema.json",
        help="Path to the ecology proof-pack schema.",
    )

    parser.add_argument(
        "--out",
        required=True,
        help="Output path for proof-pack JSON.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    manifest_path = Path(args.manifest)
    catalog_refs_path = Path(args.catalog_refs)
    schema_path = Path(args.schema)
    out_path = Path(args.out)

    if not manifest_path.exists():
        print(f"missing manifest: {manifest_path}", file=sys.stderr)
        return EXIT_MISSING_INPUT

    if not catalog_refs_path.exists():
        print(f"missing catalog refs: {catalog_refs_path}", file=sys.stderr)
        return EXIT_MISSING_INPUT

    if not schema_path.exists():
        print(f"missing schema: {schema_path}", file=sys.stderr)
        return EXIT_MISSING_SCHEMA

    try:
        manifest = load_json(manifest_path)
        catalog_refs = load_json(catalog_refs_path)

        proof_pack = build_proof_pack(
            manifest=manifest,
            manifest_ref=str(manifest_path),
            catalog_refs=catalog_refs,
        )

        errors = validate_proof_pack(
            proof_pack=proof_pack,
            schema_path=schema_path,
        )
        if errors:
            for error in errors:
                print(f"proof-pack schema invalid: {error}", file=sys.stderr)
            return EXIT_FAILURE

        write_proof_pack(out_path, proof_pack)
    except json.JSONDecodeError as exc:
        print(f"invalid json: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except ValueError as exc:
        print(f"invalid proof-pack input: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except SchemaError as exc:
        print(f"invalid proof-pack schema: {exc.message}", file=sys.stderr)
        return EXIT_MISSING_SCHEMA
    except Exception as exc:
        print(f"internal proof-pack builder error: {exc}", file=sys.stderr)
        return EXIT_INTERNAL_ERROR

    print(f"proof pack: {out_path}")
    print("status: proof_complete")
    return EXIT_PASS


if __name__ == "__main__":
    raise SystemExit(main())
```
