from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

PROFILE = "kfm.crosswalk-registry-inventory-drift.v4"
SECTION_TITLE = "Current inventory"
SECTION_HEADER = f"## {SECTION_TITLE}"
FENCE_OPEN_RE = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,}).*$")
ATX_H2_RE = re.compile(r"^ {0,3}##(?:[ \t]+(?P<title>.*?)[ \t]*|[ \t]*)$")
CLOSING_HASH_RE = re.compile(r"[ \t]+#+[ \t]*$")
ROW_RE = re.compile(r"^\|\s*\[`([^`]+)`\]\(([^)]+)\)\s*\|")
TABLE_SEPARATOR_RE = re.compile(
    r"^\|\s*:?-+:?\s*(?:\|\s*:?-+:?\s*)+\|?$"
)


def _visible_line_spans(text: str) -> list[tuple[int, int, str]]:
    visible: list[tuple[int, int, str]] = []
    fence_char: str | None = None
    fence_length = 0
    offset = 0
    for raw_line in text.splitlines(keepends=True):
        line = raw_line.rstrip("\r\n")
        if fence_char is not None:
            if re.fullmatch(
                rf" {{0,3}}{re.escape(fence_char)}{{{fence_length},}}[ \t]*",
                line,
            ):
                fence_char = None
                fence_length = 0
        else:
            opening = FENCE_OPEN_RE.match(line)
            if opening is not None:
                fence = opening.group("fence")
                fence_char = fence[0]
                fence_length = len(fence)
            else:
                visible.append((offset, offset + len(line), line))
        offset += len(raw_line)
    return visible


def _h2_spans(text: str) -> list[tuple[int, int, str]]:
    headings: list[tuple[int, int, str]] = []
    for start, end, line in _visible_line_spans(text):
        heading = ATX_H2_RE.match(line)
        if heading is None:
            continue
        title = heading.group("title") or ""
        title = CLOSING_HASH_RE.sub("", title).strip(" \t")
        headings.append((start, end, title))
    return headings


def _read_inventory_rows(
    readme_path: Path,
) -> tuple[list[dict[str, str]], list[str]]:
    text = readme_path.read_text(encoding="utf-8")
    headings = _h2_spans(text)
    section_matches = [heading for heading in headings if heading[2] == SECTION_TITLE]
    if not section_matches:
        raise ValueError(f"missing section marker: {SECTION_HEADER}")
    if len(section_matches) > 1:
        raise ValueError(f"duplicate section marker: {SECTION_HEADER}")
    section_start = section_matches[0][1]
    section_end = next(
        (start for start, _, _ in headings if start > section_start),
        len(text),
    )
    section_lines = [
        line
        for start, _, line in _visible_line_spans(text)
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
        label, link = match.groups()
        rows.append({"label": label, "link": link})
    if not rows and not invalid_rows:
        raise ValueError("crosswalk registry inventory contains no parseable rows")
    return rows, sorted(invalid_rows)


def _actual_inventory(repo_root: Path) -> list[str]:
    root = repo_root / "data" / "registry" / "crosswalks"
    if not root.is_dir():
        raise ValueError(f"crosswalk registry root is not a directory: {root}")

    paths: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part.startswith(".") for part in relative.parts):
            continue
        paths.append(relative.as_posix())
    return sorted(paths)


def validate_crosswalk_registry_inventory(
    repo_root: Path,
    *,
    readme_path: Path | None = None,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    root = repo_root / "data" / "registry" / "crosswalks"
    readme_path = (readme_path or root / "README.md").resolve()

    rows, invalid_inventory_rows = _read_inventory_rows(readme_path)
    indexed_paths = [row["link"] for row in rows]
    indexed_labels = [row["label"] for row in rows]
    actual_paths = _actual_inventory(repo_root)

    counts = Counter(indexed_paths)
    duplicate_index_paths = sorted(path for path, count in counts.items() if count > 1)
    label_link_mismatches = sorted(
        f"{row['label']}!={row['link']}"
        for row in rows
        if row["label"] != row["link"]
    )

    indexed_set = set(indexed_paths)
    actual_set = set(actual_paths)
    unindexed_paths = sorted(actual_set - indexed_set)
    stale_index_paths = sorted(indexed_set - actual_set)

    child_lanes = sorted(
        {
            Path(path).parts[0]
            for path in actual_paths
            if len(Path(path).parts) > 1
        }
    )
    missing_child_readmes = sorted(
        lane for lane in child_lanes if f"{lane}/README.md" not in actual_set
    )

    failures = (
        invalid_inventory_rows
        or duplicate_index_paths
        or label_link_mismatches
        or unindexed_paths
        or stale_index_paths
        or missing_child_readmes
    )

    return {
        "profile": PROFILE,
        "outcome": "FAIL" if failures else "PASS",
        "authority_created": False,
        "repo_root": str(repo_root),
        "readme": str(readme_path),
        "indexed_paths": indexed_paths,
        "indexed_labels": indexed_labels,
        "actual_paths": actual_paths,
        "invalid_inventory_rows": invalid_inventory_rows,
        "duplicate_index_paths": duplicate_index_paths,
        "label_link_mismatches": label_link_mismatches,
        "unindexed_paths": unindexed_paths,
        "stale_index_paths": stale_index_paths,
        "child_lanes": child_lanes,
        "missing_child_readmes": missing_child_readmes,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that data/registry/crosswalks/README.md inventory rows match "
            "the current non-hidden crosswalk registry files without creating "
            "crosswalk or catalog authority."
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
        report = validate_crosswalk_registry_inventory(
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
