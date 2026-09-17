"""Independent CLI regressions for explicit offline batch composition and review."""

from copy import deepcopy
import hashlib
import json
import shutil
import socket
import subprocess
import sys

import pytest

from tools.local_data import manage


@pytest.fixture
def batch(tmp_path):
    downloads = tmp_path / "downloads"
    downloads.mkdir()
    items = []
    paths = []
    for index, (name, data, source) in enumerate([
        ("maps/county.bin", b"independent opaque map bytes\n", "map-provider"),
        ("pictures/archive.bin", b"independent opaque picture bytes\n", "photo-provider"),
    ]):
        payload = downloads / name
        payload.parent.mkdir(parents=True, exist_ok=True)
        payload.write_bytes(data)
        item = {
            "source_id": source,
            "dataset_id": "county-records",
            "domain": "history",
            "version": "v1",
            "relative_path": name,
            "source_uri": "file-ref:independent-batch-fixture",
            "media_type": "application/octet-stream",
            "rights": {"license_id": None, "redistribution": "unknown"},
            "sensitivity": "unknown",
            "sha256": hashlib.sha256(data).hexdigest(),
            "size_bytes": len(data),
            "captured_at": "2026-09-17T00:00:00Z",
        }
        path = tmp_path / f"selected-{index}.json"
        write_manifest(path, [item])
        items.append(item)
        paths.append(path)
    return tmp_path, downloads, items, paths


def write_manifest(path, items):
    path.write_bytes(manage.canonical({"schema_version": "1", "items": items}))
    return path


def invoke(capsys, argv):
    code = manage.main([str(value) for value in argv])
    output = capsys.readouterr()
    if code:
        assert output.out == "", "failure must never masquerade as usable manifest/report JSON"
        result = json.loads(output.err)
        assert result["outcome"] == "DENY"
    else:
        assert output.err == ""
        result = json.loads(output.out)
    return code, result, output.out


def test_combined_manifest_drives_multi_source_capture_and_restored_replay(batch, capsys):
    base, downloads, items, paths = batch
    # Exercise the executable entry point, not just the combination helper.
    command = [sys.executable, str(manage.REPO_ROOT / "tools/local_data/manage.py"), "combine"]
    for path in paths:
        command += ["--manifest", str(path)]
    combined = subprocess.run(command, check=False, text=True, capture_output=True)
    assert combined.returncode == 0, combined.stderr
    assert combined.stderr == ""
    manifest = json.loads(combined.stdout)
    assert len(manifest["items"]) == 2
    selected = base / "combined.json"
    selected.write_text(combined.stdout)
    root = base / "store"
    assert manage.main(["init", "--root", str(root)]) == 0
    capsys.readouterr()
    assert manage.main([
        "sync", "--root", str(root), "--manifest", str(selected),
        "--downloads", str(downloads), "--min-free-bytes", "0",
    ]) == 0
    captured = json.loads(capsys.readouterr().out)
    assert captured["captured_objects"] == 2
    assert captured["lifecycle"] == "QUARANTINE"
    restored = base / "restored"
    shutil.copytree(root, restored)
    shutil.rmtree(downloads)
    retained = manage.full_manifest_path(restored, captured["run_id"])
    assert manage.main(["verify", "--root", str(restored), "--manifest", str(retained)]) == 0
    assert json.loads(capsys.readouterr().out)["outcome"] == "VERIFIED"
    for item in items:
        assert manage.payload_path(restored, item).is_file()


def test_combine_is_order_independent_and_preserves_restricted_assertions(batch, capsys):
    _, _, items, paths = batch
    items[1]["rights"] = {"license_id": "private-archive-license", "redistribution": "restricted"}
    items[1]["sensitivity"] = "controlled"
    write_manifest(paths[1], [items[1]])
    first = invoke(capsys, ["combine", "--manifest", paths[0], "--manifest", paths[1]])
    second = invoke(capsys, ["combine", "--manifest", paths[1], "--manifest", paths[0]])
    assert first[0] == second[0] == 0
    assert first[2] == second[2]
    assert first[2].encode() == manage.canonical(first[1])
    assert first[1]["items"][1] == items[1]


