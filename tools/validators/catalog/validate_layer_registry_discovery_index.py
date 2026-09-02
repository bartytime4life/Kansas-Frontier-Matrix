from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

PROFILE = "kfm.layer-registry-discovery-index-drift.v7"
SECTION_TITLE = "Confirmed child lanes"
SECTION_HEADER = f"## {SECTION_TITLE}"
FENCE_OPEN_RE = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,}).*$")
ATX_H2_RE = re.compile(r"^ {0,3}##(?:[ \t]+(?P<title>.*?)[ \t]*|[ \t]*)$")
CLOSING_HASH_RE = re.compile(r"[ \t]+#+[ \t]*$")
ROW_RE = re.compile(r"^\|\s*\[`([^`]+/)`\]\(([^)]+)\)\s*\|")


def _visible_line_spans(text: str) -> list[tuple[int, int, str]]:
    visible: list[tuple[int, int, str]] = []
    fence_char: str | None = None
    fence_length = 0
    offset = 0
    for raw_line in text.splitlines(keepends=True):
        line = raw_line.rstrip("\r\n")
        if fence_char is not None:
            closing = re.fullmatch(
                rf" {{0,3}}{re.escape(fence_char)}{{{fence_length},}}[ \t]*",
                line,
            )
            if closing is not None:
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
        if heading is not None:
            title = heading.group("title") or ""
            title = CLOSING_HASH_RE.sub("", title).strip(" \t")
            headings.append((start, end, title))
    return headings


def _read_indexed_lanes(readme_path: Path) -> tuple[list[str], list[str]]:
    text = readme_path.read_text(encoding="utf-8")
    headings = _h2_spans(text)
    section_matches = [heading for heading in headings if heading[2] == SECTION_TITLE]
    if len(section_matches) > 1:
        raise ValueError(f"duplicate section: {SECTION_HEADER}")
    if not section_matches:
        raise ValueError(f"missing section: {SECTION_HEADER}")
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

    lanes: list[str] = []
    invalid_link_rows: list[str] = []
    for line in section_lines:
        stripped = line.strip()
        if not stripped.startswith("| [`"):
            continue
        match = ROW_RE.match(line)
        if match is None:
            invalid_link_rows.append(stripped)
            continue
        lane, destination = match.groups()
        if destination != f"{lane}README.md":
            invalid_link_rows.append(stripped)
            continue
        lanes.append(lane)
    if not lanes and not invalid_link_rows:
        raise ValueError("layer registry child-lane index contains no parseable lane rows")
    return lanes, sorted(invalid_link_rows)


def _read_actual_lanes(registry_root: Path) -> list[str]:
    if not registry_root.is_dir():
        raise ValueError(f"layer registry root is not a directory: {registry_root}")
    return sorted(
        f"{entry.name}/"
        for entry in registry_root.iterdir()
        if entry.is_dir() and not entry.name.startswith(".")
    )


def validate_layer_registry_discovery_index(
    registry_root: Path,
    *,
    readme_path: Path | None = None,
) -> dict[str, Any]:
    registry_root = registry_root.resolve()
    readme_path = (readme_path or registry_root / "README.md").resolve()

    indexed, invalid_link_rows = _read_indexed_lanes(readme_path)
    actual = _read_actual_lanes(registry_root)
    counts = Counter(indexed)
    duplicates = sorted(name for name, count in counts.items() if count > 1)
    indexed_unique = set(indexed)
    actual_set = set(actual)
    missing_from_index = sorted(actual_set - indexed_unique)
    stale_index_entries = sorted(indexed_unique - actual_set)
    missing_child_readmes = sorted(
        lane
        for lane in indexed_unique.intersection(actual_set)
        if not (registry_root / lane.rstrip("/") / "README.md").is_file()
    )

    outcome = (
        "PASS"
        if not (
            duplicates
            or invalid_link_rows
            or missing_from_index
            or stale_index_entries
            or missing_child_readmes
        )
        else "FAIL"
    )
    return {
        "profile": PROFILE,
        "outcome": outcome,
        "authority_created": False,
        "registry_root": str(registry_root),
        "readme": str(readme_path),
        "actual_children": actual,
        "indexed_children": indexed,
        "duplicate_entries": duplicates,
        "invalid_link_rows": invalid_link_rows,
        "missing_from_index": missing_from_index,
        "stale_index_entries": stale_index_entries,
        "missing_child_readmes": missing_child_readmes,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that data/registry/layers Confirmed child lanes matches "
            "the direct layer-registry domain directories."
        )
    )
    default_root = Path(__file__).resolve().parents[3] / "data" / "registry" / "layers"
    parser.add_argument("--registry-root", type=Path, default=default_root)
    parser.add_argument("--readme", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        report = validate_layer_registry_discovery_index(
            args.registry_root,
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
