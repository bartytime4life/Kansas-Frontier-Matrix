#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_generate_markdown_debt_backlog_renders_ranked_table(tmp_path: Path) -> None:
    _write(tmp_path / "docs/a.md", "TODO\nTODO\nUNKNOWN\n")
    _write(tmp_path / "docs/b.md", "NEEDS VERIFICATION\n")
    _write(tmp_path / "docs/c.md", "TODO\nUNKNOWN\nNEEDS VERIFICATION\nTODO\n")

    out = tmp_path / "out.md"
    subprocess.run(
        [
            "python3",
            "tools/ci/generate_markdown_debt_backlog.py",
            "--root",
            str(tmp_path),
            "--top",
            "2",
            "--output",
            str(out.relative_to(tmp_path)),
        ],
        check=True,
    )

    text = out.read_text(encoding="utf-8")
    assert "# Markdown Debt Backlog" in text
    assert "| Rank | File | Total | TODO | UNKNOWN | NEEDS VERIFICATION |" in text
    assert "| 1 | `docs/c.md` | 4 | 2 | 1 | 1 |" in text
    assert "| 2 | `docs/a.md` | 3 | 2 | 1 | 0 |" in text


def test_generate_markdown_debt_backlog_invalid_top_fails(tmp_path: Path) -> None:
    proc = subprocess.run(
        [
            "python3",
            "tools/ci/generate_markdown_debt_backlog.py",
            "--root",
            str(tmp_path),
            "--top",
            "0",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 1
    assert "--top must be > 0" in proc.stderr
