"""Scaffold inventory classification and ratchet behavior on synthetic inputs."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "kfm_scaffold_inventory", ROOT / "tools" / "qa" / "scaffold_inventory.py")
assert SPEC and SPEC.loader
TOOL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOOL)


@pytest.mark.parametrize(("path", "body", "expected"), [
    ("pipelines/x/empty.py", b"", ["EMPTY_FILE"]),
    ("packages/x/__init__.py", b"", []),
    ("data/.gitkeep", b"", []),
    ("pipelines/x/ingest.py", b"# x :: ingest - greenfield placeholder\n",
     ["PLACEHOLDER_MARKER", "STUB_MODULE"]),
    ("tools/x/check.py", b'"""PROPOSED placeholder generated from docs."""\n',
     ["PLACEHOLDER_MARKER", "STUB_MODULE"]),
    ("tools/x/stub.py", b"# Greenfield validator stub: x\ndef main():\n    raise SystemExit(1)\n",
     ["PLACEHOLDER_MARKER"]),
    ("policy/x.rego", b"package x\n\n# Status: PROPOSED scaffold.\ndefault allow := false\n",
     ["PLACEHOLDER_MARKER"]),
    ("tools/x/real.py", b'"""Real module."""\nVALUE = 1\n', []),
    ("tests/x/conftest.py", b'"""Fixtures."""\n', []),
    ("tests/x/test_smoke.py", b"def test_smoke():\n    assert True\n", ["VACUOUS_TEST"]),
    ("tests/x/test_real.py", b"def test_real():\n    assert 1 + 1 == 2\n", []),
    ("scripts/regen.sh", b"#!/usr/bin/env bash\nset -euo pipefail\necho 'TODO'\n",
     ["TODO_ECHO_SCRIPT"]),
    ("scripts/real.sh", b"#!/usr/bin/env bash\nset -euo pipefail\necho 'TODO'\nexit 3\n", []),
    ("connectors/x/src/x/descriptor.yaml", b"name: x\nrole: TBD\n", ["UNRESOLVED_DESCRIPTOR"]),
    ("connectors/x/src/x/descriptor.yaml", b"name: x\nrole: primary\n", []),
    ("docs/x/README.md", b"greenfield placeholder\n", []),
])
def test_classify(path: str, body: bytes, expected: list[str]) -> None:
    assert TOOL.classify(path, body) == expected


def test_marker_below_header_is_a_guard_not_a_placeholder() -> None:
    body = b"name: guard\n" + b"x: 1\n" * 10 + b"expected: '# greenfield placeholder'\n"
    assert TOOL.classify(".github/workflows/guard.yml", body) == []


def test_compare_reports_new_and_resolved() -> None:
    baseline = [{"path": "a.py", "kind": "STUB_MODULE"}, {"path": "b.py", "kind": "EMPTY_FILE"}]
    findings = [{"path": "a.py", "kind": "STUB_MODULE"}, {"path": "c.py", "kind": "STUB_MODULE"}]
    assert TOOL.compare(findings, baseline) == {
        "new": [{"path": "c.py", "kind": "STUB_MODULE"}],
        "resolved": [{"path": "b.py", "kind": "EMPTY_FILE"}],
    }


def test_inventory_reads_explicit_paths(tmp_path: Path) -> None:
    (tmp_path / "pipelines").mkdir()
    (tmp_path / "pipelines" / "stub.py").write_text("# greenfield placeholder\n")
    (tmp_path / "pipelines" / "real.py").write_text("VALUE = 1\n")
    findings = TOOL.inventory(tmp_path, ["pipelines/stub.py", "pipelines/real.py",
                                         "pipelines/missing.py"])
    assert findings == [{"path": "pipelines/stub.py", "kind": "PLACEHOLDER_MARKER"},
                        {"path": "pipelines/stub.py", "kind": "STUB_MODULE"}]


def test_repository_matches_reviewed_baseline() -> None:
    completed = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=ROOT,
                               capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        pytest.skip("scaffold inventory reads tracked files and needs a git checkout")
    delta = TOOL.compare(TOOL.inventory(), TOOL.load_baseline())
    assert delta == {"new": [], "resolved": []}, (
        "Scaffold baseline drifted: implement or fail-close new scaffolding, and run "
        "`python tools/qa/scaffold_inventory.py --write-baseline` after resolving entries.")
