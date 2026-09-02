#!/usr/bin/env python3
"""Validate the canonical reusable-fixture root contract without network access."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.fixture_root_contract import SCOPE, ValidationResult, validate_repository


def _serialize(result: ValidationResult) -> str:
    return json.dumps(
        {
            "aggregate_validators": result.aggregate_validators,
            "authority": {
                "creates_fixture_authority": False,
                "evaluates_policy": False,
                "promotes": False,
                "publishes": False,
                "releases": False,
                "validates_all_fixture_payloads": False,
            },
            "direct_child_directories": result.direct_child_directories,
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate the fixtures/ root README contract."
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO_ROOT,
        help="Repository root; defaults to the current checkout.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    result = validate_repository(args.repo_root)
    print(_serialize(result))
    if result.ok:
        return 0
    return 2 if result.outcome == "ERROR_VALIDATOR" else 1


if __name__ == "__main__":
    raise SystemExit(main())
