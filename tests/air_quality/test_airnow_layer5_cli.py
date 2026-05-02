import subprocess,sys

def test_cli_success(tmp_path):
    r=subprocess.run([sys.executable,'tools/air_quality/airnow_layer5_qa.py','--manifest','tests/fixtures/air_quality/airnow/layer5/manifests/qa_valid_manifest.json','--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z'])
    assert r.returncode==0
    assert (tmp_path/'qa_receipt.json').exists()

def test_cli_network_fails(tmp_path):
    r=subprocess.run([sys.executable,'tools/air_quality/airnow_layer5_qa.py','--manifest','tests/fixtures/air_quality/airnow/layer5/manifests/qa_network_manifest.json','--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z'])
    assert r.returncode!=0
