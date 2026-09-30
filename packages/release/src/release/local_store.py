"""Read-only local serving boundary for an owner-provisioned release store.

Only immutable snapshot bytes and separately trusted activation metadata are
read. The application has no method for staging, reviewing or activation.
"""
from pathlib import Path
import os
import re
import sqlite3
from urllib.parse import quote

from connectors_core.captured_json import decode_object
from .core import MAX_PACKAGE_BYTES


def regular_bytes(path: Path, limit: int) -> bytes:
    import stat
    for parent in (path, *path.parents):
        if parent.is_symlink():
            raise ValueError("STORE_SYMLINK_DENIED")
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, "rb") as handle:
        info = os.fstat(handle.fileno())
        if not stat.S_ISREG(info.st_mode) or info.st_size > limit:
            raise ValueError("STORE_FILE_INVALID")
        raw = handle.read(limit + 1)
        if len(raw) > limit or len(raw) != info.st_size:
            raise ValueError("STORE_FILE_CHANGED")
        return raw


class LocalReleaseStore:
    def __init__(self, root: str):
        path = Path(root)
        if not path.is_absolute() or any(p.is_symlink() for p in (path, *path.parents)):
            raise ValueError("RELEASE_STORE_INVALID")
        info = path.stat()
        if not path.is_dir() or info.st_uid != os.getuid() or info.st_mode & 0o077:
            raise ValueError("RELEASE_STORE_NOT_PRIVATE")
        self.root = path

    def active(self):
        database = self.root / "activation.sqlite"
        # Reject symlinks/special files before SQLite opens the trusted database.
        regular_bytes(database, 16 * 1024 * 1024)
        with sqlite3.connect("file:" + quote(str(database), safe="/") + "?mode=ro", uri=True, timeout=1) as connection:
            connection.execute("PRAGMA query_only=ON")
            row = connection.execute("SELECT a.package_id, a.decision_json, p.state FROM water_active a LEFT JOIN water_packages p ON p.package_id=a.package_id WHERE a.singleton=1").fetchone()
        if row is None:
            return None
        package_id, text, state = row
        if state != "STAGED":
            return None
        if not re.fullmatch(r"sha256:[a-f0-9]{64}", package_id) or not isinstance(text, str):
            raise ValueError("ACTIVE_METADATA_INVALID")
        decision = decode_object(text.encode(), limit=8192)
        raw = regular_bytes(self.root / "objects" / (package_id.split(":")[1] + ".json"), MAX_PACKAGE_BYTES)
        if decision.get("package_id") != package_id:
            raise ValueError("ACTIVE_BINDING_MISMATCH")
        return raw, decision
