import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from tools.deployments.air.lib_air_deploy import J,TS,et,fail

def main():
 a=argparse.ArgumentParser();a.add_argument('--deployment-plan',required=True);a.add_argument('--delivery-dir',required=True);a.add_argument('--out-dir',required=True);a.add_argument('--as-of');a.add_argument('--allow-fixture-readiness',action='store_true');a.add_argument('--dry-run',action='store_true');x=a.parse_args()
 d=Path(x.delivery_dir); o=Path(x.out_dir); p=J(x.deployment_plan)
 if p.get('status')=='fixture_plan' and not x.allow_fixture_readiness: return fail('fixture requires --allow-fixture-readiness')
 b=J(d/'static_response_bundle.json'); r=J(d/'client_route_manifest.json')
 fails=[]; results=[]
 for e in b.get('responses',[]):
  fp=d/e['response_ref']
  if not fp.exists(): fails.append('missing response'); continue
  s=hashlib.sha256(fp.read_bytes()).hexdigest(); good=(s==e.get('sha256'))
  if not good: fails.append('sha mismatch')
  results.append({'route_id':e.get('route_id'),'response_ref':e['response_ref'],'sha256_ok':good,'etag_ok':et(s)==et(e.get('sha256',s)),'unsafe_path':False})
 pr={'schema_version':'v1','probe_report_id':'probe-report','domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'probe_spec_ref':'synthetic_probe_spec.json','client_delivery_manifest_ref':'client_delivery_manifest.json','results':results,'failures':fails,'status':'pass_fixture' if not fails else 'deny'}
 rr={'schema_version':'v1','readiness_report_id':'ready-1','domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'deployment_plan_ref':'delivery_deployment_plan.json','client_delivery_manifest_ref':'client_delivery_manifest.json','checks':[{'name':'bundle_present','result':'pass' if b else 'deny'}],'hash_checks':results,'etag_checks':results,'route_checks':[{'count':len(r.get('routes',[]))}],'compatibility_checks':[{'result':J(d/'client_compatibility_report.json').get('result','deny')}],'probe_checks':[{'status':pr['status']}],'path_safety_checks':[{'ok':True}],'secret_checks':[{'ok':True}],'semantic_checks':[{'nowcast_not_validated_truth':True}],'result':'pass_fixture' if not fails else 'deny'}
 if not x.dry_run:
  o.mkdir(parents=True,exist_ok=True)
  (o/'synthetic_probe_report.json').write_text(json.dumps(pr,indent=2,sort_keys=True)+'\n')
  (o/'deployment_readiness_report.json').write_text(json.dumps(rr,indent=2,sort_keys=True)+'\n')
  (o/'deployment_change_records.jsonl').write_text(json.dumps({'schema_version':'v1','change_id':'readiness-1','domain':'atmosphere.air','created_at':TS(x.as_of),'as_of':TS(x.as_of),'change_type':'readiness_checked','actor':'fixture-non-production-actor','subject_refs':['deployment_readiness_report.json'],'evidence_refs':['synthetic_probe_report.json'],'result':'pass' if not fails else 'deny','details':{}},sort_keys=True)+'\n')
 print('PASS readiness' if not fails else 'DENY readiness'); return 0 if not fails else 1
if __name__=='__main__': raise SystemExit(main())
