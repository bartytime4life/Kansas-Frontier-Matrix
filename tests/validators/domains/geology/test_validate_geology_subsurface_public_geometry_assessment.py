from __future__ import annotations

import copy
import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = ROOT / "tools/validators/validate_geology_subsurface_public_geometry_assessment.py"
SPEC = importlib.util.spec_from_file_location("geology_subsurface_public_geometry_assessment_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class GeologySubsurfacePublicGeometryAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        case = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, case)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 26)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_finite_outcome_counts(self) -> None:
        outcomes = [item["outcome"] for item in MODULE.validate_fixture_manifest()]
        self.assertEqual({"PASS": 4, "ABSTAIN": 3, "DENY": 18, "ERROR": 1}, {name: outcomes.count(name) for name in set(outcomes)})

    def test_pass_candidates_embed_no_geometry_or_coordinates(self) -> None:
        banned_keys = {"coordinates", "geometry", "latitude", "longitude", "site_location", "well_id"}
        for name in ("pass_borehole_generalized", "pass_borehole_withheld", "pass_well_log_generalized_reference", "pass_well_log_withheld"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            keys: set[str] = set()

            def collect(value: object) -> None:
                if isinstance(value, dict):
                    keys.update(str(key).lower() for key in value)
                    for item in value.values():
                        collect(item)
                elif isinstance(value, list):
                    for item in value:
                        collect(item)

            collect(candidate)
            self.assertTrue(banned_keys.isdisjoint(keys))
            self.assertFalse(candidate["governance"]["network_access"])
            self.assertFalse(candidate["governance"]["restricted_input_opened"])
            self.assertFalse(candidate["governance"]["lifecycle_mutated"])
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_identity_binds_projection_and_governance(self) -> None:
        candidate = self._candidate("pass_borehole_generalized")
        original = MODULE.compute_identity(candidate)
        changed = copy.deepcopy(candidate)
        changed["public_projection"]["precision_class"] = "COUNTY"
        self.assertNotEqual(original, MODULE.compute_identity(changed))
        changed = copy.deepcopy(candidate)
        changed["governance"]["rollback_ref"] = "fixture:rollback:changed"
        self.assertNotEqual(original, MODULE.compute_identity(changed))

    def test_exact_public_and_payload_release_fail_closed(self) -> None:
        for name in ("deny_exact_public_precision", "deny_source_precision_public", "deny_well_log_payload_public", "deny_borehole_payload_public"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_generalization_and_withholding_require_receipt_closure(self) -> None:
        for name in ("deny_generalized_missing_digest", "deny_generalized_missing_redaction", "deny_generalized_missing_quality_scope", "deny_withheld_missing_receipt"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "DENY")

    def test_unresolved_rights_or_sensitivity_abstains(self) -> None:
        for name in ("abstain_rights_unresolved", "abstain_sensitivity_unresolved"):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_duplicate_and_nonfinite_json_fail_safely(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            nonfinite = Path(directory) / "nonfinite.json"
            duplicate.write_text('{"value":1,"value":2}', encoding="utf-8")
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            self.assertEqual(["JSON_DUPLICATE_KEY"], [item.code for item in MODULE.load_json_object(duplicate)[1]])
            self.assertEqual(["JSON_NONFINITE_NUMBER"], [item.code for item in MODULE.load_json_object(nonfinite)[1]])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)

    def test_fixture_cli_rejects_abbreviated_flags(self) -> None:
        for length in range(3, len("--fixtures")):
            abbreviation = "--fixtures"[:length]
            with self.subTest(abbreviation=abbreviation):
                completed = subprocess.run(
                    [sys.executable, str(MODULE_PATH), abbreviation],
                    cwd=ROOT,
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(2, completed.returncode)
                self.assertEqual("", completed.stdout)
                self.assertIn("unrecognized arguments", completed.stderr)

    def test_fixture_cli_rejects_ignored_explicit_input(self) -> None:
        candidate = self._candidate("pass_borehole_generalized")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(MODULE_PATH), "--fixtures", str(path)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(2, completed.returncode)
        self.assertEqual("", completed.stdout)
        self.assertIn("input cannot be combined with --fixtures", completed.stderr)

    def test_option_terminator_allows_dash_prefixed_input_filename(self) -> None:
        candidate = self._candidate("pass_borehole_generalized")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "--fixtures"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(MODULE_PATH), "--", path.name],
                cwd=directory,
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(0, completed.returncode, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual("PASS", payload["outcome"])
        self.assertEqual("NONE", payload["authority"])
        self.assertNotIn("name", payload)
        self.assertNotIn("ok", payload)


if __name__ == "__main__":
    unittest.main()
