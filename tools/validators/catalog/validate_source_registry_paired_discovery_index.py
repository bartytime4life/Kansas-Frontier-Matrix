from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

try:
    from tools.validators.catalog._markdown_inventory import (
        visible_line_spans as _visible_line_spans,
    )
except ModuleNotFoundError as exc:
    if exc.name != "tools":
        raise
    from _markdown_inventory import visible_line_spans as _visible_line_spans

PROFILE = "kfm.source-registry-paired-discovery-index.v6"
SECTION_HEADER = "The 13 paired domain README lanes confirmed at the pinned base are:"
ATX_H2_RE = re.compile(r"^ {0,3}##(?:[ \t]+|[ \t]*$)")
ROW_RE = re.compile(
    r"^\|\s*[^|]+\|\s*\[`sources/([^/]+)/`\]\(([^)]+)\)\s*"
    r"\|\s*\[`([^/]+)/sources/`\]\(([^)]+)\)\s*\|$"
)
TABLE_SEPARATOR_RE = re.compile(
    r"^\|\s*:?-+:?\s*(?:\|\s*:?-+:?\s*)+\|?$"
)


def _read_index_rows(
    readme_path: Path,
) -> tuple[list[dict[str, str]], list[str]]:
    text = readme_path.read_text(encoding="utf-8")
    visible = _visible_line_spans(text)
    section_matches = [
        (start, end)
        for start, end, line in visible
        if line.strip() == SECTION_HEADER
    ]
    if not section_matches:
        raise ValueError(f"missing section marker: {SECTION_HEADER}")
    if len(section_matches) > 1:
        raise ValueError(f"duplicate section marker: {SECTION_HEADER}")
    section_start = section_matches[0][1]
    section_end = next(
        (
            start
            for start, _, line in visible
            if start > section_start and ATX_H2_RE.match(line)
        ),
        len(text),
    )
    section_lines = [
        line
        for start, _, line in visible
        if section_start <= start < section_end
    ]

    rows: list[dict[str, str]] = []
    invalid_rows: list[str] = []
    table_active = False
    for line in section_lines:
        stripped = line.strip()
        if TABLE_SEPARATOR_RE.fullmatch(stripped):
            table_active = True
            continue
        if not table_active:
            continue
        if not stripped:
            if rows or invalid_rows:
                table_active = False
            continue
        if not stripped.startswith("|"):
            if rows or invalid_rows:
                table_active = False
            continue
        match = ROW_RE.match(stripped)
        if not match:
            invalid_rows.append(stripped)
            continue
        canonical_domain, canonical_link, parallel_domain, parallel_link = match.groups()
        rows.append(
            {
                "canonical_domain": canonical_domain,
                "canonical_link": canonical_link,
                "parallel_domain": parallel_domain,
                "parallel_link": parallel_link,
            }
        )
    if not rows and not invalid_rows:
        raise ValueError("source registry paired discovery index contains no parseable rows")
    return rows, sorted(invalid_rows)


def _canonical_domains(repo_root: Path) -> list[str]:
    root = repo_root / "data" / "registry" / "sources"
    if not root.is_dir():
        raise ValueError(f"canonical source registry root is not a directory: {root}")
    return sorted(
        entry.name
        for entry in root.iterdir()
        if entry.is_dir() and not entry.name.startswith(".")
    )


def _parallel_domains(repo_root: Path) -> list[str]:
    registry_root = repo_root / "data" / "registry"
    if not registry_root.is_dir():
        raise ValueError(f"registry root is not a directory: {registry_root}")
    return sorted(
        entry.name
        for entry in registry_root.iterdir()
        if entry.is_dir()
        and not entry.name.startswith(".")
        and (entry / "sources").is_dir()
    )


