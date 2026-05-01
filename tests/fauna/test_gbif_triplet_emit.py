from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
FIX=Path('tests/fixtures/fauna/gbif')

def test_emit_triplet(tmp_path: Path):
    c=tmp_path/'c.json'; cl=tmp_path/'claims.json'
    subprocess.check_call([sys.executable,'tools/catalog/fauna/kfm_gbif_catalog_register.py','--aggregates',str(FIX/'valid/public_aggregates.json'),'--receipt',str(FIX/'valid/geoprivacy_receipt.json'),'--output',str(c)])
    subprocess.check_call([sys.executable,'tools/triplets/fauna/kfm_gbif_triplet_emit.py','--catalog',str(c),'--aggregates',str(FIX/'valid/public_aggregates.json'),'--output',str(cl)])
    d=json.loads(cl.read_text()); assert d and d[0]['evidence']['download_key']=='dl-1'
