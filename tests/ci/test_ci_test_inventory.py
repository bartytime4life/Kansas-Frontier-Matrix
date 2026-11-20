"""The CI test inventory resolves what workflow steps really execute."""
from __future__ import annotations

import importlib.util
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("ci_test_inventory", ROOT / "tools/ci/ci_test_inventory.py")
assert SPEC is not None and SPEC.loader is not None
inventory_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory_module)

MODULES = [
    "tests/a/test_direct.py",
    "tests/a/test_node.py",
    "tests/b/test_dir_one.py",
    "tests/b/deep/test_dir_two.py",
    "tests/c/test_pattern_hit.py",
    "tests/c/test_pattern_miss.py",
    "tests/d/test_dotted.py",
    "tests/e/test_glob_one.py",
    "tests/f/test_script.py",
    "tests/g/test_make.py",
    "tests/h/test_submake.py",
    "tests/i/test_collect_only.py",
    "tests/j/test_paths_filter_only.py",
    "tests/k/test_comment_only.py",
    "tests/l/test_orphan.py",
]


def _repo(tmp_path: Path, workflow: str, makefile: str = "") -> Path:
    for module in MODULES:
        path = tmp_path / module
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("def test_x():\n    assert 1 + 1 == 2\n", encoding="utf-8")
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "ci.yml").write_text(textwrap.dedent(workflow), encoding="utf-8")
    (tmp_path / "Makefile").write_text(makefile, encoding="utf-8")
    return tmp_path


WORKFLOW = """\
on:
  pull_request:
    paths:
      - "tests/j/test_paths_filter_only.py"
jobs:
  test:
    steps:
      - run: python -m pytest -q tests/a/test_direct.py tests/a/test_node.py::test_x
      - run: |
          python -m pytest -q \\
            tests/b
      - run: python -m unittest discover --start-directory tests/c --pattern 'test_pattern_hit.py'
      - run: python -m unittest -v tests.d.test_dotted
      - run: python -m pytest -q tests/e/test_glob_*.py
      - run: python tests/f/test_script.py --verbose
      - run: make lane
      - run: python -m pytest --collect-only -q tests/i
      - run: echo done  # tests/k/test_comment_only.py
"""
MAKEFILE = (
    "lane:\n\tpython -m pytest -q tests/g/test_make.py\n\t$(MAKE) sub\n"
    "sub:\n\tpython -m pytest -q tests/h/test_submake.py\n"
    "unused:\n\tpython -m pytest -q tests/l/test_orphan.py\n"
)


def test_inventory_resolves_each_invocation_form(tmp_path: Path) -> None:
    result = inventory_module.inventory(_repo(tmp_path, WORKFLOW, MAKEFILE))

    assert result["test_modules"] == len(MODULES)
    assert result["unexecuted"] == [
        "tests/c/test_pattern_miss.py",
        "tests/i/test_collect_only.py",
        "tests/j/test_paths_filter_only.py",
        "tests/k/test_comment_only.py",
        "tests/l/test_orphan.py",
    ]


def test_unexecuted_listing_is_one_path_per_line(tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
                                                 capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(inventory_module, "ROOT", _repo(tmp_path, WORKFLOW, MAKEFILE))

    assert inventory_module.main(["--unexecuted"]) == 0
    assert capsys.readouterr().out.splitlines()[0] == "tests/c/test_pattern_miss.py"


def test_unparseable_workflow_is_skipped_not_fatal(tmp_path: Path) -> None:
    root = _repo(tmp_path, "jobs: [unclosed\n")

    assert len(inventory_module.inventory(root)["unexecuted"]) == len(MODULES)


def test_repository_inventory_runs(tmp_path: Path) -> None:
    result = inventory_module.inventory(ROOT)

    assert result["authority"] == "SCHEDULING_AID_ONLY"
    assert result["executed"] + len(result["unexecuted"]) == result["test_modules"]
    assert all(path.startswith("tests/") for path in result["unexecuted"])
