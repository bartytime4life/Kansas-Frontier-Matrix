from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "tools" / "docs" / "wiki" / "sync_kfm_github_wiki.ps1"
EXPECTED_SOURCE_COMMIT = "3b2c4dc05a2a30ed045e7a04a6d15d103ce83a0d"
EXPECTED_PAGES = [
    "Home.md",
    "Getting-Started.md",
    "Project-Status.md",
    "Architecture.md",
    "Repository-Map.md",
    "Governance-and-Evidence.md",
    "Data-Lifecycle.md",
    "Domains.md",
    "Map-UI-and-AI.md",
    "Security-and-Sensitivity.md",
    "Development-and-Validation.md",
    "Contributing.md",
    "Glossary.md",
    "Wiki-Maintenance.md",
    "_Sidebar.md",
    "_Footer.md",
]


def _script_text() -> str:
    return SCRIPT.read_text(encoding="utf-8")


def test_wiki_sync_defaults_to_a_no_push_plan() -> None:
    text = _script_text()

    assert "[switch]$Publish" in text
    assert "if (-not $Publish)" in text
    assert "Outcome: PLANNED" in text
    assert text.index("if (-not $Publish)") < text.index('@("push", "origin"')


def test_wiki_sync_uses_an_exact_reviewed_source_commit() -> None:
    text = _script_text()

    assert EXPECTED_SOURCE_COMMIT in text
    assert 'ValidatePattern("^[0-9a-fA-F]{40}$")' in text
    assert "Source checkout mismatch" in text


def test_wiki_sync_page_allowlist_is_exact() -> None:
    text = _script_text()
    match = re.search(r"\$Pages\s*=\s*@\((.*?)\n\)", text, flags=re.DOTALL)

    assert match is not None
    pages = re.findall(r'"([^"]+\.md)"', match.group(1))
    assert pages == EXPECTED_PAGES
    assert "README.md" not in pages
    assert "Unexpected wiki paths changed" in text
    assert "Unexpected wiki paths staged" in text


def test_wiki_sync_never_force_pushes_or_rewrites_history() -> None:
    text = _script_text().lower()
    banned = (
        "push --force",
        "push -f",
        '"--force-with-lease"',
        '"reset", "--hard"',
        '"clean", "-fd"',
    )

    for token in banned:
        assert token not in text


def test_wiki_sync_requires_remote_commit_readback() -> None:
    text = _script_text()

    assert '@("ls-remote", "--heads", "origin", "refs/heads/$WikiBranch")' in text
    assert "Remote readback mismatch" in text
    assert "Outcome: APPLIED" in text
