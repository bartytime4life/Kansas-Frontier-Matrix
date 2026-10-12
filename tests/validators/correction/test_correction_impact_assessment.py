from __future__ import annotations

import socket
import unittest
import urllib.request
from pathlib import Path
from unittest.mock import patch

from tools.validators.correction.validate_correction_impact_assessment import (
    compute_assessment_digest,
    compute_assessment_id,
    validate,
)

ROOT = Path(__file__).resolve().parents[3]
FIXTURES = (
    ROOT
    / "fixtures/contracts/v1/correction/correction_impact_assessment"
)


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("correction impact validation attempted network access")


class CorrectionImpactAssessmentTests(unittest.TestCase):
    def setUp(self):
        self.patchers = [
            patch.object(socket.socket, "connect", side_effect=_unexpected_network),
            patch.object(socket.socket, "connect_ex", side_effect=_unexpected_network),
            patch.object(socket, "create_connection", side_effect=_unexpected_network),
            patch.object(socket, "getaddrinfo", side_effect=_unexpected_network),
            patch.object(urllib.request, "urlopen", side_effect=_unexpected_network),
        ]
        self.mocks = [patcher.start() for patcher in self.patchers]
        for patcher in self.patchers:
            self.addCleanup(patcher.stop)

    def test_valid_profiles_are_deterministic(self):
        expected = {"complete.json": "COMPLETE", "hold.json": "HOLD"}
        for path in sorted((FIXTURES / "valid").glob("*.json")):
            with self.subTest(path=path.name):
                result = validate(path)
                self.assertTrue(result.ok)
                self.assertEqual(result.outcome, expected[path.name])
                assert result.payload is not None
                self.assertEqual(
                    result.payload["assessment_digest"],
                    compute_assessment_digest(result.payload),
                )
                self.assertEqual(
                    result.payload["assessment_id"],
                    compute_assessment_id(result.payload),
                )

    def test_invalid_profiles_fail_closed(self):
        expected = {
            "ai-citation-missing.json": "AI_CITATION_REVALIDATION_REQUIRED",
            "cache-action-invalid.json": "CACHE_ACTION_INVALID",
            "digest-mismatch.json": "ASSESSMENT_DIGEST_MISMATCH",
            "missing-carrier.json": "SCHEMA_INVALID",
        }
        for path in sorted((FIXTURES / "invalid").glob("*.json")):
            with self.subTest(path=path.name):
                result = validate(path)
                self.assertFalse(result.ok)
                self.assertEqual(result.outcome, "ERROR")
                self.assertIn(
                    expected[path.name],
                    {finding.code for finding in result.findings},
                )

    def test_profile_never_calls_network_or_grants_authority(self):
        for path in FIXTURES.rglob("*.json"):
            result = validate(path)
            for mock in self.mocks:
                mock.assert_not_called()
            payload = result.payload
            if payload is None:
                continue
            for field in (
                "authority_created",
                "repository_mutation_allowed",
                "release_authorized",
                "publication_authorized",
                "public_use_allowed",
            ):
                self.assertFalse(payload[field])


if __name__ == "__main__":
    unittest.main(verbosity=2)
