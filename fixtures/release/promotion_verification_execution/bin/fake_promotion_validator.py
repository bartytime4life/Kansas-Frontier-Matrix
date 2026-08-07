#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
value=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
status='PASS' if value.get('policy_context',{}).get('evaluation')=='PASS' else 'DENY'
print(json.dumps({'status':status,'scope':'release.promotion_gate'},sort_keys=True,separators=(',',':')))
raise SystemExit(0 if status=='PASS' else 1)
