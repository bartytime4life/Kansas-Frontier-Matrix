#!/usr/bin/env python3
import sys,argparse,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.distribution.fauna._gbif_distribution_common import stable_hash,scan_forbidden,REQ_PRESENCE
L=lambda p: json.loads(Path(p).read_text())
a=argparse.ArgumentParser();a.add_argument('--distribution-bundle',required=True);a.add_argument('--runtime-answer',required=True);a.add_argument('--output',required=True);x=a.parse_args();b,ra=L(x.distribution_bundle),L(x.runtime_answer)
out=[{"api_response_id":"gbif_api_response_TEST_001","api_version":"gbif_public_api.v1","domain":"fauna","source_system":"GBIF","response_type":"occurrence_aggregate_answer","distribution_bundle_id":b['distribution_bundle_id'],"request_shape":{"route":"/api/fauna/gbif/occurrence-aggregates","query":ra['query']},"answer_posture":"cited_answer","data":ra['data'],"citations":b['citation_index'],"limitations":b['limitations'],"redactions":["exact occurrence coordinates not emitted"],"public_safe":True,"rights_posture":"public_allowed","sensitivity_posture":"public_generalized","presence_posture":REQ_PRESENCE,"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}] ; out[0]['kfm:spec_hash']=stable_hash(out[0],exclude=('created_at','api_response_id'))
errs=scan_forbidden(out)
if errs: raise SystemExit('\n'.join(errs))
Path(x.output).write_text(json.dumps(out,indent=2)+'\n');print('ok')
