from __future__ import annotations

import importlib.util
import json
import os
import socket
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = ROOT / "tools/validators/ui/validate_story_manifest.py"
SPEC = importlib.util.spec_from_file_location("validate_story_manifest", VALIDATOR_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class StoryManifestTests(unittest.TestCase):
    def test_schema_is_closed_valid_and_pins_projection_profile(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            "kfm.ui.story-manifest.public-safe.v1",
            schema["properties"]["profile"]["const"],
        )
        self.assertFalse(schema["properties"]["authoritative"]["const"])
        self.assertTrue(schema["properties"]["projection_only"]["const"])

    def test_exact_fixture_matrix(self) -> None:
        manifest = validator.load_fixtures()
        for case in manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(validator.materialize_case(manifest, case))
                actual = [{"code": item.code, "path": item.path} for item in result.findings]
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_findings"], actual)

    def test_positive_cases_cover_finite_states_and_both_outcomes(self) -> None:
        manifest = validator.load_fixtures()
        passing = [
            validator.materialize_case(manifest, case)
            for case in manifest["cases"]
            if case["expected_outcome"] == "PASS"
        ]
        self.assertEqual(
            {"READY", "PARTIAL", "ABSTAINED", "SUPERSEDED", "BLOCKED", "ERROR"},
            {item["state"] for item in passing},
        )
        outcomes = Counter(case["expected_outcome"] for case in manifest["cases"])
        self.assertEqual({"PASS": 6, "DENY": 11}, outcomes)

    def test_worst_constituent_is_visible(self) -> None:
        manifest = validator.load_fixtures()
        case = next(case for case in manifest["cases"] if case["case_id"] == "valid-blocked-rights")
        document = validator.materialize_case(manifest, case)
        self.assertEqual("BLOCKED", document["state"])
        self.assertEqual("DENY", document["outcome"])
        self.assertEqual(["kfm://story-node/context"], document["limiting_node_refs"])
        self.assertEqual(["RIGHTS_UNRESOLVED"], document["reason_codes"])

    def test_composite_trust_is_dimensionwise_least_permissive(self) -> None:
        manifest = validator.load_fixtures()
        case = next(case for case in manifest["cases"] if case["case_id"] == "valid-partial-stale")
        document = validator.materialize_case(manifest, case)
        self.assertEqual(
            document["trust_state"],
            validator._composite_trust(document["constituents"]),
        )
        drift = next(case for case in manifest["cases"] if case["case_id"] == "deny-trust-optimism")
        findings = validator.validate_payload(validator.materialize_case(manifest, drift)).findings
        self.assertEqual("STORY_MANIFEST_TRUST_REDUCTION_MISMATCH", findings[0].code)

    def test_projection_has_no_raw_body_claim_geometry_or_source_payload(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        keys: set[str] = set()

        def collect(value: object) -> None:
            if isinstance(value, dict):
                keys.update(value)
                for child in value.values():
                    collect(child)
            elif isinstance(value, list):
                for child in value:
                    collect(child)

        collect(document)
        self.assertTrue({"body", "claim", "coordinates", "geometry", "source_payload"}.isdisjoint(keys))

    def test_identity_is_content_addressed_and_replay_stable(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        first = validator.canonical_identity(document)
        second = validator.canonical_identity(json.loads(json.dumps(document)))
        self.assertEqual(first, second)
        changed = json.loads(json.dumps(document))
        changed["title"] += " changed"
        self.assertNotEqual(first, validator.canonical_identity(changed))

    def test_validation_is_deterministic_and_does_not_open_network(self) -> None:
        manifest = validator.load_fixtures()
        document = validator.materialize_case(manifest, manifest["cases"][0])
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "getaddrinfo", side_effect=AssertionError("dns denied")):
            self.assertEqual(validator.validate_payload(document), validator.validate_payload(document))

    def test_bounded_reader_rejects_duplicate_keys_and_non_object_roots(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            value, findings = validator._read(duplicate)
            self.assertIsNone(value)
            self.assertEqual("STORY_MANIFEST_JSON_DUPLICATE_KEY", findings[0].code)

            root = Path(directory) / "root.json"
            root.write_text("[]", encoding="utf-8")
            value, findings = validator._read(root)
            self.assertIsNone(value)
            self.assertEqual("STORY_MANIFEST_JSON_ROOT_INVALID", findings[0].code)

    def test_cli_fixture_mode_matches_manifest(self) -> None:
        env = os.environ.copy()
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=ROOT,
            env=env,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr + completed.stdout)
        payload = json.loads(completed.stdout)
        self.assertTrue(payload["suite_match"])
        self.assertEqual(17, payload["cases"])
        self.assertEqual("NONE", payload["authority"])

    def test_serialized_result_disclaims_authority(self) -> None:
        payload = json.loads(validator.serialize(None, validator.Result("PASS", ())))
        self.assertEqual("NONE", payload["authority"])
        self.assertEqual("FIXTURE_ONLY", payload["execution_mode"])
        self.assertIn("no_publication", payload["non_effects"])


if __name__ == "__main__":
    unittest.main()
