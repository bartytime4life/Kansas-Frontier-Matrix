from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPT = REPO_ROOT / "tools" / "docs" / "wiki" / "sync_kfm_github_wiki.ps1"
EXPECTED_SOURCE_COMMIT = "3b2c4dc05a2a30ed045e7a04a6d15d103ce83a0d"
EXPECTED_PAGES = [
    "Home.md",
    "Builder-Profile.md",
    "Visual-Tour.md",
    "Engineering-Case-Studies.md",
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


def test_native_projection_rewrites_only_allowlisted_link_destinations(tmp_path) -> None:
    import shutil
    import subprocess
    import pytest

    pwsh = shutil.which("pwsh")
    if not pwsh:
        pytest.skip("PowerShell is required for the executable projection check")
    source = _script_text()
    function = source[source.index("function Convert-WikiLinks {"):source.index("function Invoke-Git {")]
    probe = tmp_path / "probe.ps1"
    probe.write_text(function + r'''
$InputText = '[Home](Home.md) [section](Home.md#top) <a href="Home.md">home</a> [external](https://example.org/Home.md) [nested](nested/Home.md) [unknown](Other.md) [contract](README.md)'
Convert-WikiLinks -Content $InputText -PageNames @("Home.md") -SourceRef "source-pin"
''', encoding="utf-8")
    result = subprocess.run([pwsh, "-NoProfile", "-File", str(probe)], capture_output=True, text=True, check=True).stdout
    target = "https://github.com/bartytime4life/Kansas-Frontier-Matrix/wiki/Home"
    assert f"[Home]({target})" in result
    assert f"[section]({target}#top)" in result
    assert f'<a href="{target}">' in result
    assert "[external](https://example.org/Home.md)" in result
    assert "[nested](nested/Home.md)" in result
    assert "[unknown](Other.md)" in result
    assert "/blob/source-pin/docs/wiki/README.md)" in result


def test_scalar_git_outputs_are_wrapped_before_indexing() -> None:
    text = _script_text()
    for name in ("ResolvedSourceCommit", "WikiBranch", "WikiCommit", "RemoteReadback"):
        assert f"${name} = @(Get-GitLines" in text


def test_renamed_sources_keep_native_routes_and_historical_replay(tmp_path) -> None:
    import json
    import shutil
    import subprocess
    import pytest

    pwsh = shutil.which("pwsh")
    if not pwsh:
        pytest.skip("PowerShell is required for the executable projection check")
    source = _script_text()
    functions = source[source.index("$SourcePageNames = @{"):source.index("function Invoke-Git {")]
    old_dir = tmp_path / "historical"
    new_dir = tmp_path / "current"
    old_dir.mkdir()
    new_dir.mkdir()
    native_pages = ["Builder-Profile.md", "Visual-Tour.md", "Engineering-Case-Studies.md"]
    for name in native_pages:
        (old_dir / name).write_text("historical", encoding="utf-8")
        # Prefer the canonical file even if both exist in a checkout.
        (new_dir / name).write_text("legacy", encoding="utf-8")
        (new_dir / name.lower()).write_text("canonical", encoding="utf-8")
    probe = tmp_path / "renamed-sources.ps1"
    probe.write_text(r'''param([string]$OldDir, [string]$NewDir)
''' + functions + r'''
$Results = foreach ($Page in @("Builder-Profile.md", "Visual-Tour.md", "Engineering-Case-Studies.md")) {
    $OldPath = Resolve-WikiSourcePage -SourceWikiDir $OldDir -Page $Page -SourcePageNames $SourcePageNames
    $NewPath = Resolve-WikiSourcePage -SourceWikiDir $NewDir -Page $Page -SourcePageNames $SourcePageNames
    $Name = $SourcePageNames[$Page]
    $InputText = "[current]($Name#top) [historical]($Page) <a href=`"$Name#anchor`">html</a> [external](https://example.org/$Name) [nested](nested/$Name) [unknown](other.md)"
    @{
        page = $Page
        old = [System.IO.File]::ReadAllText($OldPath)
        current = [System.IO.File]::ReadAllText($NewPath)
        projected = Convert-WikiLinks -Content $InputText -PageNames @($Page) -SourceRef "source-pin" -SourcePageNames $SourcePageNames
    }
}
ConvertTo-Json -InputObject @($Results)
''', encoding="utf-8")
    result = subprocess.run(
        [pwsh, "-NoProfile", "-File", str(probe), str(old_dir), str(new_dir)],
        capture_output=True, text=True, check=True,
    )
    rows = json.loads(result.stdout)
    assert len(rows) == 3
    for row in rows:
        name = row["page"]
        assert row["old"] == "historical"
        assert row["current"] == "canonical"
        target = f"https://github.com/bartytime4life/Kansas-Frontier-Matrix/wiki/{Path(name).stem}"
        projected = row["projected"]
        assert f"[current]({target}#top)" in projected
        assert f"[historical]({target})" in projected
        assert f'<a href="{target}#anchor">' in projected
        assert f"[external](https://example.org/{name.lower()})" in projected
        assert f"[nested](nested/{name.lower()})" in projected
        assert "[unknown](other.md)" in projected


def test_wiki_source_links_resolve_with_exact_case() -> None:
    wiki = REPO_ROOT / "docs/wiki"
    filenames = {path.name for path in wiki.glob("*.md")}
    for page in wiki.glob("*.md"):
        for target in re.findall(r'\]\(([A-Za-z0-9_-]+\.md)(?:#[^)]*)?\)', page.read_text(encoding="utf-8")):
            assert target in filenames, f"{page.name} links to missing {target}"
