"""Exercise the workflow's pinned rehearsal boundary with disposable checkouts."""

from __future__ import annotations

import ast
import importlib.util
import os
from pathlib import Path
import py_compile
import shutil
import subprocess
import sys

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/rollback-drill.yml"
HELPER = Path("tools/release/rollback_apply.py")
TESTS = (
    Path("tests/release/test_synthetic_rollback_rehearsal.py"),
    Path("tests/domains/hazards/test_synthetic_rollback_rehearsal.py"),
)
FIXTURE = Path("fixtures/domains/hazards/synthetic_rollback_rehearsal")


def boundary_command() -> str:
    """Use the actual shell invocation, integrity gate, and rehearsal bootstrap."""
    workflow = yaml.safe_load(WORKFLOW.read_text(encoding="utf-8"))
    step = next(
        step["run"]
        for step in workflow["jobs"]["simulate-rollback"]["steps"]
        if step["name"] == "Confirm rollback simulation remains an explicit hold"
    )
    prefix, program = step.split("<<'PY'\n", 1)
    program = program.rsplit("\nPY", 1)[0]
    body = ast.parse(program).body

    def assignment_index(name: str) -> int:
        return next(
            index
            for index, node in enumerate(body)
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)
        )

    path_names = {
        "rollback_apply_path",
        "rehearsal_test_path",
        "hazards_rehearsal_test_path",
        "hazards_rehearsal_fixture_root",
    }
    setup = [
        node
        for node in body
        if isinstance(node, (ast.Import, ast.ImportFrom))
        or (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id in path_names
                for target in node.targets
            )
        )
    ]
    # Exclude unrelated validator/schema/authority inventory checks. Execute the
    # workflow's real security gate and loader, never a test copy of their logic.
    nodes = (
        setup
        + body[assignment_index("expected_rehearsal_digests"):assignment_index("generic_validator")]
        + body[assignment_index("rehearsal_bootstrap"):assignment_index("agriculture_schema")]
    )
    source = "\n".join(ast.unparse(node) for node in nodes)
    return prefix + "<<'PY'\n" + source + "\nprint(rehearsal_output)\nPY\n"


@pytest.fixture
def checkout(tmp_path: Path) -> Path:
    root = tmp_path / "checkout"
    for path in (HELPER, *TESTS):
        destination = root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / path, destination)
    shutil.copytree(ROOT / FIXTURE, root / FIXTURE)
    return root


