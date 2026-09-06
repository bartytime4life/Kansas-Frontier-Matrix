"""Source-level temporal workflow regression checks; not hosted-run authority."""

from copy import deepcopy
from fnmatch import fnmatchcase
from pathlib import Path
import re

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/temporal-view-state-validation.yml"
PYTHON_JOB = "validate-temporal-view-state"
EXPLORER_JOB = "explorer-temporal-conformance"
REQUIRED_INPUTS = (
    ".github/workflows/temporal-view-state-validation.yml",
    "tests/ci/test_temporal_view_state_workflow.py",
    "tests/validators/test_validate_temporal_view_state.py",
    "tests/validators/test_validate_temporal_view_state_expectations.py",
    "tests/schemas/test_common_contracts.py",
    "apps/explorer-web/src/features/temporal/index.ts",
    "apps/explorer-web/src/site/workspace-context.ts",
    "apps/explorer-web/tests/temporal-kernel.test.ts",
    "apps/explorer-web/tests/temporal-boundary-regression.test.ts",
    "apps/explorer-web/tests/workspace-context.test.ts",
    "apps/explorer-web/package.json",
    "package.json",
    "pnpm-workspace.yaml",
    "pnpm-lock.yaml",
)
PYTHON_COMMANDS = (
    "python tools/ci/install_python_ci.py project-test",
    "python -m pytest -q tests/ci/test_temporal_view_state_workflow.py",
    "set -euo pipefail python -m unittest discover --start-directory tests/validators "
    "--pattern 'test_validate_temporal_view_state*.py' --verbose",
    "set -euo pipefail python tools/validators/validate_temporal_view_state.py --fixtures",
    "set -euo pipefail python -m pytest -q tests/schemas/test_common_contracts.py -k temporal_view_state",
)
EXPLORER_COMMANDS = (
    "set -euo pipefail node --version corepack --version corepack enable pnpm --version",
    "pnpm install --frozen-lockfile --filter explorer-web...",
    "pnpm --filter explorer-web build",
    "set -euo pipefail pnpm exec vitest run tests/temporal-kernel.test.ts "
    "tests/temporal-boundary-regression.test.ts tests/workspace-context.test.ts",
)


def _normalized(command: str) -> str:
    return " ".join(command.replace("\\\n", " ").split())


def _assert_contract(workflow: dict) -> None:
    assert workflow["name"] == "temporal-view-state-validation"
    assert set(workflow["on"]) == {"pull_request", "push", "workflow_dispatch"}
    assert workflow["on"]["push"]["branches"] == ["main"]
    for event in ("pull_request", "push"):
        patterns = workflow["on"][event]["paths"]
        assert patterns and all(not item.startswith("!") for item in patterns)
        for path in REQUIRED_INPUTS:
            assert any(fnmatchcase(path, pattern) for pattern in patterns), path
    assert workflow["permissions"] == {"contents": "read"}
    assert workflow["env"]["KFM_NO_NETWORK"] == "1"
    assert workflow["env"]["COREPACK_ENABLE_STRICT"] == "1"
    assert "COREPACK_INTEGRITY_KEYS" not in workflow["env"]
    assert set(workflow["jobs"]) == {PYTHON_JOB, EXPLORER_JOB}
    for job_id, required in ((PYTHON_JOB, PYTHON_COMMANDS), (EXPLORER_JOB, EXPLORER_COMMANDS)):
        job = workflow["jobs"][job_id]
        assert job["name"] == job_id
        assert job["runs-on"] == "ubuntu-latest"
        assert job["timeout-minutes"] == 10
        assert "if" not in job and "continue-on-error" not in job
        assert "permissions" not in job and "env" not in job
        steps = job["steps"]
        for step in steps:
            assert "continue-on-error" not in step and "env" not in step
            if "uses" in step:
                assert re.fullmatch(r"actions/[a-z-]+@[0-9a-f]{40}", step["uses"])
            if step.get("uses", "").startswith("actions/checkout@"):
                assert step["with"]["persist-credentials"] is False
        commands = [_normalized(step.get("run", "")) for step in steps]
        positions = []
        for command in required:
            assert commands.count(command) == 1, command
            position = commands.index(command)
            assert "if" not in steps[position]
            assert steps[position]["shell"] == "bash"
            positions.append(position)
        assert positions == sorted(positions)
    explorer_steps = workflow["jobs"][EXPLORER_JOB]["steps"]
    setup = next(step for step in explorer_steps if step.get("uses", "").startswith("actions/setup-node@"))
    assert setup["with"]["node-version"] == "22.23.2"
    assert setup["with"]["package-manager-cache"] is False
    test_step = next(step for step in explorer_steps if _normalized(step.get("run", "")) == EXPLORER_COMMANDS[-1])
    assert test_step["working-directory"] == "apps/explorer-web"


def _workflow() -> dict:
    return yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))


def test_committed_temporal_workflow_preserves_coverage_and_safety() -> None:
    _assert_contract(_workflow())


@pytest.mark.parametrize("event", ("pull_request", "push"))
@pytest.mark.parametrize("path", (
    "tests/ci/test_temporal_view_state_workflow.py",
    "tests/validators/test_validate_temporal_view_state_expectations.py",
    "apps/explorer-web/tests/workspace-context.test.ts",
    "apps/explorer-web/tests/temporal-boundary-regression.test.ts",
))
def test_omitted_regression_trigger_is_rejected(event: str, path: str) -> None:
    workflow = _workflow()
    patterns = workflow["on"][event]["paths"]
    workflow["on"][event]["paths"] = [p for p in patterns if not fnmatchcase(path, p)]
    with pytest.raises(AssertionError):
        _assert_contract(workflow)


@pytest.mark.parametrize("job_id,command", (
    (PYTHON_JOB, PYTHON_COMMANDS[2]),
    (PYTHON_JOB, PYTHON_COMMANDS[4]),
    (EXPLORER_JOB, EXPLORER_COMMANDS[2]),
    (EXPLORER_JOB, EXPLORER_COMMANDS[3]),
))
@pytest.mark.parametrize("mutation", ("comment", "skip", "continue"))
def test_nonexecuting_or_nonblocking_gates_are_rejected(job_id: str, command: str, mutation: str) -> None:
    workflow = _workflow()
    step = next(step for step in workflow["jobs"][job_id]["steps"] if _normalized(step.get("run", "")) == command)
    if mutation == "comment":
        step["run"] = "\n".join("# " + line for line in step["run"].splitlines())
    elif mutation == "skip":
        step["if"] = "false"
    else:
        step["continue-on-error"] = True
    with pytest.raises(AssertionError):
        _assert_contract(workflow)


@pytest.mark.parametrize("mutation", ("old-node", "unfrozen", "write", "integrity-bypass", "persist-credentials"))
def test_bootstrap_and_permission_regressions_are_rejected(mutation: str) -> None:
    workflow = deepcopy(_workflow())
    steps = workflow["jobs"][EXPLORER_JOB]["steps"]
    if mutation == "old-node":
        setup = next(step for step in steps if step.get("uses", "").startswith("actions/setup-node@"))
        setup["with"]["node-version"] = "22.13.1"
    elif mutation == "unfrozen":
        install = next(step for step in steps if step.get("run", "").startswith("pnpm install"))
        install["run"] = "pnpm install --filter explorer-web..."
    elif mutation == "write":
        workflow["permissions"]["contents"] = "write"
    elif mutation == "integrity-bypass":
        workflow["env"]["COREPACK_INTEGRITY_KEYS"] = "0"
    else:
        steps[0]["with"]["persist-credentials"] = True
    with pytest.raises(AssertionError):
        _assert_contract(workflow)
