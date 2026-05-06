import json
from pathlib import Path

def loadj(path):
    return json.loads(Path(path).read_text())

def loadjl(path):
    rows=[]
    for line in Path(path).read_text().splitlines():
        line=line.strip()
        if line: rows.append(json.loads(line))
    return rows

def wj(path,obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True)+"\n")

def wjl(path,rows,cjson):
    Path(path).write_text("".join(cjson(r)+"\n" for r in rows))
