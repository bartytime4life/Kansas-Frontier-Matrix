#!/usr/bin/env python3
import argparse, json, urllib.request
from pathlib import Path
from tools.restoration.soil._delivery_restoration_common import *
REQ=['/health','/soil/current','/soil/recommissioning','/soil/recommissioning/public-report','/soil/delivery','/soil/routing']

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--recommissioning-root',required=True); p.add_argument('--base-url',required=True); p.add_argument('--out-root',required=True); p.add_argument('--recommissioning-id'); p.add_argument('--probe-id')
 ns=p.parse_args(argv)
 rid=ns.recommissioning_id or load_current_delivery_recommissioning(ns.recommissioning_root)['active_recommissioning_id']
 pid=sanitize_id(ns.probe_id or f'{rid}-probe')
 ev=[]; fails=[]
 for ep in REQ:
  try:
   r=urllib.request.urlopen(ns.base_url+ep,timeout=3); b=r.read().decode('utf-8','ignore'); ev.append({'endpoint':ep,'status':r.getcode()})
   if scan_text_for_forbidden_terms(b) or scan_payload_for_contact_or_secret_terms({'b':b}): fails.append(f'unsafe payload {ep}')
  except Exception as e: fails.append(f'{ep}: {e}')
 dec='pass' if not fails else 'fail'
 rec={'schema_version':'kfm.v1','object_type':'SoilRestorationProbeReceipt','domain':'soil','probe_id':pid,'recommissioning_id':rid,'decision':dec,'endpoint_results':ev,'failure_reasons':fails,'created':utc_now_iso()}
 out=Path(ns.out_root)/f'restoration/soil/probes/{rid}'; out.mkdir(parents=True,exist_ok=True); fp=out/f'{pid}.restoration_probe_receipt.json'; write_json_atomic(fp,rec)
 print(json.dumps({'probe_decision':dec,'probe_id':pid,'receipt':str(fp)})); return 0 if dec=='pass' else 1
if __name__=='__main__': raise SystemExit(main())
