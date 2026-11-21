"""Atmosphere AOD-as-PM2.5 denial tests stay held until their subjects exist.

Planned intent (docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md): Negative test: AOD presented as PM2.5 -> DENY.

Its policies (aod_is_not_pm25.rego, aod-not-pm25.rego) are default-deny
scaffolds. Its schemas (aod_raster, pm25_observation) define no domain fields.
Its validator validate_aod_raster.py is a WORKFLOW_HOLD stub. Each check fails
with AOD_AS_PM25_DENIAL_NOT_IMPLEMENTED when its subject gains content, so the
real tests must land in the same change.
"""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "AOD_AS_PM25_DENIAL_NOT_IMPLEMENTED"
POLICIES = (
    "policy/domains/atmosphere/aod_is_not_pm25.rego",
    "policy/domains/atmosphere/aod-not-pm25.rego",
)
SCHEMAS = (
    "schemas/contracts/v1/domains/atmosphere/aod_raster.schema.json",
    "schemas/contracts/v1/domains/atmosphere/pm25_observation.schema.json",
)
GENERIC_FIELDS = {"id", "spec_hash", "version"}
STUB_VALIDATORS = (
    "tools/validators/domains/atmosphere/validate_aod_raster.py",
)


class HeldTests(unittest.TestCase):
    def test_policies_are_still_default_deny_scaffolds(self) -> None:
        for relative in POLICIES:
            lines = (REPO_ROOT / relative).read_text(encoding="utf-8").splitlines()
            rules = [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]
            self.assertTrue(rules and rules[0].startswith("package "), relative)
            self.assertEqual(rules[1:], ["default allow := false"],
                             f"{REASON}: {relative} now has rules. Replace this hold with tests that "
                             "exercise each rule on allowed and denied inputs.")

    def test_schemas_still_have_no_domain_fields(self) -> None:
        for relative in SCHEMAS:
            schema = json.loads((REPO_ROOT / relative).read_text(encoding="utf-8"))
            fields = set(schema.get("properties", {})) - GENERIC_FIELDS
            self.assertEqual(fields, set(),
                             f"{REASON}: {relative} now defines {sorted(fields)}. Replace this hold "
                             "with tests that accept valid and reject invalid fixtures.")

    def test_validators_are_still_workflow_hold_stubs(self) -> None:
        for relative in STUB_VALIDATORS:
            completed = subprocess.run([sys.executable, str(REPO_ROOT / relative)], capture_output=True,
                                       text=True, check=False, timeout=30)
            self.assertEqual(completed.returncode, 3,
                             f"{REASON}: {relative} no longer exits 3. Replace this hold with tests "
                             "that exercise the validator on accepted and rejected fixtures.")
            self.assertIn("WORKFLOW_HOLD", completed.stderr)


if __name__ == "__main__":
    unittest.main()
