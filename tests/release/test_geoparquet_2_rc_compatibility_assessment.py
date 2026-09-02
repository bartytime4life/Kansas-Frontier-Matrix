from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from tools.validators.release.validate_geoparquet_2_rc_compatibility_assessment import (
    CASES_PATH,
    EXPECTED_TOOLCHAINS,
    assess,
    candidate_from_case,
    validate_cases,
)


class GeoParquet2RcCompatibilityAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        value = json.loads(Path(CASES_PATH).read_text(encoding="utf-8"))
        cls.base = value["base_candidate"]
        cls.cases = {
            case["case_id"]: candidate_from_case(value["base_candidate"], case)
            for case in value["cases"]
        }

    def test_exact_fixture_matrix_passes(self) -> None:
        self.assertEqual(validate_cases(), 0)

    def test_ready_means_only_ready_for_byte_probes(self) -> None:
        candidate = copy.deepcopy(self.cases["ready_exact_synthetic_declaration"])
        result = assess(candidate)
        self.assertEqual(result.outcome, "READY")
        self.assertEqual(result.reason_codes, ())
        self.assertTrue(all(value is False for value in candidate["governance"].values()))

    def test_sedona_surfaces_are_distinct(self) -> None:
        matrix = self.base["toolchain_matrix"]
        self.assertIn("SEDONA_SPARK", matrix)
        self.assertIn("SEDONA_DB", matrix)
        self.assertNotEqual(matrix["SEDONA_SPARK"]["tool_version"], matrix["SEDONA_DB"]["tool_version"])

    def test_exact_versions_match_declared_matrix(self) -> None:
        for lane, expected in EXPECTED_TOOLCHAINS.items():
            self.assertEqual(self.base["toolchain_matrix"][lane]["tool_version"], expected["tool_version"])

    def test_pending_probes_hold(self) -> None:
        result = assess(copy.deepcopy(self.cases["hold_byte_probes_pending"]))
        self.assertEqual(result.outcome, "HOLD")
        self.assertEqual(result.reason_codes, ("BYTE_PROBES_PENDING",))

    def test_wrong_tool_version_is_error(self) -> None:
        result = assess(copy.deepcopy(self.cases["error_gdal_version_mismatch"]))
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.reason_codes, ("TOOLCHAIN_VERSION_MISMATCH",))

    def test_spark_transitive_mismatch_is_error(self) -> None:
        result = assess(copy.deepcopy(self.cases["error_sedona_spark_transitive"]))
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.reason_codes, ("TOOLCHAIN_TRANSITIVE_PIN_MISMATCH",))

    def test_duplicate_evidence_reference_is_error(self) -> None:
        result = assess(copy.deepcopy(self.cases["error_duplicate_evidence_ref"]))
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.reason_codes, ("EVIDENCE_REF_REUSED",))

    def test_collapsed_sedona_matrix_is_error(self) -> None:
        candidate = copy.deepcopy(self.base)
        candidate["toolchain_matrix"].pop("SEDONA_DB")
        candidate["outcome"] = "ERROR"
        result = assess(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("SCHEMA_INVALID", result.reason_codes)

    def test_governance_claim_is_error(self) -> None:
        result = assess(copy.deepcopy(self.cases["error_governance"]))
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("GOVERNANCE_BOUNDARY_VIOLATION", result.reason_codes)


if __name__ == "__main__":
    unittest.main()
