from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = (
    ROOT
    / "tools/validators/catalog_closure/validate_catalog_distribution_mapping_profile.py"
)
SCHEMA_PATH = (
    ROOT
    / "schemas/contracts/v1/data/catalog_distribution_mapping_profile.schema.json"
)

SPEC = importlib.util.spec_from_file_location("catalog_distribution_mapping_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class CatalogDistributionMappingProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = validator.load_fixtures()

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_fixture_matrix_is_exact(self) -> None:
        outcomes: set[str] = set()
        for case in self.manifest["cases"]:
            with self.subTest(case=case["case_id"]):
                value = validator.materialize_case(self.manifest, case)
                result = validator.validate_payload(value)
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
        self.assertEqual({"PASS", "DENY"}, outcomes)

    def test_positive_candidate_is_aligned_and_non_authorizing(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("REVIEW_REQUIRED", result.profile_state)
        self.assertEqual(validator.expected_alignment(value), value["alignment"])
        self.assertTrue(value["alignment"]["locator_digest_bound"])
        self.assertFalse(value["alignment"]["catalog_records_emitted"])
        self.assertFalse(value["governance"]["network_access"])
        self.assertFalse(value["governance"]["activates_oci_or_oras"])
        self.assertFalse(value["governance"]["authorizes_release"])
        self.assertFalse(value["governance"]["publishes"])

    def test_each_carrier_repeats_the_canonical_tuple(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        artifact = value["artifact"]
        carriers = value["carriers"]
        self.assertEqual(artifact["locator"], carriers["stac"]["href"])
        self.assertEqual(artifact["locator"], carriers["dcat"]["access_url"])
        self.assertEqual(artifact["locator"], carriers["prov"]["location"])
        self.assertEqual(artifact["digest"], carriers["stac"]["checksum"])
        self.assertEqual(artifact["digest"], carriers["dcat"]["checksum"])
        self.assertEqual(artifact["digest"], carriers["prov"]["checksum"])
        self.assertEqual(carriers["prov"]["entity_ref"], carriers["prov"]["generated_entity_ref"])

    def test_identity_is_content_addressed(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        spec_hash, candidate_id = validator.canonical_identity(value)
        self.assertEqual(spec_hash, value["spec_hash"])
        self.assertEqual(candidate_id, value["candidate_id"])

    def test_duplicate_nonfinite_symlink_and_oversize_are_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}\n', encoding="utf-8")
            self.assertEqual(
                "CATALOG_MAPPING_JSON_DUPLICATE_KEY",
                validator.validate_file(duplicate).findings[0].code,
            )

            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}\n', encoding="utf-8")
            self.assertEqual(
                "CATALOG_MAPPING_JSON_NONFINITE_NUMBER",
                validator.validate_file(nonfinite).findings[0].code,
            )

            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            symlink = root / "link.json"
            symlink.symlink_to(target)
            self.assertEqual(
                "CATALOG_MAPPING_INPUT_SYMLINK_DENIED",
                validator.validate_file(symlink).findings[0].code,
            )

            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + b" " * validator.MAX_BYTES + b"}")
            self.assertEqual(
                "CATALOG_MAPPING_INPUT_TOO_LARGE",
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
                    "path": "/carriers/stac/href",
                    "value": "urn:kfm:synthetic:distribution:secret-marker@sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                }
            ]
        }
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        output = validator._serialize(Path("candidate.json"), result)
        self.assertNotIn("secret-marker", output)
        self.assertIn("CATALOG_MAPPING_LOCATOR_MISMATCH", output)

    def test_cli_fixture_replay_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
