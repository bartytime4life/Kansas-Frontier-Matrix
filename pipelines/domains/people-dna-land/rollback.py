#!/usr/bin/env python3
"""Validate People/DNA/Land rollback-readiness inputs without executing rollback.

Operational rollback remains HOLD under the domain rollback runbook. This
pipeline seam only delegates to the existing synthetic/no-network consent
revocation propagation assessment validator. It does not revoke consent,
delete data, invalidate deployed derivatives, select a release target, change
lifecycle state, publish, or authorize rollback.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
ASSESSMENT_VALIDATOR = (
    REPO_ROOT
    / "tools/validators/domains/people-dna-land/"
    "validate_consent_revocation_propagation_assessment.py"
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--fixtures",
        action="store_true",
        help="Replay deterministic synthetic consent-revocation fixtures.",
    )
    group.add_argument(
        "--input",
        type=Path,
        help="Validate one local governed propagation-assessment JSON document.",
    )
    return parser


def run_assessment(*, fixtures: bool, input_path: Path | None) -> int:
    if not ASSESSMENT_VALIDATOR.is_file():
        print(
            "PEOPLE_DNA_LAND_ROLLBACK_ASSESSMENT_VALIDATOR_MISSING "
            f"path={ASSESSMENT_VALIDATOR}",
            file=sys.stderr,
        )
        return 2

    validator_args = ["--fixtures"] if fixtures else ["--input", str(input_path)]
    completed = subprocess.run(
        [sys.executable, str(ASSESSMENT_VALIDATOR), *validator_args],
        cwd=REPO_ROOT,
        check=False,
    )
    return completed.returncode


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return run_assessment(fixtures=args.fixtures, input_path=args.input)


if __name__ == "__main__":
    raise SystemExit(main())
