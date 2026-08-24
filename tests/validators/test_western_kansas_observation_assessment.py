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
        cls.base_candidate = value["base_candidate"]
        cls.cases = {
            case["case_id"]: candidate_from_case(value["base_candidate"], case)
            for case in value["cases"]
        }

    def _forecast_candidate(self) -> dict[str, object]:
        candidate = copy.deepcopy(self.base_candidate)
        candidate["analysis_time"] = "2026-08-22T18:00:00Z"
        candidate["outcome"] = "FORECAST"
        candidate["claim"] = {
            "county_intersection_only": False,
            "kind": "DROUGHT_OUTLOOK",
            "resampled": False,
            "source_conflict": False,
            "source_support_preserved": True,
            "support_id": "cpc-sdo-kansas-2026-08-20",
            "support_kind": "POLYGON",
            "transformation_ref": None,
            "tuple_evidence_refs": ["evidence:cpc-sdo-2026-08-20"],
        }
        candidate["sources"] = [
            {
                "correction_ref": None,
                "crs": "EPSG:4326",
                "evidence_ref": "evidence:cpc-sdo-2026-08-20",
                "forecast_issue_time": "2026-08-20T12:30:00Z",
                "forecast_valid_end": "2026-11-30T23:59:59Z",
                "forecast_valid_start": "2026-08-20T12:30:00Z",
                "method": "official seasonal drought outlook",
                "observation_end": "2026-08-18T23:59:59Z",
                "observation_start": "2026-08-18T00:00:00Z",
                "observation_status": "PRESENT",
                "payload_digest": "sha256:4444444444444444444444444444444444444444444444444444444444444444",
                "predecessor_ref": "cpc-sdo-2026-07-16",
                "predecessor_relation": "SUCCESSOR",
                "publication_time": "2026-08-20T13:00:00Z",
                "resolution_m": 1000,
                "retrieval_time": "2026-08-21T14:00:00Z",
                "revision_status": "FINAL",
                "source_family": "CPC_DROUGHT_OUTLOOK",
                "source_id": "cpc-seasonal-drought-outlook",
                "source_role": "FORECAST",
                "source_version_ref": "cpc-sdo@2026-08-20",
                "supersedes_ref": None,
                "support_id": "cpc-sdo-kansas-2026-08-20",
                "support_kind": "POLYGON",
                "unit": None,
                "valid_end": None,
                "valid_start": None,
            }
        ]
        candidate["material_change"] = {
            "prior_claim_digest": "sha256:2222222222222222222222222222222222222222222222222222222222222222",
            "current_claim_digest": "sha256:5555555555555555555555555555555555555555555555555555555555555555",
            "declared_material": True,
        }
        return candidate

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

    def test_successor_forecast_remains_forecast(self) -> None:
        result = assess(self._forecast_candidate())
        self.assertEqual(result.outcome, "FORECAST")
        self.assertEqual(result.reason_codes, ())

    def test_forecast_cannot_prove_observed_condition(self) -> None:
        candidate = self._forecast_candidate()
        candidate["claim"]["kind"] = "DROUGHT_CLASSIFICATION"
        candidate["outcome"] = "ABSTAIN"
        result = assess(candidate)
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertEqual(result.reason_codes, ("FORECAST_CANNOT_PROVE_OBSERVED_CONDITION",))

    def test_future_forecast_abstains(self) -> None:
        candidate = self._forecast_candidate()
        candidate["sources"][0]["forecast_valid_start"] = "2026-08-23T00:00:00Z"
        candidate["sources"][0]["forecast_valid_end"] = "2026-11-30T23:59:59Z"
        candidate["outcome"] = "ABSTAIN"
        result = assess(candidate)
        self.assertEqual(result.outcome, "ABSTAIN")
        self.assertEqual(result.reason_codes, ("FORECAST_NOT_YET_VALID",))

    def test_expired_forecast_is_stale(self) -> None:
        candidate = self._forecast_candidate()
        candidate["analysis_time"] = "2026-12-01T00:00:00Z"
        candidate["outcome"] = "STALE"
        result = assess(candidate)
        self.assertEqual(result.outcome, "STALE")
        self.assertEqual(result.reason_codes, ("FORECAST_EXPIRED",))

    def test_successor_relationship_requires_predecessor(self) -> None:
        candidate = self._forecast_candidate()
        candidate["sources"][0]["predecessor_ref"] = None
        candidate["outcome"] = "ERROR"
        result = assess(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("FORECAST_PREDECESSOR_RELATION_INVALID", result.reason_codes)

    def test_forecast_family_requires_forecast_fields_and_role(self) -> None:
        candidate = self._forecast_candidate()
        candidate["sources"][0].pop("source_role")
        candidate["sources"][0]["forecast_issue_time"] = None
        candidate["outcome"] = "ERROR"
        result = assess(candidate)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("FORECAST_FIELDS_REQUIRED", result.reason_codes)


if __name__ == "__main__":
    unittest.main()
