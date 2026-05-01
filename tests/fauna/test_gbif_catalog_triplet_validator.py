from __future__ import annotations
import subprocess, sys
from pathlib import Path
FIX=Path('tests/fixtures/fauna/gbif')
VAL='tools/validators/fauna/gbif_catalog_triplet_validator.py'

def test_missing_receipt_fails():
    r=subprocess.run([sys.executable,VAL,'--catalog',str(FIX/'invalid/public_aggregate_missing_receipt_ref.json')],capture_output=True,text=True)
    assert r.returncode!=0

def test_confirmed_presence_wording_fails():
    r=subprocess.run([sys.executable,VAL,'--claims',str(FIX/'invalid/public_aggregate_confirmed_presence.json')],capture_output=True,text=True)
    assert r.returncode!=0

def test_uncited_answer_fails():
    r=subprocess.run([sys.executable,VAL,'--answer',str(FIX/'invalid/public_aggregate_uncited.json')],capture_output=True,text=True)
    assert r.returncode!=0
