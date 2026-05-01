#!/usr/bin/env python3
import argparse,json
from datetime import datetime,timezone
from pathlib import Path
from tools.distribution.fauna._gbif_distribution_common import stable_hash
L=lambda p: json.loads(Path(p).read_text())
a=argparse.ArgumentParser();[a.add_argument(i,required=True) for i in ['--distribution-bundle','--static-exports','--search-records','--api-responses','--endpoint-checks','--output']];x=a.parse_args();b,se,sr,ap,ec=[L(i) for i in [x.distribution_bundle,x.static_exports,x.search_records,x.api_responses,x.endpoint_checks]]
checks=[('release_approved',b.get('distribution_state')=='ready'),('manifest_valid',bool(b.get('manifest_id'))),('citation_index_present',bool(b.get('citation_index'))),('search_records_public_safe',all(i.get('public_safe') for i in sr)),('api_responses_public_safe',all(i.get('public_safe') for i in ap)),('withdrawn_artifacts_absent',all('withdrawn' not in str(i).lower() for i in [se,sr,ap])),('endpoint_checks_ok',all(i.get('check_posture')=='passed' for i in ec))]
cs=[{'check_name':n,'passed':p,'details':[]} for n,p in checks]; failed=[c['check_name'] for c in cs if not c['passed']]
out={'distribution_gate_result_id':'gbif_distribution_gate_TEST_001','gate_name':'gbif_public_distribution_gate','gate_version':'gbif_distribution.v1','distribution_bundle_id':b['distribution_bundle_id'],'release_registry_entry_id':b['release_registry_entry_id'],'manifest_id':b['manifest_id'],'gate_posture':'passed' if not failed else 'failed','checks':cs,'failed_checks':failed,'created_at':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','distribution_gate_result_id'))
Path(x.output).write_text(json.dumps(out,indent=2)+'
');print('ok')
