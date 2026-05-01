import subprocess,sys,json
from pathlib import Path
FIX=Path('tests/fixtures/fauna/gbif')

def test_cli_query_fixture(tmp_path):
    o=tmp_path/'o.json'; r=tmp_path/'r.json'
    rc=subprocess.run([sys.executable,'tools/runtime/fauna/kfm_gbif_answer_cli.py','--claims',str(FIX/'valid/gbif_occurrence_claims.json'),'--query',str(FIX/'valid/runtime_query_taxa_in_county.json'),'--output',str(o),'--receipt-output',str(r)]).returncode
    assert rc==0 and json.loads(o.read_text()) and json.loads(r.read_text())

def test_cli_direct_args(tmp_path):
    o=tmp_path/'o.json'; r=tmp_path/'r.json'
    rc=subprocess.run([sys.executable,'tools/runtime/fauna/kfm_gbif_answer_cli.py','--claims',str(FIX/'valid/gbif_occurrence_claims.json'),'--query-type','evidence_for_taxon_geography','--taxon-key','TEST_TAXON_KEY','--geography-id','KS-DOUGLAS','--aggregation-unit','county','--include-ui-cards','--output',str(o),'--receipt-output',str(r)]).returncode
    assert rc==0

def test_cli_malformed_nonzero(tmp_path):
    rc=subprocess.run([sys.executable,'tools/runtime/fauna/kfm_gbif_answer_cli.py','--claims','missing.json','--query-type','evidence_for_taxon_geography','--output',str(tmp_path/'o'),'--receipt-output',str(tmp_path/'r')]).returncode
    assert rc!=0
