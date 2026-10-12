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
    / "tools/validators/runtime/validate_database_mutation_transaction_receipt.py"
)
SPEC = importlib.util.spec_from_file_location(
    "database_mutation_transaction_receipt_validator", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class DatabaseMutationTransactionReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(
            MODULE.FIXTURE_PATH.read_text(encoding="utf-8")
        )

    def _case(self, name: str) -> dict[str, object]:
        return next(
            entry for entry in self.manifest["cases"] if entry["name"] == name
        )

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(
            self.manifest, self._case(name)
        )

    def test_schema_is_valid_draft_2020_12(self) -> None:
        Draft202012Validator.check_schema(MODULE._load_schema())

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 17)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_profile_and_embedded_run_hashes_replay(self) -> None:
        candidate = self._candidate("pass_committed_apply")
        self.assertEqual(
            candidate["run_receipt_digest"],
            MODULE.compute_run_receipt_digest(candidate),
        )
        self.assertEqual(
            candidate["profile_spec_hash"],
            MODULE.compute_profile_hash(candidate),
        )

    def test_finite_resolved_outcomes_pass(self) -> None:
        for name in (
            "pass_committed_apply",
            "pass_rollback_rehearsal",
            "pass_failed_before_commit",
        ):
            self.assertEqual(
                MODULE.validate_candidate(self._candidate(name)).outcome,
                "PASS",
            )

    def test_unknown_effect_or_recovery_abstains(self) -> None:
        indeterminate = MODULE.validate_candidate(
            self._candidate("abstain_indeterminate_transaction")
        )
        unresolved = MODULE.validate_candidate(
            self._candidate("abstain_unresolved_recovery_target")
        )
        self.assertEqual(indeterminate.outcome, "ABSTAIN")
        self.assertEqual(
            indeterminate.codes, ["TRANSACTION_OUTCOME_INDETERMINATE"]
        )
        self.assertEqual(unresolved.outcome, "ABSTAIN")
        self.assertEqual(unresolved.codes, ["RECOVERY_TARGET_UNRESOLVED"])

    def test_count_and_outcome_mismatches_fail_closed(self) -> None:
        affected = MODULE.validate_candidate(
            self._candidate("deny_affected_rows_exceed_attempted")
        )
        run_outcome = MODULE.validate_candidate(
            self._candidate("deny_run_outcome_mismatch")
        )
        self.assertEqual(
            affected.codes, ["AFFECTED_ROWS_EXCEED_ATTEMPTED"]
        )
        self.assertEqual(run_outcome.codes, ["RUN_OUTCOME_MISMATCH"])

    def test_read_only_operation_is_outside_profile(self) -> None:
        result = MODULE.validate_candidate(
            self._candidate("error_read_only_operation_excluded")
        )
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.codes, ["SCHEMA_INVALID"])

    def test_fixture_replay_is_deterministic(self) -> None:
        self.assertEqual(
            MODULE.validate_fixture_manifest(), MODULE.validate_fixture_manifest()
        )


if __name__ == "__main__":
    unittest.main()
