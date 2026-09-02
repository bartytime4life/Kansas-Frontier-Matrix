import json
from pathlib import Path
from jsonschema import Draft202012Validator

SCHEMA=Path('schemas/contracts/v1/domains/soil/catalog_closure_assessment.schema.json')
CASES=Path('fixtures/contracts/v1/domains/soil/catalog_closure_assessment/cases.json')

def test_schema_is_valid(): Draft202012Validator.check_schema(json.loads(SCHEMA.read_text()))
def test_positive_candidates_match_schema():
    validator=Draft202012Validator(json.loads(SCHEMA.read_text()))
    for case in json.loads(CASES.read_text())['cases'][:3]:
        assert not list(validator.iter_errors(case['candidate'])), case['name']
