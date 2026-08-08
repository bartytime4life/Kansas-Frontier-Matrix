from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
VALIDATOR = ROOT / "tools/validators/domains/soil/support_type/validate_support_type_alias_map.py"
SPEC = importlib.util.spec_from_file_location("support_type_alias_validator", VALIDATOR)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SoilSupportTypeAliasMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.alias_map = MODULE.load(MODULE.ALIAS_MAP)
        cls.profile = MODULE.load(MODULE.CANONICAL_PROFILE)

    def test_alias_map_is_valid_and_inactive(self) -> None:
        self.assertEqual(MODULE.validate(self.alias_map, self.profile), [])
        self.assertEqual(self.alias_map["governance"], MODULE.FALSE_GOVERNANCE)

    def test_exact_legacy_aliases_normalize_losslessly(self) -> None:
        for alias, canonical in MODULE.EXPECTED.items():
            self.assertEqual(MODULE.normalize(alias, self.alias_map, self.profile), canonical)

    def test_canonical_tokens_pass_through_unchanged(self) -> None:
        for token in MODULE.canonical_tokens(self.profile):
            self.assertEqual(MODULE.normalize(token, self.alias_map, self.profile), token)

    def test_unknown_alias_fails_closed(self) -> None:
        self.assertIsNone(MODULE.normalize("soil_observation", self.alias_map, self.profile))
        self.assertIsNone(MODULE.normalize("satellite", self.alias_map, self.profile))

    def test_cross_class_remap_is_rejected(self) -> None:
        mutated = {**self.alias_map, "aliases": [dict(item) for item in self.alias_map["aliases"]]}
        mutated["aliases"][0]["canonical"] = "station_soil_moisture"
        self.assertIn("LOSSLESS_MAPPING_MISMATCH", MODULE.validate(mutated, self.profile))

    def test_alias_cannot_claim_authority(self) -> None:
        mutated = {**self.alias_map, "governance": {**self.alias_map["governance"], "public_use_allowed": True}}
        self.assertIn("GOVERNANCE_ESCALATION", MODULE.validate(mutated, self.profile))


if __name__ == "__main__":
    unittest.main()