def run_boundary(checkout: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PATH"] = str(Path(sys.executable).parent) + os.pathsep + env.get("PATH", "")
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(
        ["bash", "-c", boundary_command()],
        cwd=checkout,
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )


def assert_real_rehearsal(result: subprocess.CompletedProcess[str]) -> None:
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Ran 14 tests" in result.stdout
    assert "OK" in result.stdout


def test_regular_checkout_runs_all_fourteen_cases(checkout: Path) -> None:
    assert_real_rehearsal(run_boundary(checkout))


@pytest.mark.parametrize("test_path", TESTS, ids=["generic", "hazards"])
@pytest.mark.parametrize("parent_link", [False, True], ids=["file", "parent-directory"])
def test_redirected_test_cannot_load_an_unpinned_helper(
    checkout: Path, test_path: Path, parent_link: bool
) -> None:
    alternate = checkout / "alternate"
    destination = alternate / test_path
    destination.parent.mkdir(parents=True)
    shutil.copyfile(checkout / test_path, destination)
    helper = alternate / HELPER
    helper.parent.mkdir(parents=True)
    sentinel = checkout / "unpinned-helper-executed"
    helper.write_text(
        (checkout / HELPER).read_text(encoding="utf-8")
        + f"\nfrom pathlib import Path as _Sentinel\n_Sentinel({str(sentinel)!r}).touch()\n",
        encoding="utf-8",
    )
    shutil.copytree(checkout / FIXTURE, alternate / FIXTURE)
    link = checkout / (test_path.parent if parent_link else test_path)
    target = destination.parent if parent_link else destination
    if parent_link:
        shutil.rmtree(link)
    else:
        link.unlink()
    link.symlink_to(os.path.relpath(target, link.parent), target_is_directory=parent_link)

    result = run_boundary(checkout)
    assert result.returncode != 0
    assert "rehearsal input path is redirected" in result.stderr
    assert not sentinel.exists()


@pytest.mark.parametrize("parent_link", [False, True], ids=["file", "parent-directory"])
def test_redirected_helper_is_denied(checkout: Path, parent_link: bool) -> None:
    alternate = checkout / "alternate/rollback_apply.py"
    alternate.parent.mkdir()
    shutil.copyfile(checkout / HELPER, alternate)
    link = checkout / (HELPER.parent if parent_link else HELPER)
    target = alternate.parent if parent_link else alternate
    if parent_link:
        shutil.rmtree(link)
    else:
        link.unlink()
    link.symlink_to(os.path.relpath(target, link.parent), target_is_directory=parent_link)
    result = run_boundary(checkout)
    assert result.returncode != 0
    assert "rehearsal input path is redirected" in result.stderr


@pytest.mark.parametrize("path", [HELPER, TESTS[0], FIXTURE / "workspace/scenario.json"])
def test_reviewed_bytes_cannot_drift(checkout: Path, path: Path) -> None:
    with (checkout / path).open("ab") as stream:
        stream.write(b"\n")
    result = run_boundary(checkout)
    assert result.returncode != 0
    assert "reviewed synthetic rollback helper" in result.stderr


@pytest.mark.parametrize("package", [False, True], ids=["module", "package"])
def test_checkout_hashlib_cannot_run_or_hide_drift(checkout: Path, package: bool) -> None:
    shadow = checkout / ("hashlib/__init__.py" if package else "hashlib.py")
    shadow.parent.mkdir(exist_ok=True)
    sentinel = checkout / "shadow-hashlib-executed"
    shadow.write_text(
        f"from pathlib import Path\nPath({str(sentinel)!r}).touch()\n"
        "raise RuntimeError('checkout hashlib must not load')\n",
        encoding="utf-8",
    )
    with (checkout / HELPER).open("ab") as stream:
        stream.write(b"\n")
    assert run_boundary(checkout).returncode != 0
    assert not sentinel.exists()


def test_unlisted_fixture_directory_symlink_is_denied(checkout: Path) -> None:
    alternate = checkout / "extra-fixture"
    alternate.mkdir()
    (alternate / "extra.json").write_text("{}", encoding="utf-8")
    (checkout / FIXTURE / "workspace/extra").symlink_to(alternate, target_is_directory=True)
    result = run_boundary(checkout)
    assert result.returncode != 0
    assert "rehearsal input path is redirected" in result.stderr


@pytest.mark.parametrize(
    "alias",
    [
        "tests.py",
        "tests/__init__.py",
        "tests/release.py",
        "tests/release/__init__.py",
        "tests/domains.py",
        "tests/domains/__init__.py",
        "tests/domains/hazards/__init__.py",
    ],
)
def test_unpinned_test_import_aliases_are_not_executed(checkout: Path, alias: str) -> None:
    sentinel = checkout / "import-alias-executed"
    path = checkout / alias
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"from pathlib import Path\nPath({str(sentinel)!r}).touch()\n"
        "raise RuntimeError('unpinned test import')\n",
        encoding="utf-8",
    )
    assert_real_rehearsal(run_boundary(checkout))
    assert not sentinel.exists()


def test_committed_helper_bytecode_cannot_replace_pinned_source(checkout: Path) -> None:
    sentinel = checkout / "cached-helper-executed"
    source = checkout / "cache-input.py"
    source.write_text(
        f"from pathlib import Path\nPath({str(sentinel)!r}).touch()\n"
        "raise RuntimeError('unpinned helper bytecode')\n",
        encoding="utf-8",
    )
    py_compile.compile(
        str(source),
        cfile=importlib.util.cache_from_source(str(checkout / HELPER)),
        doraise=True,
        invalidation_mode=py_compile.PycInvalidationMode.UNCHECKED_HASH,
    )
    assert_real_rehearsal(run_boundary(checkout))
    assert not sentinel.exists()
