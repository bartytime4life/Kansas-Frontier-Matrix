import json
from pathlib import Path
from tools.validators.domains.soil.validate_catalog_closure_assessment import derive, expected_id

CASES=Path('fixtures/contracts/v1/domains/soil/catalog_closure_assessment/cases.json')

def cases(): return json.loads(CASES.read_text())['cases']

def test_fixture_polarity():
    for case in cases(): assert derive(case['candidate']) == case['expected'], case['name']

def test_ready_identity_is_deterministic():
    c=cases()[0]['candidate']; assert c['assessment_id'] == expected_id(c)

def test_unresolved_dimension_holds(): assert derive(cases()[1]['candidate']) == 'HOLD'
def test_denied_rights_holds(): assert derive(cases()[2]['candidate']) == 'HOLD'
def test_authority_overreach_errors(): assert derive(cases()[3]['candidate']) == 'ERROR'
