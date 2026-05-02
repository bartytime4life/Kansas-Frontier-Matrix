import subprocess,sys
from pathlib import Path

CLI=[sys.executable,'tools/air_quality/airnow_layer23_snapshot_preservation_audit.py']

def run(m,tmp_path):
 o=tmp_path/m.stem
 r=subprocess.run(CLI+['--manifest',str(m),'--out-dir',str(o),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
 return r,o

def test_valid_and_no_packet(tmp_path):
 base=Path('tests/fixtures/air_quality/airnow/layer23/manifests')
 r,o=run(base/'snapshot_preservation_audit_valid_manifest.json',tmp_path)
 assert r.returncode==0
 assert (o/'snapshot_preservation_audit_packet.tar.gz').exists()
 r2,o2=run(base/'snapshot_preservation_audit_valid_no_packet_manifest.json',tmp_path)
 assert r2.returncode==0
 assert not (o2/'snapshot_preservation_audit_packet.tar.gz').exists()

def test_missing_receipts_fail(tmp_path):
 base=Path('tests/fixtures/air_quality/airnow/layer23/manifests')
 for n in ['snapshot_preservation_audit_missing_layer20_receipt_manifest.json','snapshot_preservation_audit_missing_layer21_receipt_manifest.json','snapshot_preservation_audit_missing_layer22_receipt_manifest.json','snapshot_preservation_audit_missing_decision_candidate_manifest.json']:
  r,_=run(base/n,tmp_path); assert r.returncode!=0
