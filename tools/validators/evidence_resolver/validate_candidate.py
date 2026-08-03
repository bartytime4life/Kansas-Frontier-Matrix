#!/usr/bin/env python3
"""Validate the bounded evidence-resolution candidate profile and fixtures."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/evidence-resolver/src"
sys.path.insert(0, str(PACKAGE_SRC))

from evidence_resolver.core import (  # noqa: E402
    BoundedJSONError,
    MAX_INPUT_BYTES,
    PROFILE,
    evaluate_resolution_candidate,
    loads_bounded,
    result_json,
)


EXIT_CODES = {"RESOLVED": 0, "UNRESOLVED": 2, "DENIED": 3, "ERROR": 4}
EXPECTED_VALID_FIXTURES = (
    "valid/resolved.json",
    "valid/resolved_reverified.json",
)
EXPECTED_INVALID_FIXTURES = (
    "invalid/bundle_id_mismatch.json",
    "invalid/bundle_not_found.json",
    "invalid/invalid_timestamp.json",
    "invalid/member_bundle_ref_mismatch.json",
    "invalid/missing_bundle_ref.json",
    "invalid/not_current_head.json",
    "invalid/policy_abstained.json",
    "invalid/policy_denied.json",
    "invalid/policy_error.json",
    "invalid/ref_not_member.json",
    "invalid/superseded.json",
    "invalid/unsupported_profile.json",
    "invalid/verification_corrected.json",
    "invalid/verification_effective_order_invalid.json",
    "invalid/verification_revoked.json",
    "invalid/verification_subject_mismatch.json",
    "invalid/verification_superseded.json",
    "invalid/verification_temporally_inconsistent.json",
    "invalid/verification_unknown.json",
)
EXPECTED_FIXTURES = frozenset(
    (*EXPECTED_VALID_FIXTURES, *EXPECTED_INVALID_FIXTURES)
)


def _load(path: Path) -> object:
    if path.is_symlink() or not path.is_file():
        raise BoundedJSONError("input/unreadable")
    if path.stat().st_size > MAX_INPUT_BYTES:
        raise BoundedJSONError("input/too-large")
    with path.open("rb") as handle:
        payload = handle.read(MAX_INPUT_BYTES + 1)
    return loads_bounded(payload)


def _evaluate_file(path: Path) -> tuple[str, tuple[str, ...], str]:
    payload = _load(path)
    if not isinstance(payload, dict):
        raise ValueError("fixture/not-object")
    if set(payload) != {"request", "expected"}:
        raise ValueError("fixture/invalid-shape")
    expected = payload["expected"]
    if not isinstance(expected, dict) or set(expected) != {"status", "issue_codes"}:
        raise ValueError("fixture/invalid-expected")
    expected_status = expected["status"]
    expected_codes = expected["issue_codes"]
    if expected_status not in EXIT_CODES or not isinstance(expected_codes, list):
        raise ValueError("fixture/invalid-expected")
    if not all(isinstance(code, str) for code in expected_codes):
        raise ValueError("fixture/invalid-expected")
    result = evaluate_resolution_candidate(payload["request"])
    actual_codes = tuple(issue.code for issue in result.issues)
    if result.status != expected_status or actual_codes != tuple(sorted(expected_codes)):
        raise ValueError("fixture/outcome-mismatch")
    return result.status, actual_codes, path.name


def _run_fixtures(root: Path, *, negative_only: bool) -> int:
    files = sorted(root.rglob("*.json"))
    observed = frozenset(path.relative_to(root).as_posix() for path in files)
    if observed != EXPECTED_FIXTURES:
        print("ERROR fixture/inventory-mismatch", file=sys.stderr)
        return 1
    executed = 0
    failures = 0
    statuses: dict[str, int] = {status: 0 for status in EXIT_CODES}
    for path in files:
        try:
            payload = _load(path)
            if not isinstance(payload, dict) or not isinstance(payload.get("expected"), dict):
                raise ValueError("fixture/invalid-shape")
            relative = path.relative_to(root).as_posix()
            expected_status = payload["expected"].get("status")
            if relative in EXPECTED_VALID_FIXTURES and expected_status != "RESOLVED":
                raise ValueError("fixture/polarity-mismatch")
            if relative in EXPECTED_INVALID_FIXTURES and expected_status == "RESOLVED":
                raise ValueError("fixture/polarity-mismatch")
            if negative_only and relative in EXPECTED_VALID_FIXTURES:
                continue
            status, _, name = _evaluate_file(path)
            executed += 1
            statuses[status] += 1
            print(f"PASS {name} {status}")
        except (OSError, BoundedJSONError, ValueError, KeyError):
            failures += 1
            print(f"FAIL {path.name} fixture/evaluation-error", file=sys.stderr)
    if executed == 0:
        print("ERROR fixture/no-selected-cases", file=sys.stderr)
        return 1
    print(
        "SUMMARY "
        + " ".join(f"{status}={statuses[status]}" for status in sorted(statuses))
        + f" FAILED={failures}"
    )
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", type=Path)
    group.add_argument("--fixtures", type=Path)
    parser.add_argument("--negative-only", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures is not None:
        return _run_fixtures(args.fixtures, negative_only=args.negative_only)
    if args.negative_only:
        parser.error("--negative-only requires --fixtures")
    try:
        result = evaluate_resolution_candidate(_load(args.input))
    except OSError:
        issue_code = "input/unreadable"
    except BoundedJSONError as exc:
        issue_code = exc.code
    else:
        print(result_json(result))
        return EXIT_CODES[result.status]
    print(
        json.dumps(
            {
                "profile": PROFILE,
                "status": "ERROR",
                "authoritative": False,
                "bundle_id": None,
                "checks_performed": ["serialized_input_bounds"],
                "issues": [{"code": issue_code}],
                "limitations": [
                    "no_review_release_runtime_or_publication_authority"
                ],
            },
            separators=(",", ":"),
            sort_keys=True,
        )
    )
    return EXIT_CODES["ERROR"]


if __name__ == "__main__":
    raise SystemExit(main())
