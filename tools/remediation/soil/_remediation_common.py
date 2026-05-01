from tools.corrective_actions.soil._corrective_common import *

def load_current_corrective_action(root): return load_json(Path(root)/'corrective/soil/current_corrective_action.json')
def load_corrective_manifest(root,i): return load_json(Path(root)/f'corrective/soil/cycles/{i}/corrective_action_manifest.json')
def load_corrective_receipt(root,i): return load_json(Path(root)/f'corrective/soil/cycles/{i}/corrective_action_receipt.json')
def load_public_errata_registry(root,i): return load_json(Path(root)/f'corrective/soil/cycles/{i}/public_errata_registry.json')
def load_certificate_action_dispatch_packet(root,i): return load_json(Path(root)/f'corrective/soil/cycles/{i}/certificate_action_dispatch_packet.json')
def load_successor_work_order_packet(root,i): return load_json(Path(root)/f'corrective/soil/cycles/{i}/successor_release_work_order_packet.json')
def load_retraction_review_work_order_packet(root,i): return load_json(Path(root)/f'corrective/soil/cycles/{i}/retraction_review_work_order_packet.json')
def load_corrective_action_ledger(root,i): return load_json(Path(root)/f'corrective/soil/cycles/{i}/corrective_action_ledger.json')
def load_latest_certificate_status(root, rid): return load_json(Path(root)/f'trust_registry/soil/registrations/{rid}/certificate_status.json')
def load_certificate_event_receipts(root, rid):
 p=Path(root)/f'trust_registry/soil/registrations/{rid}/events';
 return [load_json(x) for x in sorted(p.glob('*.receipt.json'))] if p.exists() else []
def build_remediation_transparency_log(entries):
 out=[]; prev=None
 for i,e in enumerate(entries,1):
  b={**e,'ordinal':i,'previous_entry_hash':prev}; h=stable_payload_hash(b); b['entry_hash']=h; out.append(b); prev=h
 return {'schema_version':'kfm.v1','object_type':'SoilRemediationTransparencyLog','domain':'soil','log_mode':'offline_deterministic_hash_chain','live_notification_performed':False,'live_helpdesk_submission_performed':False,'live_external_workflow_submission_performed':False,'entries':out,'log_root':prev}
