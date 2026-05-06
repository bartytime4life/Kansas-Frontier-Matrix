import json, subprocess
from pathlib import Path
BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def run(*args):
    return subprocess.check_output([str(BASE/args[0]),*args[1:]], text=True)

def test_maintain_help_and_version():
    subprocess.check_call([str(BASE/'kfm-ebird-maintain'),'--help'])
    assert json.loads(run('kfm-ebird-maintain','--version'))['adapter']=='kfm-ebird'

def test_migrate_help_and_version():
    subprocess.check_call([str(BASE/'kfm-ebird-migrate'),'--help'])
    assert json.loads(run('kfm-ebird-migrate','--version'))['adapter']=='kfm-ebird'

def test_diff_deterministic(tmp_path):
    out=tmp_path/'a'; out2=tmp_path/'b'
    args=['--mode','diff','--from-contract-lock',str(BASE/'contract_lock.json'),'--to-contract-lock',str(BASE/'contract_lock.json')]
    subprocess.check_call([str(BASE/'kfm-ebird-maintain'),*args,'--out-dir',str(out)])
    subprocess.check_call([str(BASE/'kfm-ebird-maintain'),*args,'--out-dir',str(out2)])
    assert (out/'contract_diff_report.json').read_text()==(out2/'contract_diff_report.json').read_text()

def test_migration_apply_requires_force(tmp_path):
    cmd=[str(BASE/'kfm-ebird-migrate'),'--mode','apply','--to-version','1.1.0','--artifact-root',str(BASE)]
    p=subprocess.run(cmd, text=True, capture_output=True)
    assert p.returncode!=0
