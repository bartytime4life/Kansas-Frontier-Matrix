import json
from pathlib import Path
def loadj(p): return json.loads(Path(p).read_text())
def loadjl(p): return [json.loads(x) for x in Path(p).read_text().splitlines() if x.strip()]
def wj(p,o): Path(p).write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def wjl(p,rows): Path(p).write_text(''.join(json.dumps(r,sort_keys=True,separators=(",",":"))+'\n' for r in rows))
