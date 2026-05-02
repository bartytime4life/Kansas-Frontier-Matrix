#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from pathlib import Path
from tools.stability.soil._stability_common import *
TYPES={"watch_window","availability_summary","latency_summary","route_health_summary","governance_only_summary","consumer_contract_summary"}
STAT={"pass","recommended","not_required","blocked"}

def main():
 a=argparse.ArgumentParser();a.add_argument('--continuity-root',required=True);a.add_argument('--stability-root',required=True);a.add_argument('--observation',required=True);a.add_argument('--continuity-id')
 ns=a.parse_args(); o=load_json(ns.observation); cid=sanitize_id(ns.continuity_id or o.get('continuity_id'))
 if o.get('steward_review',{}).get('decision')!='approved': return fail('missing steward approval')
 if o.get('observation_type') not in TYPES or o.get('observation_status') not in STAT: return fail('unknown type/status')
 if o.get('observation_status')=='pass' and o.get('observation_type')!='governance_only_summary' and not o.get('evidence_refs'): return fail('missing evidence')
 if scan_payload_for_forbidden_terms(o) or scan_payload_for_contact_or_secret_terms(o) or has_private_path(json.dumps(o)): return fail('unsafe payload')
 oid=sanitize_id(stable_payload_hash(o)[:16]); o['observation_id']=oid; o['continuity_id']=cid
 p=Path(ns.stability_root)/'stability/soil/observations'/cid/f'{oid}.steady_state_observation.json'; r=p.with_name(f'{oid}.steady_state_observation_receipt.json')
 write_json_atomic(p,o); rec={"schema_version":"kfm.v1","receipt_type":"SoilSteadyStateObservationReceipt","observation_id":oid,"continuity_id":cid,"sha256":sha256_file(p),"created":utc_now_iso()}; write_json_atomic(r,rec)
 print(json.dumps({"ok":True,"observation_id":oid,"record":str(p),"receipt":str(r)})); return 0

def fail(msg): print(json.dumps({"ok":False,"reason":msg})); return 2
if __name__=='__main__': sys.exit(main())
