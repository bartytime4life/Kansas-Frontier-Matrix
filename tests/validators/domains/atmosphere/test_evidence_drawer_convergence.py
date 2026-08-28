from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
DOMAIN_SCHEMA = (
    ROOT
    / "schemas/contracts/v1/domains/atmosphere/evidence_drawer_payload.schema.json"
)
UI_SCHEMA = ROOT / "schemas/contracts/v1/ui/evidence_drawer_payload.schema.json"
DOMAIN_COMPONENT = (
    ROOT / "apps/explorer-web/src/features/domains/atmosphere/EvidenceDrawer.tsx"
)


class AtmosphereEvidenceDrawerConvergenceTests(unittest.TestCase):
    def test_domain_schema_is_a_field_free_shared_projection(self) -> None:
        schema = json.loads(DOMAIN_SCHEMA.read_text(encoding="utf-8"))

        self.assertEqual(schema["$ref"], "../../ui/evidence_drawer_payload.schema.json")
        self.assertEqual(schema["x-kfm"]["authority"], "projection")
        self.assertEqual(
            schema["x-kfm"]["contract_doc"],
            "contracts/ui/evidence_drawer_payload.md",
        )
        self.assertEqual(
            schema["x-kfm"]["canonical_renderer"],
            "apps/explorer-web/src/features/evidence_drawer/index.tsx",
        )
        self.assertFalse(schema["x-kfm"]["public_release_authority"])
        self.assertNotIn("properties", schema)
        self.assertNotIn("required", schema)
        self.assertNotIn("additionalProperties", schema)

    def test_shared_payload_remains_closed_and_finite(self) -> None:
        schema = json.loads(UI_SCHEMA.read_text(encoding="utf-8"))

        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            schema["properties"]["outcome"]["enum"],
            ["ANSWER", "ABSTAIN", "DENY", "ERROR"],
        )
        self.assertEqual(
            schema["properties"]["profile"]["const"],
            "kfm.explorer.evidence-drawer.public-safe.v1",
        )

    def test_domain_component_delegates_without_transport_or_parallel_renderer(self) -> None:
        source = DOMAIN_COMPONENT.read_text(encoding="utf-8")

        self.assertIn('from "../../evidence_drawer"', source)
        self.assertIn("mountEvidenceDrawer", source)
        self.assertIn("resolveEvidenceDrawer", source)
        self.assertNotIn("placeholder", source)
        self.assertNotIn("fetch(", source)


if __name__ == "__main__":
    unittest.main()
