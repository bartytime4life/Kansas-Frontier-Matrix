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

from tools.ingest.ssurgo_watch.ssurgo_watch import (
    BLOCKING_OUTCOMES,
    PROFILE_ID,
    REPO_ROOT,
    SAFE_EXIT_OUTCOMES,
    compare_sidecars,
    compute_content_hash,
    compute_spatial_diff_content_hash,
    compute_spec_hash,
    load_sidecar,
    load_spatial_diff,
    main,
    serialize_report,
    validate_sidecar,
    write_report,
)


FIXTURES = Path(__file__).parent / "fixtures"
CASE_OUTCOMES = {
    "below_threshold": "NO_MATERIAL_CHANGE",
    "constraint_change": "PROPOSED_WORK_RECORD",
    "derived_state_drift": "ERROR",
    "equal_total_label_drift": "PROPOSED_WORK_RECORD",
    "geometry_drift": "GEOMETRY_DRIFT",
    "material_area_change": "PROPOSED_WORK_RECORD",
    "no_material_change": "NO_MATERIAL_CHANGE",
    "schema_change": "PROPOSED_WORK_RECORD",
    "stale_input": "STALE_INPUT",
    "table_content_change": "PROPOSED_WORK_RECORD",
    "threshold_boundary": "NO_MATERIAL_CHANGE",
}


def _case_paths(case: str) -> tuple[Path, Path]:
    directory = FIXTURES / case
    return directory / "prior.sidecar.json", directory / "current.sidecar.json"


def _spatial_diff_path(case: str) -> Path | None:
    path = FIXTURES / case / "spatial_diff.json"
    return path if path.exists() else None


def _compare_case(case: str) -> dict[str, object]:
    prior, current = _case_paths(case)
    return compare_sidecars(prior, current, _spatial_diff_path(case))


def _load_valid_fixture() -> dict[str, object]:
    prior, _ = _case_paths("no_material_change")
    return json.loads(prior.read_text(encoding="utf-8"))


class SsurgoWatchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.network_patchers = (
            mock.patch.object(
                socket,
                "create_connection",
                side_effect=AssertionError("network denied"),
            ),
            mock.patch.object(socket, "getaddrinfo", side_effect=AssertionError("DNS denied")),
            mock.patch.object(
                urllib.request,
                "urlopen",
                side_effect=AssertionError("network denied"),
            ),
        )
        self.network_mocks = tuple(patcher.start() for patcher in self.network_patchers)

    def tearDown(self) -> None:
        for patcher in reversed(self.network_patchers):
            patcher.stop()

    def test_all_fixture_pairs_have_exact_outcomes_and_valid_inputs(self) -> None:
        for case, expected in sorted(CASE_OUTCOMES.items()):
            prior, current = _case_paths(case)
            with self.subTest(case=case, side="prior"):
                self.assertEqual(load_sidecar(prior).findings, ())
            with self.subTest(case=case, side="current"):
                self.assertEqual(load_sidecar(current).findings, ())
            spatial_diff = _spatial_diff_path(case)
            if spatial_diff is not None:
                with self.subTest(case=case, side="spatial_diff"):
                    self.assertEqual(load_spatial_diff(spatial_diff).findings, ())
            report = _compare_case(case)
            with self.subTest(case=case, report="outcome"):
                self.assertEqual(report["status"], expected)
                self.assertEqual(report["decision"]["outcome"], expected)
                self.assertFalse(report["decision"]["publication"])
                self.assertFalse(report["decision"]["promotion_allowed"])
                self.assertEqual(
                    report["decision"]["steward_review_required"],
                    expected != "NO_MATERIAL_CHANGE",
                )
                self.assertEqual(
                    report["decision"]["blocking"], expected in BLOCKING_OUTCOMES
                )

    def test_no_change_is_safe_and_has_no_reason(self) -> None:
        report = _compare_case("no_material_change")
        self.assertEqual(report["checks"]["package_metadata"], "same")
        self.assertEqual(report["checks"]["mapunit_area_drift"], "same")
        self.assertEqual(report["checks"]["mapunit_label_disagreement_area_m2"], 0)
        self.assertEqual(report["decision"]["reason_codes"], [])
        self.assertEqual(report["spec_hash"], _load_valid_fixture()["spec_hash"])
        self.assertRegex(report["inputs"]["prior_content_hash"], r"^sha256:[0-9a-f]{64}$")

    def test_below_threshold_package_republish_is_non_material(self) -> None:
        report = _compare_case("below_threshold")
        self.assertEqual(report["status"], "NO_MATERIAL_CHANGE")
        self.assertEqual(report["checks"]["package_metadata"], "changed")
        self.assertEqual(report["checks"]["mapunit_label_disagreement_area_m2"], 4_000)
        self.assertEqual(report["checks"]["mapunit_change_ppm_floor"], 4_000)
        self.assertEqual(
            report["decision"]["reason_codes"],
            [
                "MAPUNIT_AREA_DRIFT_AT_OR_BELOW_THRESHOLD",
                "SOURCE_METADATA_DRIFT_BELOW_MATERIALITY",
            ],
        )

    def test_strict_threshold_boundary_does_not_create_work(self) -> None:
        report = _compare_case("threshold_boundary")
        self.assertEqual(report["status"], "NO_MATERIAL_CHANGE")
        self.assertEqual(report["checks"]["mapunit_label_disagreement_area_m2"], 5_000)
        self.assertEqual(report["checks"]["mapunit_threshold_ppm"], 5_000)
        self.assertEqual(report["checks"]["materiality_comparison"], "strictly_greater_than")

    def test_above_threshold_creates_review_only_work(self) -> None:
        report = _compare_case("material_area_change")
        self.assertEqual(report["status"], "PROPOSED_WORK_RECORD")
        self.assertEqual(report["checks"]["mapunit_label_disagreement_area_m2"], 6_000)
        self.assertEqual(
            report["decision"]["reason_codes"],
            ["MAPUNIT_AREA_CHANGE_THRESHOLD_EXCEEDED"],
        )
        self.assertNotIn("source_url", serialize_report(report))

    def test_equal_total_topology_drift_uses_spatial_not_aggregate_area(self) -> None:
        report = _compare_case("equal_total_label_drift")
        self.assertEqual(report["status"], "PROPOSED_WORK_RECORD")
        self.assertEqual(report["checks"]["aggregate_area_change_lower_bound_m2"], 0)
        self.assertEqual(report["checks"]["mapunit_label_disagreement_area_m2"], 6_000)
        self.assertEqual(report["checks"]["mapunit_area_drift"], "material")

    def test_schema_change_is_material_without_area_change(self) -> None:
        report = _compare_case("schema_change")
        self.assertEqual(report["status"], "PROPOSED_WORK_RECORD")
        self.assertEqual(report["checks"]["attribute_schema"], "changed")
        self.assertEqual(report["checks"]["mapunit_label_disagreement_area_m2"], 0)
        self.assertEqual(
            report["decision"]["reason_codes"],
            [
                "ATTRIBUTE_SCHEMA_DRIFT_REQUIRES_REVIEW",
                "TABLE_CONTENT_DRIFT_REQUIRES_REVIEW",
            ],
        )

    def test_primary_foreign_key_constraint_change_is_material(self) -> None:
        report = _compare_case("constraint_change")
        self.assertEqual(report["status"], "PROPOSED_WORK_RECORD")
        self.assertEqual(report["checks"]["attribute_schema"], "changed")
        self.assertEqual(report["checks"]["changed_attribute_tables"], ["component"])
        self.assertEqual(report["checks"]["mapunit_label_disagreement_area_m2"], 0)

    def test_profiled_table_content_change_is_material(self) -> None:
        report = _compare_case("table_content_change")
        self.assertEqual(report["status"], "PROPOSED_WORK_RECORD")
        self.assertEqual(report["checks"]["attribute_schema"], "same")
        self.assertEqual(report["checks"]["table_content"], "changed")
        self.assertEqual(report["checks"]["changed_table_content_ids"], ["component"])
        self.assertEqual(
            report["decision"]["reason_codes"],
            ["TABLE_CONTENT_DRIFT_REQUIRES_REVIEW"],
        )

    def test_same_package_with_changed_derived_state_is_error(self) -> None:
        report = _compare_case("derived_state_drift")
        self.assertEqual(report["status"], "ERROR")
        self.assertEqual(
            report["checks"]["derived_state_consistency"],
            "invalid_same_package_changed_derivation",
        )
        self.assertEqual(
            report["decision"]["reason_codes"],
            ["DERIVED_STATE_CHANGED_WITHOUT_SOURCE_OR_PROFILE_CHANGE"],
        )

    def test_geometry_drift_abstains_from_materiality_math(self) -> None:
        report = _compare_case("geometry_drift")
        self.assertEqual(report["status"], "GEOMETRY_DRIFT")
        self.assertEqual(report["checks"]["mapunit_area_drift"], "not_evaluated")
        self.assertEqual(report["checks"]["changed_mapunit_geometry_ids"], ["MU-FIX-A"])
        self.assertEqual(
            report["decision"]["reason_codes"],
            ["MAPUNIT_GEOMETRY_DRIFT_REQUIRES_SPATIAL_DIFF"],
        )

    def test_regressed_publication_date_is_stale(self) -> None:
        report = _compare_case("stale_input")
        self.assertEqual(report["status"], "STALE_INPUT")
        self.assertEqual(report["checks"]["chronology"], "regressed")
        self.assertIn("PUBLICATION_DATE_REGRESSED", report["decision"]["reason_codes"])

    def test_spec_and_content_hash_roles_are_separate(self) -> None:
        candidate = _load_valid_fixture()
        self.assertEqual(candidate["profile_id"], PROFILE_ID)
        self.assertEqual(candidate["spec_hash"], compute_spec_hash(candidate))
        self.assertEqual(candidate["content_hash"], compute_content_hash(candidate))
        original_spec_hash = candidate["spec_hash"]
        candidate["observed_at"] = "2026-05-17T00:00:00Z"
        self.assertEqual(compute_spec_hash(candidate), original_spec_hash)
        self.assertNotEqual(candidate["content_hash"], compute_content_hash(candidate))
        self.assertEqual(
            [finding.code for finding in validate_sidecar(candidate)],
            ["CONTENT_HASH_MISMATCH"],
        )

    def test_live_or_undeclared_fields_fail_closed(self) -> None:
        candidate = _load_valid_fixture()
        candidate["source_url"] = "https://example.invalid/ssurgo.zip"
        candidate["fixture_only"] = False
        candidate["spec_hash"] = compute_spec_hash(candidate)
        candidate["content_hash"] = compute_content_hash(candidate)
        codes = {finding.code for finding in validate_sidecar(candidate)}
        self.assertEqual(codes, {"FIXTURE_ONLY_REQUIRED", "UNDECLARED_TOP_LEVEL_FIELD"})

    def test_invalid_coverage_and_noncanonical_schema_fail_closed(self) -> None:
        candidate = _load_valid_fixture()
        candidate["mapunit_areas_m2"]["MU-FIX-A"] = 500_000
        candidate["attribute_schema"]["mapunit"].reverse()
        candidate["content_hash"] = compute_content_hash(candidate)
        codes = {finding.code for finding in validate_sidecar(candidate)}
        self.assertEqual(
            codes,
            {"ATTRIBUTE_COLUMNS_NOT_CANONICAL", "MAPUNIT_COVERAGE_MISMATCH"},
        )

    def test_duplicate_json_key_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"profile_id":"a","profile_id":"b"}', encoding="utf-8")
            loaded = load_sidecar(path)
        self.assertEqual([finding.code for finding in loaded.findings], ["DUPLICATE_JSON_KEY"])

    def test_oversized_integer_is_rejected_without_parser_escape(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "oversized-integer.json"
            path.write_text('{"analysis_area_m2":' + ("9" * 5_000) + "}", encoding="utf-8")
            loaded = load_sidecar(path)
        self.assertEqual([finding.code for finding in loaded.findings], ["SIDECAR_LOAD_ERROR"])

    def test_primary_and_foreign_key_contracts_fail_closed(self) -> None:
        nullable_primary_key = _load_valid_fixture()
        nullable_primary_key["attribute_schema"]["mapunit"][0]["nullable"] = True
        nullable_primary_key["content_hash"] = compute_content_hash(nullable_primary_key)
        nullable_codes = {
            finding.code for finding in validate_sidecar(nullable_primary_key)
        }
        self.assertEqual(nullable_codes, {"ATTRIBUTE_PRIMARY_KEY_NULLABLE"})

        missing_target = _load_valid_fixture()
        missing_target["attribute_schema"]["component"][2]["references"] = "missing.id"
        missing_target["content_hash"] = compute_content_hash(missing_target)
        missing_codes = {finding.code for finding in validate_sidecar(missing_target)}
        self.assertEqual(missing_codes, {"ATTRIBUTE_REFERENCE_TARGET_MISSING"})

        type_mismatch = _load_valid_fixture()
        type_mismatch["attribute_schema"]["component"][2]["type"] = "integer"
        type_mismatch["content_hash"] = compute_content_hash(type_mismatch)
        mismatch_codes = {finding.code for finding in validate_sidecar(type_mismatch)}
        self.assertEqual(mismatch_codes, {"ATTRIBUTE_REFERENCE_TYPE_MISMATCH"})

    def test_materiality_profile_drift_abstains(self) -> None:
        prior = _load_valid_fixture()
        current = copy.deepcopy(prior)
        current["observed_at"] = "2026-05-16T00:00:00Z"
        current["materiality_profile"]["mapunit_area_change_ppm"] = 6_000
        current["spec_hash"] = compute_spec_hash(current)
        current["content_hash"] = compute_content_hash(current)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prior_path = root / "prior.json"
            current_path = root / "current.json"
            prior_path.write_text(json.dumps(prior), encoding="utf-8")
            current_path.write_text(json.dumps(current), encoding="utf-8")
            report = compare_sidecars(prior_path, current_path)
        self.assertEqual(report["status"], "ABSTAIN")
        self.assertEqual(
            report["decision"]["reason_codes"], ["MATERIALITY_PROFILE_DRIFT"]
        )

    def test_extraction_profile_drift_abstains_before_comparison(self) -> None:
        prior = _load_valid_fixture()
        current = copy.deepcopy(prior)
        current["observed_at"] = "2026-05-16T00:00:00Z"
        current["extraction_profile_hash"] = "sha256:" + ("a" * 64)
        current["spec_hash"] = compute_spec_hash(current)
        current["content_hash"] = compute_content_hash(current)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prior_path = root / "prior.json"
            current_path = root / "current.json"
            prior_path.write_text(json.dumps(prior), encoding="utf-8")
            current_path.write_text(json.dumps(current), encoding="utf-8")
            report = compare_sidecars(prior_path, current_path)
        self.assertEqual(report["status"], "ABSTAIN")
        self.assertEqual(report["decision"]["reason_codes"], ["EXTRACTION_PROFILE_DRIFT"])

    def test_geometry_profile_drift_abstains_before_comparison(self) -> None:
        prior = _load_valid_fixture()
        current = copy.deepcopy(prior)
        current["observed_at"] = "2026-05-16T00:00:00Z"
        current["geometry_profile_hash"] = "sha256:" + ("a" * 64)
        current["spec_hash"] = compute_spec_hash(current)
        current["content_hash"] = compute_content_hash(current)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prior_path = root / "prior.json"
            current_path = root / "current.json"
            prior_path.write_text(json.dumps(prior), encoding="utf-8")
            current_path.write_text(json.dumps(current), encoding="utf-8")
            report = compare_sidecars(prior_path, current_path)
        self.assertEqual(report["status"], "ABSTAIN")
        self.assertEqual(report["decision"]["reason_codes"], ["GEOMETRY_PROFILE_DRIFT"])

    def test_spatial_diff_bindings_and_area_bounds_fail_closed(self) -> None:
        prior, current = _case_paths("below_threshold")
        fixture_path = _spatial_diff_path("below_threshold")
        assert fixture_path is not None
        valid_diff = json.loads(fixture_path.read_text(encoding="utf-8"))

        for field, expected_reason in (
            ("prior_content_hash", "SPATIAL_DIFF_PRIOR_BINDING_MISMATCH"),
            ("current_content_hash", "SPATIAL_DIFF_CURRENT_BINDING_MISMATCH"),
            (
                "prior_geometry_set_hash",
                "SPATIAL_DIFF_PRIOR_GEOMETRY_BINDING_MISMATCH",
            ),
            (
                "current_geometry_set_hash",
                "SPATIAL_DIFF_CURRENT_GEOMETRY_BINDING_MISMATCH",
            ),
            (
                "geometry_profile_hash",
                "SPATIAL_DIFF_GEOMETRY_PROFILE_BINDING_MISMATCH",
            ),
        ):
            forged = copy.deepcopy(valid_diff)
            forged[field] = "sha256:" + ("a" * 64)
            forged["content_hash"] = compute_spatial_diff_content_hash(forged)
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "spatial-diff.json"
                path.write_text(json.dumps(forged), encoding="utf-8")
                report = compare_sidecars(prior, current, path)
            with self.subTest(field=field):
                self.assertEqual(report["status"], "ERROR")
                self.assertIn(expected_reason, report["decision"]["reason_codes"])

        invalid_area = copy.deepcopy(valid_diff)
        invalid_area["changed_label_area_m2"] = 3_999
        invalid_area["content_hash"] = compute_spatial_diff_content_hash(invalid_area)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "spatial-diff.json"
            path.write_text(json.dumps(invalid_area), encoding="utf-8")
            report = compare_sidecars(prior, current, path)
        self.assertEqual(report["status"], "ERROR")
        self.assertEqual(
            report["decision"]["reason_codes"], ["SPATIAL_DIFF_AREA_INCONSISTENT"]
        )

    def test_spatial_diff_is_rejected_without_geometry_drift(self) -> None:
        spatial_diff = _spatial_diff_path("below_threshold")
        assert spatial_diff is not None
        report = compare_sidecars(*_case_paths("no_material_change"), spatial_diff)
        self.assertEqual(report["status"], "ERROR")
        self.assertEqual(
            report["decision"]["reason_codes"],
            ["SPATIAL_DIFF_WITHOUT_GEOMETRY_DRIFT"],
        )

    def test_invalid_spatial_diff_reason_is_normalized_once(self) -> None:
        prior, current = _case_paths("below_threshold")
        fixture_path = _spatial_diff_path("below_threshold")
        assert fixture_path is not None
        invalid = json.loads(fixture_path.read_text(encoding="utf-8"))
        invalid["crs"] = "EPSG:4326"
        invalid["content_hash"] = compute_spatial_diff_content_hash(invalid)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid-spatial-diff.json"
            path.write_text(json.dumps(invalid), encoding="utf-8")
            report = compare_sidecars(prior, current, path)
        self.assertEqual(report["status"], "ERROR")
        self.assertEqual(
            report["decision"]["reason_codes"], ["SPATIAL_DIFF_CRS_INVALID"]
        )

    def test_deterministic_and_network_is_never_used(self) -> None:
        first = serialize_report(_compare_case("material_area_change"))
        second = serialize_report(_compare_case("material_area_change"))
        self.assertEqual(first, second)
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()

    def test_cli_exit_polarity_and_json_output(self) -> None:
        for case, expected in sorted(CASE_OUTCOMES.items()):
            output = io.StringIO()
            prior, current = _case_paths(case)
            arguments = [
                "--prior",
                str(prior),
                "--current",
                str(current),
            ]
            spatial_diff = _spatial_diff_path(case)
            if spatial_diff is not None:
                arguments.extend(["--spatial-diff", str(spatial_diff)])
            arguments.append("--dry-run")
            with contextlib.redirect_stdout(output):
                code = main(arguments)
            report = json.loads(output.getvalue())
            with self.subTest(case=case):
                self.assertEqual(report["status"], expected)
                self.assertEqual(code, 0 if expected in SAFE_EXIT_OUTCOMES else 1)

    def test_output_is_create_only_and_repository_paths_are_denied(self) -> None:
        serialized = serialize_report(_compare_case("no_material_change"))
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.json"
            write_report(output, serialized)
            self.assertEqual(output.read_text(encoding="utf-8"), serialized + "\n")
            with self.assertRaises(OSError):
                write_report(output, serialized)

        denied = (
            REPO_ROOT / "ssurgo-watch-report.json",
            REPO_ROOT / "data/receipts/ssurgo-watch-report.json",
            REPO_ROOT / "data/published/ssurgo-watch-report.json",
            REPO_ROOT / "release/ssurgo-watch-report.json",
        )
        for path in denied:
            with self.subTest(path=path):
                with self.assertRaises(OSError):
                    write_report(path, serialized)


if __name__ == "__main__":
    unittest.main()
