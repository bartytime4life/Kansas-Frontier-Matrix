import json, subprocess
from pathlib import Path
BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def test_help_version():
    assert subprocess.run([str(BASE/'kfm-ebird-consumer-registry'),'--help'],check=False).returncode==0
    assert subprocess.run([str(BASE/'kfm-ebird-advisory'),'--help'],check=False).returncode==0
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-consumer-registry'),'--version'],text=True))['adapter']=='kfm-ebird'
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-advisory'),'--version'],text=True))['adapter']=='kfm-ebird'

def test_ids_deterministic(tmp_path):
    cmd=[str(BASE/'kfm-ebird-consumer-registry'),'--mode','plan','--aggregate','both','--out-dir',str(tmp_path/'a'),'--public-out-dir',str(tmp_path/'b'),'--decision','renewed']
    o1=json.loads(subprocess.check_output(cmd,text=True)); o2=json.loads(subprocess.check_output(cmd,text=True)); assert o1['registry_run_id']==o2['registry_run_id']
    acmd=[str(BASE/'kfm-ebird-advisory'),'--mode','plan','--aggregate','both','--advisory-type','consumer_reaudit','--severity','medium','--out-dir',str(tmp_path/'c'),'--public-out-dir',str(tmp_path/'d'),'--title','x','--summary','y']
    a1=json.loads(subprocess.check_output(acmd,text=True)); a2=json.loads(subprocess.check_output(acmd,text=True)); assert a1['advisory_id']==a2['advisory_id']

def test_apply_force_required(tmp_path):
    r=subprocess.run([str(BASE/'kfm-ebird-consumer-registry'),'--mode','apply','--out-dir',str(tmp_path/'o'),'--public-out-dir',str(tmp_path/'p')],capture_output=True,text=True)
    assert r.returncode!=0
