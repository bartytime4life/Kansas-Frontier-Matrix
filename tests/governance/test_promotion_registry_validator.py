import json,subprocess
from pathlib import Path

VALIDATOR=["python","tools/validators/governance/validate_promotion_registry.py"]

def run(path):
    return subprocess.run(VALIDATOR+[str(path)],capture_output=True,text=True)

def test_valid_minimal_registry_passes():
    r=run(Path('tests/fixtures/governance/promotion/valid/minimal_registry.json')); assert r.returncode==0

def test_valid_full_registry_passes():
    r=run(Path('tests/fixtures/governance/promotion/valid/full_registry.json')); assert r.returncode==0

def test_invalid_fixtures_fail():
    for p in Path('tests/fixtures/governance/promotion/invalid').glob('*.json'):
        r=run(p); assert r.returncode!=0, p
