import json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
UNSAFE=("data/raw/","data/work/","data/quarantine/","data/processed/air/")
LIVE=("http://","https://","slack","pagerduty","kubectl","terraform","cdn","dns","ticket","calendar")
SECRET=("api_key","token","secret","bearer ","private key","webhook")
def ts(v=None):
 return v or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def j(p): return json.loads(Path(p).read_text())
def h(x): return hashlib.sha256((json.dumps(x,sort_keys=True) if not isinstance(x,str) else x).encode()).hexdigest()
def w(p,o): Path(p).parent.mkdir(parents=True,exist_ok=True);Path(p).write_text(json.dumps(o,sort_keys=True,indent=2)+'\n')
def bad_text(o):
 t=(json.dumps(o,sort_keys=True) if isinstance(o,(dict,list)) else str(o)).lower()
 return any(x in t for x in UNSAFE+LIVE+SECRET)
