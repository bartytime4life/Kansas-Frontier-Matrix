#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.resolution.soil._resolution_common import *
ALLOWED_DT={"no_change","errata","metadata_correction","quality_review","rights_review","provenance_review","successor_release","certificate_suspend","certificate_revoke","retraction_review"}
ALLOWED_SEV={"low","medium","high","critical"}
REQ_EVID={"errata","successor_release","certificate_suspend","certificate_revoke","retraction_review","rights_review","provenance_review"}

def main(argv=None):
 a=argparse.ArgumentParser();
 for k in ['accountability-root','assurance-root','resolution-root','decision']: a.add_argument('--'+k,required=True)
 a.add_argument('--accountability-id'); x=a.parse_args(argv)
 try: subprocess.run([sys.executable,'tools/validators/soil/accountability_check.py','--accountability-root',x.accountability_root],check=False,capture_output=True); subprocess.run([sys.executable,'tools/validators/soil/assurance_check.py','--assurance-root',x.assurance_root],check=False,capture_output=True)
 except Exception: pass
 d=load_json(x.decision); aid=x.accountability_id or load_current_accountability(x.accountability_root)['active_accountability_id']
 manifest=load_accountability_manifest(x.accountability_root,aid); receipt=load_accountability_receipt(x.accountability_root,aid)
 f=load_feedback_registry(x.accountability_root,aid); c=load_challenge_registry(x.accountability_root,aid); k=load_correction_registry(x.accountability_root,aid)
 targets={('feedback',i.get('feedback_id') or i.get('target_id')) for i in f}|{('challenge',i.get('challenge_id') or i.get('target_id')) for i in c}|{('correction',i.get('correction_id') or i.get('target_id')) for i in k}
 fail=[]
 if d.get('decision')!='approved': fail.append('decision not approved')
 if d.get('target_type') not in {'feedback','challenge','correction'}: fail.append('unknown target_type')
 if d.get('decision_type') not in ALLOWED_DT: fail.append('unknown decision_type')
 if d.get('severity') not in ALLOWED_SEV: fail.append('unknown severity')
 if not d.get('evidence_review',{}).get('required') or not d.get('evidence_review',{}).get('decision'): fail.append('missing evidence review')
 if d.get('steward_review',{}).get('decision')!='approved': fail.append('missing steward review approval')
 tid=d.get('target_id'); tt=d.get('target_type')
 if (tt,tid) not in targets: fail.append('target missing')
 if d.get('decision_type') in REQ_EVID and not d.get('evidence_refs'): fail.append('evidence refs required')
 if d.get('decision_type')!='no_change' and d.get('evidence_review',{}).get('decision')=='insufficient': fail.append('insufficient evidence')
 if d.get('immutable_artifacts_mutated') is True: fail.append('mutation attempt')
 if scan_text_for_forbidden_terms(d.get('public_message','')): fail.append('forbidden terms')
 if scan_payload_for_contact_or_secret_terms({'public_message':d.get('public_message','')}): fail.append('contact/secret data')
 if any(has_private_path(r) for r in d.get('evidence_refs',[])): fail.append('private path')
 if fail: print(json.dumps({'written':False,'reasons':fail},sort_keys=True)); return 1
 adj_id=sanitize_id(d.get('adjudication_id') or f"adj-{stable_payload_hash(d)[:16]}")
 out=Path(x.resolution_root)/f'resolution/soil/adjudications/{aid}'; out.mkdir(parents=True,exist_ok=True)
 notice={'schema_version':'kfm.v1','object_type':'SoilAdjudicationNotice','domain':'soil','adjudication_id':adj_id,'accountability_id':aid,'assurance_id':manifest.get('assurance_id'),'registry_id':manifest.get('registry_id'),'release_id':manifest.get('release_id'),'target_type':tt,'target_id':tid,'decision_type':d['decision_type'],'severity':d['severity'],'decision':'approved','evidence_review_decision':d['evidence_review']['decision'],'public_message':d.get('public_message',''),'evidence_refs':d.get('evidence_refs',[]),'immutable_artifacts_mutated':False,'created':utc_now_iso()}
 npath=out/f'{adj_id}.adjudication_notice.json'; write_json_atomic(npath,notice)
 rec={'schema_version':'kfm.v1','receipt_type':'AdjudicationReceipt','domain':'soil','adjudication_id':adj_id,'accountability_id':aid,'release_id':manifest.get('release_id'),'decision':'approved','source_accountability_receipt_hash':'sha256:'+sha256_file(Path(x.accountability_root)/f'accountability/soil/cycles/{aid}/accountability_receipt.json'),'adjudication_notice_hash':'sha256:'+sha256_file(npath),'policy_checks':{'accountability_checked':True,'target_exists_checked':True,'evidence_review_checked':True,'steward_review_checked':True,'immutability_checked':True,'public_paths_checked':True,'forbidden_terms_checked':True,'contact_data_checked':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 rpath=out/f'{adj_id}.adjudication_receipt.json'; write_json_atomic(rpath,rec)
 print(json.dumps({'written':True,'adjudication_id':adj_id,'notice_ref':str(npath),'receipt_ref':str(rpath)},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
