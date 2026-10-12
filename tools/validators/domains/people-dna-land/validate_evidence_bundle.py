from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from tools.validators._common.jsonschema_runner import run


ROOT = Path(__file__).resolve().parents[4]
SCHEMA = ROOT / "schemas/contracts/v1/domains/people-dna-land/evidence_bundle.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/evidence_bundle"


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


def main(argv: list[str] | None = None) -> int:
    """Validate People/DNA/Land EvidenceBundle projections against shared fixtures/files."""
    args = list(sys.argv[1:] if argv is None else argv)
    option_arguments = (
        args[: args.index("--")] if "--" in args else args
    )
    abbreviation = _abbreviated_fixture_option(option_arguments)
    if abbreviation is not None:
        print(
            f"Abbreviated --fixtures option is not allowed: {abbreviation}",
            file=sys.stderr,
        )
        return 2
    if "--fixtures" in option_arguments and len(args) != 1:
        print(
            "Cannot combine --fixtures with explicit EvidenceBundle files",
            file=sys.stderr,
        )
        return 2
    return run(SCHEMA, FIXTURES, args)


if __name__ == "__main__":
    raise SystemExit(main())
