#!/usr/bin/env python3
import json, hashlib
from pathlib import Path
from datetime import datetime, timezone

BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/","data/published/air/","data/published/air/read_model/")
LIVE=("http://","https://","kubectl","terraform apply","purge","cdn","dns","pagerduty","slack","webhook")

def ts(v=None): return v or datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def J(p): return json.loads(Path(p).read_text())
def W(p,o): Path(p).parent.mkdir(parents=True,exist_ok=True); Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def etag_from_sha(s): return f'"sha256:{s}"'
def bad_text(t):
 t=t.lower(); return any(x in t for x in BAD) or any(x in t for x in LIVE) or 'validated aqs truth' in t

def fail(msg): raise SystemExit(f'DENY: {msg}')
