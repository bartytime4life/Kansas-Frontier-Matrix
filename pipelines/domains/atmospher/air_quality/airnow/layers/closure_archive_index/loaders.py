import json
from pathlib import Path
def loadj(p): return json.loads(Path(p).read_text(encoding='utf-8'))
def loadjl(p):
    rows=[]
    for line in Path(p).read_text(encoding='utf-8').splitlines():
        t=line.strip()
        if t: rows.append(json.loads(t))
    return rows
