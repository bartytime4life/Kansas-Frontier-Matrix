import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class SchemaWaveContractTests(unittest.TestCase):
    def test_schema_wave_files_are_draft_2020_12(self):
        schema_files = [
            "schemas/contracts/v1/source/source_descriptor.schema.json",
            "schemas/contracts/v1/data/dataset_version.schema.json",
            "schemas/contracts/v1/policy/decision_envelope.schema.json",
            "schemas/contracts/v1/release/release_manifest.schema.json",
            "schemas/contracts/v1/evidence/evidence_bundle.schema.json",
            "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json",
            "schemas/contracts/v1/common/run_receipt.schema.json",
            "schemas/contracts/v1/common/ai_receipt.schema.json",
        ]
        for rel in schema_files:
            with self.subTest(schema=rel):
                schema = load_json(ROOT / rel)
                self.assertEqual(schema.get("$schema"), "https://json-schema.org/draft/2020-12/schema")
                self.assertNotEqual(schema, {})

    def test_valid_fixtures_have_expected_shape(self):
        source = load_json(ROOT / "schemas/tests/fixtures/contracts/v1/valid/source_descriptor.min.valid.json")
        dataset = load_json(ROOT / "schemas/tests/fixtures/contracts/v1/valid/dataset_version.min.valid.json")
        release = load_json(ROOT / "schemas/tests/fixtures/contracts/v1/valid/release_manifest.min.valid.json")
        runtime = load_json(ROOT / "schemas/tests/fixtures/contracts/v1/valid/runtime_response_envelope.answer.valid.json")

        self.assertEqual(source.get("kind"), "SourceDescriptor")
        self.assertEqual(dataset.get("stage"), "PROCESSED")
        self.assertIn("run_receipt_ref", release)
        self.assertEqual(runtime.get("outcome"), "ANSWER")

    def test_invalid_fixtures_express_negative_cases(self):
        runtime_invalid = load_json(ROOT / "schemas/tests/fixtures/contracts/v1/invalid/runtime_response_envelope.invalid_outcome.invalid.json")
        release_invalid = load_json(ROOT / "schemas/tests/fixtures/contracts/v1/invalid/release_manifest.missing_run_receipt.invalid.json")
        ai_invalid = load_json(ROOT / "schemas/tests/fixtures/contracts/v1/invalid/ai_receipt.missing_model_ref.invalid.json")

        self.assertNotIn(runtime_invalid.get("outcome"), ["ANSWER", "ABSTAIN", "DENY", "ERROR"])
        self.assertNotIn("run_receipt_ref", release_invalid)
        self.assertNotIn("model_ref", ai_invalid)


if __name__ == "__main__":
    unittest.main()
