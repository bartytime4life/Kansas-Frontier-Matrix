import json, subprocess
from pathlib import Path

TOOL='tools/air_quality/airnow_layer16_snapshot_export_plan.py'
BASE='tests/fixtures/air_quality/airnow/layer16/manifests'

def run(name,tmp_path):
    out=tmp_path/name
    r=subprocess.run(['python',TOOL,'--manifest',f'{BASE}/{name}.json','--out-dir',str(out),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
    return r,out

def test_valid_manifest(tmp_path):
    r,out=run('snapshot_export_valid_manifest',tmp_path); assert r.returncode==0
    assert (out/'snapshot_export_planning_packet.tar.gz').exists()

def test_no_packet(tmp_path):
    r,out=run('snapshot_export_valid_no_packet_manifest',tmp_path); assert r.returncode==0
    assert not (out/'snapshot_export_planning_packet.tar.gz').exists()
    receipt=json.loads((out/'snapshot_export_receipt.json').read_text())
    assert receipt['output_hashes']['snapshot_export_planning_packet_hash'] is None
