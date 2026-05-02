import subprocess
from pathlib import Path
CMD=["python","tools/validators/governance/validate_correction_governance.py"]

def run(p): return subprocess.run(CMD+[str(p)],capture_output=True,text=True)

def test_all_valid_pass():
    for p in Path('tests/fixtures/governance/corrections/valid').glob('*.json'):
        assert run(p).returncode==0, p

def test_all_invalid_fail():
    for p in Path('tests/fixtures/governance/corrections/invalid').glob('*.json'):
        assert run(p).returncode!=0, p
