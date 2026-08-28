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
MODULE_PATH = ROOT / "tools/validators/validate_aggregate_grouping_disclosure.py"
SPEC = importlib.util.spec_from_file_location("aggregate_grouping_disclosure_validator", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AggregateGroupingDisclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(MODULE.FIXTURE_PATH.read_text(encoding="utf-8"))

    def _case(self, name: str) -> dict[str, object]:
        return next(entry for entry in self.manifest["cases"] if entry["name"] == name)

    def _candidate(self, name: str) -> dict[str, object]:
        return MODULE.materialize_fixture_case(self.manifest, self._case(name))

    def test_schema_is_valid_closed_value_free_and_inactive(self) -> None:
        schema = MODULE._load_schema()
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["x-kfm"]["status"], "PROPOSED_INACTIVE")
        self.assertFalse(schema["x-kfm"]["network"])
        self.assertFalse(schema["x-kfm"]["group_values_allowed"])
        self.assertNotIn("group_value", schema["properties"])

    def test_fixture_manifest_matches_exact_outcomes(self) -> None:
        results = MODULE.validate_fixture_manifest()
        self.assertEqual(len(results), 23)
        self.assertTrue(all(item["ok"] for item in results), results)

    def test_pass_cases_preserve_explicit_row_kinds_and_no_authority(self) -> None:
        for name in ("pass_rollup", "pass_cube", "pass_group_by"):
            candidate = self._candidate(name)
            self.assertEqual(MODULE.validate_candidate(candidate).outcome, "PASS")
            self.assertTrue(all(value is False for value in candidate["authority_claims"].values()))
        self.assertEqual(
            {row["row_kind"] for row in self._candidate("pass_rollup")["rows"]},
            {"DETAIL", "SUBTOTAL", "GRAND_TOTAL"},
        )

    def test_unresolved_declarations_abstain(self) -> None:
        for name in (
            "abstain_execution_incomplete",
            "abstain_method_unresolved",
            "abstain_output_unresolved",
            "abstain_engine_parity_unresolved",
            "abstain_group_values_unresolved",
        ):
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).outcome, "ABSTAIN")

    def test_dimension_mask_row_kind_and_rollup_rules_fail_closed(self) -> None:
        expected = {
            "deny_dimension_partition_incomplete": [
                "DIMENSION_PARTITION_INVALID",
                "ROLLUP_PREFIX_SEMANTICS_INVALID",
                "ROW_KIND_SEMANTICS_INVALID",
            ],
            "deny_grouping_mask_mismatch": ["GROUPING_MASK_MISMATCH"],
            "deny_detail_has_rollup": ["ROW_KIND_SEMANTICS_INVALID"],
            "deny_subtotal_empty_key": ["ROW_KIND_SEMANTICS_INVALID"],
            "deny_grand_total_not_all_rolled": ["ROW_KIND_SEMANTICS_INVALID"],
            "deny_rollup_nonprefix_subtotal": ["ROLLUP_PREFIX_SEMANTICS_INVALID"],
            "deny_source_null_overlaps_rollup": ["SOURCE_NULL_ROLE_INVALID"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_public_count_parity_order_and_identity_guards(self) -> None:
        expected = {
            "deny_public_label_incomplete": ["PUBLIC_LABEL_DISCLOSURE_INCOMPLETE"],
            "deny_public_reference_missing": ["PUBLIC_CANDIDATE_REFERENCE_MISSING"],
            "deny_output_row_count_mismatch": ["OUTPUT_ROW_COUNT_MISMATCH"],
            "deny_row_ordinal_sequence": ["ROW_ORDINAL_SEQUENCE_INVALID"],
            "deny_engine_parity_mismatch": ["ENGINE_PARITY_MISMATCH"],
            "deny_non_utc_timestamp": ["UTC_TIMESTAMP_REQUIRED"],
            "deny_profile_hash_tamper": ["PROFILE_SPEC_HASH_MISMATCH"],
        }
        for name, codes in expected.items():
            self.assertEqual(MODULE.validate_candidate(self._candidate(name)).codes, codes)

    def test_profile_hash_replays_and_binds_grouping_semantics(self) -> None:
        candidate = self._candidate("pass_rollup")
        self.assertEqual(candidate["profile_spec_hash"], MODULE.compute_profile_hash(candidate))
        changed = copy.deepcopy(candidate)
        changed["rows"][1]["grouping_mask"] = 1
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

    def test_fixture_replay_is_deterministic_and_no_network(self) -> None:
        with mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), mock.patch.object(
            socket, "socket", side_effect=AssertionError("network denied")
        ):
            first = MODULE.validate_fixture_manifest()
            second = MODULE.validate_fixture_manifest()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
