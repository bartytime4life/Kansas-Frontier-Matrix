import json,hashlib,re
from pathlib import Path
BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/")
LIVE=("kubectl","terraform apply","cdn purge","route53","cloudflare api","pagerduty","slack.com","webhook","dns")
SECRET=re.compile(r"(bearer\s+[a-z0-9\-\._]+|api[_-]?key|secret|private[_-]?key|token)",re.I)
TS=lambda x:x or '2026-04-30T00:00:00Z'
J=lambda p: json.loads(Path(p).read_text())

def wj(p,d): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
def js(d): return json.dumps(d,sort_keys=True,separators=(",",":"))
def h(d): return hashlib.sha256(js(d).encode()).hexdigest()
def etag(s): return f'"sha256:{s}"'
def scan(o):
 t=json.dumps(o).lower(); issues=[]
 if any(b in t for b in BAD): issues.append('unsafe path')
 if any(l in t for l in LIVE): issues.append('live instruction')
 if SECRET.search(t): issues.append('secret-like value')
 return issues
