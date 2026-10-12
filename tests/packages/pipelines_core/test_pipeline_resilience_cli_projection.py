from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CLI = REPO_ROOT / "scripts/plan_pipeline_resilience.py"
FIXTURE = (
    REPO_ROOT
    / "fixtures/contracts/v1/runtime/pipeline_resilience_plan/valid/"
    / "allow_start.request.json"
)


def test_cli_operator_projection_omits_restricted_access_metadata() -> None:
    completed = subprocess.run(
        [sys.executable, str(CLI), str(FIXTURE)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    assert '"secret_scope"' not in completed.stdout
    assert '"secret_access"' not in completed.stdout

    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "ANSWER"
    assert payload["plan"]["projection"] == "operator-safe-v1"
    assert payload["plan"]["decision"] == "ALLOW_START"
    assert set(payload["authority"].values()) == {False}


def test_cli_oversized_number_returns_finite_denial(tmp_path: Path) -> None:
    request = json.loads(FIXTURE.read_text(encoding="utf-8"))
    request["queue"]["oldest_age_seconds"] = 10**1000
    path = tmp_path / "oversized.request.json"
    path.write_text(json.dumps(request), encoding="utf-8")

    completed = subprocess.run(
        [sys.executable, str(CLI), str(path)],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 1
    payload = json.loads(completed.stdout)
    assert payload["outcome"] == "DENY"
    assert payload["plan"] is None
    assert payload["findings"] == [
        {"code": "NUMBER_NOT_FINITE", "path": "/queue/oldest_age_seconds"}
    ]
