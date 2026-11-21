"""Archaeology source-role anti-collapse tests stay held until a source-role check exists.

Planned intent (docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md): Source descriptor + source-role validation for archaeology sources; source-role anti-collapse (Atlas §24.1 / §24.9).

Source-descriptor validation itself is already tested:
tools/validators/domains/archaeology/validate_source_descriptor.py checks the
shared SourceDescriptor schema and archaeology domain_scope membership, and
tests/validators/domains/archaeology/test_archaeology_source_descriptor_validator_entrypoint.py
covers both. What is not built is the archaeology-specific source-role check
that keeps one source role from collapsing into another. The validator does not
mention source roles, and no archaeology source-role policy exists. Either
changing fails this hold with SOURCE_ROLE_ANTI_COLLAPSE_NOT_IMPLEMENTED, so the
anti-collapse tests must land in the same change.
"""
from __future__ import annotations

import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "SOURCE_ROLE_ANTI_COLLAPSE_NOT_IMPLEMENTED"
VALIDATOR = "tools/validators/domains/archaeology/validate_source_descriptor.py"
DESCRIPTOR_TEST = "tests/validators/domains/archaeology/test_archaeology_source_descriptor_validator_entrypoint.py"
POLICY_ROOT = "policy/domains/archaeology"


class HeldTests(unittest.TestCase):
    def test_descriptor_validation_is_tested_elsewhere(self) -> None:
        self.assertTrue((REPO_ROOT / DESCRIPTOR_TEST).is_file(), f"{DESCRIPTOR_TEST} moved or was removed")
        self.assertIn("validate_source_descriptor", (REPO_ROOT / DESCRIPTOR_TEST).read_text(encoding="utf-8"))

    def test_validator_still_has_no_source_role_check(self) -> None:
        text = (REPO_ROOT / VALIDATOR).read_text(encoding="utf-8")
        self.assertNotIn("source_role", text,
                         f"{REASON}: {VALIDATOR} now checks source roles. Replace this hold with tests "
                         "that reject each collapsed source-role combination.")

    def test_no_archaeology_source_role_policy_exists(self) -> None:
        policies = sorted(path.name for path in (REPO_ROOT / POLICY_ROOT).glob("*source_role*.rego"))
        self.assertEqual(policies, [],
                         f"{REASON}: {POLICY_ROOT} now has {policies}. Replace this hold with tests that "
                         "exercise each rule on allowed and denied inputs.")


if __name__ == "__main__":
    unittest.main()
