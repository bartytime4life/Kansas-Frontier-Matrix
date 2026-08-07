<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-docs-wiki-readme
title: tools/docs/wiki — Native GitHub Wiki Synchronization Helper
type: readme; directory-readme; documentation-tooling-contract
version: v0.1.0
status: proposed; review-required; manual-operator-tool; derived-mirror-only
owners: OWNER_TBD — Docs steward · Documentation tooling steward · Repository owner
created: 2026-08-07
updated: 2026-08-07
policy_label: public-documentation-tooling; explicit-remote-write; dry-run-first
current_path: tools/docs/wiki/README.md
owning_root: tools/
responsibility: provide a bounded operator tool that mirrors reviewed docs/wiki pages into the separate native GitHub Wiki repository
truth_posture: cite-or-abstain; the tool transports reviewed bytes but does not approve content, create doctrine, establish release authority, or make the native wiki canonical
related:
  - ../README.md
  - ../../../docs/wiki/README.md
  - ../../../docs/wiki/Wiki-Maintenance.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../SECURITY.md
  - ../../../data/receipts/generated/README.md
notes:
  - "The native GitHub Wiki is a derived public orientation mirror, not a KFM authority root."
  - "Default execution is a dry run; remote mutation requires the explicit -Publish switch."
  - "The helper never force-pushes, deletes native-wiki pages, changes repository settings, or writes to the main KFM repository."
[/KFM_META_BLOCK_V2] -->

# `tools/docs/wiki/` — Native GitHub Wiki synchronization helper

> Manual, dry-run-first transport for copying the reviewed `docs/wiki/` page set into the separate `Kansas-Frontier-Matrix.wiki.git` repository.

## Authority boundary

This lane owns **documentation synchronization tooling**, not documentation authority. The controlling sources remain the reviewed files under `docs/wiki/` and the canonical repository materials they cite. The native GitHub Wiki is a derived public orientation mirror.

The helper may transport reviewed bytes after an authorized operator selects `-Publish`. It does not:

- approve or review wiki content;
- adopt doctrine, contracts, schemas, policy, evidence, or release decisions;
- change the KFM default branch or repository settings;
- merge a pull request;
- activate a live source or publish KFM lifecycle data;
- delete native-wiki pages;
- force-push or rewrite shared history;
- store credentials or tokens.

## Tool

[`sync_kfm_github_wiki.ps1`](sync_kfm_github_wiki.ps1) performs this bounded flow:

```text
immutable KFM source commit
  -> allowlisted docs/wiki pages
  -> temporary clone of the native wiki
  -> staged path and whitespace validation
  -> dry-run plan by default
  -> explicit -Publish commit and push
  -> remote commit readback
```

The default source revision is the reviewed wiki-foundation merge:

```text
3b2c4dc05a2a30ed045e7a04a6d15d103ce83a0d
```

Change that input only to another immutable commit whose `docs/wiki/` source set has completed the intended repository review.

## Requirements

- Git available on `PATH`.
- PowerShell 5.1 or PowerShell 7 (`pwsh`).
- The native GitHub Wiki initialized with at least one page.
- Git credentials authorized to push to `bartytime4life/Kansas-Frontier-Matrix.wiki.git`.
- No expectation that script execution supplies content approval or publication authority.

## Safe execution

Run the full preparation and validation path without committing or pushing:

```powershell
pwsh -File tools/docs/wiki/sync_kfm_github_wiki.ps1
```

After reviewing the immutable source commit and staged page list, perform the explicit remote synchronization:

```powershell
pwsh -File tools/docs/wiki/sync_kfm_github_wiki.ps1 -Publish
```

Use a different reviewed source commit only when deliberate:

```powershell
pwsh -File tools/docs/wiki/sync_kfm_github_wiki.ps1 `
  -SourceCommit <40-character-commit-sha> `
  -Publish
```

`-KeepWorkspace` retains the temporary clones for troubleshooting. Without it, the temporary directory is removed in `finally` after success or failure.

## Page allowlist

The helper synchronizes exactly these native-wiki pages:

- `Home.md`
- `Getting-Started.md`
- `Project-Status.md`
- `Architecture.md`
- `Repository-Map.md`
- `Governance-and-Evidence.md`
- `Data-Lifecycle.md`
- `Domains.md`
- `Map-UI-and-AI.md`
- `Security-and-Sensitivity.md`
- `Development-and-Validation.md`
- `Contributing.md`
- `Glossary.md`
- `Wiki-Maintenance.md`
- `_Sidebar.md`
- `_Footer.md`

`docs/wiki/README.md` is intentionally excluded because it governs the source packet rather than serving as a native-wiki reader page.

## Safety and finite outcomes

| Outcome | Meaning |
|---|---|
| `NOOP` | The allowlisted native pages already match the selected source commit. |
| `PLANNED` | Staged diff validated; no commit or push occurred. |
| `APPLIED` | Commit pushed and the remote wiki branch read back at the same commit. |
| PowerShell error | Preconditions, clone, allowlist, staging, commit, push, or readback failed; no failure is converted into success. |

The helper verifies that no path outside the allowlist changed, runs `git diff --cached --check`, pushes without force, and verifies the resulting remote branch SHA.

## Validation boundary

Repository checks can verify the committed source, explicit publish gate, page allowlist, no-force posture, and remote-readback logic. They do not prove that:

- PowerShell is installed on every operator machine;
- Git credentials are valid;
- GitHub is available;
- the native wiki was synchronized in a particular run;
- the synchronized content is correct merely because transport succeeded.

A real publish run should retain the source commit, resulting wiki commit, operator, timestamp, and review reference in the relevant maintenance record or pull request.

## Correction and rollback

Before native-wiki synchronization, correct `docs/wiki/` through the normal repository review path. After an incorrect synchronization:

1. stop additional sync attempts;
2. identify the source and native-wiki commits;
3. revert the native-wiki commit or commit a corrected reviewed source set;
4. read back every affected page and link;
5. backport any emergency native-wiki correction into `docs/wiki/`;
6. follow `SECURITY.md` immediately if restricted or sensitive content was exposed.

Do not rewrite shared history merely to make the wiki appear clean.
