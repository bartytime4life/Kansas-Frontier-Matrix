from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_all.py"
SPEC = importlib.util.spec_from_file_location(
    "kfm_catalog_validator_registry_convergence",
    MODULE_PATH,
)
assert SPEC is not None and SPEC.loader is not None
orchestrator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = orchestrator
SPEC.loader.exec_module(orchestrator)

CATALOG_VALIDATORS = {
    "catalog-closure-packet": {
        "script": "tools/validators/catalog_closure/validate_catalog_closure.py",
        "representative_path": "fixtures/data/catalog_closure_packet/valid/valid_catalog_ready.json",
    },
    "catalog-matrix-closure": {
        "script": "tools/validators/validate_catalog_matrix_closure.py",
        "representative_path": "fixtures/data/catalog_matrix/closure/valid/valid_catalog_matrix_closure.json",
    },
    "catalog-matrix-claim-closure": {
        "script": "tools/validators/validate_catalog_matrix_claim_closure.py",
        "representative_path": "fixtures/data/catalog_matrix/claim_closure/valid/valid_published.json",
    },
    "catalog-distribution-mapping-profile": {
        "script": "tools/validators/catalog_closure/validate_catalog_distribution_mapping_profile.py",
        "representative_path": "fixtures/contracts/v1/data/catalog_distribution_mapping_profile/cases.json",
    },
}


class CatalogValidatorRegistryConvergenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = orchestrator.load_registry(
            REPO_ROOT / "tools/validators/validator_registry.json",
            REPO_ROOT,
        )

    def test_catalog_validators_are_release_dry_run_and_full_only(self) -> None:
        catalog_ids = tuple(CATALOG_VALIDATORS)
        release_ids = self.registry.profiles["release-dry-run"]
        full_ids = self.registry.profiles["full"]
        focused_ids = self.registry.profiles["focused"]

        self.assertEqual(release_ids[-4:], catalog_ids)
        self.assertEqual(full_ids[-6:-2], catalog_ids)
        for validator_id, expected in CATALOG_VALIDATORS.items():
            with self.subTest(validator_id=validator_id):
                spec = self.registry.by_id[validator_id]
                self.assertEqual(spec.script, expected["script"])
                self.assertEqual(spec.args, ("--fixtures",))
                self.assertIn(validator_id, release_ids)
                self.assertIn(validator_id, full_ids)
                self.assertNotIn(validator_id, focused_ids)

    def test_changed_area_selects_each_catalog_validator(self) -> None:
        for validator_id, expected in CATALOG_VALIDATORS.items():
            with self.subTest(validator_id=validator_id):
                selected, mode = orchestrator.select_validators(
                    self.registry,
                    profile="changed-area",
                    changed_paths=(expected["representative_path"],),
                )
                self.assertEqual(mode, "changed-area")
                self.assertIn(
                    validator_id,
                    {item.validator_id for item in selected},
                )

    def test_legacy_fixture_inventory_includes_catalog_validators(self) -> None:
        from tools.validators._common import run_all as legacy_runner

        expected_scripts = {
            Path(details["script"]).name for details in CATALOG_VALIDATORS.values()
        }
        self.assertTrue(expected_scripts.issubset(set(legacy_runner.RUNNER_VALIDATORS)))


if __name__ == "__main__":
    unittest.main()
