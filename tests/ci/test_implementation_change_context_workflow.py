"""Source contract for historical receipts; not CI, review, or release authority.

Run with pytest. The production receipt validator still verifies ancestor status
and artifact hashes; this test only guards the workflow's actual commands.
"""

from copy import deepcopy
from pathlib import Path
import shlex

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ".github/workflows/implementation-change-context.yml"
TEST = "tests/ci/test_implementation_change_context_workflow.py"
RECEIPTS = "data/receipts/generated/"
CURRENT = RECEIPTS + "genrec-implementation-change-context-history-20260911.json"
HISTORICAL = (
    (RECEIPTS + "genrec-implementation-change-context-20260806.json",
     "8b3b45fddc9c2bd9f49c26822cd6554d04eb5c66"),
    (RECEIPTS + "genrec-governance-workflow-security-readme-current-state-20260831.json",
     "f520c20c06cdbb5de000877979070023f688abb0"),
)
VALIDATOR = "tools/validators/validate_generated_receipt.py"
INSTALL = "Install declared test dependencies"
CONTRACT = "Test historical receipt workflow contract"
FOCUSED = "Run focused deterministic tests"
POLARITY = "Run exact fixture polarity"
INTEGRITY = "Verify generated authoring receipt integrity"


def _commands(value: str) -> list[list[str]]:
    """Read executable lines, not commented command-like text."""
    lines = value.replace("\\\n", " ").splitlines()
    return [tokens for line in lines if (tokens := shlex.split(line, comments=True))]


def _workflow() -> dict:
    return yaml.safe_load((ROOT / WORKFLOW).read_text(encoding="utf-8"))


def _step(workflow: dict, name: str) -> dict:
    matches = [s for s in workflow["jobs"]["validate"]["steps"] if s["name"] == name]
    assert len(matches) == 1, name
    return matches[0]


def _assert_contract(workflow: dict) -> None:
    assert workflow["name"] == "implementation-change-context"
    assert set(workflow["on"]) == {"pull_request", "push", "workflow_dispatch"}
    assert workflow["on"]["push"]["branches"] == ["main"]
    required_paths = {WORKFLOW, TEST, CURRENT, *(p for p, _ in HISTORICAL)}
    for event in ("pull_request", "push"):
        paths = workflow["on"][event]["paths"]
        assert required_paths.issubset(paths)
        assert all(not p.startswith("!") for p in paths)
    assert workflow["permissions"] == {"contents": "read"}
    assert workflow["env"]["KFM_NO_NETWORK"] == "1"
    assert set(workflow["jobs"]) == {"validate"}
    job = workflow["jobs"]["validate"]
    assert job["name"] == "validate-implementation-change-context"
    assert job["runs-on"] == "ubuntu-latest"
    assert job["timeout-minutes"] == 10
    for key in ("if", "continue-on-error", "permissions", "env"):
        assert key not in job
    steps = job["steps"]
    assert steps[0]["uses"] == "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1"
    assert steps[0]["with"] == {"persist-credentials": False, "fetch-depth": 0}
    assert steps[1]["uses"] == "actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97"
    assert steps[1]["with"]["python-version"] == "3.11"
    for step in steps:
        assert "continue-on-error" not in step and "env" not in step
        if step["name"] != "Record trust boundary":
            assert "if" not in step
    commands = {
        INSTALL: [["python", "tools/ci/install_python_ci.py", "project-test"]],
        CONTRACT: [["python", "-m", "pytest", "-q", TEST]],
        FOCUSED: [["python", "-m", "pytest", "-q",
                   "tests/validators/governance/test_implementation_change_context.py"]],
        POLARITY: [["python", "tools/validators/governance/validate_implementation_change_context.py",
                    "--cases"]],
        INTEGRITY: [["set", "-euo", "pipefail"]] + [
            ["python", VALIDATOR, path, "--repo-root", ".", "--artifact-git-ref", ref]
            for path, ref in HISTORICAL
        ] + [["python", VALIDATOR, CURRENT, "--repo-root", "."]],
    }
    positions = []
    for name, expected in commands.items():
        step = _step(workflow, name)
        assert _commands(step["run"]) == expected, name
        assert step.get("shell", "bash") == "bash"
        assert "working-directory" not in step
        positions.append(steps.index(step))
    assert positions == sorted(positions)


def test_workflow_preserves_historical_and_current_integrity() -> None:
    _assert_contract(_workflow())


@pytest.mark.parametrize("index", range(2))
@pytest.mark.parametrize("replacement", (None, "main", "f520c20", "0" * 40))
def test_missing_or_unreviewed_historical_pin_is_rejected(index, replacement) -> None:
    workflow = _workflow()
    step = _step(workflow, INTEGRITY)
    ref = HISTORICAL[index][1]
    step["run"] = step["run"].replace(
        "--artifact-git-ref " + ref,
        "" if replacement is None else "--artifact-git-ref " + replacement,
    )
    with pytest.raises(AssertionError):
        _assert_contract(workflow)


@pytest.mark.parametrize("name", (CONTRACT, FOCUSED, POLARITY, INTEGRITY))
@pytest.mark.parametrize("mutation", ("comment", "skip", "continue", "mask-exit"))
def test_nonexecuting_or_nonblocking_gate_is_rejected(name, mutation) -> None:
    workflow = _workflow()
    step = _step(workflow, name)
    if mutation == "comment":
        step["run"] = "\n".join("# " + line for line in step["run"].splitlines())
    elif mutation == "skip":
        step["if"] = "false"
    elif mutation == "continue":
        step["continue-on-error"] = True
    else:
        step["run"] += " || true"
    with pytest.raises(AssertionError):
        _assert_contract(workflow)


@pytest.mark.parametrize("event", ("pull_request", "push"))
@pytest.mark.parametrize("path", (TEST, CURRENT))
def test_new_inputs_trigger_the_workflow(event, path) -> None:
    workflow = _workflow()
    workflow["on"][event]["paths"].remove(path)
    with pytest.raises(AssertionError):
        _assert_contract(workflow)


@pytest.mark.parametrize("mutation", ("shallow", "credentials", "write", "old-current", "omit-current"))
def test_history_fetch_and_current_integrity_cannot_be_weakened(mutation) -> None:
    workflow = deepcopy(_workflow())
    checkout = workflow["jobs"]["validate"]["steps"][0]
    if mutation == "shallow":
        checkout["with"]["fetch-depth"] = 1
    elif mutation == "credentials":
        checkout["with"]["persist-credentials"] = True
    elif mutation == "write":
        workflow["permissions"]["contents"] = "write"
    else:
        step = _step(workflow, INTEGRITY)
        commands = _commands(step["run"])
        if mutation == "old-current":
            commands[-1] += ["--artifact-git-ref", HISTORICAL[1][1]]
        else:
            commands.pop()
        step["run"] = "\n".join(shlex.join(command) for command in commands)
    with pytest.raises(AssertionError):
        _assert_contract(workflow)
