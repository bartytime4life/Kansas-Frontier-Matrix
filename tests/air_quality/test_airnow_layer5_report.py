import json
from kfm.air_quality.airnow.qa.run_qa import run_qa

def test_report_has_internal_only_language():
    m=json.load(open('tests/fixtures/air_quality/airnow/layer5/manifests/qa_valid_manifest.json'))
    out,_=run_qa(m,'2026-01-01T00:00:00Z')
    assert 'Internal QA only' in out['qa_report']
    assert 'latitude' not in out['qa_report'].lower()
