"""Archaeology temporal logic tests stay held until their subjects exist.

Planned intent (docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md): `source`, `observed`, `valid`, `retrieval`, `release`, and `correction` times stay distinct where material.

Its schemas (chronology_assertion, correction_notice, domain_observation)
define no domain fields. Each check fails with TEMPORAL_LOGIC_NOT_IMPLEMENTED
when its subject gains content, so the real tests must land in the same change.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "TEMPORAL_LOGIC_NOT_IMPLEMENTED"
SCHEMAS = (
    "schemas/contracts/v1/domains/archaeology/chronology_assertion.schema.json",
    "schemas/contracts/v1/domains/archaeology/correction_notice.schema.json",
    "schemas/contracts/v1/domains/archaeology/domain_observation.schema.json",
)
GENERIC_FIELDS = {"id", "spec_hash", "version"}


class HeldTests(unittest.TestCase):
    def test_schemas_still_have_no_domain_fields(self) -> None:
        for relative in SCHEMAS:
            schema = json.loads((REPO_ROOT / relative).read_text(encoding="utf-8"))
            fields = set(schema.get("properties", {})) - GENERIC_FIELDS
            self.assertEqual(fields, set(),
                             f"{REASON}: {relative} now defines {sorted(fields)}. Replace this hold "
                             "with tests that accept valid and reject invalid fixtures.")


if __name__ == "__main__":
    unittest.main()
