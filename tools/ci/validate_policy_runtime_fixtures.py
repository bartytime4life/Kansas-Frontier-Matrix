#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ALLOWED_OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}
REQUIRED_RUNTIME_FILES = [
    Path("policy/bundles/runtime/bundle.yaml"),
    Path("policy/bundles/runtime/finite_outcomes.rego"),
    Path("policy/bundles/runtime/runtime_denials.rego"),
    Path("policy/bundles/runtime/proof_quartet.rego"),
]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate runtime policy fixture coverage and baseline runtime policy scaffold files."
    )
    parser.add_argument("--root", default=".", help="Repository root path")
    args = parser.parse_args()

    root = Path(args.root)
    failures: list[str] = []

    for rel_path in REQUIRED_RUNTIME_FILES:
        if not (root / rel_path).exists():
            failures.append(f"missing runtime policy file: {rel_path}")

    fixtures_dir = root / "policy/fixtures/runtime"
    if not fixtures_dir.exists() or not fixtures_dir.is_dir():
        failures.append("missing runtime fixtures directory: policy/fixtures/runtime")
        _emit_failures(failures)
        return 1

    fixture_paths = sorted(fixtures_dir.glob("*.json"))
    if not fixture_paths:
        failures.append("no runtime fixture JSON files found in policy/fixtures/runtime")
        _emit_failures(failures)
        return 1

    seen_outcomes: set[str] = set()
    seen_scenarios: set[str] = set()

    for fixture_path in fixture_paths:
        try:
            payload = json.loads(fixture_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"invalid JSON: {fixture_path.relative_to(root)} ({exc})")
            continue

        if not isinstance(payload, dict):
            failures.append(
                f"invalid top-level JSON type in {fixture_path.relative_to(root)}; expected object"
            )
            continue

        scenario = payload.get("scenario")
        expected = payload.get("expected")

        if not isinstance(scenario, str) or not scenario:
            failures.append(f"missing required non-empty string key 'scenario' in {fixture_path.relative_to(root)}")
            continue

        if not isinstance(expected, str) or not expected:
            failures.append(
                f"missing required non-empty string key 'expected' in {fixture_path.relative_to(root)}"
            )
            continue

        if expected not in ALLOWED_OUTCOMES:
            failures.append(
                f"invalid expected outcome '{expected}' in {fixture_path.relative_to(root)}; "
                f"must be one of {sorted(ALLOWED_OUTCOMES)}"
            )
            continue

        stem = fixture_path.stem
        if scenario != stem:
            failures.append(
                f"scenario '{scenario}' does not match filename stem '{stem}' in {fixture_path.relative_to(root)}"
            )

        if scenario in seen_scenarios:
            failures.append(f"duplicate scenario '{scenario}' in {fixture_path.relative_to(root)}")

        seen_scenarios.add(scenario)
        seen_outcomes.add(expected)

    missing_outcomes = sorted(ALLOWED_OUTCOMES - seen_outcomes)
    if missing_outcomes:
        failures.append(
            f"runtime fixtures do not cover all finite outcomes; missing: {', '.join(missing_outcomes)}"
        )

    if failures:
        _emit_failures(failures)
        return 1

    print(
        "validate_policy_runtime_fixtures: validated "
        f"{len(fixture_paths)} runtime fixtures with full finite outcome coverage"
    )
    return 0


def _emit_failures(failures: list[str]) -> None:
    print("validate_policy_runtime_fixtures: failed", file=sys.stderr)
    for failure in failures:
        print(f"- {failure}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
