from __future__ import annotations
import hashlib,json
from pathlib import Path
from typing import Any
from jsonschema import validate as js_validate

def canonical_hash(obj:dict[str,Any],field:str)->str:
    base=dict(obj);base.pop(field,None)
    return 'sha256:'+hashlib.sha256(json.dumps(base,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def write_json(path:Path,obj:dict[str,Any]):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n',encoding='utf-8')

def validate(path:Path,obj:dict[str,Any]):
    js_validate(instance=obj,schema=json.loads(path.read_text()))

def sha256_file(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for c in iter(lambda:f.read(65536),b''):h.update(c)
    return 'sha256:'+h.hexdigest()
