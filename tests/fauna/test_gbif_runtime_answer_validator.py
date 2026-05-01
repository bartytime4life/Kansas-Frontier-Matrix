import json,subprocess,sys,tempfile
from pathlib import Path
FIX=Path('tests/fixtures/fauna/gbif')

def run(kind,obj):
    with tempfile.NamedTemporaryFile('w',suffix='.json',delete=False) as f:
        json.dump(obj,f); p=f.name
    return subprocess.run([sys.executable,'tools/validators/fauna/gbif_runtime_answer_validator.py','--kind',kind,'--input',p])

def test_validator_rejects_forbidden_language():
    ans=json.loads((FIX/'valid/gbif_occurrence_claims.json').read_text())[0]
    bad={'answer_posture':'abstain','summary':'confirmed present','kfm:spec_hash':'x'}
    assert run('answer',bad).returncode!=0

def test_validator_rejects_coordinate_field():
    bad={'answer_posture':'abstain','decimalLatitude':1,'kfm:spec_hash':'x'}
    assert run('answer',bad).returncode!=0
