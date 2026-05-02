import subprocess, sys

def test_network_manifest_denied(tmp_path):
    out=tmp_path/'o'
    r=subprocess.run([sys.executable,'tools/air_quality/airnow_layer8_remediation_scaffold.py','--manifest','tests/fixtures/air_quality/airnow/layer8/manifests/remediation_network_manifest.json','--out-dir',str(out),'--created-at','2026-01-01T00:00:00Z'])
    assert r.returncode!=0
