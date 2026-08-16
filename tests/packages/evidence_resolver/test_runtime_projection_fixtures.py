#!/usr/bin/env python3
"""Cross-check resolver fixture outcomes against conservative runtime projection."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/evidence-resolver/src"
if str(PACKAGE_SRC) not in sys.path:
    sys.path.insert(0, str(PACKAGE_SRC))

from evidence_resolver.core import evaluate_resolution_candidate  # noqa: E402
from evidence_resolver.runtime_projection import (  # noqa: E402
    REQUIRED_NEXT_CHECKS,
    posture_json,
    project_runtime_posture,
)


FIXTURE_ROOT = REPO_ROOT / "fixtures/packages/evidence_resolver/v1alpha1"
EXPECTED_DISPOSITIONS = {
    "RESOLVED": "CONTINUE_GOVERNED_CHECKS",
    "UNRESOLVED": "ABSTAIN",
    "DENIED": "DENY",
    "ERROR": "ERROR",
}


class RuntimeProjectionFixtureIntegrationTests(unittest.TestCase):
    def test_every_resolver_fixture_projects_fail_closed(self) -> None:
        paths = sorted(FIXTURE_ROOT.rglob("*.json"))
        self.assertTrue(paths, "expected resolver fixtures")

        observed_statuses: set[str] = set()
        for path in paths:
            with self.subTest(path=path.relative_to(FIXTURE_ROOT).as_posix()):
                case = json.loads(path.read_text(encoding="utf-8"))
                result = evaluate_resolution_candidate(case["request"])
                posture = project_runtime_posture(result)
                payload = posture.as_dict()

                observed_statuses.add(result.status)
                self.assertEqual(payload["candidate_status"], result.status)
                self.assertEqual(
                    payload["disposition"], EXPECTED_DISPOSITIONS[result.status]
                )
                self.assertFalse(payload["authoritative"])
                self.assertFalse(payload["renderable"])
                self.assertNotEqual(payload["disposition"], "ANSWER")

                if result.status == "RESOLVED":
                    self.assertEqual(payload["bundle_id"], result.bundle_id)
                    self.assertIsNotNone(payload["bundle_id"])
                    self.assertEqual(
                        tuple(payload["required_next_checks"]), REQUIRED_NEXT_CHECKS
                    )
                else:
                    self.assertIsNone(payload["bundle_id"])
                    self.assertEqual(payload["required_next_checks"], [])

                encoded = posture_json(posture)
                self.assertEqual(encoded, posture_json(posture))
                self.assertIn('"authoritative":false', encoded)
                self.assertIn('"renderable":false', encoded)

        self.assertEqual(set(EXPECTED_DISPOSITIONS), observed_statuses)

    def test_resolved_fixtures_preserve_all_remaining_governed_checks(self) -> None:
        resolved_paths = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
        self.assertTrue(resolved_paths, "expected resolved fixtures")

        for path in resolved_paths:
            with self.subTest(path=path.name):
                case = json.loads(path.read_text(encoding="utf-8"))
                result = evaluate_resolution_candidate(case["request"])
                self.assertEqual(result.status, "RESOLVED")
                posture = project_runtime_posture(result).as_dict()
                self.assertEqual(
                    tuple(posture["required_next_checks"]), REQUIRED_NEXT_CHECKS
                )
                self.assertEqual(
                    set(posture["required_next_checks"]),
                    {
                        "evidence_authority",
                        "rights",
                        "sensitivity",
                        "policy",
                        "review",
                        "release",
                        "citation",
                        "correction",
                    },
                )
                self.assertEqual(posture["disposition"], "CONTINUE_GOVERNED_CHECKS")
                self.assertFalse(posture["renderable"])


if __name__ == "__main__":
    unittest.main()
