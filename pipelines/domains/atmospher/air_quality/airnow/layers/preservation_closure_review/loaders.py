import json
from pathlib import Path

def loadj(p):
 return json.loads(Path(p).read_text())

def wj(p,obj):
 Path(p).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")

def wjl(p,rows):
 Path(p).write_text("".join(json.dumps(r,sort_keys=True)+"\n" for r in rows))
