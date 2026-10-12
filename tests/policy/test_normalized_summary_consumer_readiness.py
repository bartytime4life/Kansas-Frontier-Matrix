import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.parametrize("registry_text", [
    "normalized_summary_consumers: []\n",
    "normalized_summary_consumers:\n",
    "normalized_summary_consumers:\n  # no enrolled consumers\n",
    "normalized_summary_consumers: null\n",
])
@pytest.mark.parametrize("strict", [False, True])
def test_empty_consumer_inventory_fails_closed(tmp_path, registry_text, strict):
    registry = tmp_path / "empty.yaml"
    registry.write_text(registry_text, encoding="utf-8")
    command = [sys.executable, str(ROOT / "scripts/maintenance/check_normalized_summary_consumer_readiness.py"),
               "--registry", str(registry)]
    if strict:
        command.append("--require-all-validated")
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=5)
    assert result.returncode == 1
    assert result.stderr == ""
    payload = json.loads(result.stdout)
    assert payload["check"] == "normalized_summary_consumer_readiness"
    assert payload["consumer_count"] == 0
    assert payload["result"] == "fail"
    assert payload["errors"] == ["normalized_summary_consumers must contain at least one consumer"]
    assert payload["require_all_validated"] is strict


def test_normalized_summary_consumer_readiness_passes_for_repo_registry():
    cmd = [sys.executable, str(ROOT / "scripts" / "maintenance" / "check_normalized_summary_consumer_readiness.py")]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["check"] == "normalized_summary_consumer_readiness"
    assert payload["result"] == "pass"


def test_normalized_summary_consumer_readiness_detects_invalid_entry(tmp_path: Path):
    bad = tmp_path / "readiness.yaml"
    bad.write_text(
        """normalized_summary_consumers:\n  - consumer: a\n    owner: team\n    status: wrong\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_normalized_summary_consumer_readiness.py"),
        "--registry",
        str(bad),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["result"] == "fail"
    assert payload["errors"]


def test_normalized_summary_consumer_readiness_require_all_validated_fails(tmp_path: Path):
    reg = tmp_path / "readiness.yaml"
    reg.write_text(
        """normalized_summary_consumers:\n  - consumer: a\n    owner: team\n    status: pending\n    validated_utc: 2026-05-13\n    evidence: ci\n    notes: n\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_normalized_summary_consumer_readiness.py"),
        "--registry",
        str(reg),
        "--require-all-validated",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["require_all_validated"] is True
    assert any("non-validated consumers" in e for e in payload["errors"])
