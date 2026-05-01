#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
from datetime import datetime, timezone

def sh(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def cid(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:16]

def parse(a):
 p=argparse.ArgumentParser(prog='kfm-ebird-consumer-upgrade')
 p.add_argument('--mode',default='plan',choices=['plan','pack','validate','notice','diff','report'])
 p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
 p.add_argument('--consumer-impact-report'); p.add_argument('--consumer-compatibility-matrix'); p.add_argument('--consumer-id',action='append',default=[])
 p.add_argument('--out-dir'); p.add_argument('--public-out-dir'); p.add_argument('--force',action='store_true'); p.add_argument('--dry-run',action='store_true'); p.add_argument('--version',action='store_true')
 return p.parse_args(a)

def main():
 a=parse(sys.argv[1:])
 if a.version: print(json.dumps({'adapter':'kfm-ebird','tool':'consumer-upgrade','version':'29.0.0'})); return
 payload={'aggregate_targets':a.aggregate,'consumer_ids':sorted(a.consumer_id),'adapter_version':'29.0.0'}
 if a.consumer_impact_report: payload['consumer_impact_report_sha256']=sh(a.consumer_impact_report)
 if a.consumer_compatibility_matrix: payload['consumer_compatibility_matrix_sha256']=sh(a.consumer_compatibility_matrix)
 upid=cid(payload)
 if a.dry_run: print(json.dumps({'upgrade_pack_id':upid})); return
 out=Path(a.out_dir or f'data/catalog/fauna/ebird/consumer-upgrades/{upid}')
 if out.exists() and any(out.iterdir()) and not a.force: raise SystemExit('--force required to overwrite out-dir')
 out.mkdir(parents=True,exist_ok=True)
 now=datetime.now(timezone.utc).isoformat()
 plan={'schema_version':'v1','object_type':'KfmEbirdConsumerUpgradePlan','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'consumer_upgrade','public_safe_final_outputs':True,'exact_points':'restricted','upgrade_pack_id':upid,'aggregate_targets':a.aggregate,'targeted_consumers':[],'global_steps':['refresh_mock_control_plane_fixtures','update_sdk_local_package','update_consumer_contracts','rerun_integration_audit','rerun_consumer_certification','verify_public_safety'],'prohibited_steps':['access_exact_points','access_restricted_observations','access_quarantines','access_suppression_receipts','access_suppressed_group_hashes','remove_governance_fields','require_credentials','require_network','claim_population_trends','claim_occupancy','claim_true_absence','claim_abundance','claim_causal_inference'],'generated_at':now}
 (out/'consumer_upgrade_plan.json').write_text(json.dumps(plan,indent=2)+"\n")
 (out/'consumer_notification_pack.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdConsumerNotificationPack','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'consumer_upgrade','public_safe_final_outputs':True,'exact_points':'restricted','upgrade_pack_id':upid,'local_only':True,'delivery_performed':False,'notifications':[],'generated_at':now},indent=2)+"\n")
 if a.public_out_dir:
  pub=Path(a.public_out_dir); pub.mkdir(parents=True,exist_ok=True)
  (pub/'public_consumer_upgrade_notice.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicKfmEbirdConsumerUpgradeNotice','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','upgrade_pack_id':upid,'aggregate_targets':a.aggregate,'notice_type':'mixed','summary':'Local-only consumer upgrade notice generated.','recommended_public_actions':['refresh_local_mock_fixtures','refresh_local_sdk','rerun_integration_audit','rerun_consumer_certification'],'public_safety_summary':{'exact_points_restricted':True,'aggregate_only_public_outputs':True,'no_restricted_observations_public':True,'no_suppression_receipts_public':True,'no_suppressed_group_details_public':True,'no_raw_rows_public':True},'generated_at':now},indent=2)+"\n")
 print(str(out))
if __name__=='__main__': main()
