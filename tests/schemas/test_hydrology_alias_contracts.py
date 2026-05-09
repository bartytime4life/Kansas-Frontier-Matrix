import json
from pathlib import Path

from tools.validators._common.jsonschema_runner import load_validator

ROOT = Path(__file__).resolve().parents[2]


def test_hydrology_alias_fixtures():
    for name in ["decision_envelope", "run_receipt", "evidence_bundle"]:
        schema_path = ROOT / f"schemas/contracts/v1/domains/hydrology/{name}.schema.json"
        doc = json.loads((ROOT / f"fixtures/domains/hydrology/{name}/valid/valid_1.json").read_text())
        validator = load_validator(schema_path)
        assert not list(validator.iter_errors(doc))


def test_hydrology_alias_rejects_unknown_top_level_properties():
    for name in ["decision_envelope", "run_receipt", "evidence_bundle"]:
        schema_path = ROOT / f"schemas/contracts/v1/domains/hydrology/{name}.schema.json"
        doc = json.loads((ROOT / f"fixtures/domains/hydrology/{name}/valid/valid_1.json").read_text())
        doc["unexpected_field"] = "should-fail"
        validator = load_validator(schema_path)
        assert list(validator.iter_errors(doc))
