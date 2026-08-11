"""Deterministic no-network tests for map-build sustainability telemetry."""

from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import re
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/telemetry/validate_map_build_sustainability.py"
SPEC = importlib.util.spec_from_file_location("kfm_map_build_sustainability", MODULE_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError("map-build sustainability validator could not be loaded")
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

SCHEMA_PATH = ROOT / "schemas/contracts/v1/telemetry/map_build_sustainability.schema.json"
FIXTURE_PATH = ROOT / "fixtures/contracts/v1/telemetry/map_build_sustainability/cases.json"
WORKFLOW_PATH = ROOT / ".github/workflows/map-build-sustainability-telemetry.yml"


class NetworkDenied(RuntimeError):
    """Raised if the focused suite attempts network access."""


def _deny_network(*_args, **_kwargs):
    raise NetworkDenied("network access is forbidden in sustainability telemetry tests")


class MapBuildSustainabilityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.network_patches = [
            mock.patch.object(socket, "create_connection", _deny_network),
            mock.patch.object(socket.socket, "connect", _deny_network),
        ]
        for patch in self.network_patches:
            patch.start()
            self.addCleanup(patch.stop)
        suite = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        self.cases = validator._materialize_cases(suite["cases"])
        self.valid = copy.deepcopy(self.cases[0]["candidate"])

    def test_schema_is_valid_closed_and_non_authoritative(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        for name in ("review_posture", "sensitivity", "authority_claims"):
            self.assertFalse(schema["properties"][name]["additionalProperties"])
        authority = schema["properties"]["authority_claims"]["properties"]
        self.assertTrue(all(value == {"const": False} for value in authority.values()))

    def test_fixture_replay_matches_exact_pass_abstain_and_deny_polarity(self) -> None:
        ok, report = validator.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual(11, len(report["cases"]))
        self.assertEqual(
            {"PASS", "ABSTAIN", "DENY"},
            {case["actual_outcome"] for case in report["cases"]},
        )
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_valid_candidate_passes_without_authority(self) -> None:
        result = validator.validate_candidate(self.valid)
        self.assertEqual("PASS", result.outcome)
        self.assertEqual([], result.codes)
        self.assertEqual("REVIEW_SIGNAL_ONLY", self.valid["review_posture"]["purpose"])
        self.assertTrue(all(value is False for value in self.valid["authority_claims"].values()))

    def test_missing_measurement_abstains_instead_of_inventing_zero(self) -> None:
        result = validator.validate_candidate(self.cases[2]["candidate"])
        self.assertEqual("ABSTAIN", result.outcome)
        self.assertEqual([], result.codes)

    def test_missing_factor_abstains_without_automatic_release_effect(self) -> None:
        result = validator.validate_candidate(self.cases[3]["candidate"])
        self.assertEqual("ABSTAIN", result.outcome)
        self.assertEqual(
            "NONE",
            self.cases[3]["candidate"]["review_posture"]["release_decision_effect"],
        )

    def test_carbon_arithmetic_mismatch_is_denied(self) -> None:
        result = validator.validate_candidate(self.cases[4]["candidate"])
        self.assertEqual("DENY", result.outcome)
        self.assertEqual(["CARBON_CALCULATION_MISMATCH"], result.codes)

    def test_carbon_without_energy_is_denied(self) -> None:
        result = validator.validate_candidate(self.cases[5]["candidate"])
        self.assertEqual(["CARBON_REQUIRES_ENERGY"], result.codes)

    def test_window_and_uncertainty_bounds_are_denied(self) -> None:
        self.assertEqual(
            ["MEASUREMENT_WINDOW_INVALID"],
            validator.validate_candidate(self.cases[6]["candidate"]).codes,
        )
        self.assertEqual(
            ["UNCERTAINTY_PERCENT_OUT_OF_RANGE"],
            validator.validate_candidate(self.cases[7]["candidate"]).codes,
        )

    def test_authority_and_release_effect_cannot_be_elevated(self) -> None:
        self.assertEqual(
            ["SCHEMA_INVALID"],
            validator.validate_candidate(self.cases[8]["candidate"]).codes,
        )
        self.assertEqual(
            ["SCHEMA_INVALID"],
            validator.validate_candidate(self.cases[9]["candidate"]).codes,
        )

    def test_rounding_tolerance_cannot_hide_a_mismatch(self) -> None:
        result = validator.validate_candidate(self.cases[10]["candidate"])
        self.assertEqual("DENY", result.outcome)
        self.assertEqual(["ROUNDING_TOLERANCE_OUT_OF_RANGE"], result.codes)

    def test_missing_canonical_schema_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.schema.json"
            with mock.patch.object(validator, "SCHEMA_PATH", missing):
                result = validator.validate_candidate(self.valid)
        self.assertEqual("ERROR", result.outcome)
        self.assertEqual(["SCHEMA_UNAVAILABLE"], result.codes)

    def test_validation_does_not_mutate_candidate(self) -> None:
        before = copy.deepcopy(self.valid)
        validator.validate_candidate(self.valid)
        self.assertEqual(before, self.valid)

    def test_json_loader_rejects_duplicate_keys_and_surrogates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            self.assertEqual(
                ["JSON_DUPLICATE_KEY"],
                [item.code for item in validator.load_json(duplicate)[1]],
            )
            surrogate = Path(directory) / "surrogate.json"
            surrogate.write_text('{"a":"\\ud800"}', encoding="utf-8")
            self.assertEqual(
                ["JSON_UNPAIRED_SURROGATE"],
                [item.code for item in validator.load_json(surrogate)[1]],
            )
            oversized = Path(directory) / "oversized.json"
            oversized.write_text(" " * (validator.MAX_JSON_BYTES + 1), encoding="utf-8")
            self.assertEqual(
                ["JSON_INPUT_INVALID"],
                [item.code for item in validator.load_json(oversized)[1]],
            )
            symlink = Path(directory) / "candidate-link.json"
            symlink.symlink_to(duplicate)
            self.assertEqual(
                ["JSON_INPUT_INVALID"],
                [item.code for item in validator.load_json(symlink)[1]],
            )

    def test_cli_bytes_are_deterministic_and_abstain_is_safe_completion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(self.cases[2]["candidate"]), encoding="utf-8")
            outputs = []
            for _ in range(2):
                stream = io.StringIO()
                with contextlib.redirect_stdout(stream):
                    code = validator.main(["--candidate", str(path)])
                self.assertEqual(0, code)
                outputs.append(stream.getvalue())
            self.assertEqual(outputs[0], outputs[1])
            self.assertEqual("ABSTAIN", json.loads(outputs[0])["outcome"])

    def test_validator_and_workflow_are_no_network_read_only(self) -> None:
        source = MODULE_PATH.read_text(encoding="utf-8")
        for token in (
            "import requests",
            "import urllib",
            "import httpx",
            "import socket",
            "subprocess",
            "git push",
        ):
            self.assertNotIn(token, source)
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertIn('persist-credentials: false', workflow)
        self.assertNotIn("secrets.", workflow)
        self.assertNotIn("actions/upload-artifact", workflow)
        self.assertIn("validate_generated_receipt.py", workflow)
        self.assertIn(
            "genrec-map-build-sustainability-telemetry-20260811.json",
            workflow,
        )
        pins = [
            line.strip().split("uses: ", 1)[1].split(" #", 1)[0]
            for line in workflow.splitlines()
            if "uses: " in line
        ]
        self.assertTrue(pins)
        self.assertTrue(all(re.fullmatch(r"[^@]+@[0-9a-f]{40}", pin) for pin in pins))


if __name__ == "__main__":
    unittest.main()
