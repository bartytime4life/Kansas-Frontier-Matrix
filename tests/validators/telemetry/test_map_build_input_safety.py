"""Synthetic input-boundary regressions; no live telemetry or network access."""

from __future__ import annotations

import builtins
import contextlib
import copy
import importlib.util
import io
import json
import os
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "tools/validators/telemetry/validate_map_build_sustainability.py"
SPEC = importlib.util.spec_from_file_location("kfm_map_build_input_safety", MODULE_PATH)
if SPEC is None or SPEC.loader is None:  # pragma: no cover
    raise RuntimeError("map-build input validator could not be loaded")
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)


def _deny_network(*_args, **_kwargs):
    raise AssertionError("network access is forbidden in input-boundary tests")


class MapBuildInputSafetyTests(unittest.TestCase):
    def setUp(self) -> None:
        for target in ("create_connection", "getaddrinfo"):
            patch = mock.patch.object(socket, target, _deny_network)
            patch.start()
            self.addCleanup(patch.stop)
        patch = mock.patch.object(socket.socket, "connect", _deny_network)
        patch.start()
        self.addCleanup(patch.stop)
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.path = self.root / "input.json"
        self.base_case = {
            "case_id": "valid_case",
            "candidate": {},
            "expected": {"outcome": "PASS", "finding_codes": []},
        }

    def assert_input_error(self) -> None:
        value, findings = validator.load_json(self.path)
        self.assertIsNone(value)
        self.assertEqual(["JSON_INPUT_INVALID"], [item.code for item in findings])

    def assert_fixture_error(self, cases: object) -> None:
        self.path.write_text(
            json.dumps({"profile": validator.PROFILE, "cases": cases}),
            encoding="utf-8",
        )
        ok, report = validator.run_fixture_suite(self.path)
        self.assertFalse(ok)
        self.assertEqual("ERROR", report["outcome"])
        self.assertEqual(["FIXTURE_SUITE_INVALID"], report["findings"])
        self.assertEqual([], report["cases"])
        self.assertEqual("NONE", report["authority"])

    def test_nonstring_outcomes_return_finite_error(self) -> None:
        for outcome in ([], {}, ["PASS"], None, True, 1):
            with self.subTest(outcome=outcome):
                case = copy.deepcopy(self.base_case)
                case["expected"]["outcome"] = outcome
                self.assert_fixture_error([case])

    def test_malformed_finding_codes_return_finite_error(self) -> None:
        for codes in ([{}], [[]], ["SCHEMA_INVALID", 1], [None], [True]):
            with self.subTest(codes=codes):
                case = copy.deepcopy(self.base_case)
                case["expected"]["finding_codes"] = codes
                self.assert_fixture_error([case])

    def test_unsorted_duplicate_and_nonlist_codes_remain_denied(self) -> None:
        for codes in (["B", "A"], ["A", "A"], "A", None):
            with self.subTest(codes=codes):
                case = copy.deepcopy(self.base_case)
                case["expected"]["finding_codes"] = codes
                self.assert_fixture_error([case])

    def test_malformed_source_references_return_finite_error(self) -> None:
        for source in ([], {}, ["valid_case"], None, True, 1, "unknown_case"):
            with self.subTest(source=source):
                derived = {
                    "case_id": "derived_case",
                    "candidate_from": source,
                    "patch": {"value": 1},
                    "expected": {"outcome": "PASS", "finding_codes": []},
                }
                self.assert_fixture_error([self.base_case, derived])

    def test_materialization_preserves_valid_derived_case_and_input(self) -> None:
        cases = [copy.deepcopy(self.base_case), {
            "case_id": "derived_case",
            "candidate_from": "valid_case",
            "patch": {"value": 1},
            "expected": {"outcome": "DENY", "finding_codes": ["SCHEMA_INVALID"]},
        }]
        before = copy.deepcopy(cases)
        result = validator._materialize_cases(cases)
        self.assertEqual({}, result[0]["candidate"])
        self.assertEqual({"value": 1}, result[1]["candidate"])
        self.assertEqual(before, cases)

    def test_regular_utf8_json_is_read(self) -> None:
        self.path.write_text('{"label":"prairie \u00e9"}', encoding="utf-8")
        value, findings = validator.load_json(self.path)
        self.assertEqual({"label": "prairie \u00e9"}, value)
        self.assertEqual((), findings)

    def test_exact_byte_limit_is_accepted(self) -> None:
        self.path.write_bytes(b"{}" + b" " * 30)
        with mock.patch.object(validator, "MAX_JSON_BYTES", 32):
            self.assertEqual(({}, ()), validator.load_json(self.path))

    def test_limit_plus_one_and_multibyte_overflow_are_denied(self) -> None:
        with mock.patch.object(validator, "MAX_JSON_BYTES", 32):
            for content in (b"{}" + b" " * 31, ('"' + "\u00e9" * 16 + '"').encode()):
                with self.subTest(size=len(content)):
                    self.path.write_bytes(content)
                    self.assert_input_error()

    def test_invalid_utf8_missing_and_directory_inputs_are_denied(self) -> None:
        self.assert_input_error()
        self.path.mkdir()
        self.assert_input_error()
        self.path.rmdir()
        self.path.write_bytes(b'"\xff"')
        self.assert_input_error()

    def test_duplicate_and_nonfinite_inputs_keep_existing_codes(self) -> None:
        for content, code in (
            ('{"a":1,"a":2}', "JSON_DUPLICATE_KEY"),
            ('{"a":NaN}', "JSON_INPUT_INVALID"),
            ('{"a":1e999}', "JSON_INPUT_INVALID"),
            ('{"a":"\\ud800"}', "JSON_UNPAIRED_SURROGATE"),
        ):
            with self.subTest(code=code, content=content):
                self.path.write_text(content, encoding="utf-8")
                self.assertEqual([code], [item.code for item in validator.load_json(self.path)[1]])

    @unittest.skipUnless(hasattr(os, "O_NOFOLLOW") and hasattr(os, "O_NONBLOCK"), "POSIX file admission")
    def test_symlink_is_rejected(self) -> None:
        target = self.root / "target.json"
        target.write_text("{}", encoding="utf-8")
        self.path.symlink_to(target)
        self.assert_input_error()

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO fixture requires POSIX")
    def test_fifo_is_rejected_before_open(self) -> None:
        os.mkfifo(self.path)
        with mock.patch.object(os, "open", side_effect=AssertionError("must reject FIFO before open")):
            self.assert_input_error()

    @unittest.skipUnless(hasattr(os, "O_NOFOLLOW"), "POSIX no-follow open")
    def test_symlink_substitution_at_open_is_denied(self) -> None:
        self.path.write_text("{}", encoding="utf-8")
        target = self.root / "replacement.json"
        target.write_text('{"replacement":true}', encoding="utf-8")
        real_open = os.open

        def substitute(path, flags):
            self.assertTrue(flags & os.O_NOFOLLOW)
            self.assertTrue(flags & os.O_NONBLOCK)
            self.path.unlink()
            self.path.symlink_to(target)
            return real_open(path, flags)

        with mock.patch.object(os, "open", side_effect=substitute):
            self.assert_input_error()

    def test_regular_file_substitution_before_read_is_denied(self) -> None:
        self.path.write_text("{}", encoding="utf-8")
        target = self.root / "replacement.json"
        target.write_text("[]", encoding="utf-8")
        real_open = os.open
        opened = []

        def substitute(path, flags):
            os.replace(target, self.path)
            descriptor = real_open(path, flags)
            opened.append(descriptor)
            return descriptor

        with mock.patch.object(os, "open", side_effect=substitute):
            self.assert_input_error()
        self.assertEqual(1, len(opened))
        with self.assertRaises(OSError):
            os.fstat(opened[0])

    def test_growth_during_read_is_bounded_and_descriptor_is_closed(self) -> None:
        self.path.write_bytes(b"{}")
        requested = []
        opened = []

        @contextlib.contextmanager
        def intercept(descriptor, mode, *, closefd):
            opened.append(descriptor)
            self.path.write_bytes(b"{}" + b" " * 100)
            with builtins.open(descriptor, mode, closefd=closefd) as stream:
                class Proxy:
                    def read(self, limit):
                        requested.append(limit)
                        return stream.read(limit)
                yield Proxy()

        with mock.patch.object(validator, "MAX_JSON_BYTES", 32):
            with mock.patch.object(validator, "open", intercept, create=True):
                self.assert_input_error()
        self.assertEqual([33], requested)
        with self.assertRaises(OSError):
            os.fstat(opened[0])

    def test_same_size_modification_during_read_is_denied(self) -> None:
        self.path.write_text("{}", encoding="utf-8")
        before = self.path.stat()

        @contextlib.contextmanager
        def intercept(descriptor, mode, *, closefd):
            self.path.write_text("[]", encoding="utf-8")
            # A deterministic metadata change avoids clock-resolution races.
            os.utime(self.path, ns=(before.st_atime_ns, before.st_mtime_ns + 1_000_000_000))
            with builtins.open(descriptor, mode, closefd=closefd) as stream:
                yield stream

        with mock.patch.object(validator, "open", intercept, create=True):
            self.assert_input_error()

    def test_path_replacement_after_open_is_denied(self) -> None:
        self.path.write_text("{}", encoding="utf-8")
        target = self.root / "replacement.json"
        target.write_text("{}", encoding="utf-8")

        @contextlib.contextmanager
        def intercept(descriptor, mode, *, closefd):
            os.replace(target, self.path)
            with builtins.open(descriptor, mode, closefd=closefd) as stream:
                yield stream

        with mock.patch.object(validator, "open", intercept, create=True):
            self.assert_input_error()

    def test_missing_safe_open_capability_fails_closed(self) -> None:
        self.path.write_text("{}", encoding="utf-8")
        if not hasattr(os, "O_NOFOLLOW"):
            self.assert_input_error()
            return
        capability = os.O_NOFOLLOW
        del os.O_NOFOLLOW
        try:
            self.assert_input_error()
        finally:
            os.O_NOFOLLOW = capability

    def test_workflow_runs_current_tests_and_pins_only_historical_receipt(self) -> None:
        workflow = (ROOT / ".github/workflows/map-build-sustainability-telemetry.yml").read_text(encoding="utf-8")
        self.assertEqual(2, workflow.count('"tests/validators/telemetry/test_map_build_input_safety.py"'))
        self.assertIn("--pattern 'test_map_build*.py'", workflow)
        self.assertIn("fetch-depth: 0", workflow)
        self.assertIn("--artifact-git-ref 25a58f324e6ada808714aecdf9e745d139e1b3bc", workflow)
        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertIn("persist-credentials: false", workflow)
        self.assertNotIn("pull_request_target:", workflow)
        self.assertNotIn("secrets.", workflow)

    def test_cli_invalid_input_is_deterministic_and_does_not_echo(self) -> None:
        sentinel = "PRIVATE_INPUT_SENTINEL"
        self.path.write_text('{"secret":"' + sentinel, encoding="utf-8")
        outputs = []
        for _ in range(2):
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                self.assertEqual(1, validator.main(["--candidate", str(self.path)]))
            outputs.append(out.getvalue())
            self.assertEqual("", err.getvalue())
            self.assertNotIn(sentinel, out.getvalue())
            self.assertNotIn(str(self.path), out.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        self.assertEqual("ERROR", json.loads(outputs[0])["outcome"])


if __name__ == "__main__":
    unittest.main()
