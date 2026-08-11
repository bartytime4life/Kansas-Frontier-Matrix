from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/source/validate_web_acquisition_conduct_assessment.py"
SPEC = importlib.util.spec_from_file_location(
    "validate_web_acquisition_conduct_assessment", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class WebAcquisitionConductAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.cases = {entry["name"]: entry for entry in cls.manifest["cases"]}

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self.cases[name])

    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        MODULE.Draft202012Validator.check_schema(schema)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), len(self.cases))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_profiles_remain_non_authoritative(self) -> None:
        for name in (
            "pass_official_api",
            "pass_html_scrape",
            "pass_source_authorized_proxy",
            "pass_browser_automation",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_unresolved_profiles_abstain(self) -> None:
        for name in (
            "abstain_unresolved_route",
            "abstain_unknown_terms",
            "abstain_unknown_robots",
            "abstain_unresolved_rate",
            "abstain_unknown_identity",
            "abstain_pending_review",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_prohibited_and_evasive_postures_are_denied(self) -> None:
        expected = {
            "deny_terms_prohibited": ["TERMS_AUTOMATION_PROHIBITED"],
            "deny_terms_restricted": ["TERMS_AUTOMATION_RESTRICTED"],
            "deny_robots_disallowed": ["ROBOTS_DISALLOWED"],
            "deny_disguised_user_agent": ["USER_AGENT_DISGUISED"],
            "deny_rotating_proxy": ["ROTATING_PROXY_EVASION"],
            "deny_unreviewed_distribution": ["DISTRIBUTED_ACQUISITION_UNREVIEWED"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_route_and_exception_support_fail_closed(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_scrape_without_robots_scope")).codes,
            ["ROUTE_ROBOTS_INCOHERENT"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_authorized_proxy_without_agreement")).codes,
            ["EXCEPTION_SUPPORT_INCOMPLETE"],
        )

    def test_profile_hash_binds_conduct_posture(self) -> None:
        candidate = self._candidate("pass_official_api")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["identity"]["proxy_posture"] = "ROTATING_EVASION"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_official_api")
        candidate["source_descriptor_ref"] = "kfm:source-descriptor:invalid\ud800"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["JSON_UNPAIRED_SURROGATE"])
        with self.assertRaises(MODULE.UnpairedSurrogateError):
            MODULE.compute_profile_hash(candidate)

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            _, findings = MODULE.load_json_object(duplicate)
            self.assertEqual([item.code for item in findings], ["JSON_DUPLICATE_KEY"])
            nonfinite = Path(directory) / "nonfinite.json"
            nonfinite.write_text('{"a":NaN}', encoding="utf-8")
            _, findings = MODULE.load_json_object(nonfinite)
            self.assertEqual([item.code for item in findings], ["JSON_NONFINITE_NUMBER"])

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network denied")
        ), mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
