import json, subprocess, tempfile
from pathlib import Path
BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def test_help_version():
    assert subprocess.run([str(BASE/'kfm-ebird-consumer-impact'),'--help'],check=False).returncode==0
    assert subprocess.run([str(BASE/'kfm-ebird-consumer-upgrade'),'--help'],check=False).returncode==0
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-consumer-impact'),'--version'],text=True))['adapter']=='kfm-ebird'
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-consumer-upgrade'),'--version'],text=True))['adapter']=='kfm-ebird'

def test_deterministic_ids():
    with tempfile.TemporaryDirectory() as td:
        reg=Path(td)/'reg.json'; reg.write_text(json.dumps({'consumers':[{'consumer_id':'c1'}]}))
        out1=subprocess.check_output([str(BASE/'kfm-ebird-consumer-impact'),'--mode','scan','--aggregate','both','--consumer-registry',str(reg),'--dry-run'],text=True)
        out2=subprocess.check_output([str(BASE/'kfm-ebird-consumer-impact'),'--mode','scan','--aggregate','both','--consumer-registry',str(reg),'--dry-run'],text=True)
        assert json.loads(out1)['impact_id']==json.loads(out2)['impact_id']
