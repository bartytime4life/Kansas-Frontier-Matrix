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


def test_historical_runtime_receipt_preserves_its_recorded_comparison() -> None:
    # Its earlier comparison basis is preserved history, not actual merge ancestry.
    receipt = json.loads((ROOT / "data/receipts/generated/site-v268-current-main-runtime-reconciliation-20261017.json").read_text())
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



def _mirror_projection(receipt: dict) -> dict:
    return {name: tuple(entry.get(key) for key in ("mirror_sha256", "site_sha256", "state"))
            for name, entry in receipt["comparison"].items()}


def test_historical_consolidation_preserves_its_recorded_lineage_comparison() -> None:
    receipt = json.loads((ROOT / "data/receipts/generated/site-v268-consolidated-runtime-lineage-20261017.json").read_text())
    directory = ROOT / "data/receipts/generated"
    previous_path = directory / receipt["predecessor_receipt"]
    previous = json.loads(previous_path.read_text())
    assert previous_path.name == "site-v268-current-main-runtime-reconciliation-20261017.json"
    assert hashlib.sha256(previous_path.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"]
    assert _mirror_projection(receipt) == _mirror_projection(previous)
    assert receipt["inventory_sha256"] == previous["inventory_sha256"]
    assert receipt["counts"] == previous["counts"]
    assert len(receipt["comparison"]) == 874
    for key in ("site_candidate_commit", "site_project_id", "site_version_id", "site_audience",
                "authoritative_site_source_paths", "canonical_document_mappings", "canonical_tool_mappings",
                "overlay", "review", "repository_safety_changes"):
        assert receipt[key] == previous[key], key
    assert receipt["counts"]["repository_withheld"] == 258
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"]["human_acceptance"] is False
    assert receipt["review"]["hosted_equivalence"] is False
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["repository_reconciliation"]["changes"] == []
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []

    correction = receipt["historical_lineage_correction"]
    assert correction["affected_receipt"] == previous_path.name
    assert correction["affected_receipt_sha256"] == receipt["predecessor_receipt_sha256"]
    assert correction["actual_parent_commit"] == "da5bc7b0ae14a9383efec17f9c9dfb0e9c4039eb"
    parent_path = directory / correction["parent_selected_receipt"]
    parent = json.loads(parent_path.read_text())
    assert parent_path.name == "site-v268-explorer-local-port-overlay-20261017.json"
    assert hashlib.sha256(parent_path.read_bytes()).hexdigest() == correction["parent_selected_receipt_sha256"]
    parent_projection = _mirror_projection(parent)
    previous_projection = _mirror_projection(previous)
    actual_delta = {name for name in parent_projection.keys() | previous_projection.keys()
                    if parent_projection.get(name) != previous_projection.get(name)}
    declared = correction["corrected_changes"]
    assert actual_delta == {entry["path"] for entry in declared} == {"tests/local-worker-runtime.test.mjs"}
    assert len(declared) == 1
    entry = declared[0]
    assert entry["previous_receipt_sha256"] == parent["comparison"][entry["path"]]["mirror_sha256"]
    assert entry["repository_base_sha256"] == entry["previous_receipt_sha256"]
    assert entry["mirror_sha256"] == receipt["comparison"][entry["path"]]["mirror_sha256"]
    assert correction["corrected_restored_recorded_paths"] == []
    inherited = set(correction["already_reconciled_paths"])
    assert len(inherited) == 24
    assert inherited == {entry["path"] for entry in previous["repository_reconciliation"]["changes"]} - actual_delta
    for name in inherited:
        assert parent_projection[name] == previous_projection[name]
    for name in correction["restored_provenance_notes"]:
        assert receipt["comparison"][name]["difference"] == parent["comparison"][name]["difference"]
    # Neither selecting an old receipt nor copying its rollback advice is a correction.
    assert previous_path.name in receipt["rollback"]["mirror"]


def test_historical_attribution_successor_names_the_commit_that_changes_the_test() -> None:
    receipt = json.loads((ROOT / "data/receipts/generated/site-v268-runtime-lineage-attribution-20261017.json").read_text())
    previous_path = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert previous_path.name == "site-v268-consolidated-runtime-lineage-20261017.json"
    assert hashlib.sha256(previous_path.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"]
    previous = json.loads(previous_path.read_text())
    for key in ("comparison", "inventory_sha256", "counts", "overlay", "review",
                "site_candidate_commit", "site_project_id", "site_version_id", "site_audience",
                "authoritative_site_source_paths", "canonical_document_mappings", "canonical_tool_mappings"):
        assert receipt[key] == previous[key], key
    assert receipt["status"] == previous["status"] == "REVIEW_ONLY"
    assert receipt["repository_reconciliation"]["changes"] == []
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    correction = receipt["historical_lineage_correction"]
    attribution = correction["attribution_correction"]
    expected = "0aaedbe41941e3867d591159b6a3fa90a90553ac"
    assert attribution["verified_change_commit"] == expected
    assert attribution["change_commit_parent"] == "e30566dfa299fd3e540da239a5c9ec018b2fd4cc"
    assert attribution["merged_head_parents"] == [expected, correction["actual_parent_commit"]]
    assert attribution["affected_receipt"] == previous_path.name
    assert attribution["affected_receipt_sha256"] == receipt["predecessor_receipt_sha256"]
    changed = correction["corrected_changes"]
    assert len(changed) == 1
    assert changed[0]["path"] == attribution["path"] == "tests/local-worker-runtime.test.mjs"
    assert changed[0]["last_repository_change_commit"] == expected
    assert previous["historical_lineage_correction"]["corrected_changes"][0]["last_repository_change_commit"] == attribution["previously_recorded_commit"]
    assert attribution["before_sha256"] == changed[0]["previous_receipt_sha256"]
    assert attribution["after_sha256"] == receipt["comparison"][attribution["path"]]["mirror_sha256"]
    assert attribution["before_sha256"] != attribution["after_sha256"]
    assert attribution["evidence_ref"].endswith("/commit/" + expected)
    assert previous_path.name in receipt["rollback"]["mirror"]


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


def test_historical_layout_receipt_preserves_unrelated_bytes_and_private_boundaries(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-explorer-reference-layout-20261017.json")
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    previous = json.loads(predecessor.read_text())
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"]
    assert set(receipt["comparison"]) == set(previous["comparison"])
    changed = {path for path in receipt["comparison"]
               if receipt["comparison"][path] != previous["comparison"][path]}
    assert changed == {"app/page.tsx", "app/inspection-panel.css"}
    declared = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declared) == changed
    for path in changed:
        entry = receipt["comparison"][path]
        assert entry["site_sha256"] == previous["comparison"][path]["site_sha256"]
        assert entry["state"] == "inherited_repository_overlay"
        assert declared[path]["previous_receipt_sha256"] == previous["comparison"][path]["mirror_sha256"]
        assert declared[path]["repository_base_sha256"] == declared[path]["previous_receipt_sha256"]
        assert declared[path]["mirror_sha256"] == entry["mirror_sha256"]
        # Bound to the receipt's own declaration: a successor (aviation layers)
        # changes current page.tsx bytes, and the selected receipt records that.
        assert "sha256:" + declared[path]["mirror_sha256"] == expected[path]
    for key in ("site_candidate_commit", "site_project_id", "site_version_id", "site_audience",
                "authoritative_site_source_paths", "canonical_document_mappings", "canonical_tool_mappings",
                "overlay", "review", "repository_safety_changes", "historical_lineage_correction"):
        assert receipt[key] == previous[key], key
    assert receipt["review"]["human_acceptance"] is False
    assert receipt["review"]["hosted_equivalence"] is False
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["counts"]["repository_withheld"] == 258
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {path: entry["mirror_sha256"] for path, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_historical_focus_mode_receipt_records_only_the_existing_repository_test(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-focus-mode-test-reconciliation-20261018.json")
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-explorer-reference-layout-20261017.json"
    previous = json.loads(predecessor.read_text())
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"]
    path = "tests/focus-mode-provenance.test.mjs"
    assert set(receipt["comparison"]) - set(previous["comparison"]) == {path}
    assert set(previous["comparison"]) - set(receipt["comparison"]) == set()
    for name, entry in previous["comparison"].items():
        assert receipt["comparison"][name] == entry, name
    entry = receipt["comparison"][path]
    digest = "58d3578d33c9a5479ba807f46397d08c3d1997c8a63dff1a687ff1aa4267277f"
    assert entry["mirror_sha256"] == hashlib.sha256((TOOL.DESTINATION / path).read_bytes()).hexdigest() == digest
    assert expected[path] == "sha256:" + digest
    assert entry["site_sha256"] is None
    assert entry["state"] == "repository_only_overlay"
    changes = receipt["repository_reconciliation"]["changes"]
    assert len(changes) == 1
    assert changes[0]["path"] == path
    assert changes[0]["previous_receipt_sha256"] is None
    assert changes[0]["repository_base_sha256"] == changes[0]["mirror_sha256"] == digest
    assert changes[0]["state"] == entry["state"]
    assert changes[0]["proposed_in_this_change"] is False
    assert changes[0]["last_repository_change_commit"] == "f64a45a46e82b3c92dfd4e0a6047cb02a29e164a"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"]
    assert len(expected) == len(previous["comparison"]) + 1 == 875
    for key, count in previous["counts"].items():
        assert receipt["counts"][key] == count + (1 if key == "repository_only_overlay" else 0), key
    for key in ("profile", "status", "authority", "selector_authority", "destination", "repository_base",
                "site_candidate_commit", "site_project_id", "site_version_id", "site_audience",
                "site_archive_sha256", "site_deployment_status", "site_deployment_id",
                "authoritative_site_source_paths", "canonical_document_mappings", "canonical_tool_mappings",
                "overlay", "review", "repository_safety_changes", "historical_lineage_correction", "reconciliation"):
        assert receipt[key] == previous[key], key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"]["human_acceptance"] is receipt["review"]["hosted_equivalence"] is False
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["counts"]["repository_withheld"] == 258
    inventory = {name: item["mirror_sha256"] for name, item in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_historical_subsurface_receipt_binds_only_the_private_output_patch(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-private-subsurface-output-reconciliation-20261019.json")
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-focus-mode-test-reconciliation-20261018.json"
    previous = json.loads(predecessor.read_text())
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"]
    modified = {"docs/subsurface-data.md", "scripts/prepare-subsurface.py", "tests/subsurface-assets.test.mjs"}
    added = {"tests/test_prepare_subsurface.py"}
    changed = modified | added
    assert set(receipt["comparison"]) - set(previous["comparison"]) == added
    assert set(previous["comparison"]) - set(receipt["comparison"]) == set()
    assert {name for name in modified if receipt["comparison"][name] != previous["comparison"][name]} == modified
    for name, entry in previous["comparison"].items():
        if name not in changed:
            assert receipt["comparison"][name] == entry, name
    declarations = {item["path"]: item for item in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == changed
    for name in changed:
        entry = receipt["comparison"][name]
        before = previous["comparison"].get(name)
        digest = hashlib.sha256((TOOL.DESTINATION / name).read_bytes()).hexdigest()
        assert entry["mirror_sha256"] == digest
        assert expected[name] == "sha256:" + digest
        assert entry["site_sha256"] == (before["site_sha256"] if before else None)
        assert entry["state"] == ("repository_safety_overlay" if before else "repository_only_overlay")
        declaration = declarations[name]
        assert declaration["previous_receipt_sha256"] == (before["mirror_sha256"] if before else None)
        assert declaration["repository_base_sha256"] == declaration["mirror_sha256"] == digest
        assert declaration["state"] == entry["state"]
        assert declaration["last_repository_change_commit"] == "128da1e110973a851e43321f1d4186b4f00e1870"
        assert declaration["proposed_in_this_change"] is False
    for key in ("profile", "status", "authority", "selector_authority", "destination", "repository_base",
                "site_candidate_commit", "site_project_id", "site_version_id", "site_audience",
                "site_archive_sha256", "site_deployment_status", "site_deployment_id",
                "authoritative_site_source_paths", "canonical_document_mappings", "canonical_tool_mappings",
                "overlay", "review", "repository_safety_changes", "historical_lineage_correction", "reconciliation"):
        assert receipt[key] == previous[key], key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"]["human_acceptance"] is receipt["review"]["hosted_equivalence"] is False
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["counts"]["repository_withheld"] == previous["counts"]["repository_withheld"] == 258
    for key, count in previous["counts"].items():
        delta = {"identical": -3, "repository_safety_overlay": 3, "repository_only_overlay": 1}.get(key, 0)
        assert receipt["counts"][key] == count + delta, key
    assert len(expected) == len(previous["comparison"]) + 1 == 876
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"]
    inventory = {name: item["mirror_sha256"] for name, item in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_historical_main_overlay_receipt_binds_only_the_merged_overlay_changes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-main-overlay-reconciliation-20261021.json")
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-private-subsurface-output-reconciliation-20261019.json"
    previous = json.loads(predecessor.read_text())
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"]
    commits = {
        5326: "f6e393640ec66870f4a1b50cd718ff39e6cfd565",
        5327: "592b7b1c873ea345e6e8231a3b65b96ca3a1f707",
        5364: "c3522ce8aa1d6262ff934d4dc587a5582f2c0a78",
        5365: "245796d6dc8f44e0140ba6645f02886009b5f39f",
        5378: "94ccd8180f20f191a4955ac35ec845f4dcaf2dcc",
    }
    modified = {
        "app/api/data-submissions/route.ts": 5326, "app/api/land-records/route.ts": 5326,
        "app/data-intake-server.ts": 5326, "drizzle/meta/_journal.json": 5326, "tests/land-records.test.mjs": 5326,
        "app/api/historical-topo/overlay/route.ts": 5327, "app/api/historical-topo/queue/route.ts": 5327,
        "app/earth-engine-local-read.ts": 5327, "scripts/qwen-local-contract.mjs": 5327,
        "scripts/serve-local-worker.mjs": 5327, "tests/historical-topo-routes.test.mjs": 5327,
        "tests/hms-smoke-playback.test.mjs": 5327, "tests/local-qwen-bridge.test.mjs": 5327,
        "tests/local-worker-runtime.test.mjs": 5327,
        "scripts/earth-engine/requirements.txt": 5364,
        "package-lock.json": 5365, "package.json": 5365,
    }
    added = {
        "drizzle/0011_submission_uploads.sql": 5326, "tests/helpers/land-fixture.mjs": 5326,
        "tests/submission-quota.test.mjs": 5326, "docs/submission-upload-quota.md": 5378,
    }
    changed = modified | added
    assert set(receipt["comparison"]) - set(previous["comparison"]) == set(added)
    assert set(previous["comparison"]) - set(receipt["comparison"]) == set()
    for name, entry in previous["comparison"].items():
        if name not in changed:
            assert receipt["comparison"][name] == entry, name
    # Golden digests independently verified against the historical Git source basis.
    recorded_digests = {
        'app/api/data-submissions/route.ts': '6b77501518d38cdb5013fede89385f969353859d2f10df04ecffe1547721a371',
        'app/api/historical-topo/overlay/route.ts': '84da2d5fa4d5981e958b7f86c1515711c7df0c0b6cca2910378e8c39b31ec3e3',
        'app/api/historical-topo/queue/route.ts': '41e1b9f62a5cb5ac0d346330176e4a235a705730aae6895e75c0c661fef5b247',
        'app/api/land-records/route.ts': '1ee1f26703db1a9582b466c928d1b5e57fb1ff574e7b8e428aa677b5fb3cba38',
        'app/data-intake-server.ts': '65d5f58c947ecd4ef5237fdcbe51aa863687c335bb96f04f0a61364bc92163a9',
        'app/earth-engine-local-read.ts': '7e39801c0ffaf5b15e739c2497e63e2af94bcc6686d1b6e7e6cdc6eca56168a1',
        'docs/submission-upload-quota.md': 'a9ffc3bcaf6279bb9b10452d334b81c5d5e42119e28c15f755842b0a85d590fd',
        'drizzle/0011_submission_uploads.sql': 'f040dd7bd87559b50fccb1a7a2c90deaaa2676e26a905319abb8d6a77c24bd36',
        'drizzle/meta/_journal.json': '7a4257d669148a8f5af469fa1d676a1a723da42975b4e1c18c53d7826fb591d6',
        'package-lock.json': '6c3aff35387b14e40e4f8fd2436a8d78e71bcab3869ef7a30e37dc982e236bf4',
        'package.json': '8782b3a363afb7855605523aaf8d963608dd1ba26e388d8b35fd390380ef8a5b',
        'scripts/earth-engine/requirements.txt': 'a81839f87d88bded8814af2f5a36ef64033501c32a5fd6e203d68ff6f5b272a1',
        'scripts/qwen-local-contract.mjs': '1f4a4bf09f136453c27b6c28276477517a1afc1336fea679e6df31ca080ffe90',
        'scripts/serve-local-worker.mjs': '967721a420eef809a5f33d4dcd2259b08e0ac49ff4c55831ee52e2b0dd65ceb2',
        'tests/helpers/land-fixture.mjs': 'e79fe9ef914971dbc509c00dc0339d289a7744023d1cf5573ff8f4122e375ee6',
        'tests/historical-topo-routes.test.mjs': 'b75eddd652d89adcb0e1d87052efc8bbf7ec9c513a569e1c2f15d071af1c1382',
        'tests/hms-smoke-playback.test.mjs': 'fbe86c252b68404e8b41e26d503c4821b94d2acf266cafa66e8416bd90e1718b',
        'tests/land-records.test.mjs': '12750d5a942e1bacda44a78e35170fcd83fd190e03ccf57edfdd0a547a6d3fb5',
        'tests/local-qwen-bridge.test.mjs': '5b1b5c3bd17b638d8e4d49bb1f1a8355ffbab739d830df62f27cb27f757fc7d2',
        'tests/local-worker-runtime.test.mjs': '0a6cd813e7f669c7c4943dc4ef20db39f55e6286d976883873ab88420271a217',
        'tests/submission-quota.test.mjs': '846465d3e86b03f2ab139c41c3d4e20d89fdb79c6683543656e6b1c2c63cb029',
    }
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "22ad18bc3d002965c672a22a0bb45be18ca881b8d11e565ae6c5300bfa942ca4"
    declarations = {item["path"]: item for item in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == set(changed)
    for name, pull_request in changed.items():
        entry = receipt["comparison"][name]
        before = previous["comparison"].get(name)
        digest = recorded_digests[name]
        assert entry["mirror_sha256"] == digest != (before["mirror_sha256"] if before else None)
        assert expected[name] == "sha256:" + digest
        assert entry["site_sha256"] == (before["site_sha256"] if before else None)
        if before is None:
            assert entry["state"] == "repository_only_overlay"
        elif before["state"] == "identical":
            assert entry["state"] == "inherited_repository_overlay"
        else:
            assert entry["state"] == before["state"]
        assert f"#{pull_request}" in entry["difference"]
        declaration = declarations[name]
        assert declaration["previous_receipt_sha256"] == (before["mirror_sha256"] if before else None)
        assert declaration["repository_base_sha256"] == declaration["mirror_sha256"] == digest
        assert declaration["state"] == entry["state"]
        assert declaration["pull_request"] == pull_request
        assert declaration["last_repository_change_commit"] == commits[pull_request]
        assert declaration["proposed_in_this_change"] is False
    for key in ("profile", "status", "authority", "selector_authority", "destination", "repository_base",
                "site_candidate_commit", "site_project_id", "site_version_id", "site_audience",
                "site_archive_sha256", "site_deployment_status", "site_deployment_id",
                "authoritative_site_source_paths", "canonical_document_mappings", "canonical_tool_mappings",
                "overlay", "review", "repository_safety_changes", "historical_lineage_correction", "reconciliation"):
        assert receipt[key] == previous[key], key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"]["human_acceptance"] is receipt["review"]["hosted_equivalence"] is False
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["counts"]["repository_withheld"] == previous["counts"]["repository_withheld"] == 258
    for key, count in previous["counts"].items():
        delta = {"identical": -14, "inherited_repository_overlay": 14, "repository_only_overlay": 4}.get(key, 0)
        assert receipt["counts"][key] == count + delta, key
    assert len(expected) == len(previous["comparison"]) + 4 == 880
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    assert receipt["repository_reconciliation"]["overlap"]["pull_requests"] == [5325, 5326, 5327, 5364, 5365, 5378]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"]
    inventory = {name: item["mirror_sha256"] for name, item in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_historical_quota_receipt_binds_exact_merged_bytes_and_preserves_history(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-historical-quota-reconciliation-20261022.json")
    receipt, expected = TOOL.reviewed_receipt()
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "77d8ba17e70384f4f37f76a2648f46899a1e18bfcd0d02dcee1cc04aeff75b63"
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-main-overlay-reconciliation-20261021.json"
    previous = json.loads(predecessor.read_text())
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"]
    # The prior receipt is intact, and its source basis is the actual pre-quota merge.
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == "22ad18bc3d002965c672a22a0bb45be18ca881b8d11e565ae6c5300bfa942ca4"
    changed = {
        "app/api/historical-topo/overlay/route.ts", "app/historical-topo-overlay-server.ts",
        "app/historical-topo-request-quota.ts", "docs/historical-topo-request-quota.md",
        "tests/historical-topo-quota.test.mjs", "tests/historical-topo-routes.test.mjs",
    }
    added = {"app/historical-topo-request-quota.ts", "docs/historical-topo-request-quota.md",
             "tests/historical-topo-quota.test.mjs"}
    head = "3a0c40d8033bb43f432320ef9dcfbded8b9d0000"
    # Pinned source manifest verified from the six PR #5400 Git blobs. CI may
    # use a shallow checkout; historical provenance must not depend on network.
    source_digests = {
        'app/api/historical-topo/overlay/route.ts': '4a7d594c16feb56ca83c57bde11a42eb7318467453cd3e54fe4e126c5cfaf420',
        'app/historical-topo-overlay-server.ts': '57f6f59875719c67a656d7022189cd433d0118e30918e80f00e376a337cd3b0f',
        'app/historical-topo-request-quota.ts': '4aa535df5311249ef4660249959e278f80eb5b817c8487808d717ab931df0a1d',
        'docs/historical-topo-request-quota.md': 'e0be1c54a8c2fe434376e26b387a311451536662fcf87d8c7464f3e053ca98f1',
        'tests/historical-topo-quota.test.mjs': '971e8585fe938da9f063b6dc9e9c8496860b2b8c3e77c9dfaff0f049fac41e97',
        'tests/historical-topo-routes.test.mjs': '9c09ab92e161be63f3dc7d03921f2609b812d5f6f8b1fc59d2416e5932c5a63d',
    }
    assert set(source_digests) == changed
    assert set(receipt["comparison"]) - set(previous["comparison"]) == added
    assert set(previous["comparison"]) - set(receipt["comparison"]) == set()
    declarations = {item["path"]: item for item in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == changed
    for name, entry in previous["comparison"].items():
        if name not in changed:
            assert receipt["comparison"][name] == entry, name
    for name in changed:
        # Keep the historical assertion bound to the independently verified
        # source manifest when a successor changes current mirror bytes.
        digest = source_digests[name]
        before = previous["comparison"].get(name)
        entry, declaration = receipt["comparison"][name], declarations[name]
        assert entry["mirror_sha256"] == digest != (before["mirror_sha256"] if before else None)
        assert expected[name] == "sha256:" + digest
        assert entry["site_sha256"] == (before["site_sha256"] if before else None)
        assert entry["state"] == ("repository_only_overlay" if before is None else
                                  "repository_safety_overlay" if before["state"] == "identical" else before["state"])
        assert "#5400" in entry["difference"]
        assert declaration["previous_receipt_sha256"] == (before["mirror_sha256"] if before else None)
        assert declaration["repository_base_sha256"] == declaration["mirror_sha256"] == digest
        assert declaration["state"] == entry["state"]
        assert declaration["pull_request"] == 5400
        assert declaration["last_repository_change_commit"] == head
        assert declaration["proposed_in_this_change"] is False
    for key in previous:
        if key not in {"comparison", "counts", "inventory_sha256", "predecessor_receipt",
                       "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
                       "repository_reconciliation", "rollback", "validation"}:
            assert receipt[key] == previous[key], key
    for key, count in previous["counts"].items():
        assert receipt["counts"][key] == count + {
            "identical": -1, "repository_safety_overlay": 1, "repository_only_overlay": 3,
        }.get(key, 0), key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["review"]["human_acceptance"] is receipt["review"]["hosted_equivalence"] is False
    assert receipt["counts"]["repository_withheld"] == 258
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "3dc133f98e9496a8f74c21aca8390d6354be6889"
    inventory = {name: item["mirror_sha256"] for name, item in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_historical_next_receipt_binds_only_the_dependency_safety_overlay(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-next-security-overlay-20261022.json")
    receipt, expected = TOOL.reviewed_receipt()
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "0ffbfaf7293dede78f560d6e9131b9b6df08069d9fbb7f8582b1243d1f697fae"
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-historical-quota-reconciliation-20261022.json"
    predecessor_digest = "77d8ba17e70384f4f37f76a2648f46899a1e18bfcd0d02dcee1cc04aeff75b63"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == predecessor_digest
    previous = json.loads(predecessor.read_text())
    changed = {"package.json", "package-lock.json"}
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"])
    actual_delta = {name for name, entry in receipt["comparison"].items()
                    if entry != previous["comparison"][name]}
    assert actual_delta == changed
    digests = {
        "package.json": "118cf2b5fc62446eb5ad8b895ef0a9a24715e2774e23e88b7fa25947d21b6f7a",
        "package-lock.json": "caf3c477c1c017e9b5aacbad2cbaffb68512098e3df20cb2de646d3c4a305a09",
    }
    declarations = receipt["repository_reconciliation"]["changes"]
    assert len(declarations) == len(changed)
    declarations = {entry["path"]: entry for entry in declarations}
    assert set(declarations) == changed
    for name, entry in receipt["comparison"].items():
        before = previous["comparison"][name]
        assert entry.get("site_sha256") == before.get("site_sha256"), name
        if name not in changed:
            assert entry == before, name
            continue
        assert before["state"] == "inherited_repository_overlay"
        assert entry["state"] == "repository_safety_overlay"
        assert entry["mirror_sha256"] == digests[name] != before["mirror_sha256"]
        assert expected[name] == "sha256:" + digests[name]
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"],
            "mirror_sha256": digests[name], "state": "repository_safety_overlay",
            "proposed_in_this_change": True,
        }
    administrative = {
        "comparison", "counts", "inventory_sha256", "predecessor_receipt",
        "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
        "repository_reconciliation", "rollback", "security", "validation",
    }
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    for key, count in previous["counts"].items():
        delta = {"inherited_repository_overlay": -2, "repository_safety_overlay": 2}.get(key, 0)
        assert receipt["counts"][key] == count + delta, key
    assert receipt["site_candidate_commit"] == "358280aee889e2e2cf832bd598155ca21653c8de"
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["review"]["human_acceptance"] is receipt["review"]["hosted_equivalence"] is False
    assert receipt["counts"]["repository_withheld"] == 258
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "e18b56879cd71ff13502c6e12f2f1f4c7f02ee6d"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: item["mirror_sha256"] for name, item in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_selected_receipt_verifies_current_dependency_files_and_mirror() -> None:
    receipt, expected = TOOL.reviewed_receipt()
    manifest = json.loads((TOOL.DESTINATION / "package.json").read_text())
    lock = json.loads((TOOL.DESTINATION / "package-lock.json").read_text())
    for section, name in (("dependencies", "next"), ("devDependencies", "eslint-config-next")):
        assert manifest[section][name] == lock["packages"][""][section][name] == "16.4.2"
    next_packages = {name: entry for name, entry in lock["packages"].items()
                     if name.startswith("node_modules/@next/") or name in {
                         "node_modules/next", "node_modules/eslint-config-next"}}
    assert len(next_packages) == 12
    assert {entry["version"] for entry in next_packages.values()} == {"16.4.2"}
    assert manifest["overrides"]["fast-uri"] == lock["packages"]["node_modules/fast-uri"]["version"] == "3.1.9"
    assert manifest["overrides"]["miniflare"]["undici"] == lock["packages"]["node_modules/undici"]["version"] == "7.30.1"
    result = TOOL.check()
    assert result["files"] == len(expected) == len(receipt["comparison"]) == 902
    assert result["receipt_file"] == TOOL.RECEIPT.name
    assert result["outcome"] == "PASS"
    assert result["authority"] == "CONTENT_PARITY_ONLY"
    assert result["file_states"]["inherited_repository_overlay"] == 59
    assert result["file_states"]["repository_only_overlay"] == 37
    assert result["file_states"]["repository_safety_overlay"] == 8
    assert result["withheld_files"] == 258
    assert result["review_acceptance"]["outcome"] == "NOT_EVALUATED"
    assert result["review_acceptance"]["source_and_overlay_review"] == "PENDING"
    assert result["hosted_equivalence"] is False


AVIATION_ADDED = {
    "app/api/aviation/metar/route.ts", "app/api/aviation/pireps/route.ts", "app/aviation-airspace.ts",
    "app/aviation-control.tsx", "app/aviation-weather-server.ts", "app/aviation-weather.ts",
    "docs/aviation-layers.md", "public/data/aviation/kansas-aviation-context.json", "tests/aviation.test.mjs",
}
AVIATION_CHANGED = {
    "app/explorer-controls.css", "app/layer-workspaces.ts", "app/page.tsx", "app/site-architecture.ts",
    "app/site-features.ts", "docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md", "tests/layer-explorer.test.mjs",
}


def test_historical_aviation_receipt_binds_only_the_aviation_overlay(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-aviation-layers-overlay-20261022.json")
    # Historical bytes are immutable. Current files are checked by the successor test.
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "ec68b24d6445238b64364a2677de575d19e1eb71f388471304e1b26daf6e5ec0"
    receipt, expected = TOOL.reviewed_receipt()
    assert TOOL.RECEIPT.name == "site-v268-aviation-layers-overlay-20261022.json"
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-next-security-overlay-20261022.json"
    predecessor_digest = "0ffbfaf7293dede78f560d6e9131b9b6df08069d9fbb7f8582b1243d1f697fae"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == predecessor_digest
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"]) | AVIATION_ADDED
    assert not AVIATION_ADDED & set(previous["comparison"])
    actual_delta = {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"].get(name)}
    assert actual_delta == AVIATION_ADDED | AVIATION_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == actual_delta and len(receipt["repository_reconciliation"]["changes"]) == len(actual_delta)
    for name in actual_delta:
        entry, before = receipt["comparison"][name], previous["comparison"].get(name)
        digest = entry["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        if before is None:
            assert entry["state"] == "repository_only_overlay" and entry["site_sha256"] is None
        else:
            assert entry["site_sha256"] == before["site_sha256"], name
            assert entry["state"] == ("inherited_repository_overlay" if before["state"] == "identical" else before["state"])
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"] if before else None,
            "repository_base_sha256": before["mirror_sha256"] if before else None,
            "mirror_sha256": digest, "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {
        "comparison", "counts", "inventory_sha256", "predecessor_receipt",
        "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
        "repository_reconciliation", "rollback", "security", "validation",
    }
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    for key, count in previous["counts"].items():
        delta = {"identical": -4, "inherited_repository_overlay": 4, "repository_only_overlay": 9}.get(key, 0)
        assert receipt["counts"][key] == count + delta, key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"] == previous["review"]
    assert receipt["overlay"] == previous["overlay"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "123d8645b84e705789390f2ca4cbd66cc1eb2f0e"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: item["mirror_sha256"] for name, item in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_historical_pirep_receipt_binds_only_the_weather_parsing_correction(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-pirep-weather-parsing-overlay-20261022.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "8a1ae49ed41d78b9dc25ac97348b217ac4d0e9a91ccf8af7c179bb78bb930dcd"
    receipt, expected = TOOL.reviewed_receipt()
    assert TOOL.RECEIPT.name == "site-v268-pirep-weather-parsing-overlay-20261022.json"
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-aviation-layers-overlay-20261022.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "ec68b24d6445238b64364a2677de575d19e1eb71f388471304e1b26daf6e5ec0"
    previous = json.loads(predecessor.read_text())
    changed = {"app/aviation-weather.ts", "app/aviation-control.tsx", "tests/aviation.test.mjs", "docs/aviation-layers.md"}
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"])
    assert {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"][name]} == changed
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == changed and len(receipt["repository_reconciliation"]["changes"]) == len(changed)
    for name in changed:
        entry, before = receipt["comparison"][name], previous["comparison"][name]
        # Bound to the receipt's own declaration: the drone-grid/TFR successor
        # changes current bytes of these files, and the selected receipt records that.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        assert entry["site_sha256"] == before["site_sha256"]
        assert entry["state"] == before["state"] == "repository_only_overlay"
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"], "mirror_sha256": digest,
            "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "inventory_sha256", "predecessor_receipt", "predecessor_receipt_sha256",
                      "recorded_at", "repository_reconciled_base", "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "472747fe92a343472829234f40e85b47d9c8e694"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["review"]["hosted_equivalence"] is receipt["review"]["human_acceptance"] is False
    assert receipt["counts"]["repository_withheld"] == 258
    inventory = {name: item["mirror_sha256"] for name, item in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_historical_river_pulse_receipt_binds_only_dismissal_changes(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-river-pulse-dismissal-overlay-20261022.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "4cb09be62161eb53f52d575abefecd2624945ef442f2ad1b31149e7e70b26c25"
    receipt, expected = TOOL.reviewed_receipt()
    assert TOOL.RECEIPT.name == "site-v268-river-pulse-dismissal-overlay-20261022.json"
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-pirep-weather-parsing-overlay-20261022.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "8a1ae49ed41d78b9dc25ac97348b217ac4d0e9a91ccf8af7c179bb78bb930dcd"
    previous = json.loads(predecessor.read_text())
    changed = {"app/globals.css", "app/hydrology-observatory.tsx", "app/page.tsx",
               "docs/water-flow-paths.md", "tests/river-pulse-visuals.test.mjs"}
    assert set(receipt["comparison"]) == set(previous["comparison"])
    assert {name for name in receipt["comparison"]
            if receipt["comparison"][name] != previous["comparison"][name]} == changed
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == changed and len(receipt["repository_reconciliation"]["changes"]) == len(changed)
    for name in changed:
        entry, before = receipt["comparison"][name], previous["comparison"][name]
        # Bound to the receipt's own declaration: later successors (the Near-here dossier link) change current page.tsx bytes.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        assert entry["site_sha256"] == before["site_sha256"]
        assert entry["state"] == "inherited_repository_overlay"
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"], "mirror_sha256": digest,
            "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "counts", "inventory_sha256", "predecessor_receipt",
                      "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
                      "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    for key, count in previous["counts"].items():
        assert receipt["counts"][key] == count + {"identical": -3, "inherited_repository_overlay": 3}.get(key, 0)
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["review"]["human_acceptance"] is receipt["review"]["hosted_equivalence"] is False
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "e699ac0a2995ac26fd801fb493c03d03cbdd38c7"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_historical_privacy_receipt_binds_only_home_path_redactions(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-privacy-path-redaction-overlay-20261023.json")
    receipt, expected = TOOL.reviewed_receipt()
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "40e10139fc1eb7101fcecac2528c25c0330191ac3c69852ed28a1ff9fa6a879f"
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-river-pulse-dismissal-overlay-20261022.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "4cb09be62161eb53f52d575abefecd2624945ef442f2ad1b31149e7e70b26c25"
    previous = json.loads(predecessor.read_text())
    changed = {"docs/HISTORIC_ROAD_MAP_STUDY.md", "docs/basemap-cache.md", "docs/unified-download-workspace.md"}
    assert set(receipt["comparison"]) == set(previous["comparison"])
    assert {name for name in receipt["comparison"]
            if receipt["comparison"][name] != previous["comparison"][name]} == changed
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == changed and len(receipt["repository_reconciliation"]["changes"]) == len(changed)
    for name in changed:
        entry, before = receipt["comparison"][name], previous["comparison"][name]
        digest = hashlib.sha256((TOOL.DESTINATION / name).read_bytes()).hexdigest()
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        assert entry["site_sha256"] == before["site_sha256"]
        assert entry["state"] == "inherited_repository_overlay"
        assert "`/home/" not in (TOOL.DESTINATION / name).read_text()
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"], "mirror_sha256": digest,
            "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "counts", "inventory_sha256", "predecessor_receipt",
                      "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
                      "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    for key, count in previous["counts"].items():
        assert receipt["counts"][key] == count + {"identical": -3, "inherited_repository_overlay": 3}.get(key, 0)
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"]["source_and_overlay_review"] == "PENDING"
    assert receipt["review"]["human_acceptance"] is receipt["review"]["hosted_equivalence"] is False
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "ce0aed1abee79dbe5d0eb1f12aa71c633905e02f"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


DRONE_GRID_ADDED = {
    "app/aviation-drone-data.ts", "app/aviation-drone-server.ts", "app/api/aviation/uas-grid/route.ts", "app/api/aviation/tfrs/route.ts",
}
DRONE_GRID_CHANGED = {
    "app/aviation-control.tsx", "app/aviation-weather-server.ts", "app/site-architecture.ts", "app/site-features.ts",
    "docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md", "docs/aviation-layers.md", "tests/aviation.test.mjs",
}


def test_historical_drone_grid_receipt_binds_only_the_grid_and_tfr_overlay(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-aviation-drone-grid-tfr-overlay-20261024.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "058b11ff01dff3f692d79a74e96f610518799dee8f75fddf0aadbe2e4052aba1"
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-privacy-path-redaction-overlay-20261023.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "40e10139fc1eb7101fcecac2528c25c0330191ac3c69852ed28a1ff9fa6a879f"
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"]) | DRONE_GRID_ADDED
    assert not DRONE_GRID_ADDED & set(previous["comparison"])
    delta = {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"].get(name)}
    assert delta == DRONE_GRID_ADDED | DRONE_GRID_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == delta and len(receipt["repository_reconciliation"]["changes"]) == len(delta)
    for name in delta:
        entry, before = receipt["comparison"][name], previous["comparison"].get(name)
        # Bound to the receipt's own declaration: the grid-request fix successor
        # changes current bytes of two of these files, and the selected receipt records that.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        if before is None:
            assert entry["state"] == "repository_only_overlay" and entry["site_sha256"] is None
        else:
            assert entry["state"] == before["state"] and entry["site_sha256"] == before["site_sha256"], name
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"] if before else None,
            "repository_base_sha256": before["mirror_sha256"] if before else None,
            "mirror_sha256": digest, "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "counts", "inventory_sha256", "predecessor_receipt",
                      "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
                      "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    for key, count in previous["counts"].items():
        assert receipt["counts"][key] == count + {"repository_only_overlay": 4}.get(key, 0), key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"] == previous["review"] and receipt["overlay"] == previous["overlay"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "370e9ad30911fef806aa4fbd2ff25bea6eaf1626"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


DEPENDENCY_OVERRIDE_CHANGED = {"package.json", "package-lock.json"}


def test_historical_dependency_override_receipt_binds_only_the_two_dependency_files(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-fast-uri-undici-security-overlay-20261024.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "e5e6fd1bfb0d7143c0875295037e2e59dcf9deeb2aa1371dab5732e6cb8137f4"
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-aviation-drone-grid-tfr-overlay-20261024.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "058b11ff01dff3f692d79a74e96f610518799dee8f75fddf0aadbe2e4052aba1"
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"])
    delta = {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"][name]}
    assert delta == DEPENDENCY_OVERRIDE_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == delta and len(receipt["repository_reconciliation"]["changes"]) == len(delta)
    for name in delta:
        entry, before = receipt["comparison"][name], previous["comparison"][name]
        digest = hashlib.sha256((TOOL.DESTINATION / name).read_bytes()).hexdigest()
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        assert entry["state"] == before["state"] == "repository_safety_overlay"
        assert entry["site_sha256"] == before["site_sha256"]
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"],
            "mirror_sha256": digest, "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "inventory_sha256", "predecessor_receipt",
                      "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
                      "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"] == previous["review"] and receipt["overlay"] == previous["overlay"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "b9e90c5e7dd7800e337a29bed97a0bd3e14b23d1"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


def test_historical_uas_grid_request_fix_receipt_binds_only_the_fix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-aviation-uas-grid-request-fix-20261024.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "718e1730302527ceed7282bf62512c10d6c4cffa3c974d5e96ced21415eda2cf"
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-fast-uri-undici-security-overlay-20261024.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "e5e6fd1bfb0d7143c0875295037e2e59dcf9deeb2aa1371dab5732e6cb8137f4"
    previous = json.loads(predecessor.read_text())
    changed = {"app/aviation-control.tsx", "tests/aviation.test.mjs"}
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"])
    assert {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"][name]} == changed
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == changed and len(receipt["repository_reconciliation"]["changes"]) == len(changed)
    for name in changed:
        entry, before = receipt["comparison"][name], previous["comparison"][name]
        # Bound to the receipt's own declaration: the live-traffic successor changes current bytes of both files.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        assert entry["state"] == before["state"] == "repository_only_overlay" and entry["site_sha256"] is None
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"], "mirror_sha256": digest,
            "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "inventory_sha256", "predecessor_receipt", "predecessor_receipt_sha256",
                      "recorded_at", "repository_reconciled_base", "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    assert receipt["counts"] == previous["counts"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "e5ea665b351e13149dd09ff5d11d5bc27d928df8"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


LIVE_TRAFFIC_ADDED = {"app/aviation-traffic.ts", "app/aviation-traffic-server.ts", "app/api/aviation/traffic/route.ts"}
LIVE_TRAFFIC_CHANGED = {
    "app/aviation-airspace.ts", "app/aviation-control.tsx", "app/site-architecture.ts", "app/site-features.ts",
    "docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md", "docs/aviation-layers.md", "public/data/aviation/kansas-aviation-context.json",
    "tests/aviation.test.mjs",
}


def test_historical_live_traffic_receipt_binds_only_traffic_and_private_use_airports(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-aviation-live-traffic-private-airports-overlay-20261024.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "e5ef16580d831d16534402a8343d080188d3558e166bf57e876327744a3dfcd6"
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-aviation-uas-grid-request-fix-20261024.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "718e1730302527ceed7282bf62512c10d6c4cffa3c974d5e96ced21415eda2cf"
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"]) | LIVE_TRAFFIC_ADDED
    assert not LIVE_TRAFFIC_ADDED & set(previous["comparison"])
    delta = {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"].get(name)}
    assert delta == LIVE_TRAFFIC_ADDED | LIVE_TRAFFIC_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == delta and len(receipt["repository_reconciliation"]["changes"]) == len(delta)
    for name in delta:
        entry, before = receipt["comparison"][name], previous["comparison"].get(name)
        # Bound to the receipt's own declaration: the traffic expiry fix successor changes current bytes of several of these files.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        if before is None:
            assert entry["state"] == "repository_only_overlay" and entry["site_sha256"] is None
        else:
            assert entry["state"] == before["state"] and entry["site_sha256"] == before["site_sha256"], name
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"] if before else None,
            "repository_base_sha256": before["mirror_sha256"] if before else None,
            "mirror_sha256": digest, "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "counts", "inventory_sha256", "predecessor_receipt",
                      "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
                      "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    for key, count in previous["counts"].items():
        assert receipt["counts"][key] == count + {"repository_only_overlay": 3}.get(key, 0), key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"] == previous["review"] and receipt["overlay"] == previous["overlay"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "151e4f1bca7c3827683955f0fd15f4a7a18b5cfd"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


TRAFFIC_EXPIRY_CHANGED = {"app/aviation-control.tsx", "app/aviation-traffic.ts", "docs/aviation-layers.md", "tests/aviation.test.mjs"}


def test_historical_traffic_expiry_fix_receipt_binds_only_the_fix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-aviation-traffic-expiry-fix-20261024.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "a37218e4ca7dcab4859d3c2a6ed91ed4cef7e147c7bc40cf4c30916094ef1339"
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-aviation-live-traffic-private-airports-overlay-20261024.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "e5ef16580d831d16534402a8343d080188d3558e166bf57e876327744a3dfcd6"
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"])
    assert {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"][name]} == TRAFFIC_EXPIRY_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == TRAFFIC_EXPIRY_CHANGED and len(receipt["repository_reconciliation"]["changes"]) == len(TRAFFIC_EXPIRY_CHANGED)
    for name in TRAFFIC_EXPIRY_CHANGED:
        entry, before = receipt["comparison"][name], previous["comparison"][name]
        # Bound to the receipt's own declaration: the identity fix successor changes current bytes of two of these files.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        assert entry["state"] == before["state"] and entry["site_sha256"] == before["site_sha256"], name
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"], "mirror_sha256": digest,
            "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "inventory_sha256", "predecessor_receipt", "predecessor_receipt_sha256",
                      "recorded_at", "repository_reconciled_base", "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    assert receipt["counts"] == previous["counts"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "848461d0a5a9a844f920af9a266290ac6ac7d4eb"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


TRAFFIC_IDENTITY_CHANGED = {"app/aviation-traffic.ts", "tests/aviation.test.mjs"}


def test_historical_traffic_identity_fix_receipt_binds_only_the_fix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-aviation-traffic-identity-fix-20261024.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "80cbf64ded731867de68b7e0dd62ea51014581e3cf7274b7d3fac356670f515b"
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-aviation-traffic-expiry-fix-20261024.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "a37218e4ca7dcab4859d3c2a6ed91ed4cef7e147c7bc40cf4c30916094ef1339"
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"])
    assert {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"][name]} == TRAFFIC_IDENTITY_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == TRAFFIC_IDENTITY_CHANGED and len(receipt["repository_reconciliation"]["changes"]) == len(TRAFFIC_IDENTITY_CHANGED)
    for name in TRAFFIC_IDENTITY_CHANGED:
        entry, before = receipt["comparison"][name], previous["comparison"][name]
        # Bound to the receipt's own declaration: the TFR volume successor changes current bytes of the test file.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        assert entry["state"] == before["state"] and entry["site_sha256"] == before["site_sha256"], name
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"], "mirror_sha256": digest,
            "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "inventory_sha256", "predecessor_receipt", "predecessor_receipt_sha256",
                      "recorded_at", "repository_reconciled_base", "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    assert receipt["counts"] == previous["counts"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "0e434a0792ee80966e1411f49bc21c5e938e93df"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


TFR_VOLUMES_CHANGED = {
    "app/aviation-control.tsx", "app/aviation-drone-data.ts", "app/aviation-drone-server.ts", "app/aviation-weather-server.ts",
    "app/site-architecture.ts", "app/site-features.ts", "docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md", "docs/aviation-layers.md",
    "tests/aviation.test.mjs",
}


def test_historical_tfr_volumes_receipt_binds_only_the_tfr_volumes(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-aviation-tfr-volumes-20261024.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "57b1cdbc695bdd559f50f02346f4ddc448a43231b5e8de62080aaf4fe889380f"
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-aviation-traffic-identity-fix-20261024.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "80cbf64ded731867de68b7e0dd62ea51014581e3cf7274b7d3fac356670f515b"
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"])
    assert {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"][name]} == TFR_VOLUMES_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == TFR_VOLUMES_CHANGED and len(receipt["repository_reconciliation"]["changes"]) == len(TFR_VOLUMES_CHANGED)
    for name in TFR_VOLUMES_CHANGED:
        entry, before = receipt["comparison"][name], previous["comparison"][name]
        # Bound to the receipt's own declaration: the 2D chart successor changes current bytes of most of these files.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        assert entry["state"] == before["state"] and entry["site_sha256"] == before["site_sha256"], name
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"], "mirror_sha256": digest,
            "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "inventory_sha256", "predecessor_receipt", "predecessor_receipt_sha256",
                      "recorded_at", "repository_reconciled_base", "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    assert receipt["counts"] == previous["counts"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "9678e903c7cf620373afc26170070a32c2da5e75"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


CHART_2D_ADDED = {"app/aviation-chart.ts", "app/aviation-profile.ts"}
CHART_2D_CHANGED = {
    "app/aviation-airspace.ts", "app/aviation-control.tsx", "app/aviation-drone-data.ts", "app/aviation-traffic.ts",
    "app/site-architecture.ts", "app/site-features.ts", "docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md", "docs/aviation-layers.md",
    "tests/aviation.test.mjs",
}


def test_historical_2d_chart_receipt_binds_only_the_2d_chart(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-aviation-2d-chart-20261025.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "0608a4ae27a0bf3e84f758db1fcb1d530808a8b81b078970794b8c87c50da31f"
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-aviation-tfr-volumes-20261024.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "57b1cdbc695bdd559f50f02346f4ddc448a43231b5e8de62080aaf4fe889380f"
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"]) | CHART_2D_ADDED
    assert not CHART_2D_ADDED & set(previous["comparison"])
    delta = {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"].get(name)}
    assert delta == CHART_2D_ADDED | CHART_2D_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == delta and len(receipt["repository_reconciliation"]["changes"]) == len(delta)
    for name in delta:
        entry, before = receipt["comparison"][name], previous["comparison"].get(name)
        # Bound to the receipt's own declaration: the Near-here successor changes current bytes of several of these files.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        if before is None:
            assert entry["state"] == "repository_only_overlay" and entry["site_sha256"] is None
        else:
            assert entry["state"] == before["state"] and entry["site_sha256"] == before["site_sha256"], name
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"] if before else None,
            "repository_base_sha256": before["mirror_sha256"] if before else None,
            "mirror_sha256": digest, "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "counts", "inventory_sha256", "predecessor_receipt",
                      "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
                      "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    for key, count in previous["counts"].items():
        assert receipt["counts"][key] == count + {"repository_only_overlay": 2}.get(key, 0), key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"] == previous["review"] and receipt["overlay"] == previous["overlay"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "4fd89b28a37211e47a9d5eae9934272fc64f896f"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


NEAR_HERE_ADDED = {"app/aviation-research.ts"}
NEAR_HERE_CHANGED = {
    "app/aviation-control.tsx", "app/page.tsx", "app/site-architecture.ts", "app/site-features.ts",
    "docs/SITE_FEATURE_CONNECTION_ACTION_MAP.md", "docs/aviation-layers.md", "docs/map-research-tools.md", "tests/aviation.test.mjs",
}


def test_historical_near_here_receipt_binds_only_the_dossier_link(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(TOOL, "RECEIPT", ROOT / "data/receipts/generated/site-v268-aviation-near-here-dossier-20261025.json")
    assert hashlib.sha256(TOOL.RECEIPT.read_bytes()).hexdigest() == "0bbc3d604015b3047dc232ff5e826c41fd60a1abbbde89105a14c98c850a7cf3"
    receipt, expected = TOOL.reviewed_receipt()
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-aviation-2d-chart-20261025.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "0608a4ae27a0bf3e84f758db1fcb1d530808a8b81b078970794b8c87c50da31f"
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"]) | NEAR_HERE_ADDED
    assert not NEAR_HERE_ADDED & set(previous["comparison"])
    delta = {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"].get(name)}
    assert delta == NEAR_HERE_ADDED | NEAR_HERE_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == delta and len(receipt["repository_reconciliation"]["changes"]) == len(delta)
    for name in delta:
        entry, before = receipt["comparison"][name], previous["comparison"].get(name)
        # Bound to the receipt's own declaration: the dossier Inspect fix changes current bytes of several of these files.
        digest = declarations[name]["mirror_sha256"]
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        if before is None:
            assert entry["state"] == "repository_only_overlay" and entry["site_sha256"] is None
        elif before["state"] == "identical":
            # A previously identical Site file becomes an inherited repository overlay; its Site hash is preserved.
            assert entry["state"] == "inherited_repository_overlay" and entry["site_sha256"] == before["site_sha256"], name
        else:
            assert entry["state"] == before["state"] and entry["site_sha256"] == before["site_sha256"], name
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"] if before else None,
            "repository_base_sha256": before["mirror_sha256"] if before else None,
            "mirror_sha256": digest, "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "counts", "inventory_sha256", "predecessor_receipt",
                      "predecessor_receipt_sha256", "recorded_at", "repository_reconciled_base",
                      "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    for key, count in previous["counts"].items():
        assert receipt["counts"][key] == count + {"repository_only_overlay": 1, "identical": -1, "inherited_repository_overlay": 1}.get(key, 0), key
    assert receipt["status"] == "REVIEW_ONLY"
    assert receipt["review"] == previous["review"] and receipt["overlay"] == previous["overlay"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "d08e613d2cbf41af929a9f4b377b6694035b5ca5"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]


DOSSIER_INSPECT_CHANGED = {"app/aviation-control.tsx", "app/page.tsx", "docs/aviation-layers.md", "docs/map-research-tools.md", "tests/aviation.test.mjs"}


def test_selected_receipt_binds_only_the_dossier_inspect_fix() -> None:
    receipt, expected = TOOL.reviewed_receipt()
    assert TOOL.RECEIPT.name == "site-v268-aviation-dossier-inspect-20261025.json"
    predecessor = ROOT / "data/receipts/generated" / receipt["predecessor_receipt"]
    assert predecessor.name == "site-v268-aviation-near-here-dossier-20261025.json"
    assert hashlib.sha256(predecessor.read_bytes()).hexdigest() == receipt["predecessor_receipt_sha256"] == "0bbc3d604015b3047dc232ff5e826c41fd60a1abbbde89105a14c98c850a7cf3"
    previous = json.loads(predecessor.read_text())
    assert set(receipt) == set(previous)
    assert set(receipt["comparison"]) == set(previous["comparison"])
    assert {name for name, entry in receipt["comparison"].items() if entry != previous["comparison"][name]} == DOSSIER_INSPECT_CHANGED
    declarations = {entry["path"]: entry for entry in receipt["repository_reconciliation"]["changes"]}
    assert set(declarations) == DOSSIER_INSPECT_CHANGED and len(receipt["repository_reconciliation"]["changes"]) == len(DOSSIER_INSPECT_CHANGED)
    for name in DOSSIER_INSPECT_CHANGED:
        entry, before = receipt["comparison"][name], previous["comparison"][name]
        digest = hashlib.sha256((TOOL.DESTINATION / name).read_bytes()).hexdigest()
        assert entry["mirror_sha256"] == digest and expected[name] == "sha256:" + digest
        assert entry["state"] == before["state"] and entry["site_sha256"] == before["site_sha256"], name
        assert declarations[name] == {
            "path": name, "previous_receipt_sha256": before["mirror_sha256"],
            "repository_base_sha256": before["mirror_sha256"], "mirror_sha256": digest,
            "state": entry["state"], "proposed_in_this_change": True,
        }
    administrative = {"comparison", "inventory_sha256", "predecessor_receipt", "predecessor_receipt_sha256",
                      "recorded_at", "repository_reconciled_base", "repository_reconciliation", "rollback", "security", "validation"}
    for key in previous.keys() - administrative:
        assert receipt[key] == previous[key], key
    assert receipt["counts"] == previous["counts"]
    assert receipt["repository_reconciled_base"] == receipt["repository_reconciliation"]["base_commit"] == "965b8783c171a14275e9b25e1ef84c0b174fb9f8"
    assert receipt["repository_reconciliation"]["authority"] == "CONTENT_PARITY_ONLY"
    assert receipt["repository_reconciliation"]["restored_recorded_paths"] == []
    inventory = {name: entry["mirror_sha256"] for name, entry in receipt["comparison"].items()}
    assert receipt["inventory_sha256"] == hashlib.sha256(json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert predecessor.name in receipt["rollback"]["mirror"]
