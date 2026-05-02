import json
from kfm.air_quality.airnow.qa.run_qa import run_qa

def test_coverage_summary_exists():
    m=json.load(open('tests/fixtures/air_quality/airnow/layer5/manifests/qa_valid_manifest.json'))
    out,errs=run_qa(m,'2026-01-01T00:00:00Z')
    assert not errs
    assert out['coverage_summary']['object_type']=='AirNowCoverageSummary'
    assert out['coverage_summary']['linkage_ratios']['sites_with_parameters_ratio'] is not None
