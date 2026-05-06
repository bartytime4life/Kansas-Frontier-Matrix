import json, subprocess
from pathlib import Path
BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def test_help_version():
    assert subprocess.run([str(BASE/'kfm-ebird-fixity'),'--help'],check=False).returncode==0
    assert subprocess.run([str(BASE/'kfm-ebird-preservation'),'--help'],check=False).returncode==0
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-fixity'),'--version'],text=True))['adapter']=='kfm-ebird'
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-preservation'),'--version'],text=True))['adapter']=='kfm-ebird'

def test_deterministic_ids(tmp_path):
    out1=json.loads(subprocess.check_output([str(BASE/'kfm-ebird-fixity'),'--mode','scan','--aggregate','both','--out-dir',str(tmp_path/'a'),'--public-out-dir',str(tmp_path/'ap')],text=True))
    out2=json.loads(subprocess.check_output([str(BASE/'kfm-ebird-fixity'),'--mode','scan','--aggregate','both','--out-dir',str(tmp_path/'b'),'--public-out-dir',str(tmp_path/'bp')],text=True))
    assert out1['fixity_run_id']==out2['fixity_run_id']
