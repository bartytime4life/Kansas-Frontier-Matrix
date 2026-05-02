import json
from kfm.air_quality.airnow.qa.run_qa import run_qa

def test_publication_denied():
    m=json.load(open('tests/fixtures/air_quality/airnow/layer5/manifests/qa_publication_manifest.json'))
    _,errs=run_qa(m,'2026-01-01T00:00:00Z')
    assert errs