@pytest.mark.parametrize("operation", ["combine", "compare"])
def test_metadata_operations_do_not_read_payloads_touch_store_or_call_network(batch, capsys, monkeypatch, operation):
    base, downloads, _, paths = batch
    shutil.rmtree(downloads)
    before = {path.relative_to(base): path.read_bytes() for path in base.rglob("*") if path.is_file()}

    def forbidden(*args, **kwargs):
        raise AssertionError("metadata-only operation crossed its declared boundary")

    for name in ("external_root", "hash_regular", "capture_file", "write_new", "inspect_objects"):
        monkeypatch.setattr(manage, name, forbidden)
    monkeypatch.setattr(socket, "socket", forbidden)
    monkeypatch.setattr(subprocess, "run", forbidden)
    monkeypatch.setenv("KFM_DATA_ROOT", str(base / "must-not-be-created"))
    arguments = (["combine", "--manifest", paths[0], "--manifest", paths[1]] if operation == "combine"
                 else ["compare", "--previous", paths[0], "--manifest", paths[1]])
    assert invoke(capsys, arguments)[0] == 0
    after = {path.relative_to(base): path.read_bytes() for path in base.rglob("*") if path.is_file()}
    assert before == after
    assert not (base / "must-not-be-created").exists()


@pytest.mark.parametrize("operation", ["combine", "compare"])
def test_manifest_symlink_is_denied_without_stdout(batch, capsys, operation):
    base, _, _, paths = batch
    link = base / "alias.json"
    link.symlink_to(paths[0])
    arguments = (["combine", "--manifest", link, "--manifest", paths[1]] if operation == "combine"
                 else ["compare", "--previous", link, "--manifest", paths[1]])
    assert invoke(capsys, arguments)[0] == 1


@pytest.mark.parametrize("invalid", ["duplicate-key", "float", "nonfinite"])
@pytest.mark.parametrize("operation", ["combine", "compare"])
def test_noncanonical_json_values_are_denied(batch, capsys, invalid, operation):
    _, _, _, paths = batch
    text = paths[0].read_text()
    if invalid == "duplicate-key":
        text = text.replace('"schema_version":"1"', '"schema_version":"1","schema_version":"1"')
    elif invalid == "float":
        # Keep the fixture length independent of future edits to its payload.
        value = json.loads(paths[0].read_bytes())
        size = value["items"][0]["size_bytes"]
        text = paths[0].read_text().replace(f'"size_bytes":{size}', f'"size_bytes":{size}.0')
    else:
        value = json.loads(paths[0].read_bytes())
        size = value["items"][0]["size_bytes"]
        text = text.replace(f'"size_bytes":{size}', '"size_bytes":NaN')
    paths[0].write_text(text)
    arguments = (["combine", "--manifest", paths[0], "--manifest", paths[1]] if operation == "combine"
                 else ["compare", "--previous", paths[0], "--manifest", paths[1]])
    assert invoke(capsys, arguments)[0] == 1


def test_combine_refuses_duplicate_items_even_across_different_input_files(batch, capsys):
    _, _, items, paths = batch
    write_manifest(paths[1], [items[0]])
    code, result, _ = invoke(capsys, ["combine", "--manifest", paths[0], "--manifest", paths[1]])
    assert code == 1
    assert result["code"] == "DUPLICATE_ITEM"


def test_combine_cannot_resolve_conflicting_declarations_for_one_download_path(batch, capsys):
    _, _, items, paths = batch
    conflicting = deepcopy(items[1])
    conflicting["relative_path"] = items[0]["relative_path"]
    write_manifest(paths[1], [conflicting])
    code, result, _ = invoke(capsys, ["combine", "--manifest", paths[0], "--manifest", paths[1]])
    assert code == 1
    assert result["code"] == "INPUT_PATH_CONFLICT"


@pytest.mark.parametrize("limit", ["items", "file", "total"])
def test_combine_enforces_limits_on_the_result(batch, capsys, limit):
    _, _, items, paths = batch
    option, value = {
        "items": ("--max-items", 1),
        "file": ("--max-file-bytes", items[0]["size_bytes"] - 1),
        "total": ("--max-total-bytes", max(item["size_bytes"] for item in items)),
    }[limit]
    assert invoke(capsys, ["combine", "--manifest", paths[0], "--manifest", paths[1], option, value])[0] == 1


def test_combine_bounds_aggregate_raw_input_even_when_each_manifest_is_small(batch, capsys):
    _, _, _, paths = batch
    for path in paths:
        path.write_bytes(b" " * (2 * 1024 * 1024) + path.read_bytes())
        assert path.stat().st_size < manage.MAX_MANIFEST_BYTES
    code, result, _ = invoke(capsys, ["combine", "--manifest", paths[0], "--manifest", paths[1]])
    assert code == 1
    assert result["code"] == "METADATA_BYTE_LIMIT"


