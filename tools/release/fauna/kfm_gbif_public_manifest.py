#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.fauna.gbif_review_release_validator import stable_hash, scan_forbidden

def load(p): return json.loads(Path(p).read_text())
def dump(p,d): Path(p).write_text(json.dumps(d,indent=2)+"\n")

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--release-registry',required=True); ap.add_argument('--package',required=True); ap.add_argument('--output',required=True); a=ap.parse_args()
 r,p=load(a.release_registry),load(a.package)
 out={'manifest_id':'gbif_public_manifest_TEST_001','manifest_version':'gbif_public_manifest.v1','domain':'fauna','source_system':'GBIF','release_channel':'public','release_registry_entry_ids':[r.get('release_registry_entry_id')],'published_package_ids':[p.get('publication_package_id')],'published_answer_ids':p.get('answer_ids',[]),'published_ui_card_ids':p.get('ui_card_ids',[]),'published_map_layer_ids':[],'citation_index':[{'source_system':'GBIF','source_evidence_bundle_id':p.get('source_evidence_bundle_ids',[None])[0],'download_key':p.get('download_keys',[None])[0],'query_predicate_hash':p.get('query_predicate_hashes',[None])[0],'source_aggregate_id':p.get('public_aggregate_ids',[None])[0],'geoprivacy_receipt_ref':p.get('geoprivacy_receipt_refs',[None])[0],'answer_receipt_ref':p.get('answer_receipt_refs',[None])[0],'kfm:spec_hash':'sha256:cit'}],'safe_public_artifacts':[{'artifact_id':p.get('ui_card_ids',[None])[0],'artifact_type':'ui_card','public_url_path':f"/fauna/gbif/cards/{p.get('ui_card_ids',[None])[0]}",'artifact_hash':'sha256:card'}],'redactions':['exact occurrence coordinates not emitted','raw GBIF point locations not emitted'],'limitations':['GBIF occurrence aggregates are reported occurrence evidence, not confirmed species-presence determinations.','Public output is generalized and does not expose exact occurrence coordinates.'],'created_at':'2026-01-01T00:00:00Z'}
 out['kfm:spec_hash']=stable_hash(out,exclude=('created_at','manifest_id'))
 dump(a.output,out); print('ok')
if __name__=='__main__': main()
