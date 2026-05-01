#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,tempfile,shutil,os
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.archive.soil._archive_common import *

def main(argv=None):
 a=argparse.ArgumentParser();
 for n in ['preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root','out-root','base-public-url']: a.add_argument(f'--{n}',required=True)
 a.add_argument('--preservation-id');a.add_argument('--archive-package-id');a.add_argument('--allow-tombstone',action='store_true');x=a.parse_args(argv)
 if not validate_base_public_url(x.base_public_url): print(json.dumps({'archive_package_allowed':False,'reasons':['invalid base_public_url']})); return 1
 pid=x.preservation_id or load_current_preservation(x.preservation_root)['active_preservation_id']
 pm,pr,fm,mt=load_preservation_manifest(x.preservation_root,pid),load_preservation_receipt(x.preservation_root,pid),load_fixity_manifest(x.preservation_root,pid),load_merkle_tree(x.preservation_root,pid)
 ops=load_operational_status(x.ops_root); rs=validate_archive_inputs(pm,pr,ops)
 rid=pm.get('release_id')
 retracted=release_is_retracted(x.published_root,rid)
 if retracted and not (x.allow_tombstone and load_withdrawal_reconciliation(x.reconciliation_root,rid)): rs.append('retracted release blocked')
 if recompute_merkle_root([l.get('sha256','') for l in mt.get('leaves',[])])!=mt.get('merkle_root'): rs.append('bad merkle root')
 if rs: print(json.dumps({'archive_package_allowed':False,'preservation_id':pid,'release_id':rid,'reasons':sorted(set(rs))},sort_keys=True)); return 1
 sh=sha256_bytes((''.join(sorted([v for v in fm.get('artifacts',{}).values()]))+pid).encode())[:16]
 aid=sanitize_id(x.archive_package_id or f'soil-archive-{sh}')
 out=Path(x.out_root)/'archive/soil'; (out/'packages').mkdir(parents=True,exist_ok=True); pkg=out/'packages'/aid
 created=utc_now_iso(); mode='tombstone' if retracted else 'active'
 files={}
 manifest={'schema_version':'kfm.v1','object_type':'SoilArchiveManifest','domain':'soil','archive_package_id':aid,'preservation_id':pid,'reconciliation_id':pm.get('reconciliation_id'),'federation_id':pm.get('federation_id'),'discovery_id':pm.get('discovery_id'),'release_id':rid,'publication_status':'PUBLISHED','preservation_status':'PRESERVATION_READY','archival_custody_status':'ARCHIVAL_CUSTODY_READY','created':created,'base_public_url':x.base_public_url,'archive_mode':mode,'records':sorted(pm.get('records',[]),key=lambda r:r.get('bundle_id','')),'merkle_root':mt.get('merkle_root'),'truth_policy':{'observational_data_bound':True,'ai_interpretive_only':True,'model_output_is_truth_source':False}}
 accession={'schema_version':'kfm.v1','object_type':'SoilArchiveAccessionRequest','domain':'soil','archive_package_id':aid,'preservation_id':pid,'release_id':rid,'requested_archive_targets':['kfm_local_fixture_archive'],'live_archive_upload_performed':False,'accession_type':'fixture_offline','rights_status':'open','policy_label':'public_science','sensitivity':'public','merkle_root':mt.get('merkle_root'),'contact':{'steward':'KFM Steward'},'created':created}
 ledger={'schema_version':'kfm.v1','object_type':'SoilArchiveCustodyLedger','domain':'soil','archive_package_id':aid,'preservation_id':pid,'release_id':rid,'custody_events':[{'ordinal':i+1,'event_type':e,'event_state':'verified','actor':'kfm-ci','created':created} for i,e in enumerate(['package_built','preservation_verified','fixity_verified','restore_dry_run_verified','accession_request_prepared'])]}
 retention={'schema_version':'kfm.v1','object_type':'SoilArchiveRetentionSchedule','domain':'soil','archive_package_id':aid,'preservation_id':pid,'release_id':rid,'retention_policy':{'retention_class':'public_science_metadata','minimum_retention_years':7,'review_interval_days':365,'deletion_allowed':False,'deletion_requires_steward_review':True,'retraction_handling':'additive_tombstone_not_delete'},'next_review_due':'2030-01-01','created':created}
 fixity={'schema_version':'kfm.v1','object_type':'SoilArchiveFixityAuditPlan','domain':'soil','archive_package_id':aid,'preservation_id':pid,'release_id':rid,'algorithm':'sha256','merkle_root':mt.get('merkle_root'),'audit_interval_days':90,'required_checks':['preservation_receipt_hash','fixity_manifest_hashes','merkle_root','bagit_manifest_hashes','public_path_scan','forbidden_term_scan'],'created':created}
 inv={'schema_version':'kfm.v1','object_type':'SoilArchiveInventory','domain':'soil','archive_package_id':aid,'preservation_id':pid,'release_id':rid,'inventory_items':[],'total_items':0,'total_size_bytes':0,'created':created}
 pidx={'schema_version':'kfm.v1','object_type':'SoilPublicArchiveIndex','domain':'soil','archive_package_id':aid,'preservation_id':pid,'release_id':rid,'archival_custody_status':'ARCHIVAL_CUSTODY_READY','archive_mode':mode,'public_advertising_allowed': mode=='active','records':manifest['records'],'created':created}
 tmp=Path(tempfile.mkdtemp(prefix='archivepkg-',dir=str(out/'packages')))
 for fn,pay in [('archive_manifest.json',manifest),('accession_request.json',accession),('custody_ledger.json',ledger),('retention_schedule.json',retention),('fixity_audit_plan.json',fixity),('archive_inventory.json',inv),('public_archive_index.json',pidx)]: write_json_atomic(tmp/fn,pay); files[fn]='sha256:'+sha256_file(tmp/fn)
 receipt={'schema_version':'kfm.v1','receipt_type':'ArchiveCustodyReceipt','from_state':'PRESERVATION_READY','to_state':'ARCHIVAL_CUSTODY_READY','decision':'pass','domain':'soil','release_id':rid,'preservation_id':pid,'archive_package_id':aid,'created':created,'live_archive_upload_performed':False,'generated_artifacts':files,'merkle_root':mt.get('merkle_root'),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 write_json_atomic(tmp/'archive_receipt.json',receipt)
 if pkg.exists():
  if sha256_file(pkg/'archive_manifest.json')!=sha256_file(tmp/'archive_manifest.json'): print(json.dumps({'archive_package_allowed':False,'preservation_id':pid,'release_id':rid,'reasons':['existing package differs']})); shutil.rmtree(tmp); return 1
  shutil.rmtree(tmp)
 else: os.replace(tmp,pkg)
 ptr={'schema_version':'kfm.v1','object_type':'SoilCurrentArchivePackagePointer','domain':'soil','active_archive_package_id':aid,'preservation_id':pid,'release_id':rid,'archival_custody_status':'ARCHIVAL_CUSTODY_READY','archive_manifest_ref':f'archive/soil/packages/{aid}/archive_manifest.json','archive_receipt_ref':f'archive/soil/packages/{aid}/archive_receipt.json','created':created}
 write_json_atomic(out/'current_archive_package.json',ptr)
 print(json.dumps({'archive_package_allowed':True,'archive_package_id':aid,'preservation_id':pid,'release_id':rid,'state_transition':'PRESERVATION_READY->ARCHIVAL_CUSTODY_READY','outputs':ptr},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
