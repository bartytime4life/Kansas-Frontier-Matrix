"""Deterministic tests for the sensitive-overlay reveal-expiry profile."""

from __future__ import annotations

import copy
from collections import Counter
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import urllib.request

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators.governance import (  # noqa: E402
    validate_sensitive_overlay_reveal_expiry as validator,
)


class SensitiveOverlayRevealExpiryTests(unittest.TestCase):
    def test_schema_is_valid_closed_and_secret_free(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        for field in ("lease", "assessment", "governance"):
            self.assertFalse(schema["properties"][field]["additionalProperties"])
        self.assertEqual("NONE", schema["x-kfm"]["authority"])
        self.assertEqual("DENIED", schema["x-kfm"]["raw_token_material"])
        self.assertEqual("DENIED", schema["x-kfm"]["key_material"])
        self.assertEqual("UNWIRED", schema["x-kfm"]["cleanup_side_effects"])

    def test_exact_fixture_matrix(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(
                    validator.materialize_case(manifest, case)
                )
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_state"], result.lease_state)
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_covers_hold_abstain_and_deny(self) -> None:
        manifest = validator.load_fixtures()
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"HOLD", "ABSTAIN", "DENY"}, set(outcomes))
        self.assertEqual(2, outcomes["HOLD"])
        self.assertEqual(2, outcomes["ABSTAIN"])
        self.assertEqual(16, outcomes["DENY"])
        self.assertNotIn("ALLOW", outcomes)

    def test_unknown_verification_summaries_abstain_and_restore_blur(self) -> None:
        manifest = validator.load_fixtures()
        by_id = {case["case_id"]: case for case in manifest["cases"]}
        for case_id in (
            "unknown-attestation-abstain",
            "unknown-revocation-status-abstain",
        ):
            document = validator.materialize_case(manifest, by_id[case_id])
            result = validator.validate_payload(document)
            with self.subTest(case=case_id):
                self.assertEqual("ABSTAIN", result.outcome)
                self.assertEqual("ABSTAINED", result.lease_state)
                self.assertEqual(validator.CLEANUP_ACTIONS, result.required_actions)
                self.assertEqual("BLURRED", document["assessment"]["target_view_state"])

    def test_expired_revoked_and_denied_states_require_cleanup_plan(self) -> None:
        manifest = validator.load_fixtures()
        by_id = {case["case_id"]: case for case in manifest["cases"]}
        for case_id in (
            "expired-reveal-deny",
            "revoked-reveal-deny",
            "stale-revocation-check-deny",
            "stale-policy-hash-deny",
            "failed-attestation-deny",
            "consumed-single-use-token-deny",
        ):
            document = validator.materialize_case(manifest, by_id[case_id])
            result = validator.validate_payload(document)
            with self.subTest(case=case_id):
                self.assertEqual("DENY", result.outcome)
                self.assertEqual(validator.CLEANUP_ACTIONS, result.required_actions)
                self.assertEqual("BLURRED", document["assessment"]["target_view_state"])

    def test_active_and_expiring_states_only_declare_countdown_actions(self) -> None:
        manifest = validator.load_fixtures()
        active = validator.materialize_case(manifest, manifest["cases"][0])
        expiring = validator.materialize_case(manifest, manifest["cases"][1])
        self.assertEqual(list(validator.ACTIVE_ACTIONS), active["assessment"]["required_actions"])
        self.assertEqual(3600, active["assessment"]["seconds_remaining"])
        self.assertEqual(
            list(validator.EXPIRING_ACTIONS),
            expiring["assessment"]["required_actions"],
        )
        self.assertEqual(240, expiring["assessment"]["seconds_remaining"])
        for document in (active, expiring):
            self.assertEqual("NONE", document["assessment"]["authority"])
            self.assertEqual("REVEALED", document["assessment"]["target_view_state"])
            self.assertNotIn(
                "DISCARD_CLIENT_KEY", document["assessment"]["required_actions"]
            )

    def test_expiry_is_inclusive_and_warning_window_is_five_minutes(self) -> None:
        manifest = validator.load_fixtures()
        document = copy.deepcopy(manifest["base"])
        document["evaluated_at"] = "2026-08-10T12:55:00Z"
        document["lease"]["revocation_checked_at"] = "2026-08-10T12:55:00Z"
        assessment = validator.derive_assessment(document)
        self.assertEqual("EXPIRING", assessment["lease_state"])
        self.assertEqual(300, assessment["seconds_remaining"])
        document["evaluated_at"] = document["lease"]["expires_at"]
        document["lease"]["revocation_checked_at"] = document["evaluated_at"]
        assessment = validator.derive_assessment(document)
        self.assertEqual("EXPIRED", assessment["lease_state"])
        self.assertEqual(0, assessment["seconds_remaining"])

    def test_exact_24_hour_ttl_is_accepted_but_one_second_more_denies(self) -> None:
        manifest = validator.load_fixtures()
        document = copy.deepcopy(manifest["base"])
        document["lease"]["expires_at"] = "2026-08-11T11:00:00Z"
        assessment = validator.derive_assessment(document)
        self.assertEqual("ACTIVE", assessment["lease_state"])
        self.assertEqual("HOLD", assessment["outcome"])
        document["lease"]["expires_at"] = "2026-08-11T11:00:01Z"
        assessment = validator.derive_assessment(document)
        self.assertEqual("DENIED", assessment["lease_state"])
        self.assertIn("LEASE_TTL_EXCEEDED", assessment["reason_codes"])

    def test_fixture_contains_hashes_but_no_secret_or_genomic_payload(self) -> None:
        text = validator.FIXTURES.read_text(encoding="utf-8")
        for marker in (
            "Bearer ",
            "eyJhbGci",
            '"access_token"',
            '"raw_token"',
            '"decryption_key"',
            '"private_key"',
            "BEGIN PRIVATE KEY",
            "raw_genotype",
            "raw_sequence",
            "vcf_payload",
        ):
            self.assertNotIn(marker, text)
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            document = validator.materialize_case(manifest, case)
            self.assertTrue(document["lease"]["reveal_token_hash"].startswith("sha256:"))
            self.assertTrue(document["lease"]["challenge_hash"].startswith("sha256:"))

    def test_undeclared_raw_token_field_fails_schema_closed(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        document["lease"]["raw_token"] = "DO_NOT_ECHO_SECRET_SENTINEL"
        result = validator.validate_payload(document)
        self.assertEqual("DENY", result.outcome)
        self.assertIn(validator.Finding("SCHEMA_INVALID", "/lease"), result.findings)

    def test_validation_is_no_network(self) -> None:
        manifest = validator.load_fixtures()
        denied = AssertionError("reveal-expiry validation attempted network access")
        with (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
            mock.patch.object(socket.socket, "connect_ex", side_effect=denied),
            mock.patch.object(socket, "create_connection", side_effect=denied),
            mock.patch.object(socket, "getaddrinfo", side_effect=denied),
            mock.patch.object(urllib.request, "urlopen", side_effect=denied),
        ):
            for case in manifest["cases"]:
                validator.validate_payload(validator.materialize_case(manifest, case))

    def test_identity_and_spec_hash_are_deterministic(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        expected_hash = document["spec_hash"]
        expected_id = document["assessment_id"]
        reordered = dict(reversed(list(copy.deepcopy(document).items())))
        self.assertEqual(expected_hash, validator.expected_spec_hash(reordered))
        self.assertEqual(expected_id, validator.expected_assessment_id(expected_hash))
        reordered["lease"]["consumed"] = True
        self.assertNotEqual(expected_hash, validator.expected_spec_hash(reordered))

    def test_fixture_cli_and_bounded_input_cli(self) -> None:
        fixture_run = subprocess.run(
            [sys.executable, str(Path(validator.__file__)), "--fixtures"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, fixture_run.returncode, fixture_run.stderr)
        suite = json.loads(fixture_run.stdout)
        self.assertTrue(suite["suite_match"])
        self.assertEqual(20, suite["case_count"])
        self.assertEqual("NONE", suite["authority"])

        manifest = validator.load_fixtures()
        hold = validator.materialize_case(manifest, manifest["cases"][0])
        deny = validator.materialize_case(manifest, manifest["cases"][2])
        with tempfile.TemporaryDirectory() as raw:
            hold_path = Path(raw) / "hold.json"
            deny_path = Path(raw) / "deny.json"
            hold_path.write_text(json.dumps(hold), encoding="utf-8")
            deny_path.write_text(json.dumps(deny), encoding="utf-8")
            hold_run = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(hold_path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            deny_run = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(deny_path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(0, hold_run.returncode, hold_run.stderr)
        self.assertEqual("HOLD", json.loads(hold_run.stdout)["outcome"])
        self.assertEqual(1, deny_run.returncode, deny_run.stderr)
        denied_payload = json.loads(deny_run.stdout)
        self.assertEqual("DENY", denied_payload["outcome"])
        self.assertEqual("EXPIRED", denied_payload["lease_state"])

    def test_duplicate_json_fails_without_echoing_candidate_value(self) -> None:
        sentinel = "RAW_REVEAL_TOKEN_SENTINEL_THAT_MUST_NOT_ECHO"
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "duplicate.json"
            path.write_text(
                '{"profile":"first","profile":"' + sentinel + '"}',
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(2, completed.returncode)
        self.assertNotIn(sentinel, completed.stdout)
        payload = json.loads(completed.stdout)
        self.assertEqual("ERROR", payload["outcome"])
        self.assertEqual("FIXTURE_JSON_INVALID", payload["findings"][0]["code"])

    def test_validator_has_no_network_crypto_or_ui_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in (
            "requests",
            "urllib.request",
            "httpx",
            "aiohttp",
            "jwt.decode",
            "cryptography",
            "localStorage",
            "indexedDB",
            "maplibre",
        ):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
