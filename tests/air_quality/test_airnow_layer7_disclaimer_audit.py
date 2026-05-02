import json, tempfile, subprocess
from pathlib import Path

def test_disclaimer_passes_for_valid_fixture():
    td=tempfile.mkdtemp(prefix='l7_')
    subprocess.run(['python','tools/air_quality/airnow_layer7_release_gate.py','--manifest','tests/fixtures/air_quality/airnow/layer7/manifests/gate_valid_internal_review_manifest.json','--out-dir',td,'--created-at','2026-01-01T00:00:00Z'],check=True)
    da=json.loads((Path(td)/'disclaimer_audit.json').read_text())
    assert da['overall_status']=='PASS'
