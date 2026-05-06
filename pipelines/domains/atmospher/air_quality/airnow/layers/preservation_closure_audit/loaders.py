import json
from pathlib import Path
def loadj(p): return json.loads(Path(p).read_text())
def loadjl(p):
    rows=[]
    for ln in Path(p).read_text().splitlines():
        if ln.strip(): rows.append(json.loads(ln))
    return rows
