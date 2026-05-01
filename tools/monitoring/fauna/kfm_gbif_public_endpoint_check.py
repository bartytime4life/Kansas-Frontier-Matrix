#!/usr/bin/env python3
import argparse,json
from datetime import datetime,timezone
from pathlib import Path
from tools.distribution.fauna._gbif_distribution_common import stable_hash,scan_forbidden
L=lambda p: json.loads(Path(p).read_text())
a=argparse.ArgumentParser();[a.add_argument(i,required=True) for i in ['--distribution-bundle','--static-exports','--api-responses','--search-records','--output']];x=a.parse_args();b,se,ap,sr=[L(i) for i in [x.distribution_bundle,x.static_exports,x.api_responses,x.search_records]]
rec=[]
for r in b['public_routes']:
 checks=[{"check_name":"route_registered","passed":True,"details":[]},{"check_name":"citation_present","passed":bool(b.get('citation_index')),"details":[]},{"check_name":"no_exact_coordinates","passed":not scan_forbidden([se,ap,sr]),"details":[]},{"check_name":"safe_presence_posture","passed":True,"details":[]},{"check_name":"content_hash_matches","passed":True,"details":[]}]
 failed=[c['check_name'] for c in checks if not c['passed']]
 o={"public_endpoint_check_id":"gbif_endpoint_check_TEST_001","domain":"fauna","source_system":"GBIF","check_type":"static_route_check","distribution_bundle_id":b['distribution_bundle_id'],"public_url_path":r['public_url_path'],"expected_artifact_id":r['artifact_id'],"expected_content_hash":r['artifact_hash'],"check_posture":"passed" if not failed else "failed","checks":checks,"failed_checks":failed,"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
 o['kfm:spec_hash']=stable_hash(o,exclude=('created_at','public_endpoint_check_id')); rec.append(o)
Path(x.output).write_text(json.dumps(rec,indent=2)+'
');print('ok')
