"""Currentness checks preserve source-specific mutable and held states."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path

import pytest

from tools.local_data import audit_curation_drift


def baseline(path: Path, raw: Path, *, mutable: bool = False) -> tuple[str, dict]:
    stat = path.stat()
    relative = path.relative_to(raw).as_posix()
    return relative, {
        "collection": relative.split("/", 1)[0],
        "size_bytes": str(stat.st_size),
        "mtime_ns": str(stat.st_mtime_ns),
        "sha256": "" if mutable else hashlib.sha256(path.read_bytes()).hexdigest(),
        "hash_state": "active_mutable_file" if mutable else "sha256_verified",
    }


def test_new_changed_and_missing_files_are_distinguished(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    folder = raw / "Kansas Road Maps"
    folder.mkdir(parents=True)
    same = folder / "same.pdf"
    changed = folder / "changed.pdf"
    missing = folder / "missing.pdf"
    for path in (same, changed, missing):
        path.write_bytes(b"original")
    previous = dict(baseline(path, raw) for path in (same, changed, missing))
    changed.write_bytes(b"new content")
    missing.unlink()
    (folder / "added.pdf").write_bytes(b"new edition")
    before = {p.name: p.read_bytes() for p in folder.iterdir()}
    result = audit_curation_drift.audit(raw, previous)
    after = {p.name: p.read_bytes() for p in folder.iterdir()}
    assert result["status"] == "SOURCE_DRIFT_REVIEW"
    assert result["change_counts"] == {
        "added_hashed": 1, "content_changed_hashed": 1, "missing_since_snapshot": 1,
    }
    assert result["by_collection"]["Kansas Road Maps"]["unchanged_stat_only"] == 1
    assert before == after


def test_stat_change_with_same_bytes_is_not_content_change(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    folder = raw / "TIGER data"
    folder.mkdir(parents=True)
    path = folder / "county.zip"
    path.write_bytes(b"same bytes")
    previous = dict([baseline(path, raw)])
    stat = path.stat()
    os.utime(path, ns=(stat.st_atime_ns, stat.st_mtime_ns + 1_000_000))
    result = audit_curation_drift.audit(raw, previous)
    assert result["change_counts"] == {"metadata_changed_bytes_same": 1}


def test_mutable_work_files_and_symlinks_are_held(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    folder = raw / "PRISM data/Kansas/work"
    folder.mkdir(parents=True)
    old = folder / "old.part"
    old.write_bytes(b"in progress")
    previous = dict([baseline(old, raw, mutable=True)])
    old.unlink()
    (folder / "new.part").write_bytes(b"in progress")
    (folder / "linked.part").symlink_to(tmp_path / "outside")
    result = audit_curation_drift.audit(raw, previous)
    assert result["change_counts"] == {
        "added_active_mutable": 1, "file_symlink_held": 1,
        "missing_since_snapshot": 1,
    }
    assert not (tmp_path / "outside").exists()


def test_baseline_rejects_escape_and_duplicate_paths(tmp_path: Path) -> None:
    import gzip

    path = tmp_path / "inventory.csv.gz"
    header = "original_path,collection,size_bytes,mtime_ns,sha256,hash_state\n"
    row = "../escape,Kansas Road Maps,1,2,abcd,sha256_verified\n"
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        handle.write(header + row)
    with pytest.raises(audit_curation_drift.review_curation.Held, match="INVALID_SOURCE_INVENTORY"):
        audit_curation_drift._load_baseline(path)
