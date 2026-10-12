from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = (
    ROOT
    / "tools/validators/evidence/validate_temporal_coalescing_receipt.py"
)
SPEC = importlib.util.spec_from_file_location(
    "temporal_coalescing_receipt_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TemporalCoalescingReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(
            MODULE.FIXTURE_PATH.read_text(encoding="utf-8")
        )

    def _case(self, name: str) -> dict[str, object]:
        return next(
            entry for entry in self.manifest["cases"] if entry["name"] == name
        )

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(MODULE._load_schema())

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 11)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_valid_profile_hash_and_set_digests_replay(self) -> None:
        candidate = MODULE.materialize_fixture_case(
            self.manifest, self._case("pass_coalesce_adjacent_intervals")
        )
        self.assertEqual(
            candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate)
        )
        for name in ("input_set", "output_set"):
            interval_set = candidate[name]
            self.assertEqual(
                interval_set["digest"],
                MODULE.compute_interval_set_digest(interval_set),
            )

    def test_all_three_source_dispositions_are_accepted(self) -> None:
        for name in (
            "pass_coalesce_adjacent_intervals",
            "pass_split_interval",
            "pass_preserve_separate_intervals",
        ):
            candidate = MODULE.materialize_fixture_case(
                self.manifest, self._case(name)
            )
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")

    def test_method_resolution_abstains_without_changing_coverage(self) -> None:
        candidate = MODULE.materialize_fixture_case(
            self.manifest, self._case("abstain_unresolved_method")
        )
        result = MODULE.validate_candidate(candidate)
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertEqual(result.codes, ["METHOD_UNRESOLVED"])

    def test_coverage_loss_and_fact_key_collapse_fail_closed(self) -> None:
        coverage = MODULE.materialize_fixture_case(
            self.manifest, self._case("deny_coverage_gap")
        )
        collapse = MODULE.materialize_fixture_case(
            self.manifest, self._case("deny_fact_key_collapse")
        )
        self.assertEqual(
            MODULE.validate_candidate(coverage).codes, ["COVERAGE_MISMATCH"]
        )
        self.assertEqual(
            MODULE.validate_candidate(collapse).codes,
            ["COVERAGE_MISMATCH", "LINEAGE_FACT_KEY_MISMATCH"],
        )

    def test_fixture_replay_is_deterministic(self) -> None:
        self.assertEqual(
            MODULE.validate_fixture_manifest(), MODULE.validate_fixture_manifest()
        )


if __name__ == "__main__":
    unittest.main()
