"""Independent acceptance checks for offline capture and recovery boundaries."""

from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path

import pytest

from tools.local_data import manage


@pytest.fixture
def capture(tmp_path):
    downloads = tmp_path / "downloads"
    downloads.mkdir()
    payload = b"independent quarantine capture\n"
    (downloads / "map.bin").write_bytes(payload)
    item = {
        "source_id": "independent-source",
        "dataset_id": "independent-dataset",
        "domain": "cross-domain",
        "version": "v1",
        "relative_path": "map.bin",
        "source_uri": "file-ref:independent-fixture",
        "media_type": "application/octet-stream",
        "rights": {"license_id": None, "redistribution": "unknown"},
        "sensitivity": "unknown",
        "sha256": hashlib.sha256(payload).hexdigest(),
        "size_bytes": len(payload),
        "captured_at": "2026-09-17T00:00:00Z",
    }
    manifest = {"schema_version": "1", "items": [item]}
    manifest_file = tmp_path / "manifest.json"
    manifest_file.write_bytes(manage.canonical(manifest))
    root = tmp_path / "store"
    args = manage.parser().parse_args([
        "sync", "--root", str(root), "--manifest", str(manifest_file),
        "--downloads", str(downloads), "--min-free-bytes", "0",
    ])
    return root, downloads, manifest, manifest_file, args


@pytest.mark.skipif(os.name != "posix", reason="POSIX double-slash alias")
def test_double_slash_cannot_place_store_inside_checkout():
    alias = "//" + str(manage.REPO_ROOT).lstrip("/") + "/private-local-store"
    assert manage.REPO_ROOT in Path(alias).resolve().parents
    with pytest.raises(ValueError):
        manage.external_root(alias)


@pytest.mark.skipif(os.name != "posix", reason="POSIX double-slash alias")
def test_double_slash_cannot_use_store_as_download_directory(capture):
    root, _, _, _, _ = capture
    manage.init_store(root)
    alias = "//" + str(root).lstrip("/")
    with pytest.raises(ValueError):
        manage.downloads_root(alias, root)


def test_plan_on_missing_store_does_not_create_files(capture, capsys):
    root, downloads, _, manifest_file, _ = capture
    before = sorted(str(path) for path in root.parent.rglob("*"))
    assert manage.main([
        "plan", "--root", str(root), "--downloads", str(downloads),
        "--manifest", str(manifest_file), "--min-free-bytes", "0",
    ]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["outcome"] == "PLANNED"
    assert report["writes"] is False
    assert not root.exists()
    assert sorted(str(path) for path in root.parent.rglob("*")) == before


def test_corrupt_existing_object_is_never_overwritten(capture):
    root, downloads, manifest, _, args = capture
    manage.init_store(root)
    assert manage.sync_store(root, manifest, downloads, args)["outcome"] == "SYNCED"
    destination = manage.payload_path(root, manifest["items"][0])
    corrupt = b"!" * manifest["items"][0]["size_bytes"]
    destination.write_bytes(corrupt)
    with pytest.raises(ValueError, match="STORED_PAYLOAD_CORRUPT"):
        manage.sync_store(root, manifest, downloads, args)
    assert destination.read_bytes() == corrupt


def test_metadata_failure_emits_partial_then_retry_recovers_without_download(capture, monkeypatch):
    root, downloads, manifest, _, args = capture
    manage.init_store(root)
    write_new = manage.write_new

    def fail_manifest_once(path, content):
        if path.name == "manifest.json":
            raise OSError("simulated metadata I/O failure")
        return write_new(path, content)

    monkeypatch.setattr(manage, "write_new", fail_manifest_once)
    with pytest.raises(OSError):
        manage.sync_store(root, manifest, downloads, args)
    attempts = list((root / "data/receipts/ingest/local-upload").rglob("attempts/*.json"))
    assert len(attempts) == 1
    partial = json.loads(attempts[0].read_bytes())
    assert partial["outcome"] == "PARTIAL"
    assert partial["bytes_in"] == manifest["items"][0]["size_bytes"]
    assert not list((root / "data/receipts").rglob("ingest-receipt.json"))
    (downloads / "map.bin").unlink()
    monkeypatch.setattr(manage, "write_new", write_new)
    retry = manage.sync_store(root, manifest, downloads, args)
    assert retry["outcome"] == "SYNCED"
    assert retry["captured_objects"] == 0
    assert retry["reused_objects"] == 1
    assert manage.check_snapshots(root, manifest, required=True) == []
    assert json.loads(attempts[0].read_bytes()) == partial


def test_same_version_cannot_replace_prior_identity(capture):
    root, downloads, manifest, _, args = capture
    manage.init_store(root)
    manage.sync_store(root, manifest, downloads, args)
    original = manage.payload_path(root, manifest["items"][0]).read_bytes()
    replacement = b"changed source revision\n"
    candidate = deepcopy(manifest)
    candidate["items"][0]["sha256"] = hashlib.sha256(replacement).hexdigest()
    candidate["items"][0]["size_bytes"] = len(replacement)
    (downloads / "map.bin").write_bytes(replacement)
    with pytest.raises(ValueError, match="CAPTURE_VERSION_CONFLICT"):
        manage.sync_store(root, candidate, downloads, args)
    assert manage.payload_path(root, manifest["items"][0]).read_bytes() == original
    assert not manage.payload_path(root, candidate["items"][0]).exists()


def test_final_capture_rechecks_input_after_preflight(capture, monkeypatch):
    root, downloads, manifest, _, args = capture
    manage.init_store(root)
    capture_file = manage.capture_file

    def replace_input_after_plan(source, destination, **kwargs):
        source.write_bytes(b"!" * manifest["items"][0]["size_bytes"])
        return capture_file(source, destination, **kwargs)

    monkeypatch.setattr(manage, "capture_file", replace_input_after_plan)
    with pytest.raises(ValueError, match="INPUT_DIGEST_OR_SIZE_MISMATCH"):
        manage.sync_store(root, manifest, downloads, args)
    assert not manage.payload_path(root, manifest["items"][0]).exists()
    assert not list((root / "data/receipts").rglob("ingest-receipt.json"))
    assert not list(root.rglob(".capture-*"))


@pytest.mark.parametrize("override", [
    ["--file", "../outside.bin"],
    ["--source-uri", "https://user:password@example.org/file"],
    ["--version", "../../changed"],
])
def test_describe_rejects_unsafe_metadata_before_read_and_keeps_stdout_empty(
    capture, monkeypatch, capsys, override,
):
    _, downloads, _, _, _ = capture

    def forbidden(*args, **kwargs):
        raise AssertionError("unsafe description reached payload hashing")

    monkeypatch.setattr(manage, "hash_regular", forbidden)
    code = manage.main([
        "describe", "--downloads", str(downloads), "--file", "map.bin",
        "--source-id", "provider", "--dataset-id", "maps", "--domain", "geology",
        "--version", "v1", "--source-uri", "file-ref:independent-description",
        *override,
    ])
    output = capsys.readouterr()
    assert code == 1
    assert output.out == ""
    assert json.loads(output.err)["outcome"] == "DENY"
