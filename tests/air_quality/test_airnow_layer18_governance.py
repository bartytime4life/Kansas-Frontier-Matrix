import subprocess
TOOL='tools/air_quality/airnow_layer18_snapshot_finalization.py'
BASE='tests/fixtures/air_quality/airnow/layer18/manifests'

def run(name,tmp_path):
 o=tmp_path/name
 return subprocess.run(['python',TOOL,'--manifest',f'{BASE}/{name}.json','--out-dir',str(o),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True).returncode

def test_denied_manifests(tmp_path):
 for n in ['snapshot_finalization_network_manifest','snapshot_finalization_publication_request_manifest','snapshot_finalization_command_execution_manifest','snapshot_finalization_export_manifest','snapshot_finalization_copy_manifest','snapshot_finalization_transfer_manifest','snapshot_finalization_publish_manifest','snapshot_finalization_file_deletion_manifest','snapshot_finalization_destruction_manifest','snapshot_finalization_chmod_manifest','snapshot_finalization_legal_hold_creation_manifest','snapshot_finalization_archive_certification_manifest','snapshot_finalization_legal_advice_manifest','snapshot_finalization_auto_apply_manifest','snapshot_finalization_task_closure_manifest','snapshot_finalization_github_action_manifest','snapshot_finalization_secret_field_manifest']:
  assert run(n,tmp_path)!=0
