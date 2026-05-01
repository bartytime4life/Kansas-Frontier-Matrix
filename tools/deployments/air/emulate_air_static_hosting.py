import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from tools.deployments.air.lib_air_deploy import J
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--deployment-dir',required=True);a.add_argument('--delivery-dir',required=True);a.add_argument('--route');a.add_argument('--record-id');a.add_argument('--publication-id');a.add_argument('--delta-cursor');a.add_argument('--include-candidates',action='store_true');a.add_argument('--show-headers',action='store_true');x=a.parse_args()
 h=J(Path(x.deployment_dir)/'static_hosting_manifest.json'); route=x.route or '/air/v1/index'
 m={r['path_template']:r for r in h['hosted_routes']}
 sel=m.get(route) or next((v for k,v in m.items() if '{record_id}' in k),None)
 if not sel: raise SystemExit('DENY missing route')
 if sel.get('visibility')=='candidate_only' and not x.include_candidates: raise SystemExit('DENY candidate route')
 body=(Path(x.delivery_dir)/sel['response_artifact_ref']).read_text()
 if x.show_headers: print(json.dumps({'ETag':sel['etag'],'Cache-Control':sel['cache_control']},sort_keys=True))
 print(body)
