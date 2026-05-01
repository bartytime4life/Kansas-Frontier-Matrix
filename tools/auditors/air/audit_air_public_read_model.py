#!/usr/bin/env python3
import json,sys
from pathlib import Path
BAD=("/raw/","/work/","/quarantine/","/processed/","data/processed/air/")
CHAIN=["QA Summary","EvidenceBundle","PromotionDecision","ReleaseManifest","PublicationManifest","PublicIndex/PublicApiRecord"]
def load(p): return json.loads(Path(p).read_text())
def bad(s): s=(s or '').lower(); return any(b in s for b in BAD)
def audit(d):
 d=Path(d); issues=[]
 idx=d/'public_index.json'
 if not idx.exists(): idx=d/'public_index.blocked.json'
 if not idx.exists(): return ['missing_public_index']
 i=load(idx)
 for e in i.get('entries',[]):
  for a in e.get('artifact_refs',[]):
   if not a.get('sha256'): issues.append('missing_sha256')
   if bad(a.get('ref','')): issues.append('unsafe_ref')
 for rp in d.glob('public_api_record.*.json'):
  r=load(rp)
  if r.get('measurements',{}).get('nowcast_is_validated_aqs_truth'): issues.append('nowcast_truth_violation')
  if r.get('measurements',{}).get('source_class')=='fixture' and r.get('status')=='public_readable': issues.append('fixture_public_readable')
  if r.get('status')=='public_readable' and r.get('publication_id','').endswith('retracted'): issues.append('retracted_active')
  for section in ('provenance','catalog'):
   for v in r.get(section,{}).values():
    if isinstance(v,str) and bad(v): issues.append('unsafe_path_exposed')
 for tp in d.glob('public_provenance_trace.*.json'):
  t=load(tp)
  if t.get('chain')!=CHAIN: issues.append('chain_separation_violation')
  if any(bad(x) for x in t.get('public_safe_refs',[])): issues.append('unsafe_trace_ref')
 return sorted(set(issues))
def main():
 if len(sys.argv)<2: print('usage: audit_air_public_read_model.py <dir> [<dir>...]'); return 2
 rc=0
 for d in sys.argv[1:]:
  i=audit(d)
  if i: rc=1; print(f'DENY {d}: '+','.join(i))
  else: print(f'PASS {d}')
 return rc
if __name__=='__main__': raise SystemExit(main())
