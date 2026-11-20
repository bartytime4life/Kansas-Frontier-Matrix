#!/usr/bin/env python3
"""Write the hash-locked pins that the running interpreter's markers exclude.

pip-audit evaluates environment markers against its own interpreter, so a pin
such as ``pyproj==3.8.0; python_version >= "3.15"`` is silently skipped when the
audit runs on an older Python. This helper copies each excluded requirement,
with its hashes and without its marker, into a per-lock file under an output
directory and prints the written paths, one per line, so the audit job can scan
them in a second pass. It reads only the given lock files and writes only
inside the output directory; it installs nothing and contacts no network.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Sequence

from packaging.markers import Marker


LOCK_LIMIT_BYTES = 1_048_576


class LockFormatError(ValueError):
    """A lock file is not in the expected hash-locked requirement format."""


def _logical_lines(text: str) -> list[str]:
    lines: list[str] = []
    current = ""
    for raw in text.splitlines():
        line = raw.strip()
        if not current and (not line or line.startswith("#")):
            continue
        if line.endswith("\\"):
            current += line[:-1].strip() + " "
            continue
        lines.append((current + line).strip())
        current = ""
    if current:
        raise LockFormatError("LOCK_TRAILING_CONTINUATION")
    return lines


def excluded_requirements(text: str) -> list[str]:
    """Return requirement lines whose marker is false here, markers removed."""
    excluded: list[str] = []
    for line in _logical_lines(text):
        head, *hashes = line.split(" --hash=")
        if not hashes:
            raise LockFormatError("LOCK_REQUIREMENT_WITHOUT_HASH")
        if ";" not in head:
            continue
        requirement, marker = (part.strip() for part in head.split(";", 1))
        if not Marker(marker).evaluate():
            excluded.append(" ".join([requirement, *("--hash=" + h for h in hashes)]))
    return excluded


def write_excluded(locks: Sequence[Path], output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for lock in locks:
        if not lock.is_file() or lock.is_symlink():
            raise LockFormatError("LOCK_NOT_REGULAR_FILE")
        if not 0 < lock.stat().st_size <= LOCK_LIMIT_BYTES:
            raise LockFormatError("LOCK_SIZE_INVALID")
        lines = excluded_requirements(lock.read_text(encoding="utf-8"))
        if not lines:
            continue
        target = output_dir / lock.name
        if target.exists():
            raise LockFormatError("LOCK_NAME_DUPLICATE")
        target.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written.append(target)
    return written


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("locks", nargs="+", type=Path)
    args = parser.parse_args(argv)
    try:
        written = write_excluded(args.locks, args.output_dir)
    except (LockFormatError, OSError, UnicodeError, ValueError) as exc:
        print(f"marker-gated pins: {exc}", file=sys.stderr)
        return 2
    for path in written:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
