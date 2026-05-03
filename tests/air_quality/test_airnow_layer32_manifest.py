from pathlib import Path
import subprocess,sys
CLI=[sys.executable,'tools/air_quality/airnow_layer32_closure_archive_index_preservation.py']
M='tests/fixtures/air_quality/airnow/layer32/manifests'
def run(name,tmp_path):
 o=tmp_path/name
 r=subprocess.run(CLI+['--manifest',f'{M}/{name}.json','--out-dir',str(o),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
 return r,o

def test_valid(tmp_path):
 r,o=run('closure_archive_index_preservation_valid_manifest',tmp_path); assert r.returncode==0
 assert (o/'closure_archive_index_preservation_packet.tar.gz').exists()
 r2,o2=run('closure_archive_index_preservation_valid_no_packet_manifest',tmp_path); assert r2.returncode==0
 assert not (o2/'closure_archive_index_preservation_packet.tar.gz').exists()

def test_missing_required(tmp_path):
 for n in ['closure_archive_index_preservation_missing_layer31_receipt_manifest','closure_archive_index_preservation_missing_hash_chain_manifest','closure_archive_index_preservation_missing_policy_ledger_manifest']:
  r,_=run(n,tmp_path); assert r.returncode!=0
