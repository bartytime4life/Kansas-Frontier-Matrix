from tests.air_quality._layer24_test_common import *

def test_smoke(tmp_path):
 cp,out=run_manifest("preservation_closure_valid_manifest.json",tmp_path)
 assert cp.returncode==0
 rec=json.loads((out/"preservation_closure_receipt.json").read_text())
 assert rec["validation_outcome"]=="PASS"

def test_denials(tmp_path):
 for m in ["preservation_closure_network_manifest.json","preservation_closure_publication_request_manifest.json","preservation_closure_command_execution_manifest.json","preservation_closure_execution_manifest.json","preservation_closure_task_closure_manifest.json","preservation_closure_governance_closure_manifest.json","preservation_closure_audit_closure_manifest.json","preservation_closure_copy_manifest.json","preservation_closure_transfer_manifest.json","preservation_closure_export_manifest.json","preservation_closure_publish_manifest.json","preservation_closure_file_deletion_manifest.json","preservation_closure_destruction_manifest.json","preservation_closure_chmod_manifest.json","preservation_closure_legal_hold_creation_manifest.json","preservation_closure_archive_certification_manifest.json","preservation_closure_legal_advice_manifest.json","preservation_closure_auto_apply_manifest.json","preservation_closure_github_action_manifest.json","preservation_closure_secret_field_manifest.json"]:
  cp,_=run_manifest(m,tmp_path); assert cp.returncode!=0
