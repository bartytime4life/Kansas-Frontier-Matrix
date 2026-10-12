"""Bounded background metadata inventory of an existing private local store.

Only regular-file metadata is inspected. No payload, credential, source registry,
or release record is read; the result cannot establish coverage or admission.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import errno
import hashlib
import os
from pathlib import Path
import re
import stat
import threading
import time


LANES = {"raw": "stored-candidate", "work": "review-material",
         "quarantine": "stored-candidate", "processed": "archive-context"}
EXCLUDED_DIRECTORIES = {"runtime", "runtimes", "venv", "node_modules", "__pycache__",
                        "earth-engine-downloads", "credentials", "secrets"}
EXCLUDED_FILES = {"credentials.json", "credential.json", "token.json", "tokens.json",
                  "config.json", "client_secret.json", "client_secrets.json"}
DIRECTORY_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW


@dataclass(frozen=True)
class ScanLimits:
    entries: int = 500_000
    collections: int = 256
    depth: int = 32
    seconds: float = 30.0


class LibraryScanError(ValueError):
    pass


def _error(error):
    if isinstance(error, LibraryScanError) and str(error) in {"LIBRARY_SCAN_LIMIT", "LIBRARY_SCAN_FAILED", "LIBRARY_SCAN_UNSAFE", "LIBRARY_SCAN_CHANGED"}:
        return str(error)
    if isinstance(error, OSError) and error.errno in (errno.ELOOP, errno.ENOTDIR):
        return "LIBRARY_SCAN_UNSAFE"
    if isinstance(error, OSError) and error.errno == errno.ENOENT:
        return "LIBRARY_SCAN_CHANGED"
    return "LIBRARY_SCAN_FAILED"


def _open_root(root):
    """Anchor every component to a descriptor: never follow a swapped symlink."""
    if not root.is_absolute() or ".." in root.parts:
        raise LibraryScanError("LIBRARY_SCAN_UNSAFE")
    descriptor = os.open(root.anchor, DIRECTORY_FLAGS)
    try:
        for part in root.parts[1:]:
            child = os.open(part, DIRECTORY_FLAGS, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        info = os.fstat(descriptor)
        if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
            raise LibraryScanError("LIBRARY_SCAN_UNSAFE")
        return descriptor
    except BaseException:
        os.close(descriptor)
        raise


def scan_library(root: Path, progress=lambda _count: None, *, limits=ScanLimits(), clock=time.monotonic):
    """Return only a complete bounded summary; errors never return partial totals."""
    started = clock()
    visited = files = total_bytes = 0
    collections = {}

    def tick():
        nonlocal visited
        visited += 1
        if visited > limits.entries or clock() - started > limits.seconds:
            raise LibraryScanError("LIBRARY_SCAN_LIMIT")
        if visited % 128 == 0:
            progress(files)

    def collection(lane, name):
        key = (lane, name)
        if key not in collections:
            if len(collections) >= limits.collections:
                raise LibraryScanError("LIBRARY_SCAN_LIMIT")
            label = re.sub(r"[\x00-\x1f\x7f\\]", " ", name).strip()[:120] if name else f"Other {lane} files"
            collections[key] = {"id": hashlib.sha256((lane + "\0" + name).encode()).hexdigest(),
                                "label": label or "Local collection", "lane": lane, "files": 0,
                                "bytes": 0, "role": LANES[lane]}
            match = re.fullmatch(r"earth-engine/(ee-[a-z0-9-]+)/([0-9]{4}|fixed)", name)
            if lane == "raw" and match:
                collections[key].update(dataset=match[1], period=match[2], label=f"{match[1]} · {match[2]}")
        return collections[key]

    def walk(descriptor, lane, group=None, depth=0):
        nonlocal files, total_bytes
        if depth > limits.depth:
            raise LibraryScanError("LIBRARY_SCAN_LIMIT")
        before = os.fstat(descriptor)
        with os.scandir(descriptor) as iterator:
            for entry in iterator:
                tick()
                lowered = entry.name.lower()
                # Exclude private/runtime names before any stat or traversal.
                if entry.name.startswith(".") or lowered in EXCLUDED_DIRECTORIES or lowered in EXCLUDED_FILES:
                    continue
                info = entry.stat(follow_symlinks=False)
                if stat.S_ISLNK(info.st_mode) or not (stat.S_ISREG(info.st_mode) or stat.S_ISDIR(info.st_mode)):
                    raise LibraryScanError("LIBRARY_SCAN_UNSAFE")
                if stat.S_ISDIR(info.st_mode):
                    name = entry.name if group is None else group
                    if lane == "raw" and group == "earth-engine" and re.fullmatch(r"ee-[a-z0-9-]+", entry.name):
                        name = group + "/" + entry.name
                    elif lane == "raw" and group and re.fullmatch(r"earth-engine/ee-[a-z0-9-]+", group) and re.fullmatch(r"[0-9]{4}|fixed", entry.name):
                        name = group + "/" + entry.name
                    child = os.open(entry.name, DIRECTORY_FLAGS, dir_fd=descriptor)
                    try:
                        opened = os.fstat(child)
                        if (opened.st_dev, opened.st_ino) != (info.st_dev, info.st_ino):
                            raise LibraryScanError("LIBRARY_SCAN_CHANGED")
                        walk(child, lane, name, depth + 1)
                    finally:
                        os.close(child)
                else:
                    record = collection(lane, group or "")
                    record["files"] += 1
                    record["bytes"] += info.st_size
                    files += 1
                    total_bytes += info.st_size
                    if total_bytes > 2 ** 53 - 1:
                        raise LibraryScanError("LIBRARY_SCAN_LIMIT")
        after = os.fstat(descriptor)
        if (before.st_mtime_ns, before.st_ctime_ns) != (after.st_mtime_ns, after.st_ctime_ns):
            raise LibraryScanError("LIBRARY_SCAN_CHANGED")

    root_descriptor = _open_root(root)
    try:
        data = os.open("data", DIRECTORY_FLAGS, dir_fd=root_descriptor)
        try:
            for lane in LANES:
                tick()
                descriptor = os.open(lane, DIRECTORY_FLAGS, dir_fd=data)
                try:
                    walk(descriptor, lane)
                finally:
                    os.close(descriptor)
        finally:
            os.close(data)
    finally:
        os.close(root_descriptor)
        progress(files)
    return {"entries": sorted(collections.values(), key=lambda row: (row["lane"], row["label"], row["id"])),
            "totalFiles": files, "totalBytes": total_bytes}


class LocalLibrary:
    """One background scan with a last-complete, memory-only snapshot."""
    def __init__(self, root: Path, *, scan=scan_library):
        self.root = root
        self.scan = scan
        self.lock = threading.Lock()
        self.thread = None
        self.value = {"schema": "kfm-local-library/v1", "state": "idle", "scannedFiles": 0,
                      "generatedAt": None, "entries": [], "totalBytes": 0, "totalFiles": 0, "error": None}

    def snapshot(self, *, start=False):
        if start:
            return self._start(initial_only=True)
        with self.lock:
            return {**self.value, "entries": [dict(row) for row in self.value["entries"]]}

    def refresh(self):
        return self._start(initial_only=False)

    def _start(self, *, initial_only):
        with self.lock:
            if self.value["state"] != "scanning" and (not initial_only or self.value["state"] == "idle"):
                self.value.update(state="scanning", scannedFiles=0, error=None)
                self.thread = threading.Thread(target=self._run, daemon=True, name="kfm-local-library")
                try:
                    self.thread.start()
                except Exception:
                    self.value.update(state="failed", error="LIBRARY_SCAN_FAILED")
            return {**self.value, "entries": [dict(row) for row in self.value["entries"]]}

    def _progress(self, count):
        with self.lock:
            self.value["scannedFiles"] = count

    def _run(self):
        try:
            result = self.scan(self.root, self._progress)
            with self.lock:
                self.value.update(result, state="complete", error=None,
                                  generatedAt=datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"))
        except Exception as error:
            with self.lock:
                self.value.update(state="failed", error=_error(error))
