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
CI_BOOTSTRAP_TRIGGER_PATHS = {
    "tools/ci/install_python_ci.py",
    "tools/ci/python-test.lock",
    "pyproject.toml",
}
GENERATED_RECEIPT_VALIDATION_TRIGGER_PATHS = {
    "tools/validators/validate_generated_receipt.py",
    "tools/validators/_common/local_resolver.py",
    "schemas/contracts/v1/**",
    "tools/ci/python-dependency-lock-migration.json",
}
ADJACENT_OBSERVATION_TRIGGER_PATHS = {
    "contracts/evidence/population_observation.md",
    "schemas/contracts/v1/evidence/population_observation.schema.json",
    "fixtures/contracts/v1/evidence/population_observation/**",
    "tools/validators/evidence/validate_population_observation.py",
    "tests/validators/evidence/test_validate_population_observation.py",
    "contracts/evidence/economic_observation.md",
    "schemas/contracts/v1/evidence/economic_observation.schema.json",
    "fixtures/contracts/v1/evidence/economic_observation/**",
    "tools/validators/evidence/validate_economic_observation.py",
    "tests/validators/evidence/test_validate_economic_observation.py",
}
SELF_PATH = "tests/validators/evidence/test_agriculture_observation_workflow_binding.py"
RECEIPT_PATH = (
    "data/receipts/generated/"
    "genrec-agriculture-observation-generated-receipt-trigger-closure-20260830.json"
)


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

    def test_ci_bootstrap_dependency_changes_trigger_agriculture_observation(self) -> None:
        workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        triggers = workflow["on"]

        for event in ("pull_request", "push"):
            with self.subTest(event=event):
                paths = set(triggers[event]["paths"])
                self.assertTrue(
                    CI_BOOTSTRAP_TRIGGER_PATHS.issubset(paths),
                    f"{event} paths must include the complete project-test CI bootstrap seam",
                )
                self.assertIn(SELF_PATH, paths)
                self.assertIn(RECEIPT_PATH, paths)

    def test_generated_receipt_validation_dependency_changes_trigger_agriculture_observation(self) -> None:
        workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        triggers = workflow["on"]

        for event in ("pull_request", "push"):
            with self.subTest(event=event):
                paths = set(triggers[event]["paths"])
                self.assertTrue(
                    GENERATED_RECEIPT_VALIDATION_TRIGGER_PATHS.issubset(paths),
                    (
                        f"{event} paths must include the generated receipt validator, "
                        "resolver-wide schema registry, and migration-ledger dependency seam"
                    ),
                )
                self.assertIn(SELF_PATH, paths)
                self.assertIn(RECEIPT_PATH, paths)

    def test_adjacent_observation_dependency_changes_trigger_agriculture_observation(self) -> None:
        workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        triggers = workflow["on"]

        for event in ("pull_request", "push"):
            with self.subTest(event=event):
                paths = set(triggers[event]["paths"])
                self.assertTrue(
                    ADJACENT_OBSERVATION_TRIGGER_PATHS.issubset(paths),
                    (
                        f"{event} paths must include the PopulationObservation and "
                        "EconomicObservation dependency seams executed by AgricultureObservation"
                    ),
                )
                self.assertIn(SELF_PATH, paths)
                self.assertIn(RECEIPT_PATH, paths)


if __name__ == "__main__":
    unittest.main()
