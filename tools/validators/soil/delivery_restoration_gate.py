#!/usr/bin/env python3
import argparse,json
from tools.validators.soil.delivery_restoration_check import main as chk

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--restoration-root',required=True); p.add_argument('--recommissioning-root',required=True)
 for n in ['resilience','closure','incident','observability','delivery','routing','active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']:
  p.add_argument(f'--{n}-root',required=True)
 ns=p.parse_args(argv)
 ok=chk(['--restoration-root',ns.restoration_root])==0
 print(json.dumps({'delivery_restoration_advertising_allowed':ok,'decision':'pass' if ok else 'blocked'})); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
