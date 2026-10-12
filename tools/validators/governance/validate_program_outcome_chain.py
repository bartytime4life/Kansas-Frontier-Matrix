#!/usr/bin/env python3
"""Validate the inactive, fixture-only ProgramOutcomeChain profile.

PASS proves bounded stage separation, ordering, deterministic identity, and
authority non-effects only. It performs no network, program, evidence, policy,
review, release, publication, or causation action.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

MODULE_ROOT = Path(__file__).resolve().parent
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from program_outcome_chain_io import (  # noqa: E402
    _load_fixture_document,
    materialize_case,
    run_fixture_suite,
    serialize,
    validate_file,
    validate_payload,
)
from program_outcome_chain_model import (  # noqa: E402
    Finding,
    ValidationResult,
    assign_identity,
)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        ok, report = run_fixture_suite()
        print(
            json.dumps(
                report,
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 0 if ok else 1

    if args.path is None:
        parser.error(
            "path is required unless --fixtures is used"
        )
    result = validate_file(args.path)
    print(serialize(args.path, result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
