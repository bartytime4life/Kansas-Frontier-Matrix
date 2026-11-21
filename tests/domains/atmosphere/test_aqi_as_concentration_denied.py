"""Atmosphere AQI-as-concentration denial tests stay held until their subjects exist.

Planned intent (docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md): Negative test: AQI presented as concentration -> DENY.

Its policies (aqi_is_not_concentration.rego) are default-deny scaffolds. Its
schemas (parameter_registry) define no domain fields. Its validator
validate_parameter_units.py is a WORKFLOW_HOLD stub. Each check fails with
AQI_AS_CONCENTRATION_DENIAL_NOT_IMPLEMENTED when its subject gains content, so
the real tests must land in the same change.
"""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "AQI_AS_CONCENTRATION_DENIAL_NOT_IMPLEMENTED"
POLICIES = (
    "policy/domains/atmosphere/aqi_is_not_concentration.rego",
)
SCHEMAS = (
    "schemas/contracts/v1/domains/atmosphere/parameter_registry.schema.json",
)
GENERIC_FIELDS = {"id", "spec_hash", "version"}
STUB_VALIDATORS = (
    "tools/validators/domains/atmosphere/validate_parameter_units.py",
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
