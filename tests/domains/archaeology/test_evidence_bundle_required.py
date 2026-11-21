"""Archaeology EvidenceBundle requirement tests stay held until their subjects exist.

Planned intent (docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md): Every claim-bearing artifact must resolve to an `EvidenceBundle`.

Its schemas (evidence_bundle) define no domain fields. data/proofs/archaeology
holds only README files. Each check fails with
EVIDENCE_BUNDLE_REQUIRED_NOT_IMPLEMENTED when its subject gains content, so the
real tests must land in the same change.

Shape validation of shared EvidenceBundle fixtures through
tools/validators/domains/archaeology/validate_evidence_bundle.py is already
tested in tests/validators/domains/archaeology/test_archaeology_evidence_bundle_validator_entrypoint.py.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "EVIDENCE_BUNDLE_REQUIRED_NOT_IMPLEMENTED"
SCHEMAS = (
    "schemas/contracts/v1/domains/archaeology/evidence_bundle.schema.json",
)
GENERIC_FIELDS = {"id", "spec_hash", "version"}
DIRECTORIES = (
    "data/proofs/archaeology",
)


class HeldTests(unittest.TestCase):
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
