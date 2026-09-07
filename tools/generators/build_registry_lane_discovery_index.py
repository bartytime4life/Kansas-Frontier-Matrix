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
import re
import sys
from pathlib import Path
from typing import Any

PROFILE = "kfm.registry-lane-discovery-index.v1"
OUTPUT_AUTHORITY = "derived_discovery_only"
LANE_NAME_RE = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")


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
        raise RegistryDiscoveryError(
            f"registry root is not a directory: {registry_root}"
        )

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


def _write_output(path: Path, content: str) -> None:
    if path.is_symlink():
        raise RegistryDiscoveryError("output path must not be a symlink")
    absolute_path = path if path.is_absolute() else Path.cwd() / path
    if any(parent.is_symlink() for parent in absolute_path.parents):
        raise RegistryDiscoveryError("output path parent must not be a symlink")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


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
        print(
            json.dumps(
                {
                    "profile": PROFILE,
                    "outcome": "ERROR",
                    "authority_created": False,
                    "error": str(exc),
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
