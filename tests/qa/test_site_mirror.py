"""The mirror comparison must bind source bytes to its reported commit."""
from __future__ import annotations

import importlib.util
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("kfm_site_mirror", ROOT / "tools/qa/site_mirror.py")
assert SPEC and SPEC.loader
TOOL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOOL)
DEFAULT_RECEIPT_RELATIVE = TOOL.RECEIPT.relative_to(ROOT)


def test_current_receipt_preserves_source_identity_withheld_inventory_and_pending_review() -> None:
    receipt = json.loads((ROOT / DEFAULT_RECEIPT_RELATIVE).read_text())
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    previous = json.loads(predecessor.read_text())
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"]
    for key in ("site_candidate_commit", "site_project_id", "site_version_id", "site_audience",
                "authoritative_site_source_paths", "canonical_document_mappings", "canonical_tool_mappings", "overlay", "review"):
        assert receipt[key] == previous[key], key
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["review"]["human_acceptance"] is False
    assert receipt["review"]["hosted_equivalence"] is False
    assert receipt["review"]["blocking_checks"] == ["repository_review", "human_acceptance"]
    assert receipt["status"] == "REVIEW_ONLY"
    changed = receipt["repository_reconciliation"]["changes"]
    assert {entry["path"] for entry in changed if entry["proposed_in_this_change"]} == {
        "tests/local-worker-runtime.test.mjs",
    }
    restored = receipt["repository_reconciliation"]["restored_recorded_paths"]
    assert [entry["path"] for entry in restored] == ["scripts/serve-local-worker.mjs"]
    assert receipt["comparison"][restored[0]["path"]] == previous["comparison"][restored[0]["path"]]
    assert restored[0]["restored_sha256"] == previous["comparison"][restored[0]["path"]]["mirror_sha256"]
    for entry in changed:
        before = previous["comparison"].get(entry["path"])
        current = receipt["comparison"][entry["path"]]
        assert entry["previous_receipt_sha256"] == (before["mirror_sha256"] if before else None)
        assert current["site_sha256"] == (before["site_sha256"] if before else None)
        assert current["mirror_sha256"] == entry["mirror_sha256"]
        assert current["state"] != "identical"
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


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


@pytest.mark.parametrize("drift", ["source", "removed_path"])
def test_reconciliation_cannot_attest_to_old_source_or_removed_paths(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, drift: str
) -> None:
    _, _, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    document = json.loads(TOOL.RECEIPT.read_text())
    document["reconciliation"] = {
        "current_site": commit, "changes": [{"path": "app/page.tsx", "kind": "site_advance"}],
    }
    TOOL.RECEIPT.write_text(json.dumps(document))
    assert TOOL.check()["outcome"] == "PASS"
    if drift == "source":
        document["reconciliation"]["current_site"] = "0" * 40
    else:
        document["reconciliation"]["changes"][0]["path"] = "docs/OLD_PATH.md"
    TOOL.RECEIPT.write_text(json.dumps(document))
    with pytest.raises(ValueError, match="MIRROR_RECONCILIATION_.*_DRIFT"):
        TOOL.check()


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


def _withhold(document: dict, path: str = "public/data/held.json.gz") -> dict:
    document.setdefault("overlay", {})["withheld_paths"] = [{
        "path": path,
        "previous_state": "identical",
        "site_sha256": TOOL.sha(b"exact records\n").removeprefix("sha256:"),
        "state": "repository_withheld",
    }]
    document["counts"]["repository_withheld"] = 1
    return document


