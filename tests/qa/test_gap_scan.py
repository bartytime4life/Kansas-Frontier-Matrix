"""Gap-scan classification and ratchet behavior on synthetic git trees."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("kfm_gap_scan", ROOT / "tools" / "qa" / "gap_scan.py")
assert SPEC and SPEC.loader
TOOL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOOL)


def _repo(tmp_path: Path, files: dict[str, str]) -> Path:
    for rel, body in files.items():
        target = tmp_path / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    return tmp_path


def _kinds(findings):
    return sorted((f["kind"], f["path"]) for f in findings)


@pytest.mark.parametrize(("path", "negative"), [
    ("fixtures/x/invalid/a.json", True),
    ("tests/diff/fixtures/malformed/x.json", True),
    ("fixtures/release/gate/error__malformed_json.json", True),
    ("fixtures/x/valid/range_polygon.geojson", False),
    ("fixtures/x/valid/invalidation_window.json", False),
])
def test_negative_fixture_detection(path: str, negative: bool) -> None:
    assert TOOL.is_negative_fixture(path) is negative


def test_parse_errors_skip_negative_fixtures(tmp_path: Path) -> None:
    root = _repo(tmp_path, {
        "fixtures/a/valid/x.geojson": "# PROPOSED placeholder\n",
        "fixtures/a/invalid/y.json": "{not json",
        "configs/ok.yaml": "a: 1\n",
        "configs/settings.toml": "a = \n",
    })
    found = TOOL.scan_parse_errors(root, TOOL.tracked_files(root))
    assert _kinds(found) == [("STRUCTURED_PARSE_ERROR", "configs/settings.toml"),
                             ("STRUCTURED_PARSE_ERROR", "fixtures/a/valid/x.geojson")]


def test_deleted_tracked_file_is_ignored(tmp_path: Path) -> None:
    root = _repo(tmp_path, {"configs/gone.json": "{", "configs/ok.json": "{}"})
    (root / "configs/gone.json").unlink()
    assert TOOL.tracked_files(root) == ["configs/ok.json"]


def test_test_package_shadow_requires_imported_root(tmp_path: Path) -> None:
    root = _repo(tmp_path, {
        "pipelines/domains/x.py": "VALUE = 1\n",
        "tests/pipelines/__init__.py": "",
        "tests/pipelines/test_x.py": "from pipelines.domains import x\n",
        "tools/run.py": "from pipelines.domains import x\n",
        "schemas/a.json": "{}",
        "tests/schemas/__init__.py": "",
    })
    found = TOOL.scan_test_shadows(root, TOOL.tracked_files(root))
    assert _kinds(found) == [("TEST_PACKAGE_SHADOW", "tests/pipelines/__init__.py")]


def test_links_resolve_files_dirs_and_angle_targets(tmp_path: Path) -> None:
    root = _repo(tmp_path, {
        "docs/a.md": "\n".join([
            "[ok](./b.md) [dir](../tools/) [web](https://example.invalid) [frag](#x)",
            "[angle](<./c (1).md>) [missing](./gone.md#x)",
            "```", "[fenced](./also-gone.md)", "```",
        ]),
        "docs/b.md": "b",
        "docs/c (1).md": "c",
        "tools/x.py": "VALUE = 1\n",
        "docs/archive/old.md": "[stale](./nowhere.md)",
    })
    found = TOOL.scan_links(root, TOOL.tracked_files(root))
    assert [(f["path"], f["detail"]) for f in found] == [("docs/a.md:2", "docs/gone.md")]


def test_placeholders_only_outside_scaffold_surfaces(tmp_path: Path) -> None:
    root = _repo(tmp_path, {
        "infra/compose/docker-compose.yml": "# PROPOSED placeholder\nservices: {}\n",
        "tools/x.py": "# greenfield placeholder\n",
        "infra/README.md": "PROPOSED placeholder\n",
        "data/receipts/r.json": '{"note": "PROPOSED placeholder"}',
    })
    found = TOOL.scan_placeholders(root, TOOL.tracked_files(root))
    assert _kinds(found) == [("UNRATCHETED_PLACEHOLDER", "infra/compose/docker-compose.yml")]


def _summary(**counts):
    base = {kind: 0 for kind in TOOL.INVARIANT_KINDS + TOOL.CENSUS_KINDS}
    base.update(counts)
    return {"counts": base}


def test_evaluate_invariants_fail_and_census_ratchets() -> None:
    baseline = {"BROKEN_LOCAL_LINK": 10, "UNRATCHETED_PLACEHOLDER": 2}
    assert TOOL.evaluate(_summary(BROKEN_LOCAL_LINK=10, UNRATCHETED_PLACEHOLDER=2), baseline)[0] == 0
    assert TOOL.evaluate(_summary(STRUCTURED_PARSE_ERROR=1), baseline)[0] == 1
    assert TOOL.evaluate(_summary(TEST_PACKAGE_SHADOW=1), baseline)[0] == 1
    assert TOOL.evaluate(_summary(BROKEN_LOCAL_LINK=11), baseline)[0] == 1
    status, messages = TOOL.evaluate(_summary(BROKEN_LOCAL_LINK=3), baseline)
    assert status == 0 and any("--write-baseline" in m for m in messages)


def test_repository_passes_its_own_check() -> None:
    summary = TOOL.summarize(TOOL.scan(ROOT))
    status, messages = TOOL.evaluate(summary, TOOL.load_baseline())
    assert status == 0, messages
