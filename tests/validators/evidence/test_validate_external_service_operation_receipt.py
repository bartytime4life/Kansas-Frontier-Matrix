from __future__ import annotations

import copy
import importlib.util
import json
import socket
import sys
import unittest
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    ROOT
    / "tools/validators/evidence/validate_external_service_operation_receipt.py"
)
SPEC = importlib.util.spec_from_file_location(
    "external_service_operation_receipt_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
MANIFEST = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))


class ExternalServiceOperationReceiptTests(unittest.TestCase):
    """Prove the bounded receipt matrix and no-effect boundary."""
    @classmethod
    def setUpClass(cls) -> None:
        schema = json.loads(MODULE.SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def _candidate(self, name: str) -> dict[str, object]:
        entry = next(item for item in MANIFEST["cases"] if item["name"] == name)
        return MODULE.materialize_fixture_case(MANIFEST, entry)

    def test_exact_fixture_matrix(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 28)
        self.assertTrue(all(item["ok"] for item in results))

    def test_complete_profiles_pass_without_authority(self) -> None:
        for name in (
            "pass_measured_credits",
            "pass_estimated_cost",
            "pass_not_charged",
            "pass_exact_provider",
            "pass_governed_replacement",
            "pass_public_support",
        ):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertFalse(any(candidate["authority_claims"].values()))
            self.assertIsNone(candidate["disclosure"]["release_manifest_ref"])

    def test_incomplete_and_unresolved_profiles_abstain(self) -> None:
        for name in (
            "abstain_incomplete",
            "abstain_platform_unresolved",
            "abstain_service_version_unresolved",
            "abstain_consumption_unresolved",
            "abstain_replay_policy_unresolved",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "ABSTAIN",
            )

    def test_consumption_semantics_fail_closed(self) -> None:
        expected = {
            "deny_measured_without_value": [
                "MEASURED_CONSUMPTION_VALUE_REQUIRED"
            ],
            "deny_measured_without_measurement_ref": [
                "MEASUREMENT_REFERENCE_REQUIRED"
            ],
            "deny_estimated_without_pricing_ref": ["PRICING_REFERENCE_REQUIRED"],
            "deny_cost_currency_pair": ["COST_CURRENCY_PAIR_REQUIRED"],
            "deny_not_charged_with_amount": [
                "NOT_CHARGED_FIELDS_MUST_BE_EMPTY"
            ],
            "deny_unresolved_consumption_fields_present": [
                "UNRESOLVED_CONSUMPTION_FIELDS_PRESENT"
            ],
        }
        for name, codes in expected.items():
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).codes,
                codes,
            )

    def test_version_and_replay_semantics_fail_closed(self) -> None:
        for name in (
            "deny_replay_policy_missing",
            "deny_replacement_vendor_lock",
            "deny_unresolved_version_value_present",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "DENY",
            )

    def test_public_candidate_requires_cost_evidence_and_review_disclosure(
        self,
    ) -> None:
        expected = {
            "deny_public_missing_caveat": [
                "EXTERNAL_SERVICE_COST_CAVEAT_REQUIRED",
                "PUBLIC_COST_CAVEAT_REQUIRED",
            ],
            "deny_public_missing_evidence": [
                "PUBLIC_EVIDENCE_REFERENCE_REQUIRED"
            ],
            "deny_public_missing_review": ["PUBLIC_REVIEW_REFERENCE_REQUIRED"],
        }
        for name, codes in expected.items():
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).codes,
                codes,
            )

    def test_hash_and_receipt_identity_bind_operation_semantics(self) -> None:
        candidate = self._candidate("pass_measured_credits")
        profile_hash = MODULE.compute_profile_hash(candidate)
        self.assertEqual(candidate["profile_spec_hash"], profile_hash)
        self.assertEqual(
            candidate["receipt_ref"],
            MODULE.expected_receipt_ref(profile_hash),
        )
        changed = copy.deepcopy(candidate)
        changed["consumption"]["credit_quantity"] = "12.6"
        self.assertNotEqual(profile_hash, MODULE.compute_profile_hash(changed))

    def test_profile_carries_no_credentials_payloads_or_billing_records(self) -> None:
        candidate = self._candidate("pass_measured_credits")
        self.assertNotIn("credential", candidate)
        self.assertNotIn("request_payload", candidate["operation"])
        self.assertNotIn("response_payload", candidate["operation"])
        self.assertNotIn("billing_record", candidate["consumption"])

    def test_error_and_schema_paths_are_finite(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("error_operation")).outcome,
            "ERROR",
        )
        self.assertEqual(
            MODULE.validate_candidate(
                self._candidate("error_schema_unknown_field")
            ).codes,
            ["SCHEMA_INVALID"],
        )

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network denied"),
        ), mock.patch.object(
            socket,
            "socket",
            side_effect=AssertionError("network denied"),
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
