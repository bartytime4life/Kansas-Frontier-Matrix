#!/usr/bin/env python3
"""Read-only local-source prerequisites; no install, network, or service startup.

This inspector supports Git checkouts and extracted source archives. It checks
the current interpreter and essential source paths, and locates optional tools
without executing them. A pass does not establish application integration,
source admission, dependency compatibility, release, or publication readiness.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Callable, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
MINIMUM_PYTHON = (3, 11)
REQUIRED_FILES = (
    "pyproject.toml",
    "docs/doctrine/directory-rules.md",
    "tools/local_data/doctor.py",
    "tools/local_data/manage.py",
    "tools/local_data/file_io.py",
    "configs/examples/local-data-manifest.json",
)
OPTIONAL_TOOLS = (
    ("git", "repository updates; optional for an extracted ZIP"),
    ("node", "Explorer development"),
    ("npm", "Sites application dependency installation"),
    ("pnpm", "Explorer Web workspace development"),
    ("corepack", "repository-pinned package manager selection"),
    ("make", "repository command shortcuts"),
    ("bash", "Sites build helpers"),
    ("curl", "Sites installation helpers"),
    ("timeout", "Sites bounded build helpers"),
    ("flock", "Sites build locking"),
)


def inspect(
    repo_root: Path,
    *,
    python_version: Sequence[int] | None = None,
    locate: Callable[[str], str | None] = shutil.which,
) -> dict[str, object]:
    """Return deterministic JSON-compatible observations without writing files."""
    version = tuple(sys.version_info[:3] if python_version is None else python_version)
    python_ok = version[:2] >= MINIMUM_PYTHON
    checks: list[dict[str, object]] = [{
        "id": "python",
        "status": "PASS" if python_ok else "FAIL",
        "observed": ".".join(str(part) for part in version),
        "required": ">=3.11",
    }]
    for relative in REQUIRED_FILES:
        path = repo_root / relative
        try:
            available = path.is_file()
        except OSError:
            available = False
        checks.append({
            "id": "source_file",
            "path": relative,
            "status": "PASS" if available else "FAIL",
            "reason": "PRESENT" if available else "MISSING_OR_NOT_FILE",
        })
    optional = []
    for name, purpose in OPTIONAL_TOOLS:
        try:
            available = locate(name) is not None
        except OSError:
            available = False
        optional.append({
            "name": name,
            "purpose": purpose,
            "availability": "FOUND" if available else "MISSING",
            "version": "NOT_CHECKED",
        })
    try:
        marker = repo_root / ".git"
        git_metadata_present = marker.is_dir() or marker.is_file()
    except OSError:
        git_metadata_present = False
    passed = all(check["status"] == "PASS" for check in checks)
    return {
        "report_version": "kfm-local-doctor-v1",
        "scope": "local-data-prerequisites",
        "outcome": "PASS" if passed else "FAIL",
        "local_data_prerequisites": "READY" if passed else "NOT_READY",
        "source_kind": "GIT_METADATA_PRESENT" if git_metadata_present else "SOURCE_DIRECTORY",
        "checks": checks,
        "optional_tools": optional,
        "not_checked": [
            "git-history-and-update-status",
            "source-content-integrity",
            "javascript-versions-and-dependencies",
            "storage-capacity-and-permissions",
            "application-integration",
            "source-admission-and-publication",
        ],
        "side_effects": {
            "files_written": False,
            "commands_executed": False,
            "network_requests": False,
            "services_started": False,
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root", type=Path, default=REPO_ROOT,
        help="source directory to inspect (default: this tool's repository)",
    )
    args = parser.parse_args(argv)
    report = inspect(args.repo_root)
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if report["outcome"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
