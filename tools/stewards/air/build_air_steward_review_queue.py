#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
TS=lambda v=None:(v or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'))
P={'critical':4,'high':3,'medium':2,'low':1,'info':0}

def j(p): return json.loads(Path(p).read_text())
def w(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
def badref(s): return any(x in s.lower() for x in ['/raw/','/work/','/quarantine/','data/raw','data/work','data/quarantine','data/processed/air'])

def main():
 a=argparse.ArgumentParser(); a.add_argument('--ops-dir',action='append',required=True); a.add_argument('--out-dir',required=True); a.add_argument('--as-of'); a.add_argument('--include-low-priority',action='store_true'); a.add_argument('--allow-fixture-queue',action='store_true'); a.add_argument('--dry-run',action='store_true'); x=a.parse_args(); items=[]
 for d in map(Path,x.ops_dir):
  inc=j(d/'incident_record.json'); rr=j(d/'retraction_request.json'); pm=j(d/'publication_manifest.json')
  if not inc.get('evidence_refs'): raise SystemExit('DENY missing incident evidence')
  if 'validated aqs truth' in json.dumps([inc,rr,pm]).lower(): raise SystemExit('DENY nowcast truth label')
  aff=[z for z in pm.get('published_artifacts',[]) if z.get('sha256')]
  if len(aff)!=len(pm.get('published_artifacts',[])): raise SystemExit('DENY missing sha256')
  if any(badref(json.dumps(z)) for z in aff): raise SystemExit('DENY unsafe paths')
  pr=inc.get('severity','medium').lower();
  if (not x.include_low_priority) and P.get(pr,0)<2: continue
  items.append({'item_id':'item_'+inc['incident_id'],'priority':pr if pr in P else 'medium','reason':inc.get('trigger','incident'),'incident_ref':str(d/'incident_record.json'),'retraction_request_ref':str(d/'retraction_request.json'),'publication_manifest_ref':str(d/'publication_manifest.json'),'affected_artifacts':aff,'evidence_refs':inc['evidence_refs'],'recommended_action':'steward_retraction_review','review_required_by':'Gate D steward','fixture_backed':True})
 items=sorted(items,key=lambda i:P[i['priority']],reverse=True)
 status='empty' if not items else ('fixture_only' if x.allow_fixture_queue and all(i['fixture_backed'] for i in items) else 'needs_review')
 q={'schema_version':'v1','queue_id':'queue-'+hashlib.sha256(str(items).encode()).hexdigest()[:10],'domain':'atmosphere.air','generated_at':TS(x.as_of),'as_of':TS(x.as_of),'input_refs':x.ops_dir,'items':items,'summary':{'count':len(items)},'status':status}
 if not x.dry_run: o=Path(x.out_dir); w(o/'steward_review_queue.json',q); (o/'ops_events.jsonl').write_text(json.dumps({'schema_version':'v1','event_type':'steward_queue_built','result':status,'created_at':TS(x.as_of)},sort_keys=True)+'\n')
 print(json.dumps({'status':status,'items':len(items)})); return 0
if __name__=='__main__': raise SystemExit(main())
