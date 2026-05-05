from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema.exceptions import SchemaError

from .ecology_map_layer_registry import (
    LayerRegistryError,
    active_layer_bindings,
    load_layer_binding,
)


EXIT_PASS = 0
EXIT_FAILURE = 1
EXIT_MISSING_INPUT = 2
EXIT_MISSING_SCHEMA = 3
EXIT_INTERNAL_ERROR = 5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m tools.registry.ecology_map_layer_registry_cli",
        description="Validate and resolve KFM ecology map-layer bindings.",
    )

    parser.add_argument(
        "--registry",
        required=True,
        help="Path to ecology map-layer registry JSON.",
    )

    parser.add_argument(
        "--schema",
        default="schemas/ecology/ecology_map_layer_binding.schema.json",
        help="Path to ecology map-layer binding schema.",
    )

    parser.add_argument(
        "--layer-id",
        default=None,
        help="Optional layer_id to resolve. If omitted, active layers are listed.",
    )

    parser.add_argument(
        "--out",
        default=None,
        help="Optional output path for resolved binding JSON.",
    )

    return parser


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    registry_path = Path(args.registry)
    schema_path = Path(args.schema)
    out_path = Path(args.out) if args.out else None

    if not registry_path.exists():
        print(f"missing registry: {registry_path}", file=sys.stderr)
        return EXIT_MISSING_INPUT

    if not schema_path.exists():
        print(f"missing schema: {schema_path}", file=sys.stderr)
        return EXIT_MISSING_SCHEMA

    try:
        if args.layer_id:
            result: object = load_layer_binding(
                registry_path=registry_path,
                layer_id=args.layer_id,
                schema_path=schema_path,
            )
        else:
            result = active_layer_bindings(
                registry_path=registry_path,
                schema_path=schema_path,
            )

        if out_path is not None:
            write_json(out_path, result)

    except json.JSONDecodeError as exc:
        print(f"invalid json: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except LayerRegistryError as exc:
        print(f"invalid registry: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except SchemaError as exc:
        print(f"invalid binding schema: {exc.message}", file=sys.stderr)
        return EXIT_MISSING_SCHEMA
    except Exception as exc:
        print(f"internal registry error: {exc}", file=sys.stderr)
        return EXIT_INTERNAL_ERROR

    if args.layer_id:
        print(f"binding: {args.layer_id}")
    else:
        print(f"active bindings: {len(result)}")

    return EXIT_PASS


if __name__ == "__main__":
    raise SystemExit(main())
