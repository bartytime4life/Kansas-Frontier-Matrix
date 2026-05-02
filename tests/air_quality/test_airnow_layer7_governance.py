import subprocess, tempfile

def test_network_manifest_fails_nonzero():
    td=tempfile.mkdtemp(prefix='l7_')
    cp=subprocess.run(['python','tools/air_quality/airnow_layer7_release_gate.py','--manifest','tests/fixtures/air_quality/airnow/layer7/manifests/gate_network_manifest.json','--out-dir',td,'--created-at','2026-01-01T00:00:00Z'])
    assert cp.returncode!=0
