#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,tempfile,os
from pathlib import Path
from tools.validators.soil.federation_check import main as federation_check
from tools.validators.soil.federation_gate import main as federation_gate
from tools.federation.soil._reconciliation_common import *

def main(argv=None):
 a=argparse.ArgumentParser();
 for k in ['federation-root','discovery-root','published-root','ops-root','submissions-root','acks-root','out-root']: a.add_argument(f'--{k}',required=True)
 a.add_argument('--federation-id');a.add_argument('--reconciliation-id');a.add_argument('--required-targets');x=a.parse_args(argv)
 fid=x.federation_id or load_current_federation(x.federation_root)['active_federation_id'];rs=[]
 if federation_check(['--federation-root',x.federation_root,'--federation-id',fid])!=0: rs.append('federation invalid')
 if federation_gate(['--federation-root',x.federation_root,'--discovery-root',x.discovery_root,'--published-root',x.published_root,'--ops-root',x.ops_root])!=0: rs.append('federation gate blocked')
 m=load_federation_manifest(x.federation_root,fid); fr=load_federation_receipt(x.federation_root,fid)
 mar=Path(x.acks_root)/f'federation/soil/mirror_audits/{fid}.mirror_audit_receipt.json'
 if not mar.exists(): rs.append('missing mirror audit receipt')
 else:
  mj=load_json(mar)
  if mj.get('decision')!='pass': rs.append('mirror audit failed')
 subs=load_mock_submission_receipts(x.submissions_root,fid); acks=load_acknowledgement_receipts(x.acks_root,fid)
 req=[t.strip() for t in (x.required_targets.split(',') if x.required_targets else [t['target_name'] for t in m.get('targets',[])]) if t.strip()]
 for t in req:
  if t not in subs: rs.append(f'missing submission {t}')
  ar=acks.get(t)
  if not ar: rs.append(f'missing ack {t}')
  elif ar.get('decision')!='accepted': rs.append(f'required target not accepted {t}')
 if rs: print(json.dumps({'reconciliation_allowed':False,'federation_id':fid,'release_id':m.get('release_id'),'reasons':rs},sort_keys=True)); return 1
 rid=sanitize_id(x.reconciliation_id) if x.reconciliation_id else 'soil-reconciliation-'+sha256_bytes((fid+''.join(sorted(stable_payload_hash(v) for v in subs.values()))+''.join(sorted(stable_payload_hash(v) for v in acks.values()))+sha256_file(mar)).encode())[:16]
 outroot=Path(x.out_root)/f'federation/soil/reconciliations/{rid}';tmp=Path(tempfile.mkdtemp(prefix='soilrec_'))/rid
 entries=[]
 for t in sorted({*subs.keys(),*acks.keys()}):
  s=subs.get(t);ak=acks.get(t)
  entries.append({'target':t,'registry_id':(ak or {}).get('registry_id'),'submission_receipt_ref':f'federation/soil/submissions/{fid}/{t}.submission_receipt.json','submission_receipt_hash':'sha256:'+sha256_file(Path(x.submissions_root)/f'federation/soil/submissions/{fid}/{t}.submission_receipt.json'),'ack_receipt_ref':f'federation/soil/acks/{fid}/{t}.ack_receipt.json' if ak else None,'ack_receipt_hash':'sha256:'+sha256_file(Path(x.acks_root)/f'federation/soil/acks/{fid}/{t}.ack_receipt.json') if ak else None,'ack_status':(ak or {}).get('decision','missing'),'external_record_id':None,'external_record_url':None,'public_accessible':True,'required':t in req,'live_submission_performed':False,'live_registry_poll_performed':False,'payload_hash':(s or {}).get('submitted_payload_hash')})
 ledger={'schema_version':'kfm.v1','object_type':'SoilExternalRegistryLedger','domain':'soil','reconciliation_id':rid,'federation_id':fid,'discovery_id':m['discovery_id'],'release_id':m['release_id'],'entries':entries}
 write_json_atomic(tmp/'registry_ledger.json',ledger)
 ext={'schema_version':'kfm.v1','object_type':'SoilExternalFederationStatus','domain':'soil','reconciliation_id':rid,'federation_id':fid,'discovery_id':m['discovery_id'],'release_id':m['release_id'],'status':'accepted','public_advertising_allowed':True,'required_targets_accepted':True,'mirror_audit_passed':True,'retracted':False,'withdrawal_required':False,'created':utc_now_iso()}; write_json_atomic(tmp/'external_status.json',ext)
 write_json_atomic(tmp/'target_statuses.json',{'schema_version':'kfm.v1','object_type':'SoilExternalFederationTargetStatuses','targets':[{'target':e['target'],'required':e['required'],'ack_status':e['ack_status'],'public_accessible':e['public_accessible'],'external_record_url':e['external_record_url'],'policy_decision':'allow'} for e in entries]})
 write_json_atomic(tmp/'mirror_status.json',{'schema_version':'kfm.v1','object_type':'SoilExternalMirrorStatus','mirror_audit_passed':True,'audit_mode':'manifest_only','mirror_status':'ready','required_file_count':0,'checked_file_count':0,'no_private_paths':True,'no_forbidden_terms':True})
 write_json_atomic(tmp/'withdrawal_status.json',{'schema_version':'kfm.v1','object_type':'SoilExternalWithdrawalStatus','release_id':m['release_id'],'retracted':False,'withdrawal_required':False,'withdrawal_prepared':False,'target_withdrawals_prepared':False,'public_advertising_allowed':True})
 manifest={'schema_version':'kfm.v1','object_type':'SoilFederationReconciliationManifest','domain':'soil','reconciliation_id':rid,'federation_id':fid,'discovery_id':m['discovery_id'],'release_id':m['release_id'],'publication_status':'PUBLISHED','discovery_status':'DISCOVERABLE','federation_status':'FEDERATION_READY','reconciliation_status':'FEDERATION_RECONCILED','external_federation_state':'accepted','created':utc_now_iso(),'required_targets':req,'target_summary':{'accepted_count':len(req),'pending_count':0,'rejected_count':0,'withdrawn_count':0,'required_accepted':True},'source_refs':{},'records':sorted(m.get('records',[]),key=lambda r:r.get('bundle_id','')),'artifact_hashes':{},'policy_summary':{'reconciliation_allowed':True,'live_registry_poll_performed':False,'live_external_submission_performed':False}}
 write_json_atomic(tmp/'reconciliation_manifest.json',manifest)
 hashes={p.name:'sha256:'+sha256_file(p) for p in tmp.glob('*.json') if p.name!='reconciliation_receipt.json'};manifest['artifact_hashes']=hashes;write_json_atomic(tmp/'reconciliation_manifest.json',manifest)
 receipt={'schema_version':'kfm.v1','receipt_type':'FederationReconciliationReceipt','from_state':'FEDERATION_READY','to_state':'FEDERATION_RECONCILED','decision':'pass','domain':'soil','release_id':m['release_id'],'discovery_id':m['discovery_id'],'federation_id':fid,'reconciliation_id':rid,'created':utc_now_iso(),'live_registry_poll_performed':False,'live_external_submission_performed':False,'source_federation_receipt':{'ref':f'federation/soil/releases/{fid}/federation_receipt.json','sha256':'sha256:'+sha256_file(Path(x.federation_root)/f'federation/soil/releases/{fid}/federation_receipt.json')},'source_mirror_audit_receipt':{'ref':f'federation/soil/mirror_audits/{fid}.mirror_audit_receipt.json','sha256':'sha256:'+sha256_file(mar)},'source_submission_receipts':[{'target':t,'ref':f'federation/soil/submissions/{fid}/{t}.submission_receipt.json','sha256':'sha256:'+sha256_file(Path(x.submissions_root)/f'federation/soil/submissions/{fid}/{t}.submission_receipt.json')} for t in sorted(subs)],'source_ack_receipts':[{'target':t,'ref':f'federation/soil/acks/{fid}/{t}.ack_receipt.json','sha256':'sha256:'+sha256_file(Path(x.acks_root)/f'federation/soil/acks/{fid}/{t}.ack_receipt.json')} for t in sorted(acks)],'generated_artifacts':hashes,'policy_checks':{'reconciliation_allowed':True,'live_registry_poll_performed_false':True,'live_external_submission_performed_false':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 write_json_atomic(tmp/'reconciliation_receipt.json',receipt)
 outroot.parent.mkdir(parents=True,exist_ok=True)
 if outroot.exists():
  old=load_json(outroot/'reconciliation_manifest.json')
  if old.get('artifact_hashes')!=manifest.get('artifact_hashes'): print(json.dumps({'reconciliation_allowed':False,'federation_id':fid,'release_id':m.get('release_id'),'reasons':['existing reconciliation directory differs']})); return 1
 else: os.replace(tmp,outroot)
 write_json_atomic(Path(x.out_root)/'federation/soil/current_reconciliation.json',{'schema_version':'kfm.v1','object_type':'SoilCurrentFederationReconciliationPointer','domain':'soil','active_reconciliation_id':rid,'federation_id':fid,'discovery_id':m['discovery_id'],'release_id':m['release_id'],'reconciliation_status':'FEDERATION_RECONCILED','external_federation_state':'accepted','reconciliation_manifest_ref':f'reconciliations/{rid}/reconciliation_manifest.json','reconciliation_receipt_ref':f'reconciliations/{rid}/reconciliation_receipt.json','created':utc_now_iso()})
 print(json.dumps({'reconciliation_allowed':True,'reconciliation_id':rid,'federation_id':fid,'discovery_id':m['discovery_id'],'release_id':m['release_id'],'state_transition':'FEDERATION_READY->FEDERATION_RECONCILED','external_federation_state':'accepted','outputs':{'reconciliation':str(outroot)}},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
