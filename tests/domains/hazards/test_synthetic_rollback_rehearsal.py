from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HELPER = ROOT / "tools/release/rollback_apply.py"
FIXTURE = ROOT / "fixtures/domains/hazards/synthetic_rollback_rehearsal"
SPEC = importlib.util.spec_from_file_location("hazards_rollback_apply", HELPER)
assert SPEC and SPEC.loader
rollback = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rollback
SPEC.loader.exec_module(rollback)


def read_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object: {path}")
    return value


def emit(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )


def timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def snapshot(root: Path) -> dict[str, bytes]:
    return {
        str(path.relative_to(root)): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


class HazardsSyntheticRollbackRehearsalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "workspace"
        shutil.copytree(FIXTURE / "workspace", self.root)
        self.scenario = read_object(self.root / "scenario.json")
        self.affected = self._carrier(self.scenario["affected_release_id"])
        self.target = self._carrier(self.scenario["target_release_id"])

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _carrier_path(self, release_id: str) -> Path:
        return self.root / "releases" / release_id / "hazards-context.json"

    def _carrier(self, release_id: str) -> dict:
        return read_object(self._carrier_path(release_id))

    def assert_bounded_hazards_carrier(self, carrier: dict) -> None:
        self.assertEqual(
            carrier["schema"],
            "kfm.synthetic_hazards_planning_context.v1",
        )
        self.assertEqual(carrier["domain"], "hazards")
        self.assertEqual(carrier["context_kind"], "PLANNING_ONLY")
        self.assertEqual(carrier["source_role"], "synthetic")
        self.assertIs(carrier["synthetic"], True)
        self.assertIs(carrier["not_for_life_safety"], True)
        self.assertIs(carrier["public_use_allowed"], False)
        self.assertIs(carrier["released"], False)
        self.assertIs(carrier["published"], False)
        self.assertEqual(carrier["geography"], "NON_LOCATING_SYNTHETIC_AREA")
        self.assertLess(
            timestamp(carrier["valid_until"]),
            timestamp(carrier["evaluated_at"]),
        )

    def test_plan_is_deterministic_bounded_and_no_write(self) -> None:
        self.assert_bounded_hazards_carrier(self.affected)
        self.assert_bounded_hazards_carrier(self.target)
        self.assertEqual(self.affected["freshness_state"], "CURRENT")
        self.assertEqual(
            self.affected["fixture_defect"],
            "STALE_CONTEXT_MISLABELED_CURRENT",
        )
        self.assertEqual(self.target["freshness_state"], "WITHHELD_STALE")
        self.assertIsNone(self.target["fixture_defect"])

        before = snapshot(self.root)
        first = rollback.rehearse(self.root, self.scenario)
        second = rollback.rehearse(self.root, self.scenario)

        self.assertEqual(first, second)
        self.assertEqual(first["outcome"], "PASS")
        self.assertEqual(first["mode"], "PLAN")
        self.assertEqual(first["operation"], "ROLLBACK")
        self.assertEqual(before, snapshot(self.root))
        self.assertEqual(
            first["after"]["current_alias"]["release_id"],
            "hazards-synthetic-planning-context-v1",
        )
        self.assertEqual(
            first["governance"],
            {
                "authority_created": False,
                "policy_evaluated": False,
                "publication_authorized": False,
                "public_state_mutated": False,
                "release_authorized": False,
                "review_completed": False,
                "synthetic_workspace_only": True,
            },
        )

    def test_apply_withholds_stale_context_and_preserves_releases(self) -> None:
        releases = snapshot(self.root / "releases")
        report = rollback.rehearse(self.root, self.scenario, apply=True)

        alias = read_object(self.root / "published/current.json")
        correction = read_object(
            self.root
            / "corrections/hazards-synthetic-stale-context-correction-001.json"
        )
        invalidation = read_object(
            self.root
            / "invalidations/hazards-synthetic-stale-context-rollback-001.json"
        )

        self.assertEqual(report["outcome"], "PASS")
        self.assertEqual(report["mode"], "APPLY")
        self.assertEqual(alias["release_id"], self.scenario["target_release_id"])
        self.assertEqual(
            correction["reason_code"],
            "SYNTHETIC_STALE_CONTEXT_MISLABELED",
        )
        self.assertEqual(
            invalidation["invalidations"],
            list(rollback.INVALIDATIONS),
        )
        self.assertEqual(releases, snapshot(self.root / "releases"))
        self.assertEqual(
            self._carrier(alias["release_id"])["freshness_state"],
            "WITHHELD_STALE",
        )
        self.assertIs(report["governance"]["public_state_mutated"], False)

    def test_tampered_hazards_carrier_fails_closed_before_apply(self) -> None:
        alias_before = (self.root / "published/current.json").read_bytes()
        self.affected["public_use_allowed"] = True
        emit(
            self._carrier_path(self.scenario["affected_release_id"]),
            self.affected,
        )

        with self.assertRaises(rollback.RehearsalError) as caught:
            rollback.rehearse(self.root, self.scenario, apply=True)

        self.assertEqual(caught.exception.code, "ARTIFACT_DIGEST_MISMATCH")
        self.assertEqual(
            alias_before,
            (self.root / "published/current.json").read_bytes(),
        )
        self.assertFalse((self.root / "corrections").exists())
        self.assertFalse((self.root / "invalidations").exists())

    def test_non_synthetic_scenario_fails_closed_before_apply(self) -> None:
        alias_before = (self.root / "published/current.json").read_bytes()
        self.scenario["synthetic"] = False

        with self.assertRaises(rollback.RehearsalError) as caught:
            rollback.rehearse(self.root, self.scenario, apply=True)

        self.assertEqual(caught.exception.code, "NON_SYNTHETIC_INPUT_DENIED")
        self.assertEqual(
            alias_before,
            (self.root / "published/current.json").read_bytes(),
        )
        self.assertFalse((self.root / "corrections").exists())
        self.assertFalse((self.root / "invalidations").exists())


if __name__ == "__main__":
    unittest.main()
