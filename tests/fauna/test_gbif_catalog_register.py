from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
FIX=Path('tests/fixtures/fauna/gbif')
CMD='tools/catalog/fauna/kfm_gbif_catalog_register.py'

def test_valid_register(tmp_path: Path):
    out=tmp_path/'catalog.json'
    r=subprocess.run([sys.executable,CMD,'--aggregates',str(FIX/'valid/public_aggregates.json'),'--receipt',str(FIX/'valid/geoprivacy_receipt.json'),'--output',str(out)],capture_output=True,text=True)
    assert r.returncode==0, r.stderr
    d=json.loads(out.read_text())[0]
    assert d['source_evidence_bundle_id']=='eb-1'

def test_spec_hash_stable_created_at():
    from tools.catalog.fauna.kfm_gbif_catalog_register import compute_spec_hash
    d={'a':1,'created_at':'x','aggregate_ids':[]}
    h=compute_spec_hash(d); d['created_at']='y'; assert h==compute_spec_hash(d)
