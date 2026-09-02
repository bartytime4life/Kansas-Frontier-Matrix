from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

PROFILE = "kfm.catalog-domain-child-index-drift.v3"
SECTION_TITLE = "Known child lanes"
SECTION_HEADER = f"## {SECTION_TITLE}"
SECTION_HEADER_RE = re.compile(
    rf"(?m)^##[ \t]+{re.escape(SECTION_TITLE)}(?:[ \t]+#+)?[ \t]*$"
)
NEXT_H2_RE = re.compile(r"(?m)^##(?:[ \t]+|$)")
ROW_RE = re.compile(r"^\|\s*`([^`]+/)`\s*\|")


def _read_indexed_lanes(readme_path: Path) -> list[str]:
    text = readme_path.read_text(encoding="utf-8")
    section_matches = list(SECTION_HEADER_RE.finditer(text))
    if len(section_matches) > 1:
        raise ValueError(f"duplicate section: {SECTION_HEADER}")
    if not section_matches:
        raise ValueError(f"missing section: {SECTION_HEADER}")
    section = text[section_matches[0].end():]
    next_h2 = NEXT_H2_RE.search(section)
    if next_h2 is not None:
        section = section[:next_h2.start()]

    lanes: list[str] = []
    for line in section.splitlines():
        match = ROW_RE.match(line)
        if match:
            lanes.append(match.group(1))
    if not lanes:
        raise ValueError("domain child-lane index contains no parseable lane rows")
    return lanes


def _read_actual_lanes(domain_root: Path) -> list[str]:
    if not domain_root.is_dir():
        raise ValueError(f"domain catalog root is not a directory: {domain_root}")
    return sorted(
        f"{entry.name}/"
        for entry in domain_root.iterdir()
        if entry.is_dir() and not entry.name.startswith(".")
    )


def validate_catalog_domain_child_index(
    domain_root: Path,
    *,
    readme_path: Path | None = None,
) -> dict[str, Any]:
    domain_root = domain_root.resolve()
    readme_path = (readme_path or domain_root / "README.md").resolve()

    indexed = _read_indexed_lanes(readme_path)
    actual = _read_actual_lanes(domain_root)
    counts = Counter(indexed)
    duplicates = sorted(name for name, count in counts.items() if count > 1)
    indexed_unique = set(indexed)
    actual_set = set(actual)
    missing_from_index = sorted(actual_set - indexed_unique)
    stale_index_entries = sorted(indexed_unique - actual_set)

    outcome = (
        "PASS"
        if not (duplicates or missing_from_index or stale_index_entries)
        else "FAIL"
    )
    return {
        "profile": PROFILE,
        "outcome": outcome,
        "authority_created": False,
        "domain_root": str(domain_root),
        "readme": str(readme_path),
        "actual_children": actual,
        "indexed_children": indexed,
        "duplicate_entries": duplicates,
        "missing_from_index": missing_from_index,
        "stale_index_entries": stale_index_entries,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that the canonical data/catalog/domain Known child lanes "
            "index matches the direct domain catalog directories."
        )
    )
    default_root = Path(__file__).resolve().parents[3] / "data" / "catalog" / "domain"
    parser.add_argument("--domain-root", type=Path, default=default_root)
    parser.add_argument("--readme", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        report = validate_catalog_domain_child_index(
            args.domain_root,
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
