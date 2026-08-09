"""Command-line inspection for the local schema registry snapshot."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from schema_registry.core import SchemaRegistryError, build_registry_snapshot


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build a deterministic, no-network KFM schema registry snapshot."
    )
    parser.add_argument("schema_root", type=Path)
    parser.add_argument("--pretty", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        snapshot = build_registry_snapshot(args.schema_root)
    except SchemaRegistryError as exc:
        payload = {
            "outcome": "ERROR",
            "error": exc.as_dict(),
            "authority": "helper_only",
        }
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")), file=sys.stderr)
        return 2

    payload = {
        "outcome": "RESOLVED",
        "snapshot": snapshot.as_dict(),
    }
    if args.pretty:
        print(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        print(
            json.dumps(
                payload,
                sort_keys=True,
                ensure_ascii=False,
                separators=(",", ":"),
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
