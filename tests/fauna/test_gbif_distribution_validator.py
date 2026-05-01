import json
from tools.validators.fauna.gbif_distribution_validator import validate

def test_validator_flags_forbidden_and_missing():
 d={"search_index_record_id":"x","kfm:spec_hash":"y","title":"confirmed present","public_url_path":"/x"}
 errs=validate('search',d)
 assert any('forbidden language' in e for e in errs)
 assert any('citation' in e for e in errs)
