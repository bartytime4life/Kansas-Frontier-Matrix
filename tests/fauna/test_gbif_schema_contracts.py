import pytest
pytest.importorskip("jsonschema", reason="jsonschema dependency unavailable in this environment")

import json
from pathlib import Path
from jsonschema import Draft202012Validator
FIX=Path('tests/fixtures/fauna/gbif')

def test_query_schema_validates():
    s=json.loads(Path('schemas/runtime/fauna/gbif_occurrence_query.schema.json').read_text())
    q=json.loads((FIX/'valid/runtime_query_taxa_in_county.json').read_text())
    assert not list(Draft202012Validator(s).iter_errors(q))
