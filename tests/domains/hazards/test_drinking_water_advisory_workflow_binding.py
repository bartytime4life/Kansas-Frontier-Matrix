from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
WORKFLOW = ROOT / ".github/workflows/drinking-water-advisory.yml"
SELF_PATH = "tests/domains/hazards/test_drinking_water_advisory_workflow_binding.py"
RECEIPT_PATH = (
    "data/receipts/generated/"
    "genrec-drinking-water-advisory-receipt-trigger-closure-20260828.json"
)
DIRECT_EXECUTION_TRIGGER_PATHS = {
    "contracts/domains/hazards/drinking_water_advisory.md",
    "schemas/contracts/v1/domains/hazards/drinking_water_advisory.schema.json",
    "fixtures/domains/hazards/drinking_water_advisory/**",
    "tools/validators/domains/hazards/validate_drinking_water_advisory.py",
    "tests/domains/hazards/test_drinking_water_advisory.py",
    "contracts/common/advisory_event_envelope.md",
    "schemas/contracts/v1/common/advisory_event_envelope.schema.json",
    "fixtures/contracts/v1/common/advisory_event_envelope/**",
    "tools/validators/validate_advisory_event_envelope.py",
    "tools/validators/advisory_event_envelope_support.py",
    "tests/validators/test_validate_advisory_event_envelope.py",
    "contracts/source/source_adapter.md",
    "contracts/source/source_record_absence_assessment.md",
    "schemas/contracts/v1/source/source_record_absence_assessment.schema.json",
    "fixtures/contracts/v1/source/source_record_absence_assessment/**",
    "tools/validators/validate_source_record_absence_assessment.py",
    "tests/validators/test_validate_source_record_absence_assessment.py",
    "schemas/contracts/v1/**",
    "schemas/contracts/v1/receipts/generated_receipt.schema.json",
    "tools/validators/validate_generated_receipt.py",
    "tools/validators/_common/local_resolver.py",
    "tools/ci/install_python_ci.py",
    "tools/ci/python-dependency-lock-migration.json",
    "tools/ci/python-test.lock",
    "packages/hashing/src/hashing/**",
    "pyproject.toml",
}


class DrinkingWaterAdvisoryWorkflowBindingTests(unittest.TestCase):
    def test_direct_execution_dependencies_trigger_both_hosted_events(self) -> None:
        workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
        triggers = workflow["on"]

        for event in ("pull_request", "push"):
            with self.subTest(event=event):
                paths = set(triggers[event]["paths"])
                self.assertTrue(
                    DIRECT_EXECUTION_TRIGGER_PATHS.issubset(paths),
                    f"{event} paths must include the direct advisory execution seam",
                )
                self.assertIn(SELF_PATH, paths)
                self.assertIn(RECEIPT_PATH, paths)


if __name__ == "__main__":
    unittest.main()
