#!/usr/bin/env python3
from tools.resilience.soil._resilience_common import *

def build_recommissioning_transparency_log(entries):
 out=[]; prev=None
 for i,e in enumerate(entries,1):
  rec=dict(e); rec['ordinal']=i; rec['previous_entry_hash']=prev
  rec['entry_hash']=sha256_bytes(json.dumps(rec,sort_keys=True,separators=(',',':')).encode())
  prev=rec['entry_hash']; out.append(rec)
 return out, prev

load_current_public_resilience=lambda r:load_json(Path(r)/'resilience/soil/current_public_delivery_resilience.json')
load_public_resilience_manifest=lambda r,i:load_json(Path(r)/f'resilience/soil/cycles/{i}/public_delivery_resilience_manifest.json')
load_public_resilience_receipt=lambda r,i:load_json(Path(r)/f'resilience/soil/cycles/{i}/public_delivery_resilience_receipt.json')
load_followup_work_order_registry=lambda r,i:load_json(Path(r)/f'resilience/soil/cycles/{i}/followup_work_order_registry.json')
load_safe_mode_exit_handoff_packet=lambda r,i:load_json(Path(r)/f'resilience/soil/cycles/{i}/safe_mode_exit_handoff_packet.json')
load_monitoring_baseline_update_packet=lambda r,i:load_json(Path(r)/f'resilience/soil/cycles/{i}/monitoring_baseline_update_packet.json')
load_slo_error_budget_update_packet=lambda r,i:load_json(Path(r)/f'resilience/soil/cycles/{i}/slo_error_budget_update_packet.json')
