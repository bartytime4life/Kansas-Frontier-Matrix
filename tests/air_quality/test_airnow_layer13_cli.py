import json, subprocess, sys

def test_layer13_cli(tmp_path):
    out=tmp_path/'out'
    r=subprocess.run([sys.executable,'tools/air_quality/airnow_layer13_retention_plan.py','--manifest','tests/fixtures/air_quality/airnow/layer13/manifests/retention_valid_manifest.json','--out-dir',str(out),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
    assert r.returncode==0
    data=json.loads(r.stdout)
    assert data['workflow_outcome']=='RETENTION_PLAN_COMPLETE_INTERNAL_ONLY'
    assert (out/'retention_receipt.json').exists()
