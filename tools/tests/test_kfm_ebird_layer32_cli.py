from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

VK='tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_verifier.py'
OV='tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_verify_offline.py'

def run(s,*a): return subprocess.run([sys.executable,s,*a],capture_output=True,text=True)

def test_help_version()->None:
    assert run(VK,'--help').returncode==0
    assert run(VK,'--version').returncode==0
    assert run(OV,'--help').returncode==0
    assert run(OV,'--version').returncode==0

def test_ids_deterministic(tmp_path:Path)->None:
    a=tmp_path/'a'; pa=tmp_path/'pa'; b=tmp_path/'b'; pb=tmp_path/'pb'
    r1=run(VK,'--out-dir',str(a),'--public-out-dir',str(pa)); assert r1.returncode==0, r1.stderr
    r2=run(VK,'--out-dir',str(b),'--public-out-dir',str(pb)); assert r2.returncode==0, r2.stderr
    id1=json.loads((a/'verifier_kit_manifest.json').read_text())['verifier_kit_id']
    id2=json.loads((b/'verifier_kit_manifest.json').read_text())['verifier_kit_id']
    assert id1==id2
    o1=tmp_path/'o1'; op1=tmp_path/'op1'; o2=tmp_path/'o2'; op2=tmp_path/'op2'
    rr1=run(OV,'--public-verifier-kit-manifest',str(pa/'public_verifier_kit_manifest.json'),'--verifier-proof-index',str(pa/'public_verifier_proof_index.json'),'--checksum-inventory',str(pa/'public_verifier_checksum_inventory.txt'),'--out-dir',str(o1),'--public-out-dir',str(op1),'--strict')
    rr2=run(OV,'--public-verifier-kit-manifest',str(pb/'public_verifier_kit_manifest.json'),'--verifier-proof-index',str(pb/'public_verifier_proof_index.json'),'--checksum-inventory',str(pb/'public_verifier_checksum_inventory.txt'),'--out-dir',str(o2),'--public-out-dir',str(op2),'--strict')
    assert rr1.returncode==0 and rr2.returncode==0
    v1=json.loads((o1/'offline_verification_report.json').read_text())['verification_id']
    v2=json.loads((o2/'offline_verification_report.json').read_text())['verification_id']
    assert v1==v2
