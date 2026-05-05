from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

T="tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_transparency.py"
C="tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_governance_calendar.py"

def run(script:str,*args:str):
    return subprocess.run([sys.executable,script,*args],check=False,text=True,capture_output=True)

def test_transparency_help_version()->None:
    assert run(T,"--help").returncode==0
    assert run(T,"--version").returncode==0

def test_calendar_help_version()->None:
    assert run(C,"--help").returncode==0
    assert run(C,"--version").returncode==0

def test_transparency_id_deterministic(tmp_path:Path)->None:
    o1=tmp_path/"a"; p1=tmp_path/"pa"
    r1=run(T,"--out-dir",str(o1),"--public-out-dir",str(p1))
    assert r1.returncode==0, r1.stderr
    id1=json.loads((o1/"transparency_manifest.json").read_text())["transparency_id"]
    o2=tmp_path/"b"; p2=tmp_path/"pb"
    r2=run(T,"--out-dir",str(o2),"--public-out-dir",str(p2))
    id2=json.loads((o2/"transparency_manifest.json").read_text())["transparency_id"]
    assert id1==id2

def test_calendar_id_and_ics_deterministic(tmp_path:Path)->None:
    a=tmp_path/"c1"; pa=tmp_path/"cp1"
    b=tmp_path/"c2"; pb=tmp_path/"cp2"
    run(C,"--out-dir",str(a),"--public-out-dir",str(pa),"--start-date","2026-01-01","--end-date","2026-12-31")
    run(C,"--out-dir",str(b),"--public-out-dir",str(pb),"--start-date","2026-01-01","--end-date","2026-12-31")
    j1=json.loads((pa/"public_governance_calendar.json").read_text())
    j2=json.loads((pb/"public_governance_calendar.json").read_text())
    assert j1["calendar_id"]==j2["calendar_id"]
    assert (pa/"public_governance_calendar.ics").read_text()==(pb/"public_governance_calendar.ics").read_text()
