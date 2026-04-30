import json, subprocess, tempfile
from pathlib import Path

def test_validator_rejects_latitude_in_public_safe():
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/'x.json'
        p.write_text(json.dumps({'public_safe':True,'latitude':1})+'\n')
        r=subprocess.run(['python','tools/validators/fauna/validate_observability.py',str(p)],capture_output=True,text=True)
        assert r.returncode!=0
