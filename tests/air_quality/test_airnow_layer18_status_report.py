import json, subprocess
TOOL='tools/air_quality/airnow_layer18_snapshot_finalization.py'
BASE='tests/fixtures/air_quality/airnow/layer18/manifests'

def run(name,tmp_path):
 o=tmp_path/name
 r=subprocess.run(['python',TOOL,'--manifest',f'{BASE}/{name}.json','--out-dir',str(o),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
 return r,o

def test_valid_and_no_packet(tmp_path):
 r,o=run('snapshot_finalization_valid_manifest',tmp_path); assert r.returncode==0; assert (o/'snapshot_finalization_packet.tar.gz').exists()
 r,o=run('snapshot_finalization_valid_no_packet_manifest',tmp_path); assert r.returncode==0; assert not (o/'snapshot_finalization_packet.tar.gz').exists();
 rec=json.loads((o/'snapshot_finalization_receipt.json').read_text()); assert rec['output_hashes']['snapshot_finalization_packet_hash'] is None
