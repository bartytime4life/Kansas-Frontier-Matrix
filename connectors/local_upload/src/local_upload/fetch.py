"""Bounded local-byte capture primitives; no source admission or network access.

Callers own the destination tree. Static symlinks and special files are denied;
this is not a sandbox against another process replacing directory ancestors.
"""

from __future__ import annotations

import hashlib
import os
import stat
import tempfile
from pathlib import Path

CHUNK_BYTES = 1024 * 1024


def check_directory(path: Path, *, create: bool = False) -> None:
    """Require a real-directory chain, optionally creating private directories."""
    absolute = path.absolute()
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        if part in {".", ".."}:
            raise ValueError("UNSAFE_PATH")
        current /= part
        try:
            mode = current.lstat().st_mode
        except FileNotFoundError:
            if not create:
                raise ValueError("DIRECTORY_MISSING") from None
            current.mkdir(mode=0o700)
            fsync_directory(current.parent)
            mode = current.lstat().st_mode
        if not stat.S_ISDIR(mode):
            raise ValueError("DIRECTORY_SYMLINK_OR_SPECIAL")


def open_regular(path: Path) -> int:
    """Open a regular file without following its final symlink or blocking FIFO."""
    check_directory(path.parent)
    before = path.lstat()
    if not stat.S_ISREG(before.st_mode):
        raise ValueError("INPUT_SYMLINK_OR_SPECIAL")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    fd = os.open(path, flags)
    after = os.fstat(fd)
    if not stat.S_ISREG(after.st_mode) or (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
        os.close(fd)
        raise ValueError("INPUT_CHANGED")
    return fd


def _identity(value: os.stat_result) -> tuple[int, int, int, int, int]:
    return value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns, value.st_ctime_ns


def hash_regular(path: Path, max_bytes: int, *, expected_size: int | None = None) -> tuple[str, int]:
    """Hash one explicit regular file in bounded memory and detect input changes."""
    fd = open_regular(path)
    with os.fdopen(fd, "rb") as handle:
        before = os.fstat(handle.fileno())
        if before.st_size > max_bytes or (expected_size is not None and before.st_size != expected_size):
            raise ValueError("INPUT_SIZE_MISMATCH_OR_LIMIT")
        digest = hashlib.sha256()
        count = 0
        while True:
            chunk = handle.read(min(CHUNK_BYTES, max_bytes - count + 1))
            if not chunk:
                break
            count += len(chunk)
            if count > max_bytes:
                raise ValueError("INPUT_BYTE_LIMIT")
            digest.update(chunk)
        if count != before.st_size or _identity(before) != _identity(os.fstat(handle.fileno())):
            raise ValueError("INPUT_CHANGED")
        return digest.hexdigest(), count


def read_regular(path: Path, max_bytes: int) -> bytes:
    """Read a bounded metadata file through the same regular-file checks."""
    fd = open_regular(path)
    with os.fdopen(fd, "rb") as handle:
        before = os.fstat(handle.fileno())
        if before.st_size > max_bytes:
            raise ValueError("METADATA_BYTE_LIMIT")
        result = handle.read(max_bytes + 1)
        if len(result) > max_bytes:
            raise ValueError("METADATA_BYTE_LIMIT")
        if len(result) != before.st_size or _identity(before) != _identity(os.fstat(handle.fileno())):
            raise ValueError("INPUT_CHANGED")
        return result


def fsync_directory(path: Path) -> None:
    """Persist a completed directory entry where the platform supports it."""
    if os.name != "posix":
        return
    fd = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def write_new(path: Path, content: bytes) -> None:
    """Write an immutable metadata object; never replace an existing path."""
    check_directory(path.parent, create=True)
    fd, name = tempfile.mkstemp(prefix=".capture-", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.link(temporary, path)
        fsync_directory(path.parent)
    finally:
        temporary.unlink(missing_ok=True)


def capture_file(source: Path, destination: Path, *, sha256: str, size_bytes: int, max_bytes: int) -> None:
    """Stream verified opaque bytes into an absent immutable quarantine object.

    Filesystem hard links provide an atomic no-overwrite commit. Unsupported
    filesystems fail closed. The source bytes are never parsed or extracted.
    """
    if size_bytes < 1 or size_bytes > max_bytes:
        raise ValueError("INPUT_BYTE_LIMIT")
    source_fd = open_regular(source)
    temporary: Path | None = None
    try:
        with os.fdopen(source_fd, "rb") as reader:
            before = os.fstat(reader.fileno())
            if before.st_size != size_bytes:
                raise ValueError("INPUT_SIZE_MISMATCH")
            check_directory(destination.parent, create=True)
            fd, name = tempfile.mkstemp(prefix=".capture-", dir=destination.parent)
            temporary = Path(name)
            with os.fdopen(fd, "wb") as writer:
                digest = hashlib.sha256()
                count = 0
                while True:
                    chunk = reader.read(min(CHUNK_BYTES, size_bytes - count + 1))
                    if not chunk:
                        break
                    count += len(chunk)
                    if count > size_bytes:
                        raise ValueError("INPUT_BYTE_LIMIT")
                    digest.update(chunk)
                    writer.write(chunk)
                if count != size_bytes or digest.hexdigest() != sha256:
                    raise ValueError("INPUT_DIGEST_OR_SIZE_MISMATCH")
                if _identity(before) != _identity(os.fstat(reader.fileno())):
                    raise ValueError("INPUT_CHANGED")
                writer.flush()
                os.fsync(writer.fileno())
            os.link(temporary, destination)
            fsync_directory(destination.parent)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
