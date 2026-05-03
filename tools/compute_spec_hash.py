import json,hashlib,sys
from pathlib import Path
p=Path(sys.argv[1])
o=json.loads(p.read_text())
c=json.dumps(o,sort_keys=True,separators=(",",":"))
print(hashlib.sha256(c.encode()).hexdigest())
