#!/usr/bin/env python3
"""Deterministic tests for the fixture-only CDL material-change watcher."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import socket
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(REPO_ROOT))

from tools.ingest.cdl_watch.cdl_watch import (  # noqa: E402
    MAX_AREA_M2,
    PROFILE_ID,
    SAFE_EXIT_OUTCOMES,
    compare_sidecars,
    compute_profile_hash,
    load_sidecar,
    main,
    serialize_report,
    validate_sidecar,
    write_report,
)
from tools.validators._common.public_safe_fixture import (  # noqa: E402
    MAX_FIXTURE_BYTES,
    Finding,
)


FIXTURE_ROOT = Path(__file__).with_name("fixtures")
CASE_OUTCOMES = {
    "absolute_threshold": "PROPOSED_WORK_RECORD",
    "below_threshold": "NO_MATERIAL_CHANGE",
    "classmap_drift": "CLASSMAP_DRIFT",
    "geometry_drift": "GEOMETRY_DRIFT",
    "metadata_change": "NO_MATERIAL_CHANGE",
    "no_material_change": "NO_MATERIAL_CHANGE",
    "relative_threshold": "PROPOSED_WORK_RECORD",
}


def _case_paths(case: str) -> tuple[Path, Path]:
    root = FIXTURE_ROOT / case
    return root / "prior_sidecar.json", root / "current_sidecar.json"


def _load_candidate(
    case: str = "no_material_change", which: str = "prior"
) -> dict[str, object]:
    prior, current = _case_paths(case)
    path = prior if which == "prior" else current
    return json.loads(path.read_text(encoding="utf-8"))


def _write_candidate(path: Path, candidate: dict[str, object]) -> None:
    candidate["profile_hash"] = compute_profile_hash(candidate)
    path.write_text(
        json.dumps(candidate, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )


class CdlWatchTests(unittest.TestCase):
    def setUp(self) -> None:
        denied = RuntimeError("network access is forbidden in CDL watcher tests")
        self.network_mocks: list[mock.Mock] = []
        for patcher in (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
            mock.patch.object(socket.socket, "connect_ex", side_effect=denied),
            mock.patch.object(socket, "create_connection", side_effect=denied),
            mock.patch.object(socket, "getaddrinfo", side_effect=denied),
            mock.patch.object(urllib.request, "urlopen", side_effect=denied),
        ):
            self.network_mocks.append(patcher.start())
            self.addCleanup(patcher.stop)

    def test_fixture_inventory_and_exact_outcomes(self) -> None:
        self.assertEqual(
            {path.name for path in FIXTURE_ROOT.iterdir() if path.is_dir()},
            set(CASE_OUTCOMES),
        )
        for case, expected in sorted(CASE_OUTCOMES.items()):
            prior, current = _case_paths(case)
            with self.subTest(case=case):
                self.assertEqual(load_sidecar(prior).findings, ())
                self.assertEqual(load_sidecar(current).findings, ())
                report = compare_sidecars(prior, current)
                self.assertEqual(report["status"], expected)
                self.assertEqual(report["decision"]["outcome"], expected)
                self.assertFalse(report["decision"]["publication"])
                self.assertTrue(report["decision"]["promotion_required"])

    def test_no_change_excludes_observation_time_from_profile_hash(self) -> None:
        prior, current = _case_paths("no_material_change")
        prior_candidate = json.loads(prior.read_text(encoding="utf-8"))
        current_candidate = json.loads(current.read_text(encoding="utf-8"))
        self.assertNotEqual(
            prior_candidate["observed_at"], current_candidate["observed_at"]
        )
        self.assertEqual(prior_candidate["profile_hash"], current_candidate["profile_hash"])
        self.assertEqual(
            compute_profile_hash(prior_candidate), prior_candidate["profile_hash"]
        )
        self.assertEqual(
            compute_profile_hash(current_candidate), current_candidate["profile_hash"]
        )

    def test_metadata_and_year_drift_are_diagnostics_without_crop_change(self) -> None:
        report = compare_sidecars(*_case_paths("metadata_change"))
        self.assertEqual(report["status"], "NO_MATERIAL_CHANGE")
        self.assertEqual(report["checks"]["metadata_drift"], "changed")
        self.assertEqual(report["checks"]["histogram_drift"], "same")
        self.assertEqual(report["decision"]["reason_codes"], [])

        prior = _load_candidate()
        current = copy.deepcopy(prior)
        current["cdl_year"] = 2026
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prior_path = root / "prior.json"
            current_path = root / "current.json"
            _write_candidate(prior_path, prior)
            _write_candidate(current_path, current)
            report = compare_sidecars(prior_path, current_path)
        self.assertEqual(report["status"], "NO_MATERIAL_CHANGE")
        self.assertEqual(report["checks"]["cdl_year"], "advanced")
        self.assertEqual(report["checks"]["histogram_drift"], "same")
        self.assertEqual(report["decision"]["reason_codes"], [])

    def test_below_threshold_change_is_not_promoted_to_material(self) -> None:
        report = compare_sidecars(*_case_paths("below_threshold"))
        self.assertEqual(report["status"], "NO_MATERIAL_CHANGE")
        self.assertEqual(report["checks"]["histogram_drift"], "below_threshold")
        self.assertEqual(report["checks"]["maximum_class_change_m2"], 1_999_999)
        self.assertEqual(report["decision"]["reason_codes"], [])

    def test_relative_boundary_is_inclusive(self) -> None:
        report = compare_sidecars(*_case_paths("relative_threshold"))
        self.assertEqual(report["checks"]["maximum_class_change_m2"], 2_000_000)
        self.assertIn(
            "CDL_HISTOGRAM_RELATIVE_THRESHOLD_REACHED",
            report["decision"]["reason_codes"],
        )

    def test_absolute_boundary_is_inclusive_and_independent(self) -> None:
        report = compare_sidecars(*_case_paths("absolute_threshold"))
        self.assertEqual(report["checks"]["absolute_change_threshold_m2"], 2_500_000)
        self.assertEqual(report["checks"]["maximum_class_change_m2"], 2_500_000)
        self.assertIn(
            "CDL_HISTOGRAM_ABSOLUTE_THRESHOLD_REACHED",
            report["decision"]["reason_codes"],
        )
        self.assertNotIn(
            "CDL_HISTOGRAM_RELATIVE_THRESHOLD_REACHED",
            report["decision"]["reason_codes"],
        )

    def test_classmap_and_geometry_drift_fail_closed_before_histograms(self) -> None:
        expected = {
            "classmap_drift": (
                "CLASSMAP_DRIFT",
                "CDL_CLASSMAP_DRIFT_REQUIRES_REMAP_REVIEW",
            ),
            "geometry_drift": (
                "GEOMETRY_DRIFT",
                "COUNTY_GEOMETRY_DRIFT_REQUIRES_REBASE",
            ),
        }
        for case, (outcome, reason) in expected.items():
            report = compare_sidecars(*_case_paths(case))
            with self.subTest(case=case):
                self.assertEqual(report["status"], outcome)
                self.assertEqual(report["checks"]["histogram_drift"], "not_evaluated")
                self.assertEqual(report["decision"]["reason_codes"], [reason])
                self.assertTrue(report["decision"]["blocking"])

    def test_threshold_profile_drift_abstains(self) -> None:
        prior = _load_candidate()
        current = copy.deepcopy(prior)
        thresholds = current["thresholds"]
        self.assertIsInstance(thresholds, dict)
        thresholds["relative_change_ppm"] = 30_000
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prior_path = root / "prior.json"
            current_path = root / "current.json"
            _write_candidate(prior_path, prior)
            _write_candidate(current_path, current)
            report = compare_sidecars(prior_path, current_path)
        self.assertEqual(report["status"], "ABSTAIN")
        self.assertEqual(report["decision"]["reason_codes"], ["MATERIALITY_PROFILE_DRIFT"])

    def test_regressed_year_is_stale(self) -> None:
        prior = _load_candidate()
        current = copy.deepcopy(prior)
        current["cdl_year"] = 2024
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prior_path = root / "prior.json"
            current_path = root / "current.json"
            _write_candidate(prior_path, prior)
            _write_candidate(current_path, current)
            report = compare_sidecars(prior_path, current_path)
        self.assertEqual(report["status"], "STALE_INPUT")
        self.assertEqual(report["decision"]["reason_codes"], ["CDL_YEAR_REGRESSED"])

    def test_regressed_observation_or_source_time_is_stale(self) -> None:
        cases = {
            "observed_at": ("observed_at", "2025-12-31T23:59:59Z", "OBSERVED_AT_REGRESSED"),
            "last_modified": (
                "last_modified",
                "2025-12-30T23:59:59Z",
                "SOURCE_LAST_MODIFIED_REGRESSED",
            ),
        }
        for case, (field, value, expected) in cases.items():
            prior = _load_candidate()
            current = copy.deepcopy(prior)
            if field == "observed_at":
                current[field] = value
            else:
                metadata = current["source_metadata"]
                self.assertIsInstance(metadata, dict)
                metadata[field] = value
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                prior_path = root / "prior.json"
                current_path = root / "current.json"
                _write_candidate(prior_path, prior)
                _write_candidate(current_path, current)
                report = compare_sidecars(prior_path, current_path)
            with self.subTest(case=case):
                self.assertEqual(report["status"], "STALE_INPUT")
                self.assertEqual(report["decision"]["reason_codes"], [expected])

    def test_county_area_drift_blocks_histogram_comparison(self) -> None:
        prior = _load_candidate()
        current = copy.deepcopy(prior)
        current["county_area_m2"] = 100_000_001
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prior_path = root / "prior.json"
            current_path = root / "current.json"
            _write_candidate(prior_path, prior)
            _write_candidate(current_path, current)
            report = compare_sidecars(prior_path, current_path)
        self.assertEqual(report["status"], "GEOMETRY_DRIFT")
        self.assertEqual(report["checks"]["county_area_m2"], "changed")
        self.assertEqual(report["checks"]["histogram_drift"], "not_evaluated")
        self.assertEqual(
            report["decision"]["reason_codes"],
            ["COUNTY_AREA_DRIFT_REQUIRES_REBASE"],
        )

    def test_profile_hash_mismatch_returns_non_echoing_error(self) -> None:
        candidate = _load_candidate()
        candidate["profile_hash"] = "sha256:" + ("e" * 64)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sensitive-sentinel.json"
            path.write_text(json.dumps(candidate), encoding="utf-8")
            report = compare_sidecars(path, _case_paths("no_material_change")[1])
        self.assertEqual(report["status"], "ERROR")
        serialized = serialize_report(report)
        self.assertIn("PRIOR_PROFILE_HASH_MISMATCH", serialized)
        self.assertNotIn("fixture-etag-a", serialized)
        self.assertNotIn("\"1\":40000000", serialized)

    def test_duplicate_keys_and_oversized_inputs_are_bounded(self) -> None:
        current = _case_paths("no_material_change")[1]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            duplicate = root / "duplicate.json"
            duplicate.write_text('{"profile_id":"a","profile_id":"b"}', encoding="utf-8")
            oversized = root / "oversized.json"
            oversized.write_bytes(b"{" + b" " * MAX_FIXTURE_BYTES + b"}")
            duplicate_report = compare_sidecars(duplicate, current)
            oversized_report = compare_sidecars(oversized, current)
        self.assertEqual(duplicate_report["status"], "ERROR")
        self.assertIn(
            "PRIOR_FIXTURE_JSON_INVALID",
            duplicate_report["decision"]["reason_codes"],
        )
        self.assertEqual(oversized_report["status"], "ERROR")
        self.assertIn(
            "PRIOR_FIXTURE_TOO_LARGE",
            oversized_report["decision"]["reason_codes"],
        )

    def test_integer_only_area_profile_rejects_floats_negative_and_overflow(self) -> None:
        cases = (
            (1.5, Finding("CLASS_AREA_INVALID", "$.class_histogram_m2.1")),
            (-1, Finding("CLASS_AREA_INVALID", "$.class_histogram_m2.1")),
            (MAX_AREA_M2 + 1, Finding("CLASS_AREA_INVALID", "$.class_histogram_m2.1")),
        )
        for value, expected in cases:
            candidate = _load_candidate()
            histogram = candidate["class_histogram_m2"]
            self.assertIsInstance(histogram, dict)
            histogram["1"] = value
            findings = validate_sidecar(candidate)
            with self.subTest(value=value):
                self.assertIn(expected, findings)

    def test_profile_rejects_empty_coverage_bad_chronology_and_class_aliases(self) -> None:
        cases: dict[str, tuple[dict[str, object], Finding]] = {}

        zero_coverage = _load_candidate()
        zero_coverage["class_histogram_m2"] = {"1": 0, "2": 0, "3": 0}
        cases["zero_coverage"] = (
            zero_coverage,
            Finding("CLASS_HISTOGRAM_ZERO_COVERAGE", "$.class_histogram_m2"),
        )

        future_modified = _load_candidate()
        metadata = future_modified["source_metadata"]
        self.assertIsInstance(metadata, dict)
        metadata["last_modified"] = "2026-01-02T00:00:00Z"
        cases["future_modified"] = (
            future_modified,
            Finding(
                "SOURCE_LAST_MODIFIED_AFTER_OBSERVED",
                "$.source_metadata.last_modified",
            ),
        )

        future_year = _load_candidate()
        future_year["cdl_year"] = 2027
        cases["future_year"] = (
            future_year,
            Finding("CDL_YEAR_AFTER_OBSERVED", "$.cdl_year"),
        )

        class_alias = _load_candidate()
        histogram = class_alias["class_histogram_m2"]
        self.assertIsInstance(histogram, dict)
        histogram["01"] = 1
        cases["class_alias"] = (
            class_alias,
            Finding("CLASS_ID_INVALID", "$.class_histogram_m2.01"),
        )

        for name, (candidate, expected) in cases.items():
            candidate["profile_hash"] = compute_profile_hash(candidate)
            with self.subTest(name=name):
                self.assertIn(expected, validate_sidecar(candidate))

    def test_reports_are_deterministic_and_network_is_never_used(self) -> None:
        prior, current = _case_paths("relative_threshold")
        first = serialize_report(compare_sidecars(prior, current))
        second = serialize_report(compare_sidecars(prior, current))
        self.assertEqual(first, second)
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()

    def test_cli_exit_polarity_and_json_output(self) -> None:
        for case, expected in sorted(CASE_OUTCOMES.items()):
            prior, current = _case_paths(case)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = main(
                    [
                        "--prior",
                        str(prior),
                        "--current",
                        str(current),
                        "--dry-run",
                    ]
                )
            report = json.loads(output.getvalue())
            with self.subTest(case=case):
                self.assertEqual(report["status"], expected)
                self.assertEqual(code, 0 if expected in SAFE_EXIT_OUTCOMES else 1)

    def test_explicit_output_is_create_only_and_repository_paths_fail(self) -> None:
        serialized = serialize_report(
            compare_sidecars(*_case_paths("no_material_change"))
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.json"
            write_report(output, serialized)
            self.assertEqual(output.read_text(encoding="utf-8"), serialized + "\n")
            with self.assertRaises(OSError):
                write_report(output, serialized)

            with contextlib.chdir(directory):
                relative_output = Path("relative-report.json")
                write_report(relative_output, serialized)
                self.assertEqual(
                    relative_output.read_text(encoding="utf-8"), serialized + "\n"
                )

        denied_paths = (
            REPO_ROOT / "cdl-watch-report.json",
            REPO_ROOT / "data/receipts/cdl-watch-report.json",
            REPO_ROOT / "docs/cdl-watch-report.json",
            REPO_ROOT / "policy/cdl-watch-report.json",
            REPO_ROOT / "schemas/cdl-watch-report.json",
        )
        for denied in denied_paths:
            with self.subTest(denied=denied):
                with self.assertRaises(OSError):
                    write_report(denied, serialized)

        with contextlib.chdir(REPO_ROOT / "tests"):
            traversal = Path("../data/receipts/cdl-watch-report.json")
            with self.assertRaises(OSError):
                write_report(traversal, serialized)


if __name__ == "__main__":
    unittest.main()
