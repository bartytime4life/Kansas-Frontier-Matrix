from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_all.py"
SPEC = importlib.util.spec_from_file_location(
    "kfm_western_kansas_observation_assessment_registry",
    MODULE_PATH,
)
assert SPEC is not None and SPEC.loader is not None
orchestrator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = orchestrator
SPEC.loader.exec_module(orchestrator)

VALIDATOR_ID = "western-kansas-observation-assessment"
VALIDATOR_SCRIPT = (
    "tools/validators/evidence/"
    "validate_western_kansas_observation_assessment.py"
)
REPRESENTATIVE_PATHS = (
    ".github/workflows/western-kansas-observation-assessment.yml",
    "contracts/domains/hydrology/western_kansas_observation_assessment.md",
    "schemas/contracts/v1/domains/hydrology/"
    "western_kansas_observation_assessment.schema.json",
    "fixtures/domains/hydrology/"
    "western_kansas_observation_assessment/cases.json",
    "tests/validators/test_western_kansas_observation_assessment.py",
    VALIDATOR_SCRIPT,
)


class WesternKansasObservationAssessmentRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = orchestrator.load_registry(
            REPO_ROOT / "tools/validators/validator_registry.json",
            REPO_ROOT,
        )

    def test_registration_is_full_profile_only(self) -> None:
        spec = self.registry.by_id[VALIDATOR_ID]

        self.assertEqual(spec.script, VALIDATOR_SCRIPT)
        self.assertEqual(spec.args, ("--cases",))
        self.assertIn(VALIDATOR_ID, self.registry.profiles["full"])
        self.assertNotIn(VALIDATOR_ID, self.registry.profiles["focused"])
        self.assertNotIn(
            VALIDATOR_ID,
            self.registry.profiles["release-dry-run"],
        )
        for path in REPRESENTATIVE_PATHS:
            with self.subTest(path=path):
                self.assertIn(path, spec.path_globs)

    def test_changed_area_selects_the_validator_for_its_owned_surface(self) -> None:
        for path in REPRESENTATIVE_PATHS:
            with self.subTest(path=path):
                selected, mode = orchestrator.select_validators(
                    self.registry,
                    profile="changed-area",
                    changed_paths=(path,),
                )
                self.assertEqual(mode, "changed-area")
                self.assertIn(
                    VALIDATOR_ID,
                    {item.validator_id for item in selected},
                )

    def test_explicit_orchestration_runs_the_exact_case_matrix(self) -> None:
        code, report = orchestrator.orchestrate(
            self.registry,
            repo_root=REPO_ROOT,
            profile="full",
            requested_ids=(VALIDATOR_ID,),
        )

        self.assertEqual(code, orchestrator.EXIT_PASS)
        self.assertEqual(report["outcome"], "PASS")
        self.assertEqual(report["reason_code"], "ALL_SELECTED_VALIDATORS_PASSED")
        self.assertEqual(report["selected_count"], 1)
        self.assertEqual(report["results"][0]["validator_id"], VALIDATOR_ID)
        self.assertEqual(report["results"][0]["status"], "PASS")

    def test_legacy_fixture_inventory_is_not_silently_widened(self) -> None:
        from tools.validators._common import run_all as legacy_runner

        self.assertNotIn(
            Path(VALIDATOR_SCRIPT).name,
            legacy_runner.RUNNER_VALIDATORS,
        )
        self.assertNotIn(
            VALIDATOR_ID,
            legacy_runner.LEGACY_CORE_VALIDATOR_IDS,
        )


if __name__ == "__main__":
    unittest.main()
