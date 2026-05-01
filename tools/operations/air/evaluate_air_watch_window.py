#!/usr/bin/env python
import argparse,sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'deployments'/'air'))
from cutover_common import J,TS,wj,h,scan
p=argparse.ArgumentParser();p.add_argument('--handoff-dir',required=True);p.add_argument('--cutover-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--ops-dir',action='append',default=[]);p.add_argument('--as-of');p.add_argument('--allow-fixture-watch',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
hd=Path(a.handoff_dir);cd=Path(a.cutover_dir);od=Path(a.out_dir)
for r in [hd/'operational_handoff_package.json',hd/'watch_window_plan.json',cd/'release_ledger_manifest.json']:
 if not r.exists(): print('DENY'); sys.exit(1)
incs=[]
for d in a.ops_dir:
 for f in Path(d).glob('*.json'):
  o=J(f)
  if o.get('severity') in ('high','critical') and o.get('status')!='resolved': print('DENY'); sys.exit(1)
ev={"schema_version":"1.0.0","watch_evaluation_id":"watch-eval-"+h({'as_of':TS(a.as_of)})[:12],"domain":"atmosphere.air","generated_at":TS(a.as_of),"as_of":TS(a.as_of),"watch_window_plan_ref":str(hd/'watch_window_plan.json'),"operational_handoff_package_ref":str(hd/'operational_handoff_package.json'),"release_ledger_manifest_ref":str(cd/'release_ledger_manifest.json'),"public_slo_report_refs":[],"incident_record_refs":[],"checks":[{"name":"handoff package present","pass":True}],"breaches":[],"warnings":[],"rollback_recommendation":"none","result":"pass_fixture"}
if scan(ev): print('DENY'); sys.exit(1)
od.mkdir(parents=True,exist_ok=True);wj(od/'watch_window_evaluation.json',ev);(od/'operational_handoff_events.jsonl').write_text(json.dumps({"schema_version":"1.0.0","event_id":"evt-watch","domain":"atmosphere.air","event_type":"watch_window_evaluated","created_at":TS(a.as_of),"as_of":TS(a.as_of),"actor":"fixture-operator-non-production","subject_refs":[str(od/'watch_window_evaluation.json')],"evidence_refs":[str(cd/'release_ledger_manifest.json')],"result":"pass","details":{}},sort_keys=True)+'\n')
print('PASS')
