from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock


# Keep this focused helper suite runnable in the repository's no-network
# development profile. Hosted CI installs the declared jsonschema/referencing
# dependencies before importing the runner.
if importlib.util.find_spec("jsonschema") is None:
    jsonschema_stub = types.ModuleType("jsonschema")
    jsonschema_stub.Draft202012Validator = object
    sys.modules["jsonschema"] = jsonschema_stub

if importlib.util.find_spec("referencing") is None:
    referencing_stub = types.ModuleType("referencing")
    referencing_stub.Registry = object
    referencing_stub.Resource = object
    sys.modules["referencing"] = referencing_stub

from tools.validators._common import jsonschema_runner


_DEFAULT_FIXTURE_DIRECTORY = object()


class _SyntheticError:
    def __init__(self, message: str):
        self.message = message
        self.path = ()


class _SyntheticValidator:
    def iter_errors(self, instance):
        if instance.get("raise_error"):
            raise RuntimeError("synthetic validator failure")
        if instance.get("valid"):
            return []
        return [_SyntheticError("synthetic schema rejection")]


class JsonSchemaRunnerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.fixtures = self.root / "fixtures"
        (self.fixtures / "valid").mkdir(parents=True)
        (self.fixtures / "invalid").mkdir(parents=True)
        self.validator = _SyntheticValidator()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _write_json(self, lane: str, filename: str, payload: dict[str, bool]) -> Path:
        path = self.fixtures / lane / filename
        path.write_text(json.dumps(payload) + "\n", encoding="utf-8")
        return path

    def _run(self, argv, *, fixtures_dir=_DEFAULT_FIXTURE_DIRECTORY):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with (
            mock.patch.object(
                jsonschema_runner,
                "load_validator",
                return_value=self.validator,
            ),
            contextlib.redirect_stdout(stdout),
            contextlib.redirect_stderr(stderr),
        ):
            exit_code = jsonschema_runner.run(
                self.root / "synthetic.schema.json",
                self.fixtures
                if fixtures_dir is _DEFAULT_FIXTURE_DIRECTORY
                else fixtures_dir,
                argv,
            )
        return exit_code, stdout.getvalue(), stderr.getvalue()

    def test_fixture_mode_is_sorted_and_labels_expected_invalids(self) -> None:
        valid_z = self._write_json("valid", "z.json", {"valid": True})
        valid_a = self._write_json("valid", "a.json", {"valid": True})
        invalid_z = self._write_json("invalid", "z.json", {"valid": False})
        invalid_a = self._write_json("invalid", "a.json", {"valid": False})

        exit_code, stdout, stderr = self._run(["--fixtures"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, "")
        self.assertEqual(
            stdout.splitlines(),
            [
                f"OK {valid_a}",
                f"OK {valid_z}",
                f"EXPECTED_FAIL {invalid_a}: synthetic schema rejection",
                f"EXPECTED_FAIL {invalid_z}: synthetic schema rejection",
            ],
        )

    def test_fixture_mode_rejects_empty_valid_lane(self) -> None:
        self._write_json("invalid", "invalid.json", {"valid": False})

        exit_code, stdout, _ = self._run(["--fixtures"])

        self.assertEqual(exit_code, 1)
        self.assertIn(
            f"FAIL {self.fixtures / 'valid'}: no JSON fixtures found",
            stdout,
        )

    def test_fixture_mode_rejects_empty_invalid_lane(self) -> None:
        self._write_json("valid", "valid.json", {"valid": True})

        exit_code, stdout, _ = self._run(["--fixtures"])

        self.assertEqual(exit_code, 1)
        self.assertIn(
            f"FAIL {self.fixtures / 'invalid'}: no JSON fixtures found",
            stdout,
        )

    def test_fixture_mode_rejects_invalid_data_in_valid_lane(self) -> None:
        fixture = self._write_json("valid", "wrong.json", {"valid": False})
        self._write_json("invalid", "invalid.json", {"valid": False})

        exit_code, stdout, _ = self._run(["--fixtures"])

        self.assertEqual(exit_code, 1)
        self.assertIn(f"FAIL {fixture}: synthetic schema rejection", stdout)

    def test_fixture_mode_rejects_valid_data_in_invalid_lane(self) -> None:
        self._write_json("valid", "valid.json", {"valid": True})
        fixture = self._write_json("invalid", "wrong.json", {"valid": True})

        exit_code, stdout, _ = self._run(["--fixtures"])

        self.assertEqual(exit_code, 1)
        self.assertIn(f"FAIL {fixture}: expected schema rejection", stdout)

    def test_malformed_invalid_fixture_is_a_harness_failure(self) -> None:
        self._write_json("valid", "valid.json", {"valid": True})
        fixture = self.fixtures / "invalid" / "malformed.json"
        fixture.write_text("{not-json}\n", encoding="utf-8")

        exit_code, stdout, _ = self._run(["--fixtures"])

        self.assertEqual(exit_code, 1)
        self.assertIn(f"FAIL {fixture}:", stdout)
        self.assertNotIn(f"EXPECTED_FAIL {fixture}:", stdout)

    def test_validator_exception_is_contained(self) -> None:
        self._write_json("valid", "valid.json", {"valid": True})
        fixture = self._write_json("invalid", "error.json", {"raise_error": True})

        exit_code, stdout, _ = self._run(["--fixtures"])

        self.assertEqual(exit_code, 1)
        self.assertIn(f"FAIL {fixture}: synthetic validator failure", stdout)

    def test_explicit_mode_preserves_valid_and_invalid_exit_codes(self) -> None:
        valid = self.root / "valid.json"
        invalid = self.root / "invalid.json"
        valid.write_text('{"valid": true}\n', encoding="utf-8")
        invalid.write_text('{"valid": false}\n', encoding="utf-8")

        valid_result = self._run([str(valid)])
        invalid_result = self._run([str(invalid)])

        self.assertEqual(valid_result, (0, f"OK {valid}\n", ""))
        self.assertEqual(invalid_result[0], 1)
        self.assertEqual(
            invalid_result[1],
            f"FAIL {invalid}: synthetic schema rejection\n",
        )

    def test_no_input_returns_two_without_loading_schema(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with (
            mock.patch.object(
                jsonschema_runner,
                "load_validator",
                side_effect=AssertionError("schema load must not run"),
            ),
            contextlib.redirect_stdout(stdout),
            contextlib.redirect_stderr(stderr),
        ):
            exit_code = jsonschema_runner.run(
                self.root / "missing.schema.json",
                self.fixtures,
                [],
            )

        self.assertEqual(exit_code, 2)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "No files provided\n")

    def test_fixture_mode_requires_configured_directory(self) -> None:
        exit_code, stdout, _ = self._run(["--fixtures"], fixtures_dir=None)

        self.assertEqual(exit_code, 1)
        self.assertEqual(
            stdout,
            "FAIL fixture configuration: no fixture directory configured\n",
        )


if __name__ == "__main__":
    unittest.main()
