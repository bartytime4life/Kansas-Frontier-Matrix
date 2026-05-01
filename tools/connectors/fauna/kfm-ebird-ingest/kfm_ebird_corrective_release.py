#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, hashlib, sys
from pathlib import Path
from datetime import datetime, timezone
VERSION='0.22.0'

def now(): return datetime.now(timezone.utc).isoformat()
def fail(m): print(f'ERROR: {m}',file=sys.stderr); raise SystemExit(2)
def sh(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()

def parse(argv):
  p=argparse.ArgumentParser(prog='kfm-ebird-corrective-release')
  p.add_argument('--version',action='version',version=VERSION)
  p.add_argument('--mode',default='plan',choices=['plan','build','validate','approve-local','rollback-plan','report'])
  p.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
  for a in ['remediation-plan','remediation-receipt','remediation-manifest','public-correction-notice','release-receipt','package-manifest','deployment-receipt','public-out-dir']:
    p.add_argument(f'--{a}')
  p.add_argument('--published-root',default='data/published/fauna/ebird');p.add_argument('--catalog-root',default='data/catalog/fauna/ebird');p.add_argument('--layer-registry-dir',default='data/published/fauna/layers')
  p.add_argument('--out-dir',default='data/catalog/fauna/ebird/corrective-releases/run');p.add_argument('--decision',choices=['approve','block','needs-review'])
  p.add_argument('--dry-run',action='store_true');p.add_argument('--force',action='store_true')
  return p.parse_args(argv)

def main():
  a=parse(sys.argv[1:])
  if a.mode=='build' and not a.remediation_plan: fail('build requires --remediation-plan')
  if a.mode=='approve-local' and (not a.force or not a.remediation_receipt): fail('approve-local requires --force and --remediation-receipt')
  out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
  rp=json.loads(Path(a.remediation_plan).read_text()) if a.remediation_plan and Path(a.remediation_plan).exists() else {}
  rid=rp.get('remediation_id','unknown')
  blocked = bool(json.loads(Path(a.remediation_manifest).read_text()).get('counts',{}).get('actions_blocked_requires_rerun',0)) if a.remediation_manifest and Path(a.remediation_manifest).exists() else False
  obj={"aggregate_targets":a.aggregate,"remediation_id":rid}
  for f in ['remediation_receipt','remediation_manifest','public_correction_notice','release_receipt','package_manifest','deployment_receipt']:
    v=getattr(a,f)
    if v and Path(v).exists(): obj[f+'_sha256']=sh(Path(v))
  cid=hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:16]
  plan={"schema_version":"v1","object_type":"EbirdCorrectiveReleasePlan","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"corrective_release","public_safe_final_outputs":True,"exact_points":"restricted","corrective_release_id":cid,"remediation_id":rid,"aggregate_targets":[a.aggregate],"corrective_release_type":"blocked_requires_full_rerun" if blocked else "mixed_public_safe","blocked_actions":["requires_full_rerun"] if blocked else [],"generated_at":now()}
  (out/'corrective_release_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
  (out/'corrective_release_manifest.json').write_text(json.dumps({"schema_version":"v1","object_type":"EbirdCorrectiveReleaseManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"corrective_release","public_safe_final_outputs":True,"exact_points":"restricted","corrective_release_id":cid,"remediation_id":rid,"input_artifacts":[],"output_artifacts":[],"generated_at":now()},indent=2)+'\n')
  (out/'corrective_release_validation_report.json').write_text(json.dumps({"schema_version":"v1","object_type":"EbirdCorrectiveReleaseValidationReport","corrective_release_id":cid,"status":"fail" if blocked else "pass"},indent=2)+'\n')
  if a.mode=='approve-local':
    dec='blocked' if blocked else ('approved' if a.decision=='approve' else 'needs_review')
    (out/'corrective_release_receipt.json').write_text(json.dumps({"schema_version":"v1","object_type":"EbirdCorrectiveReleaseReceipt","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","corrective_release_id":cid,"remediation_id":rid,"decision":dec,"blockers":["blocked_actions"] if blocked else [],"generated_at":now()},indent=2)+'\n')
  print(cid)

if __name__=='__main__': main()
