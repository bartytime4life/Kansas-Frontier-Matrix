"""The schema-less soil candidate gates enforce their closed schemas and literal-false effects.

Each of these workflows runs only its validator, never the schema, so a field the schema
forbids (for example an injected authority flag) must still be refused, at any depth. Every case starts
from the validator's own PASS fixture and recomputes its content identity, so the only
defect is the one under test.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
# validator name -> id prefix of its content-bound identity
VALIDATORS = {
    "soil_component": "soil-component",
    "soil_map_unit": "soil-map-unit",
    "component_horizon_join": "soil-component-horizon-join",
    "domain_feature_identity": "soil-identity",
    "domain_layer_descriptor": "soil-layer",
    "domain_observation": "soil-observation",
    "domain_validation_report": "soil-validation",
}


def load(name):
    spec = importlib.util.spec_from_file_location(f"soil_{name}_closed_shape", ROOT / f"tools/validators/domains/soil/validate_{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def closed_objects(value, schema, path=()):
    """Paths, within one valid candidate, of every nested object its schema closes."""
    found = []
    if isinstance(value, dict) and isinstance(schema.get("properties"), dict):
        if path and schema.get("additionalProperties") is False:
            found.append(path)
        for key, subschema in schema["properties"].items():
            if key in value:
                found += closed_objects(value[key], subschema, (*path, key))
    if isinstance(value, list) and isinstance(schema.get("items"), dict):
        for index, item in enumerate(value):
            found += closed_objects(item, schema["items"], (*path, index))
    return found


def at(candidate, path):
    for step in path:
        candidate = candidate[step]
    return candidate


def rebound(module, prefix, candidate):
    """Recompute spec_hash and id so the candidate's identity matches its content."""
    if hasattr(module, "expected_identity"):
        candidate["spec_hash"], candidate["id"] = module.expected_identity(candidate)
    else:
        digest = module.canonical_hash(candidate)
        candidate["spec_hash"], candidate["id"] = f"sha256:{digest}", f"{prefix}:{digest[:24]}"
    return candidate


class SoilCandidateClosedShapeTests(unittest.TestCase):
    def cases(self):
        for name, prefix in VALIDATORS.items():
            module = load(name)
            rows = json.loads(Path(module.CASES).read_text(encoding="utf-8"))["cases"]
            # Every valid fixture, so nested objects that only some carry (such as report findings) are covered.
            for row in rows:
                if row["expected_outcome"] == "PASS":
                    yield f"{name}:{row['name']}", prefix, module, row["candidate"]

    def evaluate(self, module, prefix, valid, change):
        candidate = copy.deepcopy(valid)
        change(candidate)
        return module.evaluate(rebound(module, prefix, candidate))

    def test_valid_fixtures_satisfy_the_closed_schema(self):
        for name, _prefix, module, valid in self.cases():
            with self.subTest(name):
                self.assertIs(module.SCHEMA_DOC["additionalProperties"], False)
                self.assertEqual(set(module.SCHEMA_DOC["required"]), set(module.SCHEMA_DOC["properties"]))
                self.assertEqual(module.closed_shape_violations(valid, module.SCHEMA_DOC), [])

    def test_rebound_control_still_passes(self):
        for name, prefix, module, valid in self.cases():
            with self.subTest(name):
                self.assertEqual(self.evaluate(module, prefix, valid, lambda c: None), ("PASS", []))

    def test_injected_or_missing_fields_are_refused(self):
        changes = {
            "injected authority flag": lambda c: c.update(release_authorized=True),
            "injected approver": lambda c: c.update(approved_by="alice"),
            "missing field": lambda c: c.pop(next(k for k in c if k not in {"id", "spec_hash", "profile", "status"})),
        }
        for name, prefix, module, valid in self.cases():
            for label, change in changes.items():
                with self.subTest(validator=name, case=label):
                    outcome, findings = self.evaluate(module, prefix, valid, change)
                    self.assertEqual(outcome, "ERROR")
                    self.assertIn("FIELD_SET_INVALID", findings)

    def test_nested_closed_objects_refuse_injected_or_missing_fields(self):
        checked = set()
        for name, prefix, module, valid in self.cases():
            nested = closed_objects(valid, module.SCHEMA_DOC)
            self.assertTrue(nested, name)
            for path in nested:
                checked.add(path[0])
                cases = {"injected": lambda c, p=path: at(c, p).update(release_authorized=True),
                         "missing": lambda c, p=path: at(c, p).pop(next(iter(at(c, p))))}
                for label, change in cases.items():
                    with self.subTest(validator=name, path=path, case=label):
                        outcome, findings = self.evaluate(module, prefix, valid, change)
                        self.assertIn("FIELD_SET_INVALID", findings)
                        # Tampered effects are also an EFFECT_OVERCLAIM, which the domain_* gates rank as DENY.
                        self.assertIn(outcome, {"ERROR", "DENY"} if path[0] == "effects" else {"ERROR"})
        # The nested objects named in review: every one is exercised by some validator.
        self.assertLessEqual({"temporal_scope", "source_native_keys", "temporal_support", "findings", "effects"}, checked)

    def test_effects_must_be_literal_false(self):
        for name, prefix, module, valid in self.cases():
            first = next(iter(valid["effects"]))
            for value in (0, 0.0):
                with self.subTest(validator=name, value=value):
                    outcome, findings = self.evaluate(module, prefix, valid,
                                                      lambda c, key=first, zero=value: c["effects"].update({key: zero}))
                    self.assertEqual(outcome, "DENY")
                    self.assertEqual(findings, ["EFFECT_OVERCLAIM"])


if __name__ == "__main__":
    unittest.main()
