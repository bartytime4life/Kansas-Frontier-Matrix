from __future__ import annotations

import copy
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = REPO_ROOT / "tools/validators/validate_dem_source_asset_candidate.py"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/spatial-foundation/dem_source_asset_candidate/cases.json"
SCHEMA = REPO_ROOT / "schemas/contracts/v1/spatial-foundation/dem_source_asset_candidate.schema.json"
WORKFLOW = REPO_ROOT / ".github/workflows/dem-source-asset-candidate.yml"
NO_NETWORK_GUARD = REPO_ROOT / "tools/ci/kfm_no_network/sitecustomize.py"
DEM_RECEIPT_NAME = "genrec-dem-source-asset-candidate-20260909.json"
DEM_AUTHORING_MERGE_REF = "0d0dbf355370fa7271feabba8f5b6c9f35fdb3a8"
DEM_RECEIPT_STEP_NAME = "Replay immutable authoring receipt at the PR 4452 merge"

spec = importlib.util.spec_from_file_location("dem_source_asset_candidate_validator", VALIDATOR)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


class DemSourceAssetCandidateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = json.loads(FIXTURES.read_text(encoding="utf-8"))
        base = self.fixture["base_candidate"]
        self.by_id = {
            case["case_id"]: {
                **case,
                "candidate": module.materialize_case(base, case),
            }
            for case in self.fixture["cases"]
        }

    def test_schema_is_closed_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual("PROPOSED_INACTIVE", schema["x-kfm"]["status"])
        self.assertEqual("FIXTURE_ONLY", schema["x-kfm"]["execution_mode"])
        self.assertEqual("NONE", schema["x-kfm"]["authority"])

    def test_workflow_activates_shared_python_no_network_guard(self) -> None:
        workflow = WORKFLOW.read_text(encoding="utf-8")
        guard = (
            "PYTHONPATH: ${{ github.workspace }}/tools/ci/kfm_no_network:"
            "${{ github.workspace }}"
        )
        self.assertTrue(NO_NETWORK_GUARD.is_file())
        self.assertEqual(3, workflow.count(guard))
        for step_name in (
            "Validate exact inactive DEM candidate",
            "Verify renderer-neutral package exports",
            DEM_RECEIPT_STEP_NAME,
        ):
            self.assertIn(
                f"- name: {step_name}\n"
                "        env:\n"
                f"          {guard}\n",
                workflow,
            )

    def test_workflow_replays_immutable_receipt_at_exact_merge_ref(self) -> None:
        workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        steps = workflow["jobs"]["validate"]["steps"]

        checkout_steps = [
            step
            for step in steps
            if str(step.get("uses", "")).startswith("actions/checkout@")
        ]
        self.assertEqual(len(checkout_steps), 1)
        self.assertEqual(checkout_steps[0]["with"]["fetch-depth"], 0)
        self.assertFalse(checkout_steps[0]["with"]["persist-credentials"])

        receipt_steps = [
            step
            for step in steps
            if "validate_generated_receipt.py" in str(step.get("run", ""))
            and DEM_RECEIPT_NAME in str(step.get("run", ""))
        ]
        self.assertEqual(len(receipt_steps), 1)
        self.assertEqual(receipt_steps[0]["name"], DEM_RECEIPT_STEP_NAME)
        receipt_command = str(receipt_steps[0]["run"])
        self.assertIn("--repo-root .", receipt_command)
        artifact_refs = re.findall(
            r"--artifact-git-ref\s+([0-9a-f]{40})", receipt_command
        )
        self.assertEqual(artifact_refs, [DEM_AUTHORING_MERGE_REF])

    def test_fixture_suite_has_exact_polarity(self) -> None:
        ok, report = module.run_fixture_suite()
        self.assertTrue(ok, report)
        self.assertEqual(50, len(report["cases"]))
        statuses = [case["actual_status"] for case in report["cases"]]
        self.assertEqual(1, statuses.count("PASS"))
        self.assertEqual(49, statuses.count("DENY"))
        self.assertTrue(all(case["ok"] for case in report["cases"]))

    def test_exact_ellsworth_candidate_passes_only_as_hold(self) -> None:
        candidate = self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]
        result = module.validate_document(candidate)
        self.assertEqual(("PASS", "HOLD", ()), (result.status, result.review_outcome, result.findings))
        self.assertEqual("USGS_1M_14_x56y429_KS_Statewide_2018_A18", candidate["source_identity"]["tile_id"])
        self.assertEqual(26914, candidate["delivered_crs"]["code"])
        self.assertEqual(3744, candidate["lineage"]["source_horizontal_crs"]["code"])
        self.assertEqual(5703, candidate["vertical_reference"]["datum_code"])
        self.assertEqual(-999999, candidate["raster_grid"]["nodata"]["value"])
        self.assertEqual("UNRESOLVED", candidate["vertical_accuracy"]["status"])

    def test_exact_asset_hashes_and_dates_are_distinct(self) -> None:
        candidate = self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]
        self.assertEqual(
            "sha256:8d923dc122ee99303201acb07c9fc49c190b19545a75768384f49ccb4e975cd7",
            candidate["assets"]["raster_tiff"]["content_sha256"],
        )
        self.assertEqual(
            "sha256:b2125a3c069284a48feef0e1d9935b13ae1426ce5e7aab3e3e914c23cec00d00",
            candidate["assets"]["metadata_xml"]["content_sha256"],
        )
        temporal = candidate["temporal_identity"]
        self.assertEqual("2018-04-30", temporal["source_observation_interval"]["start"])
        self.assertEqual("2019-03-20", temporal["source_observation_interval"]["end"])
        self.assertEqual("2023-06-12", temporal["tile_publication_date"])
        self.assertFalse(temporal["tile_metadata_temporal_range"]["treated_as_source_observation_interval"])

    def test_geoid_scope_and_accuracy_hold_are_explicit(self) -> None:
        candidate = self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]
        vertical = candidate["vertical_reference"]
        self.assertEqual(
            {
                "status": "UNRESOLVED",
                "model": None,
                "scope": "DELIVERED_TILE",
                "evidence": None,
            },
            vertical["delivered_tile_geoid"],
        )
        self.assertEqual("GEOID12B", vertical["source_work_unit_geoid"]["model"])
        report = candidate["vertical_accuracy"]["available_project_report"]
        self.assertEqual("PROJECT_UTM14_MULTI_WORK_UNIT", report["scope"])
        self.assertEqual((708, 0.0864, 0.1694), (report["nva_checkpoint_count"], report["nva_rmsez"], report["nva_accuracy_95"]))
        self.assertEqual((492, 0.2397), (report["vva_checkpoint_count"], report["vva_percentile_95"]))
        self.assertEqual("NOT_ESTABLISHED", report["applicability_to_delivered_tile"])
        self.assertEqual(
            [
                "GEOID_MODEL_UNRESOLVED",
                "HUMAN_REVIEW_REQUIRED",
                "VERTICAL_ACCURACY_UNRESOLVED",
            ],
            candidate["blockers"],
        )

    def test_fixture_sample_is_public_safe_unexaggerated_and_quantized(self) -> None:
        sample = self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]["inspection_sample"]
        self.assertEqual((-98.23, 38.73), (sample["longitude"], sample["latitude"]))
        self.assertEqual((2909, 6934), (sample["row"], sample["column"]))
        self.assertEqual(469.4603271484375, sample["source_elevation"]["value"])
        self.assertEqual([129, 213, 118], sample["fixture_encoding"]["rgb"])
        self.assertEqual(469.4609375, sample["fixture_encoding"]["decoded_value_m"])
        self.assertEqual(-999999, sample["fixture_encoding"]["source_nodata_value"])
        self.assertEqual(1, sample["fixture_encoding"]["validity_mask_value"])
        self.assertEqual(1, sample["display_default_exaggeration"])
        self.assertFalse(sample["reported_value_exaggerated"])
        self.assertFalse(sample["runtime_sample_authorized"])

    def test_captured_lineage_and_kansas_boundaries_have_offline_projection_binding(self) -> None:
        candidate = self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]
        captures = candidate["evidence_captures"]
        index = captures["three_dep_index_query"]
        self.assertEqual(5003, index["byte_length"])
        self.assertEqual(
            "sha256:add44226c3e31c2f459cba04e6d66e5de06eb177b26cb79dd0f793a37bc35fd7",
            index["content_sha256"],
        )
        self.assertEqual("KS_Statewide_B10_2018", index["captured_projection"]["work_unit"])
        state = captures["census_state_point_query"]
        self.assertEqual(
            ("20", "KS", "Kansas"),
            (
                state["captured_projection"]["state_geoid"],
                state["captured_projection"]["state_abbreviation"],
                state["captured_projection"]["state_name"],
            ),
        )
        county = captures["census_county_point_query"]
        self.assertEqual(
            ("20053", "20", "053", "Ellsworth County"),
            (
                county["captured_projection"]["county_geoid"],
                county["captured_projection"]["state_code"],
                county["captured_projection"]["county_code"],
                county["captured_projection"]["county_name"],
            ),
        )
        self.assertTrue(all(not capture["raw_response_stored"] for capture in captures.values()))
        self.assertTrue(
            all(
                capture["remote_byte_identity_scope"] == "AUTHOR_TIME_OBSERVATION_ONLY"
                for capture in captures.values()
            )
        )
        snapshot, valid = module._load_projection_snapshot()
        self.assertTrue(valid)
        self.assertIsNotNone(snapshot)
        assert snapshot is not None
        self.assertEqual(
            captures["census_county_point_query"]["captured_projection"],
            snapshot["projections"]["census_county_point_query"],
        )

    def test_public_domain_rights_are_bound_to_the_hashed_metadata_asset(self) -> None:
        candidate = self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]
        rights = candidate["source_identity"]["rights_evidence"]
        self.assertEqual(
            "PUBLIC_DOMAIN_WITH_USGS_METADATA_CONSTRAINTS",
            candidate["source_identity"]["rights"],
        )
        self.assertEqual(candidate["source_identity"]["rights"], rights["classification"])
        self.assertEqual("assets.metadata_xml", rights["evidence_asset_ref"])
        self.assertEqual(
            candidate["assets"]["metadata_xml"]["content_sha256"],
            rights["evidence_content_sha256"],
        )
        self.assertEqual(
            "ALL_3DEP_PRODUCTS_PUBLIC_DOMAIN", rights["public_domain_assertion"]
        )
        self.assertEqual("/metadata/idinfo/accconst", rights["access_constraints_xpath"])
        self.assertEqual("/metadata/idinfo/useconst", rights["use_constraints_xpath"])

    def test_declared_cross_crs_transform_reconciles_point_and_footprint(self) -> None:
        candidate = self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]
        sample = candidate["inspection_sample"]
        transformed = module._utm14_forward(sample["longitude"], sample["latitude"])
        self.assertAlmostEqual(sample["projected_x"], transformed[0], delta=0.001)
        self.assertAlmostEqual(sample["projected_y"], transformed[1], delta=0.001)

        bounds = candidate["spatial_coverage"]["nominal_projected_bounds"]
        corners = (
            (bounds["x_min"], bounds["y_min"]),
            (bounds["x_min"], bounds["y_max"]),
            (bounds["x_max"], bounds["y_min"]),
            (bounds["x_max"], bounds["y_max"]),
        )
        geographic = [module._utm14_inverse(*corner) for corner in corners]
        actual = candidate["spatial_coverage"]["wgs84_bbox"]
        expected = {
            "west": min(point[0] for point in geographic),
            "south": min(point[1] for point in geographic),
            "east": max(point[0] for point in geographic),
            "north": max(point[1] for point in geographic),
        }
        for key, value in expected.items():
            self.assertAlmostEqual(actual[key], value, delta=1e-8)

    def test_identity_is_deterministic(self) -> None:
        candidate = self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]
        self.assertEqual(candidate, module.finalize_document(candidate))
        self.assertEqual(candidate["candidate_id"], module._identity(candidate)[0])
        self.assertEqual(candidate["spec_hash"], module._identity(candidate)[1])

    def test_stored_base_identity_is_validated_without_repair(self) -> None:
        base = self.fixture["base_candidate"]
        for field, value, code in (
            (
                "candidate_id",
                "kfm:dem-source-asset-candidate:" + "f" * 64,
                "CANDIDATE_ID_MISMATCH",
            ),
            ("spec_hash", "sha256:" + "f" * 64, "CANDIDATE_SPEC_HASH_MISMATCH"),
        ):
            candidate = {**base, field: value}
            case = {"case_id": f"tampered-{field}", "tamper": []}
            materialized = module.materialize_case(candidate, case)
            self.assertEqual(value, materialized[field])
            result = module.validate_document(materialized)
            self.assertEqual("DENY", result.status)
            self.assertIn(code, {finding.code for finding in result.findings})

    def test_huge_raw_numbers_deny_without_reaching_float_arithmetic(self) -> None:
        base = self.fixture["base_candidate"]
        for path in (
            "raster_grid.width",
            "inspection_sample.projected_x",
            "inspection_sample.source_elevation.value",
            "inspection_sample.fixture_encoding.decoded_value_m",
            "vertical_accuracy.available_project_report.nva_rmsez",
        ):
            candidate = copy.deepcopy(base)
            module._set_path(candidate, path, 10**400)
            result = module.validate_document(candidate)
            self.assertEqual("DENY", result.status, path)
            self.assertEqual(
                {"NUMERIC_DOMAIN_INVALID"},
                {finding.code for finding in result.findings},
                path,
            )

    def test_negative_controls_cover_boundary(self) -> None:
        expected = {
            "invalid-asset-tile-identity": "ASSET_TILE_ID_MISMATCH",
            "invalid-project-identity-drift": "PROJECT_IDENTITY_MISMATCH",
            "invalid-authoritative-asset-locator": "ASSET_LOCATOR_MISMATCH",
            "invalid-authoritative-asset-bytes": "ASSET_BYTES_MISMATCH",
            "invalid-asset-retrieval-chronology": "ASSET_RETRIEVAL_BEFORE_LAST_MODIFIED",
            "invalid-index-capture-bytes": "EVIDENCE_CAPTURE_BYTES_MISMATCH",
            "invalid-capture-chronology-before-census-vintage": "CENSUS_VINTAGE_AFTER_CAPTURE",
            "invalid-capture-after-authoring-cutoff": "EVIDENCE_CAPTURE_AFTER_AUTHORING_CUTOFF",
            "invalid-index-capture-projection": "INDEX_CAPTURE_LINEAGE_MISMATCH",
            "invalid-projection-snapshot-binding": "EVIDENCE_PROJECTION_SNAPSHOT_MISMATCH",
            "invalid-rights-evidence-binding": "RIGHTS_EVIDENCE_MISMATCH",
            "invalid-temporal-identity-conflated": "TEMPORAL_IDENTITY_CONFLATED",
            "invalid-incomplete-delivered-crs": "SCHEMA_INVALID",
            "invalid-geoid-blocker-omitted": "SCHEMA_INVALID",
            "invalid-accuracy-blocker-omitted": "SCHEMA_INVALID",
            "invalid-program-accuracy-substitution": "SCHEMA_INVALID",
            "invalid-project-accuracy-report-internal-mismatch": "ACCURACY_REPORT_INTERNAL_MISMATCH",
            "invalid-pilot-point-outside-tile": "COVERAGE_POINT_OUTSIDE_TILE",
            "invalid-kansas-state-capture": "KANSAS_COVERAGE_EVIDENCE_MISMATCH",
            "invalid-ellsworth-county-capture": "ELLSWORTH_COVERAGE_EVIDENCE_MISMATCH",
            "invalid-metadata-footprint-transform": "COVERAGE_CRS_TRANSFORM_MISMATCH",
            "invalid-projected-coordinate-magnitude": "NUMERIC_DOMAIN_INVALID",
            "invalid-jcs-safe-integer-domain": "NUMERIC_DOMAIN_INVALID",
            "invalid-sample-cross-crs-transform": "SAMPLE_CRS_TRANSFORM_MISMATCH",
            "invalid-storage-bounds": "RASTER_GRID_BOUNDS_MISMATCH",
            "invalid-sample-validity-mask-binding": "SAMPLE_VALIDITY_MASK_MISMATCH",
            "invalid-sample-decoding": "SAMPLE_ENCODING_MISMATCH",
            "invalid-candidate-identity": "CANDIDATE_ID_MISMATCH",
        }
        for case_id, code in expected.items():
            result = module.validate_document(self.by_id[case_id]["candidate"])
            self.assertEqual("DENY", result.status, case_id)
            self.assertIn(code, {finding.code for finding in result.findings}, case_id)

    def test_all_authority_effects_remain_false(self) -> None:
        candidate = self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]
        self.assertTrue(all(value is False for value in candidate["effects"].values()))
        expected_effect_cases = {
            "invalid-effect-" + key.replace("_", "-") for key in candidate["effects"]
        }
        actual_effect_cases = {
            case_id
            for case_id in self.by_id
            if case_id.startswith("invalid-effect-")
        }
        self.assertEqual(expected_effect_cases, actual_effect_cases)
        for case_id in expected_effect_cases:
            result = module.validate_document(self.by_id[case_id]["candidate"])
            self.assertEqual("DENY", result.status, case_id)
            self.assertEqual(
                {"SCHEMA_INVALID"},
                {finding.code for finding in result.findings},
                case_id,
            )
        serialized = json.loads(module._serialize(module.validate_document(candidate)))
        self.assertEqual("NONE", serialized["authority"])
        self.assertEqual("FIXTURE_ONLY", serialized["execution_mode"])
        self.assertEqual("HOLD", serialized["review_outcome"])

    def test_symlink_input_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "fixture.json"
            target.write_text(
                json.dumps(self.by_id["valid-exact-ellsworth-tile-hold"]["candidate"]),
                encoding="utf-8",
            )
            link = Path(directory) / "link.json"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            result = module.validate_file(link)
            self.assertEqual("ERROR", result.status)
            self.assertEqual({"CANDIDATE_JSON_INVALID"}, {finding.code for finding in result.findings})

    def test_cli_is_deterministic(self) -> None:
        command = [sys.executable, str(VALIDATOR), "--fixtures"]
        first = subprocess.run(command, check=True, capture_output=True, text=True)
        second = subprocess.run(command, check=True, capture_output=True, text=True)
        self.assertEqual(first.stdout, second.stdout)
        self.assertTrue(json.loads(first.stdout)["ok"])

    def test_validator_has_no_network_or_write_surface(self) -> None:
        source = VALIDATOR.read_text(encoding="utf-8")
        for token in (
            "import requests",
            "import urllib",
            "import socket",
            "from socket",
            ".write_text(",
            ".write_bytes(",
            "os.remove(",
            "os.replace(",
            "urlopen(",
        ):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
