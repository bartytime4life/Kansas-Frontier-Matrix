import json
from kfm.air_quality.airnow.archival_finalization.run_archival_finalization import run_archival_finalization

def test_manifest_denied(tmp_path):
    m='tests/fixtures/air_quality/airnow/layer15/manifests/archival_finalization_valid_manifest.json'
    d=json.loads(open(m).read()); d['publication_requested']=True
    p=tmp_path/'m.json'; p.write_text(json.dumps(d))
    r=run_archival_finalization(str(p),str(tmp_path/'o'),'2026-01-01T00:00:00Z')
    assert r['finite_outcome']=='DENY'
