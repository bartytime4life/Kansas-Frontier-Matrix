from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from tools.validators.release.validate_geoparquet_2_rc_compatibility_assessment import (
    CASES_PATH,
    assess,
    validate_cases,
)


class GeoParquet2RcCompatibilityAssessmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        value = json.loads(Path(CASES_PATH).read_text(encoding="utf-8"))
        cls.cases = {case["case_id"]: case["candidate"] for case in value["cases"]}

    def test_exact_fixture_matrix_passes(self) -> None:
        self.assertEqual(validate_cases(), 0)

    def test_ready_means_only_ready_for_byte_probes(self) -> None:
        result = assess(copy.deepcopy(self.cases["ready_synthetic_packet"]))
        self.assertEqual(result.outcome, "READY")
        self.assertEqual(result.reason_codes, ())
        self.assertTrue(all(value is False for value in self.cases["ready_synthetic_packet"]["governance"].values()))

    def test_pending_probes_hold(self) -> None:
        result = assess(copy.deepcopy(self.cases["hold_byte_probes_pending"]))
        self.assertEqual(result.outcome, "HOLD")
        self.assertEqual(result.reason_codes, ("BYTE_PROBES_PENDING",))

    def test_default_change_is_error(self) -> None:
        result = assess(copy.deepcopy(self.cases["error_default_changed"]))
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("DECLARED_DEFAULT_CHANGED", result.reason_codes)

    def test_unpinned_tool_holds(self) -> None:
        result = assess(copy.deepcopy(self.cases["hold_tool_unpinned"]))
        self.assertEqual(result.outcome, "HOLD")
        self.assertIn("TOOL_VERSION_NOT_PINNED", result.reason_codes)

    def test_governance_claim_is_error(self) -> None:
        result = assess(copy.deepcopy(self.cases["error_governance"]))
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("GOVERNANCE_BOUNDARY_VIOLATION", result.reason_codes)


if __name__ == "__main__":
    unittest.main()
