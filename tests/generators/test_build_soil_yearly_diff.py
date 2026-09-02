from __future__ import annotations

import copy
import importlib.util
import io
import json
import socket
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/generators/build_soil_yearly_diff.py"
SPEC = importlib.util.spec_from_file_location("build_soil_yearly_diff", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

SNAPSHOTS = ROOT / "fixtures/domains/soil/yearly_diff/snapshots"
PREVIOUS = SNAPSHOTS / "ssurgo-2025.json"
CURRENT = SNAPSHOTS / "ssurgo-2026.json"


class SoilYearlyDiffBuilderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.previous = MODULE.read_manifest(PREVIOUS)
        self.current = MODULE.read_manifest(CURRENT)

    def test_build_is_deterministic_and_profile_valid(self) -> None:
        first = MODULE.build_result(self.previous, self.current)
        second = MODULE.build_result(self.previous, self.current)
        self.assertEqual(first, second)
        self.assertEqual(
            "PASS",
            MODULE.profile_validator.validate_payload(first["profile"]).outcome,
        )
        self.assertEqual(
            first["record_diff_sha256"],
            MODULE.compute_spec_hash(first["record_diff"]),
        )

    def test_record_delta_is_exact_and_canonical(self) -> None:
        result = MODULE.build_result(self.previous, self.current)
        detail = result["record_diff"]
        profile = result["profile"]
        self.assertEqual(["mapunit-004"], detail["added_record_keys"])
        self.assertEqual(["mapunit-002"], detail["removed_record_keys"])
        self.assertEqual(["mapunit-001"], [item["record_key"] for item in detail["modified_records"]])
        self.assertEqual(
            ["representative_slope_pct", "texture_class"],
            detail["changed_property_names"],
        )
        self.assertEqual(
            (1, 1, 1),
            (
                profile["diff"]["added_records"],
                profile["diff"]["removed_records"],
                profile["diff"]["modified_records"],
            ),
        )

    def test_nonconsecutive_years_fail_closed(self) -> None:
        current = copy.deepcopy(self.current)
        current["dataset_year"] = 2027
        with self.assertRaisesRegex(MODULE.BuildFailure, "YEAR_SEQUENCE_INVALID"):
            MODULE.build_result(self.previous, current)

    def test_source_role_collapse_fails_closed(self) -> None:
        current = copy.deepcopy(self.current)
        current["support_type"] = "GRIDDED_DERIVATIVE_SOIL"
        with self.assertRaisesRegex(MODULE.BuildFailure, "SOURCE_ROLE_INVALID"):
            MODULE.build_result(self.previous, current)

    def test_noncanonical_record_order_fails_closed(self) -> None:
        current = copy.deepcopy(self.current)
        current["records"] = list(reversed(current["records"]))
        with self.assertRaisesRegex(MODULE.BuildFailure, "RECORD_KEYS_NOT_CANONICAL"):
            MODULE.build_result(self.previous, current)

    def test_default_cli_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "result.json"
            stream = io.StringIO()
            with redirect_stdout(stream):
                code = MODULE.main([str(PREVIOUS), str(CURRENT)])
            self.assertEqual(0, code)
            self.assertFalse(output.exists())
            self.assertEqual("SoilYearlyDiffBuildResult", json.loads(stream.getvalue())["object_type"])

    def test_explicit_write_and_overwrite_guard(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "result.json"
            self.assertEqual(0, MODULE.main([str(PREVIOUS), str(CURRENT), "--write", str(output)]))
            first = output.read_bytes()
            self.assertEqual(2, MODULE.main([str(PREVIOUS), str(CURRENT), "--write", str(output)]))
            self.assertEqual(first, output.read_bytes())
            self.assertEqual(
                0,
                MODULE.main(
                    [str(PREVIOUS), str(CURRENT), "--write", str(output), "--force"]
                ),
            )
            self.assertEqual(first, output.read_bytes())

    def test_builder_does_not_open_network(self) -> None:
        def denied(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access denied")

        with mock.patch.object(socket, "socket", denied), mock.patch.object(
            socket, "create_connection", denied
        ), mock.patch.object(socket, "getaddrinfo", denied):
            result = MODULE.build_result(self.previous, self.current)
            self.assertTrue(all(value is False for value in result["governance"].values()))


if __name__ == "__main__":
    unittest.main()
