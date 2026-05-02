import json
from pathlib import Path

def loadj(path):
    return json.loads(Path(path).read_text())

def loadjl(path):
    rows=[]
    for line in Path(path).read_text().splitlines():
        line=line.strip()
        if line:
            rows.append(json.loads(line))
    return rows
