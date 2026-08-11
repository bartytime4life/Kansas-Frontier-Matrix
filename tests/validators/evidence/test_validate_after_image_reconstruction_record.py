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

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/evidence/validate_after_image_reconstruction_record.py"
SPEC = importlib.util.spec_from_file_location("validate_after_image_reconstruction_record", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AfterImageReconstructionRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))
        cls.cases = {entry["name"]: entry for entry in cls.manifest["cases"]}

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self.cases[name])

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), len(self.cases))
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_reference_modes_pass_without_payload_or_authority(self) -> None:
        for name in ("pass_external_bounded", "pass_minimized_reference", "pass_external_archival"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(candidate["after_image"]["inline_payload_present"])
            self.assertFalse(any(candidate["authority_claims"].values()))

    def test_nonreconstructable_after_image_modes_abstain(self) -> None:
        expected = {
            "abstain_digest_only": ["AFTER_IMAGE_DIGEST_ONLY"],
            "abstain_withheld": ["AFTER_IMAGE_WITHHELD"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "ABSTAIN")
            self.assertEqual(result.codes, codes)

    def test_unresolved_controls_abstain(self) -> None:
        expected = {
            "abstain_tracking_log_unresolved": ["TRACKING_LOG_UNRESOLVED"],
            "abstain_retention_policy_unresolved": ["RETENTION_POLICY_UNRESOLVED"],
            "abstain_minimization_unresolved": ["MINIMIZATION_UNRESOLVED"],
            "abstain_sensitivity_unresolved": ["SENSITIVITY_UNRESOLVED"],
            "abstain_review_pending": ["REVIEW_PENDING"],
            "abstain_review_unknown": ["REVIEW_UNKNOWN"],
        }
        for name, codes in expected.items():
            result = MODULE.validate_candidate(self._candidate(name))
            self.assertEqual(result.outcome, "ABSTAIN")
            self.assertEqual(result.codes, codes)

    def test_after_image_and_tracking_bindings_fail_closed(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_resolved_tracking_log_missing_digest")).codes,
            ["TRACKING_LOG_BINDING_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_external_reference_missing_ref")).codes,
            ["AFTER_IMAGE_BINDING_INCOHERENT"],
        )
        result = MODULE.validate_candidate(self._candidate("deny_withheld_missing_reason"))
        self.assertEqual(result.outcome, "DENY")
        self.assertEqual(
            result.codes,
            ["AFTER_IMAGE_BINDING_INCOHERENT", "AFTER_IMAGE_WITHHELD", "WITHHOLDING_REASON_REQUIRED"],
        )

    def test_reconstruction_use_cases_require_support(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_audit_without_run_receipt")).codes,
            ["RECONSTRUCTION_SUPPORT_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_disputed_release_without_as_of_snapshot")).codes,
            ["AS_OF_SNAPSHOT_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_noncanonical_use_cases")).codes,
            ["ARRAY_NOT_CANONICAL"],
        )

    def test_retention_and_minimization_fail_closed(self) -> None:
        expected = {
            "deny_minimized_without_applied_minimization": ["MINIMIZATION_REQUIRED"],
            "deny_bounded_without_expiry": ["RETENTION_EXPIRY_REQUIRED"],
            "deny_archival_with_expiry": ["RETENTION_EXPIRY_PROHIBITED"],
            "deny_expiry_not_future": ["RETENTION_EXPIRY_NOT_FUTURE"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_temporal_ordering_fails_closed(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_transaction_after_recorded_at")).codes,
            ["TRANSACTION_TIME_AFTER_RECORDED_AT"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_valid_time_order")).codes,
            ["VALID_TIME_ORDER_INVALID"],
        )

    def test_complete_review_requires_evidence_and_rationale(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_complete_without_review_ref")).codes,
            ["REVIEW_RECORD_REQUIRED"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_complete_without_rationale")).codes,
            ["RATIONALE_SUMMARY_REQUIRED"],
        )

    def test_profile_hash_binds_after_image_and_retention(self) -> None:
        candidate = self._candidate("pass_external_bounded")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["retention"]["class"] = "ARCHIVAL"
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_unpaired_surrogate_is_finite_error(self) -> None:
        candidate = self._candidate("pass_external_bounded")
        candidate["review"]["rationale_summary"] = "invalid \ud800 text"
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["JSON_UNPAIRED_SURROGATE"])
        with self.assertRaises(MODULE.UnpairedSurrogateError):
            MODULE.compute_profile_hash(candidate)

    def test_file_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            _, findings = MODULE.load_json_object(duplicate)
            self.assertEqual([item.code for item in findings], ["JSON_DUPLICATE_KEY"])
            nonfinite = root / "nonfinite.json"
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
