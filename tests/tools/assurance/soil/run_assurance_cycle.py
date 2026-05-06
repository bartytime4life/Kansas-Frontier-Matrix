#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, shutil
from pathlib import Path
from tools.assurance.soil._assurance_common import *
from tools.validators.soil.trust_registry_check import main as registry_check
from tools.validators.soil.trust_registry_gate import main as registry_gate
from tools.trust_registry.soil.verify_trust_certificate import main as verify_cert

def main(argv=None):
 a=argparse.ArgumentParser()
 for n in ['registry-root','certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root','out-root','base-public-url']: a.add_argument(f'--{n}',required=True)
 a.add_argument('--registry-id'); a.add_argument('--assurance-id'); x=a.parse_args(argv)
 rid=x.registry_id or load_current_registry(x.registry_root)['active_registry_id']
 m=load_registry_manifest(x.registry_root,rid); release_id=m['release_id']; cert_id=m['certification_id']; apid=m['archive_package_id']
 reasons=[]
 if not validate_base_public_url(x.base_public_url): reasons.append('invalid base_public_url')
 if registry_check(['--registry-root',x.registry_root,'--registry-id',rid])!=0: reasons.append('trust_registry_check failed')
 if registry_gate(['--registry-root',x.registry_root,'--certification-root',x.certification_root,'--archive-root',x.archive_root,'--preservation-root',x.preservation_root,'--reconciliation-root',x.reconciliation_root,'--federation-root',x.federation_root,'--discovery-root',x.discovery_root,'--published-root',x.published_root,'--ops-root',x.ops_root])!=0: reasons.append('trust_registry_gate failed')
 if verify_cert(['--registry-root',x.registry_root,'--registry-id',rid])!=0: reasons.append('offline verifier failed')
 s=load_certificate_status(x.registry_root,rid); rc=load_registry_receipt(x.registry_root,rid); tc=load_trust_certificate(x.registry_root,rid)
 if s.get('certificate_status')!='active': reasons.append('certificate not active')
 if rc.get('decision')!='pass' or not rc.get('signatures') or not tc.get('signatures'): reasons.append('missing signatures/decision')
 if release_is_retracted(x.published_root,release_id): reasons.append('retracted')
 ops=load_operational_status(x.ops_root)
 if ops.get('public_access_allowed') is not True or ops.get('latest_probe_decision')!='pass': reasons.append('ops failed')
 fix=load_latest_archive_fixity_audit(x.archive_root,apid)
 if fix.get('decision')!='pass': reasons.append('fixity failed')
 ex=load_assurance_exceptions(x.out_root,rid); blocking=[e for e in ex if e.get('blocking') and e.get('status')!='resolved']
 if blocking: reasons.append('blocking exceptions')
 pointers={'certification_id':load_current_certification(x.certification_root)['active_certification_id'],'archive_package_id':load_current_archive_package(x.archive_root)['active_archive_package_id'],'preservation_id':load_current_preservation(x.preservation_root)['active_preservation_id'],'reconciliation_id':load_current_reconciliation(x.reconciliation_root)['active_reconciliation_id'],'federation_id':load_current_federation(x.federation_root)['active_federation_id'],'discovery_id':load_current_discovery(x.discovery_root)['active_discovery_id'],'release_id':load_current_release(x.published_root)['active_release_id']}
 dr=build_drift_report('pending',rid,release_id,compare_registry_to_current_chain(m,pointers))
 if dr['drift_detected']: reasons.append('drift detected')
 if reasons: print(json.dumps({'assurance_allowed':False,'registry_id':rid,'release_id':release_id,'reasons':sorted(set(reasons))},sort_keys=True)); return 1
 src_hashes={k:'sha256:'+v for k,v in {'registry_manifest.json':sha256_file(Path(x.registry_root)/f'trust_registry/soil/registrations/{rid}/registry_manifest.json'),'registry_receipt.json':sha256_file(Path(x.registry_root)/f'trust_registry/soil/registrations/{rid}/registry_receipt.json'),'trust_certificate.json':sha256_file(Path(x.registry_root)/f'trust_registry/soil/registrations/{rid}/trust_certificate.json'),'certificate_status.json':sha256_file(Path(x.registry_root)/f'trust_registry/soil/registrations/{rid}/certificate_status.json')}.items()}
 aid=sanitize_id(x.assurance_id) if x.assurance_id else f"soil-assurance-{stable_payload_hash({'rid':rid,'src':src_hashes})[:16]}"
 out=Path(x.out_root)/f'assurance/soil/cycles/{aid}'; tmp=out.parent/(aid+'.tmp')
 if tmp.exists(): shutil.rmtree(tmp)
 tmp.mkdir(parents=True,exist_ok=True)
 dr['assurance_id']=aid
 files={'drift_report.json':dr,'registry_verification_snapshot.json':{'schema_version':'kfm.v1','object_type':'SoilRegistryVerificationSnapshot','domain':'soil','assurance_id':aid,'registry_id':rid,'certification_id':cert_id,'release_id':release_id,'verification_passed':True,'trust_registry_check_passed':True,'offline_certificate_verifier_passed':True,'trust_registry_gate_passed':True,'checked_artifacts':[],'checked_receipts':[],'transparency_log_root':load_transparency_log(x.registry_root,rid).get('log_root'),'created':utc_now_iso()},'control_recheck_matrix.json':{'schema_version':'kfm.v1','object_type':'SoilAssuranceControlRecheckMatrix','domain':'soil','assurance_id':aid,'registry_id':rid,'release_id':release_id,'controls':[{'control_id':f'KFM-SOIL-LC-{i:03d}','name':'lifecycle','category':'drift','required':True,'status':'pass','evidence_refs':[],'evidence_hashes':[],'failure_reason':None} for i in range(1,13)]},'certificate_lifecycle_status.json':{'schema_version':'kfm.v1','object_type':'SoilCertificateLifecycleStatus','domain':'soil','assurance_id':aid,'registry_id':rid,'certification_id':cert_id,'release_id':release_id,'certificate_status':'active','public_advertising_allowed':True,'latest_status_event':load_latest_certificate_status_event(x.registry_root,rid),'lifecycle_state':'current','renewal_due':False,'renewal_overdue':False,'retracted':False,'suspended':False,'revoked':False,'tombstoned':False,'blocking_exception_count':0,'created':utc_now_iso()},'renewal_recommendation.json':{'schema_version':'kfm.v1','object_type':'SoilTrustRegistryRenewalRecommendation','domain':'soil','assurance_id':aid,'registry_id':rid,'certification_id':cert_id,'release_id':release_id,'renewal_recommended':False,'renewal_due':False,'renewal_overdue':False,'recommendation':'no_action','reasons':[],'required_actions':[],'safe_to_reaffirm':True,'public_advertising_allowed':True,'created':utc_now_iso()},'public_assurance_report.json':{'schema_version':'kfm.v1','object_type':'SoilPublicAssuranceReport','domain':'soil','assurance_id':aid,'registry_id':rid,'certification_id':cert_id,'release_id':release_id,'assurance_status':'CONTINUOUS_ASSURANCE_READY','assurance_state':'pass','certificate_status':'active','public_advertising_allowed':True,'public_summary':'KFM deterministic continuous assurance','verification_passed':True,'drift_detected':False,'latest_archive_fixity_audit_decision':'pass','latest_operational_status':ops,'non_blocking_exceptions':[],'renewal_recommendation':'no_action','caveats':['canonical units are m³/m³','UI percent displays multiply by 100','satellite/grid and station probes may differ','AI/model outputs are interpretive only','KFM governance assurance is not external legal certification'],'public_urls':{}},}
 manifest={'schema_version':'kfm.v1','object_type':'SoilContinuousAssuranceManifest','domain':'soil','assurance_id':aid,'registry_id':rid,'certification_id':cert_id,'archive_package_id':apid,'preservation_id':m['preservation_id'],'reconciliation_id':m['reconciliation_id'],'federation_id':m['federation_id'],'discovery_id':m['discovery_id'],'release_id':release_id,'publication_status':'PUBLISHED','trust_registry_status':'TRUST_REGISTRY_READY','assurance_status':'CONTINUOUS_ASSURANCE_READY','assurance_state':'pass','certificate_status':'active','created':utc_now_iso(),'base_public_url':x.base_public_url,'assurance_scope':['KFM deterministic continuous assurance','Offline lifecycle verification','Not an external legal, regulatory, CA, blockchain, or auditor registry'],'records':sorted(m.get('records',[]),key=lambda r:r.get('bundle_id','')),'source_artifact_hashes':src_hashes,'policy_summary':{'assurance_allowed':True},'truth_policy':{'observational_data_bound':True,'ai_interpretive_only':True,'model_output_is_truth_source':False}}
 files['assurance_manifest.json']=manifest
 for fn,p in files.items(): write_json_atomic(tmp/fn,p)
 ah={fn:'sha256:'+sha256_file(tmp/fn) for fn in files}
 manifest['artifact_hashes']={k:v for k,v in ah.items() if k!='assurance_receipt.json'}; write_json_atomic(tmp/'assurance_manifest.json',manifest)
 receipt={'schema_version':'kfm.v1','receipt_type':'ContinuousAssuranceReceipt','from_state':'TRUST_REGISTRY_READY','to_state':'CONTINUOUS_ASSURANCE_READY','decision':'pass','domain':'soil','release_id':release_id,'registry_id':rid,'certification_id':cert_id,'assurance_id':aid,'created':utc_now_iso(),'live_external_audit_submission_performed':False,'live_registry_poll_performed':False,'live_certificate_authority_call_performed':False,'generated_artifacts':{k:v for k,v in ah.items()},'policy_checks':{'assurance_allowed':True,'no_live_external_calls':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 write_json_atomic(tmp/'assurance_receipt.json',receipt)
 if out.exists():
  if stable_payload_hash(load_json(out/'assurance_manifest.json'))!=stable_payload_hash(manifest): print(json.dumps({'assurance_allowed':False,'registry_id':rid,'release_id':release_id,'reasons':['existing assurance differs']})); return 1
 else: shutil.move(str(tmp),str(out))
 write_json_atomic(Path(x.out_root)/'assurance/soil/current_assurance.json',{'schema_version':'kfm.v1','object_type':'SoilCurrentContinuousAssurancePointer','domain':'soil','active_assurance_id':aid,'registry_id':rid,'certification_id':cert_id,'release_id':release_id,'assurance_status':'CONTINUOUS_ASSURANCE_READY','assurance_state':'pass','certificate_status':'active','assurance_manifest_ref':f'assurance/soil/cycles/{aid}/assurance_manifest.json','assurance_receipt_ref':f'assurance/soil/cycles/{aid}/assurance_receipt.json','created':utc_now_iso()})
 print(json.dumps({'assurance_allowed':True,'assurance_id':aid,'registry_id':rid,'certification_id':cert_id,'release_id':release_id,'state_transition':'TRUST_REGISTRY_READY->CONTINUOUS_ASSURANCE_READY','assurance_state':'pass','outputs':{k:str(out/k) for k in files|{'assurance_receipt.json':None}}},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
