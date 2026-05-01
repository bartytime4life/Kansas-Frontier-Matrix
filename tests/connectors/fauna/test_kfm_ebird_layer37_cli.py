import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
CK=ROOT/'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-checkpoint'
LG=ROOT/'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-ledger'


def run(*args):
    return subprocess.run([str(args[0]),*map(str,args[1:])],capture_output=True,text=True)


def test_help_version():
    assert run(CK,'--help').returncode==0
    assert run(CK,'--version').returncode==0
    assert run(LG,'--help').returncode==0
    assert run(LG,'--version').returncode==0


def test_checkpoint_and_ledger(tmp_path:Path):
    out=tmp_path/'catalog'; pub=tmp_path/'public'
    r=run(CK,'--mode','build','--aggregate','both','--out-dir',out,'--public-out-dir',pub)
    assert r.returncode==0, r.stderr
    m=json.loads((out/'checkpoint_manifest.json').read_text())
    assert m['checkpoint_id']
    assert any(p['proof_type']=='checkpoint_hash' for p in json.loads((out/'checkpoint_proof_bundle.json').read_text())['proofs'])
    led=tmp_path/'ledger.jsonl'; lout=tmp_path/'lrun'
    r2=run(LG,'--mode','append','--aggregate','both','--checkpoint-manifest',out/'checkpoint_manifest.json','--ledger-path',led,'--out-dir',lout,'--apply','--force')
    assert r2.returncode==0, r2.stderr
    rec=json.loads((lout/'ledger_append_receipt.json').read_text())
    assert rec['apply_used'] is True and rec['force_used'] is True
