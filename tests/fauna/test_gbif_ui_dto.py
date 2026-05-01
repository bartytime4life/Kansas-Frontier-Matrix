import json
from pathlib import Path
from tools.runtime.fauna.kfm_gbif_answer_service import build_answer
FIX=Path('tests/fixtures/fauna/gbif')

def test_ui_cards_and_layers():
    claims=json.loads((FIX/'valid/gbif_occurrence_claims.json').read_text())
    q=json.loads((FIX/'valid/runtime_query_taxon_geographies.json').read_text()); q['include_ui_cards']=True; q['include_geometry']=True
    ans,_=build_answer(claims,q)
    card=ans['ui_cards'][0]
    assert 'not confirmed presence' in card['badges']
    assert card['citations']
    assert 'decimalLatitude' not in json.dumps(card)
    assert ans['map_layers'][0]['geometry_role']=='generalized_public_area'
