#!/usr/bin/env python3
"""Validate People/DNA/Land catalog closure through the shared local profile.

This domain-side adapter delegates unchanged to the repository's existing
CatalogMatrix closure validator. It does not create catalog records, resolve
rights or evidence, activate sources, promote lifecycle state, publish data, or
weaken the shared validator's fail-closed behavior.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
SHARED_VALIDATOR = REPO_ROOT / "tools/validators/validate_catalog_matrix_closure.py"


def run_shared(args: Sequence[str]) -> int:
    if not SHARED_VALIDATOR.is_file():
        print(
            f"PEOPLE_DNA_LAND_CATALOG_VALIDATOR_MISSING path={SHARED_VALIDATOR}",
            file=sys.stderr,
        )
        return 2

    completed = subprocess.run(
        [sys.executable, str(SHARED_VALIDATOR), *args],
        cwd=REPO_ROOT,
        check=False,
    )
    return completed.returncode


def main(argv: Sequence[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if "--fixtures" in arguments and len(arguments) != 1:
        print(
            "Cannot combine --fixtures with explicit CatalogMatrix files",
            file=sys.stderr,
        )
        return 2
    return run_shared(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