def test_withheld_paths_must_stay_absent_from_the_mirror(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, destination, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    document = _withhold(json.loads(TOOL.RECEIPT.read_text(encoding="utf-8")))
    TOOL.RECEIPT.write_text(json.dumps(document), encoding="utf-8")
    result = TOOL.check()
    assert result["withheld_files"] == 1
    assert "Withheld files confirmed absent" in TOOL.markdown_report(result)

    held = destination / "public/data/held.json.gz"
    held.parent.mkdir(parents=True)
    held.write_bytes(b"exact records\n")
    # Present on disk but untracked still fails: a local build would serve it.
    with pytest.raises(ValueError, match="MIRROR_WITHHELD_PATH_PRESENT:public/data/held.json.gz"):
        TOOL.check()
    assert TOOL.diagnose()["withheld_paths_present"] == ["public/data/held.json.gz"]
    assert TOOL.diagnose()["outcome"] == "REVIEW_REQUIRED"

    _git(destination.parents[2], "add", ".")
    with pytest.raises(ValueError, match="MIRROR_WITHHELD_PATH_PRESENT"):
        TOOL.check()

    held.unlink()
    held.symlink_to(destination / "app/page.tsx")
    with pytest.raises(ValueError, match="MIRROR_WITHHELD_PATH_PRESENT"):
        TOOL.check()


@pytest.mark.parametrize("damage", ["count", "state", "in_comparison", "duplicate", "unsafe", "digest", "not_list"])
def test_withheld_entries_are_validated(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, damage: str
) -> None:
    _, _, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    document = _withhold(json.loads(TOOL.RECEIPT.read_text(encoding="utf-8")))
    entry = document["overlay"]["withheld_paths"][0]
    expected = "MIRROR_WITHHELD_INVALID"
    if damage == "count":
        document["counts"]["repository_withheld"] = 0
        expected = "MIRROR_RECEIPT_COUNTS_DRIFT"
    elif damage == "state":
        entry["state"] = "identical"
    elif damage == "in_comparison":
        entry["path"] = "app/page.tsx"
    elif damage == "duplicate":
        document["overlay"]["withheld_paths"].append(dict(entry))
        document["counts"]["repository_withheld"] = 2
    elif damage == "unsafe":
        entry["path"] = "../outside.json"
        expected = "UNSAFE_MIRROR_PATH"
    elif damage == "digest":
        entry["site_sha256"] = "not-a-digest"
    else:
        document["overlay"]["withheld_paths"] = {"path": entry["path"]}
    TOOL.RECEIPT.write_text(json.dumps(document), encoding="utf-8")
    with pytest.raises(ValueError, match=expected):
        TOOL.check()


@pytest.mark.parametrize("status", ["review_pending", "accepted", None])
def test_parity_reports_review_declarations_without_evaluating_acceptance(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], status: str | None
) -> None:
    _, _, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    document = json.loads(TOOL.RECEIPT.read_text())
    if status is not None:
        document.update(status=status, review={
            "source_and_overlay_review": "PENDING" if status == "review_pending" else "ACCEPTED",
            "blocking_checks": ["repository_review", "overlay_reconciliation_with_next_site_version"],
        })
    TOOL.RECEIPT.write_text(json.dumps(document))
    monkeypatch.setattr(sys, "argv", ["site_mirror.py", "--check"])

    assert TOOL.main() == 0
    result = json.loads(capsys.readouterr().out)
    assert {key: result[key] for key in ("outcome", "files", "source_commit", "authority", "hosted_equivalence")} == {
        "outcome": "PASS", "files": 1, "source_commit": commit,
        "authority": "CONTENT_PARITY_ONLY", "hosted_equivalence": False,
    }
    assert result["review_acceptance"] == {
        "outcome": "NOT_EVALUATED", "authority": "RECEIPT_DECLARATION_ONLY", "receipt_status": status,
        "source_and_overlay_review": document.get("review", {}).get("source_and_overlay_review"),
        "blocking_checks": document.get("review", {}).get("blocking_checks"),
    }


@pytest.mark.parametrize("state", [
    "inherited_repository_overlay", "merged_water_overlay", "repository_only_water_overlay", "repository_only_overlay",
])
def test_overlay_parity_never_implies_overlay_review_or_hosted_equivalence(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, state: str
) -> None:
    _, _, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    document = json.loads(TOOL.RECEIPT.read_text())
    document["comparison"]["app/page.tsx"]["state"] = state
    document["counts"].update(identical=0, **{state: 1})
    document.update(status="review_pending", site_candidate_deployed=True,
                    review={"source_and_overlay_review": "PENDING", "blocking_checks": ["repository_review"]})
    TOOL.RECEIPT.write_text(json.dumps(document))

    result = TOOL.check()
    assert result["outcome"] == "PASS"
    assert result["file_states"] == {state: 1}
    assert result["repository_overlay_files"] == 1
    assert result["review_acceptance"]["outcome"] == "NOT_EVALUATED"
    assert result["review_acceptance"]["source_and_overlay_review"] == "PENDING"
    assert result["hosted_equivalence"] is False


@pytest.mark.parametrize("drift", [False, True])
def test_workflow_summary_preserves_parity_exit_and_separate_review_state(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, drift: bool
) -> None:
    _, destination, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    document = json.loads(TOOL.RECEIPT.read_text())
    document.update(status="review_pending", review={"source_and_overlay_review": "PENDING",
                    "blocking_checks": ["repository_review", "overlay_reconciliation_with_next_site_version"]})
    repo = TOOL.ROOT
    script = repo / "tools/qa/site_mirror.py"
    script.parent.mkdir(parents=True)
    script.write_bytes((ROOT / "tools/qa/site_mirror.py").read_bytes())
    receipt = repo / DEFAULT_RECEIPT_RELATIVE
    receipt.parent.mkdir(parents=True)
    receipt.write_text(json.dumps(document))
    if drift:
        (destination / "app/page.tsx").write_text("new unrecorded bytes\n")

    workflow = yaml.safe_load((ROOT / ".github/workflows/water-pilot.yml").read_text())
    steps = workflow["jobs"]["water-conformance"]["steps"]
    step = next(item for item in steps if "site_mirror.py --check" in item.get("run", ""))
    assert step["shell"] == "bash"
    test_step = next(item for item in steps if "pytest" in item.get("run", ""))
    assert "tests/qa/test_site_mirror.py" in test_step["run"]
    summary = tmp_path / "summary.md"
    environment = {**os.environ, "GITHUB_STEP_SUMMARY": str(summary),
                   "PATH": str(Path(sys.executable).parent) + os.pathsep + os.environ.get("PATH", "")}
    run = subprocess.run(["bash", "--noprofile", "--norc", "-e", "-o", "pipefail", "-c", step["run"]],
                         cwd=repo, env=environment, capture_output=True, text=True, timeout=30)
    assert run.returncode == (1 if drift else 0), run.stderr
    assert run.stdout == summary.read_text()
    assert 'Review acceptance evaluated by this check | <code>"NOT_EVALUATED"</code>' in run.stdout
    assert "Hosted equivalence established by this check | <code>false</code>" in run.stdout
    if drift:
        assert 'Recorded content parity | <code>"FAIL"</code>' in run.stdout
        assert "MIRROR_REVIEW_REQUIRED" in run.stdout
    else:
        assert 'Recorded content parity | <code>"PASS"</code>' in run.stdout
        assert 'Declared receipt status | <code>"review_pending"</code>' in run.stdout
        assert 'Declared source and overlay review | <code>"PENDING"</code>' in run.stdout
        assert "overlay_reconciliation_with_next_site_version" in run.stdout


