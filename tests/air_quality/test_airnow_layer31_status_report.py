from pathlib import Path
import subprocess,sys
CLI=[sys.executable,'tools/air_quality/airnow_layer31_closure_archive_index_audit.py']
M='tests/fixtures/air_quality/airnow/layer31/manifests'

def run(name,tmp_path):
    out=tmp_path/name
    r=subprocess.run(CLI+['--manifest',f'{M}/{name}.json','--out-dir',str(out),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
    return r,out

def test_valid_and_no_packet(tmp_path):
    r,out=run('closure_archive_index_audit_valid_manifest',tmp_path);assert r.returncode==0
    assert (out/'closure_archive_index_audit_packet.tar.gz').exists()
    r2,out2=run('closure_archive_index_audit_valid_no_packet_manifest',tmp_path);assert r2.returncode==0
    assert not (out2/'closure_archive_index_audit_packet.tar.gz').exists()

def test_denied_manifests(tmp_path):
    for n in ['closure_archive_index_audit_network_manifest','closure_archive_index_audit_publication_request_manifest','closure_archive_index_audit_command_execution_manifest','closure_archive_index_audit_database_write_manifest','closure_archive_index_audit_search_api_manifest','closure_archive_index_audit_public_catalog_manifest','closure_archive_index_audit_task_closure_manifest','closure_archive_index_audit_governance_closure_manifest','closure_archive_index_audit_audit_closure_manifest','closure_archive_index_audit_copy_manifest','closure_archive_index_audit_transfer_manifest','closure_archive_index_audit_export_manifest','closure_archive_index_audit_publish_manifest','closure_archive_index_audit_file_deletion_manifest','closure_archive_index_audit_destruction_manifest','closure_archive_index_audit_chmod_manifest','closure_archive_index_audit_legal_hold_creation_manifest','closure_archive_index_audit_archive_certification_manifest','closure_archive_index_audit_legal_advice_manifest','closure_archive_index_audit_auto_apply_manifest','closure_archive_index_audit_github_action_manifest','closure_archive_index_audit_secret_field_manifest','closure_archive_index_audit_coordinate_leak_manifest','closure_archive_index_audit_missing_layer28_receipt_manifest','closure_archive_index_audit_missing_layer29_receipt_manifest','closure_archive_index_audit_missing_layer30_receipt_manifest','closure_archive_index_audit_missing_decision_candidate_manifest']:
        r,_=run(n,tmp_path); assert r.returncode!=0
