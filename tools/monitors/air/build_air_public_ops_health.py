#!/usr/bin/env python3
import argparse, json, hashlib, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone

def ts(v=None): return v or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def load(p): return json.loads(Path(p).read_text())
def dump(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n")
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--read-model-dir',action='append',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--publication-dir',action='append'); ap.add_argument('--as-of'); ap.add_argument('--max-index-age-hours',type=int,default=24); ap.add_argument('--allow-fixture-ops',action='store_true'); ap.add_argument('--dry-run',action='store_true')
 a=ap.parse_args(); out=Path(a.out_dir); incidents=[]; warnings=[]; checks={}
 rd=Path(a.read_model_dir[0]); pd=Path((a.publication_dir or [a.read_model_dir[0]])[0])
 cmd=[sys.executable,'tools/auditors/air/replay_air_lineage.py','--read-model-dir',str(rd),'--publication-dir',str(pd),'--out-dir',str(out/'lineage'),'--as-of',ts(a.as_of)]
 if a.allow_fixture_ops: cmd.append('--allow-fixture')
 if a.dry_run: cmd.append('--dry-run')
 r=subprocess.run(cmd,capture_output=True,text=True)
 payload=json.loads(r.stdout.strip().splitlines()[-1]) if r.stdout.strip() else {"result":"deny","deny":["lineage_runtime_error"]}
 checks['lineage_replay_passed']=payload['result']=='pass'; hard=payload.get('deny',[])
 idx=rd/'public_index.json'; st=rd/'public_status.json'; pman=pd/'publication_manifest.json'
 checks['public_read_model_present']=idx.exists() and st.exists(); checks['publication_manifest_present']=pman.exists(); checks['hashes_verified']='missing_sha256' not in hard
 checks['no_raw_work_quarantine_refs']=not any('unsafe_ref' in d for d in hard); checks['no_direct_processed_exposure']='unsafe_ref' not in ''.join(hard)
 checks['no_fixture_real_public_promotion']='fixture_real_public_truth' not in hard; checks['no_active_tombstoned_publication']='retracted_active' not in ''.join(hard)
 checks['nowcast_labelled_operational']='nowcast_labelled_validated_truth' not in hard; checks['nowcast_not_validated_aqs_truth']='nowcast_labelled_validated_truth' not in hard
 fixture='fixture' in json.dumps(load(pd/'evidence_bundle.json')).lower() if (pd/'evidence_bundle.json').exists() else False
 status='fixture_only' if fixture else ('red' if hard else 'green')
 if fixture and status=='green': hard.append('fixture_marked_green')
 if hard and status!='fixture_only': status='red'
 slo='fixture_only' if fixture else ('fail' if hard else 'pass')
 for i,d in enumerate(sorted(set(hard))): incidents.append({"schema_version":"v1","incident_id":f"inc-{i}-{hashlib.sha256(d.encode()).hexdigest()[:8]}","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"severity":"high","trigger":d,"affected_refs":[str(rd)],"evidence_refs":[str(pd)],"recommended_action":"prepare_retraction_candidate","status":"opened"})
 health={"schema_version":"v1","health_id":"health-"+hashlib.sha256((str(rd)+ts(a.as_of)).encode()).hexdigest()[:12],"domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"input_refs":[str(rd),str(pd)],"checks":checks,"counts":{"hard_violations":len(hard)},"warnings":warnings,"incidents":[i['incident_id'] for i in incidents],"status":status}
 slo_r={"schema_version":"v1","slo_report_id":"slo-"+health['health_id'],"domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"input_refs":[str(rd)],"objectives":["freshness","hash_coverage","manifest_resolution","no_internal_refs"],"measurements":checks,"breaches":hard,"status":slo}
 if not a.dry_run:
  dump(out/'public_ops_health.json',health); dump(out/'public_slo_report.json',slo_r)
  for inc in incidents: dump(out/'incident_records'/f"{inc['incident_id']}.json",inc)
  (out/'ops_events.jsonl').write_text(json.dumps({"schema_version":"v1","event_id":"evt-health","domain":"atmosphere.air","event_type":"health_report","created_at":ts(a.as_of),"actor":"fixture-non-production-monitor","subject_refs":[str(rd)],"result":"pass" if not hard else "deny","details":{"violations":hard}},sort_keys=True)+"\n")
 print(json.dumps({"status":status,"slo":slo,"incidents":len(incidents)},sort_keys=True))
 return 0 if (not hard or a.dry_run or (fixture and a.allow_fixture_ops)) else 1
if __name__=='__main__': raise SystemExit(main())
