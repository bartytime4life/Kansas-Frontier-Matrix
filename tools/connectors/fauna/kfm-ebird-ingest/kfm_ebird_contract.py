#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ADAPTER_NAME='kfm-ebird'
ADAPTER_VERSION='1.0.0'
SCHEMA_BUNDLE_VERSION='v1'

def now_iso()->str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')

def canonical_json(value:Any)->str:
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)

def sha256_text(text:str)->str:
    return 'sha256:'+hashlib.sha256(text.encode('utf-8')).hexdigest()

def compute_contract_hash(obj:dict[str,Any])->str:
    payload={k:v for k,v in obj.items() if k not in {'generated_at','contract_hash'}}
    return sha256_text(canonical_json(payload))

def load_contract_lock(path:Path)->dict[str,Any]:
    data=json.loads(path.read_text(encoding='utf-8'))
    return data

def verify_contract_lock(data:dict[str,Any])->tuple[bool,str,str]:
    expected=compute_contract_hash(data)
    actual=str(data.get('contract_hash',''))
    return expected==actual, expected, actual

def version_payload(tool_name:str, contract_lock_path:Path|None=None)->dict[str,Any]:
    payload={'tool':tool_name,'adapter':ADAPTER_NAME,'version':ADAPTER_VERSION,'schema_bundle_version':SCHEMA_BUNDLE_VERSION}
    if contract_lock_path and contract_lock_path.exists():
      data=load_contract_lock(contract_lock_path)
      payload['contract_lock_hash']=data.get('contract_hash')
    return payload
