#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

def main(argv=None):
 ap=argparse.ArgumentParser();
 for n in ['outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']:
  ap.add_argument(f'--{n}-root',required=True)
 a=ap.parse_args(argv)
 p=subprocess.run([sys.executable,str(ROOT/'tools/validators/soil/remediation_outcome_check.py'),'--outcome-root',a.outcome_root],capture_output=True,text=True)
 if p.returncode!=0: print(json.dumps({'remediation_outcome_advertising_allowed':False,'decision':'fail'})); return 1
 d=json.loads(p.stdout)
 print(json.dumps({'remediation_outcome_advertising_allowed':True,'release_id':d.get('release_id'),'registry_id':d.get('registry_id'),'remediation_id':d.get('remediation_id'),'outcome_cycle_id':d.get('outcome_cycle_id'),'certificate_status':'active','decision':'pass'},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
