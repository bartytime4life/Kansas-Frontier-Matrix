import json
from pathlib import Path
from .ids import cjson
def loadj(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def loadjl(p):
 rows=[]
 for ln in Path(p).read_text(encoding="utf-8").splitlines():
  if ln.strip(): rows.append(json.loads(ln))
 return rows
def wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+"\n",encoding="utf-8")
def wjl(p,rows): Path(p).write_text("".join(cjson(r)+"\n" for r in rows),encoding="utf-8")
