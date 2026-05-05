#!/usr/bin/env python3
from __future__ import annotations
import json,sys,hashlib
from pathlib import Path
from datetime import datetime

def cjson(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def ts(s): return datetime.fromisoformat(s.replace('Z','+00:00'))

def main(args):
 rows=[];ids=set();last=None
 for p in args:
  o=json.loads(Path(p).read_text())
  eid=o.get('event_id') or o.get('execution_id'); t=o.get('timestamp') or o.get('executed_at')
  if eid in ids: raise SystemExit('duplicate event ids')
  if last and ts(t)<last: raise SystemExit('out-of-order timestamps')
  last=ts(t); ids.add(eid)
  et='rollback' if o['object_type']=='RollbackExecutionReceipt' else ('correction' if o['object_type']=='CorrectionNotice' else 'withdrawal')
  entry={"event_id":eid,"event_type":et,"timestamp":t}
  entry['entry_hash']=hashlib.sha256(cjson(entry).encode()).hexdigest(); rows.append(entry)
 out={"object_type":"PromotionCorrectionLedger","schema_version":"v1","ledger_id":"ledger-001","entries":rows}
 out['chain_hash']=hashlib.sha256(''.join(x['entry_hash'] for x in rows).encode()).hexdigest()
 print(cjson(out))
if __name__=='__main__': main(sys.argv[1:])
