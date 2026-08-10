from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/ui/validate_renderer_capability_profile.py"
spec = importlib.util.spec_from_file_location("renderer_capability_profile", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class RendererCapabilityProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()

    def test_schema_self_check(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        validator.Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        self.assertGreaterEqual(len(self.manifest["cases"]), 15)
        outcomes: set[str] = set()
        for case in self.manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                result = validator.validate_payload(
                    validator.materialize_case(self.manifest, case)
                )
                outcomes.add(result.outcome)
                self.assertEqual(case["expected_outcome"], result.outcome)
                self.assertEqual(case["expected_profile_state"], result.profile_state)
                self.assertEqual(
                    case["expected_findings"],
                    [
                        {"code": finding.code, "path": finding.path}
                        for finding in result.findings
                    ],
                )
        self.assertEqual({"PASS", "ABSTAIN", "DENY"}, outcomes)

    def test_positive_profile_is_review_required_and_non_authorizing(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("REVIEW_REQUIRED", result.profile_state)
        self.assertFalse(value["compatibility"]["production_selection_authorized"])
        self.assertFalse(value["boundary"]["direct_store_access"])
        self.assertFalse(value["boundary"]["network_probe_performed"])
        self.assertFalse(value["governance"]["release_authorized"])
        self.assertFalse(value["governance"]["publication_authorized"])

    def test_browser_rule_is_fail_closed(self) -> None:
        case = next(
            item
            for item in self.manifest["cases"]
            if item["case_id"] == "native_renderer_in_browser_denied"
        )
        result = validator.validate_payload(validator.materialize_case(self.manifest, case))
        self.assertEqual("DENY", result.outcome)
        self.assertEqual("RENDERER_BROWSER_RULE_VIOLATION", result.findings[0].code)

    def test_declared_contract_references_exist(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        for contract_ref in value["contract_refs"]:
            path = ROOT / contract_ref
            self.assertTrue(path.is_file(), path)
            self.assertFalse(path.is_symlink(), path)

    def test_duplicate_key_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}\n', encoding="utf-8")
            self.assertEqual(
                "RENDERER_JSON_DUPLICATE_KEY",
                validator.validate_file(duplicate).findings[0].code,
            )

            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}\n', encoding="utf-8")
            self.assertEqual(
                "RENDERER_JSON_NONFINITE_NUMBER",
                validator.validate_file(nonfinite).findings[0].code,
            )

            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            symlink = root / "link.json"
            symlink.symlink_to(target)
            self.assertEqual(
                "RENDERER_INPUT_SYMLINK_DENIED",
                validator.validate_file(symlink).findings[0].code,
            )

            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + b" " * validator.MAX_BYTES + b"}")
            self.assertEqual(
                "RENDERER_INPUT_TOO_LARGE",
                validator.validate_file(oversized).findings[0].code,
            )

    def test_validation_does_not_open_network(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        with patch("socket.socket", side_effect=AssertionError("network denied")):
            result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)

    def test_serialization_does_not_echo_candidate_values(self) -> None:
        case = {
            "mutations": [
                {
                    "path": "/renderer/implementation_ref",
                    "value": "urn:kfm:synthetic:renderer:postgres-secret-marker",
                }
            ]
        }
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        output = validator._serialize(Path("candidate.json"), result)
        self.assertNotIn("secret-marker", output)
        self.assertIn("RENDERER_IMPLEMENTATION_REFERENCE_DENIED", output)

    def test_cli_fixture_replay_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
