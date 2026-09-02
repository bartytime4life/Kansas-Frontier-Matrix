from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_all.py"
SPEC = importlib.util.spec_from_file_location("kfm_citation_registry_orchestrator", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
orchestrator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = orchestrator
SPEC.loader.exec_module(orchestrator)


class CitationValidationReportRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.registry = orchestrator.load_registry(
            REPO_ROOT / "tools/validators/validator_registry.json",
            REPO_ROOT,
        )

    def test_registration_is_full_only_and_uses_existing_fixture_validator(self) -> None:
        spec = self.registry.by_id["citation-validation-report"]

        self.assertEqual(
            spec.script,
            "tools/validators/citation/validate_citation_validation_report.py",
        )
        self.assertEqual(spec.args, ("--fixtures",))
        self.assertIn("citation-validation-report", self.registry.profiles["full"])
        self.assertNotIn("citation-validation-report", self.registry.profiles["focused"])
        self.assertNotIn(
            "citation-validation-report",
            self.registry.profiles["release-dry-run"],
        )
        self.assertGreater(
            self.registry.profiles["full"].index("citation-validation-report"),
            self.registry.profiles["full"].index("evidence-bundle"),
        )
        self.assertLess(
            self.registry.profiles["full"].index("citation-validation-report"),
            self.registry.profiles["full"].index("layer-manifest"),
        )

    def test_owned_surfaces_select_the_validator_in_changed_area(self) -> None:
        representative_paths = (
            ".github/workflows/citation-validation.yml",
            "contracts/evidence/citation_validation_report.md",
            "schemas/contracts/v1/evidence/citation_validation_report.schema.json",
            "fixtures/contracts/v1/evidence/citation_validation_report/valid/example.json",
            "tests/validators/test_validate_citation_validation_report.py",
            "tools/validators/citation/validate_citation_validation_report.py",
            "tools/validators/validate_citation_validation.py",
            "docs/intake/exploratory/citation-validation-report-closure-source-map.md",
            "data/receipts/generated/genrec-citation-validation-report-closure-20260810.json",
        )

        for path in representative_paths:
            with self.subTest(path=path):
                selected, mode = orchestrator.select_validators(
                    self.registry,
                    profile="changed-area",
                    changed_paths=(path,),
                )
                self.assertEqual(mode, "changed-area")
                self.assertIn(
                    "citation-validation-report",
                    {item.validator_id for item in selected},
                )

    def test_orchestrator_executes_only_the_registered_citation_validator(self) -> None:
        code, report = orchestrator.orchestrate(
            self.registry,
            repo_root=REPO_ROOT,
            profile="full",
            requested_ids=("citation-validation-report",),
        )

        self.assertEqual(code, 0)
        self.assertEqual(report["outcome"], "PASS")
        self.assertEqual(report["selected_count"], 1)
        self.assertEqual(
            report["results"][0]["validator_id"],
            "citation-validation-report",
        )


if __name__ == "__main__":
    unittest.main()
