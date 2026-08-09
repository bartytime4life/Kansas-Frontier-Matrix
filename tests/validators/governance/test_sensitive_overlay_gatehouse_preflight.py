"""Deterministic tests for the sensitive-overlay gatehouse preflight."""

from __future__ import annotations

import copy
import json
import socket
import subprocess
import sys
import tempfile
import unittest
import urllib.request
from collections import Counter
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.governance import (
    validate_sensitive_overlay_gatehouse_preflight as validator,
)

ROOT = Path(__file__).resolve().parents[3]


class SensitiveOverlayGatehousePreflightTests(unittest.TestCase):
    def test_schema_is_valid_closed_and_token_free(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["properties"]["consent"]["additionalProperties"])
        self.assertFalse(schema["properties"]["identity"]["additionalProperties"])
        self.assertFalse(schema["properties"]["egress"]["additionalProperties"])
        self.assertEqual("DENIED", schema["x-kfm"]["raw_token_material"])

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
                self.assertEqual(case["expected_findings"], actual)

    def test_fixture_polarity_is_one_hold_and_fail_closed_denials(self) -> None:
        manifest = validator.load_fixtures()
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"HOLD", "DENY"}, set(outcomes))
        self.assertEqual(1, outcomes["HOLD"])
        self.assertGreaterEqual(outcomes["DENY"], 35)

    def test_clean_summary_is_hold_with_no_authority(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        result = validator.validate_payload(document)
        payload = json.loads(validator.render_result(result))
        self.assertEqual("HOLD", payload["outcome"])
        self.assertEqual("NONE", payload["authority"])
        self.assertEqual(list(validator.HOLDS), payload["holds"])
        self.assertIn("SIGNED_RECEIPT_EMISSION_UNWIRED", payload["holds"])
        self.assertIn("no_raw_token_or_genomic_material", payload["non_effects"])
        self.assertIn(
            "no_release_deployment_publication_or_public_use",
            payload["non_effects"],
        )

    def test_profile_requires_24_hour_consent_cap_and_requested_ttl_coverage(self) -> None:
        manifest = validator.load_fixtures()
        by_id = {case["case_id"]: case for case in manifest["cases"]}
        exceeded = validator.validate_payload(
            validator.materialize_case(manifest, by_id["consent-ttl-over-24-hours"])
        )
        insufficient = validator.validate_payload(
            validator.materialize_case(
                manifest, by_id["consent-ttl-insufficient-for-job"]
            )
        )
        self.assertEqual(("CONSENT_TTL_EXCEEDED",), tuple(x.code for x in exceeded.findings))
        self.assertEqual(
            ("CONSENT_TTL_INSUFFICIENT",),
            tuple(x.code for x in insufficient.findings),
        )

    def test_ga4gh_summaries_are_explicit_and_urls_are_opaque_synthetic_refs(self) -> None:
        manifest = validator.load_fixtures()
        base = manifest["base"]
        self.assertEqual("GA4GH_PASSPORT_1_2_1", base["identity"]["passport_profile"])
        self.assertEqual("ControlledAccessGrants", base["identity"]["visas"][0]["type"])
        for key in ("target_ref",):
            self.assertIn(".invalid/", base[key])
        for key in ("value_ref", "issuer_ref", "source_ref"):
            self.assertIn(".invalid/", base["identity"]["visas"][0][key])

    def test_fixture_contains_no_jwt_bearer_or_genomic_payload(self) -> None:
        text = validator.FIXTURES.read_text(encoding="utf-8")
        for marker in (
            "Bearer ",
            "eyJhbGci",
            "ga4gh_passport_v1\": [\"eyJ",
            "raw_genotype",
            "raw_sequence",
            "vcf_payload",
            "fasta_payload",
        ):
            self.assertNotIn(marker, text)

    def test_validation_is_no_network(self) -> None:
        manifest = validator.load_fixtures()
        denied = AssertionError("gatehouse preflight attempted network access")
        with (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
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
        expected_id = document["preflight_id"]
        reordered = dict(reversed(list(copy.deepcopy(document).items())))
        self.assertEqual(expected_hash, validator.expected_spec_hash(reordered))
        self.assertEqual(expected_id, validator.expected_preflight_id(expected_hash))
        reordered["requested_ttl_seconds"] = 7200
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
        self.assertIn('"suite_match":true', fixture_run.stdout)

        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        with tempfile.TemporaryDirectory() as raw:
            path = Path(raw) / "preflight.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(Path(validator.__file__)), str(path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual("HOLD", json.loads(completed.stdout)["outcome"])

    def test_duplicate_json_fails_without_echoing_sensitive_value(self) -> None:
        sentinel = "SENSITIVE_TOKEN_SENTINEL_THAT_MUST_NOT_ECHO"
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
        self.assertEqual(1, completed.returncode)
        self.assertNotIn(sentinel, completed.stdout)
        payload = json.loads(completed.stdout)
        self.assertEqual("GATEHOUSE_INPUT_INVALID", payload["findings"][0]["code"])

    def test_validator_has_no_host_or_token_client(self) -> None:
        source = Path(validator.__file__).read_text(encoding="utf-8")
        for token in (
            "requests",
            "urllib.request",
            "httpx",
            "aiohttp",
            "jwt.decode",
            "jose.jwt",
            "openid",
            "oauthlib",
        ):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
