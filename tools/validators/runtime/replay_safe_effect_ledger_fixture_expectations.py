"""Match fixture expectations against the exact validation stage, outcome, and findings.

This helper is intentionally side-effect free.  It does not run validation, read files,
or grant evidence, review, release, or publication authority.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

VALIDATION_STAGES = frozenset({"PARSE", "SCHEMA", "SEMANTIC"})


@dataclass(frozen=True)
class FixtureExpectationMismatch:
    """One deterministic mismatch between a manifest case and an observation."""

    code: str
    expected: object
    actual: object

    def as_dict(self) -> dict[str, object]:
        return {
            "code": self.code,
            "expected": self.expected,
            "actual": self.actual,
        }


def evaluate_fixture_expectation(
    case: Mapping[str, Any],
    *,
    validation_stage: str,
    outcome: str,
    findings: Sequence[Mapping[str, str]],
) -> tuple[FixtureExpectationMismatch, ...]:
    """Return exact, ordered mismatches for one fixture-manifest case."""

    mismatches: list[FixtureExpectationMismatch] = []
    expected_stage = case.get("expected_validation_stage")
    if expected_stage not in VALIDATION_STAGES:
        mismatches.append(
            FixtureExpectationMismatch(
                "MANIFEST_VALIDATION_STAGE_INVALID",
                sorted(VALIDATION_STAGES),
                expected_stage,
            )
        )
    elif validation_stage != expected_stage:
        mismatches.append(
            FixtureExpectationMismatch(
                "VALIDATION_STAGE_MISMATCH",
                expected_stage,
                validation_stage,
            )
        )

    expected_outcome = case.get("expected_outcome")
    if outcome != expected_outcome:
        mismatches.append(
            FixtureExpectationMismatch(
                "OUTCOME_MISMATCH",
                expected_outcome,
                outcome,
            )
        )

    expected_findings = case.get("expected_findings")
    actual_findings = [dict(item) for item in findings]
    if actual_findings != expected_findings:
        mismatches.append(
            FixtureExpectationMismatch(
                "FINDINGS_MISMATCH",
                expected_findings,
                actual_findings,
            )
        )

    return tuple(mismatches)
