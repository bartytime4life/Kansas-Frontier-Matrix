#!/usr/bin/env python3
import argparse,json
from datetime import datetime,timezone
from pathlib import Path
from tools.distribution.fauna._gbif_distribution_common import stable_hash
L=lambda p: json.loads(Path(p).read_text())
a=argparse.ArgumentParser();a.add_argument('--distribution-bundle',required=True);a.add_argument('--reason',required=True);a.add_argument('--output',required=True);x=a.parse_args();b=L(x.distribution_bundle)
out={"cache_invalidation_receipt_id":"gbif_cache_TEST_001","domain":"fauna","source_system":"GBIF","distribution_bundle_id":b['distribution_bundle_id'],"release_registry_entry_id":b['release_registry_entry_id'],"reason":x.reason,"cache_keys":[r['cache_key'] for r in b['public_routes']],"public_url_paths":[r['public_url_path'] for r in b['public_routes']],"invalidation_state":"requested","affected_artifact_ids":[r['artifact_id'] for r in b['public_routes']],"replacement_distribution_bundle_id":None,"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','cache_invalidation_receipt_id'))
Path(x.output).write_text(json.dumps(out,indent=2)+'
');print('ok')
