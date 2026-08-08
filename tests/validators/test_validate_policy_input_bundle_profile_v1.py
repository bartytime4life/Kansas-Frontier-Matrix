from __future__ import annotations

import copy
import importlib.util
import json
import socket
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT / "tools/validators/policy/validate_policy_input_bundle_profile_v1.py"
)
SCHEMA_PATH = (
    REPO_ROOT / "schemas/contracts/v1/policy/policy_input_bundle_profile_v1.schema.json"
)
VALID_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/policy/policy_input_bundle_profile_v1/valid/valid_1.json"
)

SPEC = importlib.util.spec_from_file_location(
    "validate_policy_input_bundle_profile_v1", VALIDATOR_PATH
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PolicyInputBundleProfileV1Tests(unittest.TestCase):
    def _valid(self) -> dict[str, object]:
        return json.loads(VALID_PATH.read_text(encoding="utf-8"))

    def test_schema_is_closed_and_inactive(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertEqual(schema["x-kfm"]["execution_mode"], "FIXTURE_ONLY")

    def test_valid_public_render_passes(self) -> None:
        self.assertTrue(MODULE.validate_record(VALID_PATH).ok)

    def test_semantic_negative_polarity(self) -> None:
        unresolved = self._valid()
        unresolved["evidence"]["resolution_status"] = "UNRESOLVED"
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(unresolved).findings},
            {"EVIDENCE_NOT_RESOLVED"},
        )

        unknown_rights = self._valid()
        unknown_rights["rights"]["status"] = "UNKNOWN"
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(unknown_rights).findings},
            {"PUBLIC_RIGHTS_NOT_CLEAR", "RIGHTS_UNRESOLVED"},
        )

        unsafe_precision = self._valid()
        unsafe_precision["sensitivity"]["exact_location"] = True
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(unsafe_precision).findings},
            {"PUBLIC_EXACT_LOCATION_DENIED"},
        )

        noncanonical = self._valid()
        noncanonical["evidence"]["evidence_refs"] = ["evidence:z", "evidence:a"]
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(noncanonical).findings},
            {"REFERENCES_NOT_CANONICAL"},
        )

    def test_release_prerequisites_fail_closed(self) -> None:
        release = self._valid()
        release["operation"] = "RELEASE"
        release["audience"] = "RELEASE_GATE"
        release["release"] = {
            "state": "CANDIDATE",
            "release_manifest_ref": None,
            "rollback_ref": None,
        }
        self.assertEqual(
            {item.code for item in MODULE.validate_payload(release).findings},
            {"RELEASE_MANIFEST_REQUIRED", "ROLLBACK_REFERENCE_REQUIRED"},
        )

    def test_governance_overclaim_is_schema_invalid(self) -> None:
        overclaim = self._valid()
        overclaim["governance"]["policy_evaluated"] = True
        self.assertIn(
            "SCHEMA_INVALID",
            {item.code for item in MODULE.validate_payload(overclaim).findings},
        )

    def test_cli_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.serialize(VALID_PATH, MODULE.validate_record(VALID_PATH))
            second = MODULE.serialize(VALID_PATH, MODULE.validate_record(VALID_PATH))
        self.assertEqual(first, second)

        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), str(VALID_PATH)],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertEqual(len(completed.stdout.splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
