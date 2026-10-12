#!/usr/bin/env python3
"""Validate Hydrology source admission through the shared SourceDescriptor profile,
plus one domain-specific semantic check: domain_scope membership.

This domain-side adapter validates candidates against the repository's
existing canonical SourceDescriptor schema
(``schemas/contracts/v1/source/source_descriptor.schema.json``; see
``contracts/source/source_descriptor.md``) -- the same shared,
non-domain-specific contract every domain uses -- and additionally checks
one well-grounded rule: ``domain_scope`` (or its deprecated singular alias
``domain``) is itself a real, schema-declared field. It is optional -- the
contract states it "is not an authority grant by itself" -- so a candidate
that omits it is not rejected here. But a candidate that DOES declare a
scope, and is being checked through this domain's adapter, should include
"hydrology" in that scope; otherwise the descriptor does not claim to apply
to this domain. This adapter does not admit a source, resolve rights or
sensitivity, decide policy, activate connectors, promote lifecycle state,
or publish data.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for _import_root in (REPO_ROOT, HASHING_SRC):
    if str(_import_root) not in sys.path:
        sys.path.insert(0, str(_import_root))

from tools.validators._common.jsonschema_runner import load_validator  # noqa: E402
from hashing import JsonInputError, load_json_file  # noqa: E402


DOMAIN = "hydrology"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/source_descriptor.schema.json"
FIXTURES_DIR = REPO_ROOT / "fixtures/domains/hydrology/source_descriptor"

_VALIDATOR = load_validator(SCHEMA_PATH)


def _domain_scope_finding(candidate: dict[str, Any]) -> str | None:
    """Return a failure message, or None if domain_scope (or its absence) is fine."""

    scope = candidate.get("domain_scope")
    if isinstance(scope, list) and scope:
        if DOMAIN not in scope:
            return f"domain_scope does not include {DOMAIN!r}: {scope!r}"
        return None

    legacy = candidate.get("domain")
    if isinstance(legacy, str) and legacy:
        if legacy != DOMAIN:
            return f"legacy domain {legacy!r} does not match {DOMAIN!r}"
        return None

    return None


def validate_candidate_file(path: Path) -> str | None:
    """Return a failure message, or None if the candidate passes."""

    try:
        candidate = load_json_file(path)
    except JsonInputError as exc:
        return str(exc)

    errors = sorted(
        _VALIDATOR.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    if errors:
        return errors[0].message
    if not isinstance(candidate, dict):
        return "candidate document must be a JSON object"

    return _domain_scope_finding(candidate)


def _validate_paths(paths: list[Path]) -> bool:
    ok = True
    for path in paths:
        message = validate_candidate_file(path)
        if message is None:
            print(f"OK {path}")
        else:
            print(f"FAIL {path}: {message}")
            ok = False
    return ok


def _run_fixtures() -> int:
    valid_dir = FIXTURES_DIR / "valid"
    invalid_dir = FIXTURES_DIR / "invalid"
    valid_files = sorted(valid_dir.glob("*.json"))
    invalid_files = sorted(invalid_dir.glob("*.json"))

    ok = True
    if not valid_files:
        print(f"FAIL {valid_dir}: no JSON fixtures found")
        ok = False
    for path in valid_files:
        message = validate_candidate_file(path)
        if message is None:
            print(f"OK {path}")
        else:
            print(f"FAIL {path}: {message}")
            ok = False

    if not invalid_files:
        print(f"FAIL {invalid_dir}: no JSON fixtures found")
        ok = False
    for path in invalid_files:
        message = validate_candidate_file(path)
        if message is not None:
            print(f"EXPECTED_FAIL {path}: {message}")
        else:
            print(f"FAIL {path}: expected rejection")
            ok = False

    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    """Run shared shape validation, plus domain_scope membership, for explicit files or --fixtures."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    if "--fixtures" in arguments and any(
        argument != "--fixtures" for argument in arguments
    ):
        print("Cannot combine --fixtures with explicit files", file=sys.stderr)
        return 2
    if "--fixtures" in arguments:
        return _run_fixtures()
    if not arguments:
        print("No files provided", file=sys.stderr)
        return 2
    return 0 if _validate_paths([Path(argument) for argument in arguments]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
