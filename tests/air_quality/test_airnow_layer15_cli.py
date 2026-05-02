import json, subprocess, sys
from pathlib import Path

def test_layer15_cli_runs(tmp_path):
    m='tests/fixtures/air_quality/airnow/layer15/manifests/archival_finalization_valid_manifest.json'
    out=tmp_path/'o'
    r=subprocess.run([sys.executable,'tools/air_quality/airnow_layer15_archival_finalization.py','--manifest',m,'--out-dir',str(out),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
    assert r.returncode==0
    data=json.loads(r.stdout)
    assert data['workflow_outcome'] in {'ARCHIVAL_FINALIZATION_COMPLETE_INTERNAL_ONLY','ARCHIVAL_FINALIZATION_NEEDS_MORE_INPUT'}
    assert (out/'archival_finalization_receipt.json').exists()
