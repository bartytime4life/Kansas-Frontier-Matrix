#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse,json
from datetime import datetime,timezone
from pathlib import Path
from tools.distribution.fauna._gbif_distribution_common import stable_hash,scan_forbidden,deterministic_cache_key,REQ_PRESENCE
L1='GBIF occurrence aggregates are reported occurrence evidence, not confirmed species-presence determinations.'
L2='Public output is generalized and does not expose exact occurrence coordinates.'

def load(p): return json.loads(Path(p).read_text())
def main():
 a=argparse.ArgumentParser();
 a.add_argument('--release-registry',required=True);a.add_argument('--manifest',required=True);a.add_argument('--review-decision',required=True);a.add_argument('--package',required=True);a.add_argument('--output',required=True);x=a.parse_args()
 r,m,rv,p=[load(i) for i in [x.release_registry,x.manifest,x.review_decision,x.package]]
 state='ready'; reasons=[]
 if r.get('release_state')!='published': state='blocked'; reasons.append('release_not_published')
 if rv.get('decision')!='approve_publish': state='blocked'; reasons.append('review_not_approved')
 if not m.get('citation_index'): state='blocked'; reasons.append('manifest_missing_citation_index')
 if not m.get('redactions'): state='blocked'; reasons.append('manifest_missing_redactions')
 if not p.get('policy_results',{}).get('passed',False): state='blocked'; reasons.append('package_policy_failed')
 if r.get('rights_posture')!='public_allowed' or r.get('sensitivity_posture')=='restricted' or r.get('presence_posture')!=REQ_PRESENCE: state='blocked'; reasons.append('posture_failure')
 if r.get('release_state')=='superseded' and not r.get('successor_release_registry_entry_id'): state='blocked'; reasons.append('superseded_without_successor')
 cidx=m.get('citation_index',[])
 out={"distribution_bundle_id":"gbif_dist_TEST_001","domain":"fauna","source_system":"GBIF","bundle_type":"public_occurrence_distribution_bundle","distribution_state":state,"release_registry_entry_id":r.get('release_registry_entry_id'),"manifest_id":m.get('manifest_id'),"publication_package_id":p.get('publication_package_id'),"review_decision_receipt_id":rv.get('review_decision_receipt_id'),"published_package_ids":m.get('published_package_ids',[]),"published_answer_ids":m.get('published_answer_ids',[]),"published_ui_card_ids":m.get('published_ui_card_ids',[]),"published_map_layer_ids":m.get('published_map_layer_ids',[]),"citation_index":cidx,"public_routes":[],"search_index_record_ids":["gbif_search_TEST_001"],"static_export_record_ids":["gbif_static_TEST_001"],"api_response_ids":["gbif_api_response_TEST_001"],"rights_posture":r.get('rights_posture'),"sensitivity_posture":r.get('sensitivity_posture'),"presence_posture":r.get('presence_posture'),"redactions":m.get('redactions',[]),"limitations":[L1,L2],"block_reasons":reasons,"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
 for c in out['published_ui_card_ids']: out['public_routes'].append({'route_id':f'route_{c}','route_type':'card','public_url_path':f'/fauna/gbif/cards/{c}','artifact_id':c,'artifact_hash':'sha256:card','cache_key':deterministic_cache_key('card',c)})
 out['public_routes'].append({'route_id':'route_api_occurrence_aggregates','route_type':'api','public_url_path':'/api/fauna/gbif/occurrence-aggregates','artifact_id':'gbif_api_response_TEST_001','artifact_hash':'sha256:api','cache_key':deterministic_cache_key('api','gbif_api_response_TEST_001')})
 errs=scan_forbidden(out)
 if errs: raise SystemExit('\n'.join(errs))
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','distribution_bundle_id'))
 Path(x.output).write_text(json.dumps(out,indent=2)+'\n'); print('ok')
if __name__=='__main__': main()
