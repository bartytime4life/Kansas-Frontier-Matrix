#!/usr/bin/env python
import argparse,json
from pathlib import Path
from _assurance_common import *
def main():
 p=argparse.ArgumentParser();[p.add_argument(x,required=True) for x in ('--closure-dir','--handoff-dir','--cutover-dir','--delivery-dir','--out-dir')];p.add_argument('--as-of');p.add_argument('--allow-fixture-assurance',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 cd,hd,dd=Path(a.closure_dir),Path(a.handoff_dir),Path(a.delivery_dir)
 req=[cd/'release_closure_dossier.json',cd/'evidence_archive_manifest.json',hd/'operational_handoff_package.json',hd/'watch_window_evaluation.json',Path(a.cutover_dir)/'release_ledger_manifest.json',dd/'client_delivery_manifest.json']
 if any(not x.exists() for x in req): print('DENY'); return 1
 out={"schema_version":"1.0.0","assurance_plan_id":"cap-"+h(ts(a.as_of))[:12],"domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"release_closure_dossier_ref":str(req[0]),"operational_handoff_package_ref":str(req[2]),"evidence_archive_manifest_ref":str(req[1]),"release_ledger_manifest_ref":str(req[4]),"watch_window_evaluation_ref":str(req[3]),"client_delivery_manifest_ref":str(req[5]),"assurance_objectives":["fixture governance"],"recertification_schedule":["metadata-only"],"archive_integrity_schedule":["metadata-only"],"runbook_review_schedule":["metadata-only"],"drift_observation_schedule":["metadata-only"],"maintenance_review_schedule":["metadata-only"],"evidence_refs":[str(x) for x in req],"forbidden_actions":["no live ops"],"safety_checks":[{"name":"no_network","pass":True}],"status":"fixture_assurance_plan"}
 if bad_text(out): print('DENY'); return 1
 od=Path(a.out_dir);evt={"schema_version":"1.0.0","event_id":"evt-"+h(out)[:12],"domain":"atmosphere.air","event_type":"continuous_assurance_plan_created","created_at":ts(a.as_of),"as_of":ts(a.as_of),"actor":"fixture-actor-non-production","subject_refs":[str(od/'continuous_assurance_plan.json')],"evidence_refs":out['evidence_refs'],"result":"pass","details":{}}
 if not a.dry_run:
  w(od/'continuous_assurance_plan.json',out)
  (od/'continuous_assurance_events.jsonl').write_text(json.dumps(evt,sort_keys=True)+'\n')
 print('PASS'); return 0
if __name__=='__main__': raise SystemExit(main())
