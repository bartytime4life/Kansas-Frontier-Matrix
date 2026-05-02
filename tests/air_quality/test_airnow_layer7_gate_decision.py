import json, subprocess, tempfile
from pathlib import Path

def run(manifest):
    td=tempfile.mkdtemp(prefix='l7_')
    cp=subprocess.run(['python','tools/air_quality/airnow_layer7_release_gate.py','--manifest',manifest,'--out-dir',td,'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
    rec=json.loads((Path(td)/'release_gate_receipt.json').read_text())
    dec=json.loads((Path(td)/'release_gate_decision.json').read_text())
    return cp,rec,dec

def test_valid_allow_internal_review_only():
    cp,_,dec=run('tests/fixtures/air_quality/airnow/layer7/manifests/gate_valid_internal_review_manifest.json')
    assert cp.returncode==0
    assert dec['decision_outcome']=='ALLOW_INTERNAL_REVIEW_ONLY'
    assert dec['public_release_allowed'] is False

def test_publication_denied_nonzero():
    cp,_,dec=run('tests/fixtures/air_quality/airnow/layer7/manifests/gate_publication_request_manifest.json')
    assert cp.returncode!=0
    assert dec['decision_outcome'] in ('DENY_PUBLICATION','DENY_REQUESTED_CAPABILITY')
