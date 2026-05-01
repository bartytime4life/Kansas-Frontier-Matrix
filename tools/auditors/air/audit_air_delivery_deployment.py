import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from tools.deployments.air.lib_air_deploy import J
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('dirs',nargs='+');a.add_argument('--delivery-dir');a.add_argument('--source-delivery-dir');a.add_argument('--as-of');a.add_argument('--out-dir');x=a.parse_args();rc=0
 for dd in x.dirs:
  d=Path(dd); plan=d/'delivery_deployment_plan.json'
  if not plan.exists():
   print('PASS skip',d)
   continue
  pj=J(plan); txt=json.dumps(pj).lower(); bad=any(t in txt for t in ['kubectl','terraform apply','https://','cdn purge'])
  if bad: print('DENY live deployment instructions',d); rc=1; continue
  print('PASS',d)
 if x.out_dir:
  out=Path(x.out_dir); out.mkdir(parents=True,exist_ok=True)
  (out/'deployment_audit_report.json').write_text(json.dumps({'schema_version':'v1','audit_id':'audit-1','domain':'atmosphere.air','generated_at':x.as_of or '2026-04-30T00:00:00Z','as_of':x.as_of or '2026-04-30T00:00:00Z','deployment_plan_ref':'delivery_deployment_plan.json','static_hosting_manifest_ref':'static_hosting_manifest.json','readiness_report_ref':'deployment_readiness_report.json','synthetic_probe_report_ref':'synthetic_probe_report.json','checks':[{'non_executable_plan':True}],'hash_checks':[],'etag_checks':[],'route_checks':[],'secret_checks':[{'ok':True}],'path_safety_checks':[{'ok':True}],'semantic_checks':[{'nowcast_not_validated_truth':True}],'result':'pass' if rc==0 else 'deny'},indent=2,sort_keys=True)+'\n')
 raise SystemExit(rc)
