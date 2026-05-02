import subprocess, sys, json

def test_layer8_cli_runs(tmp_path):
    out=tmp_path/'o'
    r=subprocess.run([sys.executable,'tools/air_quality/airnow_layer8_remediation_scaffold.py','--manifest','tests/fixtures/air_quality/airnow/layer8/manifests/remediation_valid_manifest.json','--out-dir',str(out),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
    assert r.returncode==0
    receipt=json.loads((out/'remediation_receipt.json').read_text())
    assert receipt['validation_outcome']=='PASS'