def test_combine_requires_a_bounded_explicit_input_list(batch, capsys):
    _, _, _, paths = batch
    assert invoke(capsys, ["combine", "--manifest", paths[0]])[0] == 1
    arguments = ["combine"]
    for _ in range(1001):
        arguments.extend(["--manifest", paths[0]])
    assert invoke(capsys, arguments)[0] == 1


def test_compare_covers_changed_unchanged_added_and_omitted_without_deletion(batch, capsys):
    base, _, items, paths = batch
    old = deepcopy(items)
    unchanged = deepcopy(items[0])
    unchanged["relative_path"] = "maps/unchanged.bin"
    old.append(unchanged)
    write_manifest(paths[0], old)
    current = deepcopy(items[0])
    current["version"] = "v2"
    current["captured_at"] = "2026-09-18T00:00:00Z"
    current["sha256"] = hashlib.sha256(b"new map content").hexdigest()
    current["size_bytes"] = len(b"new map content")
    added = deepcopy(items[1])
    added["relative_path"] = "pictures/new.bin"
    write_manifest(paths[1], [added, unchanged, current])
    code, report, _ = invoke(capsys, ["compare", "--previous", paths[0], "--manifest", paths[1]])
    assert code == 0
    assert report["outcome"] == "COMPARED"
    assert report["counts"] == {"added": 1, "omitted": 1, "changed": 1, "unchanged": 1, "version_conflicts": 0}
    assert report["writes"] is report["deletions"] is report["byte_verification"] is False
    assert all(value is False for value in report["authority"].values())
    changes = {entry["status"]: entry for entry in report["changes"]}
    assert changes["CHANGED"]["payload_changed"] is True
    assert changes["CHANGED"]["changed_fields"] == ["captured_at", "sha256", "size_bytes", "version"]
    assert changes["UNCHANGED"]["changed_fields"] == []
    assert changes["UNCHANGED"]["payload_changed"] is False
    assert changes["OMITTED"]["proposed_version"] is None
    assert changes["ADDED"]["previous_version"] is None
    assert changes["OMITTED"]["payload_changed"] is None
    assert changes["ADDED"]["payload_changed"] is None
    assert all(not entry["version_conflict"] for entry in report["changes"])
    assert report["previous_run_id"] != report["proposed_run_id"]
    assert not (base / "store").exists()


@pytest.mark.parametrize("field,replacement", [
    ("rights", {"license_id": "restricted-record", "redistribution": "denied"}),
    ("sensitivity", "restricted"),
    ("captured_at", "2026-09-18T00:00:00Z"),
    ("sha256", "a" * 64),
    ("size_bytes", 50),
])
def test_compare_reports_conflicting_reuse_of_the_same_revision(batch, capsys, field, replacement):
    _, _, items, paths = batch
    changed = deepcopy(items[0])
    changed[field] = replacement
    write_manifest(paths[1], [changed])
    code, report, _ = invoke(capsys, ["compare", "--previous", paths[0], "--manifest", paths[1]])
    assert code == 0, "a successful review report may identify a capture conflict"
    assert report["counts"]["version_conflicts"] == 1
    change = report["changes"][0]
    assert change["status"] == "CHANGED"
    assert change["version_conflict"] is True
    assert change["changed_fields"] == [field]
    assert change["payload_changed"] is (field in {"sha256", "size_bytes"})


def test_compare_identical_manifests_is_metadata_noop(batch, capsys):
    _, _, _, paths = batch
    code, report, _ = invoke(capsys, ["compare", "--previous", paths[0], "--manifest", paths[0]])
    assert code == 0
    assert report["previous_run_id"] == report["proposed_run_id"]
    assert report["counts"] == {"added": 0, "omitted": 0, "changed": 0, "unchanged": 1, "version_conflicts": 0}
    assert report["byte_verification"] is False


@pytest.mark.parametrize("side", ["previous", "proposed"])
def test_compare_refuses_ambiguous_multiple_versions_of_one_logical_file(batch, capsys, side):
    base, _, items, paths = batch
    older = deepcopy(items[0])
    older["version"] = "v0"
    ambiguous = write_manifest(base / "ambiguous.json", [older, items[0]])
    previous, proposed = (ambiguous, paths[0]) if side == "previous" else (paths[0], ambiguous)
    code, report, _ = invoke(capsys, ["compare", "--previous", previous, "--manifest", proposed])
    assert code == 1
    assert report["code"] == "AMBIGUOUS_COMPARISON_VERSION"
