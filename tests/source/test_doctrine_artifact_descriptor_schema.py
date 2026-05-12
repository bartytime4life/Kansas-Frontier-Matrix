import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_doctrine_artifact_descriptor_fixtures_validate():
    cmd = [
        sys.executable,
        str(ROOT / "tools" / "validators" / "source" / "validate_doctrine_artifact_descriptor.py"),
        "--fixtures",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0, res.stdout + res.stderr
