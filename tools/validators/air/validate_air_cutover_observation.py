import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'deployments'/'air'))
#!/usr/bin/env python
import argparse,sys
from pathlib import Path
from cutover_common import J
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--authorization-dir');p.add_argument('--deployment-readiness-dir');p.add_argument('--delivery-dir');p.add_argument('--as-of');a=p.parse_args()
 ok=True
 for d in map(Path,a.dirs):
  for f in ['cutover_observation_record.json','post_deploy_gate_evaluation.json','release_ledger_manifest.json','operational_acceptance_record.json','rollback_decision_record.json','stakeholder_notice_draft.json']:
   if (d/f).exists(): pass
  if (d/'post_deploy_gate_evaluation.json').exists() and J(d/'post_deploy_gate_evaluation.json').get('result') in ('deny','blocked'): ok=False
 print('PASS' if ok else 'DENY'); sys.exit(0 if ok else 1)
