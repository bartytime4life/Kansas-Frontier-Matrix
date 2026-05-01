import json, tempfile, copy
from pathlib import Path
from tools.publication.fauna.kfm_gbif_publication_package import main as build
from tools.validators.fauna.gbif_publication_ops_validator import stable_hash

def run_build(tmp):
    import subprocess
    cmd=['python','tools/publication/fauna/kfm_gbif_publication_package.py','--evidencebundle','tests/fixtures/fauna/gbif/valid/publication_chain/evidencebundle.json','--aggregates','tests/fixtures/fauna/gbif/valid/publication_chain/public_aggregates.json','--geoprivacy-receipt','tests/fixtures/fauna/gbif/valid/publication_chain/geoprivacy_receipt.json','--catalog','tests/fixtures/fauna/gbif/valid/publication_chain/catalog_entries.json','--claims','tests/fixtures/fauna/gbif/valid/publication_chain/triplet_claims.json','--answer','tests/fixtures/fauna/gbif/valid/publication_chain/runtime_answer.json','--ui-cards','tests/fixtures/fauna/gbif/valid/publication_chain/ui_cards.json','--answer-receipt','tests/fixtures/fauna/gbif/valid/publication_chain/answer_receipt.json','--output',str(tmp)]
    subprocess.check_call(cmd)

def test_valid_full_chain_creates_package_successfully(tmp_path):
    out=tmp_path/'pkg.json'; run_build(out); pkg=json.loads(out.read_text()); assert pkg['source_evidence_bundle_ids']==['evidence_TEST_001']

def test_spec_hash_stable_when_created_at_changes(tmp_path):
    out=tmp_path/'pkg.json'; run_build(out); pkg=json.loads(out.read_text()); p2=copy.deepcopy(pkg); p2['created_at']='2030-01-01T00:00:00Z';
    assert stable_hash(pkg,exclude=('created_at','publication_package_id','kfm:spec_hash'))==stable_hash(p2,exclude=('created_at','publication_package_id','kfm:spec_hash'))
