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

ROOT = Path(__file__).resolve().parents[5]
VALIDATOR_PATH = (
    ROOT
    / "tools/validators/domains/habitat/validate_cover_class_crosswalk_profile.py"
)
SCHEMA_PATH = (
    ROOT
    / "schemas/contracts/v1/domains/habitat/land_cover/cover_class_crosswalk_profile.schema.json"
)

SPEC = importlib.util.spec_from_file_location("cover_class_crosswalk_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


class CoverClassCrosswalkProfileTests(unittest.TestCase):
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

    def test_positive_candidate_is_review_required_and_non_authorizing(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        result = validator.validate_payload(value)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual("REVIEW_REQUIRED", result.profile_state)
        self.assertFalse(value["summary"]["silent_recode_authorized"])
        self.assertFalse(value["summary"]["reverse_use_authorized"])
        self.assertFalse(value["governance"]["recodes_source_data"])
        self.assertFalse(value["governance"]["source_activation_authority"])
        self.assertFalse(value["governance"]["renderer_authority"])
        self.assertFalse(value["governance"]["release_authority"])
        self.assertFalse(value["governance"]["publication_authority"])

    def test_every_source_class_is_accounted_once(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        declared = value["source_scheme"]["class_codes"]
        mapped = [code for row in value["mappings"] for code in row["source_codes"]]
        self.assertEqual(declared, sorted(mapped))
        self.assertEqual(len(mapped), len(set(mapped)))
        self.assertEqual(0, value["summary"]["unmapped_source_class_count"])

    def test_ontology_references_bind_scheme_versions(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        self.assertTrue(validator._version_bound(value["source_scheme"]))
        self.assertTrue(validator._version_bound(value["target_scheme"]))
        self.assertTrue(value["summary"]["ontology_versions_bound"])

    def test_many_to_one_mapping_is_lossy_and_caveated(self) -> None:
        value = validator.materialize_case(self.manifest, self.manifest["cases"][0])
        aggregate = next(
            row for row in value["mappings"] if row["mapping_state"] == "AGGREGATED"
        )
        self.assertGreaterEqual(len(aggregate["source_codes"]), 2)
        self.assertEqual(1, len(aggregate["target_codes"]))
        self.assertTrue(aggregate["lossy"])
        self.assertTrue(aggregate["caveat_required"])

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
                "CROSSWALK_JSON_DUPLICATE_KEY",
                validator.validate_file(duplicate).findings[0].code,
            )

            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}\n', encoding="utf-8")
            self.assertEqual(
                "CROSSWALK_JSON_NONFINITE_NUMBER",
                validator.validate_file(nonfinite).findings[0].code,
            )

            target = root / "target.json"
            target.write_text("{}\n", encoding="utf-8")
            symlink = root / "link.json"
            symlink.symlink_to(target)
            self.assertEqual(
                "CROSSWALK_INPUT_SYMLINK_DENIED",
                validator.validate_file(symlink).findings[0].code,
            )

            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + b" " * validator.MAX_BYTES + b"}")
            self.assertEqual(
                "CROSSWALK_INPUT_TOO_LARGE",
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
                    "path": "/mappings/0/target_codes",
                    "value": ["secret-marker"],
                }
            ]
        }
        value = validator.materialize_case(self.manifest, case)
        result = validator.validate_payload(value)
        output = validator._serialize(Path("candidate.json"), result)
        self.assertNotIn("secret-marker", output)
        self.assertIn("CROSSWALK_TARGET_CODE_UNKNOWN", output)

    def test_cli_fixture_replay_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR_PATH), "--fixtures"]
        first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
