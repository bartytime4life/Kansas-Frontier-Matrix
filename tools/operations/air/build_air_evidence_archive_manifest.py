#!/usr/bin/env python
import argparse,sys,json,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'deployments'/'air'))
from cutover_common import TS,wj,scan
p=argparse.ArgumentParser();
for x in ('--handoff-dir','--cutover-dir','--authorization-dir','--deployment-readiness-dir','--delivery-dir','--out-dir'): p.add_argument(x,required=True)
p.add_argument('--include-ops-dir',action='append',default=[]);p.add_argument('--as-of');p.add_argument('--allow-fixture-archive',action='store_true');a=p.parse_args()
refs=[]
for d in [a.cutover_dir,a.authorization_dir,a.deployment_readiness_dir,a.delivery_dir,a.handoff_dir]:
 for f in Path(d).glob('*.json'):
  b=f.read_bytes(); refs.append({"artifact_type":f.stem,"path":str(f),"sha256":hashlib.sha256(b).hexdigest(),"source_ref":str(f),"public_safe":True})
out={"schema_version":"1.0.0","archive_id":"archive-001","domain":"atmosphere.air","created_at":TS(a.as_of),"as_of":TS(a.as_of),"source_chain_refs":[a.cutover_dir,a.authorization_dir,a.deployment_readiness_dir,a.delivery_dir],"archived_artifact_refs":refs,"hash_algorithm":"sha256","chain_summary":["fixture manifest only"],"redactions":[],"retention_policy":"local-fixture","safety_checks":[{"name":"no_external_storage","pass":True}],"status":"fixture_archive_manifest"}
if scan(out): print('DENY');sys.exit(1)
Path(a.out_dir).mkdir(parents=True,exist_ok=True);wj(Path(a.out_dir)/'evidence_archive_manifest.json',out);print('PASS')
