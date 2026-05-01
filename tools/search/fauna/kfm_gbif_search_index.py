#!/usr/bin/env python3
import sys,argparse,json
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.distribution.fauna._gbif_distribution_common import stable_hash,scan_forbidden,REQ_PRESENCE
L=lambda p: json.loads(Path(p).read_text())
a=argparse.ArgumentParser();a.add_argument('--distribution-bundle',required=True);a.add_argument('--ui-cards',required=True);a.add_argument('--output',required=True);x=a.parse_args();b,cards=L(x.distribution_bundle),L(x.ui_cards);out=[]
for c in cards:
 r={"search_index_record_id":"gbif_search_TEST_001","domain":"fauna","source_system":"GBIF","index_name":"fauna_public_gbif_occurrence_aggregates","record_type":"gbif_occurrence_aggregate_card","distribution_bundle_id":b['distribution_bundle_id'],"release_registry_entry_id":b['release_registry_entry_id'],"artifact_id":c['card_id'],"public_url_path":c['public_url_path'],"title":c['title'],"subtitle":"GBIF-reported public occurrence aggregate","summary":c['summary'],"taxon_key":c['taxon_key'],"scientific_name":c['scientific_name'],"geography_id":c['geography_id'],"display_name":c['display_name'],"aggregation_unit":"county","badges":["reported occurrence","public generalized","not confirmed presence"],"citation_refs":b['citation_index'],"rights_posture":"public_allowed","sensitivity_posture":"public_generalized","presence_posture":REQ_PRESENCE,"public_safe":True,"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')};r['kfm:spec_hash']=stable_hash(r,exclude=('created_at','search_index_record_id'));out.append(r)
errs=scan_forbidden(out)
if errs: raise SystemExit('\n'.join(errs))
Path(x.output).write_text(json.dumps(out,indent=2)+'\n');print('ok')
