#!/usr/bin/env python3
"""Validate People/DNA/Land SourceDescriptor candidates via shared source authority.

This domain entrypoint delegates to the repository's shared SourceDescriptor
validator and therefore inherits the existing schema and deterministic fixture
polarity. Validation checks shape only. It does not admit or activate a source,
retrieve source payloads, decide rights, consent, sensitivity, or authority,
promote lifecycle state, release, publish, or wire Explorer/runtime behavior.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.sources.validate_source_descriptor import main as _shared_main  # noqa: E402


_FIXTURE_OPTION = "--fixtures"


def _abbreviated_fixture_option(arguments: list[str]) -> str | None:
    """Return an abbreviated fixture flag before the option terminator."""
    for argument in arguments:
        if argument == "--":
            break
        if (
            2 < len(argument) < len(_FIXTURE_OPTION)
            and _FIXTURE_OPTION.startswith(argument)
        ):
            return argument
    return None


def main(argv: Sequence[str] | None = None) -> int:
    """Run the shared SourceDescriptor validator through the People/DNA/Land seam."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    option_arguments = (
        arguments[: arguments.index("--")] if "--" in arguments else arguments
    )
    abbreviation = _abbreviated_fixture_option(option_arguments)
    if abbreviation is not None:
        print(
            f"Abbreviated --fixtures option is not allowed: {abbreviation}",
            file=sys.stderr,
        )
        return 2
    if "--fixtures" in option_arguments and len(arguments) != 1:
        print(
            "Cannot combine --fixtures with explicit SourceDescriptor files",
            file=sys.stderr,
        )
        return 2
    return _shared_main(arguments)


if __name__ == "__main__":
    raise SystemExit(main())
