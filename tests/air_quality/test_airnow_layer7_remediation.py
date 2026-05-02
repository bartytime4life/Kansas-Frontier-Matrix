import json, tempfile, subprocess
from pathlib import Path

def test_remediation_generated_for_denied_request():
    td=tempfile.mkdtemp(prefix='l7_')
    subprocess.run(['python','tools/air_quality/airnow_layer7_release_gate.py','--manifest','tests/fixtures/air_quality/airnow/layer7/manifests/gate_public_api_manifest.json','--out-dir',td,'--created-at','2026-01-01T00:00:00Z'])
    rp=json.loads((Path(td)/'remediation_plan.json').read_text())
    assert rp['items']
