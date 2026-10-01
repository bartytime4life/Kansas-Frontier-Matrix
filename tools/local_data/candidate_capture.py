"""Private, immutable local candidate output for bounded source connectors.

Connectors choose fixed object names and supply captured bytes; this operator
boundary validates the external destination and owns every filesystem write.
No candidate produced here is admitted, reviewed, or released.
"""

from __future__ import annotations

import os
import re
import stat
from pathlib import Path

from tools.local_data.file_io import check_directory, fsync_directory

REPOSITORY = Path(__file__).resolve().parents[2]
NAME = re.compile(r"[a-z0-9][a-z0-9._-]{0,127}\Z")
MAX_OBJECT_BYTES = 32 * 1024 * 1024


def _external(path: Path) -> Path:
    if not isinstance(path, Path) or not path.is_absolute() or ".." in path.parts:
        raise ValueError("CANDIDATE_PATH_INVALID")
    check_directory(path.parent)
    absolute = path.absolute()
    if absolute == REPOSITORY or REPOSITORY in absolute.parents:
        raise ValueError("CANDIDATE_INSIDE_REPOSITORY")
    return absolute


def create_candidate(directory: Path) -> None:
    target = _external(directory)
    target.mkdir(mode=0o700, exist_ok=False)
    fsync_directory(target.parent)


def write_candidate(directory: Path, name: str, body: bytes) -> None:
    target = _external(directory)
    if not NAME.fullmatch(name) or name in {".", ".."}:
        raise ValueError("CANDIDATE_NAME_INVALID")
    if not isinstance(body, bytes) or len(body) > MAX_OBJECT_BYTES:
        raise ValueError("CANDIDATE_OBJECT_LIMIT")
    mode = target.lstat().st_mode
    if not stat.S_ISDIR(mode) or (mode & 0o077) or target.stat().st_uid != os.getuid():
        raise ValueError("CANDIDATE_DIRECTORY_UNSAFE")
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(target / name, flags, 0o600)
    with os.fdopen(fd, "wb") as output:
        output.write(body)
        output.flush()
        os.fsync(output.fileno())
    fsync_directory(target)
