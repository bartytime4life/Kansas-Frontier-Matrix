import json
from pathlib import Path
from tools.runtime.fauna.kfm_gbif_answer_service import build_answer
FIX=Path('tests/fixtures/fauna/gbif')

def load(p): return json.loads((FIX/p).read_text())

def test_valid_queries_cited():
    claims=load('valid/gbif_occurrence_claims.json')
    for qf in ['valid/runtime_query_taxa_in_county.json','valid/runtime_query_taxon_geographies.json']:
        ans,rec=build_answer(claims,load(qf)); assert ans['answer_posture']=='cited_answer'; assert rec['policy_version']

def test_abstains():
    claims=load('valid/gbif_occurrence_claims.json')
    q=load('valid/runtime_query_taxa_in_county.json'); q['taxon_key']='NOPE'; assert build_answer(claims,q)[0]['abstain_reason']=='no_matching_cited_claim'
    assert build_answer(claims,load('invalid/runtime_query_exact_coordinates.json'))[0]['abstain_reason']=='exact_coordinates_requested'
    assert build_answer(claims,load('invalid/runtime_query_confirmed_presence.json'))[0]['abstain_reason']=='confirmed_presence_requested'
    assert build_answer(load('invalid/claims_restricted_rights.json'),load('valid/runtime_query_taxa_in_county.json'))[0]['abstain_reason']=='restricted_rights'
    assert build_answer(load('invalid/claims_restricted_sensitivity.json'),load('valid/runtime_query_taxa_in_county.json'))[0]['abstain_reason']=='restricted_sensitivity'
    assert build_answer(load('invalid/claims_missing_citations.json'),load('valid/runtime_query_taxa_in_county.json'))[0]['abstain_reason']=='missing_citation'
