#!/usr/bin/env python3
import json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
FORBIDDEN=("/raw/","/work/","/quarantine/","/processed/","data/published/air/","data/published/air/read_model/")
SECRET_RE=re.compile(r"(?i)(secret|token|apikey|api[_-]?key|bearer|private[_-]?key|webhook|pagerduty|slack|credential)")

def ts(v=None):
    return v or datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def readj(p):
    return json.loads(Path(p).read_text())

def writej(p,obj):
    Path(p).parent.mkdir(parents=True,exist_ok=True); Path(p).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')

def sha(p):
    h=hashlib.sha256(); h.update(Path(p).read_bytes()); return h.hexdigest()

def has_unsafe_text(text):
    t=text.lower()
    return any(x in t for x in FORBIDDEN) or bool(SECRET_RE.search(text))

def has_unsafe_obj(o):
    s=json.dumps(o,sort_keys=True)
    return has_unsafe_text(s)
