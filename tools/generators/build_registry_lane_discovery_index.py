#!/usr/bin/env python3
"""Build deterministic discovery metadata for direct KFM registry lanes.

The canonical source remains the repository topology under ``data/registry/``.
This generator exposes only immediate lane names and README presence so
Catalog/Explorer consumers can discover governed registry seams without reading
registry payloads or inferring source admission, policy, evidence, release, or
publication state.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import stat
import sys
from pathlib import Path
from typing import Any

PROFILE = "kfm.registry-lane-discovery-index.v1"
OUTPUT_AUTHORITY = "derived_discovery_only"
LANE_NAME_RE = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")
SECURE_OUTPUT_SUPPORTED = (
    os.name == "posix"
    and hasattr(os, "O_DIRECTORY")
    and hasattr(os, "O_NOFOLLOW")
    and all(
        function in os.supports_dir_fd
        for function in (os.open, os.mkdir, os.stat)
    )
    and os.stat in os.supports_follow_symlinks
)


class RegistryDiscoveryError(ValueError):
    """Raised when registry topology cannot be projected safely."""


def _lane_record(root: Path, entry: Path) -> dict[str, Any]:
    name = entry.name
    if not LANE_NAME_RE.fullmatch(name):
        raise RegistryDiscoveryError(f"unsupported registry lane name: {name}")
    readme = entry / "README.md"
    if readme.is_symlink():
        raise RegistryDiscoveryError(
            f"registry lane README must not be a symlink: {name}"
        )
    return {
        "lane": name,
        "path": (Path("data") / "registry" / name).as_posix(),
        "readme_present": readme.is_file(),
    }


def build_registry_lane_discovery_index(registry_root: Path) -> dict[str, Any]:
    if registry_root.is_symlink():
        raise RegistryDiscoveryError("registry root must not be a symlink")
    absolute_root = (
        registry_root if registry_root.is_absolute() else Path.cwd() / registry_root
    )
    if any(parent.is_symlink() for parent in absolute_root.parents):
        raise RegistryDiscoveryError("registry root parent must not be a symlink")
    registry_root = registry_root.resolve()
    if not registry_root.is_dir():
        raise RegistryDiscoveryError("registry root is not a directory")

    lanes = []
    for entry in sorted(registry_root.iterdir(), key=lambda item: item.name):
        if entry.name.startswith("."):
            continue
        if entry.is_symlink():
            raise RegistryDiscoveryError(
                f"registry lane must not be a symlink: {entry.name}"
            )
        if entry.is_dir():
            lanes.append(_lane_record(registry_root, entry))
    lanes.sort(key=lambda item: item["lane"])

    return {
        "profile": PROFILE,
        "authority": OUTPUT_AUTHORITY,
        "authority_created": False,
        "scope": "registry-root-lane-topology-only",
        "source_root": "data/registry",
        "payloads_read": False,
        "public_readiness_inferred": False,
        "lane_count": len(lanes),
        "lanes": lanes,
    }


def render_index(index: dict[str, Any]) -> str:
    return json.dumps(index, sort_keys=True, separators=(",", ":")) + "\n"


def _open_output_parent(parent: Path) -> int:
    if not SECURE_OUTPUT_SUPPORTED:
        raise RegistryDiscoveryError("secure output writes are unavailable")

    absolute_parent = Path(os.path.abspath(parent))
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    current_fd = os.open(absolute_parent.anchor, flags)
    try:
        for component in absolute_parent.parts[1:]:
            try:
                expected = os.stat(
                    component,
                    dir_fd=current_fd,
                    follow_symlinks=False,
                )
            except FileNotFoundError:
                try:
                    os.mkdir(component, dir_fd=current_fd)
                except FileExistsError:
                    pass
                expected = os.stat(
                    component,
                    dir_fd=current_fd,
                    follow_symlinks=False,
                )
            if stat.S_ISLNK(expected.st_mode):
                raise RegistryDiscoveryError(
                    "output path parent must not be a symlink"
                )
            if not stat.S_ISDIR(expected.st_mode):
                raise RegistryDiscoveryError(
                    "output path parent must be a directory"
                )
            try:
                next_fd = os.open(component, flags, dir_fd=current_fd)
            except OSError as exc:
                raise RegistryDiscoveryError(
                    "output path parent changed during validation"
                ) from exc
            actual = os.fstat(next_fd)
            if (expected.st_dev, expected.st_ino) != (actual.st_dev, actual.st_ino):
                os.close(next_fd)
                raise RegistryDiscoveryError(
                    "output path parent changed during validation"
                )
            os.close(current_fd)
            current_fd = next_fd
        return current_fd
    except Exception:
        os.close(current_fd)
        raise


def _validate_output_stat(output_stat: os.stat_result) -> None:
    if stat.S_ISLNK(output_stat.st_mode):
        raise RegistryDiscoveryError("output path must not be a symlink")
    if not stat.S_ISREG(output_stat.st_mode):
        raise RegistryDiscoveryError("output path must be a regular file")
    if output_stat.st_nlink > 1:
        raise RegistryDiscoveryError("output path must not be hard linked")


def _write_output(path: Path, content: str) -> None:
    if not path.name:
        raise RegistryDiscoveryError("output path must be a regular file")
    parent_fd = _open_output_parent(path.parent)
    output_fd: int | None = None
    try:
        try:
            expected = os.stat(
                path.name,
                dir_fd=parent_fd,
                follow_symlinks=False,
            )
        except FileNotFoundError:
            expected = None
        if expected is not None:
            _validate_output_stat(expected)

        flags = os.O_WRONLY | os.O_NOFOLLOW
        try:
            if expected is None:
                output_fd = os.open(
                    path.name,
                    flags | os.O_CREAT | os.O_EXCL,
                    0o644,
                    dir_fd=parent_fd,
                )
            else:
                output_fd = os.open(path.name, flags, dir_fd=parent_fd)
        except OSError as exc:
            raise RegistryDiscoveryError(
                "output path changed during validation"
            ) from exc

        actual = os.fstat(output_fd)
        _validate_output_stat(actual)
        if expected is not None and (expected.st_dev, expected.st_ino) != (
            actual.st_dev,
            actual.st_ino,
        ):
            raise RegistryDiscoveryError("output path changed during validation")

        os.ftruncate(output_fd, 0)
        with os.fdopen(output_fd, "w", encoding="utf-8", newline="") as stream:
            output_fd = None
            stream.write(content)
    finally:
        if output_fd is not None:
            os.close(output_fd)
        os.close(parent_fd)


def _parser() -> argparse.ArgumentParser:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description=(
            "Build deterministic discovery metadata for direct data/registry lanes."
        )
    )
    parser.add_argument(
        "--registry-root",
        type=Path,
        default=repo_root / "data" / "registry",
    )
    parser.add_argument("--output", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        output = render_index(build_registry_lane_discovery_index(args.registry_root))
        if args.output is None:
            sys.stdout.write(output)
        else:
            _write_output(args.output, output)
    except (OSError, RegistryDiscoveryError) as exc:
        error = (
            str(exc)
            if isinstance(exc, RegistryDiscoveryError)
            else "registry discovery I/O failed"
        )
        print(
            json.dumps(
                {
                    "profile": PROFILE,
                    "outcome": "ERROR",
                    "authority_created": False,
                    "error": error,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
