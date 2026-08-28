import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_presence_input_renderer_emits_present_map(tmp_path: Path):
    receipt = tmp_path / "receipt.json"
    check_cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--output",
        str(receipt),
    ]
    subprocess.run(check_cmd, cwd=ROOT, check=False, capture_output=True, text=True)

    render_cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "render_doctrine_presence_input.py"),
        str(receipt),
    ]
    res = subprocess.run(render_cmd, cwd=ROOT, check=True, capture_output=True, text=True)
    payload = json.loads(res.stdout)
    assert "present" in payload
    assert isinstance(payload["present"], dict)
    assert len(payload["present"]) == 3
