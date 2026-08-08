from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOIL = ROOT / "schemas/contracts/v1/domains/soil"
RUNTIME = ROOT / "schemas/contracts/v1/runtime/decision_envelope.schema.json"


class SoilDecisionEnvelopeSchemaConvergenceTests(unittest.TestCase):
    def load(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_soil_projection_delegates_shape_to_runtime_schema(self) -> None:
        schema = self.load(SOIL / "decision_envelope.schema.json")
        self.assertEqual(schema["$ref"], "../../runtime/decision_envelope.schema.json")
        self.assertEqual(schema["x-kfm"]["authority"], "projection")
        self.assertFalse(schema["x-kfm"]["public_release_authority"])
        self.assertNotIn("properties", schema)
        self.assertNotIn("required", schema)

    def test_legacy_soil_schema_is_alias_only(self) -> None:
        schema = self.load(SOIL / "soil_decision_envelope.schema.json")
        self.assertEqual(schema["$ref"], "decision_envelope.schema.json")
        self.assertEqual(schema["x-kfm"]["authority"], "compatibility_alias")
        self.assertEqual(schema["x-kfm"]["direct_edits"], "DENY")
        self.assertNotIn("properties", schema)
        self.assertNotIn("required", schema)

    def test_runtime_contract_keeps_finite_closed_shape(self) -> None:
        schema = self.load(RUNTIME)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["properties"]["outcome"]["enum"], ["ANSWER", "ABSTAIN", "DENY", "ERROR"])
        self.assertEqual(
            schema["required"],
            ["decision_id", "outcome", "policy_family", "reasons", "obligations", "evaluated_at"],
        )


if __name__ == "__main__":
    unittest.main()
