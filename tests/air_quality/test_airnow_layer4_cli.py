import subprocess,sys

def test_cli_success(tmp_path):
    r=subprocess.run([sys.executable,'tools/air_quality/airnow_reconcile_layer4.py','--manifest','tests/fixtures/air_quality/airnow/layer4/manifests/reconcile_valid_manifest.json','--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z'])
    assert r.returncode==0
    assert (tmp_path/'reconciliation_receipt.json').exists()

def test_cli_missing_receipt_fails(tmp_path):
    r=subprocess.run([sys.executable,'tools/air_quality/airnow_reconcile_layer4.py','--manifest','tests/fixtures/air_quality/airnow/layer4/manifests/reconcile_missing_receipt_manifest.json','--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z'])
    assert r.returncode!=0
