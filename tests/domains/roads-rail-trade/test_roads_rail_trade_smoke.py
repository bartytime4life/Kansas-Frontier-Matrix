"""Deterministic, no-network smoke checks for the Roads/Rail/Trade domain lane.

Runs the domain's shared validator entrypoints in their fixture modes and
checks source-descriptor fixture polarity and strict JSON parsing of every
committed domain fixture. Passing proves only that these bounded validators
and fixtures agree at this revision; it grants no admission, policy, release,
or publication authority.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

DOMAIN = "roads-rail-trade"
REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATORS = REPO_ROOT / "tools" / "validators" / "domains" / DOMAIN
FIXTURES = REPO_ROOT / "fixtures" / "domains" / DOMAIN
SCHEMAS = REPO_ROOT / "schemas" / "contracts" / "v1" / "domains" / DOMAIN
ENV = {**os.environ, "KFM_NO_NETWORK": "1", "PYTHONHASHSEED": "0",
       "PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"}


def run_validator(name: str, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(VALIDATORS / name), *arguments],
                          cwd=REPO_ROOT, env=ENV, capture_output=True, text=True,
                          timeout=120, check=False)


def _strict_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key {key!r}")
        result[key] = value
    return result


def _reject_constant(token: str) -> None:
    raise ValueError(f"non-standard JSON number {token}")


class RoadsRailTradeSmokeTests(unittest.TestCase):
    def assert_exit(self, completed: subprocess.CompletedProcess[str], code: int) -> None:
        self.assertEqual(completed.returncode, code, completed.stdout + completed.stderr)

    def test_lane_surfaces_exist(self) -> None:
        for path in (VALIDATORS, FIXTURES, SCHEMAS):
            self.assertTrue(path.is_dir(), path)
        self.assertTrue(any(SCHEMAS.glob("*.schema.json")))

    def test_schema_validator_passes(self) -> None:
        self.assert_exit(run_validator("validate_schema.py", *()), 0)

    def test_fixture_modes_pass(self) -> None:
        for name in ("validate_source_descriptor.py", "validate_evidence_bundle.py",
                     "validate_catalog_matrix.py"):
            with self.subTest(validator=name):
                self.assert_exit(run_validator(name, "--fixtures"), 0)

    def test_source_descriptor_fixture_polarity(self) -> None:
        valid = sorted((FIXTURES / "source_descriptor" / "valid").glob("*.json"))
        invalid = sorted((FIXTURES / "source_descriptor" / "invalid").glob("*.json"))
        self.assertTrue(valid and invalid, "both polarities need at least one fixture")
        for path in valid:
            with self.subTest(valid=path.name):
                self.assert_exit(run_validator("validate_source_descriptor.py", str(path)), 0)
        for path in invalid:
            with self.subTest(invalid=path.name):
                self.assert_exit(run_validator("validate_source_descriptor.py", str(path)), 1)

    def test_fixtures_are_strict_json(self) -> None:
        paths = sorted(FIXTURES.rglob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(fixture=path.relative_to(FIXTURES).as_posix()):
                json.loads(path.read_text(encoding="utf-8"),
                           object_pairs_hook=_strict_object, parse_constant=_reject_constant)


if __name__ == "__main__":
    unittest.main()
