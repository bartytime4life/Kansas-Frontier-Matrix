#!/usr/bin/env python3
import argparse, json, hashlib
from datetime import datetime, timezone
from pathlib import Path

def nowz(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def load(p): return json.loads(Path(p).read_text())
def dump(p,o): Path(p).parent.mkdir(parents=True,exist_ok=True); Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')

def main():
 p=argparse.ArgumentParser();p.add_argument('--release-candidate-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--attester',default='fixture-attester');p.add_argument('--role',default='release_manager');p.add_argument('--statement',default='fixture boundary attestation');p.add_argument('--signature',default='fixture-signature');p.add_argument('--signature-type',default='fixture_signature');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 asof=a.as_of or nowz(); fixture=a.fixture_only or a.signature_type=='fixture_signature'; prod_allowed=False if fixture else False
 status='fixture_attested' if fixture else 'candidate_attested'
 if a.signature_type=='fixture_signature' and prod_allowed: raise SystemExit('fixture signature cannot authorize production')
 o={'schema_version':'v1','attestation_id':'gate-d-'+hashlib.sha256((a.release_candidate_dir+asof).encode()).hexdigest()[:12],'domain':'atmosphere.air','created_at':nowz(),'as_of':asof,'gate':'D','subject_refs':[str(Path(a.release_candidate_dir)/'reentry_release_candidate_package.json')],'attester':a.attester,'role':a.role,'statement':a.statement,'signature':a.signature,'signature_type':a.signature_type,'fixture_backed':fixture,'production_use_allowed':prod_allowed,'status': status if not fixture else 'fixture_attested'}
 ev={'schema_version':'v1','event_id':'evt-'+o['attestation_id'],'domain':'atmosphere.air','event_type':'gate_d_attestation_created','created_at':o['created_at'],'as_of':asof,'actor':f"{a.attester}-nonprod" if fixture else a.attester,'subject_refs':o['subject_refs'],'evidence_refs':[],'result':'pass','details':'fixture-only gate d attestation'}
 if not a.dry_run:
  out=Path(a.out_dir);dump(out/'reentry_gate_d_attestation.json',o); (out/'reentry_publication_boundary_events.jsonl').write_text(json.dumps(ev,sort_keys=True)+'\n')
 print('PASS')
if __name__=='__main__': main()
