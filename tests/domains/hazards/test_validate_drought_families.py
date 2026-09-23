#!/usr/bin/env python3
"""Negative-path proof for the drought-family validator CLI.

The committed fixture polarity is proven by ``test_hazards_smoke``. These
tests prove the CLI itself returns finite outcomes for malformed inputs and
refuses to pass a fixture suite whose negative lane is empty.
"""

from __future__ import annotations

import contextlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.validators.hazards import validate_drought_families as drought


def _quiet(func, *args, **kwargs):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return func(*args, **kwargs)


class DroughtFamiliesValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)

    def _write(self, name: str, text: str) -> Path:
        path = self.tmp / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_committed_fixture_suites_pass(self) -> None:
        self.assertEqual(0, _quiet(drought.main, ["--fixtures"]))

    def test_non_object_roots_are_finite_errors(self) -> None:
        for index, text in enumerate(("[]", "null", "1", '"DroughtObservation"')):
            with self.subTest(root=text):
                path = self._write(f"root_{index}.json", text)
                self.assertEqual("ERROR", _quiet(drought.validate_file, path))
                self.assertEqual(1, _quiet(drought.main, [str(path)]))

    def test_unhashable_or_unknown_object_type_is_denied(self) -> None:
        for index, value in enumerate(([], {}, 1, None, "DroughtWatch")):
            with self.subTest(object_type=value):
                path = self._write(f"type_{index}.json", json.dumps({"object_type": value}))
                self.assertEqual("DENY", _quiet(drought.validate_file, path))

    def test_malformed_json_is_finite_error(self) -> None:
        path = self._write("broken.json", '{"object_type": "DroughtObservation"')
        self.assertEqual("ERROR", _quiet(drought.validate_file, path))

    def test_empty_negative_lane_fails_suite(self) -> None:
        family = self.tmp / "family"
        (family / "valid").mkdir(parents=True)
        (family / "invalid").mkdir()
        shutil.copy(drought.OBS_FIXTURES / "valid" / "valid_1.json", family / "valid")
        self.assertFalse(_quiet(drought.run_fixtures, family, label="DroughtObservation"))

    def test_empty_positive_lane_fails_suite(self) -> None:
        family = self.tmp / "family"
        (family / "valid").mkdir(parents=True)
        (family / "invalid").mkdir()
        shutil.copy(
            drought.OBS_FIXTURES / "invalid" / "invalid_5_undeclared_fields.json",
            family / "invalid",
        )
        self.assertFalse(_quiet(drought.run_fixtures, family, label="DroughtObservation"))


if __name__ == "__main__":
    unittest.main()
