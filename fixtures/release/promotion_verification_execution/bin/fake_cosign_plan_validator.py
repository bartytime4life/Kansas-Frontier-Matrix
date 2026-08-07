#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
value=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
outcome='PASS' if value.get('predicate',{}).get('check_claims') is True else 'FAIL'
print(json.dumps({'outcome':outcome,'scope':'cosign-attestation-verification-plan-preflight-only'},sort_keys=True,separators=(',',':')))
raise SystemExit(0 if outcome=='PASS' else 1)
