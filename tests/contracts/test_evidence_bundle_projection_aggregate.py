import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DOMAINS_ROOT = REPO_ROOT / "schemas" / "contracts" / "v1" / "domains"
CANONICAL_REF = "../../evidence/evidence_bundle.schema.json"
CANONICAL_SEMANTICS = "contracts/evidence/evidence_bundle.md"
CANONICAL_SHAPE = "schemas/contracts/v1/evidence/evidence_bundle.schema.json"
FORBIDDEN_SCHEMA_KEYS = {
    "type",
    "properties",
    "required",
    "additionalProperties",
    "allOf",
    "anyOf",
    "oneOf",
    "not",
    "if",
    "then",
    "else",
    "$defs",
    "dependentSchemas",
    "unevaluatedProperties",
}


class EvidenceBundleProjectionAggregateTests(unittest.TestCase):
    def projection_paths(self) -> list[Path]:
        paths = sorted(DOMAINS_ROOT.glob("*/evidence_bundle.schema.json"))
        self.assertTrue(paths, "Expected at least one domain EvidenceBundle projection")
        return paths

    def test_all_domain_projections_delegate_without_independent_schema_semantics(self) -> None:
        for path in self.projection_paths():
            with self.subTest(path=path.relative_to(REPO_ROOT).as_posix()):
                payload = json.loads(path.read_text(encoding="utf-8"))
                domain = path.parent.name
                metadata = payload.get("x-kfm")

                self.assertEqual(payload.get("$schema"), "https://json-schema.org/draft/2020-12/schema")
                self.assertEqual(payload.get("$ref"), CANONICAL_REF)
                self.assertIsInstance(metadata, dict)
                self.assertEqual(metadata.get("authority"), "projection")
                self.assertEqual(metadata.get("canonical_semantics"), CANONICAL_SEMANTICS)
                self.assertEqual(metadata.get("canonical_shape"), CANONICAL_SHAPE)
                self.assertEqual(metadata.get("domain_scope"), domain)
                self.assertEqual(metadata.get("independent_fields"), "DENY")
                self.assertIs(metadata.get("public_release_authority"), False)

                forbidden = sorted(FORBIDDEN_SCHEMA_KEYS.intersection(payload))
                self.assertEqual(
                    forbidden,
                    [],
                    f"{domain} projection must not add independent EvidenceBundle schema semantics",
                )

    def test_declared_projection_validators_exist(self) -> None:
        for path in self.projection_paths():
            with self.subTest(path=path.relative_to(REPO_ROOT).as_posix()):
                payload = json.loads(path.read_text(encoding="utf-8"))
                validator = payload.get("x-kfm", {}).get("validator")
                self.assertIsInstance(validator, str)
                self.assertTrue(validator, "Projection must declare its validator")
                validator_path = REPO_ROOT / validator
                self.assertTrue(
                    validator_path.is_file(),
                    f"Declared validator does not exist: {validator}",
                )


if __name__ == "__main__":
    unittest.main()
