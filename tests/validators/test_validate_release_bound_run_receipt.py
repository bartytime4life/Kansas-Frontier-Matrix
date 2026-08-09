from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/evidence/validate_release_bound_run_receipt.py"
SPEC = importlib.util.spec_from_file_location("release_bound_run_receipt_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ReleaseBoundRunReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(MODULE._load_schema())

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 10)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_valid_profile_hash_replays(self) -> None:
        candidate = self.manifest["cases"][0]["candidate"]
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))

    def test_profiles_are_deterministic(self) -> None:
        first = MODULE.validate_fixture_manifest()
        second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)

    def test_authority_overclaim_fails_closed(self) -> None:
        candidate = next(case["candidate"] for case in self.manifest["cases"] if case["name"] == "deny_authority_overclaim")
        self.assertEqual(MODULE.validate_candidate(candidate).outcome, "ERROR")

    def test_unverified_attestation_abstains(self) -> None:
        candidate = next(case["candidate"] for case in self.manifest["cases"] if case["name"] == "abstain_unverified_attestation")
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertEqual(result.codes, ["ATTESTATION_UNVERIFIED", "SIGNATURE_PENDING"])


if __name__ == "__main__":
    unittest.main()
