#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from pathlib import Path
from tools.stability.soil._stability_common import *
T={"route_regression","schema_regression","header_regression","access_log_regression","consumer_contract_regression","slo_regression","fallback_regression"}
S={"armed","recommended","not_required","blocked"};V={"low","medium","high","critical"}

def main():
 a=argparse.ArgumentParser();a.add_argument('--continuity-root',required=True);a.add_argument('--stability-root',required=True);a.add_argument('--sentinel',required=True)
 ns=a.parse_args(); d=load_json(ns.sentinel); cid=sanitize_id(d.get('continuity_id'))
 if d.get('steward_review',{}).get('decision')!='approved': return fail('missing steward approval')
 if d.get('sentinel_type') not in T or d.get('sentinel_status') not in S or d.get('severity') not in V: return fail('invalid enums')
 if d.get('severity') in {'high','critical'} and d.get('sentinel_status')=='not_required' and not d.get('evidence_refs'): return fail('high/critical needs evidence')
 if scan_payload_for_forbidden_terms(d) or scan_payload_for_contact_or_secret_terms(d) or has_private_path(json.dumps(d)): return fail('unsafe payload')
 sid=sanitize_id(stable_payload_hash(d)[:16]); d['sentinel_id']=sid
 p=Path(ns.stability_root)/'stability/soil/sentinels'/cid/f'{sid}.regression_sentinel.json'; r=p.with_name(f'{sid}.regression_sentinel_receipt.json')
 write_json_atomic(p,d); write_json_atomic(r,{"schema_version":"kfm.v1","receipt_type":"SoilRegressionSentinelReceipt","sentinel_id":sid,"continuity_id":cid,"sha256":sha256_file(p),"created":utc_now_iso()})
 print(json.dumps({"ok":True,"sentinel_id":sid})); return 0

def fail(m): print(json.dumps({"ok":False,"reason":m})); return 2
if __name__=='__main__': sys.exit(main())
