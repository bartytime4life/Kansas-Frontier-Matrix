import subprocess
from pathlib import Path

BASE='tests/fixtures/air_quality/airnow/layer27/manifests'
CLI=['python','tools/air_quality/airnow_layer27_preservation_closure_audit.py']

def run(name,tmp_path):
    return subprocess.run(CLI+['--manifest',f'{BASE}/{name}','--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z'],check=False)

def test_valid_and_no_packet(tmp_path):
    assert run('preservation_closure_audit_valid_manifest.json',tmp_path/'a').returncode==0
    assert (tmp_path/'a'/'preservation_closure_audit_packet.tar.gz').exists()
    assert run('preservation_closure_audit_valid_no_packet_manifest.json',tmp_path/'b').returncode==0
    assert not (tmp_path/'b'/'preservation_closure_audit_packet.tar.gz').exists()

def test_denied_requests_nonzero(tmp_path):
    for n in Path(BASE).glob('*_manifest.json'):
        if 'valid' in n.name or 'partial' in n.name or 'blockers' in n.name: continue
        if 'missing_' in n.name: continue
        if 'execution_manifest'==n.name: continue
        if any(x in n.name for x in ['network','publication_request','command_execution','task_closure','governance_closure','audit_closure','copy_manifest','transfer_manifest','export_manifest','publish_manifest','file_deletion','destruction','chmod','legal_hold','archive_certification','legal_advice','auto_apply','github_action','coordinate_leak','secret_field']):
            assert run(n.name,tmp_path/n.stem).returncode!=0
