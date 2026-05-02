import subprocess
def test_cli_valid(tmp_path):
 p=subprocess.run(['python','tools/air_quality/airnow_layer22_snapshot_preservation_finalization.py','--manifest','tests/fixtures/air_quality/airnow/layer22/manifests/snapshot_preservation_finalization_valid_manifest.json','--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z'],check=False);assert p.returncode==0
def test_cli_no_packet(tmp_path):
 p=subprocess.run(['python','tools/air_quality/airnow_layer22_snapshot_preservation_finalization.py','--manifest','tests/fixtures/air_quality/airnow/layer22/manifests/snapshot_preservation_finalization_valid_no_packet_manifest.json','--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z'],check=False);assert p.returncode==0
