from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
FIX=Path('tests/fixtures/fauna/gbif')

def _claims(tmp_path: Path):
    c=tmp_path/'c.json'; cl=tmp_path/'cl.json'
    subprocess.check_call([sys.executable,'tools/catalog/fauna/kfm_gbif_catalog_register.py','--aggregates',str(FIX/'valid/public_aggregates.json'),'--receipt',str(FIX/'valid/geoprivacy_receipt.json'),'--output',str(c)])
    subprocess.check_call([sys.executable,'tools/triplets/fauna/kfm_gbif_triplet_emit.py','--catalog',str(c),'--aggregates',str(FIX/'valid/public_aggregates.json'),'--output',str(cl)])
    return cl

def test_cited_answer(tmp_path: Path):
    cl=_claims(tmp_path); out=tmp_path/'a.json'
    subprocess.check_call([sys.executable,'tools/readmodels/fauna/kfm_gbif_occurrence_readmodel.py','--claims',str(cl),'--taxon-key','tx-1','--geography-id','county-001','--aggregation-unit','county','--output',str(out)])
    assert json.loads(out.read_text())['answer_posture']=='cited_answer'

def test_abstain_no_claim(tmp_path: Path):
    cl=_claims(tmp_path); out=tmp_path/'a.json'
    subprocess.check_call([sys.executable,'tools/readmodels/fauna/kfm_gbif_occurrence_readmodel.py','--claims',str(cl),'--taxon-key','none','--geography-id','county-001','--aggregation-unit','county','--output',str(out)])
    assert json.loads(out.read_text())['answer_posture']=='abstain'

def test_abstain_exact_coords(tmp_path: Path):
    cl=_claims(tmp_path); out=tmp_path/'a.json'
    subprocess.check_call([sys.executable,'tools/readmodels/fauna/kfm_gbif_occurrence_readmodel.py','--claims',str(cl),'--query-text','need exact coordinates','--output',str(out)])
    assert json.loads(out.read_text())['abstain_reason']=='exact_coordinate_request'
