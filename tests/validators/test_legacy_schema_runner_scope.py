from __future__ import annotations

import contextlib
import io
import unittest
from unittest import mock

from tools.validators._common import run_all as legacy_runner


class LegacySchemaRunnerScopeTests(unittest.TestCase):
    def test_main_selects_only_reviewed_legacy_core_validators(self) -> None:
        sentinel_registry = object()
        report = {
            "outcome": "PASS",
            "selection": {
                "mode": "explicit",
                "requested_validator_ids": list(
                    legacy_runner.LEGACY_CORE_VALIDATOR_IDS
                ),
            },
        }

        with (
            mock.patch.object(
                legacy_runner,
                "load_registry",
                return_value=sentinel_registry,
            ) as load_registry,
            mock.patch.object(
                legacy_runner,
                "orchestrate",
                return_value=(0, report),
            ) as orchestrate,
            contextlib.redirect_stdout(io.StringIO()) as stdout,
        ):
            code = legacy_runner.main()

        self.assertEqual(code, 0)
        load_registry.assert_called_once_with(
            legacy_runner.REGISTRY_PATH,
            legacy_runner.REPO_ROOT,
        )
        orchestrate.assert_called_once_with(
            sentinel_registry,
            repo_root=legacy_runner.REPO_ROOT,
            profile="full",
            requested_ids=legacy_runner.LEGACY_CORE_VALIDATOR_IDS,
        )
        rendered = stdout.getvalue()
        self.assertIn('"mode": "explicit"', rendered)
        self.assertNotIn("repository-topology", rendered)
        self.assertNotIn("workflow-security", rendered)
        self.assertNotIn("catalog-closure-packet", rendered)

    def test_live_full_profile_keeps_non_legacy_validators_separate(self) -> None:
        registry = legacy_runner.load_registry(
            legacy_runner.REGISTRY_PATH,
            legacy_runner.REPO_ROOT,
        )
        full_ids = registry.profiles["full"]
        legacy_ids = legacy_runner.LEGACY_CORE_VALIDATOR_IDS

        self.assertEqual(len(legacy_ids), 9)
        self.assertTrue(set(legacy_ids).issubset(set(full_ids)))
        self.assertIn("catalog-closure-packet", full_ids)
        self.assertIn("catalog-matrix-closure", full_ids)
        self.assertIn("catalog-matrix-claim-closure", full_ids)
        self.assertIn("catalog-distribution-mapping-profile", full_ids)
        self.assertIn("workflow-security", full_ids)
        self.assertIn("repository-topology", full_ids)
        self.assertNotIn("workflow-security", legacy_ids)
        self.assertNotIn("repository-topology", legacy_ids)


if __name__ == "__main__":
    unittest.main()
