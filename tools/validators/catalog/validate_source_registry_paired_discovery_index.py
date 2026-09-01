from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

PROFILE = "kfm.source-registry-paired-discovery-index.v2"
SECTION_HEADER = "The 13 paired domain README lanes confirmed at the pinned base are:"
ROW_RE = re.compile(
    r"^\|\s*[^|]+\|\s*\[`sources/([^/]+)/`\]\(([^)]+)\)\s*"
    r"\|\s*\[`([^/]+)/sources/`\]\(([^)]+)\)\s*\|$"
)


def _read_index_rows(readme_path: Path) -> list[dict[str, str]]:
    text = readme_path.read_text(encoding="utf-8")
    start = text.find(SECTION_HEADER)
    if start < 0:
        raise ValueError(f"missing section marker: {SECTION_HEADER}")
    section = text[start + len(SECTION_HEADER):]
    next_h2 = section.find("\n## ")
    if next_h2 >= 0:
        section = section[:next_h2]

    rows: list[dict[str, str]] = []
    for line in section.splitlines():
        match = ROW_RE.match(line)
        if not match:
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
    if not rows:
        raise ValueError("source registry paired discovery index contains no parseable rows")
    return rows


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
        and (entry / "sources" / "README.md").is_file()
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

    rows = _read_index_rows(readme_path)
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
    missing_canonical_readmes = sorted(
        domain
        for domain in canonical_index_set.intersection(canonical_actual_set)
        if not (canonical_root / domain / "README.md").is_file()
    )

    missing_canonical_index = sorted(paired_actual_set - canonical_index_set)
    stale_canonical_index = sorted(canonical_index_set - canonical_actual_set)
    missing_parallel_index = sorted(paired_actual_set - parallel_index_set)
    stale_parallel_index = sorted(parallel_index_set - parallel_actual_set)
    unpaired_canonical_domains = sorted(canonical_actual_set - parallel_actual_set)
    unpaired_parallel_domains = sorted(parallel_actual_set - canonical_actual_set)

    failures = (
        duplicate_index_domains
        or row_domain_mismatches
        or link_mismatches
        or missing_canonical_index
        or stale_canonical_index
        or missing_parallel_index
        or stale_parallel_index
        or missing_canonical_readmes
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
        "duplicate_index_domains": duplicate_index_domains,
        "row_domain_mismatches": row_domain_mismatches,
        "link_mismatches": link_mismatches,
        "missing_canonical_index": missing_canonical_index,
        "stale_canonical_index": stale_canonical_index,
        "missing_parallel_index": missing_parallel_index,
        "stale_parallel_index": stale_parallel_index,
        "missing_canonical_readmes": missing_canonical_readmes,
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
