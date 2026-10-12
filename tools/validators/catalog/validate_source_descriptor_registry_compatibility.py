from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

PROFILE = "kfm.source-descriptor-registry-compatibility.v1"
COMPATIBILITY_REL = Path("data/registry/source_descriptors")
CANONICAL_REL = Path("data/registry/sources")
REQUIRED_MARKERS = (
    "registry_scope: source-descriptor-compatibility-and-routing",
    "canonical-source-registry-parent-confirmed-at-data-registry-sources",
    "data/registry/sources/",
    "compatibility/routing lane",
)


def validate_source_descriptor_registry_compatibility(repo_root: Path) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    compatibility_root = repo_root / COMPATIBILITY_REL
    canonical_root = repo_root / CANONICAL_REL
    readme_path = compatibility_root / "README.md"
    canonical_readme = canonical_root / "README.md"

    findings: list[str] = []
    missing_markers: list[str] = []
    unexpected_entries: list[str] = []

    if not compatibility_root.is_dir():
        findings.append("COMPATIBILITY_ROOT_MISSING")
        readme_text = ""
    elif not readme_path.is_file():
        findings.append("COMPATIBILITY_README_MISSING")
        readme_text = ""
    else:
        readme_text = readme_path.read_text(encoding="utf-8")
        missing_markers = sorted(
            marker for marker in REQUIRED_MARKERS if marker not in readme_text
        )
        if missing_markers:
            findings.append("COMPATIBILITY_MARKERS_MISSING")

        for entry in sorted(compatibility_root.iterdir(), key=lambda item: item.name):
            if entry.name.startswith("."):
                continue
            if entry.is_dir() or entry.suffix.lower() != ".md":
                unexpected_entries.append(entry.name)
        if unexpected_entries:
            findings.append("UNEXPECTED_COMPATIBILITY_PAYLOAD")

    if not canonical_root.is_dir():
        findings.append("CANONICAL_SOURCE_REGISTRY_MISSING")
    elif not canonical_readme.is_file():
        findings.append("CANONICAL_SOURCE_REGISTRY_README_MISSING")

    return {
        "profile": PROFILE,
        "outcome": "PASS" if not findings else "FAIL",
        "authority_created": False,
        "repo_root": str(repo_root),
        "compatibility_root": str(compatibility_root),
        "canonical_target": str(canonical_root),
        "missing_markers": missing_markers,
        "unexpected_entries": unexpected_entries,
        "findings": sorted(findings),
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that data/registry/source_descriptors remains a pointer-only "
            "compatibility lane to canonical data/registry/sources."
        )
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        report = validate_source_descriptor_registry_compatibility(args.repo_root)
    except OSError as exc:
        report = {
            "profile": PROFILE,
            "outcome": "ERROR",
            "authority_created": False,
            "error": str(exc),
        }
        print(json.dumps(report, sort_keys=True, separators=(",", ":")))
        return 2

    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if report["outcome"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
