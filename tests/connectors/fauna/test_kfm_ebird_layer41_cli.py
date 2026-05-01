import json, subprocess
from pathlib import Path
BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')


def test_help_version():
    assert subprocess.run([str(BASE/'kfm-ebird-archive-renew'),'--help'],check=False).returncode==0
    assert subprocess.run([str(BASE/'kfm-ebird-preservation-supersede'),'--help'],check=False).returncode==0
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-archive-renew'),'--version'],text=True))['adapter']=='kfm-ebird'
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-preservation-supersede'),'--version'],text=True))['adapter']=='kfm-ebird'


def test_deterministic_ids(tmp_path:Path):
    a=json.loads(subprocess.check_output([str(BASE/'kfm-ebird-archive-renew'),'--mode','plan','--aggregate','both','--out-dir',str(tmp_path/'a')],text=True))
    b=json.loads(subprocess.check_output([str(BASE/'kfm-ebird-archive-renew'),'--mode','plan','--aggregate','both','--out-dir',str(tmp_path/'b')],text=True))
    assert a['archive_renewal_id']==b['archive_renewal_id']


def test_requires_flags(tmp_path:Path):
    r=subprocess.run([str(BASE/'kfm-ebird-archive-renew'),'--mode','renew-local','--out-dir',str(tmp_path/'x')],capture_output=True,text=True)
    assert r.returncode!=0
