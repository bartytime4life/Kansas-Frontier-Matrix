import json
from pathlib import Path
def loadj(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))
