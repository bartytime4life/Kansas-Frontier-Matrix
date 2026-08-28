#!/usr/bin/env python3
"""CLI for the proposed deterministic KFM STAC Item catalog-health profile.

Network is denied by default. PASS is record-local validation evidence only and
creates no evidence, policy, review, promotion, release, publication, public-use,
or source-activation authority.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.catalog.catalog_health_core import (
    FIXTURE_ROOT,
    HeadResult,
    ValidationResult,
    serialize,
)
from tools.validators.catalog.catalog_health_rules import validate_record

# Stable test/import surface.
_serialize = serialize


def _fixture_paths() -> list[Path]:
    return sorted(
        list((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        + list((FIXTURE_ROOT / "hold").glob("hold_*.json"))
        + list((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
    )


def run_fixture_profile() -> int:
    try:
        outcomes = json.loads(
            (FIXTURE_ROOT / "expected_outcomes.json").read_text(encoding="utf-8")
        )
        expected = json.loads(
            (FIXTURE_ROOT / "expected_findings.json").read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    paths = _fixture_paths()
    if (
        not paths
        or set(outcomes) != {path.name for path in paths}
        or set(expected) != set(outcomes)
    ):
        return 1
    passed = True
    for path in paths:
        result = validate_record(path, asset_root=FIXTURE_ROOT)
        print(_serialize(result))
        actual = sorted({item.code for item in result.findings})
        if result.outcome != outcomes[path.name] or actual != sorted(expected[path.name]):
            passed = False
            print(
                json.dumps(
                    {
                        "file": path.name,
                        "outcome": "FIXTURE_POLARITY_ERROR",
                        "actual": {"outcome": result.outcome, "findings": actual},
                        "expected": {
                            "outcome": outcomes[path.name],
                            "findings": expected[path.name],
                        },
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
    return 0 if passed else 1


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate proposed KFM STAC Item catalog health."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--asset-root", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--network-head", action="store_true")
    parser.add_argument("--allow-host", action="append", default=[])
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.fixtures:
        if args.files or args.network_head or args.allow_host or args.asset_root:
            print("--fixtures cannot be combined with other inputs", file=sys.stderr)
            return 2
        return run_fixture_profile()
    if not args.files:
        print("at least one file or --fixtures is required", file=sys.stderr)
        return 2
    if args.network_head and os.environ.get("KFM_NO_NETWORK") == "1":
        print("network probes denied by KFM_NO_NETWORK=1", file=sys.stderr)
        return 2
    mode = "HEAD" if args.network_head else "DENY"
    exit_codes = {"PASS": 0, "FAIL": 1, "ERROR": 2, "HOLD": 3}
    code = 0
    for path in args.files:
        result = validate_record(
            path,
            asset_root=args.asset_root,
            network_mode=mode,
            allowed_hosts=args.allow_host,
        )
        print(_serialize(result))
        code = max(code, exit_codes[result.outcome])
    return code


if __name__ == "__main__":
    raise SystemExit(main())
