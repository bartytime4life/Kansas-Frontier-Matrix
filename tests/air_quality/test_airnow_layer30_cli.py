import json, subprocess
from pathlib import Path

CLI=["python","tools/air_quality/airnow_layer30_closure_archive_index_finalization.py"]
BASE='tests/fixtures/air_quality/airnow/layer30/manifests'

def run(name,tmp_path):
    out=tmp_path/name.replace('.json','')
    cp=subprocess.run(CLI+["--manifest",f"{BASE}/{name}","--out-dir",str(out),"--created-at","2026-01-01T00:00:00Z"],capture_output=True,text=True)
    return cp,out

def test_valid_and_packet(tmp_path):
    cp,out=run('closure_archive_index_finalization_valid_manifest.json',tmp_path)
    assert cp.returncode==0
    r=json.loads((out/'closure_archive_index_finalization_receipt.json').read_text())
    assert r['output_hashes']['closure_archive_index_finalization_packet_hash']
    assert (out/'closure_archive_index_finalization_packet.tar.gz').exists()

def test_no_packet(tmp_path):
    cp,out=run('closure_archive_index_finalization_valid_no_packet_manifest.json',tmp_path)
    assert cp.returncode==0
    r=json.loads((out/'closure_archive_index_finalization_receipt.json').read_text())
    assert r['output_hashes']['closure_archive_index_finalization_packet_hash'] is None

import pytest
@pytest.mark.parametrize('name',[p.name for p in Path(BASE).glob('*network_manifest.json')] + [
'closure_archive_index_finalization_publication_request_manifest.json',
'closure_archive_index_finalization_command_execution_manifest.json',
'closure_archive_index_finalization_database_write_manifest.json'])
def test_denied_manifests(name,tmp_path):
    cp,_=run(name,tmp_path)
    assert cp.returncode!=0
