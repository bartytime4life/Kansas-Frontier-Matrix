"""Deterministic no-network tests for the Fauna tile field allowlist profile."""

from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    ROOT
    / "tools"
    / "validators"
    / "domains"
    / "fauna"
    / "tiles"
    / "validate_tile_field_allowlist.py"
)
SPEC = importlib.util.spec_from_file_location("kfm_fauna_tile_field_allowlist", MODULE_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError("tile field allowlist validator could not be loaded")
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/fauna/tile_field_allowlist.schema.json"
POLICY_PATH = ROOT / "policy/domains/fauna/tile_field_allowlist.yaml"
FIXTURE_PATH = ROOT / "fixtures/domains/fauna/layers/tile_field_allowlist_cases.json"


class NetworkDenied(RuntimeError):
    """Raised if the focused suite attempts network access."""


def _deny_network(*_args, **_kwargs):
    raise NetworkDenied("network access is forbidden in tile allowlist tests")


class TileFieldAllowlistTests(unittest.TestCase):
    def setUp(self) -> None:
        self.network_patches = [
            mock.patch.object(socket, "create_connection", _deny_network),
            mock.patch.object(socket.socket, "connect", _deny_network),
        ]
        for patch in self.network_patches:
            patch.start()
            self.addCleanup(patch.stop)

        policy, findings = validator.load_policy(POLICY_PATH)
        self.assertEqual((), findings)
        self.assertIsNotNone(policy)
        self.policy = policy
        suite = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        self.valid_candidate = copy.deepcopy(suite["cases"][0]["candidate"])

    def test_schema_is_valid_closed_and_non_authoritative(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        for name in ("applies_to", "candidate_requirements", "authority_claims"):
            self.assertFalse(schema["properties"][name]["additionalProperties"])
        authority = schema["properties"]["authority_claims"]["properties"]
        self.assertTrue(authority)
        self.assertTrue(all(item == {"const": False} for item in authority.values()))

    def test_canonical_policy_passes_and_remains_inactive(self) -> None:
        result = validator.validate_policy(self.policy)
        self.assertEqual("PASS", result.outcome)
        self.assertEqual([], result.codes)
        self.assertEqual("KFM-P18-INV-400", self.policy["source_card"])
        self.assertEqual("PROPOSED_INACTIVE_FIXTURE_ONLY", self.policy["profile_status"])
        self.assertEqual(
            {"evidence_ref", "feature_id"},
            set(self.policy["required_public_fields"]),
        )
        self.assertTrue(all(value is False for value in self.policy["authority_claims"].values()))

    def test_fixture_replay_matches_all_exact_negative_polarities(self) -> None:
        ok, report = validator.run_fixture_suite(self.policy)
        self.assertTrue(ok, report)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual(8, len(report["cases"]))
        self.assertTrue(all(case["ok"] for case in report["cases"]))
        self.assertEqual(
            {"DENY", "PASS"},
            {case["actual_outcome"] for case in report["cases"]},
        )

    def test_valid_candidate_is_format_neutral_within_declared_scope(self) -> None:
        for vector_format in ("MLT", "MVT", "PMTILES"):
            with self.subTest(vector_format=vector_format):
                candidate = copy.deepcopy(self.valid_candidate)
                candidate["vector_format"] = vector_format
                result = validator.evaluate_candidate(self.policy, candidate)
                self.assertEqual("PASS", result.outcome)
                self.assertEqual([], result.codes)

    def test_manifest_declaration_cannot_approve_forbidden_coordinates(self) -> None:
        candidate = copy.deepcopy(self.valid_candidate)
        candidate["encoded_fields"].extend(["latitude", "longitude"])
        candidate["encoded_fields"].sort()
        candidate["layer_manifest_public_field_allowlist"].extend(["latitude", "longitude"])
        candidate["layer_manifest_public_field_allowlist"].sort()
        result = validator.evaluate_candidate(self.policy, candidate)
        self.assertEqual("DENY", result.outcome)
        self.assertEqual(
            [
                "ENCODED_FIELD_NOT_POLICY_ALLOWLISTED",
                "FORBIDDEN_FIELD_DECLARED",
                "LAYER_MANIFEST_FIELD_NOT_POLICY_ALLOWLISTED",
            ],
            result.codes,
        )

    def test_encoded_fields_must_be_manifest_allowlisted(self) -> None:
        candidate = copy.deepcopy(self.valid_candidate)
        candidate["layer_manifest_public_field_allowlist"].remove("freshness_state")
        result = validator.evaluate_candidate(self.policy, candidate)
        self.assertEqual(["ENCODED_FIELD_NOT_IN_LAYER_MANIFEST"], result.codes)

    def test_click_to_evidence_fixture_fields_are_required(self) -> None:
        candidate = copy.deepcopy(self.valid_candidate)
        candidate["encoded_fields"].remove("evidence_ref")
        candidate["layer_manifest_public_field_allowlist"].remove("evidence_ref")
        result = validator.evaluate_candidate(self.policy, candidate)
        self.assertEqual(
            [
                "REQUIRED_PUBLIC_FIELD_MISSING",
                "REQUIRED_PUBLIC_FIELD_NOT_IN_LAYER_MANIFEST",
            ],
            result.codes,
        )

    def test_style_only_protection_and_authority_elevation_are_denied(self) -> None:
        candidate = copy.deepcopy(self.valid_candidate)
        candidate["style_only_protection"] = True
        candidate["authority_claims"]["release_authority"] = True
        result = validator.evaluate_candidate(self.policy, candidate)
        self.assertEqual(
            ["AUTHORITY_CLAIM_FORBIDDEN", "STYLE_ONLY_PROTECTION_FORBIDDEN"],
            result.codes,
        )

    def test_policy_rejects_parallel_allow_and_deny_semantics(self) -> None:
        policy = copy.deepcopy(self.policy)
        policy["allowed_public_fields"].append("observer_email")
        policy["allowed_public_fields"].sort()
        result = validator.validate_policy(policy)
        self.assertEqual("DENY", result.outcome)
        self.assertIn("POLICY_ALLOWED_FIELD_FORBIDDEN", result.codes)
        self.assertIn("POLICY_ALLOWED_FIELD_MATCHES_DENY_PATTERN", result.codes)

    def test_policy_collections_must_be_sorted_and_unique(self) -> None:
        policy = copy.deepcopy(self.policy)
        policy["required_public_fields"] = ["feature_id", "evidence_ref"]
        result = validator.validate_policy(policy)
        self.assertEqual("DENY", result.outcome)
        self.assertIn("POLICY_COLLECTION_NOT_SORTED_UNIQUE", result.codes)

    def test_duplicate_yaml_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.yaml"
            path.write_text(
                "object_type: FaunaTileFieldAllowlistProfile\nobject_type: duplicate\n",
                encoding="utf-8",
            )
            policy, findings = validator.load_policy(path)
        self.assertIsNone(policy)
        self.assertEqual(["POLICY_DUPLICATE_KEY"], sorted(item.code for item in findings))

    def test_cli_fixture_mode_emits_value_safe_machine_output(self) -> None:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            exit_code = validator.main(["--fixtures"])
        self.assertEqual(0, exit_code)
        payload = json.loads(buffer.getvalue())
        self.assertEqual("NONE", payload["authority"])
        self.assertEqual("PASS", payload["outcome"])
        serialized = buffer.getvalue()
        self.assertNotIn("latitude", serialized)
        self.assertNotIn("observer_email", serialized)


if __name__ == "__main__":
    unittest.main()
