from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_sign(*args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    run_env = dict(os.environ)
    if env:
        run_env.update(env)
    return subprocess.run(
        [sys.executable, "tools/attest/sign_decision_envelope.py", *args],
        check=False,
        text=True,
        capture_output=True,
        env=run_env,
    )


def run_verify(*args: str, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    run_env = dict(os.environ)
    if env:
        run_env.update(env)
    return subprocess.run(
        [sys.executable, "tools/attest/verify_decision_envelope.py", *args],
        check=False,
        text=True,
        capture_output=True,
        env=run_env,
    )


def decision_fixture() -> dict[str, object]:
    return {
        "decision_id": "kfm://decision/example/1",
        "candidate_ref": "kfm://candidate/ecology/example",
        "status": "allow",
        "spec_hash": "a" * 64,
    }


def test_sign_then_verify_success(tmp_path: Path) -> None:
    decision_path = tmp_path / "decision.json"
    sign_out = tmp_path / "decision-sign-result.json"
    verify_out = tmp_path / "decision-verify-result.json"

    write_json(decision_path, decision_fixture())

    sign = run_sign(
        str(decision_path),
        "--artifact-uri",
        "ghcr.io/example/promotion:overlay-floodplain-kansas-v1",
        "--output",
        str(sign_out),
        "--yes",
        env={"KFM_ATTEST_SIGNING_KEY": "unit-test-key"},
    )

    assert sign.returncode == 0
    assert sign_out.exists()

    verify = run_verify(
        "ghcr.io/example/promotion:overlay-floodplain-kansas-v1",
        "--decision",
        str(decision_path),
        "--sign-result",
        str(sign_out),
        "--output",
        str(verify_out),
        env={"KFM_ATTEST_SIGNING_KEY": "unit-test-key"},
    )

    assert verify.returncode == 0
    assert "verified" in verify.stdout

    result = json.loads(verify_out.read_text(encoding="utf-8"))
    assert result["verified"] is True
    assert result["status"] == "verified"


def test_sign_requires_yes(tmp_path: Path) -> None:
    decision_path = tmp_path / "decision.json"
    sign_out = tmp_path / "decision-sign-result.json"

    write_json(decision_path, decision_fixture())

    sign = run_sign(
        str(decision_path),
        "--artifact-uri",
        "ghcr.io/example/promotion:overlay-floodplain-kansas-v1",
        "--output",
        str(sign_out),
    )

    assert sign.returncode == 4
    assert "pass --yes" in sign.stderr
    assert not sign_out.exists()


def test_verify_fails_on_artifact_mismatch(tmp_path: Path) -> None:
    decision_path = tmp_path / "decision.json"
    sign_out = tmp_path / "decision-sign-result.json"
    verify_out = tmp_path / "decision-verify-result.json"

    write_json(decision_path, decision_fixture())

    sign = run_sign(
        str(decision_path),
        "--artifact-uri",
        "ghcr.io/example/promotion:correct",
        "--output",
        str(sign_out),
        "--yes",
        env={"KFM_ATTEST_SIGNING_KEY": "unit-test-key"},
    )
    assert sign.returncode == 0

    verify = run_verify(
        "ghcr.io/example/promotion:wrong",
        "--decision",
        str(decision_path),
        "--sign-result",
        str(sign_out),
        "--output",
        str(verify_out),
        env={"KFM_ATTEST_SIGNING_KEY": "unit-test-key"},
    )

    assert verify.returncode == 1
    result = json.loads(verify_out.read_text(encoding="utf-8"))
    assert result["verified"] is False
    assert result["checks"]["artifact_uri_match"] is False
