"""Resumable, chunk-verified Studio uploads for evidence larger than one request.

An upload session lives in ``<store>/uploads/<id>/`` as ``meta.json`` and a
``data`` file. The bytes on disk are the progress record: a client resumes at
the current size of ``data``. Every chunk carries its SHA-256 and is checked
before it is written, so an interrupted write leaves only a correct prefix.
Each session belongs to the account that started it; another account sees
it as absent. Completing a session hands the staged file to the Store, which hashes,
extracts and quarantines it exactly as a single-request upload. Sessions grant
no review, admission or publication state.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import shutil
import stat
import threading
import time
import uuid

SESSION_ID = re.compile(r"[a-f0-9]{32}")
DIGEST = re.compile(r"[a-f0-9]{64}")
MAX_ACTIVE_SESSIONS = 4
STALE_SECONDS = 24 * 60 * 60
FREE_SPACE_MARGIN = 256 * 1024 * 1024
MAX_NAME_CHARACTERS = 255


class UploadSessions:
    def __init__(self, store_root, *, max_bytes, chunk_bytes, check_head, clock=time.time):
        self.store_root = Path(store_root)
        self.root = self.store_root / "uploads"
        self.max_bytes = max_bytes
        self.chunk_bytes = chunk_bytes
        self.check_head = check_head
        self.clock = clock
        self.lock = threading.Lock()

    def _dir(self, upload_id):
        if not isinstance(upload_id, str) or not SESSION_ID.fullmatch(upload_id):
            raise KeyError("Upload not found.")
        path = self.root / upload_id
        if path.is_symlink() or not path.is_dir():
            raise KeyError("Upload not found.")
        return path

    def _owned(self, upload_id, owner):
        path = self._dir(upload_id)
        meta = json.loads((path / "meta.json").read_text(encoding="utf-8"))
        if not isinstance(owner, str) or not hmac.compare_digest(meta.get("owner", ""), owner):
            raise KeyError("Upload not found.")
        return path

    def _meta(self, path):
        meta = json.loads((path / "meta.json").read_text(encoding="utf-8"))
        data = path / "data"
        info = os.lstat(data)
        if not stat.S_ISREG(info.st_mode) or info.st_size > meta["size"]:
            raise ValueError("Upload storage changed. Cancel it and upload the file again.")
        return {"id": path.name, "name": meta["name"], "size": meta["size"],
                "received": info.st_size, "chunkBytes": self.chunk_bytes}

    def _require_space(self, needed):
        if shutil.disk_usage(self.store_root).free < needed + FREE_SPACE_MARGIN:
            raise ValueError("Not enough free disk space for this upload. Free space and try again.")

    def cleanup(self):
        """Remove sessions untouched for STALE_SECONDS. Caller holds the lock."""
        if not self.root.is_dir():
            return
        cutoff = self.clock() - STALE_SECONDS
        for child in self.root.iterdir():
            if (SESSION_ID.fullmatch(child.name) and not child.is_symlink() and child.is_dir()
                    and child.stat().st_mtime < cutoff):
                shutil.rmtree(child)

    def create(self, name, size, *, owner):
        if not isinstance(owner, str) or not 0 < len(owner) <= 128:
            raise ValueError("Upload needs a signed-in account.")
        if (not isinstance(name, str) or not 0 < len(name) <= MAX_NAME_CHARACTERS
                or re.search(r"[\x00-\x1f\x7f]", name)):
            raise ValueError("Upload needs a file name of 1 to 255 visible characters.")
        if type(size) is not int or not 0 < size <= self.max_bytes:
            raise ValueError(f"File must contain 1 byte to {self.max_bytes // (1024 ** 3)} GiB.")
        with self.lock:
            self.cleanup()
            self.root.mkdir(mode=0o700, exist_ok=True)
            active = [c for c in self.root.iterdir() if SESSION_ID.fullmatch(c.name)]
            if len(active) >= MAX_ACTIVE_SESSIONS:
                raise RuntimeError("Too many unfinished uploads. Finish or cancel one, then try again.")
            self._require_space(size)
            upload_id = uuid.uuid4().hex
            path = self.root / upload_id
            path.mkdir(mode=0o700)
            (path / "meta.json").write_text(json.dumps({"name": name, "size": size, "owner": owner}),
                                            encoding="utf-8")
            os.close(os.open(path / "data", os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600))
            return self._meta(path)

    def status(self, upload_id, *, owner):
        with self.lock:
            return self._meta(self._owned(upload_id, owner))

    def append(self, upload_id, offset, chunk, digest, *, owner):
        if not isinstance(digest, str) or not DIGEST.fullmatch(digest):
            raise ValueError("Each upload part needs its SHA-256 in X-KFM-Chunk-SHA256.")
        if not chunk or len(chunk) > self.chunk_bytes:
            raise ValueError("Upload part is empty or larger than the part size.")
        if hashlib.sha256(chunk).hexdigest() != digest:
            raise ValueError("Upload part failed its integrity check. Send it again.")
        with self.lock:
            path = self._owned(upload_id, owner)
            current = self._meta(path)
            if offset != current["received"]:
                raise RuntimeError(f"Upload is at byte {current['received']}. Resume from there.")
            if current["received"] + len(chunk) > current["size"]:
                raise ValueError("Upload part goes past the declared file size.")
            if offset == 0:
                self.check_head(chunk[:20])
            self._require_space(len(chunk))
            fd = os.open(path / "data", os.O_WRONLY | os.O_NOFOLLOW)
            try:
                info = os.fstat(fd)
                if not stat.S_ISREG(info.st_mode) or info.st_size != offset:
                    raise ValueError("Upload storage changed. Cancel it and upload the file again.")
                os.lseek(fd, offset, os.SEEK_SET)
                view = memoryview(chunk)
                while view:
                    view = view[os.write(fd, view):]
                os.fsync(fd)
            finally:
                os.close(fd)
            os.utime(path)
            return self._meta(path)

    def take(self, upload_id, *, owner):
        """Move a complete upload's bytes out of its session for ingestion."""
        with self.lock:
            path = self._owned(upload_id, owner)
            current = self._meta(path)
            if current["received"] != current["size"]:
                raise ValueError(f"Upload is incomplete: {current['received']} of {current['size']} bytes received.")
            staged = self.store_root / f"upload-{upload_id}"
            os.replace(path / "data", staged)
            shutil.rmtree(path)
            return staged, current["name"]

    def cancel(self, upload_id, *, owner):
        with self.lock:
            shutil.rmtree(self._owned(upload_id, owner))
