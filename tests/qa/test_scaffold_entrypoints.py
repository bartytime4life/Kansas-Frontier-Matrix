"""Unimplemented operator tools cannot report successful work or mutate inputs."""
from __future__ import annotations

import os
from pathlib import Path
import runpy
import socket
import subprocess
import sys

import pytest
import yaml

from tools.validators.ci_readiness import classify_validator_source


ROOT = Path(__file__).resolve().parents[2]
HELD_ENTRYPOINTS = (
    "scripts/maintenance/audit_published_aliases.py",
    "tools/scripts/aggregate.py",
    "tools/validators/ai/validate_evidence_before_model.py",
    "tools/validators/domains/atmosphere/validate_aod_raster.py",
    "tools/validators/domains/atmosphere/validate_atmosphere_decision_envelope.py",
    "tools/validators/domains/atmosphere/validate_forecast_context.py",
    "tools/validators/domains/atmosphere/validate_parameter_units.py",
    "tools/validators/domains/atmosphere/validate_smoke_context.py",
    "tools/validators/domains/geology/validate_public_safe_geometry.py",
    "tools/validators/evidence/validate_identity.py",
    "tools/validators/genealogy/validate_consent_receipt.py",
    "tools/validators/genealogy/validate_gedcom.py",
    "tools/validators/hydro/check_crosswalk.py",
    "tools/validators/hydro/check_huc12.py",
    "tools/validators/hydro/emit_manifest.py",
    "tools/validators/identity/jcs_spec_hash.py",
    "tools/validators/validate_attestation_ref.py",
)


@pytest.mark.parametrize("relative", HELD_ENTRYPOINTS)
@pytest.mark.parametrize("arguments", [(), ("--help",), ("private-input.json", "--output", "private-output.json")])
def test_unimplemented_cli_holds_without_touching_inputs(relative, arguments, tmp_path) -> None:
    source = tmp_path / "private-input.json"
    source.write_text('{"synthetic_private_content": "retain unchanged"}\n')
    before = {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    result = subprocess.run(
        [sys.executable, "-B", str(ROOT / relative), *arguments],
        cwd=tmp_path, capture_output=True, text=True, check=False, timeout=10,
    )
    assert result.returncode == 3, (result.stdout, result.stderr)
    assert result.stdout == ""
    assert result.stderr == f"WORKFLOW_HOLD: {relative} is not implemented; no work was performed.\n"
    assert before == {p.name: p.read_bytes() for p in tmp_path.iterdir()}
    assert str(ROOT) not in result.stderr
    assert str(tmp_path) not in result.stderr


@pytest.mark.parametrize("relative", HELD_ENTRYPOINTS)
def test_importing_placeholder_remains_inert(relative, monkeypatch, capsys) -> None:
    def forbidden(*args, **kwargs):
        raise AssertionError("placeholder attempted a side effect during import")

    monkeypatch.setattr(socket, "socket", forbidden)
    monkeypatch.setattr(subprocess, "Popen", forbidden)
    monkeypatch.setattr(Path, "write_text", forbidden)
    monkeypatch.setattr(Path, "write_bytes", forbidden)
    runpy.run_path(str(ROOT / relative), run_name="unimplemented_tool_import")
    assert capsys.readouterr() == ("", "")


@pytest.mark.parametrize("relative", HELD_ENTRYPOINTS)
def test_named_holds_remain_unimplemented_for_readiness(relative) -> None:
    result = classify_validator_source((ROOT / relative).read_text())
    assert result.placeholder is True
    assert result.detail == "explicit unimplemented HOLD"


def _published_alias_guard() -> str:
    workflow = yaml.safe_load((ROOT / ".github/workflows/rollback-drill.yml").read_text())
    steps = workflow["jobs"]["verify-published-aliases"]["steps"]
    script = next(step["run"] for step in steps
                  if step["name"] == "Confirm published-alias verification remains an explicit hold")
    return script.split("python - <<'PY'\n", 1)[1].split("\nPY", 1)[0]


@pytest.mark.parametrize("mutation", [None, "auditor", "alias", "rollback-payload"])
def test_real_alias_workflow_guard_preserves_absence_and_exact_source_checks(tmp_path, mutation) -> None:
    required = (
        "scripts/maintenance/audit_published_aliases.py",
        "docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md",
        "data/published/README.md",
        "data/rollback/README.md",
        "release/rollback_cards/README.md",
    )
    for relative in required:
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / relative).read_bytes())
    if mutation == "auditor":
        target = tmp_path / required[0]
        target.write_text(target.read_text() + "\nprint('unexpected work')\n")
    elif mutation in {"alias", "rollback-payload"}:
        relative = "data/published/water/current.json" if mutation == "alias" else "data/rollback/payload.json"
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("{}\n")
    before = {str(p.relative_to(tmp_path)): p.read_bytes()
              for p in tmp_path.rglob("*") if p.is_file()}
    env = {**os.environ, "KFM_NO_NETWORK": "1",
           "PYTHONPATH": str(ROOT / "tools/ci/kfm_no_network")}
    result = subprocess.run(
        [sys.executable, "-B", "-c", _published_alias_guard()],
        cwd=tmp_path, env=env, capture_output=True, text=True, check=False, timeout=10,
    )
    assert (result.returncode == 0) is (mutation is None), result.stderr
    if mutation is None:
        assert "WORKFLOW_HOLD:" in result.stdout
        assert "explicit exit-3 HOLD" in result.stdout
    else:
        expected = {"auditor": "drifted from its explicit HOLD",
                    "alias": "published current aliases have appeared",
                    "rollback-payload": "rollback data material has appeared"}[mutation]
        assert expected in result.stderr
    assert before == {str(p.relative_to(tmp_path)): p.read_bytes()
                      for p in tmp_path.rglob("*") if p.is_file()}
