import json, subprocess
from pathlib import Path
BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def test_layer36_help_version():
    assert subprocess.run([str(BASE/'kfm-ebird-rebaseline'),'--help'],check=False).returncode==0
    assert subprocess.run([str(BASE/'kfm-ebird-baseline-propagate'),'--help'],check=False).returncode==0
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-rebaseline'),'--version'],text=True))['tool']=='rebaseline'
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-baseline-propagate'),'--version'],text=True))['tool']=='baseline-propagate'

def test_layer36_deterministic_ids_and_flags(tmp_path):
    out1=tmp_path/'r1'; pub1=tmp_path/'p1'; work1=tmp_path/'w1'
    a=json.loads(subprocess.check_output([str(BASE/'kfm-ebird-rebaseline'),'--mode','plan','--aggregate','both','--out-dir',str(out1),'--public-out-dir',str(pub1),'--work-dir',str(work1),'--force'],text=True))
    out2=tmp_path/'r2'; pub2=tmp_path/'p2'; work2=tmp_path/'w2'
    b=json.loads(subprocess.check_output([str(BASE/'kfm-ebird-rebaseline'),'--mode','plan','--aggregate','both','--out-dir',str(out2),'--public-out-dir',str(pub2),'--work-dir',str(work2),'--force'],text=True))
    assert a['rebaseline_id']==b['rebaseline_id']
    p1=tmp_path/'bp1'; pp1=tmp_path/'bpp1'
    c=json.loads(subprocess.check_output([str(BASE/'kfm-ebird-baseline-propagate'),'--mode','plan','--aggregate','both','--out-dir',str(p1),'--public-out-dir',str(pp1),'--force'],text=True))
    p2=tmp_path/'bp2'; pp2=tmp_path/'bpp2'
    d=json.loads(subprocess.check_output([str(BASE/'kfm-ebird-baseline-propagate'),'--mode','plan','--aggregate','both','--out-dir',str(p2),'--public-out-dir',str(pp2),'--force'],text=True))
    assert c['baseline_propagation_id']==d['baseline_propagation_id']
    fail=subprocess.run([str(BASE/'kfm-ebird-baseline-propagate'),'--mode','apply-local'],capture_output=True,text=True)
    assert fail.returncode!=0
