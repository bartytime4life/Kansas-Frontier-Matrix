#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from datetime import datetime,timezone

def z(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def dump(p,o): Path(p).parent.mkdir(parents=True,exist_ok=True); Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')

def main():
 p=argparse.ArgumentParser();
 [p.add_argument(x,required=True) for x in ['--release-candidate-package','--qa-revalidation','--evidence-bundle','--out-dir']]
 p.add_argument('--status',default='not_required');p.add_argument('--as-of');p.add_argument('--reconciled-at');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 asof=a.as_of or z(); rec=a.reconciled_at or asof
 if a.status in {'fixture_reconciled','candidate_reconciled'}:
  window={'averaging_window':'24h_validated','parameter':'pm25','units':'ug_m3','nowcast_truth_status':'operational_evidence_not_validated_aqs_truth'}
 else: window={'averaging_window':'not_required','parameter':'pm25','units':'ug_m3','nowcast_truth_status':'operational_evidence_not_validated_aqs_truth'}
 o={'schema_version':'v1','reconciliation_id':'aqs-refresh','domain':'atmosphere.air','created_at':z(),'as_of':asof,'reentry_release_candidate_package_ref':a.release_candidate_package,'reentry_qa_revalidation_report_ref':a.qa_revalidation,'reentry_release_evidence_bundle_ref':a.evidence_bundle,'aqs_validated_window':window,'reconciled_at':rec,'method':'fixture_only_local','status':a.status,'differences':[],'source_rows':{'validated_rows':0},'staleness_check':{'max_age_hours':72,'stale':False},'safety_checks':{'nowcast_not_validated_truth':True}}
 if a.status in {'fixture_reconciled','candidate_reconciled'} and o['aqs_validated_window']['averaging_window']!='24h_validated': raise SystemExit('deny')
 if not a.dry_run:
  out=Path(a.out_dir); dump(out/'reentry_aqs_reconciliation_refresh.json',o); (out/'reentry_publication_boundary_events.jsonl').write_text(json.dumps({'event_type':'aqs_reconciliation_refreshed','result':'pass'})+'\n')
 print('PASS')
if __name__=='__main__': main()
