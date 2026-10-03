"""The mirror comparison must bind source bytes to its reported commit."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("kfm_site_mirror", ROOT / "tools/qa/site_mirror.py")
assert SPEC and SPEC.loader
TOOL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOOL)


def _git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def _repos(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[Path, Path, str]:
    source = tmp_path / "source"
    repo = tmp_path / "repo"
    destination = repo / "apps/site/source"
    (source / "app").mkdir(parents=True)
    (destination / "app").mkdir(parents=True)
    (source / "app/page.tsx").write_text("source A\n", encoding="utf-8")
    (destination / "app/page.tsx").write_text("source A\n", encoding="utf-8")
    for root in (source, repo):
        _git(root, "init", "-q")
        _git(root, "add", ".")
        _git(root, "-c", "user.name=KFM test", "-c", "user.email=kfm-test@example.invalid",
             "commit", "-qm", "fixture")
    monkeypatch.setattr(TOOL, "ROOT", repo)
    monkeypatch.setattr(TOOL, "DESTINATION", destination)
    return source, destination, _git(source, "rev-parse", "HEAD")


def _receipt(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, site_commit: str) -> None:
    digest = TOOL.sha(b"source A\n").removeprefix("sha256:")
    receipt = tmp_path / "reviewed-receipt.json"
    receipt.write_text(json.dumps({
        "profile": "kfm.site-mirror-receipt/v1",
        "destination": "apps/site/source",
        "site_candidate_commit": site_commit,
        "counts": {"missing": 0, "unexpected_difference": 0, "identical": 1},
        "comparison": {"app/page.tsx": {
            "state": "identical", "mirror_sha256": digest, "site_sha256": digest,
        }},
    }), encoding="utf-8")
    monkeypatch.setattr(TOOL, "RECEIPT", receipt)


def test_clean_source_comparison_binds_commit_and_bytes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source, _, commit = _repos(tmp_path, monkeypatch)

    result = TOOL.compare(source)

    assert result["source_commit"] == commit
    assert result["source_dirty"] is False
    assert result["changes"] == []
    assert result["unexpected_deletions"] == []


def test_dirty_source_cannot_be_labeled_with_head_commit(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source, _, commit = _repos(tmp_path, monkeypatch)
    (source / "app/page.tsx").write_text("uncommitted B\n", encoding="utf-8")

    with pytest.raises(ValueError, match="SOURCE_WORKTREE_DIRTY"):
        TOOL.compare(source)
    assert _git(source, "rev-parse", "HEAD") == commit


def test_dirty_source_cli_returns_finite_hold(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    source, _, _ = _repos(tmp_path, monkeypatch)
    (source / "app/page.tsx").write_text("uncommitted B\n", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["site_mirror.py", "--source", str(source)])

    assert TOOL.main() == 1
    assert json.loads(capsys.readouterr().out) == {
        "outcome": "FAIL", "reason_code": "MIRROR_REVIEW_REQUIRED"
    }


def test_source_change_during_comparison_fails_closed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source, _, _ = _repos(tmp_path, monkeypatch)
    original_safe = TOOL.safe
    changed = False

    def change_during_read(root: Path, name: str) -> Path:
        nonlocal changed
        path = original_safe(root, name)
        if root == source and not changed:
            path.write_text("changed during comparison\n", encoding="utf-8")
            changed = True
        return path

    monkeypatch.setattr(TOOL, "safe", change_during_read)
    with pytest.raises(ValueError, match="SOURCE_WORKTREE_CHANGED"):
        TOOL.compare(source)


def test_diagnose_reports_exact_working_tree_drift_without_lifting_check(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    source, destination, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    assert TOOL.check()["outcome"] == "PASS"
    clean_report = TOOL.diagnose()
    assert clean_report["outcome"] == "RECORDED_BYTES_MATCH"
    assert clean_report["changed"] == []
    assert clean_report["repository_dirty"] is False

    changed = destination / "app/page.tsx"
    changed.write_text("monorepo overlay B\n", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["site_mirror.py", "--diagnose"])
    assert TOOL.main() == 1
    report = json.loads(capsys.readouterr().out)
    assert report["outcome"] == "REVIEW_REQUIRED"
    assert report["authority"] == "REVIEW_ONLY"
    assert report["byte_source"] == "working_tree"
    assert report["repository_dirty"] is True
    assert report["site_candidate_commit_in_receipt"] == commit
    assert report["changed"] == [{
        "path": "app/page.tsx", "receipt_state": "identical",
        "recorded_sha256": TOOL.sha(b"source A\n"),
        "working_tree_sha256": TOOL.sha(b"monorepo overlay B\n"),
    }]
    assert changed.read_text(encoding="utf-8") == "monorepo overlay B\n"
    with pytest.raises(ValueError, match="MIRROR_CONTENT_DRIFT:app/page.tsx"):
        TOOL.check()


def test_diagnose_lists_unrecorded_tracked_mirror_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source, destination, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    extra = destination / "app/new-client.ts"
    extra.write_text("export const added = true;\n", encoding="utf-8")
    _git(destination.parents[2], "add", ".")
    report = TOOL.diagnose()
    assert report["outcome"] == "REVIEW_REQUIRED"
    assert report["unrecorded_mirror_paths"] == ["app/new-client.ts"]
    assert report["missing_mirror_paths"] == []
    with pytest.raises(ValueError, match="MIRROR_FILE_SET_DRIFT"):
        TOOL.check()


def test_diagnostic_cannot_accept_an_invalid_reviewed_receipt(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, _, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    document = json.loads(TOOL.RECEIPT.read_text(encoding="utf-8"))
    document["comparison"]["app/page.tsx"]["mirror_sha256"] = "0" * 64
    TOOL.RECEIPT.write_text(json.dumps(document), encoding="utf-8")
    for validate in (TOOL.check, TOOL.diagnose):
        with pytest.raises(ValueError, match="MIRROR_IDENTICAL_MISMATCH"):
            validate()


def test_repository_only_overlay_state_is_counted_and_unknown_states_fail(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, destination, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    extra = destination / "app/new-client.ts"
    extra.write_text("export const added = true;\n", encoding="utf-8")
    _git(destination.parents[2], "add", ".")
    document = json.loads(TOOL.RECEIPT.read_text(encoding="utf-8"))
    document["comparison"]["app/new-client.ts"] = {
        "state": "repository_only_overlay",
        "mirror_sha256": TOOL.sha(b"export const added = true;\n").removeprefix("sha256:"),
    }
    document["counts"]["repository_only_overlay"] = 1
    TOOL.RECEIPT.write_text(json.dumps(document), encoding="utf-8")
    assert TOOL.check()["files"] == 2

    document["counts"]["repository_only_overlay"] = 0
    TOOL.RECEIPT.write_text(json.dumps(document), encoding="utf-8")
    with pytest.raises(ValueError, match="MIRROR_RECEIPT_COUNTS_DRIFT"):
        TOOL.check()

    document["comparison"]["app/new-client.ts"]["state"] = "unreviewed_overlay"
    TOOL.RECEIPT.write_text(json.dumps(document), encoding="utf-8")
    with pytest.raises(ValueError, match="MIRROR_RECEIPT_STATE_INVALID"):
        TOOL.check()
