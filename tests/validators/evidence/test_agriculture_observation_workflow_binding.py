from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
WORKFLOW = ROOT / ".github/workflows/agriculture-observation.yml"
COUNTY_YEAR_PANEL_TRIGGER_PATHS = {
    "contracts/data/county_year_panel.md",
    "schemas/contracts/v1/data/county_year_panel.schema.json",
    "fixtures/contracts/v1/data/county_year_panel/**",
    "tools/validators/data/validate_county_year_panel.py",
    "tests/data/test_county_year_panel.py",
}
SELF_PATH = "tests/validators/evidence/test_agriculture_observation_workflow_binding.py"


class AgricultureObservationWorkflowBindingTests(unittest.TestCase):
    def test_county_year_panel_dependency_changes_trigger_agriculture_observation(self) -> None:
        workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        triggers = workflow["on"]

        for event in ("pull_request", "push"):
            with self.subTest(event=event):
                paths = set(triggers[event]["paths"])
                self.assertTrue(
                    COUNTY_YEAR_PANEL_TRIGGER_PATHS.issubset(paths),
                    f"{event} paths must include the complete CountyYearPanel dependency seam",
                )
                self.assertIn(SELF_PATH, paths)


if __name__ == "__main__":
    unittest.main()
