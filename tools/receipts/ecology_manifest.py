```python
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .ecology_manifest_builder import build_manifest, write_manifest


EXIT_PASS = 0
EXIT_FAILURE = 1
EXIT_MISSING_RECEIPT = 2
EXIT_INTERNAL_ERROR = 5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m tools.receipts.ecology_manifest",
        description="Build a KFM ecology receipt manifest from receipt JSON files.",
    )

    parser.add_argument(
        "--candidate-id",
        required=True,
        help="Candidate identifier for the ecology artifact.",
    )

    parser.add_argument(
        "--candidate-type",
        required=True,
        choices=[
            "eco_index",
            "ecological_claim",
            "map_layer",
            "processed_artifact",
        ],
        help="Candidate artifact type.",
    )

    parser.add_argument(
        "--spec-hash",
        required=True,
        help="Expected candidate spec_hash.",
    )

    parser.add_argument(
        "--receipt",
        action="append",
        default=[],
        help="Receipt JSON path. May be provided multiple times.",
    )

    parser.add_argument(
        "--out",
        required=True,
        help="Output path for the generated receipt manifest.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    receipt_paths = [Path(path) for path in args.receipt]
    out_path = Path(args.out)

    for receipt_path in receipt_paths:
        if not receipt_path.exists():
            print(f"missing receipt: {receipt_path}", file=sys.stderr)
            return EXIT_MISSING_RECEIPT

    try:
        manifest = build_manifest(
            candidate_id=args.candidate_id,
            candidate_type=args.candidate_type,
            spec_hash=args.spec_hash,
            receipt_paths=receipt_paths,
        )
        write_manifest(out_path, manifest)
    except json.JSONDecodeError as exc:
        print(f"invalid receipt json: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except ValueError as exc:
        print(f"invalid receipt: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except Exception as exc:
        print(f"internal manifest builder error: {exc}", file=sys.stderr)
        return EXIT_INTERNAL_ERROR

    print(f"manifest: {out_path}")
    print(f"decision: {manifest['decision']}")
    return EXIT_PASS


if __name__ == "__main__":
    raise SystemExit(main())
```
