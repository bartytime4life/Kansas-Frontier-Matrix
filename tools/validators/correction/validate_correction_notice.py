"""Validate PROPOSED CorrectionNotice instances without network or mutation.

This validator intentionally enforces only the current paired Draft 2020-12
schema and bounded JSON-input safety. A PASS does not prove correction
completion, evidence closure, policy or review approval, release authority,
rollback execution, or publication state.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/correction/correction_notice.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/correction/correction_notice"
MAX_JSON_BYTES = 2 * 1024 * 1024


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> object:
    raise ValueError("non-finite number")


def _parse_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise ValueError("non-finite number")
    return parsed


def load_document(path: Path) -> tuple[dict[str, object] | None, tuple[str, ...]]:
    """Read one bounded, duplicate-free JSON object."""
    try:
        if path.is_symlink() or not path.is_file():
            return None, ("INPUT_NOT_FILE",)
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, ("INPUT_TOO_LARGE",)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_float,
        )
    except DuplicateKeyError:
        return None, ("JSON_DUPLICATE_KEY",)
    except (json.JSONDecodeError, UnicodeError, ValueError, RecursionError):
        return None, ("JSON_INVALID",)
    except OSError:
        return None, ("INPUT_UNREADABLE",)
    if not isinstance(value, dict):
        return None, ("JSON_ROOT_INVALID",)
    return value, ()


def _validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def validate_document(document: Mapping[str, object]) -> tuple[str, ...]:
    """Return stable, non-value-bearing findings for the paired schema only."""
    return ("SCHEMA_INVALID",) if list(_validator().iter_errors(document)) else ()


def validate_path(path: Path) -> tuple[str, ...]:
    document, findings = load_document(path)
    if document is None:
        return findings
    return validate_document(document)


def run_fixtures(root: Path = FIXTURES_ROOT) -> int:
    valid = sorted((root / "valid").glob("*.json"))
    invalid = sorted((root / "invalid").glob("*.json"))
    if not valid or not invalid:
        print("CORRECTION_NOTICE_FIXTURES_ERROR nonempty valid and invalid lanes required")
        return 2
    failures: list[str] = []
    for path in valid:
        if validate_path(path):
            failures.append(f"valid/{path.name}")
    for path in invalid:
        if "SCHEMA_INVALID" not in validate_path(path):
            failures.append(f"invalid/{path.name}")
    if failures:
        for failure in failures:
            print(f"CORRECTION_NOTICE_FIXTURE_POLARITY_FAIL {failure}")
        return 1
    print(
        "CORRECTION_NOTICE_FIXTURES_VALID "
        f"valid={len(valid)} invalid={len(invalid)} no_network=true non_publisher=true"
    )
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate CorrectionNotice instances against the current proposed schema."
    )
    parser.add_argument("notices", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.notices:
            parser.error("--fixtures cannot be combined with notice paths")
        return run_fixtures()
    if not args.notices:
        parser.error("at least one notice path is required unless --fixtures is used")
    failed = False
    for path in sorted(args.notices):
        findings = validate_path(path)
        if findings:
            failed = True
            for code in findings:
                print(f"CORRECTION_NOTICE_INVALID file={path.name} code={code}")
        else:
            print(f"CORRECTION_NOTICE_VALID file={path.name}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
