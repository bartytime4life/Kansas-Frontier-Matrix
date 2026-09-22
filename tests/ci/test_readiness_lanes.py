from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import stat

import pytest

ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = ROOT / "tools" / "readiness" / "run_lane.py"
SPEC = importlib.util.spec_from_file_location("kfm_readiness_lanes", TOOL_PATH)
assert SPEC and SPEC.loader
TOOL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOOL)


def test_registry_has_one_bounded_implementation_and_three_named_holds() -> None:
    registry = TOOL.load_registry()
    assert tuple(item["id"] for item in registry["lanes"]) == TOOL.LANE_IDS
    statuses = {item["id"]: item["status"] for item in registry["lanes"]}
    assert statuses == {
        "policy": "IMPLEMENTED",
        "fixtures": "HOLD",
        "proof-slice": "HOLD",
        "catalog": "HOLD",
    }


@pytest.mark.parametrize("lane_id", ["fixtures", "proof-slice", "catalog"])
def test_unimplemented_lanes_fail_closed_with_named_hold(lane_id: str) -> None:
    lane = TOOL.lane_by_id(TOOL.load_registry(), lane_id)
    code, payload = TOOL.run_lane(lane)
    assert code == 3
    assert payload["status"] == "HOLD"
    assert payload["reason"] == lane["hold_reason"]
    assert all(value is False for value in payload["effects"].values())


def test_policy_runner_executes_only_registered_pair(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    arguments_path = tmp_path / "arguments.json"
    fake_opa = tmp_path / "opa"
    fake_opa.write_text(
        "#!/usr/bin/env python3\n"
        "import json, os, sys\n"
        "from pathlib import Path\n"
        "Path(os.environ['OPA_ARGUMENTS_PATH']).write_text(json.dumps(sys.argv[1:]))\n",
        encoding="utf-8",
    )
    fake_opa.chmod(fake_opa.stat().st_mode | stat.S_IXUSR)
    monkeypatch.setenv("OPA_BIN", str(fake_opa))
    monkeypatch.setenv("OPA_ARGUMENTS_PATH", str(arguments_path))

    lane = TOOL.lane_by_id(TOOL.load_registry(), "policy")
    code, payload = TOOL.run_lane(lane)
    assert code == 0
    assert payload["status"] == "PASS"
    assert json.loads(arguments_path.read_text()) == lane["command"][1:]
    assert all(value is False for value in payload["effects"].values())


def test_policy_registry_never_uses_repository_wide_policy_directory() -> None:
    lane = TOOL.lane_by_id(TOOL.load_registry(), "policy")
    command = " ".join(lane["command"])
    assert "policy/rego/release_gate_v1.rego" in command
    assert "policy/rego/release_gate_v1_test.rego" in command
    assert "opa test policy/ -v" not in command
