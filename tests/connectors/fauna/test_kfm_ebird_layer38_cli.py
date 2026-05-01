import json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
REST=ROOT/'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-checkpoint-restore'
CONT=ROOT/'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-continuity-drill'
CK=ROOT/'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-checkpoint'

def run(cmd,*args):
    return subprocess.run([str(cmd),*map(str,args)],capture_output=True,text=True)

def test_help_version():
    assert run(REST,'--help').returncode==0
    assert run(REST,'--version').returncode==0
    assert run(CONT,'--help').returncode==0
    assert run(CONT,'--version').returncode==0

def test_plan_and_continuity(tmp_path:Path):
    ck=tmp_path/'ck'; pub=tmp_path/'pub'
    assert run(CK,'--mode','build','--aggregate','both','--out-dir',ck,'--public-out-dir',pub).returncode==0
    out=tmp_path/'restore'; ppub=tmp_path/'ppub'
    r=run(REST,'--mode','plan','--aggregate','both','--checkpoint-manifest',ck/'checkpoint_manifest.json','--out-dir',out,'--public-out-dir',ppub)
    assert r.returncode==0, r.stderr
    plan=json.loads((out/'checkpoint_restore_plan.json').read_text())
    assert plan['restore_id']
    cdir=tmp_path/'cont'; cpub=tmp_path/'cpub'
    r2=run(CONT,'--mode','run','--aggregate','both','--out-dir',cdir,'--public-out-dir',cpub)
    assert r2.returncode==0, r2.stderr
    ready=json.loads((cdir/'continuity_readiness_report.json').read_text())
    assert ready['status'] in {'pass','warn','fail'}
