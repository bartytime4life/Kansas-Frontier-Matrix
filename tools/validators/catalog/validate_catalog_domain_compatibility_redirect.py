from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

PROFILE = "kfm.catalog-domain-compatibility-redirect.v5"
SECTION_HEADER = "## Current bounded inventory"
ROW_RE = re.compile(
    r"^-\s+\[`([^`]+/)`\]\(\./([^/]+)/README\.md\)\s*$"
)
CONFLICT_BOUNDARY_RE = re.compile(r"^(?:<{7,}|>{7,})(?: .*)?$")


def _read_redirect_rows(readme_path: Path) -> tuple[list[str], list[str]]:
    text = readme_path.read_text(encoding="utf-8")
    marker_count = sum(
        line.strip() == SECTION_HEADER for line in text.splitlines()
    )
    if marker_count == 0:
        raise ValueError(f"missing section: {SECTION_HEADER}")
    if marker_count > 1:
        raise ValueError(f"duplicate section: {SECTION_HEADER}")
    start = text.find(SECTION_HEADER)
    section = text[start + len(SECTION_HEADER):]
    next_h2 = section.find("\n## ")
    if next_h2 >= 0:
        section = section[:next_h2]

    lanes: list[str] = []
    invalid_rows: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("- ["):
            continue
        match = ROW_RE.match(stripped)
        if match is None:
            invalid_rows.append(stripped)
            continue
        lane, linked_lane = match.groups()
        if lane.rstrip("/") != linked_lane:
            invalid_rows.append(stripped)
            continue
        lanes.append(lane)
    if not lanes and not invalid_rows:
        raise ValueError("compatibility redirect inventory contains no parseable child rows")
    return lanes, sorted(invalid_rows)


def _direct_children(root: Path) -> list[str]:
    if not root.is_dir():
        raise ValueError(f"root is not a directory: {root}")
    return sorted(
        f"{entry.name}/"
        for entry in root.iterdir()
        if entry.is_dir() and not entry.name.startswith(".")
    )


def _unexpected_root_files(root: Path) -> list[str]:
    return sorted(
        entry.name
        for entry in root.iterdir()
        if entry.is_file()
        and not entry.name.startswith(".")
        and entry.name != "README.md"
    )


def _child_redirect_reason_codes(readme_path: Path, lane: str) -> list[str]:
    text = readme_path.read_text(encoding="utf-8")
    reasons: list[str] = []
    if any(CONFLICT_BOUNDARY_RE.fullmatch(line) for line in text.splitlines()):
        reasons.append("MERGE_CONFLICT_MARKER")
    if f"data/catalog/domain/{lane}/" not in text:
        reasons.append("CANONICAL_TARGET_MISSING")
    return reasons


def validate_catalog_domain_compatibility_redirect(
    compatibility_root: Path,
    canonical_root: Path,
    *,
    readme_path: Path | None = None,
) -> dict[str, Any]:
    compatibility_root = compatibility_root.resolve()
    canonical_root = canonical_root.resolve()
    readme_path = (readme_path or compatibility_root / "README.md").resolve()

    indexed, invalid_redirect_rows = _read_redirect_rows(readme_path)
    actual = _direct_children(compatibility_root)
    unexpected_root_files = _unexpected_root_files(compatibility_root)
    counts = Counter(indexed)
    duplicate_entries = sorted(name for name, count in counts.items() if count > 1)
    indexed_unique = set(indexed)
    actual_set = set(actual)
    missing_from_index = sorted(actual_set - indexed_unique)
    stale_index_entries = sorted(indexed_unique - actual_set)

    missing_child_readmes: list[str] = []
    invalid_child_redirects: list[str] = []
    invalid_child_redirect_details: list[dict[str, Any]] = []
    missing_canonical_targets: list[str] = []
    for lane in sorted(actual_set | indexed_unique):
        child = compatibility_root / lane.rstrip("/")
        target = canonical_root / lane.rstrip("/")
        child_readme = child / "README.md"
        if child.is_dir():
            if not child_readme.is_file():
                missing_child_readmes.append(lane)
            else:
                reason_codes = _child_redirect_reason_codes(
                    child_readme, lane.rstrip("/")
                )
                if reason_codes:
                    invalid_child_redirects.append(lane)
                    invalid_child_redirect_details.append(
                        {"lane": lane, "reason_codes": reason_codes}
                    )
        if lane in indexed_unique and not target.is_dir():
            missing_canonical_targets.append(lane)

    outcome = (
        "PASS"
        if not (
            duplicate_entries
            or invalid_redirect_rows
            or missing_from_index
            or stale_index_entries
            or missing_child_readmes
            or invalid_child_redirects
            or missing_canonical_targets
            or unexpected_root_files
        )
        else "FAIL"
    )
    return {
        "profile": PROFILE,
        "outcome": outcome,
        "authority_created": False,
        "compatibility_root": str(compatibility_root),
        "canonical_root": str(canonical_root),
        "readme": str(readme_path),
        "actual_redirect_children": actual,
        "indexed_redirect_children": indexed,
        "duplicate_entries": duplicate_entries,
        "invalid_redirect_rows": invalid_redirect_rows,
        "missing_from_index": missing_from_index,
        "stale_index_entries": stale_index_entries,
        "missing_child_readmes": missing_child_readmes,
        "invalid_child_redirects": invalid_child_redirects,
        "invalid_child_redirect_details": invalid_child_redirect_details,
        "missing_canonical_targets": missing_canonical_targets,
        "unexpected_root_files": unexpected_root_files,
        "canonical_only_children_allowed": True,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate catalog/domain compatibility redirect discovery against "
            "its canonical data/catalog/domain targets."
        )
    )
    repo_root = Path(__file__).resolve().parents[3]
    parser.add_argument(
        "--compatibility-root",
        type=Path,
        default=repo_root / "catalog" / "domain",
    )
    parser.add_argument(
        "--canonical-root",
        type=Path,
        default=repo_root / "data" / "catalog" / "domain",
    )
    parser.add_argument("--readme", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        report = validate_catalog_domain_compatibility_redirect(
            args.compatibility_root,
            args.canonical_root,
            readme_path=args.readme,
        )
    except (OSError, ValueError) as exc:
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
