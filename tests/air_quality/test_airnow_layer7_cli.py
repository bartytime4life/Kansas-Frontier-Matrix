import subprocess, tempfile

def test_cli_prints_receipt_json():
    td=tempfile.mkdtemp(prefix='l7_')
    cp=subprocess.run(['python','tools/air_quality/airnow_layer7_release_gate.py','--manifest','tests/fixtures/air_quality/airnow/layer7/manifests/gate_valid_internal_review_manifest.json','--out-dir',td,'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
    assert cp.returncode==0
    assert 'AirNowReleaseGateReceipt' in cp.stdout
