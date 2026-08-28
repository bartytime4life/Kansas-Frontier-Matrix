"""Deterministic no-network tests for the environmental indicator EvidenceBundle profile."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import os
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.validate_environmental_indicator_evidence_bundle_profile import (
    FIXTURE_PATH,
    SCHEMA_PATH,
    main as validate_main,
    load_fixture_cases,
    run_fixture_suite,
    validate_document,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[2]


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("environmental evidence validation attempted network access")


class EnvironmentalIndicatorEvidenceBundleProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cases, findings = load_fixture_cases()
        if findings:
            raise AssertionError(findings)
        cls.by_id = {case["case_id"]: case for case in cls.cases}

    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.path = self.root / "candidate.json"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _document(self, case_id: str) -> dict[str, object]:
        return copy.deepcopy(self.by_id[case_id]["document"])

    def _write(self, value: object) -> Path:
        self.path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        return self.path

    def test_profile_schema_is_valid_closed_and_reuses_evidence_bundle(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(
            schema["$defs"]["environmental_indicator"]["additionalProperties"]
        )
        self.assertEqual(
            schema["properties"]["bundle"]["$ref"],
            "https://schemas.kfm.local/contracts/v1/evidence/evidence_bundle.schema.json",
        )
        self.assertEqual(
            schema["properties"]["status"]["const"],
            "PROPOSED_INACTIVE",
        )
        self.assertEqual(
            schema["properties"]["execution_mode"]["const"],
            "FIXTURE_ONLY",
        )

    def test_fixture_matrix_has_exact_polarity_and_findings(self) -> None:
        self.assertEqual(len(self.cases), 14)
        self.assertEqual(
            sum(case["expected_outcome"] == "PASS" for case in self.cases),
            3,
        )
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                result = validate_document(case["document"])
                actual = [
                    {"code": finding.code, "path": finding.path}
                    for finding in result.findings
                ]
                self.assertEqual(result.outcome, case["expected_outcome"])
                self.assertEqual(actual, case["expected_findings"])

    def test_fixture_runner_passes_without_authority(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload["outcome"], "PASS")
        self.assertEqual(payload["cases"], 14)
        self.assertEqual(payload["counts"], {"PASS": 3, "DENY": 11, "ERROR": 0})
        self.assertEqual(payload["authority"], "NONE")
        self.assertIn("no_live_source_access", payload["non_effects"])
        self.assertIn(
            "no_promotion_release_deployment_or_publication",
            payload["non_effects"],
        )

    def test_existing_evidence_bundle_contract_is_a_hard_dependency(self) -> None:
        candidate = self._document("valid_populated_county_indicator")
        candidate["bundle"]["evidence_refs"] = []
        result = validate_document(candidate)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            "ENV_PROFILE_SCHEMA_INVALID",
            {finding.code for finding in result.findings},
        )

    def test_identity_and_hash_bindings_fail_closed(self) -> None:
        candidate = self._document("valid_populated_county_indicator")
        candidate["environmental_indicator"]["method"] = (
            "synthetic_changed_method_without_hash_rebinding"
        )
        result = validate_document(candidate)
        codes = {finding.code for finding in result.findings}
        self.assertEqual(result.outcome, "DENY")
        self.assertIn("INDICATOR_SPEC_HASH_MISMATCH", codes)
        self.assertIn("ANALYSIS_ID_MISMATCH", codes)
        self.assertIn("BUNDLE_INDICATOR_CHECKSUM_MISMATCH", codes)
        self.assertIn("CLAIM_SCOPE_BINDING_INVALID", codes)

        threshold_candidate = self._document("valid_populated_county_indicator")
        threshold_candidate["environmental_indicator"]["threshold_profile"][
            "version"
        ] = "1.0.1"
        threshold_result = validate_document(threshold_candidate)
        self.assertIn(
            "THRESHOLD_PROFILE_HASH_MISMATCH",
            {finding.code for finding in threshold_result.findings},
        )

    def test_empty_and_no_data_states_are_explicit(self) -> None:
        for case_id in ("valid_empty_period", "valid_no_data_period"):
            candidate = self._document(case_id)
            result = validate_document(candidate)
            self.assertEqual(result.outcome, "PASS", result.findings)
            self.assertEqual(candidate["environmental_indicator"]["county_fips"], [])
            self.assertEqual(candidate["environmental_indicator"]["ranked_rows"], [])
            self.assertEqual(
                candidate["environmental_indicator"]["cluster_summary"],
                {"cluster_count": 0, "clusters": []},
            )

        invalid = self._document("valid_empty_period")
        invalid["environmental_indicator"]["county_fips"] = ["20001"]
        result = validate_document(invalid)
        self.assertEqual(result.outcome, "DENY")
        self.assertIn(
            "DATA_STATE_CONTENT_INVALID",
            {finding.code for finding in result.findings},
        )

    def test_reference_and_cluster_closure_fail_closed(self) -> None:
        unresolved = validate_document(
            self._document("invalid_ranked_evidence_ref")
        )
        self.assertIn(
            "EVIDENCE_REF_UNRESOLVED",
            {finding.code for finding in unresolved.findings},
        )

        outside_scope = validate_document(
            self._document("invalid_cluster_county_scope")
        )
        self.assertIn(
            "CLUSTER_COUNTY_SCOPE_INVALID",
            {finding.code for finding in outside_scope.findings},
        )

        wrong_count = validate_document(self._document("invalid_cluster_count"))
        self.assertIn(
            "CLUSTER_COUNT_MISMATCH",
            {finding.code for finding in wrong_count.findings},
        )

    def test_validation_is_no_network_and_diagnostics_do_not_echo_values(self) -> None:
        candidate = self._document("valid_populated_county_indicator")
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            self.assertEqual(validate_document(candidate).outcome, "PASS")

        marker = "synthetic-untrusted-method-marker-that-must-not-echo"
        candidate["environmental_indicator"]["method"] = marker
        path = self._write(candidate)
        outputs: list[str] = []
        for _ in range(2):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                code = validate_main([str(path)])
            self.assertEqual(code, 1)
            outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertNotIn(marker, outputs[0])
        self.assertIn("INDICATOR_SPEC_HASH_MISMATCH", outputs[0])

    def test_bounded_loader_rejects_unsafe_json_inputs(self) -> None:
        valid = self._document("valid_populated_county_indicator")
        text = json.dumps(valid, indent=2)
        duplicate = text.replace(
            '  "profile": "kfm.environmental_indicator_evidence_bundle_profile.v1",',
            '  "profile": "kfm.environmental_indicator_evidence_bundle_profile.v1",\n'
            '  "profile": "kfm.environmental_indicator_evidence_bundle_profile.v1",',
            1,
        )
        self.path.write_text(duplicate, encoding="utf-8")
        self.assertEqual(validate_file(self.path).outcome, "ERROR")

        self.path.write_text('{"value": NaN}\n', encoding="utf-8")
        self.assertEqual(validate_file(self.path).outcome, "ERROR")

        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * 1_000_001)
        self.assertEqual(validate_file(oversized).outcome, "ERROR")

        target = self._write(valid)
        linked = self.root / "linked.json"
        linked.symlink_to(target)
        self.assertEqual(validate_file(linked).outcome, "ERROR")

    def test_cli_uses_finite_exit_codes(self) -> None:
        valid = self._write(
            self._document("valid_populated_county_indicator")
        )
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validate_main([str(valid)]), 0)

        denied = self._write(self._document("invalid_analysis_id"))
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validate_main([str(denied)]), 1)

        self.path.write_text("{not-json}\n", encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validate_main([str(self.path)]), 2)


if __name__ == "__main__":
    unittest.main()
