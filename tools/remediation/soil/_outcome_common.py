from tools.corrective_actions.soil._corrective_common import *
from pathlib import Path

def load_current_remediation_handoff(remediation_root): return load_json(Path(remediation_root)/'remediation/soil/current_remediation_handoff.json')
def load_remediation_handoff_manifest(remediation_root, remediation_id): return load_json(Path(remediation_root)/f'remediation/soil/cycles/{remediation_id}/remediation_handoff_manifest.json')
def load_remediation_handoff_receipt(remediation_root, remediation_id): return load_json(Path(remediation_root)/f'remediation/soil/cycles/{remediation_id}/remediation_handoff_receipt.json')
def load_errata_publication_registry(remediation_root, remediation_id): return load_json(Path(remediation_root)/f'remediation/soil/cycles/{remediation_id}/errata_publication_registry.json')
def load_certificate_event_execution_tracker(remediation_root, remediation_id): return load_json(Path(remediation_root)/f'remediation/soil/cycles/{remediation_id}/certificate_event_execution_tracker.json')
def load_successor_release_intake_bundle(remediation_root, remediation_id): return load_json(Path(remediation_root)/f'remediation/soil/cycles/{remediation_id}/successor_release_intake_bundle.json')
def load_retraction_review_intake_bundle(remediation_root, remediation_id): return load_json(Path(remediation_root)/f'remediation/soil/cycles/{remediation_id}/retraction_review_intake_bundle.json')
def load_publication_receipt(published_root, release_id): return load_json(Path(published_root)/f'published/soil/releases/{release_id}/publication_receipt.json')
def load_retraction_notice(published_root, release_id): return load_json(Path(published_root)/f'published/soil/retractions/{release_id}.retraction_notice.json')
def load_retraction_receipt(published_root, release_id): return load_json(Path(published_root)/f'published/soil/retractions/{release_id}.retraction_receipt.json')
def load_archive_tombstone(archive_root, release_id): return load_json(Path(archive_root)/f'archive/soil/tombstones/{release_id}.tombstone_receipt.json')

def load_latest_certificate_status(registry_root, registry_id): return load_json(Path(registry_root)/f'trust_registry/soil/registrations/{registry_id}/certificate_status.json')
def load_certificate_event_receipts(registry_root, registry_id):
 p=Path(registry_root)/f'trust_registry/soil/registrations/{registry_id}/events'; return [load_json(x) for x in sorted(p.glob('*.receipt.json'))] if p.exists() else []

def validate_successor_release_chain(*_a, **_kw): return []
def validate_retraction_outcome_chain(*_a, **_kw): return []
def validate_certificate_event_outcome(*_a, **_kw): return []
def validate_remediation_outcome_inputs(*_a, **_kw): return []

def build_outcome_transparency_log(entries):
 out=[]; prev=None
 for i,e in enumerate(entries,1):
  x={**e,'ordinal':i,'previous_entry_hash':prev}; h=stable_payload_hash(x); x['entry_hash']=h; out.append(x); prev=h
 return {'schema_version':'kfm.v1','object_type':'SoilRemediationOutcomeTransparencyLog','domain':'soil','log_mode':'offline_deterministic_hash_chain','live_notification_performed':False,'live_helpdesk_submission_performed':False,'live_external_workflow_submission_performed':False,'entries':out,'log_root':prev,'created':utc_now_iso()}
