#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.fauna.gbif_publication_ops_validator import stable_hash, scan

def load(p): return json.loads(Path(p).read_text())

def ck(name,cond,msg=""):
    return {"check_name":name,"passed":bool(cond),"details":[] if cond else [msg]}

def main():
    ap=argparse.ArgumentParser()
    for k in ["package","evidencebundle","aggregates","geoprivacy_receipt","catalog","claims","answer","ui_cards","answer_receipt","output"]: ap.add_argument('--'+k.replace('_','-'), required=True)
    a=ap.parse_args()
    pkg=load(a.package); eb=load(a.evidencebundle); ag=load(a.aggregates); gp=load(a.geoprivacy_receipt); cat=load(a.catalog); cl=load(a.claims); ans=load(a.answer); ui=load(a.ui_cards); ar=load(a.answer_receipt)
    checks=[]
    checks.append(ck("evidencebundle_referenced", eb.get('evidence_bundle_id') in pkg.get('source_evidence_bundle_ids',[]),"missing source evidence"))
    checks.append(ck("download_key_preserved", eb.get('download_key') in pkg.get('download_keys',[]),"missing download key"))
    checks.append(ck("geoprivacy_receipt_present", gp.get('receipt_id') in pkg.get('geoprivacy_receipt_refs',[]),"missing geoprivacy"))
    checks.append(ck("answer_receipt_present", ar.get('answer_receipt_id') in pkg.get('answer_receipt_refs',[]),"missing answer receipt"))
    checks.append(ck("no_exact_coordinate_fields", not scan({"pkg":pkg,"ans":ans,"ui":ui}),"forbidden fields/language"))
    checks.append(ck("presence_posture_safe", pkg.get('presence_posture')=="reported_occurrence_not_confirmed_presence","presence posture unsafe"))
    hash_ok=pkg.get('artifact_hashes',{}).get('evidencebundle',[None])[0]==stable_hash(eb) and pkg.get('artifact_hashes',{}).get('runtime_answers',[None])[0]==stable_hash(ans)
    checks.append(ck("spec_hashes_match", hash_ok and bool(pkg.get('kfm:spec_hash')),"hash mismatch"))
    failed=[c['check_name'] for c in checks if not c['passed']]
    out={"replay_verification_id":"gbif_replay_TEST_001","publication_package_id":pkg.get('publication_package_id'),"source_system":"GBIF","verification_posture":"verified" if not failed else "failed","verified_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),"checks":checks,"failed_checks":failed,"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
    out['kfm:spec_hash']=stable_hash(out,exclude=("verified_at","created_at","replay_verification_id","kfm:spec_hash"))
    Path(a.output).write_text(json.dumps(out,indent=2)+"\n")
    print("ok")
if __name__=='__main__':main()
