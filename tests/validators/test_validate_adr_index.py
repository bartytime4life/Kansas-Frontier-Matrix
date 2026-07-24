from __future__ import annotations

from pathlib import Path

from tools.validators.validate_adr_index import validate_repository


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _adr(adr_id: str, status: str, title: str = "Decision") -> str:
    return f"""<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/{adr_id}
title: {adr_id} — {title}
type: adr
status: {status}
[/KFM_META_BLOCK_V2] -->

# {adr_id} — {title}
"""


def _row(
    adr_id: str,
    filename: str,
    effective: str,
    source: str,
    supersedes: str = "—",
    superseded_by: str = "—",
) -> str:
    return (
        f"| `{adr_id}` | [{adr_id}](./{filename}) | `{effective}` | `{source}` | "
        f"{supersedes} | {superseded_by} |"
    )


def _index(rows: list[str], scaffolds: list[str] | None = None) -> str:
    scaffold_rows = scaffolds or []
    return "\n".join(
        [
            "<!-- [KFM_META_BLOCK_V2]",
            f"numbered_records: {len(rows)}",
            f"unassigned_scaffolds: {len(scaffold_rows)}",
            "[/KFM_META_BLOCK_V2] -->",
            "# Architecture Decision Record Index",
            "<!-- ADR_INDEX_TABLE_START -->",
            "| ID | Record | Effective status | Source metadata | Supersedes | Superseded by |",
            "|---|---|---|---|---|---|",
            *rows,
            "<!-- ADR_INDEX_TABLE_END -->",
            "<!-- ADR_SCAFFOLD_TABLE_START -->",
            "| File | Classification | Decision status |",
            "|---|---|---|",
            *scaffold_rows,
            "<!-- ADR_SCAFFOLD_TABLE_END -->",
            "",
        ]
    )


def _base_repo(tmp_path: Path) -> Path:
    _write(
        tmp_path / "docs/adr/README.md",
        "# ADRs\n\nSee the [canonical ADR index](./INDEX.md).\n",
    )
    _write(
        tmp_path / "docs/registers/ADR_INDEX.md",
        "<!--\ncanonical_adr_index: ../adr/INDEX.md\n-->\n"
        "# ADR Index Cross-Register\n\n[Canonical index](../adr/INDEX.md)\n",
    )
    return tmp_path


def test_valid_index_accepts_proposed_and_draft_source_metadata(tmp_path: Path) -> None:
    root = _base_repo(tmp_path)
    first = "ADR-0001-first-decision.md"
    second = "ADR-0002-second-decision.md"
    _write(root / "docs/adr" / first, _adr("ADR-0001", "proposed", "First"))
    _write(root / "docs/adr" / second, _adr("ADR-0002", "draft", "Second"))
    _write(
        root / "docs/adr/INDEX.md",
        _index(
            [
                _row("ADR-0001", first, "proposed", "proposed"),
                _row("ADR-0002", second, "proposed", "draft"),
            ]
        ),
    )

    assert validate_repository(root) == []


def test_valid_index_accepts_legacy_proposed_meta_status(tmp_path: Path) -> None:
    root = _base_repo(tmp_path)
    filename = "ADR-0007-legacy-decision.md"
    _write(root / "docs/adr" / filename, _adr("ADR-0007", "legacy-proposed", "Legacy"))
    _write(
        root / "docs/adr/INDEX.md",
        _index([_row("ADR-0007", filename, "proposed", "legacy-proposed")]),
    )

    assert validate_repository(root) == []


def test_number_collision_is_rejected(tmp_path: Path) -> None:
    root = _base_repo(tmp_path)
    _write(root / "docs/adr/ADR-0001-first.md", _adr("ADR-0001", "proposed"))
    _write(root / "docs/adr/ADR-0001-second.md", _adr("ADR-0001", "proposed"))
    _write(
        root / "docs/adr/INDEX.md",
        _index([_row("ADR-0001", "ADR-0001-first.md", "proposed", "proposed")]),
    )

    errors = validate_repository(root)
    assert any("number collisions" in error for error in errors)


def test_missing_numbered_record_row_is_rejected(tmp_path: Path) -> None:
    root = _base_repo(tmp_path)
    _write(root / "docs/adr/ADR-0001-first.md", _adr("ADR-0001", "proposed"))
    _write(root / "docs/adr/INDEX.md", _index([]))

    errors = validate_repository(root)
    assert any("numbered ADR missing from index: ADR-0001" in error for error in errors)


def test_index_cannot_promote_source_status(tmp_path: Path) -> None:
    root = _base_repo(tmp_path)
    filename = "ADR-0001-first.md"
    _write(root / "docs/adr" / filename, _adr("ADR-0001", "proposed"))
    _write(
        root / "docs/adr/INDEX.md",
        _index([_row("ADR-0001", filename, "accepted", "proposed")]),
    )

    errors = validate_repository(root)
    assert any("does not match source-normalized 'proposed'" in error for error in errors)


def test_supersession_requires_reciprocal_link(tmp_path: Path) -> None:
    root = _base_repo(tmp_path)
    first = "ADR-0001-first.md"
    second = "ADR-0002-second.md"
    _write(root / "docs/adr" / first, _adr("ADR-0001", "superseded"))
    _write(root / "docs/adr" / second, _adr("ADR-0002", "accepted"))
    _write(
        root / "docs/adr/INDEX.md",
        _index(
            [
                _row(
                    "ADR-0001",
                    first,
                    "superseded",
                    "superseded",
                    superseded_by="ADR-0002",
                ),
                _row("ADR-0002", second, "accepted", "accepted"),
            ]
        ),
    )

    errors = validate_repository(root)
    assert any("ADR-0002 lacks reciprocal Supersedes link" in error for error in errors)


def test_unassigned_scaffold_must_be_indexed(tmp_path: Path) -> None:
    root = _base_repo(tmp_path)
    _write(
        root / "docs/adr/ADR-XXXX-future.md",
        "# Future ADR\n\n**Status:** PROPOSED scaffold.\n",
    )
    _write(root / "docs/adr/INDEX.md", _index([]))

    errors = validate_repository(root)
    assert any("unassigned ADR scaffold missing from index" in error for error in errors)


def test_register_must_not_duplicate_numbered_rows(tmp_path: Path) -> None:
    root = _base_repo(tmp_path)
    filename = "ADR-0001-first.md"
    _write(root / "docs/adr" / filename, _adr("ADR-0001", "proposed"))
    _write(
        root / "docs/adr/INDEX.md",
        _index([_row("ADR-0001", filename, "proposed", "proposed")]),
    )
    with (root / "docs/registers/ADR_INDEX.md").open("a", encoding="utf-8") as handle:
        handle.write("\n| `ADR-0001` | duplicate |\n")

    errors = validate_repository(root)
    assert any("must not duplicate numbered ADR rows" in error for error in errors)
