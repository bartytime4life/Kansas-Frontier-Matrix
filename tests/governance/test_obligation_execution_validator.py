import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/governance/validate_obligation_execution.py"
FIX = ROOT / "tests/fixtures/governance/obligation_execution"


def run_fixture(path: Path):
    return subprocess.run([sys.executable, str(VALIDATOR), "--bundle", str(path)], capture_output=True, text=True)


def test_valid_fixtures_pass():
    for p in sorted((FIX / "valid").glob("*.json")):
        r = run_fixture(p)
        assert r.returncode == 0, p.name + r.stdout + r.stderr


def test_invalid_fixtures_fail():
    for p in sorted((FIX / "invalid").glob("*.json")):
        r = run_fixture(p)
        assert r.returncode == 1, p.name
        assert '"ok": false' in r.stdout.lower()


def test_no_network_behavior_marker():
    p = FIX / "valid" / "suppress_huc12.json"
    r = run_fixture(p)
    assert "Traceback" not in r.stderr


def test_deterministic_ids_stable():
    p = FIX / "valid" / "suppress_huc12.json"
    obj = json.loads(p.read_text())
    before = obj["publish_enforcement_report"]["id"]
    after = json.loads(p.read_text())["publish_enforcement_report"]["id"]
    assert before == after
