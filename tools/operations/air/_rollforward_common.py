#!/usr/bin/env python
import hashlib, json, re
from pathlib import Path
from datetime import datetime, timezone
BAD_PATTERNS=("data/raw/","data/work/","data/quarantine/","data/processed/air/","bearer ","api_key","secret","token","webhook","slack","pagerduty","calendar","kubectl","terraform","cdn purge","dns ","http://","https://")

def ts(v=None):
    if v: return v
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')

def j(p):
    return json.loads(Path(p).read_text())

def w(p,o):
    Path(p).parent.mkdir(parents=True,exist_ok=True)
    Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n")

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def etag_from_sha(s):
    return f'"sha256:{s}"'

def ensure_safe_text(x):
    t=json.dumps(x).lower()
    return not any(b in t for b in BAD_PATTERNS)

def deny(msg):
    raise SystemExit(f"DENY: {msg}")