def validate_source_registry_paired_discovery_index(
    repo_root: Path,
    *,
    readme_path: Path | None = None,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    readme_path = (
        readme_path or repo_root / "data" / "registry" / "sources" / "README.md"
    ).resolve()

    rows, invalid_index_rows = _read_index_rows(readme_path)
    canonical_index = [row["canonical_domain"] for row in rows]
    parallel_index = [row["parallel_domain"] for row in rows]
    canonical_actual = _canonical_domains(repo_root)
    parallel_actual = _parallel_domains(repo_root)

    canonical_counts = Counter(canonical_index)
    duplicate_index_domains = sorted(
        domain for domain, count in canonical_counts.items() if count > 1
    )
    row_domain_mismatches = sorted(
        f"{row['canonical_domain']}!={row['parallel_domain']}"
        for row in rows
        if row["canonical_domain"] != row["parallel_domain"]
    )
    link_mismatches = sorted(
        row["canonical_domain"]
        for row in rows
        if row["canonical_link"] != f"{row['canonical_domain']}/README.md"
        or row["parallel_link"]
        != f"../{row['canonical_domain']}/sources/README.md"
    )

    canonical_index_set = set(canonical_index)
    parallel_index_set = set(parallel_index)
    canonical_actual_set = set(canonical_actual)
    parallel_actual_set = set(parallel_actual)
    paired_actual_set = canonical_actual_set.intersection(parallel_actual_set)
    canonical_root = repo_root / "data" / "registry" / "sources"
    parallel_root = repo_root / "data" / "registry"
    missing_canonical_readmes = sorted(
        domain
        for domain in canonical_index_set.intersection(canonical_actual_set)
        if not (canonical_root / domain / "README.md").is_file()
    )
    missing_parallel_readmes = sorted(
        domain
        for domain in parallel_index_set.intersection(parallel_actual_set)
        if not (parallel_root / domain / "sources" / "README.md").is_file()
    )

    missing_canonical_index = sorted(paired_actual_set - canonical_index_set)
    stale_canonical_index = sorted(canonical_index_set - canonical_actual_set)
    missing_parallel_index = sorted(paired_actual_set - parallel_index_set)
    stale_parallel_index = sorted(parallel_index_set - parallel_actual_set)
    unpaired_canonical_domains = sorted(canonical_actual_set - parallel_actual_set)
    unpaired_parallel_domains = sorted(parallel_actual_set - canonical_actual_set)

    failures = (
        invalid_index_rows
        or duplicate_index_domains
        or row_domain_mismatches
        or link_mismatches
        or missing_canonical_index
        or stale_canonical_index
        or missing_parallel_index
        or stale_parallel_index
        or missing_canonical_readmes
        or missing_parallel_readmes
    )

    return {
        "profile": PROFILE,
        "outcome": "FAIL" if failures else "PASS",
        "authority_created": False,
        "repo_root": str(repo_root),
        "readme": str(readme_path),
        "indexed_domains": canonical_index,
        "canonical_domains": canonical_actual,
        "parallel_domains": parallel_actual,
        "paired_domains": sorted(paired_actual_set),
        "invalid_index_rows": invalid_index_rows,
        "duplicate_index_domains": duplicate_index_domains,
        "row_domain_mismatches": row_domain_mismatches,
        "link_mismatches": link_mismatches,
        "missing_canonical_index": missing_canonical_index,
        "stale_canonical_index": stale_canonical_index,
        "missing_parallel_index": missing_parallel_index,
        "stale_parallel_index": stale_parallel_index,
        "missing_canonical_readmes": missing_canonical_readmes,
        "missing_parallel_readmes": missing_parallel_readmes,
        "unpaired_canonical_domains": unpaired_canonical_domains,
        "unpaired_parallel_domains": unpaired_parallel_domains,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that the canonical source-registry discovery matrix matches "
            "both data/registry/sources/<domain>/ and domain-first compatibility lanes."
        )
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
    )
    parser.add_argument("--readme", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        report = validate_source_registry_paired_discovery_index(
            args.repo_root,
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
