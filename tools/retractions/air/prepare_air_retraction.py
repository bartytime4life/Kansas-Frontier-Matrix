#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
from datetime import datetime, timezone

def ts(v=None): return v or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def load(p): return json.loads(Path(p).read_text())
def dump(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n")
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--incident-record',required=True); ap.add_argument('--publication-dir',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--requested-by',default='ops-bot-non-production'); ap.add_argument('--as-of'); ap.add_argument('--dry-run',action='store_true')
 a=ap.parse_args(); inc=load(a.incident_record); p=Path(a.publication_dir)/'publication_manifest.json'; pm=load(p)
 req={"schema_version":"v1","retraction_request_id":"rr-"+hashlib.sha256((inc['incident_id']+pm['publication_id']).encode()).hexdigest()[:12],"domain":"atmosphere.air","created_at":ts(a.as_of),"requested_by":a.requested_by,"incident_ref":str(a.incident_record),"publication_manifest_ref":str(p),"reason":inc['trigger'],"affected_artifacts":[x.get('path') for x in pm.get('published_artifacts',[])],"evidence_refs":inc.get('evidence_refs',[]),"recommended_tombstone":{"publication_id":pm['publication_id'],"reason":inc['trigger'],"preview_only":True},"status":"candidate","steward_review_required":True}
 if not a.dry_run:
  out=Path(a.out_dir); dump(out/'retraction_request.json',req); dump(out/'recommended_tombstone.preview.json',req['recommended_tombstone'])
  (out/'ops_events.jsonl').write_text(json.dumps({"schema_version":"v1","event_id":"evt-retract","domain":"atmosphere.air","event_type":"retraction_requested","created_at":ts(a.as_of),"actor":"fixture-non-production-retraction-tool","subject_refs":[str(p)],"result":"warn","details":{"status":"candidate"}},sort_keys=True)+"\n")
 print(json.dumps({"status":"candidate","publication":pm['publication_id']},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
