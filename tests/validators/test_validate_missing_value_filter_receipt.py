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

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/validators/validate_missing_value_filter_receipt.py"
SPEC = importlib.util.spec_from_file_location("missing_value_filter_receipt_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class MissingValueFilterReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(entry for entry in self.manifest["cases"] if entry["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_valid_closed_and_payload_free(self) -> None:
        schema = MODULE._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertFalse(schema["x-kfm"]["source_row_payloads"])
        self.assertNotIn("rows", schema["properties"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 17)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_fixtures_hold_for_review(self) -> None:
        for name in ("pass_single_filter_receipt", "pass_no_rows_excluded"):
            candidate = self._candidate(name)
            self.assertEqual(candidate["downstream_disposition"], "HOLD_FOR_REVIEW")
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")

    def test_unresolved_inputs_abstain(self) -> None:
        for name in (
            "abstain_analysis_scope_unresolved",
            "abstain_input_dataset_unresolved",
            "abstain_supporting_artifact_unresolved",
            "abstain_population_change_unresolved",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_filter_rule_and_count_failures_deny(self) -> None:
        expected = {
            "deny_filter_count_mismatch": ["FILTER_COUNT_MISMATCH"],
            "deny_filter_chain_start_mismatch": ["FILTER_CHAIN_MISMATCH"],
            "deny_missing_rule_empty": ["MISSING_RULE_EMPTY"],
            "deny_sentinel_tokens_not_canonical": ["SENTINEL_TOKENS_NOT_CANONICAL"],
            "deny_output_count_mismatch": ["OUTPUT_COUNT_MISMATCH"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_summary_pair_and_count_failures_deny(self) -> None:
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_summary_pair_incomplete")).codes,
            ["SUMMARY_PAIR_INCOMPLETE"],
        )
        self.assertEqual(
            MODULE.validate_candidate(self._candidate("deny_summary_row_count_mismatch")).codes,
            ["SUMMARY_ROW_COUNT_MISMATCH"],
        )

    def test_profile_hash_replays_and_binds_semantics(self) -> None:
        candidate = self._candidate("pass_single_filter_receipt")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["population_change_assessment"]["rationale"] = (
            "A materially different synthetic population-change rationale that must alter deterministic identity."
        )
        self.assertNotEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(changed))

    def test_input_loader_rejects_unsafe_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"a":1,"a":2}', encoding="utf-8")
            nonfinite = root / "nonfinite.json"
            nonfinite.write_text('{"a":Infinity}', encoding="utf-8")
            target = root / "target.json"
            target.write_text("{}", encoding="utf-8")
            link = root / "link.json"
            link.symlink_to(target)
            self.assertEqual(MODULE.load_json_object(duplicate)[1][0].code, "JSON_DUPLICATE_KEY")
            self.assertEqual(MODULE.load_json_object(nonfinite)[1][0].code, "JSON_NONFINITE_NUMBER")
            self.assertEqual(MODULE.load_json_object(link)[1][0].code, "INPUT_SYMLINK_DENIED")
            self.assertEqual(MODULE.load_json_object(root / "missing.json")[1][0].code, "FILE_NOT_FOUND")

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
