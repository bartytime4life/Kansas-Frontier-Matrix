#!/usr/bin/env python3
import argparse, json, subprocess, sys
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.resilience.soil._resilience_common import *
def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--resilience-root',required=True); ap.add_argument('--closure-root',required=True)
 for n in ['incident','observability','delivery','routing','active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']: ap.add_argument(f'--{n}-root',required=True)
 a=ap.parse_args(argv)
 chk=subprocess.run([sys.executable,'tools/validators/soil/public_resilience_check.py','--resilience-root',a.resilience_root],capture_output=True,text=True)
 obj=json.loads(chk.stdout or '{}'); fails=[] if chk.returncode==0 else ['resilience_check_failed']
 if obj.get('resilience_state')!='ready': fails.append('not_ready_for_advertising')
 print(json.dumps({'public_resilience_advertising_allowed':not fails,'prior_release_id':obj.get('prior_release_id'),'active_release_id':obj.get('active_release_id'),'resilience_id':obj.get('resilience_id'),'resilience_state':obj.get('resilience_state'),'decision':'pass' if not fails else 'blocked'})); return 0 if not fails else 1
if __name__=='__main__': raise SystemExit(main())
