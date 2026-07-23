#!/usr/bin/env python3
"""Validate KFM's human Architecture Decision Record control plane.

This validator is intentionally standard-library only. It verifies repository
structure and cross-file coherence; it does not accept an ADR, prove that a
decision is implemented, or authorize policy, release, or publication.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ALLOWED_EFFECTIVE_STATUSES = {"proposed", "accepted", "superseded", "rejected"}
NUMBERED_NAME_RE = re.compile(r"^ADR-(\d{4})(?:-|\s)")
PLACEHOLDER_NAME_RE = re.compile(r"^ADR-(?:NNNN|XXXX)(?:-|\s)")
ADR_REF_RE = re.compile(r"ADR-\d{4}")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\((?:<([^>]+)>|([^)]+))\)")

INDEX_START = "<!-- ADR_INDEX_TABLE_START -->"
INDEX_END = "<!-- ADR_INDEX_TABLE_END -->"
SCAFFOLD_START = "<!-- ADR_SCAFFOLD_TABLE_START -->"
SCAFFOLD_END = "<!-- ADR_SCAFFOLD_TABLE_END -->"


@dataclass(frozen=True)
class IndexRow:
    adr_id: str
    target: str
    effective_status: str
    source_metadata: str
    supersedes: tuple[str, ...]
    superseded_by: tuple[str, ...]
    line: int


@dataclass(frozen=True)
class SourceStatus:
    label: str
    effective: str


def _table_lines(text: str, start_marker: str, end_marker: str) -> list[tuple[int, str]]:
    lines = text.splitlines()
    try:
        start = lines.index(start_marker)
        end = lines.index(end_marker, start + 1)
    except ValueError as exc:
        raise ValueError(f"missing table marker: {exc}") from exc
    if end <= start + 2:
        raise ValueError(f"empty or malformed table between {start_marker} and {end_marker}")
    return [(idx + 1, lines[idx]) for idx in range(start + 1, end)]


def _cells(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def _link_target(cell: str) -> str | None:
    match = MARKDOWN_LINK_RE.search(cell)
    if not match:
        return None
    return (match.group(1) or match.group(2) or "").strip()


def _normalized_id(cell: str) -> str:
    return cell.replace("`", "").strip()


def _refs(cell: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(ADR_REF_RE.findall(cell)))


def parse_numbered_index(index_path: Path) -> tuple[list[IndexRow], list[str]]:
    errors: list[str] = []
    try:
        marked_lines = _table_lines(index_path.read_text(encoding="utf-8"), INDEX_START, INDEX_END)
    except (OSError, ValueError) as exc:
        return [], [f"{index_path}: {exc}"]

    if len(marked_lines) < 2:
        return [], [f"{index_path}: numbered table is incomplete"]

    header = _cells(marked_lines[0][1])
    expected_header = [
        "ID",
        "Record",
        "Effective status",
        "Source metadata",
        "Supersedes",
        "Superseded by",
    ]
    if header != expected_header:
        errors.append(f"{index_path}:{marked_lines[0][0]}: expected header {expected_header!r}, found {header!r}")

    rows: list[IndexRow] = []
    for line_no, line in marked_lines[2:]:
        cells = _cells(line)
        if not cells:
            continue
        if len(cells) != 6:
            errors.append(f"{index_path}:{line_no}: expected 6 cells, found {len(cells)}")
            continue
        target = _link_target(cells[1])
        if target is None:
            errors.append(f"{index_path}:{line_no}: record cell has no Markdown link")
            continue
        rows.append(
            IndexRow(
                adr_id=_normalized_id(cells[0]),
                target=target,
                effective_status=_normalized_id(cells[2]).lower(),
                source_metadata=_normalized_id(cells[3]).lower(),
                supersedes=_refs(cells[4]),
                superseded_by=_refs(cells[5]),
                line=line_no,
            )
        )
    return rows, errors


def parse_scaffold_index(index_path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    try:
        marked_lines = _table_lines(index_path.read_text(encoding="utf-8"), SCAFFOLD_START, SCAFFOLD_END)
    except (OSError, ValueError) as exc:
        return {}, [f"{index_path}: {exc}"]

    header = _cells(marked_lines[0][1])
    expected_header = ["File", "Classification", "Decision status"]
    if header != expected_header:
        errors.append(f"{index_path}:{marked_lines[0][0]}: expected header {expected_header!r}, found {header!r}")

    rows: dict[str, str] = {}
    for line_no, line in marked_lines[2:]:
        cells = _cells(line)
        if not cells:
            continue
        if len(cells) != 3:
            errors.append(f"{index_path}:{line_no}: expected 3 scaffold cells, found {len(cells)}")
            continue
        target = _link_target(cells[0])
        if target is None:
            errors.append(f"{index_path}:{line_no}: scaffold cell has no Markdown link")
            continue
        filename = Path(target).name
        if filename in rows:
            errors.append(f"{index_path}:{line_no}: duplicate scaffold row for {filename}")
        rows[filename] = _normalized_id(cells[2]).lower()
        if rows[filename] != "not-assigned":
            errors.append(f"{index_path}:{line_no}: scaffold {filename} must be not-assigned")
    return rows, errors


def source_status(path: Path) -> SourceStatus:
    text = path.read_text(encoding="utf-8")
    meta_match = re.search(r"\[KFM_META_BLOCK_V2\](.*?)\[/KFM_META_BLOCK_V2\]", text, re.DOTALL)
    if meta_match:
        status_match = re.search(r"(?mi)^status:\s*([^\n#]+)", meta_match.group(1))
        if status_match:
            raw = status_match.group(1).strip().strip('"\'').lower()
            raw = raw.split(";", 1)[0].strip()
            if raw in {"draft", "proposed"}:
                return SourceStatus(label=raw, effective="proposed")
            if raw in ALLOWED_EFFECTIVE_STATUSES:
                return SourceStatus(label=raw, effective=raw)
            raise ValueError(f"unsupported KFM meta status {raw!r}")

    legacy_match = re.search(r"(?mi)^adr_status:\s*([^\n#]+)", text[:6000])
    if legacy_match:
        raw = legacy_match.group(1).strip().lower()
        if raw == "proposed":
            return SourceStatus(label="legacy-proposed", effective="proposed")
        if raw in ALLOWED_EFFECTIVE_STATUSES:
            return SourceStatus(label=f"legacy-{raw}", effective=raw)
        raise ValueError(f"unsupported legacy adr_status {raw!r}")

    raise ValueError("no supported ADR source-status field")


def _numbered_files(adr_dir: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    collisions: dict[str, list[Path]] = {}
    for path in sorted(adr_dir.glob("ADR-*.md")):
        match = NUMBERED_NAME_RE.match(path.name)
        if not match:
            continue
        adr_id = f"ADR-{match.group(1)}"
        if adr_id in result:
            collisions.setdefault(adr_id, [result[adr_id]]).append(path)
        else:
            result[adr_id] = path
    if collisions:
        rendered = "; ".join(
            f"{adr_id}: {[path.name for path in paths]}" for adr_id, paths in sorted(collisions.items())
        )
        raise ValueError(f"number collisions: {rendered}")
    return result


def _scaffold_files(adr_dir: Path) -> set[str]:
    scaffolds: set[str] = set()
    for path in adr_dir.glob("ADR-*.md"):
        if path.name == "ADR-template.md" or NUMBERED_NAME_RE.match(path.name):
            continue
        if PLACEHOLDER_NAME_RE.match(path.name):
            scaffolds.add(path.name)
            continue
        text = path.read_text(encoding="utf-8")
        if "PROPOSED scaffold" in text:
            scaffolds.add(path.name)
    return scaffolds


def _validate_supersession(rows: Iterable[IndexRow], errors: list[str]) -> None:
    row_map = {row.adr_id: row for row in rows}
    for row in row_map.values():
        for ref in (*row.supersedes, *row.superseded_by):
            if ref == row.adr_id:
                errors.append(f"{row.adr_id}: supersession relationship cannot reference itself")
            elif ref not in row_map:
                errors.append(f"{row.adr_id}: supersession reference does not resolve: {ref}")

        if row.effective_status == "superseded" and len(row.superseded_by) != 1:
            errors.append(f"{row.adr_id}: superseded status requires exactly one Superseded by reference")
        if row.effective_status != "superseded" and row.superseded_by:
            errors.append(f"{row.adr_id}: Superseded by is set but effective status is {row.effective_status}")

        for predecessor in row.supersedes:
            previous = row_map.get(predecessor)
            if previous and row.adr_id not in previous.superseded_by:
                errors.append(f"{row.adr_id}: {predecessor} lacks reciprocal Superseded by link")
        for successor in row.superseded_by:
            next_row = row_map.get(successor)
            if next_row and row.adr_id not in next_row.supersedes:
                errors.append(f"{row.adr_id}: {successor} lacks reciprocal Supersedes link")


def validate_repository(repo_root: Path) -> list[str]:
    root = repo_root.resolve()
    adr_dir = root / "docs/adr"
    index_path = adr_dir / "INDEX.md"
    readme_path = adr_dir / "README.md"
    register_path = root / "docs/registers/ADR_INDEX.md"
    errors: list[str] = []

    for required in (adr_dir, index_path, readme_path, register_path):
        if not required.exists():
            errors.append(f"required path missing: {required.relative_to(root)}")
    if errors:
        return errors

    try:
        files = _numbered_files(adr_dir)
    except ValueError as exc:
        errors.append(str(exc))
        files = {}

    rows, parse_errors = parse_numbered_index(index_path)
    errors.extend(parse_errors)
    row_map: dict[str, IndexRow] = {}
    for row in rows:
        if row.adr_id in row_map:
            errors.append(f"{index_path.relative_to(root)}:{row.line}: duplicate index ID {row.adr_id}")
        row_map[row.adr_id] = row

    file_ids = set(files)
    row_ids = set(row_map)
    for adr_id in sorted(file_ids - row_ids):
        errors.append(f"numbered ADR missing from index: {adr_id} ({files[adr_id].name})")
    for adr_id in sorted(row_ids - file_ids):
        errors.append(f"index row has no numbered ADR file: {adr_id}")

    for adr_id in sorted(file_ids & row_ids):
        path = files[adr_id]
        row = row_map[adr_id]
        expected_target = f"./{path.name}"
        if row.target != expected_target:
            errors.append(f"{adr_id}: index target {row.target!r} does not match {expected_target!r}")
        resolved = (index_path.parent / row.target).resolve()
        if resolved != path.resolve() or not resolved.is_file():
            errors.append(f"{adr_id}: index link does not resolve to its ADR file")

        h1_match = re.search(r"(?m)^#\s+.*\b(ADR-\d{4})\b", path.read_text(encoding="utf-8"))
        if not h1_match or h1_match.group(1) != adr_id:
            found = h1_match.group(1) if h1_match else "none"
            errors.append(f"{path.name}: H1 ADR ID mismatch; expected {adr_id}, found {found}")

        if row.effective_status not in ALLOWED_EFFECTIVE_STATUSES:
            errors.append(f"{adr_id}: invalid effective status {row.effective_status!r}")
        try:
            source = source_status(path)
        except ValueError as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        if row.source_metadata != source.label:
            errors.append(
                f"{adr_id}: index source metadata {row.source_metadata!r} does not match {source.label!r}"
            )
        if row.effective_status != source.effective:
            errors.append(
                f"{adr_id}: effective status {row.effective_status!r} does not match source-normalized {source.effective!r}"
            )

    scaffold_rows, scaffold_errors = parse_scaffold_index(index_path)
    errors.extend(scaffold_errors)
    actual_scaffolds = _scaffold_files(adr_dir)
    indexed_scaffolds = set(scaffold_rows)
    for filename in sorted(actual_scaffolds - indexed_scaffolds):
        errors.append(f"unassigned ADR scaffold missing from index: {filename}")
    for filename in sorted(indexed_scaffolds - actual_scaffolds):
        errors.append(f"scaffold index row does not resolve to an unassigned scaffold: {filename}")

    index_text = index_path.read_text(encoding="utf-8")
    count_match = re.search(r"(?m)^numbered_records:\s*(\d+)\s*$", index_text)
    scaffold_count_match = re.search(r"(?m)^unassigned_scaffolds:\s*(\d+)\s*$", index_text)
    if not count_match or int(count_match.group(1)) != len(files):
        errors.append(f"INDEX.md numbered_records metadata must equal {len(files)}")
    if not scaffold_count_match or int(scaffold_count_match.group(1)) != len(actual_scaffolds):
        errors.append(f"INDEX.md unassigned_scaffolds metadata must equal {len(actual_scaffolds)}")

    register_text = register_path.read_text(encoding="utf-8")
    if "canonical_adr_index: ../adr/INDEX.md" not in register_text:
        errors.append("docs/registers/ADR_INDEX.md lacks canonical_adr_index pointer")
    if "../adr/INDEX.md" not in register_text:
        errors.append("docs/registers/ADR_INDEX.md does not link to the canonical index")
    if INDEX_START in register_text or re.search(r"(?m)^\|\s*`?ADR-\d{4}", register_text):
        errors.append("docs/registers/ADR_INDEX.md must not duplicate numbered ADR rows")

    readme_text = readme_path.read_text(encoding="utf-8")
    if "[canonical ADR index](./INDEX.md)" not in readme_text:
        errors.append("docs/adr/README.md lacks the canonical ADR index link")

    _validate_supersession(rows, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root (default: current directory)",
    )
    args = parser.parse_args(argv)
    errors = validate_repository(args.repo_root)
    if errors:
        print("FAIL: ADR index coherence")
        for error in errors:
            print(f"- {error}")
        return 1

    adr_dir = args.repo_root.resolve() / "docs/adr"
    numbered = len(_numbered_files(adr_dir))
    scaffolds = len(_scaffold_files(adr_dir))
    print(f"PASS: ADR index coherence ({numbered} numbered records, {scaffolds} unassigned scaffolds)")
    print("BOUNDARY: coherence is not ADR acceptance, implementation proof, release approval, or publication authority")
    return 0


if __name__ == "__main__":
    sys.exit(main())
