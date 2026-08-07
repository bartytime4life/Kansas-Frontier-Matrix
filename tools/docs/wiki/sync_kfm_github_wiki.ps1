<#
.SYNOPSIS
Stages the reviewed KFM wiki source set and optionally synchronizes it to the native GitHub Wiki.

.DESCRIPTION
The script clones the main KFM repository at an immutable source commit, copies the allowlisted
files from docs/wiki/ into the separate Kansas-Frontier-Matrix.wiki.git repository, validates the
staged diff, and defaults to a no-push dry run. Use -Publish for the explicit remote mutation.

The tool is transport only. It does not approve documentation, establish KFM authority, change
repository settings, merge pull requests, release KFM data, or convert the native wiki into a
canonical source.

.EXAMPLE
pwsh -File tools/docs/wiki/sync_kfm_github_wiki.ps1

Runs the full clone, copy, allowlist, and staged-diff validation path without committing or pushing.

.EXAMPLE
pwsh -File tools/docs/wiki/sync_kfm_github_wiki.ps1 -Publish

Commits and pushes the validated page set to the current native-wiki branch, then verifies the
remote commit by readback.
#>

[CmdletBinding()]
param(
    [Parameter()]
    [ValidatePattern("^[0-9a-fA-F]{40}$")]
    [string]$SourceCommit = "3b2c4dc05a2a30ed045e7a04a6d15d103ce83a0d",

    [Parameter()]
    [switch]$Publish,

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$CommitMessage = "docs: synchronize reviewed KFM wiki source",

    [Parameter()]
    [switch]$KeepWorkspace
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$SourceRepo = "https://github.com/bartytime4life/Kansas-Frontier-Matrix.git"
$WikiRepo = "https://github.com/bartytime4life/Kansas-Frontier-Matrix.wiki.git"

$Pages = @(
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
    "_Footer.md"
)

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,

        [Parameter()]
        [string]$WorkingDirectory
    )

    if ([string]::IsNullOrWhiteSpace($WorkingDirectory)) {
        & git @Arguments
    }
    else {
        & git -C $WorkingDirectory @Arguments
    }

    if ($LASTEXITCODE -ne 0) {
        throw "git command failed: git $($Arguments -join ' ')"
    }
}

function Get-GitLines {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,

        [Parameter(Mandatory = $true)]
        [string]$WorkingDirectory
    )

    $Output = @(& git -C $WorkingDirectory @Arguments)
    if ($LASTEXITCODE -ne 0) {
        throw "git command failed: git $($Arguments -join ' ')"
    }

    return @($Output | ForEach-Object { $_.ToString().Trim() } | Where-Object { $_ })
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or is not available on PATH."
}

$WorkRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("kfm-wiki-sync-" + [guid]::NewGuid().ToString("N"))
$SourceDir = Join-Path $WorkRoot "source"
$WikiDir = Join-Path $WorkRoot "wiki"

New-Item -ItemType Directory -Path $WorkRoot -Force | Out-Null

