"""Atmosphere advisory life-safety tests stay held until their subjects exist.

Planned intent (docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md): AdvisoryContext output never contains imperative life-safety language.

Its policies (advisory_no_life_safety.rego, advisory-not-alert.rego) are
default-deny scaffolds. Its schemas (advisory_context, advisory-context) define
no domain fields. Each check fails with ADVISORY_LIFE_SAFETY_NOT_IMPLEMENTED
when its subject gains content, so the real tests must land in the same change.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "ADVISORY_LIFE_SAFETY_NOT_IMPLEMENTED"
POLICIES = (
    "policy/domains/atmosphere/advisory_no_life_safety.rego",
    "policy/domains/atmosphere/advisory-not-alert.rego",
)
SCHEMAS = (
    "schemas/contracts/v1/domains/atmosphere/advisory_context.schema.json",
    "schemas/contracts/v1/domains/atmosphere/advisory-context.schema.json",
)
GENERIC_FIELDS = {"id", "spec_hash", "version"}


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


if __name__ == "__main__":
    unittest.main()
