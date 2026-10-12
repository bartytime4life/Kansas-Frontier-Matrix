import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


def test_doctrine_artifact_policy_exists_and_is_non_empty():
    policy_path = ROOT / "policy" / "source" / "doctrine_artifact_required.rego"
    text = policy_path.read_text(encoding="utf-8")
    assert "package" in text
    assert "deny" in text


def test_required_doctrine_artifact_check_fails_until_canonical_artifacts_are_admitted():
    cmd = [sys.executable, str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py")]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    payload = json.loads(res.stdout)
    assert payload["check"] == "required_doctrine_artifacts"
    assert payload["missing_count"] >= 1
    assert payload["result"] == "fail"
    assert isinstance(payload["present"], dict)
    assert payload["status_mismatches"] == []


def test_required_doctrine_artifact_check_writes_receipt(tmp_path: Path):
    out = tmp_path / "doctrine_artifact_check.json"
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "check_required_doctrine_artifacts.py"),
        "--output",
        str(out),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    written = json.loads(out.read_text(encoding="utf-8"))
    assert written["check"] == "required_doctrine_artifacts"
    assert written["result"] == "fail"
    assert isinstance(written["present"], dict)
    assert isinstance(written["status_mismatches"], list)
    assert "integrity" in written


REQUIRED = (
    "KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf",
    "Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf",
    "Master_MapLibre_Components-Functions-Features.pdf",
)


def _opa_binary() -> str:
    binary = os.environ.get("OPA_BIN") or shutil.which("opa")
    if not binary:
        pytest.skip("OPA_BINARY_UNAVAILABLE: install opa or set OPA_BIN to evaluate the Rego")
    return binary


def _eval_deny(present: dict[str, bool]) -> list[str]:
    completed = subprocess.run(
        [_opa_binary(), "eval", "--format", "json", "--stdin-input",
         "--data", str(ROOT / "policy" / "source" / "doctrine_artifact_required.rego"),
         "data.kfm.doctrine_artifact_required.deny"],
        cwd=ROOT, input=json.dumps({"present": present}), capture_output=True, text=True,
        timeout=60, check=False,
    )
    assert completed.returncode == 0, completed.stderr
    return sorted(json.loads(completed.stdout)["result"][0]["expressions"][0]["value"])


def test_doctrine_artifact_policy_denies_each_missing_artifact():
    assert _eval_deny({}) == [f"missing_required_doctrine_artifact:{name}" for name in REQUIRED]
    partial = {REQUIRED[0]: True, REQUIRED[1]: False}
    assert _eval_deny(partial) == [f"missing_required_doctrine_artifact:{name}"
                                   for name in REQUIRED[1:]]


def test_doctrine_artifact_policy_denies_nothing_when_all_artifacts_are_present():
    assert _eval_deny({name: True for name in REQUIRED}) == []
