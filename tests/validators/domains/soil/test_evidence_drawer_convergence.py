from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOIL_SCHEMA = ROOT / "schemas/contracts/v1/domains/soil/evidence_drawer_payload.schema.json"
UI_SCHEMA = ROOT / "schemas/contracts/v1/ui/evidence_drawer_payload.schema.json"
SOIL_COMPONENT = ROOT / "apps/explorer-web/src/features/domains/soil/EvidenceDrawer.tsx"


class SoilEvidenceDrawerConvergenceTests(unittest.TestCase):
    def test_soil_schema_projects_shared_ui_payload(self) -> None:
        schema = json.loads(SOIL_SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(schema["$ref"], "../../ui/evidence_drawer_payload.schema.json")
        self.assertEqual(schema["x-kfm"]["authority"], "projection")
        self.assertFalse(schema["x-kfm"]["public_release_authority"])
        self.assertNotIn("properties", schema)
        self.assertNotIn("required", schema)

    def test_shared_ui_payload_remains_closed_and_finite(self) -> None:
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

    def test_soil_component_delegates_to_shared_renderer(self) -> None:
        source = SOIL_COMPONENT.read_text(encoding="utf-8")
        self.assertIn('from "../../evidence_drawer"', source)
        self.assertIn("mountEvidenceDrawer", source)
        self.assertIn("resolveEvidenceDrawer", source)
        self.assertNotIn("placeholder", source)
        self.assertNotIn("fetch(", source)


if __name__ == "__main__":
    unittest.main()
