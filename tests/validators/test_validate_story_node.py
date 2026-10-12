from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
import unittest
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/ui/validate_story_node.py"
SPEC = importlib.util.spec_from_file_location("validate_story_node", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class StoryNodeValidatorTests(unittest.TestCase):
    def test_fixture_matrix_has_exact_polarity(self) -> None:
        self.assertEqual(0, MODULE.run_fixtures())

    def test_schema_is_closed_and_pins_projection_profile(self) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            "kfm.ui.story-node.public-safe.v1",
            schema["properties"]["profile"]["const"],
        )
        self.assertEqual(
            ["READY", "PARTIAL", "ABSTAINED", "BLOCKED", "ERROR", "SUPERSEDED"],
            schema["properties"]["state"]["enum"],
        )
        self.assertFalse(schema["properties"]["authoritative"]["const"])
        self.assertTrue(schema["properties"]["projection_only"]["const"])

    def test_valid_lane_covers_all_finite_states(self) -> None:
        manifest = json.loads(MODULE.EXPECTED_MANIFEST.read_text(encoding="utf-8"))
        states = {
            json.loads((MODULE.FIXTURES_ROOT / "valid" / name).read_text(encoding="utf-8"))["state"]
            for name in manifest["valid"]
        }
        self.assertEqual(
            {"READY", "PARTIAL", "ABSTAINED", "BLOCKED", "ERROR", "SUPERSEDED"},
            states,
        )

    def test_ready_requires_release_safe_support(self) -> None:
        findings = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "semantic_invalid/ready-unreleased.json"
        )
        codes = {item.code for item in findings}
        self.assertIn("READY_TRUST_STATE_INVALID", codes)
        self.assertIn("UNRELEASED_READY_DENIED", codes)

    def test_blocked_and_error_states_do_not_leak_support(self) -> None:
        blocked = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "semantic_invalid/blocked-support-leak.json"
        )
        error = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "semantic_invalid/error-support-leak.json"
        )
        self.assertIn("BLOCKED_SUPPORT_LEAK", {item.code for item in blocked})
        self.assertIn("ERROR_SUPPORT_LEAK", {item.code for item in error})

    def test_corrected_ready_requires_correction_reference(self) -> None:
        findings = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "semantic_invalid/corrected-without-correction-ref.json"
        )
        self.assertIn("CORRECTED_REFS_REQUIRED", {item.code for item in findings})

    def test_superseded_node_requires_nonself_replacement_and_correction(self) -> None:
        missing = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "semantic_invalid/superseded-without-correction.json"
        )
        self_ref = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "semantic_invalid/supersession-self-reference.json"
        )
        self.assertIn("SUPERSEDED_CORRECTION_REQUIRED", {item.code for item in missing})
        self.assertIn("SUPERSESSION_SELF_REFERENCE", {item.code for item in self_ref})

    def test_unresolved_rights_fail_closed(self) -> None:
        findings = MODULE.validate_payload(
            MODULE.FIXTURES_ROOT / "semantic_invalid/rights-unresolved-answer.json"
        )
        codes = {item.code for item in findings}
        self.assertIn("READY_RIGHTS_INVALID", codes)
        self.assertIn("UNRESOLVED_RIGHTS_FAIL_CLOSED", codes)

    def test_validator_is_deterministic_and_no_network(self) -> None:
        path = MODULE.FIXTURES_ROOT / "valid/ready-corrected.json"
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "getaddrinfo", side_effect=AssertionError("dns denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("socket denied")):
            self.assertEqual(MODULE.validate_payload(path), MODULE.validate_payload(path))

    def test_cli_fixture_mode(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr + completed.stdout)
        self.assertIn("STORY_NODE_FIXTURES_VALID", completed.stdout)
        self.assertIn("authority=false", completed.stdout)


if __name__ == "__main__":
    unittest.main()
