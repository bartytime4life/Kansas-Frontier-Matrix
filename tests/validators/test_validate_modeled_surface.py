from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/validate_modeled_surface.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/modeled_surface.schema.json"

spec = importlib.util.spec_from_file_location("validate_modeled_surface", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class ModeledSurfaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases = validator.load_fixture_cases()
        cls.by_name = {
            raw["name"]: (raw, candidate) for raw, candidate in cls.cases
        }

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        observed = {"PASS": 0, "DENY": 0, "ERROR": 0}
        for raw, candidate in self.cases:
            result = validator.validate_payload(candidate)
            observed[result.outcome] += 1
            self.assertEqual(result.outcome, raw["expected_outcome"], raw["name"])
            self.assertEqual(
                [item.code for item in result.findings],
                raw["expected_findings"],
                raw["name"],
            )
        self.assertEqual(observed, {"PASS": 4, "DENY": 15, "ERROR": 1})

    def test_identity_is_stable_across_mapping_order(self) -> None:
        candidate = self.by_name["valid_inside_support_current"][1]
        reordered = {key: candidate[key] for key in reversed(list(candidate))}
        self.assertEqual(validator.canonical_spec_hash(reordered), candidate["spec_hash"])
        self.assertEqual(validator.expected_surface_id(reordered), candidate["modeled_surface_id"])

    def test_model_role_support_and_derived_posture_are_fixed(self) -> None:
        expected = {
            "source_role_collapse": "SOURCE_ROLE_COLLAPSE",
            "support_type_collapse": "SUPPORT_TYPE_COLLAPSE",
            "derived_only_missing": "DERIVED_ONLY_REQUIRED",
            "field_truth_overclaim": "FIELD_TRUTH_OVERCLAIM",
        }
        for name, code in expected.items():
            result = validator.validate_payload(self.by_name[name][1])
            self.assertEqual(result.outcome, "DENY")
            self.assertEqual([item.code for item in result.findings], [code])

    def test_model_version_and_training_support_are_required(self) -> None:
        expected = {
            "model_version_missing": "MODEL_CONTEXT_INCOMPLETE",
            "training_support_missing": "TRAINING_SUPPORT_INCOMPLETE",
        }
        for name, code in expected.items():
            result = validator.validate_payload(self.by_name[name][1])
            self.assertEqual([item.code for item in result.findings], [code])

    def test_resolution_and_support_confidence_fail_closed(self) -> None:
        expected = {
            "grid_resolution_missing": "GRID_RESOLUTION_REQUIRED",
            "outside_support_confidence_overclaim": "SUPPORT_CONFIDENCE_OVERCLAIM",
            "uncertainty_reference_missing": "UNCERTAINTY_REFERENCE_REQUIRED",
        }
        for name, code in expected.items():
            result = validator.validate_payload(self.by_name[name][1])
            self.assertEqual([item.code for item in result.findings], [code])

    def test_model_time_dimensions_remain_distinct(self) -> None:
        expected = {
            "training_cutoff_after_model_run": "TRAINING_CUTOFF_AFTER_MODEL_RUN",
            "validity_interval_inverted": "VALIDITY_INTERVAL_INVALID",
        }
        for name, code in expected.items():
            result = validator.validate_payload(self.by_name[name][1])
            self.assertEqual([item.code for item in result.findings], [code])

    def test_release_public_and_effect_overclaims_are_separate(self) -> None:
        expected = {
            "release_overclaim": "RELEASE_OVERCLAIM",
            "public_use_overclaim": "PUBLIC_USE_OVERCLAIM",
            "effect_overclaim": "EFFECT_OVERCLAIM",
        }
        for name, code in expected.items():
            result = validator.validate_payload(self.by_name[name][1])
            self.assertEqual(result.outcome, "DENY")
            self.assertEqual([item.code for item in result.findings], [code])

    def test_duplicate_json_key_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"profile":"a","profile":"b"}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings, (validator.Finding("JSON_DUPLICATE_KEY", "/"),))

    def test_nonfinite_json_number_is_operational_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":Infinity}', encoding="utf-8")
            result = validator.validate_file(path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings, (validator.Finding("JSON_NONFINITE_NUMBER", "/"),))

    def test_symlink_input_is_denied(self) -> None:
        if not hasattr(os, "symlink"):
            self.skipTest("symbolic links are unavailable")
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = Path(directory) / "link.json"
            link.symlink_to(target)
            result = validator.validate_file(link)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.findings, (validator.Finding("INPUT_SYMLINK_DENIED", "/"),))

    def test_validator_has_no_network_client_import(self) -> None:
        source = VALIDATOR_PATH.read_text(encoding="utf-8")
        forbidden = ("import requests", "import httpx", "import aiohttp", "import socket", "from urllib", "urlopen(")
        self.assertFalse(any(token in source for token in forbidden))

    def test_cli_pass_is_value_free_and_authority_is_false(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.json"
            path.write_text(json.dumps(self.by_name["valid_inside_support_current"][1]), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), str(path)],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(set(payload["authority"].values()), {False})
        self.assertNotIn("synthetic-model-provider", completed.stdout)
        self.assertNotIn("synthetic_environmental_index", completed.stdout)

    def test_fixture_cli_replays_every_case(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--fixtures"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        rows = [json.loads(line) for line in completed.stdout.splitlines() if line.strip()]
        self.assertEqual(len(rows), 20)
        self.assertEqual({row["outcome"] for row in rows}, {"PASS", "DENY", "ERROR"})


if __name__ == "__main__":
    unittest.main()
