#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json, shutil
from datetime import datetime, timezone, timedelta
from pathlib import Path
from tools.trust_registry.soil._trust_registry_common import *
from tools.validators.soil.certification_check import main as certification_check
from tools.validators.soil.trust_certification_gate import main as trust_gate

def main(argv=None):
 a=argparse.ArgumentParser()
 for n in ['certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root','out-root','base-public-url']: a.add_argument(f'--{n}',required=True)
 a.add_argument('--certification-id'); a.add_argument('--registry-id'); x=a.parse_args(argv)
 if not validate_base_public_url(x.base_public_url): print(json.dumps({'registry_allowed':False,'reasons':['invalid base_public_url']})); return 1
 cid=x.certification_id or load_current_certification(x.certification_root)['active_certification_id']
 if certification_check(['--certification-root',x.certification_root,'--certification-id',cid])!=0: print(json.dumps({'registry_allowed':False,'certification_id':cid,'reasons':['certification_check failed']})); return 1
 tg=trust_gate(['--certification-root',x.certification_root,'--archive-root',x.archive_root,'--preservation-root',x.preservation_root,'--reconciliation-root',x.reconciliation_root,'--federation-root',x.federation_root,'--discovery-root',x.discovery_root,'--published-root',x.published_root,'--ops-root',x.ops_root])
 if tg!=0: print(json.dumps({'registry_allowed':False,'certification_id':cid,'reasons':['trust_certification_gate failed']})); return 1
 m=load_certification_manifest(x.certification_root,cid); r=load_certification_receipt(x.certification_root,cid); c=load_control_matrix(x.certification_root,cid); rc=load_receipt_chain(x.certification_root,cid); pt=load_public_trust_report(x.certification_root,cid)
 release_id=m['release_id']; archive_package_id=m['archive_package_id']
 reasons=[]; ops=load_operational_status(x.ops_root)
 if r.get('decision')!='pass' or not r.get('signatures'): reasons.append('bad certification receipt')
 if any(i.get('required') and i.get('status')!='pass' for i in c.get('controls',[])): reasons.append('control failure')
 if rc.get('chain_integrity_passed') is not True: reasons.append('receipt chain failed')
 if release_is_retracted(x.published_root,release_id): reasons.append('retracted')
 if ops.get('public_access_allowed') is not True: reasons.append('public_access_blocked')
 if ops.get('latest_probe_decision') not in [None,'pass']: reasons.append('latest probe not pass')
 recs=sorted(m.get('records',[]),key=lambda z:z.get('bundle_id',''))
 for rr in recs:
  if rr.get('sensitivity')!='public' or rr.get('publication_status')!='PUBLISHED' or not is_public_rights(rr.get('rights_status')) or not rr.get('evidence_bundle_ref'): reasons.append('record public safety failure')
 if scan_payload_for_forbidden_terms({'m':m,'r':r,'pt':pt}): reasons.append('forbidden term')
 if reasons: print(json.dumps({'registry_allowed':False,'certification_id':cid,'release_id':release_id,'reasons':sorted(set(reasons))},sort_keys=True)); return 1
 src={
  'certification_manifest.json': sha256_file(Path(x.certification_root)/f'certification/soil/certifications/{cid}/certification_manifest.json'),
  'certification_receipt.json': sha256_file(Path(x.certification_root)/f'certification/soil/certifications/{cid}/certification_receipt.json'),
  'public_trust_report.json': sha256_file(Path(x.certification_root)/f'certification/soil/certifications/{cid}/public_trust_report.json'),
  'control_matrix.json': sha256_file(Path(x.certification_root)/f'certification/soil/certifications/{cid}/control_matrix.json'),
  'receipt_chain.json': sha256_file(Path(x.certification_root)/f'certification/soil/certifications/{cid}/receipt_chain.json')}
 rid=sanitize_id(x.registry_id) if x.registry_id else f"soil-registry-{stable_payload_hash({'cid':cid,'src':src})[:16]}"
 out=Path(x.out_root)/'trust_registry/soil/registrations'/rid; tmp=out.parent/(rid+'.tmp')
 if tmp.exists(): shutil.rmtree(tmp)
 tmp.mkdir(parents=True)
 created=utc_now_iso(); urls={k:public_url_join(x.base_public_url,f'trust_registry/soil/registrations/{rid}/{v}') for k,v in {'registry':'public_trust_registry_index.json','certificate':'trust_certificate.json','status':'certificate_status.json','verification_bundle':'verification_bundle.json','badge':'public_badge.json'}.items()}
 trlog_entries,root=build_hash_chain([{'event_type':'registered','object_type':'SoilTrustRegistryManifest','ref':'registry_manifest.json','sha256':'pending','created':created},{'event_type':'certified','object_type':'SoilTrustCertificate','ref':'trust_certificate.json','sha256':'pending','created':created}])
 tlog={'schema_version':'kfm.v1','object_type':'SoilTrustTransparencyLog','domain':'soil','registry_id':rid,'certification_id':cid,'release_id':release_id,'log_mode':'offline_deterministic_hash_chain','live_transparency_log_submission_performed':False,'entries':trlog_entries,'log_root':root,'created':created}
 cert={'schema_version':'kfm.v1','object_type':'SoilTrustCertificate','domain':'soil','registry_id':rid,'certification_id':cid,'release_id':release_id,'subject':{'title':m.get('title','Soil Release'),'release_id':release_id,'domain':'soil','public_landing_url':public_url_join(x.base_public_url,f'soil/releases/{release_id}/manifest')},'issuer':{'name':'Kansas Frontier Matrix','issuer_type':'kfm-governance-fixture'},'certificate_status':'active','trust_state':'TRUST_REGISTRY_READY','not_before':created,'review_due':(datetime.now(timezone.utc)+timedelta(days=365)).date().isoformat(),'certificate_claims':{'evidence_bound':True,'rights_checked':True,'sensitivity_public':True,'qa_passed':True,'provenance_verified':True,'receipt_chain_verified':True,'archive_fixity_passed':True,'steward_attestation_approved':True,'no_live_external_calls':True,'model_output_is_truth_source':False},'identifiers':{'registry_id':rid,'certification_id':cid,'archive_package_id':archive_package_id,'preservation_id':m.get('preservation_id'),'release_id':release_id},'hashes':{'certification_manifest_sha256':'sha256:'+src['certification_manifest.json'],'certification_receipt_sha256':'sha256:'+src['certification_receipt.json'],'public_trust_report_sha256':'sha256:'+src['public_trust_report.json'],'control_matrix_sha256':'sha256:'+src['control_matrix.json'],'receipt_chain_sha256':'sha256:'+src['receipt_chain.json'],'transparency_log_root':root},'public_urls':urls,'caveats':['KFM trust certification is not external legal or regulatory certification.','Canonical soil moisture units are m³/m³.','UI percent displays multiply by 100.','Satellite/grid and station probes may differ.'],'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 status={'schema_version':'kfm.v1','object_type':'SoilTrustCertificateStatus','domain':'soil','registry_id':rid,'certification_id':cid,'release_id':release_id,'certificate_status':'active','public_advertising_allowed':True,'status_reason':'initial_registration','status_events':[{'event_type':'registered','decision':'pass','ref':'registry_receipt.json','sha256':'pending','created':created}],'retracted':False,'suspended':False,'revoked':False,'tombstoned':False,'created':created}
 manifest={'schema_version':'kfm.v1','object_type':'SoilTrustRegistryManifest','domain':'soil','registry_id':rid,'certification_id':cid,'archive_package_id':archive_package_id,'preservation_id':m.get('preservation_id'),'reconciliation_id':m.get('reconciliation_id'),'federation_id':m.get('federation_id'),'discovery_id':m.get('discovery_id'),'release_id':release_id,'publication_status':'PUBLISHED','certification_status':'TRUST_CERTIFIED','trust_registry_status':'TRUST_REGISTRY_READY','certificate_status':'active','created':created,'base_public_url':x.base_public_url,'registry_scope':['KFM deterministic public trust registry','Offline verification bundle','Not an external legal, regulatory, CA, blockchain, or auditor registry'],'records':recs,'certificate_summary':{'subject':cert['subject'],'issuer':'Kansas Frontier Matrix','certificate_status':'active','trust_level':'kfm-governed-public','evidence_bound':True,'receipt_chain_verified':True,'controls_passed':True,'public_verification_available':True},'source_artifact_hashes':{k:'sha256:'+v for k,v in src.items()},'transparency_log_root':root,'policy_summary':{'registry_allowed':True},'truth_policy':{'observational_data_bound':True,'ai_interpretive_only':True,'model_output_is_truth_source':False}}
 vb={'schema_version':'kfm.v1','object_type':'SoilTrustVerificationBundle','domain':'soil','registry_id':rid,'certification_id':cid,'release_id':release_id,'verification_mode':'offline_deterministic','required_checks':['artifact_hashes_match','receipt_signatures_present','certificate_status_active','required_controls_pass','receipt_chain_integrity_passed','no_private_paths','no_forbidden_terms','public_rights','public_sensitivity','no_live_external_calls'],'artifacts':[],'records':recs,'verifier_instructions':['Run tools/trust_registry/soil/verify_trust_certificate.py against this registry root.','Fail closed on missing receipts, missing signatures, hash mismatch, suspended/revoked/tombstoned status, private paths, or forbidden terms.'],'created':created}
 idx={'schema_version':'kfm.v1','object_type':'SoilPublicTrustRegistryIndex','domain':'soil','registry_id':rid,'certification_id':cid,'release_id':release_id,'trust_registry_status':'TRUST_REGISTRY_READY','certificate_status':'active','public_advertising_allowed':True,'public_summary':'KFM governed public trust registry','records':recs,'public_urls':{'certificate':'trust_certificate.json','status':'certificate_status.json','verification_bundle':'verification_bundle.json','public_trust_report':'public_trust_report.json','badge':'public_badge.json'},'caveats':cert['caveats']}
 badge={'schema_version':'kfm.v1','object_type':'SoilTrustBadge','domain':'soil','registry_id':rid,'certification_id':cid,'release_id':release_id,'label':'KFM Trust Certified','status':'active','trust_state':'TRUST_REGISTRY_READY','evidence_bound':True,'verification_bundle_ref':'verification_bundle.json','certificate_status_ref':'certificate_status.json','badge_svg_ref':'badge.svg','public_advertising_allowed':True,'caveat':'KFM governance certification, not external legal certification.'}
 svg='<svg xmlns="http://www.w3.org/2000/svg" width="220" height="20"><rect width="220" height="20" fill="#1f2937"/><text x="8" y="14" fill="#fff" font-size="12">KFM Soil | Trust Certified | Active</text></svg>\n'
 vins={'schema_version':'kfm.v1','object_type':'SoilTrustVerifierInputs','domain':'soil','registry_id':rid,'certification_id':cid,'release_id':release_id,'expected_certificate_status':'active','expected_trust_registry_status':'TRUST_REGISTRY_READY','expected_transparency_log_root':root,'expected_controls':{'required_controls_all_pass':True},'expected_public_safety':{'rights_status_open':True,'sensitivity_public':True,'no_private_paths':True,'no_forbidden_terms':True},'created':created}
 files={'registry_manifest.json':manifest,'trust_certificate.json':cert,'certificate_status.json':status,'verification_bundle.json':vb,'transparency_log.json':tlog,'public_trust_registry_index.json':idx,'public_badge.json':badge,'verifier_inputs.json':vins}
 for fn,p in files.items(): write_json_atomic(tmp/fn,p)
 write_text_atomic(tmp/'badge.svg',svg)
 hashes={fn:'sha256:'+sha256_file(tmp/fn) for fn in list(files)+['badge.svg']}
 receipt={'schema_version':'kfm.v1','receipt_type':'TrustRegistryReceipt','from_state':'TRUST_CERTIFIED','to_state':'TRUST_REGISTRY_READY','decision':'pass','domain':'soil','release_id':release_id,'certification_id':cid,'archive_package_id':archive_package_id,'registry_id':rid,'created':created,'external_certificate_authority_submission_performed':False,'live_transparency_log_submission_performed':False,'blockchain_anchoring_performed':False,'generated_artifacts':hashes,'transparency_log_root':root,'policy_checks':{'registry_allowed':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 write_json_atomic(tmp/'registry_receipt.json',receipt)
 if out.exists():
  old=load_json(out/'registry_manifest.json');
  if stable_payload_hash(old)!=stable_payload_hash(manifest): print(json.dumps({'registry_allowed':False,'reasons':['existing registry differs']})); return 1
 else: shutil.move(str(tmp),str(out))
 write_json_atomic(Path(x.out_root)/'trust_registry/soil/current_registry.json',{'schema_version':'kfm.v1','object_type':'SoilCurrentTrustRegistryPointer','domain':'soil','active_registry_id':rid,'certification_id':cid,'archive_package_id':archive_package_id,'release_id':release_id,'trust_registry_status':'TRUST_REGISTRY_READY','certificate_status':'active','registry_manifest_ref':f'trust_registry/soil/registrations/{rid}/registry_manifest.json','registry_receipt_ref':f'trust_registry/soil/registrations/{rid}/registry_receipt.json','certificate_status_ref':f'trust_registry/soil/registrations/{rid}/certificate_status.json','created':created})
 print(json.dumps({'registry_allowed':True,'registry_id':rid,'certification_id':cid,'archive_package_id':archive_package_id,'release_id':release_id,'state_transition':'TRUST_CERTIFIED->TRUST_REGISTRY_READY','outputs':{k:str(out/k) for k in ['registry_manifest.json','trust_certificate.json','certificate_status.json','verification_bundle.json','transparency_log.json','public_trust_registry_index.json','public_badge.json','badge.svg','verifier_inputs.json','registry_receipt.json']}},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
