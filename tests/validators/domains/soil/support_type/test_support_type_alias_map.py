from __future__ import annotations

import copy
import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

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

    def mutated(self, change):
        """The tracked map with one change, so a finding can only come from that change."""
        alias_map = copy.deepcopy(self.alias_map)
        change(alias_map)
        return MODULE.validate(alias_map, self.profile)

    def test_closed_shape_and_literal_false_governance(self) -> None:
        cases = {
            "governance flag is 0": (lambda m: m["governance"].update(release_authorized=0), "GOVERNANCE_ESCALATION"),
            "governance flag is 0.0": (lambda m: m["governance"].update(public_use_allowed=0.0), "GOVERNANCE_ESCALATION"),
            "governance flag missing": (lambda m: m["governance"].pop("policy_evaluated"), "GOVERNANCE_ESCALATION"),
            "governance extra flag": (lambda m: m["governance"].update(approved_by=False), "GOVERNANCE_ESCALATION"),
            "governance not an object": (lambda m: m.update(governance=[]), "GOVERNANCE_ESCALATION"),
            "extra top-level key": (lambda m: m.update(activated_by="alice"), "UNEXPECTED_FIELDS"),
            "top-level key missing": (lambda m: m.pop("schema_version"), "UNEXPECTED_FIELDS"),
            "alias carries authority": (lambda m: m["aliases"][0].update(public_use_allowed=True),
                                        "UNEXPECTED_ALIAS_FIELDS:interpretation"),
            "canonical not a string": (lambda m: m["aliases"][0].update(canonical=["soil_interpretation"]),
                                       "UNKNOWN_CANONICAL:['soil_interpretation']"),
            "class_preserved is 1": (lambda m: m["aliases"][0].update(class_preserved=1), "CLASS_NOT_PRESERVED:interpretation"),
        }
        for name, (change, finding) in cases.items():
            with self.subTest(name):
                self.assertIn(finding, self.mutated(change))

    def test_identity_and_alias_findings(self) -> None:
        cases = {
            "object type": (lambda m: m.update(object_type="Other"), "BAD_OBJECT_TYPE"),
            "schema version": (lambda m: m.update(schema_version="2.0.0"), "BAD_SCHEMA_VERSION"),
            "status activated": (lambda m: m.update(status="ACTIVE"), "BAD_STATUS"),
            "canonical profile": (lambda m: m.update(canonical_profile="elsewhere.json"), "BAD_CANONICAL_PROFILE"),
            "aliases not an array": (lambda m: m.update(aliases={}), "ALIASES_NOT_ARRAY"),
            "alias order": (lambda m: m["aliases"].reverse(), "ALIAS_SET_OR_ORDER_MISMATCH"),
            "non-object entry": (lambda m: m["aliases"].append("pedon"), "BAD_ALIAS_ENTRY"),
            "unknown canonical": (lambda m: m["aliases"][1].update(canonical="pedon"), "UNKNOWN_CANONICAL:pedon"),
        }
        for name, (change, finding) in cases.items():
            with self.subTest(name):
                self.assertIn(finding, self.mutated(change))
        shadowing = copy.deepcopy(self.profile)
        shadowing["support_types"].append({**shadowing["support_types"][0], "support_type": "interpretation"})
        self.assertIn("ALIAS_SHADOWS_CANONICAL:interpretation", MODULE.validate(self.alias_map, shadowing))

    def run_cli(self, *argv: str) -> tuple[int, str]:
        out = io.StringIO()
        code = 0
        with patch("sys.argv", ["validator", *argv]), redirect_stdout(out):
            try:
                MODULE.main()
            except SystemExit as exit_:
                code = exit_.code
        return code, out.getvalue()

    def test_cli_validates_and_normalizes(self) -> None:
        self.assertEqual(self.run_cli(), (0, "PASS support_type_alias_map canonical=8 aliases=3 no_network=true authority=compatibility_only\n"))
        self.assertEqual(self.run_cli("--token", "pedon_evidence"), (0, "profile_soil_evidence\n"))
        self.assertEqual(self.run_cli("--token", "soil_observation"), (2, "DENY_UNKNOWN_SUPPORT_TYPE\n"))
        broken = {**self.alias_map, "status": "ACTIVE"}
        with patch.object(MODULE, "load", side_effect=[broken, self.profile]):
            self.assertEqual(self.run_cli(), (1, "BAD_STATUS\n"))


if __name__ == "__main__":
    unittest.main()
