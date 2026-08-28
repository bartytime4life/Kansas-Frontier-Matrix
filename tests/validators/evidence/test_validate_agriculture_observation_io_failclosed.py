from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.evidence import validate_agriculture_observation as validator


class AgricultureObservationIoFailClosedTests(unittest.TestCase):
    def test_bounded_reader_fails_closed_on_metadata_and_read_oserror(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "candidate.json"
            candidate.write_text("{}", encoding="utf-8")

            with self.subTest(stage="metadata"):
                with mock.patch.object(Path, "stat", side_effect=OSError("metadata unavailable")):
                    value, findings = validator._read(candidate)
                self.assertIsNone(value)
                self.assertEqual(
                    (validator.Finding("AGRICULTURE_JSON_INVALID", "/"),),
                    findings,
                )

            with self.subTest(stage="read"):
                with mock.patch.object(Path, "read_text", side_effect=OSError("read denied")):
                    value, findings = validator._read(candidate)
                self.assertIsNone(value)
                self.assertEqual(
                    (validator.Finding("AGRICULTURE_JSON_INVALID", "/"),),
                    findings,
                )

    def test_bounded_reader_fails_closed_on_json_recursion_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory) / "candidate.json"
            candidate.write_text("{}", encoding="utf-8")

            with mock.patch.object(
                validator.json,
                "loads",
                side_effect=RecursionError("maximum JSON nesting exceeded"),
            ):
                value, findings = validator._read(candidate)

            self.assertIsNone(value)
            self.assertEqual(
                (validator.Finding("AGRICULTURE_JSON_INVALID", "/"),),
                findings,
            )


if __name__ == "__main__":
    unittest.main()
