#!/usr/bin/env python3
import argparse,json
from pathlib import Path
BAD=("/raw/","/work/","/quarantine/","/processed/")
def bad(s): s=(s or '').lower(); return any(b in s for b in BAD)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--index',required=True); ap.add_argument('--aggregation'); ap.add_argument('--from'); ap.add_argument('--to'); ap.add_argument('--include-candidates',action='store_true'); a=ap.parse_args()
 idx=json.loads(Path(a.index).read_text())
 out=[]
 for e in idx.get('entries',[]):
  if any(bad(x.get('ref','')) for x in e.get('artifact_refs',[])): raise SystemExit('unsafe path detected')
  if e.get('visibility')=='candidate_only' and not a.include_candidates: continue
  out.append(e)
 print(json.dumps({'entries':out},sort_keys=True))
if __name__=='__main__': main()
