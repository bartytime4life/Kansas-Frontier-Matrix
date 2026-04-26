from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .ecology_manifest import (
    decision_to_dict,
    evaluate_ecology_receipt_manifest,
)


EXIT_PASS = 0
EXIT_FAILURE = 1
EXIT_MISSING_MANIFEST = 2
EXIT_INTERNAL_ERROR = 5


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m tools.validators.promotion_gate.ecology_manifest_cli",
        description="Evaluate a KFM ecology receipt manifest for promotion-gate use.",
    )

    parser.add_argument(
        "--manifest",
        required=True,
        help="Path to ecology receipt manifest JSON.",
    )

    parser.add_argument(
        "--out",
        default=None,
        help="Optional output path for promotion gate result JSON.",
    )

    return parser


def write_result(path: Path, result: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    manifest_path = Path(args.manifest)
    out_path = Path(args.out) if args.out else None

    if not manifest_path.exists():
        print(f"missing manifest: {manifest_path}", file=sys.stderr)
        return EXIT_MISSING_MANIFEST

    try:
        decision = evaluate_ecology_receipt_manifest(manifest_path)
        result = decision_to_dict(decision)

        if out_path is not None:
            write_result(out_path, result)
    except json.JSONDecodeError as exc:
        print(f"invalid manifest json: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except ValueError as exc:
        print(f"invalid manifest: {exc}", file=sys.stderr)
        return EXIT_FAILURE
    except Exception as exc:
        print(f"internal promotion manifest error: {exc}", file=sys.stderr)
        return EXIT_INTERNAL_ERROR

    print(f"decision: {result['decision']}")
    return EXIT_PASS if decision.ok else EXIT_FAILURE


if __name__ == "__main__":
    raise SystemExit(main())