def test_summary_escapes_receipt_text_without_hiding_declared_review_state() -> None:
    report = TOOL.markdown_report({"outcome": "PASS", "review_acceptance": {
        "outcome": "NOT_EVALUATED", "receipt_status": '<script>bad</script>|\n# ACCEPTED',
    }})
    assert "<script>" not in report
    assert "&lt;script&gt;bad&lt;/script&gt;&#124;\\n# ACCEPTED" in report


@pytest.mark.parametrize("drift", [None, "source_name", "site_sha256", "repository_sha256", "outside_docs"])
def test_canonical_document_mapping_binds_source_and_destination(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, drift: str | None
) -> None:
    _, destination, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    target = destination / "docs/prepared-review.md"
    target.parent.mkdir()
    target.write_text("review context\n")
    _git(TOOL.ROOT, "add", "apps/site/source/docs/prepared-review.md")
    digest = TOOL.sha(target.read_bytes()).removeprefix("sha256:")
    receipt = json.loads(TOOL.RECEIPT.read_text())
    receipt["counts"]["identical"] = 2
    receipt["comparison"]["docs/prepared-review.md"] = {
        "state": "identical", "site_source_path": "docs/PREPARED_REVIEW.md",
        "site_sha256": digest, "mirror_sha256": digest,
    }
    mapping = {"destination": "apps/site/source/docs/prepared-review.md",
               "site_sha256": digest, "repository_sha256": digest}
    receipt["canonical_document_mappings"] = {"docs/PREPARED_REVIEW.md": mapping}
    if drift == "source_name":
        receipt["comparison"]["docs/prepared-review.md"]["site_source_path"] = "docs/other.md"
    elif drift in ("site_sha256", "repository_sha256"):
        mapping[drift] = "0" * 64
    elif drift == "outside_docs":
        mapping["destination"] = "apps/site/source/app/page.tsx"
    TOOL.RECEIPT.write_text(json.dumps(receipt))
    if drift:
        with pytest.raises(ValueError, match="MIRROR_DOCUMENT_MAPPING_DRIFT"):
            TOOL.check()
    else:
        assert TOOL.check()["outcome"] == "PASS"


@pytest.mark.parametrize("drift", [None, "present", "invalid_path", "wrong_digest", "wrong_count"])
def test_withheld_private_geometry_cannot_be_reintroduced_as_parity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, drift: str | None
) -> None:
    _, destination, commit = _repos(tmp_path, monkeypatch)
    _receipt(tmp_path, monkeypatch, commit)
    receipt = json.loads(TOOL.RECEIPT.read_text())
    name = "public/data/subsurface/held.json.gz"
    entry = {"path": name, "site_sha256": "0" * 64, "state": "repository_withheld",
             "reason_code": "EXACT_GEOMETRY_PUBLICATION_HELD"}
    receipt["counts"]["repository_withheld"] = 1
    if drift == "present":
        target = destination / name
        target.parent.mkdir(parents=True)
        target.write_bytes(b"private geometry")
    elif drift == "invalid_path":
        entry["path"] = "../not-geometry.ts"
    elif drift == "wrong_digest":
        entry["site_sha256"] = "invalid"
    elif drift == "wrong_count":
        receipt["counts"]["repository_withheld"] = 0
    receipt["overlay"] = {"withheld_paths": [entry]}
    TOOL.RECEIPT.write_text(json.dumps(receipt))
    if drift:
        with pytest.raises(ValueError, match="MIRROR_WITHHELD|MIRROR_RECEIPT_COUNTS_DRIFT|UNSAFE_MIRROR_PATH"):
            TOOL.check()
    else:
        result = TOOL.check()
        assert result["outcome"] == "PASS"
        assert result["withheld_files"] == 1
