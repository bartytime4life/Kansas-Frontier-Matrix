"""Deterministic no-network tests for water-planning document receipt validation.

These tests verify that:
- Valid receipts with properly formed SHA-256 digests pass.
- Null document digests (unpinned) are rejected.
- All-zero placeholder digests are rejected.
- Malformed digest strings are rejected.
- Blocked behaviors (connector, proof, release, publication, source_activation)
  are rejected.
- Validation is fully no-network.
"""

from __future__ import annotations

import io
import json
import socket
import unittest
import urllib.request
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.domains.water_planning.validate_document_receipts import (
    main,
    validate_candidate,
    validate_file,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = (
    REPO_ROOT / "fixtures" / "domains" / "water_planning" / "document_receipts"
)
VALID_FIXTURE = FIXTURE_ROOT / "valid" / "valid_1.json"

INVALID_FIXTURES = {
    FIXTURE_ROOT / "invalid" / "null_digest.json": {
        (
            "DOCUMENT_DIGEST_UNPINNED",
            "$.document_receipts[0].document_digest",
        ),
    },
    FIXTURE_ROOT / "invalid" / "zero_placeholder_digest.json": {
        (
            "DOCUMENT_DIGEST_IS_PLACEHOLDER",
            "$.document_receipts[0].document_digest",
        ),
    },
    FIXTURE_ROOT / "invalid" / "bad_format_digest.json": {
        (
            "DOCUMENT_DIGEST_FORMAT_INVALID",
            "$.document_receipts[0].document_digest",
        ),
    },
    FIXTURE_ROOT / "invalid" / "blocked_behaviors.json": {
        ("CONNECTOR_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.connector"),
        ("PROOF_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.proof"),
        ("RELEASE_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.release"),
        ("PUBLICATION_BEHAVIOR_FORBIDDEN", "$.blocked_behaviors.publication"),
        (
            "SOURCE_ACTIVATION_BEHAVIOR_FORBIDDEN",
            "$.blocked_behaviors.source_activation",
        ),
    },
}


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError(
        "Document receipt validation attempted network access"
    )


class WaterPlanningDocumentReceiptTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_valid_fixture_passes(self):
        self.assertEqual(validate_file(VALID_FIXTURE), ())

    def test_valid_fixture_has_two_pinned_receipts(self):
        """Valid fixture must have exactly 2 document receipts with non-null digests."""
        candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        receipts = candidate["document_receipts"]
        self.assertEqual(len(receipts), 2)
        for receipt in receipts:
            digest = receipt["document_digest"]
            self.assertIsNotNone(digest)
            self.assertTrue(
                digest.startswith("sha256:"),
                f"digest must be sha256: prefixed; got {digest!r}",
            )
            self.assertNotEqual(
                digest,
                "sha256:" + "0" * 64,
                "digest must not be all-zero placeholder",
            )

    def test_invalid_fixtures_produce_stable_expected_findings(self):
        for fixture_path, expected_findings in INVALID_FIXTURES.items():
            with self.subTest(fixture=fixture_path.name):
                findings = validate_file(fixture_path)
                actual_findings = {
                    (finding.code, finding.path) for finding in findings
                }
                self.assertEqual(actual_findings, expected_findings)

    def test_null_digest_is_rejected_for_titled_document(self):
        """A document with a title and null digest must be rejected."""
        candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        candidate["document_receipts"][0]["document_digest"] = None
        findings = validate_candidate(candidate)
        codes = {f.code for f in findings}
        self.assertIn("DOCUMENT_DIGEST_UNPINNED", codes)

    def test_zero_placeholder_is_rejected(self):
        """All-zero digest (sha256:000...0) is rejected as an unpinned placeholder."""
        candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        candidate["document_receipts"][0]["document_digest"] = (
            "sha256:" + "0" * 64
        )
        findings = validate_candidate(candidate)
        codes = {f.code for f in findings}
        self.assertIn("DOCUMENT_DIGEST_IS_PLACEHOLDER", codes)

    def test_malformed_digest_is_rejected(self):
        """Digest strings that do not match sha256:[a-f0-9]{64} are rejected."""
        for bad_digest in (
            "not-a-sha256",
            "sha256:tooshort",
            "sha256:" + "g" * 64,  # invalid hex chars
            "",
        ):
            with self.subTest(digest=bad_digest):
                candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
                candidate["document_receipts"][0]["document_digest"] = bad_digest
                findings = validate_candidate(candidate)
                codes = {f.code for f in findings}
                self.assertIn("DOCUMENT_DIGEST_FORMAT_INVALID", codes)

    def test_program_version_fixture_has_pinned_digest(self):
        """The canonical FY2027 program_version fixture must have a non-null, non-zero digest."""
        program_version_fixture = (
            REPO_ROOT
            / "fixtures"
            / "domains"
            / "water_planning"
            / "program_version"
            / "valid"
            / "valid_1.json"
        )
        fixture = json.loads(program_version_fixture.read_text(encoding="utf-8"))
        digest = fixture.get("document_digest")
        self.assertIsNotNone(
            digest, "program_version document_digest must not be null"
        )
        self.assertRegex(
            digest,
            r"^sha256:[0-9a-f]{64}$",
            "program_version document_digest must be a valid sha256 hex digest",
        )
        self.assertNotEqual(
            digest,
            "sha256:" + "0" * 64,
            "program_version document_digest must not be the all-zero placeholder",
        )

    def test_scoring_matrix_fixture_has_pinned_digest(self):
        """The canonical FY2027 scoring_matrix_version fixture must have a non-null, non-zero digest."""
        scoring_fixture = (
            REPO_ROOT
            / "fixtures"
            / "domains"
            / "water_planning"
            / "scoring_matrix_version"
            / "valid"
            / "valid_1.json"
        )
        fixture = json.loads(scoring_fixture.read_text(encoding="utf-8"))
        digest = fixture.get("digest")
        self.assertIsNotNone(
            digest, "scoring_matrix_version digest must not be null"
        )
        self.assertRegex(
            digest,
            r"^sha256:[0-9a-f]{64}$",
            "scoring_matrix_version digest must be a valid sha256 hex digest",
        )
        self.assertNotEqual(
            digest,
            "sha256:" + "0" * 64,
            "scoring_matrix_version digest must not be the all-zero placeholder",
        )

    def test_cli_exit_contract_is_deterministic(self):
        valid_output = io.StringIO()
        with redirect_stdout(valid_output):
            valid_code = main([str(VALID_FIXTURE)])
        self.assertEqual(valid_code, 0)
        self.assertEqual(
            valid_output.getvalue(),
            '{"files": 1, "outcome": "VALIDATOR_PASS"}\n',
        )

        first = io.StringIO()
        second = io.StringIO()
        with redirect_stdout(first):
            first_code = main(
                [str(FIXTURE_ROOT / "invalid" / "null_digest.json")]
            )
        with redirect_stdout(second):
            second_code = main(
                [str(FIXTURE_ROOT / "invalid" / "null_digest.json")]
            )
        self.assertEqual(first_code, 1)
        self.assertEqual(second_code, 1)
        self.assertEqual(first.getvalue(), second.getvalue())
        parsed = json.loads(first.getvalue())
        self.assertEqual(parsed["outcome"], "VALIDATOR_FAIL")
        self.assertGreater(len(parsed["findings"]), 0)

    def test_missing_input_returns_finite_finding(self):
        findings = validate_file(FIXTURE_ROOT / "nonexistent-fixture.json")
        self.assertEqual(
            tuple((f.code, f.path) for f in findings),
            (("INPUT_NOT_FOUND", "$"),),
        )


if __name__ == "__main__":
    unittest.main()
