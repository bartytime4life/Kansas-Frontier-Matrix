import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
ARCH=ROOT/'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-archive-handoff'
COLD=ROOT/'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-coldstart'
CK=ROOT/'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-checkpoint'


def run(cmd,*args):
    return subprocess.run([str(cmd),*map(str,args)],capture_output=True,text=True)

def test_help_version():
    assert run(ARCH,'--help').returncode==0
    assert run(ARCH,'--version').returncode==0
    assert run(COLD,'--help').returncode==0
    assert run(COLD,'--version').returncode==0

def test_archive_and_coldstart(tmp_path:Path):
    ck=tmp_path/'ck'; pub=tmp_path/'pub'
    assert run(CK,'--mode','build','--aggregate','both','--out-dir',ck,'--public-out-dir',pub).returncode==0
    out=tmp_path/'a'; pout=tmp_path/'apub'
    r=run(ARCH,'--mode','build','--aggregate','both','--checkpoint-manifest',ck/'checkpoint_manifest.json','--out-dir',out,'--public-out-dir',pout,'--archive-root',tmp_path/'arch','--public-archive-root',tmp_path/'parch','--force')
    assert r.returncode==0, r.stderr
    manifest=out/'archive_handoff_manifest.json'
    c=run(COLD,'--mode','plan','--aggregate','both','--archive-handoff-manifest',manifest,'--out-dir',tmp_path/'c','--public-out-dir',tmp_path/'cpub')
    assert c.returncode==0, c.stderr
    plan=json.loads((tmp_path/'c'/'coldstart_plan.json').read_text())
    assert plan['coldstart_id']
