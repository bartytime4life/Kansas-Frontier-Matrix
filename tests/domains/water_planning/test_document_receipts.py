"""Deterministic no-network tests for water-planning receipt fixtures.

Positive digest examples are synthetic and recomputable from embedded fixture
bytes. Official KWO fixture records remain unresolved until exact source bytes
are captured and independently hashed.
"""

from __future__ import annotations

import hashlib
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
        ("DOCUMENT_DIGEST_UNPINNED", "$.document_receipts[0].document_digest"),
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
    FIXTURE_ROOT / "invalid" / "official_source_digest.json": {
        (
            "OFFICIAL_SOURCE_DIGEST_FORBIDDEN_IN_FIXTURE",
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
    raise AssertionError("Document receipt validation attempted network access")


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

    def test_valid_fixture_digests_match_embedded_payloads(self):
        candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        receipts = candidate["document_receipts"]
        self.assertEqual(len(receipts), 2)
        for receipt in receipts:
            self.assertTrue(receipt["source_ref"].startswith("fixture:"))
            payload = receipt["fixture_payload_utf8"].encode("utf-8")
            expected = "sha256:" + hashlib.sha256(payload).hexdigest()
            self.assertEqual(receipt["document_digest"], expected)

    def test_invalid_fixtures_produce_stable_expected_findings(self):
        for fixture_path, expected_findings in INVALID_FIXTURES.items():
            with self.subTest(fixture=fixture_path.name):
                findings = validate_file(fixture_path)
                actual_findings = {(finding.code, finding.path) for finding in findings}
                self.assertEqual(actual_findings, expected_findings)

    def test_null_digest_is_rejected_for_titled_fixture_document(self):
        candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        candidate["document_receipts"][0]["document_digest"] = None
        findings = validate_candidate(candidate)
        self.assertIn("DOCUMENT_DIGEST_UNPINNED", {f.code for f in findings})

    def test_zero_placeholder_is_rejected(self):
        candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        candidate["document_receipts"][0]["document_digest"] = "sha256:" + "0" * 64
        findings = validate_candidate(candidate)
        self.assertIn("DOCUMENT_DIGEST_IS_PLACEHOLDER", {f.code for f in findings})

    def test_malformed_digest_is_rejected(self):
        for bad_digest in (
            "not-a-sha256",
            "sha256:tooshort",
            "sha256:" + "g" * 64,
            "",
        ):
            with self.subTest(digest=bad_digest):
                candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
                candidate["document_receipts"][0]["document_digest"] = bad_digest
                findings = validate_candidate(candidate)
                self.assertIn(
                    "DOCUMENT_DIGEST_FORMAT_INVALID", {f.code for f in findings}
                )

    def test_fixture_payload_mismatch_is_rejected(self):
        candidate = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
        candidate["document_receipts"][0]["fixture_payload_utf8"] += "changed"
        findings = validate_candidate(candidate)
        self.assertIn("FIXTURE_DIGEST_MISMATCH", {f.code for f in findings})

    def test_program_version_fixture_preserves_unobserved_digest(self):
        fixture_path = (
            REPO_ROOT
            / "fixtures"
            / "domains"
            / "water_planning"
            / "program_version"
            / "valid"
            / "valid_1.json"
        )
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
        self.assertIsNone(fixture["document_digest"])

    def test_scoring_matrix_fixture_preserves_unobserved_digest(self):
        fixture_path = (
            REPO_ROOT
            / "fixtures"
            / "domains"
            / "water_planning"
            / "scoring_matrix_version"
            / "valid"
            / "valid_1.json"
        )
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
        self.assertIsNone(fixture["digest"])

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
        invalid_path = FIXTURE_ROOT / "invalid" / "null_digest.json"
        with redirect_stdout(first):
            first_code = main([str(invalid_path)])
        with redirect_stdout(second):
            second_code = main([str(invalid_path)])
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
