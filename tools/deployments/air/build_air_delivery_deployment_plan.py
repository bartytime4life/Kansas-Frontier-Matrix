import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
#!/usr/bin/env python3
import argparse, json, hashlib
from pathlib import Path
from tools.deployments.air.lib_air_deploy import build_plan
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--delivery-dir',required=True);a.add_argument('--out-dir',required=True);a.add_argument('--environment',default='local_fixture');a.add_argument('--previous-delivery-dir');a.add_argument('--as-of');a.add_argument('--allow-fixture-deployment-plan',action='store_true');a.add_argument('--dry-run',action='store_true');x=a.parse_args();
 raise SystemExit(build_plan(Path(x.delivery_dir),Path(x.out_dir),x.environment,x.as_of,x.allow_fixture_deployment_plan,x.dry_run))
