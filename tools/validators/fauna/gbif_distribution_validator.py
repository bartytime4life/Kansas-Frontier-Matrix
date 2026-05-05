#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from tools.distribution.fauna._gbif_distribution_common import scan_forbidden,REQ_PRESENCE

def validate(kind,d):
 e=scan_forbidden(d)
 if not d.get('kfm:spec_hash'): e.append('missing kfm:spec_hash')
 if kind in {'search','api','static'} and not d.get('public_safe'): e.append('public_safe must be true')
 if d.get('rights_posture') and d.get('rights_posture')!='public_allowed': e.append('rights_posture != public_allowed')
 if d.get('sensitivity_posture')=='restricted': e.append('sensitivity restricted')
 if d.get('presence_posture') and d.get('presence_posture')!=REQ_PRESENCE: e.append('presence posture mismatch')
 if kind=='search':
  if not d.get('public_url_path'): e.append('search record without public_url_path')
  if not d.get('citation_refs'): e.append('search record without citation_refs')
 if kind=='api':
  if not d.get('citations'): e.append('API response without citations')
 if kind=='static':
  if not d.get('content_hash'): e.append('static export without content_hash')
  if not d.get('citation_refs'): e.append('static export without citation_refs')
 if kind=='endpoint' and d.get('check_posture')=='passed' and any(not c.get('passed') for c in d.get('checks',[])): e.append('endpoint check passed while check failed')
 if kind=='gate' and d.get('gate_posture')=='passed' and any(not c.get('passed') for c in d.get('checks',[])): e.append('distribution gate passed while check failed')
 if kind=='takedown':
  if not (d.get('withdrawal_receipt_ref') or d.get('correction_receipt_ref')): e.append('takedown missing withdrawal or correction ref')
  if d.get('public_use_allowed') is not False: e.append('takedown public_use_allowed must be false')
 return e

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--kind',required=True);ap.add_argument('--input',required=True);a=ap.parse_args();doc=json.loads(Path(a.input).read_text());errs=validate(a.kind,doc);print('ok' if not errs else '\n'.join(errs));raise SystemExit(0 if not errs else 1)
