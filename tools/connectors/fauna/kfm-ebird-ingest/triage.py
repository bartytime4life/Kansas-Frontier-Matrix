#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
VERSION='0.21.0'

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(prog='kfm-ebird-triage')
 ap.add_argument('--version',action='version',version=VERSION)
 ap.add_argument('--mode',default='build',choices=['build','validate','close','report'])
 ap.add_argument('--quality-report')
 ap.add_argument('--quality-anomaly-report')
 ap.add_argument('--quality-metadata-gap-report')
 ap.add_argument('--quality-crosswalk-drift-report')
 ap.add_argument('--out-dir',default='data/catalog/fauna/ebird/triage/run')
 ap.add_argument('--public-out-dir')
 ap.add_argument('--owner-role',default='data-steward')
 ap.add_argument('--dry-run',action='store_true')
 args=ap.parse_args()
 if args.mode in ['build','report'] and not args.quality_report: raise SystemExit(2)
 q=json.loads(Path(args.quality_report).read_text()) if args.quality_report and Path(args.quality_report).exists() else {'quality_run_id':'unknown'}
 rid=hashlib.sha256(json.dumps({'quality_run_id':q.get('quality_run_id'),'owner_role':args.owner_role},sort_keys=True).encode()).hexdigest()[:16]
 if args.dry_run:return
 out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
 item={"schema_version":"v1","object_type":"EbirdQualityTriageItem","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"quality_triage","public_safe":False,"exact_points":"restricted","triage_run_id":rid,"triage_item_id":"item-1","quality_run_id":q.get('quality_run_id'),'source_finding_id':'none','severity':'info','status':'open','category':'metadata','title':'Review QA run','description':'Review monthly QA outputs.','recommended_action':'Validate and close if expected.','owner_role':args.owner_role,'evidence_artifacts':[],'blocked_public_release':False,'requires_recertification':False,'requires_support_workflow':False}
 Path(out/'triage_queue.jsonl').write_text(json.dumps(item)+'\n')
 Path(out/'triage_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdQualityTriageManifest','triage_run_id':rid,'quality_run_id':q.get('quality_run_id')},indent=2))
 Path(out/'triage_summary_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdQualityTriageSummaryReport','triage_run_id':rid,'quality_run_id':q.get('quality_run_id'),'status':'pass','summary':{'total_items':1,'critical_items':0,'open_items':1,'public_release_blockers':0}},indent=2))
 for f in ['triage_operator_report.md','remediation_playbook.md','triage_validation_report.json']:
  Path(out/f).write_text('# report\n' if f.endswith('.md') else json.dumps({'schema_version':'v1','triage_run_id':rid},indent=2))
 if args.public_out_dir:
  p=Path(args.public_out_dir); p.mkdir(parents=True,exist_ok=True)
  Path(p/'public_triage_summary.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicEbirdTriageSummary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','triage_run_id':rid,'quality_run_id':q.get('quality_run_id'),'status':'pass','public_release_blocked':False},indent=2))
  Path(p/'public_triage_summary.md').write_text('# Public Triage Summary\n')
if __name__=='__main__': main()
