from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
HYDROLOGY_SCHEMA = (
    ROOT / "schemas/contracts/v1/domains/hydrology/evidence_drawer_payload.schema.json"
)
UI_SCHEMA = ROOT / "schemas/contracts/v1/ui/evidence_drawer_payload.schema.json"
HYDROLOGY_COMPONENT = (
    ROOT / "apps/explorer-web/src/features/domains/hydrology/EvidenceDrawer.tsx"
)
HYDROLOGY_MAP_CONTRACT = ROOT / "docs/domains/hydrology/MAP_UI_CONTRACTS.md"


class HydrologyEvidenceDrawerConvergenceTests(unittest.TestCase):
    def test_hydrology_schema_projects_shared_ui_payload_without_parallel_shape(self) -> None:
        schema = json.loads(HYDROLOGY_SCHEMA.read_text(encoding="utf-8"))

        self.assertEqual(schema["$ref"], "../../ui/evidence_drawer_payload.schema.json")
        self.assertEqual(schema["x-kfm"]["authority"], "projection")
        self.assertEqual(
            schema["x-kfm"]["contract_doc"],
            "contracts/ui/evidence_drawer_payload.md",
        )
        self.assertFalse(schema["x-kfm"]["public_release_authority"])
        self.assertNotIn("properties", schema)
        self.assertNotIn("required", schema)
        self.assertNotIn("additionalProperties", schema)

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

    def test_hydrology_component_delegates_to_shared_renderer(self) -> None:
        source = HYDROLOGY_COMPONENT.read_text(encoding="utf-8")

        self.assertIn('from "../../evidence_drawer"', source)
        self.assertIn("mountEvidenceDrawer", source)
        self.assertIn("resolveEvidenceDrawer", source)
        self.assertNotIn("placeholder", source)
        self.assertNotIn("fetch(", source)

    def test_hydrology_docs_keep_the_payload_cross_cutting(self) -> None:
        source = HYDROLOGY_MAP_CONTRACT.read_text(encoding="utf-8")

        self.assertIn(
            "schemas/contracts/v1/ui/evidence_drawer_payload.schema.json",
            source,
        )
        self.assertIn("does **not** maintain a parallel schema home", source)


if __name__ == "__main__":
    unittest.main()
