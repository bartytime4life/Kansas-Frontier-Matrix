from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from tools.validators.evidence.validate_western_kansas_observation_assessment import (
    CASES_PATH,
    assess,
    candidate_from_case,
    validate_cases,
)


class WesternKansasObservationAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        value = json.loads(Path(CASES_PATH).read_text(encoding="utf-8"))
        cls.cases = {
            case["case_id"]: candidate_from_case(value["base_candidate"], case)
            for case in value["cases"]
        }

    def test_exact_case_matrix_passes(self) -> None:
        self.assertEqual(validate_cases(), 0)

    def test_observed_direct_support(self) -> None:
        result = assess(copy.deepcopy(self.cases["observed_streamflow"]))
        self.assertEqual(result.outcome, "OBSERVED")
        self.assertEqual(result.reason_codes, ())

    def test_cross_source_derivation(self) -> None:
        result = assess(copy.deepcopy(self.cases["derived_cross_source_stress"]))
        self.assertEqual(result.outcome, "DERIVED")
        self.assertEqual(result.reason_codes, ())

    def test_recent_publication_does_not_refresh_old_observation(self) -> None:
        result = assess(copy.deepcopy(self.cases["stale_observation"]))
        self.assertEqual(result.outcome, "STALE")
        self.assertEqual(result.reason_codes, ("OBSERVATION_STALE",))

    def test_timezone_less_analysis_timestamp_is_finite_error(self) -> None:
        result = assess(copy.deepcopy(self.cases["timezone_less_analysis_timestamp"]))
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.reason_codes, ("TEMPORAL_ORDER_INVALID",))

    def test_timezone_less_source_timestamp_is_finite_error(self) -> None:
        candidate = copy.deepcopy(self.cases["observed_streamflow"])
        candidate["sources"][0]["observation_end"] = "2026-07-28T23:59:59"
        result = assess(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(result.reason_codes, ("TEMPORAL_ORDER_INVALID",))

    def test_groundwater_shortcuts_abstain(self) -> None:
        usdm = assess(copy.deepcopy(self.cases["deny_usdm_groundwater_inference"]))
        flow = assess(copy.deepcopy(self.cases["deny_streamflow_groundwater_inference"]))
        self.assertEqual(usdm.outcome, "ABSTAIN")
        self.assertEqual(flow.outcome, "ABSTAIN")

    def test_support_erasure_is_error(self) -> None:
        result = assess(copy.deepcopy(self.cases["deny_resampling_support_erasure"]))
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("SOURCE_SUPPORT_ERASURE_DENIED", result.reason_codes)

    def test_correction_and_supersession_differ(self) -> None:
        corrected = assess(copy.deepcopy(self.cases["corrected_observation"]))
        superseded = assess(copy.deepcopy(self.cases["superseded_observation"]))
        self.assertEqual(corrected.outcome, "OBSERVED")
        self.assertEqual(superseded.outcome, "ABSTAIN")

    def test_governance_claim_is_error(self) -> None:
        result = assess(copy.deepcopy(self.cases["deny_governance_claim"]))
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("GOVERNANCE_BOUNDARY_VIOLATION", result.reason_codes)


if __name__ == "__main__":
    unittest.main()