try {
    Write-Host "Cloning the KFM source repository..."
    Invoke-Git -Arguments @("clone", "--no-checkout", "--filter=blob:none", $SourceRepo, $SourceDir)

    Write-Host "Checking out reviewed source commit $SourceCommit..."
    Invoke-Git -WorkingDirectory $SourceDir -Arguments @("checkout", "--detach", $SourceCommit)

    $ResolvedSourceCommit = (Get-GitLines -WorkingDirectory $SourceDir -Arguments @("rev-parse", "HEAD"))[0]
    if ($ResolvedSourceCommit.ToLowerInvariant() -ne $SourceCommit.ToLowerInvariant()) {
        throw "Source checkout mismatch. Requested=$SourceCommit Resolved=$ResolvedSourceCommit"
    }

    Write-Host "Cloning the initialized native GitHub Wiki..."
    Invoke-Git -Arguments @("clone", $WikiRepo, $WikiDir)

    $SourceWikiDir = Join-Path (Join-Path $SourceDir "docs") "wiki"
    if (-not (Test-Path $SourceWikiDir -PathType Container)) {
        throw "Reviewed wiki source directory was not found at $SourceWikiDir."
    }

    foreach ($Page in $Pages) {
        $SourcePath = Join-Path $SourceWikiDir $Page
        $TargetPath = Join-Path $WikiDir $Page

        if (-not (Test-Path $SourcePath -PathType Leaf)) {
            throw "Required source page is missing: $SourcePath"
        }

        Copy-Item -LiteralPath $SourcePath -Destination $TargetPath -Force
    }

    $ChangedPaths = @(
        Get-GitLines -WorkingDirectory $WikiDir -Arguments @("diff", "--name-only")
        Get-GitLines -WorkingDirectory $WikiDir -Arguments @("ls-files", "--others", "--exclude-standard")
    ) | Sort-Object -Unique

    if ($ChangedPaths.Count -eq 0) {
        Write-Host "Outcome: NOOP"
        Write-Host "The native wiki already matches the reviewed source set."
        return
    }

    $UnexpectedPaths = @($ChangedPaths | Where-Object { $Pages -notcontains $_ })
    if ($UnexpectedPaths.Count -gt 0) {
        throw "Unexpected wiki paths changed: $($UnexpectedPaths -join ', ')"
    }

    $AddArguments = @("add", "--") + $Pages
    Invoke-Git -WorkingDirectory $WikiDir -Arguments $AddArguments
    Invoke-Git -WorkingDirectory $WikiDir -Arguments @("diff", "--cached", "--check")

    $StagedPaths = Get-GitLines -WorkingDirectory $WikiDir -Arguments @("diff", "--cached", "--name-only")
    $UnexpectedStagedPaths = @($StagedPaths | Where-Object { $Pages -notcontains $_ })
    if ($UnexpectedStagedPaths.Count -gt 0) {
        throw "Unexpected wiki paths staged: $($UnexpectedStagedPaths -join ', ')"
    }

    Write-Host "Validated staged wiki changes:"
    Invoke-Git -WorkingDirectory $WikiDir -Arguments @("diff", "--cached", "--name-status")
    Invoke-Git -WorkingDirectory $WikiDir -Arguments @("diff", "--cached", "--stat")

    if (-not $Publish) {
        Write-Host ""
        Write-Host "Outcome: PLANNED"
        Write-Host "Dry run completed. No commit or push was performed."
        Write-Host "Re-run with -Publish after reviewing the source commit and staged page list."
        return
    }

    Write-Warning "-Publish performs a public mutation of the separate GitHub Wiki repository."

    # Keep the sync commit attributable without exposing a personal email address.
    Invoke-Git -WorkingDirectory $WikiDir -Arguments @("config", "user.name", "bartytime4life")
    Invoke-Git -WorkingDirectory $WikiDir -Arguments @("config", "user.email", "203533328+bartytime4life@users.noreply.github.com")
    Invoke-Git -WorkingDirectory $WikiDir -Arguments @("commit", "-m", $CommitMessage)

    $WikiBranch = (Get-GitLines -WorkingDirectory $WikiDir -Arguments @("branch", "--show-current"))[0]
    if ([string]::IsNullOrWhiteSpace($WikiBranch)) {
        throw "Unable to determine the native wiki branch."
    }

    Write-Host "Pushing the reviewed page set to the native wiki..."
    Invoke-Git -WorkingDirectory $WikiDir -Arguments @("push", "origin", "HEAD:refs/heads/$WikiBranch")

    $WikiCommit = (Get-GitLines -WorkingDirectory $WikiDir -Arguments @("rev-parse", "HEAD"))[0]
    $RemoteReadback = Get-GitLines -WorkingDirectory $WikiDir -Arguments @("ls-remote", "--heads", "origin", "refs/heads/$WikiBranch")
    if ($RemoteReadback.Count -ne 1) {
        throw "Expected one remote branch readback entry for $WikiBranch; received $($RemoteReadback.Count)."
    }

    $RemoteCommit = ($RemoteReadback[0] -split "\s+")[0]
    if ($RemoteCommit -ne $WikiCommit) {
        throw "Remote readback mismatch. Local=$WikiCommit Remote=$RemoteCommit"
    }

    Write-Host ""
    Write-Host "Outcome: APPLIED"
    Write-Host "KFM native wiki synchronized successfully."
    Write-Host "Source commit: $ResolvedSourceCommit"
    Write-Host "Wiki branch: $WikiBranch"
    Write-Host "Wiki commit: $WikiCommit"
    Write-Host "Open: https://github.com/bartytime4life/Kansas-Frontier-Matrix/wiki"
}
finally {
    if ($KeepWorkspace) {
        Write-Host "Temporary workspace retained at: $WorkRoot"
    }
    elseif (Test-Path $WorkRoot) {
        Remove-Item -LiteralPath $WorkRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
