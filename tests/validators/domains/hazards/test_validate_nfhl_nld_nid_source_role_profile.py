"""Deterministic no-network tests for the NFHL/NLD/NID source-role profile."""
from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

from tools.validators.domains.hazards.validate_nfhl_nld_nid_source_role_profile import (
    FIXTURE_PATH,
    SCHEMA_PATH,
    load_fixture_cases,
    main as validate_main,
    run_fixture_suite,
    validate_document,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[4]


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("hazards source-role validation attempted network access")


class NfhlNldNidSourceRoleProfileTests(unittest.TestCase):
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
        self.path.write_text(
            json.dumps(value, indent=2) + "\n",
            encoding="utf-8",
        )
        return self.path

    def test_schema_is_valid_closed_and_fixture_only(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            schema["properties"]["status"]["const"],
            "PROPOSED_INACTIVE",
        )
        self.assertEqual(
            schema["properties"]["execution_mode"]["const"],
            "FIXTURE_ONLY",
        )
        self.assertEqual(
            set(schema["properties"]["sources"]["required"]),
            {"nfhl", "nld", "nid"},
        )

    def test_fixture_matrix_has_exact_polarity_and_findings(self) -> None:
        self.assertEqual(len(self.cases), 14)
        self.assertEqual(
            {
                outcome: sum(
                    case["expected_outcome"] == outcome
                    for case in self.cases
                )
                for outcome in ("PASS", "ABSTAIN", "DENY", "ERROR")
            },
            {"PASS": 2, "ABSTAIN": 2, "DENY": 10, "ERROR": 0},
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
        self.assertEqual(
            payload["counts"],
            {"PASS": 2, "ABSTAIN": 2, "DENY": 10, "ERROR": 0},
        )
        self.assertEqual(payload["authority"], "NONE")
        self.assertIn("no_live_source_access", payload["non_effects"])
        self.assertIn(
            "no_policy_review_promotion_release_or_publication",
            payload["non_effects"],
        )

    def test_source_roles_cannot_collapse_into_event_or_condition_truth(self) -> None:
        observed = validate_document(
            self._document("deny_observed_flood_claim")
        )
        self.assertEqual(observed.outcome, "DENY")
        self.assertIn(
            "NFHL_OBSERVED_FLOOD_COLLAPSE_DENIED",
            {finding.code for finding in observed.findings},
        )

        condition = validate_document(
            self._document("deny_nld_operational_condition_claim")
        )
        self.assertEqual(condition.outcome, "DENY")
        self.assertIn(
            "NLD_OPERATIONAL_CONDITION_DENIED",
            {finding.code for finding in condition.findings},
        )

    def test_sensitive_infrastructure_requires_public_safe_projection(self) -> None:
        exact = validate_document(
            self._document("deny_exact_operational_detail")
        )
        self.assertIn(
            "HAZARD_OPERATIONAL_DETAIL_DENIED",
            {finding.code for finding in exact.findings},
        )

        missing_transform = validate_document(
            self._document("deny_missing_generalization_receipt")
        )
        self.assertIn(
            "INFRASTRUCTURE_GENERALIZATION_REQUIRED",
            {finding.code for finding in missing_transform.findings},
        )

    def test_missing_support_abstains_instead_of_fabricating_empty_truth(self) -> None:
        no_data = validate_document(
            self._document("abstain_nid_no_data")
        )
        self.assertEqual(no_data.outcome, "ABSTAIN")
        self.assertEqual(
            [finding.code for finding in no_data.findings],
            ["NID_NO_DATA"],
        )

        unresolved = validate_document(
            self._document("abstain_relation_evidence_unresolved")
        )
        self.assertEqual(unresolved.outcome, "ABSTAIN")
        self.assertEqual(
            [finding.code for finding in unresolved.findings],
            ["HAZARD_RELATION_EVIDENCE_UNRESOLVED"],
        )

    def test_identity_time_and_relation_canonicalization_fail_closed(self) -> None:
        for case_id, code in (
            (
                "deny_identity_hash_drift",
                "HAZARD_SOURCE_ROLE_SPEC_HASH_MISMATCH",
            ),
            (
                "deny_source_time_order",
                "HAZARD_SOURCE_TIME_ORDER_INVALID",
            ),
            (
                "deny_native_identity_collision",
                "HAZARD_NATIVE_IDENTITY_COLLISION",
            ),
            (
                "deny_relation_order",
                "HAZARD_RELATIONS_NOT_CANONICAL",
            ),
        ):
            with self.subTest(case=case_id):
                result = validate_document(self._document(case_id))
                self.assertEqual(result.outcome, "DENY")
                self.assertIn(code, {item.code for item in result.findings})

    def test_validation_is_no_network_and_diagnostics_do_not_echo_values(self) -> None:
        candidate = self._document("valid_populated_sources")
        with (
            mock.patch.object(socket.socket, "connect", _unexpected_network),
            mock.patch.object(socket, "create_connection", _unexpected_network),
            mock.patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            self.assertEqual(validate_document(candidate).outcome, "PASS")

        marker = "synthetic-sensitive-marker-must-not-echo"
        candidate["sources"]["nfhl"]["evidence_refs"] = [marker]
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
        self.assertIn("HAZARD_SOURCE_ROLE_SCHEMA_INVALID", outputs[0])

    def test_bounded_loader_and_finite_cli_exit_codes(self) -> None:
        valid = self._write(
            self._document("valid_populated_sources")
        )
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validate_main([str(valid)]), 0)

        abstain = self._write(
            self._document("abstain_nid_no_data")
        )
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validate_main([str(abstain)]), 3)

        denied = self._write(
            self._document("deny_observed_flood_claim")
        )
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validate_main([str(denied)]), 1)

        self.path.write_text("{not-json}\n", encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(validate_main([str(self.path)]), 2)

        duplicate = (
            '{"profile":"x","profile":"y"}\n'
        )
        self.path.write_text(duplicate, encoding="utf-8")
        self.assertEqual(validate_file(self.path).outcome, "ERROR")

        oversized = self.root / "oversized.json"
        oversized.write_bytes(b" " * (2 * 1024 * 1024 + 1))
        self.assertEqual(validate_file(oversized).outcome, "ERROR")

        linked = self.root / "linked.json"
        linked.symlink_to(valid)
        self.assertEqual(validate_file(linked).outcome, "ERROR")


if __name__ == "__main__":
    unittest.main()
