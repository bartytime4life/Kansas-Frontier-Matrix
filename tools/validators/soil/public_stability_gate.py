#!/usr/bin/env python3
import argparse, json, subprocess, sys

def main():
 p=argparse.ArgumentParser();p.add_argument('--stability-root',required=True)
 for x in ['continuity','resilience','closure','incident','observability','delivery','routing','active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']: p.add_argument(f'--{x}-root',required=True)
 a=p.parse_args()
 rc=subprocess.run([sys.executable,'tools/validators/soil/public_stability_check.py','--stability-root',a.stability_root],capture_output=True,text=True)
 if rc.returncode!=0: print(json.dumps({"public_stability_advertising_allowed":False,"decision":"blocked"})); return 2
 d=json.loads(rc.stdout); print(json.dumps({"public_stability_advertising_allowed":True,"stability_id":d['stability_id'],"stability_state":d['stability_state'],"decision":"pass"})); return 0
if __name__=='__main__': sys.exit(main())
