from tests.air_quality._layer25_test_common import *

def test_smoke(tmp_path):
 cp,out=run_manifest("preservation_closure_review_valid_manifest.json",tmp_path)
 assert cp.returncode==0
 rec=json.loads((out/"preservation_closure_review_receipt.json").read_text())
 assert rec["validation_outcome"]=="PASS"

def test_denials(tmp_path):
 for m in ["preservation_closure_review_network_manifest.json","preservation_closure_review_publication_request_manifest.json","preservation_closure_review_command_execution_manifest.json","preservation_closure_review_execution_manifest.json","preservation_closure_review_task_closure_manifest.json","preservation_closure_review_governance_closure_manifest.json","preservation_closure_review_audit_closure_manifest.json","preservation_closure_review_copy_manifest.json","preservation_closure_review_transfer_manifest.json","preservation_closure_review_export_manifest.json","preservation_closure_review_publish_manifest.json","preservation_closure_review_file_deletion_manifest.json","preservation_closure_review_destruction_manifest.json","preservation_closure_review_chmod_manifest.json","preservation_closure_review_legal_hold_creation_manifest.json","preservation_closure_review_archive_certification_manifest.json","preservation_closure_review_legal_advice_manifest.json","preservation_closure_review_auto_apply_manifest.json","preservation_closure_review_github_action_manifest.json","preservation_closure_review_secret_field_manifest.json","preservation_closure_review_coordinate_leak_manifest.json"]:
  cp,_=run_manifest(m,tmp_path); assert cp.returncode!=0
