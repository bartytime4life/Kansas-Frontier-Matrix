import subprocess

def test_cli_hourly(tmp_path):
    c=['python','tools/air_quality/airnow_parse_file_product.py','--manifest','tests/fixtures/air_quality/airnow/layer3/manifests/hourly_aq_obs_manifest.json','--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z']
    r=subprocess.run(c,check=False,capture_output=True,text=True)
    assert r.returncode==0 and (tmp_path/'parse_receipt.json').exists()

def test_cli_network_denied(tmp_path):
    c=['python','tools/air_quality/airnow_parse_file_product.py','--manifest','tests/fixtures/air_quality/airnow/layer3/manifests/invalid_network_manifest.json','--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z']
    r=subprocess.run(c,check=False)
    assert r.returncode!=0
