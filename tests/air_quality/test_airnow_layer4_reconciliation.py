import json
from pathlib import Path
from kfm.air_quality.airnow.reconcile.reconcile_batch import reconcile_from_manifest

def test_reconcile_outputs_present():
    m=json.loads(Path('tests/fixtures/air_quality/airnow/layer4/manifests/reconcile_valid_manifest.json').read_text())
    out,errs=reconcile_from_manifest(m,'2026-01-01T00:00:00Z')
    assert not errs
    assert out['site_index']
    assert out['zip_reporting_area_index']
    assert any(e['predicate']=='ZIP_ASSIGNED_TO_REPORTING_AREA' for e in out['relationship_edges'])
