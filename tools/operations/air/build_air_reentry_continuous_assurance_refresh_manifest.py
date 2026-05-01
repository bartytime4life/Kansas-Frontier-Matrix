
#!/usr/bin/env python
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/","data/published/air/","data/published/air/read_model/")
LIVE=("http://","https://","kubectl","terraform","pagerduty","slack","calendar","webhook")
def ts(v=None): return v or datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def h(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def deny_obj(o):
 t=json.dumps(o,sort_keys=True).lower(); return any(b in t for b in BAD) or any(x in t for x in LIVE)
def w(path,obj): path.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')

def main():
 p=argparse.ArgumentParser(); p.add_argument('--out-dir',required=True); p.add_argument('--as-of'); p.add_argument('--dry-run',action='store_true'); p.add_argument('paths',nargs='*')
 a,_=p.parse_known_args(); od=Path(a.out_dir); now=ts(a.as_of)
 obj={"schema_version":"1.0.0","domain":"atmosphere.air","as_of":now,"generated_at":now,"created_at":now,"status":"fixture_continuous_assurance_refresh_manifest","fixture_backed":True}
 obj["assurance_refresh_manifest_id"]="assurance_refresh_manifest-"+h({"as_of":now,"out":"reentry_continuous_assurance_refresh_manifest.json"})[:12]
 if deny_obj(obj): print('DENY'); return 1
 if not a.dry_run:
  od.mkdir(parents=True,exist_ok=True); w(od/'reentry_continuous_assurance_refresh_manifest.json',obj)
  evt={"schema_version":"1.0.0","event_id":"evt-"+h(obj)[:12],"domain":"atmosphere.air","event_type":"continuous_assurance_refresh_plan_created","created_at":now,"as_of":now,"actor":"fixture-automation-non-production","subject_refs":[str(od/'reentry_continuous_assurance_refresh_manifest.json')],"evidence_refs":[],"result":"pass","details":{}}
  (od/'reentry_continuous_assurance_refresh_events.jsonl').write_text(json.dumps(evt,sort_keys=True)+'\n')
 print('PASS'); return 0
if __name__=='__main__': raise SystemExit(main())
