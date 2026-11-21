"""Flora rights and source-role tests stay held until their subjects exist.

Planned intent (docs/domains/flora/MISSING_OR_PLANNED_FILES.md): Source-rights and source-role gates.

Its policies (flora_rights.rego, flora_source_role.rego, rights.rego,
source_role.rego) are default-deny scaffolds.
packages/domains/flora/source_role_resolver holds only README files. Each check
fails with RIGHTS_VALIDATORS_NOT_IMPLEMENTED when its subject gains content, so
the real tests must land in the same change.

Intake licence classification is already tested in
tests/packages/domains/flora/normalizers/test_intake_governance.py.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "RIGHTS_VALIDATORS_NOT_IMPLEMENTED"
POLICIES = (
    "policy/domains/flora/flora_rights.rego",
    "policy/domains/flora/flora_source_role.rego",
    "policy/domains/flora/rights.rego",
    "policy/domains/flora/source_role.rego",
)
DIRECTORIES = (
    "packages/domains/flora/source_role_resolver",
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

    def test_directories_still_hold_only_readmes(self) -> None:
        for relative in DIRECTORIES:
            base = REPO_ROOT / relative
            self.assertTrue(base.is_dir(), f"{REASON}: {relative} moved; point this hold at its new home.")
            content = sorted(
                path.relative_to(REPO_ROOT).as_posix()
                for path in base.rglob("*")
                if path.is_file() and path.suffix != ".md" and path.name != ".gitkeep"
                and "__pycache__" not in path.parts
            )
            self.assertEqual(content, [], f"{REASON}: {relative} now holds {content}. Replace this hold "
                             "with tests for that content.")


if __name__ == "__main__":
    unittest.main()
