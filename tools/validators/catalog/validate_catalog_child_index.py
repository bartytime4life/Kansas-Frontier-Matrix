from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

PROFILE = "kfm.catalog-child-index-drift.v5"
SECTION_TITLE = "Current bounded child-lane index"
SECTION_HEADER = f"## {SECTION_TITLE}"
FENCE_OPEN_RE = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,}).*$")
ATX_H2_RE = re.compile(r"^ {0,3}##(?:[ \t]+(?P<title>.*?)[ \t]*|[ \t]*)$")
CLOSING_HASH_RE = re.compile(r"[ \t]+#+[ \t]*$")
ROW_RE = re.compile(r"^\|\s*`([^`]+/)`\s*\|\s*(.*?)\s*\|\s*$")
ALIAS_TARGET_RE = re.compile(
    r"`PROPOSED\s*/\s*COMPATIBILITY-ALIAS`\s+to\s+`([^`]+/)`",
    re.IGNORECASE,
)


def _h2_spans(text: str) -> list[tuple[int, int, str]]:
    headings: list[tuple[int, int, str]] = []
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
                heading = ATX_H2_RE.match(line)
                if heading is not None:
                    title = heading.group("title") or ""
                    title = CLOSING_HASH_RE.sub("", title).strip(" \t")
                    headings.append((offset, offset + len(line), title))
        offset += len(raw_line)
    return headings


def _read_index_rows(readme_path: Path) -> list[tuple[str, str]]:
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
    section = text[section_start:section_end]

    rows: list[tuple[str, str]] = []
    for line in section.splitlines():
        match = ROW_RE.match(line)
        if match:
            rows.append((match.group(1), match.group(2).strip()))
    if not rows:
        raise ValueError("child-lane index contains no parseable lane rows")
    return rows


def _read_actual_lanes(catalog_root: Path) -> list[str]:
    if not catalog_root.is_dir():
        raise ValueError(f"catalog root is not a directory: {catalog_root}")
    return sorted(
        f"{entry.name}/"
        for entry in catalog_root.iterdir()
        if entry.is_dir() and not entry.name.startswith(".")
    )


def _resolve_catalog_relative(catalog_root: Path, lane: str) -> Path:
    if not lane.endswith("/"):
        raise ValueError(f"catalog lane must end with '/': {lane}")
    relative = Path(lane.rstrip("/"))
    if relative.is_absolute() or not relative.parts or any(
        part in {"", ".", ".."} for part in relative.parts
    ):
        raise ValueError(f"unsafe catalog-relative lane: {lane}")
    resolved = (catalog_root / relative).resolve()
    try:
        resolved.relative_to(catalog_root)
    except ValueError as exc:
        raise ValueError(f"catalog lane escapes root: {lane}") from exc
    return resolved


def _read_compatibility_aliases(
    rows: list[tuple[str, str]],
) -> tuple[dict[str, str], list[str]]:
    aliases: dict[str, str] = {}
    invalid: list[str] = []
    for lane, posture in rows:
        if "COMPATIBILITY-ALIAS" not in posture.upper():
            continue
        match = ALIAS_TARGET_RE.search(posture)
        if match is None:
            invalid.append(lane)
            continue
        aliases[lane] = match.group(1)
    return aliases, sorted(invalid)


def validate_catalog_child_index(
    catalog_root: Path,
    *,
    readme_path: Path | None = None,
) -> dict[str, Any]:
    catalog_root = catalog_root.resolve()
    readme_path = (readme_path or catalog_root / "README.md").resolve()

    rows = _read_index_rows(readme_path)
    indexed = [lane for lane, _ in rows]
    actual = _read_actual_lanes(catalog_root)
    counts = Counter(indexed)
    duplicates = sorted(name for name, count in counts.items() if count > 1)
    indexed_unique = set(indexed)
    actual_set = set(actual)
    missing_from_index = sorted(actual_set - indexed_unique)
    stale_index_entries = sorted(indexed_unique - actual_set)

    aliases, invalid_alias_entries = _read_compatibility_aliases(rows)
    missing_alias_targets: list[str] = []
    missing_alias_readmes: list[str] = []
    alias_target_not_documented: list[str] = []
    alias_targets_are_aliases: list[str] = []

    alias_lanes = set(aliases)
    for alias, target in sorted(aliases.items()):
        try:
            alias_dir = _resolve_catalog_relative(catalog_root, alias)
            target_dir = _resolve_catalog_relative(catalog_root, target)
        except ValueError:
            invalid_alias_entries.append(alias)
            continue

        if not target_dir.is_dir():
            missing_alias_targets.append(f"{alias} -> {target}")

        alias_readme = alias_dir / "README.md"
        if not alias_readme.is_file():
            missing_alias_readmes.append(alias)
        else:
            alias_text = alias_readme.read_text(encoding="utf-8")
            canonical_reference = f"`data/catalog/{target}`"
            if canonical_reference not in alias_text:
                alias_target_not_documented.append(f"{alias} -> {target}")

        target_root = f"{Path(target.rstrip('/')).parts[0]}/"
        if target_root in alias_lanes:
            alias_targets_are_aliases.append(f"{alias} -> {target}")

    invalid_alias_entries = sorted(set(invalid_alias_entries))
    outcome = (
        "PASS"
        if not (
            duplicates
            or missing_from_index
            or stale_index_entries
            or invalid_alias_entries
            or missing_alias_targets
            or missing_alias_readmes
            or alias_target_not_documented
            or alias_targets_are_aliases
        )
        else "FAIL"
    )
    return {
        "profile": PROFILE,
        "outcome": outcome,
        "authority_created": False,
        "catalog_root": str(catalog_root),
        "readme": str(readme_path),
        "actual_children": actual,
        "indexed_children": indexed,
        "duplicate_entries": duplicates,
        "missing_from_index": missing_from_index,
        "stale_index_entries": stale_index_entries,
        "compatibility_aliases": [
            {"alias": alias, "canonical_target": target}
            for alias, target in sorted(aliases.items())
        ],
        "invalid_alias_entries": invalid_alias_entries,
        "missing_alias_targets": missing_alias_targets,
        "missing_alias_readmes": missing_alias_readmes,
        "alias_target_not_documented": alias_target_not_documented,
        "alias_targets_are_aliases": alias_targets_are_aliases,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate the canonical data/catalog direct-child discovery index "
            "and its compatibility-alias targets."
        )
    )
    default_root = Path(__file__).resolve().parents[3] / "data" / "catalog"
    parser.add_argument("--catalog-root", type=Path, default=default_root)
    parser.add_argument("--readme", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        report = validate_catalog_child_index(
            args.catalog_root,
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
