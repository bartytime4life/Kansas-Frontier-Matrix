import json
from pathlib import Path
from jsonschema import Draft202012Validator\n
ROOT = Path(__file__).resolve().parents[2]\n
def test_hydrology_alias_fixtures():
    for name in ["decision_envelope", "run_receipt", "evidence_bundle"]:
        schema = json.loads((ROOT / f"schemas/contracts/v1/domains/hydrology/{name}.schema.json").read_text())
        doc = json.loads((ROOT / f"fixtures/domains/hydrology/{name}/valid/valid_1.json").read_text())
        assert not list(Draft202012Validator(schema).iter_errors(doc))
