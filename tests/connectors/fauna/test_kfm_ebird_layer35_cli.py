import json, subprocess
from pathlib import Path

BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def test_layer35_help_version():
    assert subprocess.run([str(BASE/'kfm-ebird-hardening-apply'),'--help'],check=False).returncode==0
    assert subprocess.run([str(BASE/'kfm-ebird-contract-refresh'),'--help'],check=False).returncode==0
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-hardening-apply'),'--version'],text=True))['tool']=='hardening-apply'
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-contract-refresh'),'--version'],text=True))['tool']=='contract-refresh'

def test_layer35_plan_and_require_flags(tmp_path):
    o=tmp_path/'h'; p=tmp_path/'hp'
    subprocess.check_call([str(BASE/'kfm-ebird-hardening-apply'),'--mode','plan','--aggregate','both','--out-dir',str(o),'--public-out-dir',str(p),'--force'])
    assert (o/'hardening_apply_plan.json').exists()
    r=subprocess.run([str(BASE/'kfm-ebird-hardening-apply'),'--mode','apply','--out-dir',str(tmp_path/'x'),'--public-out-dir',str(tmp_path/'y')],capture_output=True,text=True)
    assert r.returncode!=0
