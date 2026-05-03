import json, subprocess, tempfile
from pathlib import Path
CMD=["python","tools/air_quality/airnow_layer34_closure_archive_index_preservation_finalization.py"]
M=Path("tests/fixtures/air_quality/airnow/layer34/manifests")

def run(name):
 d=tempfile.mkdtemp(prefix='l34-')
 p=subprocess.run(CMD+["--manifest",str(M/name),"--out-dir",d,"--created-at","2026-01-01T00:00:00Z"],capture_output=True,text=True)
 return p,Path(d)

def test_valid_and_packet():
 p,d=run("closure_archive_index_preservation_finalization_valid_manifest.json")
 assert p.returncode==0
 r=json.loads((d/"closure_archive_index_preservation_finalization_receipt.json").read_text())
 assert r["output_hashes"]["closure_archive_index_preservation_finalization_packet_hash"]
 assert (d/"closure_archive_index_preservation_finalization_packet.tar.gz").exists()

def test_no_packet():
 p,d=run("closure_archive_index_preservation_finalization_valid_no_packet_manifest.json")
 assert p.returncode==0
 assert not (d/"closure_archive_index_preservation_finalization_packet.tar.gz").exists()

def test_denied_samples():
 for n in [x.name for x in M.glob('*_manifest.json') if any(t in x.name for t in ['network','publication_request','command_execution','database_write','search_api','public_catalog','copy_manifest','transfer_manifest','export_manifest','publish_manifest','file_deletion','destruction','chmod','legal_hold_creation','archive_certification','legal_advice','auto_apply','task_closure','github_action','coordinate_leak','secret_field'])]:
  p,_=run(n); assert p.returncode!=0, n
