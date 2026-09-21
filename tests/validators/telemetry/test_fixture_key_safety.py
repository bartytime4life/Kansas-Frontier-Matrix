"""Negative-path proof for the fixture-only telemetry JSON key guard."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.validators.telemetry.check_fixture_keys import FIXTURE_ROOT, scan_tree


class FixtureKeySafetyTests(unittest.TestCase):
    def test_admitted_fixture_profiles_have_no_named_prompt_or_coordinate_keys(self) -> None:
        self.assertEqual(scan_tree(FIXTURE_ROOT, "prompts"), ())
        self.assertEqual(scan_tree(FIXTURE_ROOT, "coordinates"), ())

    def test_nested_case_variant_is_rejected_without_reflecting_payload(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "case.json").write_text(
                '{"outer":[{"RAWpRoMpT":"PRIVATE_CANARY"},'
                '{"LONGITUDE":-98.3}]}',
                encoding="utf-8",
            )
            prompts = scan_tree(root, "prompts")
            coordinates = scan_tree(root, "coordinates")
        self.assertEqual([item.code for item in prompts], ["FORBIDDEN_KEY"])
        self.assertEqual([item.code for item in coordinates], ["FORBIDDEN_KEY"])
        self.assertNotIn("PRIVATE_CANARY", str(prompts))
        self.assertNotIn("RAWpRoMpT", str(prompts))

    def test_duplicate_keys_and_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "duplicate.json").write_text('{"a":1,"a":2}', encoding="utf-8")
            (root / "nonfinite.json").write_text('{"metric":NaN}', encoding="utf-8")
            findings = scan_tree(root, "coordinates")
        self.assertEqual(
            [(item.code, item.path) for item in findings],
            [
                ("JSON_DUPLICATE_KEY", "duplicate.json"),
                ("JSON_NONFINITE_NUMBER", "nonfinite.json"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
