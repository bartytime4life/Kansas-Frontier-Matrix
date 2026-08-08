#!/usr/bin/env python3
"""Tests for conservative evidence-candidate runtime projection."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/evidence-resolver/src"
if str(PACKAGE_SRC) not in sys.path:
    sys.path.insert(0, str(PACKAGE_SRC))

from evidence_resolver.core import ResolutionCandidate, ResolutionIssue  # noqa: E402
from evidence_resolver.runtime_projection import (  # noqa: E402
    REQUIRED_NEXT_CHECKS,
    posture_json,
    project_runtime_posture,
)


def _candidate(status: str, bundle_id: str | None) -> ResolutionCandidate:
    issues = () if status == "RESOLVED" else (ResolutionIssue("fixture/reason"),)
    return ResolutionCandidate(
        profile="kfm/evidence-ref-bundle-candidate/v1alpha1",
        status=status,
        bundle_id=bundle_id,
        checks_performed=("fixture",),
        issues=issues,
    )


class RuntimeProjectionTests(unittest.TestCase):
    def test_resolved_continues_checks_without_becoming_answer(self) -> None:
        posture = project_runtime_posture(_candidate("RESOLVED", "bundle:test"))
        payload = posture.as_dict()

        self.assertEqual(payload["disposition"], "CONTINUE_GOVERNED_CHECKS")
        self.assertEqual(payload["bundle_id"], "bundle:test")
        self.assertEqual(tuple(payload["required_next_checks"]), REQUIRED_NEXT_CHECKS)
        self.assertFalse(payload["authoritative"])
        self.assertFalse(payload["renderable"])
        self.assertNotEqual(payload["disposition"], "ANSWER")

    def test_negative_statuses_project_to_finite_fail_closed_postures(self) -> None:
        expected = {
            "UNRESOLVED": "ABSTAIN",
            "DENIED": "DENY",
            "ERROR": "ERROR",
        }
        for status, disposition in expected.items():
            with self.subTest(status=status):
                payload = project_runtime_posture(_candidate(status, None)).as_dict()
                self.assertEqual(payload["disposition"], disposition)
                self.assertIsNone(payload["bundle_id"])
                self.assertEqual(payload["required_next_checks"], [])
                self.assertFalse(payload["authoritative"])
                self.assertFalse(payload["renderable"])

    def test_inconsistent_candidate_shapes_fail_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "resolved-bundle-missing"):
            project_runtime_posture(_candidate("RESOLVED", None))

        with self.assertRaisesRegex(ValueError, "nonresolved-bundle-present"):
            project_runtime_posture(_candidate("UNRESOLVED", "bundle:leak"))

        with self.assertRaisesRegex(ValueError, "status-unsupported"):
            project_runtime_posture(_candidate("ANSWER", None))

    def test_serialization_is_deterministic_and_non_authoritative(self) -> None:
        posture = project_runtime_posture(_candidate("DENIED", None))
        first = posture_json(posture)
        second = posture_json(posture)

        self.assertEqual(first, second)
        self.assertIn('"authoritative":false', first)
        self.assertIn('"renderable":false', first)
        self.assertNotIn('"ANSWER"', first)


if __name__ == "__main__":
    unittest.main()
