#!/usr/bin/env python
import json,hashlib,re
from datetime import datetime, timezone
from pathlib import Path
DENY_PAT=["data/raw/","data/work/","data/quarantine/","data/processed/air/","data/published/air/","bearer ","secret","token","webhook","slack","pagerduty","calendar","kubectl","terraform","dns","cdn purge","http://","https://"]
def ts(v=None):
 return v or datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def j(p): return json.loads(Path(p).read_text())
def w(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def deny(m): raise SystemExit("DENY: "+m)
def has_unsafe(o):
 s=json.dumps(o).lower(); return any(x in s for x in DENY_PAT)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def etag_from_sha(h): return f'"sha256:{h[:16]}"'
