#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path

def _j(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def _sha(path):
    h=hashlib.sha256(); h.update(Path(path).read_bytes()); return h.hexdigest()

def _canon(obj): return json.dumps(obj, sort_keys=True, separators=(',',':'))

def _id(payload): return hashlib.sha256(_canon(payload).encode()).hexdigest()[:16]

def parse(argv):
    p=argparse.ArgumentParser(prog='kfm-ebird-consumer-impact')
    p.add_argument('--mode',default='scan',choices=['scan','compare','matrix','renewal','validate','report'])
    p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
    p.add_argument('--consumer-registry'); p.add_argument('--previous-sdk-manifest'); p.add_argument('--current-sdk-manifest')
    p.add_argument('--previous-consumer-contract-manifest'); p.add_argument('--current-consumer-contract-manifest')
    p.add_argument('--previous-root-of-trust'); p.add_argument('--current-root-of-trust')
    p.add_argument('--previous-gate-decision'); p.add_argument('--current-gate-decision')
    p.add_argument('--thresholds',default='configs/fauna/ebird/consumer_impact_thresholds.json')
    p.add_argument('--out-dir'); p.add_argument('--public-out-dir'); p.add_argument('--force',action='store_true'); p.add_argument('--dry-run',action='store_true')
    p.add_argument('--version',action='store_true')
    return p.parse_args(argv)

def main():
    a=parse(sys.argv[1:])
    if a.version:
        print(json.dumps({'adapter':'kfm-ebird','tool':'consumer-impact','version':'29.0.0'})); return
    inputs={k:v for k,v in vars(a).items() if k.endswith('manifest') or k in ['consumer_registry','previous_root_of_trust','current_root_of_trust','previous_gate_decision','current_gate_decision','thresholds'] if v}
    for v in inputs.values():
        if not Path(v).exists(): raise SystemExit(f'missing input: {v}')
    payload={'aggregate_targets':a.aggregate,'adapter_version':'29.0.0'}
    if a.consumer_registry: payload['consumer_registry_sha256']=_sha(a.consumer_registry)
    for k in ['previous_sdk_manifest','current_sdk_manifest','previous_consumer_contract_manifest','current_consumer_contract_manifest','previous_gate_decision','current_gate_decision']:
        v=getattr(a,k)
        if v: payload[f'{k}_sha256']=_sha(v)
    for k in ['previous_root_of_trust','current_root_of_trust']:
        v=getattr(a,k)
        if v: payload[k]=_j(v).get('root_hash')
    impact_id=_id(payload)
    if a.dry_run: print(json.dumps({'impact_id':impact_id,'mode':a.mode})); return
    out=Path(a.out_dir or f'data/catalog/fauna/ebird/consumer-impact/{impact_id}')
    pub=Path(a.public_out_dir) if a.public_out_dir else None
    if out.exists() and any(out.iterdir()) and not a.force: raise SystemExit('--force required to overwrite out-dir')
    out.mkdir(parents=True,exist_ok=True)
    now=datetime.now(timezone.utc).isoformat()
    report={'schema_version':'v1','object_type':'KfmEbirdConsumerImpactReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'consumer_impact','public_safe_final_outputs':True,'exact_points':'restricted','impact_id':impact_id,'aggregate_targets':a.aggregate,'status':'pass','consumers':[],'summary':{'consumers_total':0,'compatible':0,'compatible_with_warnings':0,'requires_reaudit':0,'requires_recertification':0,'requires_upgrade':0,'requires_revocation_review':0,'unknown':0},'generated_at':now}
    if a.consumer_registry:
      reg=_j(a.consumer_registry)
      for c in reg.get('consumers',[]):
        st='compatible'; act='no_action'; reasons=[]
        if a.current_gate_decision and _j(a.current_gate_decision).get('decision')=='no_go': st='requires_revocation_review'; act='revoke_review'; reasons=[{'reason_id':'failed_gate','reason_type':'failed_gate','severity':'critical','message':'Current gate decision is no_go'}]
        report['consumers'].append({'consumer_id':c.get('consumer_id','unknown'),'consumer_name':c.get('consumer_name'),'certification_id':c.get('certification_id'),'certification_status':c.get('certification_status','unknown'),'compatibility_status':st,'impact_level':'critical' if st!='compatible' else 'none','reasons':reasons,'recommended_actions':[act]})
      report['summary']['consumers_total']=len(report['consumers'])
      for c in report['consumers']: report['summary'][c['compatibility_status']]+=1
    (out/'consumer_impact_report.json').write_text(json.dumps(report,indent=2)+"\n",encoding='utf-8')
    (out/'consumer_compatibility_matrix.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdConsumerCompatibilityMatrix','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'consumer_impact','public_safe_final_outputs':True,'exact_points':'restricted','impact_id':impact_id,'matrix':[{'consumer_id':c['consumer_id'],'consumer_name':c.get('consumer_name'),'aggregate_targets':a.aggregate,'compatibility_status':c['compatibility_status'],'required_action':c['recommended_actions'][0],'public_safe':True,'exact_points':'restricted'} for c in report['consumers']],'generated_at':now},indent=2)+"\n")
    if pub:
      pub.mkdir(parents=True,exist_ok=True)
      (pub/'public_consumer_impact_summary.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdConsumerImpactSummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','impact_id':impact_id,'aggregate_targets':a.aggregate,'impact_status':report['status'],'summary':report['summary'],'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'no_restricted_observations_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True},'generated_at':now},indent=2)+"\n")
    print(str(out))

if __name__=='__main__': main()
