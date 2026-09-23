from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

import pytest

from tools.validators.evidence.validate_western_kansas_observation_assessment import (
    CASES_PATH,
    assess,
    candidate_from_case,
    validate_cases,
)


DIRECT_CLAIMS = (
    ("DROUGHT_CLASSIFICATION", "USDM", "POLYGON"),
    ("STREAMFLOW_CONDITION", "USGS_STREAMFLOW", "STATION"),
    ("GROUNDWATER_CONDITION", "KGS_GROUNDWATER", "POINT"),
    ("EVAPORATIVE_DEMAND", "PRECIP_EDDI", "GRID_CELL"),
    ("PRECIPITATION_CONDITION", "PRECIP_EDDI", "GRID_CELL"),
    ("SOIL_MOISTURE_CONDITION", "SOIL_MOISTURE", "GRID_CELL"),
    ("AGRICULTURE_CONTEXT", "AGRICULTURE_CONTEXT", "POLYGON"),
    ("MANAGEMENT_BOUNDARY_CONTEXT", "WATER_MANAGEMENT_BOUNDARY", "MANAGEMENT_AREA"),
)


def _candidate(case_id: str = "observed_streamflow") -> dict:
    value = json.loads(Path(CASES_PATH).read_text(encoding="utf-8"))
    case = next(case for case in value["cases"] if case["case_id"] == case_id)
    return candidate_from_case(value["base_candidate"], case)


@pytest.mark.parametrize("kind,family,support_kind", DIRECT_CLAIMS)
@pytest.mark.parametrize("support_change", ["none", "id", "kind"])
def test_direct_claim_uses_recorded_source_support(
    kind: str, family: str, support_kind: str, support_change: str
) -> None:
    candidate = _candidate()
    candidate["claim"].update(kind=kind, support_kind=support_kind)
    candidate["sources"][0].update(source_family=family, support_kind=support_kind)
    if support_change == "id":
        candidate["claim"]["support_id"] = "synthetic-other-support"
    elif support_change == "kind":
        candidate["claim"]["support_kind"] = "COUNTY"
    candidate["outcome"] = "OBSERVED" if support_change == "none" else "ABSTAIN"

    result = assess(candidate)

    assert result.outcome == candidate["outcome"]
    assert result.reason_codes == (
        () if support_change == "none" else ("SOURCE_SUPPORT_MISMATCH",)
    )


@pytest.mark.parametrize("resampled", [False, True])
@pytest.mark.parametrize("preserved", [False, True])
@pytest.mark.parametrize("transform", [None, "transform:synthetic-resample"])
def test_direct_support_mismatch_cannot_be_overridden_by_claim_flags(
    resampled: bool, preserved: bool, transform: str | None
) -> None:
    candidate = _candidate()
    candidate["claim"].update(
        support_id="synthetic-other-station",
        resampled=resampled,
        source_support_preserved=preserved,
        transformation_ref=transform,
    )
    erasure = resampled and not preserved
    candidate["outcome"] = "ERROR" if erasure else "ABSTAIN"

    result = assess(candidate)

    assert result.outcome == candidate["outcome"]
    assert result.reason_codes == (
        ("SOURCE_SUPPORT_ERASURE_DENIED",) if erasure else ("SOURCE_SUPPORT_MISMATCH",)
    )


def test_support_mismatch_cannot_be_declared_observed() -> None:
    candidate = _candidate()
    candidate["claim"]["support_id"] = "synthetic-other-station"
    result = assess(candidate)
    assert result.outcome == "ERROR"
    assert result.reason_codes == (
        "DECLARED_OUTCOME_MISMATCH",
        "SOURCE_SUPPORT_MISMATCH",
    )


def test_each_direct_source_must_match_claim_support() -> None:
    candidate = _candidate()
    other_source = copy.deepcopy(candidate["sources"][0])
    other_source.update(support_id="synthetic-other-station", evidence_ref="evidence:other")
    candidate["sources"].append(other_source)
    candidate["claim"]["tuple_evidence_refs"].append(other_source["evidence_ref"])
    candidate["outcome"] = "ABSTAIN"
    result = assess(candidate)
    assert result.outcome == "ABSTAIN"
    assert result.reason_codes == ("SOURCE_SUPPORT_MISMATCH",)


@pytest.mark.parametrize("case_id", ["corrected_observation", "stale_observation"])
def test_support_mismatch_preserves_correction_and_finite_precedence(case_id: str) -> None:
    candidate = _candidate(case_id)
    candidate["claim"]["support_id"] = "synthetic-other-station"
    candidate["outcome"] = "ABSTAIN"
    result = assess(candidate)
    assert result.outcome == "ABSTAIN"
    expected = ("SOURCE_SUPPORT_MISMATCH",)
    if case_id == "stale_observation":
        expected = ("OBSERVATION_STALE", "SOURCE_SUPPORT_MISMATCH")
    assert result.reason_codes == expected


def test_explicit_cross_source_derivation_preserves_different_supports() -> None:
    candidate = _candidate("derived_cross_source_stress")
    claim_support = (candidate["claim"]["support_kind"], candidate["claim"]["support_id"])
    assert all(
        (source["support_kind"], source["support_id"]) != claim_support
        for source in candidate["sources"]
    )
    result = assess(candidate)
    assert result.outcome == "DERIVED"
    assert result.reason_codes == ()


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
        candidate["outcome"] = "ERROR"
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
