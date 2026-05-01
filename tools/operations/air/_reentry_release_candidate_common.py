#!/usr/bin/env python
import hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
UNSAFE=('data/raw/','data/work/','data/quarantine/','data/processed/air/','data/published/air/','secret','token','bearer ','kubectl','terraform','pagerduty','slack')
def ts(v=None): return v or datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def canon(o): return json.dumps(o,sort_keys=True,separators=(',',':'))
def sha_path(p):
 t=Path(p).read_bytes(); return 'sha256:'+hashlib.sha256(t).hexdigest()
def writej(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def has_unsafe_text(t):
 l=t.lower(); return any(x in l for x in UNSAFE)
def deny(msg): raise SystemExit('DENY: '+msg)
def chk_obj(o):
 if has_unsafe_text(canon(o)): deny('unsafe content')
def ref(path):
 s=str(path)
 if any(x in s.lower() for x in ('data/raw/','data/work/','data/quarantine/','data/processed/air/','data/published/air/')): deny('unsafe ref '+s)
 return s
