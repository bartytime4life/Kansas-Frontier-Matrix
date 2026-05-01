#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, datetime as dt, hashlib, json
from pathlib import Path
from tools.audit.soil._published_common import is_retracted, validate_published_release

def digest(payload): return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",",":")).encode()).hexdigest()

def main(argv=None):
 ap=argparse.ArgumentParser();ap.add_argument('--published-root',required=True);ap.add_argument('--from-release',required=True);ap.add_argument('--to-release',required=True);ap.add_argument('--out',required=True);a=ap.parse_args(argv)
 root=Path(a.published_root)
 try:
  if is_retracted(root,a.from_release) or is_retracted(root,a.to_release): raise ValueError('retracted release cannot be diffed')
  fr,tr=validate_published_release(root,a.from_release),validate_published_release(root,a.to_release)
  if not fr['valid'] or not tr['valid']: raise ValueError('invalid release input')
  A={r['bundle_id']:r for r in fr['index'].get('records') or []};B={r['bundle_id']:r for r in tr['index'].get('records') or []}
  keys=sorted(set(A)|set(B));added=[];removed=[];unch=[];chg=[];flags={k:False for k in ['rights_changed','sensitivity_changed','evidence_changed','provenance_changed','metric_changed']}
  for k in keys:
   if k not in A: added.append(k); continue
   if k not in B: removed.append(k); continue
   x,y=A[k],B[k];d={}
   for f in ['metrics','time_window','bbox','evidence_bundle_ref','stac_ref','dcat_ref','prov_ref','triplet_ref','rights_status','policy_label','sensitivity']:
    if x.get(f)!=y.get(f): d[f]={'from':x.get(f),'to':y.get(f)}
   if not d: unch.append(k)
   else:
    chg.append({'bundle_id':k,'changes':d});flags['metric_changed']|=('metrics' in d);flags['rights_changed']|=('rights_status' in d or 'policy_label' in d);flags['sensitivity_changed']|=('sensitivity' in d);flags['evidence_changed']|=('evidence_bundle_ref' in d);flags['provenance_changed']|=bool({'stac_ref','dcat_ref','prov_ref','triplet_ref'}&set(d))
  payload={'schema_version':'kfm.v1','object_type':'SoilPublishedReleaseDiff','domain':'soil','from_release':a.from_release,'to_release':a.to_release,'added_bundles':added,'removed_bundles':removed,'unchanged_bundles':unch,'changed_bundles':sorted(chg,key=lambda z:z['bundle_id']),'governance_flags':flags}
  payload['deterministic_hash']=digest(payload);payload['created']=dt.datetime.now(dt.timezone.utc).isoformat()
  out=Path(a.out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
  print(json.dumps({'diff_created':True,'from_release':a.from_release,'to_release':a.to_release,'out':str(out)},sort_keys=True));return 0
 except Exception as e:
  print(json.dumps({'diff_created':False,'reasons':[str(e)]},sort_keys=True));return 1
if __name__=='__main__': raise SystemExit(main())
