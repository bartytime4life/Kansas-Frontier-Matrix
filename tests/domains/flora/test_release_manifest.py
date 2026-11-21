"""Flora release manifest tests stay held until their subjects exist.

Planned intent (docs/domains/flora/MISSING_OR_PLANNED_FILES.md): `ReleaseManifest` validation and rollback chain.

Its policies (release_gate.rego) are default-deny scaffolds. Its schemas
(release_manifest, rollback_card) define no domain fields.
release/candidates/flora and data/proofs/flora hold only README files. Each
check fails with RELEASE_MANIFEST_NOT_IMPLEMENTED when its subject gains
content, so the real tests must land in the same change.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "RELEASE_MANIFEST_NOT_IMPLEMENTED"
POLICIES = (
    "policy/domains/flora/release_gate.rego",
)
SCHEMAS = (
    "schemas/contracts/v1/domains/flora/release_manifest.schema.json",
    "schemas/contracts/v1/domains/flora/rollback_card.schema.json",
)
GENERIC_FIELDS = {"id", "spec_hash", "version"}
DIRECTORIES = (
    "release/candidates/flora",
    "data/proofs/flora",
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
