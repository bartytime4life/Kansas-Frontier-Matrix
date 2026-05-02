from pathlib import Path
import json
def loadj(p): return json.loads(Path(p).read_text())
def loadjl(p):
 return [json.loads(x) for x in Path(p).read_text().splitlines() if x.strip()]
