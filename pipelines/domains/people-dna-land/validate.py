#!/usr/bin/env python3
"""Dispatch People/DNA/Land validation through existing fail-closed validators.

This pipeline-side entrypoint provides one stable executable seam for downstream
People/DNA/Land jobs. It delegates to already-governed validators and does not
admit sources, infer identity or kinship, decide consent or sovereignty, publish
data, or weaken the delegated validators' fail-closed behavior.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATORS = {
    "schema": REPO_ROOT / "tools/validators/domains/people-dna-land/validate_schema.py",
    "evidence-bundle": REPO_ROOT
    / "tools/validators/domains/people-dna-land/validate_evidence_bundle.py",
    "source-descriptor": REPO_ROOT
    / "tools/validators/domains/people-dna-land/validate_source_descriptor.py",
    "catalog-matrix": REPO_ROOT
    / "tools/validators/domains/people-dna-land/validate_catalog_matrix.py",
    "living-person": REPO_ROOT / "tools/validators/genealogy/screen_living_persons.py",
    "consent-overlay": REPO_ROOT
    / "tools/validators/domains/people-dna-land/validate_consent_overlay.py",
    "consent-revocation": REPO_ROOT
    / "tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "validator",
        choices=sorted(VALIDATORS),
        help="Existing People/DNA/Land validation seam to execute.",
    )
    parser.add_argument(
        "validator_args",
        nargs=argparse.REMAINDER,
        help="Arguments passed unchanged to the selected validator.",
    )
    return parser


def run_validator(name: str, validator_args: Sequence[str]) -> int:
    validator = VALIDATORS[name]
    if not validator.is_file():
        print(
            f"PEOPLE_DNA_LAND_VALIDATOR_MISSING validator={name} path={validator}",
            file=sys.stderr,
        )
        return 2

    args = list(validator_args)
    if args[:1] == ["--"]:
        args = args[1:]

    completed = subprocess.run(
        [sys.executable, str(validator), *args],
        cwd=REPO_ROOT,
        check=False,
    )
    return completed.returncode


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return run_validator(args.validator, args.validator_args)


if __name__ == "__main__":
    raise SystemExit(main())
